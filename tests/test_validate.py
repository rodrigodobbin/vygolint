import unittest

from helpers import categorias_validas, diretriz_valida, schema_valido
from vygolint_catalog.validate import validate_diretriz


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
        self.assertTrue(any("D18.1" in e for e in self.check(d)))

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
