import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from helpers import REPO, catalogo_real
from vygolint_catalog.merge import ids_por_categoria, injetar, ler_partes
from vygolint_catalog.report import validate_avaliacao
from vygolint_catalog.scaffold import render_scaffold

PROVA = "gameplay/s.mp4 00:00:01 — x"


def _entrada(grau="atendido"):
    return {"grau": grau, "fontes": {"video": {"grau": grau, "provas": [PROVA], "observacao": "texto: com dois-pontos"}}}


class MergeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cat = catalogo_real()
        cls.esqueleto = render_scaffold(
            cls.cat, jogo="J", sala_de_aula=False, fontes=["video"], artefatos={"video": ["gameplay/s.mp4"]},
            avaliador="teste", data="2026-11-06",
        )

    def test_categories_cover_the_catalog(self):
        por = ids_por_categoria(self.cat)
        self.assertEqual(sorted(c for ids in por.values() for c in ids), sorted(self.cat["criterios"]))
        self.assertEqual(sorted(por), sorted(c["chave"] for c in self.cat["categorias"]["categorias"]))

    def test_entries_replace_the_scaffold_blocks_and_keep_comments(self):
        entradas = {"D17.1": _entrada("parcial"), "D40.1": {"grau": "nao_avaliado", "razao": "sem fonte"}}
        texto, fora = injetar(self.esqueleto, entradas)
        self.assertEqual(fora, [])
        av = yaml.safe_load(texto)
        self.assertEqual(av["criterios"]["D17.1"], entradas["D17.1"])
        self.assertEqual(av["criterios"]["D40.1"], entradas["D40.1"])
        self.assertEqual(av["criterios"]["D18.1"]["razao"], "PREENCHER")
        self.assertEqual(list(av["criterios"]), sorted(self.cat["criterios"]))
        self.assertEqual(validate_avaliacao(av, self.cat), [])
        c = self.cat["criterios"]["D17.1"]["criterio"]
        self.assertIn(f"  # D17.1 ({c['nivel']}) — {c['enunciado']}\n", texto)
        self.assertEqual(texto.count("  D17.1:"), 1)
        # merging again with another grade replaces the multi-line block, it does not append
        de_novo, _ = injetar(texto, {"D17.1": _entrada("atendido")})
        self.assertEqual(yaml.safe_load(de_novo)["criterios"]["D17.1"]["grau"], "atendido")
        self.assertEqual(de_novo.count("  D17.1:"), 1)
        self.assertEqual(de_novo.count(PROVA), 1)

    def test_id_missing_from_the_file_is_reported(self):
        sem = "\n".join(l for l in self.esqueleto.split("\n") if "D17.1" not in l)
        _, fora = injetar(sem, {"D17.1": _entrada()})
        self.assertEqual(fora, ["D17.1"])

    def test_parts_are_checked_against_the_catalog(self):
        dump = lambda d: yaml.safe_dump(d, allow_unicode=True)
        entradas, erros, notas = ler_partes({
            "linguagem": dump({"D38.1": _entrada()}),
            "mediacao": dump({"criterios": {"D17.1": _entrada(), "D36.1": _entrada()}}),
            "resto": dump({"D01.1": _entrada()}),
        }, self.cat)
        self.assertEqual(erros, [])
        self.assertEqual(sorted(entradas), ["D01.1", "D17.1", "D36.1", "D38.1"])
        self.assertTrue(any(n.startswith("mediacao: entradas vieram dentro de `criterios:`") for n in notas))
        self.assertTrue(any(n.startswith("mediacao: faltam critérios da categoria") and "D18.1" in n for n in notas))
        self.assertTrue(any(n == "mediacao: traz critérios de outra categoria: D36.1" for n in notas))
        self.assertFalse(any(n.startswith("linguagem") or n.startswith("resto") for n in notas))

    def test_bad_parts_are_errors(self):
        dump = lambda d: yaml.safe_dump(d, allow_unicode=True)
        _, erros, _ = ler_partes({
            "a": dump({"D17.1": _entrada(), "D99.1": _entrada(), "D18.1": "texto"}),
            "b": dump({"D17.1": _entrada()}),
            "c": "D01.1: [",
            "d": dump(["lista"]),
        }, self.cat)
        self.assertEqual(len(erros), 5)
        for trecho in ("a: D99.1: critério inexistente", "a: D18.1: entrada deve ser mapa", "b: D17.1: já veio em a",
                       "c: YAML inválido", "d: o topo deve ser um mapa"):
            self.assertTrue(any(trecho in e for e in erros), trecho)


class JuntarCliTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        r = subprocess.run(
            [sys.executable, str(REPO / "scripts" / "vygolint_scaffold.py"), "--jogo", "J", "--sala-de-aula", "false",
             "--fontes", "video", "--artefato", "video=gameplay/s.mp4", "--out", str(self.tmp / "o")],
            capture_output=True, text=True, cwd=self.tmp,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.alvo = self.tmp / "o" / "avaliacao.yaml"
        self.cmd = [sys.executable, str(REPO / "scripts" / "vygolint_juntar.py"), str(self.alvo)]

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp)

    def _parte(self, nome, doc):
        pasta = self.tmp / "o" / "partes"
        pasta.mkdir(exist_ok=True)
        (pasta / f"{nome}.yaml").write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False), encoding="utf-8")

    def test_merges_parts_and_reports_what_is_left(self):
        self._parte("linguagem", {"D38.1": _entrada()})
        self._parte("aprendizado", {"D40.1": _entrada("parcial")})
        r = subprocess.run(self.cmd, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("2 entrada(s) de 2 parte(s)", r.stdout)
        self.assertIn("41 critério(s) sem parte", r.stdout)
        self.assertIn("PREENCHER", r.stdout)
        av = yaml.safe_load(self.alvo.read_text(encoding="utf-8"))
        self.assertEqual(av["criterios"]["D38.1"]["grau"], "atendido")
        self.assertEqual(av["criterios"]["D40.1"]["grau"], "parcial")
        self.assertEqual(validate_avaliacao(av, catalogo_real()), [])

    def test_errors_leave_the_file_untouched(self):
        antes = self.alvo.read_text(encoding="utf-8")
        self._parte("linguagem", {"D38.1": _entrada()})
        self._parte("outra", {"D38.1": _entrada(), "D99.9": _entrada()})
        r = subprocess.run(self.cmd, capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertIn("já veio em linguagem", r.stderr)
        self.assertIn("D99.9", r.stderr)
        self.assertIn("não foi alterado", r.stderr)
        self.assertEqual(self.alvo.read_text(encoding="utf-8"), antes)

    def test_no_parts_or_no_file(self):
        r = subprocess.run(self.cmd, capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertIn("nenhuma parte", r.stderr)
        r = subprocess.run([sys.executable, str(REPO / "scripts" / "vygolint_juntar.py"), str(self.tmp / "nao.yaml")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertIn("vygolint_scaffold.py", r.stderr)
