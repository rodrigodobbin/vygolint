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
            "- Vídeo: Registrar timestamp de cada erro e classificar o feedback\n  - ao menos 3 ocorrências de erro\n  - cada ocorrência mostra orientação",
            "- Atendido: Todas as ocorrências",
            "- Parcial: Algumas ocorrências",
            "- Não atendido: Feedback só sinaliza",
            "**Depende de.** —",
        ):
            with self.subTest(trecho=trecho):
                self.assertIn(trecho, out)

    def test_definicoes_block_before_enunciado(self):
        from helpers import REPO
        from vygolint_catalog.validate import load_definicoes
        g = load_definicoes(REPO / "catalog" / "definicoes.yaml")
        d = diretriz_valida()
        c = d["criterios"][0]
        c["definicoes"] = {
            "glossario": ["missao"],
            "locais": {"dispositivo": "um elemento presente na abertura"},
            "termos_comuns": {"cenário": "sentido corrente"},
        }
        out = render_markdown([d], self.cats, g)
        bloco = (
            "**Definições.**\n\n"
            "- *missão*: " + g["missao"]["texto"] + "\n"
            "- *dispositivo*: um elemento presente na abertura\n"
            "- *cenário* (sentido corrente): sentido corrente\n\n"
            "**Enunciado.**"
        )
        self.assertIn(bloco, out)
        self.assertLess(out.index("**Definições.**"), out.index("**Enunciado.**"))

    def test_no_definicoes_block_when_absent(self):
        out = render_markdown([diretriz_valida()], self.cats, {})
        self.assertNotIn("**Definições.**", out)

    def test_glossary_section(self):
        from helpers import REPO
        from vygolint_catalog.validate import load_definicoes
        g = load_definicoes(REPO / "catalog" / "definicoes.yaml")
        out = render_markdown([diretriz_valida()], self.cats, g)
        self.assertIn("## Glossário", out)
        self.assertIn("- **missão** (âncora D28; gatilhos: missão, missões): " + g["missao"]["texto"], out)
        self.assertLess(out.index("## Glossário"), out.index("## Resumo"))
        self.assertNotIn("## Glossário", render_markdown([diretriz_valida()], self.cats))

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

    def test_recomendacoes_block_between_escala_and_depende_de(self):
        out = render_markdown([diretriz_valida()], self.cats)
        bloco = (
            "- Não atendido: Feedback só sinaliza acerto/erro ou inexiste\n\n"
            "**Recomendações.**\n"
            "- Documentação: Registrar no documento de design a tabela de erros com a mensagem exibida em cada um e a próxima ação que ela indica\n"
            "- Design: Definir, para cada ação incorreta prevista, a próxima ação que a mensagem indica ao jogador\n"
            "- Código: Trocar, em cada manipulador de erro, a mensagem que só sinaliza o erro por uma que indica a próxima ação\n\n"
            "**Depende de.** —"
        )
        self.assertIn(bloco, out)

    def test_recomendacao_null_via_renders_nao_se_aplica(self):
        d = diretriz_valida()
        d["criterios"][0]["recomendacao"]["codigo"] = None
        out = render_markdown([d], self.cats)
        self.assertIn("- Código: não se aplica\n\n**Depende de.**", out)


from vygolint_catalog.render import escape_latex, render_latex


class RenderLatexTest(unittest.TestCase):
    def test_escape(self):
        self.assertEqual(escape_latex("a & b % c _ d # e"), r"a \& b \% c \_ d \# e")
        self.assertEqual(escape_latex(r"x\y"), r"x\textbackslash{}y")
        self.assertEqual(escape_latex("{a}"), r"\{a\}")

    def test_longtable_structure(self):
        out = render_latex([diretriz_valida()], categorias_validas())
        self.assertTrue(out.startswith("% ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão."))
        self.assertIn(r"\begin{longtable}", out)
        self.assertIn(r"\label{tab:catalogo_vygolint}", out)
        self.assertIn(r"\endfirsthead", out)
        self.assertIn(r"\endhead", out)
        self.assertIn(r"D17 & Mediação & O jogo deve exibir feedback construtivo para as ações do jogador & D17.1 (A) \\", out)
        self.assertIn(r"\end{longtable}", out)

    def test_rows_escaped_and_sorted(self):
        a = diretriz_valida()
        a["diretriz"] = "Texto com & e 100%"
        b = diretriz_valida()
        b["id"] = "D06"
        b["categoria"] = "interacao"
        b["criterios"][0]["id"] = "D06.1"
        out = render_latex([a, b], categorias_validas())
        self.assertIn(r"Texto com \& e 100\%", out)
        self.assertLess(out.index("D06 &"), out.index("D17 &"))
