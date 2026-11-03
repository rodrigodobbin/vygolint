import unittest

from helpers import REPO, categorias_validas, diretriz_valida, glossario_valido, schema_valido
from vygolint_catalog.validate import load_definicoes, validate_diretriz
from vygolint_catalog.validate import validate_catalogo


class ValidateDiretrizTest(unittest.TestCase):
    def setUp(self):
        self.schema = schema_valido()
        self.categorias = categorias_validas()

    def check(self, d):
        return validate_diretriz(d, self.schema, self.categorias)

    def test_valid_diretriz_has_no_errors(self):
        self.assertEqual(self.check(diretriz_valida()), [])

    def test_missing_required_field(self):
        d = diretriz_valida()
        del d["fonte"]
        errors = self.check(d)
        self.assertEqual(len(errors), 1)
        self.assertIn("D17", errors[0])
        self.assertIn("fonte", errors[0])

    def test_bad_diretriz_id(self):
        d = diretriz_valida()
        d["id"] = "D7"
        self.assertTrue(any("id" in e for e in self.check(d)))

    def test_unknown_categoria(self):
        d = diretriz_valida()
        d["categoria"] = "magia"
        self.assertTrue(any("categoria" in e for e in self.check(d)))

    def test_non_string_categoria_is_error_not_crash(self):
        d = diretriz_valida()
        d["categoria"] = ["x"]
        self.assertTrue(any("categoria" in e for e in self.check(d)))

    def test_unknown_evidencia_key(self):
        d = diretriz_valida()
        d["criterios"][0]["evidencia"]["audio"] = None
        self.assertTrue(any("desconhecidas" in e for e in self.check(d)))

    def test_bad_modalidade(self):
        d = diretriz_valida()
        d["modalidade"] = "talvez"
        self.assertTrue(any("modalidade" in e for e in self.check(d)))

    def test_aplicabilidade_must_be_null_or_text(self):
        d = diretriz_valida()
        d["aplicabilidade"] = ""
        self.assertTrue(any("aplicabilidade" in e for e in self.check(d)))
        d["aplicabilidade"] = "Somente quando aplicado em sala de aula"
        self.assertEqual(self.check(d), [])

    def test_criterios_must_be_non_empty_list(self):
        d = diretriz_valida()
        d["criterios"] = []
        self.assertTrue(any("criterios" in e for e in self.check(d)))

    def test_criterio_missing_field(self):
        d = diretriz_valida()
        del d["criterios"][0]["escala"]
        errors = self.check(d)
        self.assertTrue(any("D17.1" in e and "escala" in e for e in errors))

    def test_criterio_id_must_match_diretriz(self):
        d = diretriz_valida()
        d["criterios"][0]["id"] = "D18.1"
        self.assertTrue(any("D18.1" in e and "não pertence" in e for e in self.check(d)))

    def test_criterio_bad_nivel(self):
        d = diretriz_valida()
        d["criterios"][0]["nivel"] = "B"
        self.assertTrue(any("nivel" in e for e in self.check(d)))

    def test_justificativa_enums_and_text(self):
        d = diretriz_valida()
        d["criterios"][0]["nivel_justificativa"]["essencialidade"] = "enorme"
        self.assertTrue(any("essencialidade" in e for e in self.check(d)))
        d = diretriz_valida()
        d["criterios"][0]["nivel_justificativa"]["texto"] = ""
        self.assertTrue(any("texto" in e for e in self.check(d)))

    def test_evidencia_requires_all_three_keys(self):
        d = diretriz_valida()
        del d["criterios"][0]["evidencia"]["documentacao"]
        self.assertTrue(any("documentacao" in e for e in self.check(d)))

    def test_evidencia_at_least_one_source(self):
        d = diretriz_valida()
        for k in ("codigo", "documentacao", "video"):
            d["criterios"][0]["evidencia"][k] = None
        self.assertTrue(any("evidencia" in e for e in self.check(d)))

    def test_evidencia_source_shape(self):
        d = diretriz_valida()
        d["criterios"][0]["evidencia"]["codigo"] = {"procedimento": "x", "indicadores": []}
        self.assertTrue(any("indicadores" in e for e in self.check(d)))
        d = diretriz_valida()
        d["criterios"][0]["evidencia"]["codigo"] = {"indicadores": ["a"]}
        self.assertTrue(any("procedimento" in e for e in self.check(d)))

    def test_escala_requires_three_non_empty_descriptors(self):
        d = diretriz_valida()
        d["criterios"][0]["escala"]["parcial"] = ""
        self.assertTrue(any("parcial" in e for e in self.check(d)))
        d = diretriz_valida()
        del d["criterios"][0]["escala"]["nao_atendido"]
        self.assertTrue(any("nao_atendido" in e for e in self.check(d)))

    def test_depende_de_must_be_list_of_lists_of_ids(self):
        d = diretriz_valida()
        d["criterios"][0]["depende_de"] = ["D06.1"]
        self.assertTrue(any("depende_de" in e for e in self.check(d)))
        d = diretriz_valida()
        d["criterios"][0]["depende_de"] = [["D06.1", "D07.1"]]
        self.assertEqual(self.check(d), [])


def _segunda_diretriz():
    d = diretriz_valida()
    d["id"] = "D06"
    d["categoria"] = "interacao"
    d["diretriz"] = "O jogador deve trocar informações com outros jogadores por comunicação síncrona"
    c = d["criterios"][0]
    c["id"] = "D06.1"
    c["nivel"] = "AAA"
    c["nivel_justificativa"]["essencialidade"] = "media"
    c["nivel_justificativa"]["viabilidade"] = "baixa"
    return d


class ValidateCatalogoTest(unittest.TestCase):
    def test_valid_catalog_has_no_errors(self):
        self.assertEqual(validate_catalogo([diretriz_valida(), _segunda_diretriz()]), [])

    def test_duplicate_diretriz_id(self):
        errors = validate_catalogo([diretriz_valida(), diretriz_valida()])
        self.assertTrue(any("duplicado" in e and "D17" in e for e in errors))

    def test_duplicate_criterio_id_across_files(self):
        a = diretriz_valida()
        b = _segunda_diretriz()
        b["criterios"][0]["id"] = "D06.1"
        b["criterios"].append(dict(b["criterios"][0]))
        errors = validate_catalogo([a, b])
        self.assertTrue(any("duplicado" in e and "D06.1" in e for e in errors))

    def test_depende_de_unknown_target(self):
        a = diretriz_valida()
        a["criterios"][0]["depende_de"] = [["D99.1"]]
        errors = validate_catalogo([a])
        self.assertTrue(any("D99.1" in e for e in errors))

    def test_depende_de_self_reference(self):
        a = diretriz_valida()
        a["criterios"][0]["depende_de"] = [["D17.1"]]
        errors = validate_catalogo([a])
        self.assertTrue(any("si mesmo" in e for e in errors))

    def test_depende_de_resolves_across_files(self):
        a = diretriz_valida()
        a["criterios"][0]["depende_de"] = [["D06.1"]]
        self.assertEqual(validate_catalogo([a, _segunda_diretriz()]), [])

    def test_declared_level_must_match_table(self):
        a = diretriz_valida()
        a["criterios"][0]["nivel"] = "AAA"
        errors = validate_catalogo([a])
        self.assertTrue(any("nivel" in e and "esperado A (" in e for e in errors))

    def test_pode_rule_applied_in_coherence_check(self):
        a = diretriz_valida()
        a["modalidade"] = "pode"
        errors = validate_catalogo([a])
        self.assertTrue(any("esperado AA" in e for e in errors))
        a["criterios"][0]["nivel"] = "AA"
        self.assertEqual(validate_catalogo([a]), [])


def _glossario():
    return load_definicoes(REPO / "catalog" / "definicoes.yaml")


class DefinicoesCriterioTest(unittest.TestCase):
    def setUp(self):
        self.schema = schema_valido()
        self.categorias = categorias_validas()
        self.g = _glossario()

    def check(self, d):
        return validate_diretriz(d, self.schema, self.categorias, self.g)

    def _com_missao(self):
        d = diretriz_valida()
        c = d["criterios"][0]
        c["enunciado"] = "Toda ação incorreta do jogador em uma missão recebe mensagem que indica o que fazer"
        c["definicoes"] = {"glossario": ["missao"]}
        return d

    def test_valid_reference_passes(self):
        self.assertEqual(self.check(self._com_missao()), [])

    def test_without_glossary_param_nothing_is_checked(self):
        d = self._com_missao()
        d["criterios"][0]["definicoes"] = {"glossario": ["nao_existe"]}
        self.assertEqual(validate_diretriz(d, self.schema, self.categorias), [])

    def test_unknown_key(self):
        d = self._com_missao()
        d["criterios"][0]["definicoes"]["glossario"] = ["missao", "nao_existe"]
        self.assertTrue(any("nao_existe" in e for e in self.check(d)))

    def test_gatilho_without_key_is_error(self):
        d = self._com_missao()
        d["criterios"][0]["definicoes"] = {}
        errors = self.check(d)
        self.assertTrue(any('"missão"' in e and "missao" in e for e in errors), errors)

    def test_gatilho_in_indicator_and_scale_is_linted(self):
        d = diretriz_valida()
        c = d["criterios"][0]
        c["evidencia"]["codigo"]["indicadores"].append("mensagem cita o desafio")
        self.assertTrue(any("desafio" in e for e in self.check(d)))
        d = diretriz_valida()
        d["criterios"][0]["escala"]["parcial"] = "Alguns cenários orientam"
        self.assertTrue(any("cenario_jogavel" in e for e in self.check(d)))

    def test_justificativa_is_not_linted(self):
        d = diretriz_valida()
        d["criterios"][0]["nivel_justificativa"]["texto"] = "A missão é o centro da ZDP."
        self.assertEqual(self.check(d), [])

    def test_key_listed_but_unused_is_error(self):
        d = diretriz_valida()
        d["criterios"][0]["definicoes"] = {"glossario": ["missao"]}
        self.assertTrue(any("missao" in e and "nenhum gatilho" in e for e in self.check(d)))

    def test_glossary_text_cascades(self):
        # cenario_jogavel's text mentions "missão" and "caminho obrigatório": both keys are required.
        d = diretriz_valida()
        c = d["criterios"][0]
        c["enunciado"] = "Em todo cenário jogável o feedback orienta"
        c["definicoes"] = {"glossario": ["cenario_jogavel"]}
        errors = self.check(d)
        self.assertTrue(any("missao" in e for e in errors), errors)
        self.assertTrue(any("caminho_obrigatorio" in e for e in errors), errors)
        c["definicoes"]["glossario"] += ["missao", "caminho_obrigatorio"]
        self.assertEqual(self.check(d), [])

    def test_locais_shape_and_count_as_usage(self):
        d = diretriz_valida()
        c = d["criterios"][0]
        c["definicoes"] = {"locais": {"dispositivo": "um elemento presente na abertura da missão"}, "glossario": ["missao"]}
        self.assertEqual(self.check(d), [])
        c["definicoes"]["locais"] = {"dispositivo": ""}
        self.assertTrue(any("locais" in e for e in self.check(d)))
        c["definicoes"]["locais"] = ["dispositivo"]
        self.assertTrue(any("locais" in e for e in self.check(d)))

    def test_termos_comuns_silences_lint_with_justification(self):
        d = diretriz_valida()
        c = d["criterios"][0]
        c["escala"]["parcial"] = "O cenário de erro orienta em parte"
        c["definicoes"] = {"termos_comuns": {"cenário": "sentido corrente de situação, não o cenário jogável"}}
        self.assertEqual(self.check(d), [])
        c["definicoes"]["termos_comuns"] = {"cenário": ""}
        self.assertTrue(any("termos_comuns" in e for e in self.check(d)))
        c["definicoes"]["termos_comuns"] = {"foguete": "x"}
        self.assertTrue(any("foguete" in e for e in self.check(d)))
        c["definicoes"] = {"termos_comuns": {"cenário": "x"}, "glossario": ["cenario_jogavel", "missao", "caminho_obrigatorio"]}
        self.assertTrue(any("termos_comuns" in e and "glossario" in e for e in self.check(d)))

    def test_inline_definitions_are_forbidden(self):
        d = self._com_missao()
        c = d["criterios"][0]
        c["escala"]["parcial"] += ". Definição: missão é uma unidade do jogo"
        self.assertTrue(any("Definição" in e for e in self.check(d)))
        d = self._com_missao()
        d["criterios"][0]["enunciado"] += "; missão é " + self.g["missao"]["texto"]
        self.assertTrue(any("glossário" in e and "missao" in e for e in self.check(d)))

    def test_unknown_definicoes_key_and_shape(self):
        d = self._com_missao()
        d["criterios"][0]["definicoes"]["extra"] = 1
        self.assertTrue(any("extra" in e for e in self.check(d)))
        d["criterios"][0]["definicoes"] = "missao"
        self.assertTrue(any("definicoes" in e for e in self.check(d)))
