import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from helpers import REPO, catalogo_real
from vygolint_catalog.scaffold import PLACEHOLDER, render_inventario, render_scaffold
from vygolint_catalog.status import render_status, status_avaliacao

PROVA = "gameplay/s.mp4 00:00:01 — x"


def _entrada(grau="atendido"):
    return {"grau": grau, "fontes": {"video": {"grau": grau, "provas": [PROVA]}}}


class StatusTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cat = catalogo_real()
        cls.esqueleto = render_scaffold(
            cls.cat, jogo="J", sala_de_aula=False, fontes=["video"], artefatos={"video": ["gameplay/s.mp4"]},
            avaliador="teste", data="2026-11-09",
        )

    def _av(self, **entradas):
        av = yaml.safe_load(self.esqueleto)
        for cid, e in entradas.items():
            av["criterios"][cid] = e
        return av

    def test_fresh_scaffold_counts_only_the_prefilled_entries_as_done(self):
        s = status_avaliacao(self._av(), self.cat)
        self.assertEqual(s["total"], 43)
        # D22.1 and D22.2 come as fora_do_contexto with a reason; D06.1-like entries whose criterion accepts no
        # source of the context also come with a written reason. Everything with PREENCHER is pending.
        self.assertEqual(s["preenchidos"] + s["pendentes"], 43)
        self.assertIn("D22.1", s["ids_preenchidos"])
        self.assertIn("D01.1", s["ids_pendentes"])
        self.assertEqual(s["proximo"], "D01.1")
        self.assertEqual(s["proximo_categoria"], "interacao")

    def test_graded_entries_and_written_reasons_count_as_done(self):
        av = self._av(**{
            "D01.1": _entrada(),
            "D02.1": {"grau": "nao_avaliado", "razao": "o vídeo não mostra o início de nenhuma missão"},
        })
        s = status_avaliacao(av, self.cat)
        self.assertIn("D01.1", s["ids_preenchidos"])
        self.assertIn("D02.1", s["ids_preenchidos"])
        self.assertEqual(s["proximo"], "D03.1")
        base = status_avaliacao(self._av(), self.cat)["por_categoria"]["interacao"]["preenchidos"]
        self.assertEqual(s["por_categoria"]["interacao"]["preenchidos"], base + 2)
        self.assertEqual(s["por_categoria"]["interacao"]["total"], 17)

    def test_missing_entries_are_pending(self):
        av = self._av()
        del av["criterios"]["D01.1"]
        s = status_avaliacao(av, self.cat)
        self.assertIn("D01.1", s["ids_pendentes"])
        self.assertIn("D01.1", s["sem_entrada"])
        self.assertEqual(s["proximo"], "D01.1")

    def test_everything_done_has_no_next(self):
        av = self._av(**{cid: _entrada() for cid in self.cat["criterios"] if cid not in ("D22.1", "D22.2")})
        s = status_avaliacao(av, self.cat)
        self.assertEqual(s["pendentes"], 0)
        self.assertIsNone(s["proximo"])

    def test_header_and_inventory_placeholders_are_counted(self):
        av = self._av()
        av["avaliador"] = PLACEHOLDER
        inv = render_inventario("J", ["video"], {"video": ["gameplay/s.mp4"]})
        s = status_avaliacao(av, self.cat, inventario=inv)
        self.assertEqual(s["cabecalho_pendente"], ["avaliador"])
        self.assertGreater(s["inventario_pendente"], 0)
        self.assertIsNone(status_avaliacao(av, self.cat)["inventario_pendente"])

    def test_render_lists_counts_next_and_categories(self):
        av = self._av(**{"D01.1": _entrada()})
        texto = render_status(status_avaliacao(av, self.cat, inventario="x PREENCHER y"))
        self.assertIn("de 43 critérios preenchidos", texto)
        self.assertIn("Próximo: D02.1 (interacao)", texto)
        self.assertIn("interacao", texto)
        self.assertIn("inventario.md: 1 PREENCHER", texto)
        texto = render_status(status_avaliacao(self._av(**{cid: _entrada() for cid in self.cat["criterios"]}), self.cat))
        self.assertIn("nenhum critério pendente", texto)


class CliTest(unittest.TestCase):
    def _run(self, *args):
        return subprocess.run(
            [sys.executable, str(REPO / "scripts" / "vygolint_report.py"), *args],
            capture_output=True, text=True, encoding="utf-8",
        )

    def test_status_reads_a_scaffold_without_validating_or_writing(self):
        cat = catalogo_real()
        with tempfile.TemporaryDirectory() as tmp:
            pasta = Path(tmp)
            (pasta / "avaliacao.yaml").write_text(render_scaffold(
                cat, jogo="J", sala_de_aula=False, fontes=["video"], artefatos={"video": ["gameplay/s.mp4"]},
                avaliador=PLACEHOLDER, data="2026-11-09",
            ), encoding="utf-8")
            (pasta / "inventario.md").write_text(render_inventario("J", ["video"], {"video": ["gameplay/s.mp4"]}), encoding="utf-8")
            r = self._run(str(pasta / "avaliacao.yaml"), "--status")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("de 43 critérios preenchidos", r.stdout)
            self.assertIn("Próximo: D01.1", r.stdout)
            self.assertIn("avaliador", r.stdout)
            self.assertIn("inventario.md", r.stdout)
            self.assertFalse((pasta / "relatorio.md").exists())

    def test_status_reports_invalid_yaml(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "avaliacao.yaml"
            p.write_text("criterios: [\n", encoding="utf-8")
            r = self._run(str(p), "--status")
            self.assertEqual(r.returncode, 1)
            self.assertIn("YAML inválido", r.stderr)


if __name__ == "__main__":
    unittest.main()
