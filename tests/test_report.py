import copy
import unittest

from helpers import avaliacao_valida, catalogo_real
from vygolint_catalog.report import aggregate, grau_esperado, validate_avaliacao, vias_para


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




class ViasParaTest(unittest.TestCase):
    rec = {"documentacao": "doc", "design": "des", "codigo": "cod"}

    def test_rule(self):
        self.assertEqual(vias_para(["codigo", "documentacao", "video"], self.rec), [("codigo", "cod")])
        self.assertEqual(vias_para(["documentacao"], self.rec), [("documentacao", "doc"), ("design", "des")])
        self.assertEqual(vias_para(["video"], self.rec), [("design", "des"), ("codigo", "cod")])
        self.assertEqual(
            vias_para(["documentacao", "video"], self.rec),
            [("documentacao", "doc"), ("design", "des"), ("codigo", "cod")],
        )

    def test_null_via_falls_back(self):
        rec = {"documentacao": "doc", "design": "des", "codigo": None}
        self.assertEqual(vias_para(["codigo"], rec), [("documentacao", "doc"), ("design", "des")])
        rec = {"documentacao": None, "design": "des", "codigo": "cod"}
        self.assertEqual(vias_para(["documentacao"], rec), [("design", "des")])


class AggregateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cat = catalogo_real()

    def agg(self, av):
        return aggregate(av, self.cat)

    def test_all_met_is_aaa(self):
        res = self.agg(avaliacao_valida())
        self.assertEqual(res["nivel"], "AAA")
        self.assertEqual(res["bloqueios"], [])
        self.assertEqual(res["parciais"], [])
        self.assertEqual(res["cobertura_nivel"]["A"]["atendido"], 21)
        self.assertEqual(res["cobertura_nivel"]["AA"]["atendido"], 12)
        self.assertEqual(res["cobertura_nivel"]["AAA"]["atendido"], 10)
        self.assertEqual(res["cobertura_categoria"]["interacao"]["atendido"], 17)
        self.assertEqual(list(res["cobertura_categoria"]), [c["chave"] for c in self.cat["categorias"]["categorias"]])

    def test_level_steps(self):
        av = avaliacao_valida()
        av["criterios"]["D06.1"]["grau"] = "nao_atendido"
        av["criterios"]["D06.1"]["fontes"]["codigo"]["grau"] = "nao_atendido"
        av["criterios"]["D06.1"]["fontes"]["video"]["grau"] = "nao_atendido"
        self.assertEqual(self.agg(av)["nivel"], "AA")  # D06.1 is AAA
        av["criterios"]["D07.1"]["grau"] = "parcial"
        av["criterios"]["D07.1"]["fontes"]["codigo"]["grau"] = "parcial"
        av["criterios"]["D07.1"]["fontes"]["video"]["grau"] = "parcial"
        self.assertEqual(self.agg(av)["nivel"], "A")  # D07.1 is AA
        av["criterios"]["D17.1"]["grau"] = "parcial"
        av["criterios"]["D17.1"]["fontes"]["codigo"]["grau"] = "parcial"
        av["criterios"]["D17.1"]["fontes"]["video"]["grau"] = "parcial"
        self.assertEqual(self.agg(av)["nivel"], "sem_conformidade")  # D17.1 is A

    def test_dependency_not_met_forces_nao_atendido(self):
        av = avaliacao_valida()
        for cid in ("D06.1", "D07.1"):
            av["criterios"][cid]["grau"] = "nao_atendido"
            for f in av["criterios"][cid]["fontes"].values():
                f["grau"] = "nao_atendido"
        res = self.agg(av)
        c = res["criterios"]["D13.1"]
        self.assertEqual(c["grau_declarado"], "atendido")
        self.assertEqual(c["grau"], "nao_atendido")
        self.assertIn("D06.1", c["nota"])
        self.assertIn("D07.1", c["nota"])
        # D27.1 depends on D13.1: propagates
        self.assertEqual(res["criterios"]["D27.1"]["grau"], "nao_atendido")
        self.assertIn("D13.1", res["criterios"]["D27.1"]["nota"])

    def test_dependency_on_nao_avaliado(self):
        av = avaliacao_valida()
        av["criterios"]["D17.1"] = {"grau": "nao_avaliado", "razao": "sem evidência"}
        res = self.agg(av)
        self.assertEqual(res["criterios"]["D40.1"]["grau"], "nao_avaliado")
        self.assertIn("D17.1", res["criterios"]["D40.1"]["nota"])
        self.assertEqual(res["cobertura_nivel"]["A"]["nao_avaliado"], 2)
        self.assertEqual(res["cobertura_nivel"]["A"]["nao_atendido"], 2)
        self.assertEqual(res["nivel"], "sem_conformidade")

    def test_fora_do_contexto_excluded_from_level(self):
        av = avaliacao_valida()
        av["contexto"]["sala_de_aula"] = False
        av["criterios"]["D22.1"] = {"grau": "fora_do_contexto", "razao": "sem sala de aula"}
        av["criterios"]["D22.2"] = {"grau": "fora_do_contexto", "razao": "sem sala de aula"}
        res = self.agg(av)
        self.assertEqual(res["nivel"], "AAA")
        self.assertEqual(res["cobertura_nivel"]["AA"]["fora_do_contexto"], 1)
        self.assertEqual(res["cobertura_nivel"]["AAA"]["fora_do_contexto"], 1)
        self.assertEqual(res["cobertura_nivel"]["AA"]["atendido"], 11)

    def test_bloqueios_target_next_level_with_vias(self):
        # documentacao + video: every criterion has a source, so only D07.1 fails; vias rule gives the three vias
        av = avaliacao_valida(fontes=("documentacao", "video"))
        av["criterios"]["D07.1"]["grau"] = "parcial"
        for f in av["criterios"]["D07.1"]["fontes"].values():
            f["grau"] = "parcial"
        res = self.agg(av)
        self.assertEqual(res["nivel"], "A")
        ids = [b["id"] for b in res["bloqueios"]]
        self.assertEqual(ids, ["D07.1"])
        b = res["bloqueios"][0]
        self.assertEqual(b["nivel"], "AA")
        self.assertEqual(b["grau"], "parcial")
        self.assertEqual([v for v, _ in b["vias"]], ["documentacao", "design", "codigo"])
        self.assertEqual(b["enunciado"], self.cat["criterios"]["D07.1"]["criterio"]["enunciado"])
        self.assertEqual([p["id"] for p in res["parciais"]], ["D07.1"])
        self.assertEqual(res["parciais"][0]["escala_parcial"], self.cat["criterios"]["D07.1"]["criterio"]["escala"]["parcial"])

    def test_bloqueio_by_dependency_points_to_dependency(self):
        av = avaliacao_valida()
        for cid in ("D06.1", "D07.1"):
            av["criterios"][cid]["grau"] = "nao_atendido"
            for f in av["criterios"][cid]["fontes"].values():
                f["grau"] = "nao_atendido"
        res = self.agg(av)
        self.assertEqual(res["nivel"], "A")
        por_id = {b["id"]: b for b in res["bloqueios"]}
        self.assertIn("D07.1", por_id)
        self.assertIn("D16.1", por_id)  # AA, depends on D06.1 or D07.1
        self.assertEqual(por_id["D16.1"]["vias"], [])
        self.assertIn("D06.1", por_id["D16.1"]["nota"])
        self.assertTrue(por_id["D07.1"]["vias"])

    def test_bloqueios_empty_at_aaa_and_sorted(self):
        av = avaliacao_valida()
        self.assertEqual(self.agg(av)["bloqueios"], [])
        for cid in ("D38.1", "D01.1"):
            av["criterios"][cid]["grau"] = "nao_atendido"
            for f in av["criterios"][cid]["fontes"].values():
                f["grau"] = "nao_atendido"
        self.assertEqual([b["id"] for b in self.agg(av)["bloqueios"]], ["D01.1", "D38.1"])
