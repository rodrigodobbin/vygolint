import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from helpers import REPO, catalogo_real
from vygolint_catalog.report import validate_avaliacao
from vygolint_catalog.scaffold import PLACEHOLDER, render_scaffold


class RenderScaffoldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cat = catalogo_real()

    def _render(self, **kw):
        base = dict(
            jogo="Jogo: de \"teste\"", sala_de_aula=False, fontes=["video"],
            artefatos={"video": ["gameplay/s.mp4"]}, avaliador="teste", data="2026-11-05",
        )
        base.update(kw)
        return render_scaffold(self.cat, **base)

    def test_is_valid_avaliacao_with_every_criterion(self):
        av = yaml.safe_load(self._render())
        self.assertEqual(validate_avaliacao(av, self.cat), [])
        self.assertEqual(list(av["criterios"]), sorted(self.cat["criterios"]))
        self.assertEqual(av["jogo"], "Jogo: de \"teste\"")
        self.assertEqual(av["contexto"], {"sala_de_aula": False, "fontes": ["video"], "artefatos": {"video": ["gameplay/s.mp4"]}})
        self.assertEqual(av["data"], "2026-11-05")

    def test_d22_out_of_context_only_without_classroom(self):
        av = yaml.safe_load(self._render())
        for cid, item in self.cat["criterios"].items():
            esperado = "fora_do_contexto" if item["diretriz"].get("aplicabilidade") else "nao_avaliado"
            self.assertEqual(av["criterios"][cid]["grau"], esperado, cid)
        av = yaml.safe_load(self._render(sala_de_aula=True, fontes=["documentacao"], artefatos={"documentacao": ["gdd.md"]}))
        self.assertEqual(validate_avaliacao(av, self.cat), [])
        self.assertTrue(all(e["grau"] == "nao_avaliado" for e in av["criterios"].values()))

    def test_placeholder_only_where_a_source_can_decide(self):
        av = yaml.safe_load(self._render())
        for cid, item in self.cat["criterios"].items():
            e = av["criterios"][cid]
            if e["grau"] == "fora_do_contexto":
                self.assertNotIn(PLACEHOLDER, e["razao"])
            elif item["criterio"]["evidencia"].get("video") is None:
                self.assertNotIn(PLACEHOLDER, e["razao"], cid)
                self.assertIn("video", e["razao"])
            else:
                self.assertEqual(e["razao"], PLACEHOLDER, cid)

    def test_comments_carry_statement_and_sources(self):
        texto = self._render(fontes=["codigo", "video"], artefatos={"codigo": ["src"], "video": ["g.mp4"]})
        c = self.cat["criterios"]["D17.1"]["criterio"]
        self.assertIn(f"# D17.1 ({c['nivel']}) — {c['enunciado']}", texto)
        self.assertIn("# fontes deste contexto que o critério aceita: codigo, video", texto)
        self.assertTrue(texto.startswith("# "))


class ScaffoldCliTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.cmd = [
            sys.executable, str(REPO / "scripts" / "vygolint_scaffold.py"), "--jogo", "Jogo X",
            "--sala-de-aula", "false", "--fontes", "video,codigo",
            "--artefato", "video=gameplay/a.mp4", "--artefato", "video=gameplay/b.mp4", "--artefato", "codigo=src",
            "--out", str(self.tmp / "vygolint-out"),
        ]

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp)

    def test_writes_file_and_refuses_overwrite(self):
        ok = subprocess.run(self.cmd, capture_output=True, text=True)
        self.assertEqual(ok.returncode, 0, ok.stderr)
        alvo = self.tmp / "vygolint-out" / "avaliacao.yaml"
        av = yaml.safe_load(alvo.read_text(encoding="utf-8"))
        self.assertEqual(av["contexto"]["fontes"], ["codigo", "video"])
        self.assertEqual(av["contexto"]["artefatos"], {"codigo": ["src"], "video": ["gameplay/a.mp4", "gameplay/b.mp4"]})
        self.assertEqual(validate_avaliacao(av, catalogo_real()), [])
        alvo.write_text("preenchido", encoding="utf-8")
        again = subprocess.run(self.cmd, capture_output=True, text=True)
        self.assertEqual(again.returncode, 1)
        self.assertIn("--force", again.stderr)
        self.assertEqual(alvo.read_text(encoding="utf-8"), "preenchido")
        forced = subprocess.run(self.cmd + ["--force"], capture_output=True, text=True)
        self.assertEqual(forced.returncode, 0, forced.stderr)
        self.assertNotEqual(alvo.read_text(encoding="utf-8"), "preenchido")

    def test_rejects_bad_arguments(self):
        casos = (
            (["--fontes", "video,audio"], "audio"),
            (["--artefato", "documentacao=gdd.md"], "documentacao"),
            (["--artefato", "sem-igual"], "fonte=caminho"),
        )
        for extra, trecho in casos:
            with self.subTest(extra=extra):
                r = subprocess.run(self.cmd + extra, capture_output=True, text=True)
                self.assertNotEqual(r.returncode, 0)
                self.assertIn(trecho, r.stderr)
        r = subprocess.run(
            [sys.executable, str(REPO / "scripts" / "vygolint_scaffold.py"), "--jogo", "J", "--sala-de-aula", "true",
             "--fontes", "video,codigo", "--artefato", "video=a.mp4", "--out", str(self.tmp / "o")],
            capture_output=True, text=True,
        )
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("codigo", r.stderr)


class ScaffoldEscopoTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        for rel in ("gameplay/s1.mp4", "gameplay/s2.mp4", "docs/gdd.md"):
            p = self.tmp / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("x", encoding="utf-8")
        self.base = [
            sys.executable, str(REPO / "scripts" / "vygolint_scaffold.py"), "--jogo", "J", "--sala-de-aula", "false",
            "--out", "vygolint-out",
        ]

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp)

    def _run(self, *extra):
        return subprocess.run(self.base + list(extra), capture_output=True, text=True, cwd=self.tmp)

    def test_folder_artefact_lists_its_files_as_comments(self):
        r = self._run("--fontes", "video,documentacao", "--artefato", "video=gameplay", "--artefato", "documentacao=docs")
        self.assertEqual(r.returncode, 0, r.stderr)
        texto = (self.tmp / "vygolint-out" / "avaliacao.yaml").read_text(encoding="utf-8")
        for linha in ("    #   gameplay/s1.mp4", "    #   gameplay/s2.mp4", "    #   docs/gdd.md"):
            self.assertIn(linha, texto)
        av = yaml.safe_load(texto)
        self.assertEqual(av["contexto"]["artefatos"], {"documentacao": ["docs"], "video": ["gameplay"]})
        self.assertNotIn("fontes_externas", av["contexto"])
        self.assertEqual(validate_avaliacao(av, catalogo_real()), [])

    def test_missing_artefact_warns_but_writes(self):
        r = self._run("--fontes", "video", "--artefato", "video=sumiu")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("sumiu", r.stderr)

    def test_external_source_replaces_the_artefact(self):
        r = self._run("--fontes", "video,codigo", "--artefato", "video=gameplay",
                      "--externa", "codigo=repositório github.com/x/y, sem cópia local")
        self.assertEqual(r.returncode, 0, r.stderr)
        av = yaml.safe_load((self.tmp / "vygolint-out" / "avaliacao.yaml").read_text(encoding="utf-8"))
        self.assertEqual(av["contexto"]["artefatos"], {"video": ["gameplay"]})
        self.assertEqual(av["contexto"]["fontes_externas"], {"codigo": ["repositório github.com/x/y, sem cópia local"]})
        self.assertEqual(validate_avaliacao(av, catalogo_real()), [])
        r = self._run("--fontes", "video", "--artefato", "video=gameplay", "--externa", "codigo=x", "--force")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("codigo", r.stderr)
