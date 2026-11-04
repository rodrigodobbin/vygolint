import copy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from helpers import REPO, avaliacao_valida, catalogo_real
from vygolint_catalog.report import (
    CLAUSULA, aggregate, build_report, grau_esperado, render_relatorio, render_resultado,
    validate_avaliacao, vias_para,
)
from vygolint_catalog.html import build_data, render_relatorio_html


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

    def test_non_list_fontes_does_not_raise(self):
        for valor in (5, True):
            av = avaliacao_valida()
            av["contexto"]["fontes"] = valor
            errors = self.check(av)
            self.assertTrue(any("contexto.fontes" in e for e in errors))

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
        self.assertTrue(any("contexto.fontes deve ser lista" in e for e in self.check(av)))
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

    def test_fontes_not_allowed_on_ungraded_entries(self):
        av = avaliacao_valida()
        av["criterios"]["D06.1"] = {"grau": "nao_avaliado", "razao": "x", "fontes": "x"}
        self.assertTrue(any("D06.1" in e and "fontes não se aplicam" in e for e in self.check(av)))
        av = avaliacao_valida()
        av["contexto"]["sala_de_aula"] = False
        av["criterios"]["D22.1"] = {
            "grau": "fora_do_contexto", "razao": "x",
            "fontes": {"documentacao": {"grau": "atendido", "provas": ["x"]}},
        }
        self.assertTrue(any("D22.1" in e and "fontes não se aplicam" in e for e in self.check(av)))
        for vazio in ({}, None):
            av = avaliacao_valida()
            av["criterios"]["D06.1"] = {"grau": "nao_avaliado", "razao": "x", "fontes": vazio}
            self.assertEqual(self.check(av), [])

    def test_artefatos_values_must_be_lists_of_texts(self):
        av = avaliacao_valida()
        av["contexto"]["artefatos"]["codigo"] = "src"
        self.assertTrue(any("artefatos" in e for e in self.check(av)))
        av = avaliacao_valida()
        av["contexto"]["artefatos"]["codigo"] = ["src", ""]
        self.assertTrue(any("artefatos" in e for e in self.check(av)))

    def test_observacao_must_be_text(self):
        av = avaliacao_valida()
        av["criterios"]["D17.1"]["fontes"]["codigo"]["observacao"] = 5
        self.assertTrue(any("D17.1" in e and "observacao deve ser texto não vazio" in e for e in self.check(av)))



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

    def _set(self, av, cid, grau):
        av["criterios"][cid]["grau"] = grau
        for f in av["criterios"][cid]["fontes"].values():
            f["grau"] = grau

    def test_nota_accumulates_all_failing_groups(self):
        cat = copy.deepcopy(self.cat)
        crit = cat["criterios"]["D13.1"]["criterio"]
        crit["depende_de"] = [["D06.1", "D07.1"], ["D17.1"]]
        dc = next(c for d in cat["diretrizes"] for c in d["criterios"] if c["id"] == "D13.1")
        self.assertIs(dc, crit)
        av = avaliacao_valida()
        for cid in ("D06.1", "D07.1", "D17.1"):
            self._set(av, cid, "nao_atendido")
        nota = aggregate(av, cat)["criterios"]["D13.1"]["nota"]
        self.assertIn("D06.1 ou D07.1", nota)
        self.assertIn("D17.1", nota)

    def test_mixed_group_with_nao_avaliado_is_nao_avaliado(self):
        av = avaliacao_valida()
        av["criterios"]["D06.1"] = {"grau": "nao_avaliado", "razao": "sem evidência"}
        self._set(av, "D07.1", "nao_atendido")
        c = self.agg(av)["criterios"]["D13.1"]
        self.assertEqual(c["grau"], "nao_avaliado")
        self.assertIn("não avaliado por dependência", c["nota"])

    def test_bloqueios_empty_at_aaa_and_sorted(self):
        av = avaliacao_valida()
        self.assertEqual(self.agg(av)["bloqueios"], [])
        for cid in ("D38.1", "D01.1"):
            av["criterios"][cid]["grau"] = "nao_atendido"
            for f in av["criterios"][cid]["fontes"].values():
                f["grau"] = "nao_atendido"
        self.assertEqual([b["id"] for b in self.agg(av)["bloqueios"]], ["D01.1", "D38.1"])


def _escrever(av, pasta):
    p = Path(pasta) / "avaliacao.yaml"
    p.write_text(yaml.safe_dump(av, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return p


class RenderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cat = catalogo_real()

    def _exemplo(self):
        av = avaliacao_valida(fontes=("documentacao", "video"))
        av["contexto"]["sala_de_aula"] = False
        av["criterios"]["D22.1"] = {"grau": "fora_do_contexto", "razao": "o jogo não é aplicado em sala de aula"}
        av["criterios"]["D22.2"] = {"grau": "fora_do_contexto", "razao": "o jogo não é aplicado em sala de aula"}
        av["criterios"]["D06.1"] = {"grau": "nao_avaliado", "razao": "não há vídeo com dois jogadores"}
        av["criterios"]["D01.1"]["grau"] = "parcial"
        av["criterios"]["D01.1"]["fontes"]["video"]["grau"] = "parcial"
        av["criterios"]["D01.1"]["fontes"]["video"]["observacao"] = "missão 2 resolvida repetindo a mesma ação"
        return av

    def test_report_sections_and_content(self):
        av = self._exemplo()
        res = aggregate(av, self.cat)
        md = render_relatorio(res, av, self.cat)
        self.assertTrue(md.startswith("<!-- ARQUIVO GERADO por scripts/vygolint_report.py"))
        self.assertIn("# Relatório vygolint — Jogo de teste", md)
        self.assertIn(CLAUSULA, md)
        for titulo in (
            "## 1. Cláusula", "## 2. Nível alcançado", "## 3. Cobertura por nível",
            "## 4. Cobertura por categoria", "## 5. Bloqueios", "## 6. Parciais", "## 7. Provas por critério",
        ):
            self.assertIn(titulo, md)
        self.assertIn("**Nível alcançado: sem conformidade**", md)
        self.assertIn("| A | 20 | 1 | 0 (dos quais 0 não avaliados) | 0 |", md)
        self.assertIn("| AAA | 8 | 0 | 1 (dos quais 1 não avaliados) | 1 |", md)
        self.assertIn("#### D01.1 — Nível A — parcial", md)
        self.assertIn("- Documentação: " + self.cat["criterios"]["D01.1"]["criterio"]["recomendacao"]["documentacao"], md)
        self.assertIn("- Design: " + self.cat["criterios"]["D01.1"]["criterio"]["recomendacao"]["design"], md)
        self.assertNotIn("- Código:", md.split("## 6. Parciais")[0].split("#### D01.1")[1].split("####")[0])
        self.assertIn("- Falta: " + self.cat["criterios"]["D01.1"]["criterio"]["escala"]["atendido"], md)
        self.assertIn("### D22.1 — fora do contexto", md)
        self.assertIn("o jogo não é aplicado em sala de aula", md)
        self.assertIn("### D06.1 — não avaliado", md)
        self.assertIn("- Vídeo (parcial):\n  - gameplay/sessao1.mp4 00:00:00 — observação que satisfaz D01.1\n  - Observação: missão 2 resolvida", md)

    def test_resultado_yaml(self):
        av = self._exemplo()
        res = aggregate(av, self.cat)
        doc = yaml.safe_load(render_resultado(res, av))
        self.assertEqual(doc["jogo"], "Jogo de teste")
        self.assertEqual(doc["nivel"], "sem_conformidade")
        self.assertEqual(len(doc["criterios"]), 43)
        self.assertEqual(doc["criterios"]["D01.1"], {"nivel": "A", "grau": "parcial", "grau_declarado": "parcial", "nota": None})
        self.assertEqual(doc["criterios"]["D22.1"]["grau"], "fora_do_contexto")
        self.assertEqual(list(doc["criterios"])[:2], ["D01.1", "D02.1"])

    def test_deterministic(self):
        av = self._exemplo()
        res = aggregate(av, self.cat)
        self.assertEqual(render_relatorio(res, av, self.cat), render_relatorio(aggregate(av, self.cat), av, self.cat))


class BuildReportTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp)

    def test_writes_all_files(self):
        p = _escrever(avaliacao_valida(), self.tmp)
        self.assertEqual(build_report(p, REPO / "catalog", self.tmp), [])
        self.assertTrue((self.tmp / "relatorio.md").exists())
        self.assertTrue((self.tmp / "relatorio.html").exists())
        self.assertTrue((self.tmp / "resultado.yaml").exists())

    def test_html_report(self):
        import json
        import re

        cat = catalogo_real()
        av = yaml.safe_load((REPO / "docs" / "exemplo" / "avaliacao.yaml").read_text(encoding="utf-8"))
        res = aggregate(av, cat)
        html = render_relatorio_html(res, av, cat)
        self.assertIn(CLAUSULA, html)
        self.assertIn("ARQUIVO GERADO", html)
        self.assertNotIn("/*__DATA__*/", html)
        blob = re.search(r"const DATA = (\{.*?\});\n", html, re.S).group(1)
        data = json.loads(blob)
        self.assertEqual(data, build_data(res, av, cat))
        self.assertEqual(data["nivel"], res["nivel"])
        self.assertEqual(len(data["criterios"]), len(cat["criterios"]))
        self.assertEqual([c["id"] for c in data["criterios"]], sorted(cat["criterios"]))
        por_id = {c["id"]: c for c in data["criterios"]}
        for cid, c in res["criterios"].items():
            self.assertEqual(por_id[cid]["grau"], c["grau"])
            self.assertEqual(por_id[cid]["nota"], c["nota"])
        self.assertEqual(data["bloqueios"], [b["id"] for b in res["bloqueios"]])
        self.assertEqual(data["parciais"], [p["id"] for p in res["parciais"]])
        for c in data["criterios"]:
            if c["nota"] and c["grau_declarado"] != c["grau"]:
                self.assertEqual(c["vias"], [])
        self.assertEqual(data["clausula"], CLAUSULA)

    def test_html_destravas(self):
        cat = catalogo_real()
        av = avaliacao_valida(fontes=("video",))
        for cid in ("D06.1", "D22.1"):
            av["criterios"].pop(cid, None)
        av["criterios"]["D06.1"] = {"grau": "nao_avaliado", "razao": "sem gravação com dois jogadores"}
        av["contexto"]["sala_de_aula"] = False
        av["criterios"]["D22.1"] = {"grau": "fora_do_contexto", "razao": "sem sala de aula"}
        for cid, e in av["criterios"].items():
            if cid not in ("D06.1", "D22.1") and e.get("fontes"):
                e["fontes"] = {"video": {"grau": e["grau"], "provas": ["gameplay/s.mp4 00:00:01 — x"]}} if cat["criterios"][cid]["criterio"]["evidencia"].get("video") else None
                if e["fontes"] is None:
                    av["criterios"][cid] = {"grau": "nao_avaliado", "razao": "critério não aceita vídeo"}
        self.assertEqual(validate_avaliacao(av, cat), [])
        data = build_data(aggregate(av, cat), av, cat)
        grupos = {d["entregar"]: d["criterios"] for d in data["destravas"]}
        codigo = [k for k in grupos if "código" in k]
        self.assertTrue(codigo)
        self.assertIn("D06.1", grupos[codigo[0]])
        sala = [k for k in grupos if "sala de aula" in k]
        self.assertTrue(sala)
        self.assertEqual(grupos[sala[0]], ["D22.1"])

    def test_missing_file_is_reported(self):
        errors = build_report(self.tmp / "nao-existe.yaml", REPO / "catalog", self.tmp)
        self.assertEqual(len(errors), 1)
        self.assertIn("nao-existe.yaml", errors[0])
        self.assertEqual(list(self.tmp.iterdir()), [])

    def test_invalid_writes_nothing(self):
        av = avaliacao_valida()
        del av["criterios"]["D17.1"]
        p = _escrever(av, self.tmp)
        errors = build_report(p, REPO / "catalog", self.tmp)
        self.assertTrue(any("D17.1" in e for e in errors))
        self.assertFalse((self.tmp / "relatorio.md").exists())

    def test_bad_yaml_reports_filename(self):
        p = self.tmp / "avaliacao.yaml"
        p.write_text("jogo: [unclosed\n", encoding="utf-8")
        errors = build_report(p, REPO / "catalog", self.tmp)
        self.assertEqual(len(errors), 1)
        self.assertIn("avaliacao.yaml", errors[0])

    def test_invalid_date_reports_filename(self):
        p = self.tmp / "avaliacao.yaml"
        p.write_text("jogo: x\ndata: 2026-02-30\n", encoding="utf-8")
        errors = build_report(p, REPO / "catalog", self.tmp)
        self.assertEqual(len(errors), 1)
        self.assertIn("avaliacao.yaml", errors[0])
        self.assertEqual([x.name for x in self.tmp.iterdir()], ["avaliacao.yaml"])

    def test_cli(self):
        p = _escrever(avaliacao_valida(), self.tmp)
        cmd = [sys.executable, str(REPO / "scripts" / "vygolint_report.py"), str(p), "--out", str(self.tmp)]
        ok = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertIn("OK: nível AAA", ok.stdout)
        av = avaliacao_valida()
        av["criterios"]["D17.1"]["grau"] = "quase"
        p = _escrever(av, self.tmp)
        bad = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertIn("D17.1", bad.stderr)
