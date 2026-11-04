import copy
import unittest

from helpers import avaliacao_valida, catalogo_real
from vygolint_catalog.report import grau_esperado, validate_avaliacao


class GrauEsperadoTest(unittest.TestCase):
    def test_worst_among_sources(self):
        self.assertEqual(grau_esperado({"codigo": {"grau": "atendido"}, "video": {"grau": "parcial"}}), "parcial")
        self.assertEqual(grau_esperado({"codigo": {"grau": "nao_atendido"}, "video": {"grau": "atendido"}}), "nao_atendido")

    def test_video_overrides_documentacao(self):
        self.assertEqual(grau_esperado({"documentacao": {"grau": "parcial"}, "video": {"grau": "atendido"}}), "atendido")
        self.assertEqual(grau_esperado({"documentacao": {"grau": "atendido"}, "video": {"grau": "parcial"}}), "parcial")
        self.assertEqual(grau_esperado({"documentacao": {"grau": "parcial"}}), "parcial")

    def test_codigo_still_counts_with_video(self):
        self.assertEqual(
            grau_esperado({"codigo": {"grau": "parcial"}, "documentacao": {"grau": "atendido"}, "video": {"grau": "atendido"}}),
            "parcial",
        )

    def test_no_sources(self):
        self.assertIsNone(grau_esperado({}))


class ValidateAvaliacaoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cat = catalogo_real()

    def check(self, av):
        return validate_avaliacao(av, self.cat)

    def test_valid_fixture_passes(self):
        self.assertEqual(self.check(avaliacao_valida()), [])
        self.assertEqual(self.check(avaliacao_valida(fontes=("documentacao",))), [])

    def test_header_fields(self):
        av = avaliacao_valida()
        del av["jogo"]
        self.assertTrue(any("jogo" in e for e in self.check(av)))
        av = avaliacao_valida()
        av["contexto"]["sala_de_aula"] = "sim"
        self.assertTrue(any("sala_de_aula" in e for e in self.check(av)))
        av = avaliacao_valida()
        av["contexto"]["fontes"] = ["codigo", "audio"]
        self.assertTrue(any("fontes" in e and "audio" in e for e in self.check(av)))
        av = avaliacao_valida()
        av["contexto"]["fontes"] = []
        self.assertTrue(any("fontes" in e for e in self.check(av)))
        av = avaliacao_valida()
        av["data"] = "ontem"
        self.assertTrue(any("data" in e for e in self.check(av)))

    def test_unknown_and_missing_criteria(self):
        av = avaliacao_valida()
        av["criterios"]["D99.1"] = {"grau": "atendido", "fontes": {"codigo": {"grau": "atendido", "provas": ["x"]}}}
        self.assertTrue(any("D99.1" in e and "inexistente" in e for e in self.check(av)))
        av = avaliacao_valida()
        del av["criterios"]["D17.1"]
        self.assertTrue(any("D17.1" in e and "nao_avaliado" in e for e in self.check(av)))

    def test_grau_enum_and_razao(self):
        av = avaliacao_valida()
        av["criterios"]["D17.1"]["grau"] = "quase"
        self.assertTrue(any("D17.1" in e and "grau" in e for e in self.check(av)))
        av = avaliacao_valida()
        av["criterios"]["D17.1"] = {"grau": "nao_avaliado"}
        self.assertTrue(any("D17.1" in e and "razao" in e for e in self.check(av)))

    def test_fora_do_contexto_rules(self):
        av = avaliacao_valida()
        av["criterios"]["D17.1"] = {"grau": "fora_do_contexto", "razao": "x"}
        self.assertTrue(any("D17.1" in e and "aplicabilidade" in e for e in self.check(av)))
        av = avaliacao_valida()
        av["criterios"]["D22.1"] = {"grau": "fora_do_contexto", "razao": "sem sala de aula"}
        self.assertTrue(any("D22.1" in e and "sala_de_aula" in e for e in self.check(av)))
        av["contexto"]["sala_de_aula"] = False
        self.assertEqual(self.check(av), [])

    def test_fontes_shape(self):
        av = avaliacao_valida()
        av["criterios"]["D17.1"]["fontes"]["codigo"]["provas"] = []
        self.assertTrue(any("D17.1" in e and "provas" in e for e in self.check(av)))
        av = avaliacao_valida()
        av["criterios"]["D17.1"]["fontes"]["codigo"]["grau"] = "nao_avaliado"
        self.assertTrue(any("D17.1" in e and "codigo" in e and "grau" in e for e in self.check(av)))
        av = avaliacao_valida()
        av["criterios"]["D17.1"]["fontes"]["audio"] = {"grau": "atendido", "provas": ["x"]}
        self.assertTrue(any("D17.1" in e and "audio" in e for e in self.check(av)))
        av = avaliacao_valida()
        av["criterios"]["D17.1"]["fontes"] = {}
        self.assertTrue(any("D17.1" in e and "fonte" in e for e in self.check(av)))

    def test_source_must_exist_in_criterion_and_context(self):
        av = avaliacao_valida()
        # D22.1 has only documentacao in the catalog
        av["criterios"]["D22.1"]["fontes"]["codigo"] = {"grau": "atendido", "provas": ["x"]}
        self.assertTrue(any("D22.1" in e and "codigo" in e and "evidencia" in e for e in self.check(av)))
        av = avaliacao_valida(fontes=("documentacao",))
        av["criterios"]["D17.1"]["fontes"]["codigo"] = {"grau": "atendido", "provas": ["x"]}
        self.assertTrue(any("D17.1" in e and "codigo" in e and "contexto" in e for e in self.check(av)))

    def test_grau_must_match_sources_unless_justified(self):
        av = avaliacao_valida()
        av["criterios"]["D17.1"]["fontes"]["video"]["grau"] = "parcial"
        errors = self.check(av)
        self.assertTrue(any("D17.1" in e and "justificativa_conflito" in e for e in errors), errors)
        av["criterios"]["D17.1"]["justificativa_conflito"] = "o vídeo não alcançou o ponto"
        self.assertEqual(self.check(av), [])
        av = avaliacao_valida()
        av["criterios"]["D17.1"]["grau"] = "parcial"  # worse than sources, also needs justification
        self.assertTrue(any("D17.1" in e and "justificativa_conflito" in e for e in self.check(av)))
