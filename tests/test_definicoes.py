import copy
import sys
import unittest
from collections import defaultdict

import yaml

from helpers import REPO, glossario_valido
from vygolint_catalog.validate import load_definicoes, validate_definicoes

sys.path.insert(0, str(REPO / "scripts"))
from migrate_definicoes import (  # noqa: E402
    ALIASES,
    _prefixo_menos,
    agrupar,
    clausulas,
    emit_yaml,
    extrair_blocos,
    migrar_criterio,
    normalizar_clausula,
    relatorio_markdown,
)


class GlossarioTest(unittest.TestCase):
    def test_repo_glossary_is_valid(self):
        self.assertEqual(validate_definicoes(glossario_valido()), [])

    def test_load_returns_map_by_key(self):
        g = load_definicoes(REPO / "catalog" / "definicoes.yaml")
        self.assertIn("missao", g)
        self.assertEqual(g["missao"]["termo"], "missão")
        self.assertIn("missões", g["missao"]["gatilhos"])
        self.assertTrue(g["missao"]["texto"].startswith("uma unidade do jogo"))

    def test_required_fields_and_shapes(self):
        doc = glossario_valido()
        del doc["termos"][0]["texto"]
        self.assertTrue(any("missao" in e and "texto" in e for e in validate_definicoes(doc)))
        doc = glossario_valido()
        doc["termos"][0]["gatilhos"] = []
        self.assertTrue(any("gatilhos" in e for e in validate_definicoes(doc)))
        doc = glossario_valido()
        doc["termos"][0]["chave"] = "Missão"
        self.assertTrue(any("chave" in e for e in validate_definicoes(doc)))
        doc = glossario_valido()
        doc["termos"][0]["chave"] = ["x"]
        self.assertTrue(any("chave" in e for e in validate_definicoes(doc)))

    def test_duplicate_key_and_duplicate_gatilho(self):
        doc = glossario_valido()
        doc["termos"].append(copy.deepcopy(doc["termos"][0]))
        errors = validate_definicoes(doc)
        self.assertTrue(any("duplicad" in e and "missao" in e for e in errors))
        doc = glossario_valido()
        doc["termos"][1]["gatilhos"].append("missão")
        self.assertTrue(any("gatilho" in e and "missão" in e for e in validate_definicoes(doc)))

    def test_non_map_document(self):
        self.assertTrue(validate_definicoes(["x"]))
        self.assertTrue(validate_definicoes({"termos": "x"}))


class EmitYamlTest(unittest.TestCase):
    def test_roundtrip_every_catalog_file(self):
        for path in sorted((REPO / "catalog").glob("D*.yaml")):
            with self.subTest(path=path.name):
                d = yaml.safe_load(path.read_text(encoding="utf-8"))
                self.assertEqual(yaml.safe_load(emit_yaml(d)), d)

    def test_layout_and_quoting(self):
        from helpers import diretriz_valida
        d = diretriz_valida()
        d["criterios"][0]["enunciado"] = 'Texto com "aspas" e \\ barra'
        d["criterios"][0]["depende_de"] = [["D06.1", "D07.1"]]
        d["criterios"][0]["definicoes"] = {"glossario": ["missao"], "locais": {"abertura da missão": "trecho"}}
        out = emit_yaml(d)
        self.assertTrue(out.startswith("id: D17\ncategoria: mediacao\ndiretriz: \"O jogo"))
        self.assertIn('    enunciado: "Texto com \\"aspas\\" e \\\\ barra"', out)
        self.assertIn("      codigo:\n        procedimento: \"Localizar", out)
        self.assertIn("        indicadores:\n          - \"mensagem", out)
        self.assertIn("      documentacao: null\n", out)
        self.assertIn("    depende_de:\n      - [D06.1, D07.1]\n", out)
        self.assertIn("    definicoes:\n      glossario: [missao]\n      locais:\n        \"abertura da missão\": \"trecho\"\n", out)
        self.assertEqual(yaml.safe_load(out), d)


class ExtratorTest(unittest.TestCase):
    def test_block_at_end_of_enunciado(self):
        t = "A abertura apresenta um dispositivo; Definições: missão é uma unidade; dispositivo é um destes elementos (a; b) presentes"
        texto, blocos = extrair_blocos(t)
        self.assertEqual(texto, "A abertura apresenta um dispositivo")
        self.assertEqual(blocos, ["missão é uma unidade; dispositivo é um destes elementos (a; b) presentes"])

    def test_block_in_middle_of_procedimento(self):
        t = "Verificar no GDD cada missão. Definições: missão é uma unidade do jogo. Regra de desempate: vale o GDD"
        texto, blocos = extrair_blocos(t)
        self.assertEqual(texto, "Verificar no GDD cada missão. Regra de desempate: vale o GDD")
        self.assertEqual(blocos, ["missão é uma unidade do jogo"])

    def test_single_definition_in_scale(self):
        t = "Nenhuma missão tem dispositivo, nos termos do enunciado. Definição: abertura da missão é o trecho exibido antes"
        texto, blocos = extrair_blocos(t)
        self.assertEqual(texto, "Nenhuma missão tem dispositivo, nos termos do enunciado")
        self.assertEqual(blocos, ["abertura da missão é o trecho exibido antes"])

    def test_trailing_chain_without_prefix(self):
        t = "O jogador alcança áreas fora do caminho da missão em curso; caminho da missão é a sequência de objetivos exigidos para completá-la"
        texto, blocos = extrair_blocos(t)
        self.assertEqual(texto, "O jogador alcança áreas fora do caminho da missão em curso")
        self.assertEqual(blocos, ["caminho da missão é a sequência de objetivos exigidos para completá-la"])

    def test_no_block(self):
        self.assertEqual(extrair_blocos("Texto simples; outra frase"), ("Texto simples; outra frase", []))

    def test_clausulas_respect_parentheses(self):
        self.assertEqual(clausulas("a é x (p; q); b é y"), ["a é x (p; q)", "b é y"])

    def test_agrupar_merges_clauses_starting_with_article_or_verb(self):
        grupos = agrupar(["detalhe é um elemento", "o desafio exige o detalhe quando X", "o detalhe é sinalizado quando Y", "fala é áudio"])
        self.assertEqual(grupos, [("detalhe", ["detalhe é um elemento", "o desafio exige o detalhe quando X", "o detalhe é sinalizado quando Y"]), ("fala", ["fala é áudio"])])
        self.assertEqual(agrupar(["caminho obrigatório, o mesmo que caminho da missão em D05, é a sequência"]), [("caminho obrigatório", ["caminho obrigatório, o mesmo que caminho da missão em D05, é a sequência"])])
        self.assertEqual(agrupar(["a missão aceita dois jogadores quando o jogo permite"]), [("", ["a missão aceita dois jogadores quando o jogo permite"])])

    def test_aliases_and_normalization(self):
        self.assertEqual(ALIASES["missão ou desafio"], ["missao", "desafio"])
        self.assertEqual(normalizar_clausula("objetivos de aprendizagem são os listados no GDD. "), "objetivos de aprendizagem = os listados no GDD")
        self.assertEqual(normalizar_clausula("missão é  uma unidade"), "missão = uma unidade")

    def test_trailing_chain_keeps_continuation_clauses(self):
        t = "Existe missão em grupo; jogador é uma pessoa que joga; a missão exige mais de um jogador quando a conclusão só é registrada depois de dois"
        texto, blocos = extrair_blocos(t)
        self.assertEqual(texto, "Existe missão em grupo")
        self.assertEqual(blocos, ["jogador é uma pessoa que joga; a missão exige mais de um jogador quando a conclusão só é registrada depois de dois"])
        self.assertEqual(extrair_blocos(t, cadeia=False), (t, []))

    def test_term_cannot_start_with_conjunction_or_be_a_scope_note(self):
        grupos = agrupar([
            "comparação visível é aquela em que a tela mostra outro jogador",
            "quando o resultado é de equipe, comparação visível é aquela em que a tela mostra outra equipe",
            "poder acessar áreas fora do caminho é tratado em D05, e o acesso sem recompensa não conta",
        ])
        self.assertEqual([t for t, _ in grupos], ["comparação visível"])
        self.assertEqual(len(grupos[0][1]), 3)

    def test_term_with_apposition(self):
        self.assertEqual(agrupar(["cenário, neste critério, é o ambiente visual"])[0][0], "cenário")


class MigrarCriterioTest(unittest.TestCase):
    def setUp(self):
        from helpers import diretriz_valida
        self.glossario = load_definicoes(REPO / "catalog" / "definicoes.yaml")
        self.c = diretriz_valida()["criterios"][0]
        self.rel = defaultdict(list)

    def migrar(self):
        migrar_criterio(self.c, self.glossario, self.rel, "D17")
        _prefixo_menos(self.c, self.glossario, "D17", self.rel)
        return self.c.get("definicoes", {})

    def test_clauses_after_glossary_term_become_locais(self):
        self.c["enunciado"] = ("Existe missão em grupo; missão ou tarefa é uma unidade do jogo com objetivo e condição de conclusão próprios; "
                               "a missão exige mais de um jogador quando a conclusão só é registrada depois de dois")
        defs = self.migrar()
        self.assertEqual(self.c["enunciado"], "Existe missão em grupo")
        self.assertEqual(defs["glossario"], ["missao"])
        self.assertEqual(defs["locais"], {"missão exige mais de um jogador": "quando a conclusão só é registrada depois de dois"})
        self.assertEqual(len(self.rel["sobras"]), 1)
        self.assertEqual([d[3] for d in self.rel["divergencias"]], ["missao"])
        self.assertEqual(self.rel["manuais"], [])

    def test_clauses_after_local_term_stay_in_that_definition(self):
        self.c["enunciado"] = "O desafio exige detalhe; Definições: detalhe é um elemento visível; o desafio exige o detalhe quando não há outra via"
        defs = self.migrar()
        self.assertEqual(defs["locais"], {"detalhe": "um elemento visível; o desafio exige o detalhe quando não há outra via"})

    def test_glossary_keys_follow_cascade_in_glossary_order(self):
        self.c["enunciado"] = "Cada desafio tem fim; Definições: desafio é cada missão ou minijogo"
        defs = self.migrar()
        self.assertEqual(self.c["enunciado"], "Cada desafio tem fim")
        self.assertEqual(defs["glossario"], ["missao", "minijogo", "desafio"])
        self.assertEqual(self.rel["divergencias"], [])
        self.assertEqual(sorted(a[3] for a in self.rel["adicionadas"]), ["minijogo", "missao"])

    def test_untermed_quando_clause_gets_its_own_key(self):
        self.c["escala"]["parcial"] = "Existe missão que aceita dois jogadores. Definição: a missão aceita dois jogadores quando o jogo permite"
        defs = self.migrar()
        self.assertEqual(self.c["escala"]["parcial"], "Existe missão que aceita dois jogadores")
        self.assertEqual(defs["locais"], {"missão aceita dois jogadores": "quando o jogo permite"})

    def test_manual_items(self):
        self.c["enunciado"] = "A premissa cita a fonte; Definições: premissa do jogo é a situação inicial, e missão é uma atividade com objetivo"
        self.c["escala"]["atendido"] = "Cada missão apresenta uma situação-problema, isto é, uma situação com estado inicial"
        self.c["escala"]["nao_atendido"] = "Nenhum objetivo de aprendizagem é apresentado em situação real"
        defs = self.migrar()
        self.assertEqual(defs["locais"], {"premissa do jogo": "a situação inicial, e missão é uma atividade com objetivo"})
        onde = [m[2] for m in self.rel["manuais"]]
        self.assertIn("locais[premissa do jogo]", onde)
        self.assertIn("escala.atendido", onde)
        self.assertNotIn("escala.nao_atendido", onde)

    def test_manual_items_for_locais_and_literal_glossary_text(self):
        self.c["enunciado"] = ("O jogo tem incentivo; Definições: incentivo é uma recompensa (item tratado em D12); "
                               "poder acessar áreas é tratado em D05, e o acesso sem recompensa não conta; "
                               "conteúdo e objetivo de aprendizagem são os listados no GDD")
        self.c["escala"]["parcial"] = "Em cada missão ou minijogo há fim"
        self.migrar()
        manuais = [(m[2], m[3]) for m in self.rel["manuais"]]
        self.assertEqual(sum(1 for onde, motivo in manuais if onde == "locais[incentivo]" and "escopo" in motivo), 1)
        self.assertTrue(any(onde == "locais[conteúdo e objetivo de aprendizagem]" and "objetivo_de_aprendizagem" in motivo for onde, motivo in manuais))
        self.assertTrue(any(onde == "escala.parcial" and "`desafio`" in motivo for onde, motivo in manuais))

    def test_glossary_key_without_trigger_is_reported(self):
        self.c["enunciado"] = "O professor lê a documentação; Definições: documentação é o documento de design"
        defs = self.migrar()
        self.assertEqual(defs["glossario"], ["documentacao_equivalente"])
        self.assertTrue(any(m[2] == "definicoes.glossario" and "documentacao_equivalente" in m[3] for m in self.rel["manuais"]))

    def test_report_has_six_sections_and_groups_fields(self):
        self.c["enunciado"] = "Cada missão tem fim; Definições: missão é uma atividade"
        self.c["escala"]["parcial"] = "Alguma missão tem fim. Definição: missão é uma atividade"
        self.migrar()
        md = relatorio_markdown(self.rel, self.glossario)
        self.assertEqual(md.count("\n## "), 6)
        linhas = [l for l in md.splitlines() if "D17/D17.1" in l and "missão é uma atividade" in l]
        self.assertEqual(len(linhas), 1)
        self.assertIn("enunciado", linhas[0])
        self.assertIn("escala.parcial", linhas[0])
