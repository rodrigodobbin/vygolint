import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from helpers import REPO
from vygolint_catalog.diff import comparar, render_diff


def _resultado(nivel="sem_conformidade", **criterios):
    doc = {"jogo": "J", "data": "2026-11-04", "avaliador": "teste", "nivel": nivel, "criterios": {}}
    for cid, spec in criterios.items():
        grau, nota = (spec, None) if isinstance(spec, str) else spec
        doc["criterios"][cid] = {"nivel": "A", "grau": grau, "grau_declarado": grau, "nota": nota}
    return doc


class CompararTest(unittest.TestCase):
    def test_same_results_have_no_changes(self):
        a = _resultado(**{"D01.1": "atendido", "D02.1": "nao_atendido"})
        d = comparar(a, a)
        self.assertEqual(d["mudancas"], [])
        self.assertEqual(d["nivel"], ("sem_conformidade", "sem_conformidade"))
        self.assertEqual(d["so_antes"], [])
        self.assertEqual(d["so_depois"], [])

    def test_changes_are_classified_by_direction(self):
        antes = _resultado(**{
            "D01.1": "nao_atendido",   # melhora
            "D02.1": "atendido",       # piora
            "D03.1": "nao_avaliado",   # passou a ser avaliado
            "D04.1": "parcial",        # deixou de ser avaliado
            "D05.1": "fora_do_contexto",  # entrou no contexto
            "D06.1": "parcial",        # igual
        })
        depois = _resultado(nivel="A", **{
            "D01.1": "atendido",
            "D02.1": "parcial",
            "D03.1": "nao_atendido",
            "D04.1": "nao_avaliado",
            "D05.1": "atendido",
            "D06.1": "parcial",
        })
        d = comparar(antes, depois)
        tipos = {m["id"]: m["tipo"] for m in d["mudancas"]}
        self.assertEqual(tipos, {
            "D01.1": "melhora",
            "D02.1": "piora",
            "D03.1": "passou_a_ser_avaliado",
            "D04.1": "deixou_de_ser_avaliado",
            "D05.1": "entrou_no_contexto",
        })
        self.assertEqual(d["nivel"], ("sem_conformidade", "A"))
        self.assertEqual(d["contagem"]["antes"]["parcial"], 2)
        self.assertEqual(d["contagem"]["depois"]["atendido"], 2)
        self.assertEqual([m["id"] for m in d["mudancas"]], ["D01.1", "D02.1", "D03.1", "D04.1", "D05.1"])

    def test_leaving_the_context_is_its_own_type(self):
        d = comparar(_resultado(**{"D22.1": "atendido"}), _resultado(**{"D22.1": "fora_do_contexto"}))
        self.assertEqual(d["mudancas"][0]["tipo"], "saiu_do_contexto")

    def test_note_changes_are_reported_even_with_the_same_grade(self):
        antes = _resultado(**{"D13.1": ("nao_avaliado", "não avaliado por dependência (D06.1)")})
        depois = _resultado(**{"D13.1": ("nao_avaliado", None)})
        d = comparar(antes, depois)
        self.assertEqual(d["mudancas"], [])
        self.assertEqual([n["id"] for n in d["notas"]], ["D13.1"])
        self.assertEqual(d["notas"][0]["antes"], "não avaliado por dependência (D06.1)")
        self.assertIsNone(d["notas"][0]["depois"])

    def test_declared_grade_overridden_by_the_script_is_flagged(self):
        depois = _resultado(**{"D40.1": "nao_atendido"})
        depois["criterios"]["D40.1"]["grau_declarado"] = "atendido"
        d = comparar(_resultado(**{"D40.1": "nao_atendido"}), depois)
        self.assertEqual(d["mudancas"], [])
        self.assertEqual(d["sobrescritos"]["depois"], [("D40.1", "atendido", "nao_atendido")])
        self.assertEqual(d["sobrescritos"]["antes"], [])

    def test_criteria_present_in_only_one_file_are_listed_apart(self):
        d = comparar(_resultado(**{"D01.1": "atendido", "D99.1": "atendido"}), _resultado(**{"D01.1": "atendido", "D98.1": "parcial"}))
        self.assertEqual(d["so_antes"], ["D99.1"])
        self.assertEqual(d["so_depois"], ["D98.1"])
        self.assertEqual(d["mudancas"], [])

    def test_different_games_raise_a_warning(self):
        b = _resultado()
        b["jogo"] = "Outro"
        d = comparar(_resultado(), b)
        self.assertTrue(any("jogo" in a for a in d["avisos"]))
        self.assertEqual(comparar(_resultado(), _resultado())["avisos"], [])

    def test_missing_fields_do_not_break_the_comparison(self):
        d = comparar({"criterios": {"D01.1": {"grau": "atendido"}}}, {"criterios": {"D01.1": {"grau": "parcial"}}})
        self.assertEqual(d["nivel"], (None, None))
        self.assertEqual(d["mudancas"][0]["tipo"], "piora")


class RenderTest(unittest.TestCase):
    def test_render_lists_header_changes_and_criteria(self):
        antes = _resultado(**{"D01.1": "nao_atendido", "D02.1": "atendido", "D03.1": ("nao_avaliado", "sem vídeo")})
        depois = _resultado(nivel="A", **{"D01.1": "atendido", "D02.1": "atendido", "D03.1": ("nao_avaliado", None)})
        depois["data"] = "2026-11-06"
        texto = render_diff(comparar(antes, depois))
        self.assertIn("sem_conformidade", texto)
        self.assertIn("→ A", texto)
        self.assertIn("2026-11-04", texto)
        self.assertIn("2026-11-06", texto)
        self.assertIn("D01.1", texto)
        self.assertIn("nao_atendido → atendido", texto)
        self.assertNotIn("| D02.1", texto)
        self.assertIn("D03.1", texto)
        self.assertIn("sem vídeo", texto)
        self.assertIn("não classifica o jogo como sociointeracionista", texto)

    def test_render_without_changes_says_so(self):
        texto = render_diff(comparar(_resultado(**{"D01.1": "atendido"}), _resultado(**{"D01.1": "atendido"})))
        self.assertIn("Nenhum critério mudou de grau", texto)


class CliTest(unittest.TestCase):
    def _run(self, *args):
        return subprocess.run(
            [sys.executable, str(REPO / "scripts" / "vygolint_diff.py"), *args],
            capture_output=True, text=True, encoding="utf-8",
        )

    def test_cli_prints_the_diff_and_can_write_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / "a.yaml"
            b = Path(tmp) / "b.yaml"
            out = Path(tmp) / "diff.md"
            a.write_text(yaml.safe_dump(_resultado(**{"D01.1": "nao_atendido"}), allow_unicode=True), encoding="utf-8")
            b.write_text(yaml.safe_dump(_resultado(**{"D01.1": "atendido"}), allow_unicode=True), encoding="utf-8")
            r = self._run(str(a), str(b), "--out", str(out))
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("1 melhora", r.stdout)
            self.assertIn("nao_atendido → atendido", out.read_text(encoding="utf-8"))

    def test_cli_rejects_a_file_that_is_not_a_resultado(self):
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / "a.yaml"
            b = Path(tmp) / "b.yaml"
            a.write_text("jogo: J\n", encoding="utf-8")
            b.write_text(yaml.safe_dump(_resultado(**{"D01.1": "atendido"})), encoding="utf-8")
            r = self._run(str(a), str(b))
            self.assertEqual(r.returncode, 1)
            self.assertIn("criterios", r.stderr)
            r = self._run(str(Path(tmp) / "nao_existe.yaml"), str(b))
            self.assertEqual(r.returncode, 1)


if __name__ == "__main__":
    unittest.main()
