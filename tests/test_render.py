import unittest

from helpers import categorias_validas, diretriz_valida
from vygolint_catalog.render import render_markdown


class RenderMarkdownTest(unittest.TestCase):
    def setUp(self):
        self.cats = categorias_validas()

    def test_header_marks_generated_file(self):
        out = render_markdown([diretriz_valida()], self.cats)
        self.assertTrue(out.startswith("<!-- ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão. -->"))

    def test_summary_table_row(self):
        out = render_markdown([diretriz_valida()], self.cats)
        self.assertIn("| D17 | Mediação | O jogo deve exibir feedback construtivo para as ações do jogador | D17.1 (A) |", out)

    def test_detail_section_contains_all_blocks(self):
        out = render_markdown([diretriz_valida()], self.cats)
        for trecho in (
            "### D17 — O jogo deve exibir feedback construtivo para as ações do jogador",
            "#### D17.1 — Nível A",
            "**Enunciado.** Toda ação incorreta",
            "essencialidade alta, viabilidade alta",
            "- Código: Localizar tratadores de erro",
            "- Documentação: não se aplica",
            "- Vídeo: Registrar timestamp",
            "Indicadores: ao menos 3 ocorrências de erro; cada ocorrência mostra orientação",
            "- Atendido: Todas as ocorrências",
            "- Parcial: Algumas ocorrências",
            "- Não atendido: Feedback só sinaliza",
            "**Depende de.** —",
        ):
            with self.subTest(trecho=trecho):
                self.assertIn(trecho, out)

    def test_depende_de_rendering(self):
        d = diretriz_valida()
        d["criterios"][0]["depende_de"] = [["D06.1", "D07.1"], ["D09.1"]]
        out = render_markdown([d], self.cats)
        self.assertIn("**Depende de.** (D06.1 ou D07.1) e (D09.1)", out)

    def test_aplicabilidade_and_modalidade(self):
        d = diretriz_valida()
        d["modalidade"] = "pode"
        d["aplicabilidade"] = "Somente quando aplicado em sala de aula"
        d["criterios"][0]["nivel"] = "AA"
        out = render_markdown([d], self.cats)
        self.assertIn("- Modalidade: pode", out)
        self.assertIn("- Aplicabilidade: Somente quando aplicado em sala de aula", out)

    def test_sorted_by_id_and_deterministic(self):
        a = diretriz_valida()
        b = diretriz_valida()
        b["id"] = "D06"
        b["categoria"] = "interacao"
        b["criterios"][0]["id"] = "D06.1"
        out1 = render_markdown([a, b], self.cats)
        out2 = render_markdown([b, a], self.cats)
        self.assertEqual(out1, out2)
        self.assertLess(out1.index("| D06 |"), out1.index("| D17 |"))

    def test_ressalva_present(self):
        out = render_markdown([diretriz_valida()], self.cats)
        self.assertIn("suprimiu as categorias", out)
