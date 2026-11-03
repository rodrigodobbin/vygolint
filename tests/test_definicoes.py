import copy
import sys
import unittest
from collections import defaultdict
from pathlib import Path

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
from verify_definicoes import _parser, comparar_criterio, comparar_diretriz, main as verify_main, validar_aceitas  # noqa: E402


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
        # The only manual item is the report of the prefix-less chain cut from the enunciado.
        self.assertEqual([m[3].split(":")[0] for m in self.rel["manuais"]], ["cadeia sem prefixo extraída do enunciado"])

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
        self.c["escala"]["atendido"] = "Todo desafio tem fim, e o desafio é cada missão ou minijogo"
        self.migrar()
        manuais = [(m[2], m[3]) for m in self.rel["manuais"]]
        self.assertEqual(sum(1 for onde, motivo in manuais if onde == "locais[incentivo]" and "escopo" in motivo), 1)
        self.assertTrue(any(onde == "locais[conteúdo e objetivo de aprendizagem]" and "objetivo_de_aprendizagem" in motivo for onde, motivo in manuais))
        # Same rule as the lint: only "<termo|gatilho> é|são <texto>" repeats a glossary definition.
        self.assertTrue(any(onde == "escala.atendido" and "`desafio`" in motivo for onde, motivo in manuais), manuais)
        self.assertFalse(any(onde == "escala.parcial" and "`desafio`" in motivo for onde, motivo in manuais), manuais)

    def test_criterion_rule_folded_into_local_definition_is_reported(self):
        self.c["enunciado"] = "O jogo tem x e y; Definições: x é um objeto; precedência: a sobre b; y é outro"
        self.c["escala"]["parcial"] = ("Alguma missão tem z. Definições: minijogo é " + self.glossario["minijogo"]["texto"]
                                       + "; z é algo; a regra vale para este critério; w é uma função; cada função conta por um elemento")
        defs = self.migrar()
        self.assertEqual(defs["locais"]["x"], "um objeto; precedência: a sobre b")
        regras = [(m[2], m[3], m[4]) for m in self.rel["manuais"] if "regra de critério" in m[3]]
        self.assertEqual(regras, [
            ("enunciado", "regra de critério dentro da definição local `x`", "precedência: a sobre b"),
            ("escala.parcial", "regra de critério dentro da definição local `z`", "a regra vale para este critério"),
            ("escala.parcial", "regra de critério dentro da definição local `w`", "cada função conta por um elemento"),
        ])

    def test_ordinary_continuation_clause_is_not_reported(self):
        self.c["enunciado"] = "O jogo tem x e y; Definições: x é um objeto; o objeto é vermelho quando aceso; y é outro"
        defs = self.migrar()
        self.assertEqual(defs["locais"]["x"], "um objeto; o objeto é vermelho quando aceso")
        self.assertEqual(self.rel["manuais"], [])

    def test_prefixless_chain_cut_is_reported(self):
        self.c["enunciado"] = "Existe x no jogo; x é um objeto qualquer que aparece na tela inicial e que o jogador pode tocar a qualquer momento da partida"
        defs = self.migrar()
        self.assertEqual(self.c["enunciado"], "Existe x no jogo")
        self.assertIn("x", defs["locais"])
        cadeias = [m for m in self.rel["manuais"] if m[3].startswith("cadeia sem prefixo")]
        self.assertEqual(len(cadeias), 1)
        self.assertEqual(cadeias[0][2], "enunciado")
        self.assertEqual(cadeias[0][3], "cadeia sem prefixo extraída do enunciado: `x é um objeto qualquer que aparece na tela inicial e que o jogador pode tocar a…`")
        md = relatorio_markdown(self.rel, self.glossario)
        self.assertIn("- D17/D17.1 (enunciado): cadeia sem prefixo extraída do enunciado: `x é um objeto", md)

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


class VerifyTest(unittest.TestCase):
    def setUp(self):
        from helpers import diretriz_valida
        self.g = load_definicoes(REPO / "catalog" / "definicoes.yaml")
        self.antigo = diretriz_valida()["criterios"][0]
        self.antigo["enunciado"] = "A abertura de cada missão tem um dispositivo; Definições: missão é " + self.g["missao"]["texto"] + "; dispositivo é um elemento da abertura"
        self.antigo["escala"]["parcial"] = "Uma missão tem, outra não. Definição: dispositivo é um elemento da abertura"
        self.novo = diretriz_valida()["criterios"][0]
        self.novo["enunciado"] = "A abertura de cada missão tem um dispositivo"
        self.novo["escala"]["parcial"] = "Uma missão tem, outra não, nos termos das definições"
        self.novo["definicoes"] = {"glossario": ["missao"], "locais": {"dispositivo": "um elemento da abertura"}}
        self.aceitas = {"clausulas": [], "adicoes": [], "remocoes": [], "campos": []}

    def test_equal_after_migration(self):
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_changed_field_text_is_reported(self):
        self.novo["enunciado"] = "A abertura de cada missão tem dois dispositivos"
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("enunciado" in d for d in diffs), diffs)
        self.aceitas["campos"].append({"criterio": "D17.1", "campo": "enunciado", "de": "A abertura de cada missão tem um dispositivo", "para": "A abertura de cada missão tem dois dispositivos"})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_lost_definition_is_reported(self):
        del self.novo["definicoes"]["locais"]
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("dispositivo" in d for d in diffs), diffs)
        self.aceitas["remocoes"].append({"criterio": "D17.1", "clausula": "dispositivo = um elemento da abertura"})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_added_glossary_key_needs_adicao(self):
        self.novo["definicoes"]["glossario"].append("desafio")
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("desafio" in d for d in diffs), diffs)
        self.aceitas["adicoes"].append({"criterio": "*", "chave": "desafio"})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_variant_needs_clausula_mapping(self):
        self.antigo["enunciado"] = self.antigo["enunciado"].replace(self.g["missao"]["texto"], "uma atividade com objetivo próprio")
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("missão = uma atividade" in d for d in diffs), diffs)
        self.aceitas["clausulas"].append({"de": "missão = uma atividade com objetivo próprio", "para": normalizar_clausula("missão é " + self.g["missao"]["texto"]), "tipo": "decisao", "decisao": 1})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_remover_in_campos(self):
        self.antigo["escala"]["atendido"] = "Todas orientam, e missão é uma atividade"
        self.novo["escala"]["atendido"] = "Todas orientam"
        self.aceitas["campos"].append({"criterio": "D17.1", "campo": "*", "remover": ", e missão é uma atividade"})
        self.aceitas["clausulas"].append({"de": "missão = uma atividade", "para": normalizar_clausula("missão é " + self.g["missao"]["texto"]), "tipo": "decisao", "decisao": 1})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    # --- additions beyond the brief ---

    def test_missing_or_null_definicoes_does_not_raise(self):
        for valor in ("ausente", None, {}, {"glossario": None, "locais": None}):
            novo = copy.deepcopy(self.novo)
            if valor == "ausente":
                del novo["definicoes"]
            else:
                novo["definicoes"] = valor
            diffs = comparar_criterio(self.antigo, novo, self.g, self.aceitas)
            self.assertTrue(any("missão = " in d for d in diffs), (valor, diffs))
            self.assertTrue(any("dispositivo = " in d for d in diffs), (valor, diffs))

    def test_unknown_glossary_key_is_reported_not_raised(self):
        self.novo["definicoes"]["glossario"].append("inexistente")
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("inexistente" in d for d in diffs), diffs)
        self.aceitas["adicoes"].append({"criterio": "*", "chave": "inexistente"})
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("inexistente" in d for d in diffs), diffs)

    def test_adicao_by_key_covers_every_clause_of_the_key(self):
        self.novo["definicoes"]["glossario"].append("cenario_jogavel")
        self.assertEqual(len(clausulas(self.g["cenario_jogavel"]["texto"])), 2)
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertEqual(len(diffs), 2, diffs)
        self.aceitas["adicoes"].append({"criterio": "D17.1", "chave": "cenario_jogavel"})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_aceitas_for_other_criterion_do_not_apply(self):
        self.novo["definicoes"]["glossario"].append("desafio")
        self.aceitas["adicoes"].append({"criterio": "D18.1", "chave": "desafio"})
        self.assertTrue(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas))

    def test_clausula_mapping_to_two_keys(self):
        self.antigo["enunciado"] = "Cada missão ou desafio tem fim; Definições: missão ou desafio é uma atividade"
        self.novo["enunciado"] = "Cada missão ou desafio tem fim"
        self.novo["definicoes"]["glossario"] = ["missao", "minijogo", "desafio"]
        self.aceitas["clausulas"].append({"de": "missão ou desafio = uma atividade", "para": [
            normalizar_clausula("missão é " + self.g["missao"]["texto"]), normalizar_clausula("desafio é " + self.g["desafio"]["texto"])], "tipo": "decisao", "decisao": 2})
        self.aceitas["adicoes"].append({"criterio": "*", "chave": "minijogo"})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_remover_that_matches_nothing_is_reported(self):
        self.aceitas["campos"].append({"criterio": "D17.1", "campo": "*", "remover": ", e missão é outra coisa"})
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("remover" in d for d in diffs), diffs)

    def test_new_or_dropped_text_field_is_reported(self):
        self.novo["evidencia"]["video"]["indicadores"].append("indicador novo")
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("video.indicadores[2]" in d for d in diffs), diffs)
        self.novo["evidencia"]["video"]["indicadores"].pop()
        self.novo["evidencia"]["video"]["indicadores"].pop()
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("video.indicadores[1]" in d for d in diffs), diffs)

    def test_non_text_fields_must_not_change(self):
        self.novo["nivel"] = "AA"
        self.novo["nivel_justificativa"]["texto"] = "outro"
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("nivel" in d and "AA" in d for d in diffs), diffs)
        self.assertTrue(any("nivel_justificativa" in d for d in diffs), diffs)

    def test_diretriz_level_fields_and_criteria_pairing(self):
        from helpers import diretriz_valida
        antigo, novo = diretriz_valida(), diretriz_valida()
        antigo["criterios"][0] = self.antigo
        novo["criterios"][0] = self.novo
        self.assertEqual(comparar_diretriz(antigo, novo, self.g, self.aceitas), [])
        novo["fonte"] = "outra"
        novo["criterios"].append(dict(self.novo, id="D17.2"))
        antigo["criterios"].append(dict(self.antigo, id="D17.3"))
        diffs = comparar_diretriz(antigo, novo, self.g, self.aceitas)
        self.assertTrue(any("fonte" in d for d in diffs), diffs)
        self.assertTrue(any("D17.2" in d for d in diffs), diffs)
        self.assertTrue(any("D17.3" in d for d in diffs), diffs)

    def test_pointer_already_in_stage_1_text(self):
        # D29 stage 1 already says "classificadas nos termos das definições" outside the block.
        self.antigo["escala"]["atendido"] = "Todas orientam, classificadas nos termos das definições"
        self.novo["escala"]["atendido"] = "Todas orientam, classificadas nos termos das definições"
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])
        self.novo["escala"]["atendido"] = "Todas orientam, classificadas"
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])
        self.novo["escala"]["atendido"] = "Todas orientam"
        self.assertTrue(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas))

    def test_comparator_agrees_with_migration_script(self):
        """Whatever migrar_criterio produces must verify clean, up to glossary divergences and cascade keys."""
        textos = {
            "enunciado": ("O jogo tem incentivo e cenário; Definições: incentivo é uma recompensa visível; o incentivo persiste quando o jogador sai; "
                          "cenário, neste critério, é o ambiente visual; a missão exige mais de um jogador quando a conclusão só é registrada depois de dois"),
            "codigo.procedimento": "Verificar cada incentivo. Definições: incentivo é uma recompensa visível; o incentivo persiste quando o jogador sai. Regra de desempate: vale o código",
            "escala.parcial": "Existe missão que aceita dois jogadores. Definição: a missão aceita dois jogadores quando o jogo permite",
            "escala.atendido": "Cada missão tem fim. Definições: missão é " + self.g["missao"]["texto"] + "; a missão exige mais de um jogador quando há placar; jogador é uma pessoa que joga",
        }
        antigo = copy.deepcopy(self.antigo)
        antigo["enunciado"] = textos["enunciado"]
        antigo["evidencia"]["codigo"]["procedimento"] = textos["codigo.procedimento"]
        antigo["escala"]["parcial"] = textos["escala.parcial"]
        antigo["escala"]["atendido"] = textos["escala.atendido"]
        novo = copy.deepcopy(antigo)
        rel = defaultdict(list)
        migrar_criterio(novo, self.g, rel, "D17")
        self.assertIn("missão exige mais de um jogador", novo["definicoes"]["locais"])
        self.assertIn("cenário", novo["definicoes"]["locais"])
        self.assertEqual(rel["divergencias"], [])
        diffs = comparar_criterio(antigo, novo, self.g, self.aceitas)
        self.assertTrue(diffs and all("definição nova não aceita [glossario: " in d for d in diffs), diffs)
        self.aceitas["adicoes"] = [{"criterio": "D17.1", "chave": a[3]} for a in rel["adicionadas"]]
        self.assertEqual(comparar_criterio(antigo, novo, self.g, self.aceitas), [])


    # --- review fixes ---

    def _variante(self):
        """Stage 1 uses a variant of the missão definition; the glossary key is accepted as an addition."""
        self.antigo["enunciado"] = self.antigo["enunciado"].replace(self.g["missao"]["texto"], "uma atividade com objetivo próprio")
        self.aceitas["adicoes"].append({"criterio": "*", "chave": "missao"})
        return {"de": "missão = uma atividade com objetivo próprio", "para": normalizar_clausula("missão é " + self.g["missao"]["texto"]), "tipo": "equivalente"}

    def test_malformed_clausula_entry_is_not_applied(self):
        base = self._variante()
        ruins = [{k: v for k, v in base.items() if k != "para"}]
        ruins += [dict(base, para=p) for p in (None, "", [], [""], [None], 3)]
        ruins += [dict(base, de=""), dict(base, de=None), dict(base, tipo="outro"), {k: v for k, v in base.items() if k != "tipo"},
                  dict(base, tipo="decisao"), dict(base, tipo="decisao", decisao=None)]
        for ruim in ruins:
            self.aceitas["clausulas"] = [ruim]
            diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
            self.assertTrue(any("missão = uma atividade com objetivo próprio" in d for d in diffs), (ruim, diffs))
        self.aceitas["clausulas"] = [dict(base, tipo="decisao", decisao=3)]
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_every_escala_key_and_evidencia_source_is_compared(self):
        self.antigo["escala"]["extra"] = "texto da etapa 1"
        self.novo["escala"]["extra"] = "texto mudado"
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("escala" in d and "texto mudado" in d for d in diffs), diffs)
        self.novo["escala"]["extra"] = "texto da etapa 1"
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])
        self.antigo["evidencia"]["quinta"] = {"procedimento": "proc", "indicadores": ["ind"]}
        self.novo["evidencia"]["quinta"] = {"procedimento": "proc", "indicadores": ["ind mudado"]}
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("evidencia" in d and "ind mudado" in d for d in diffs), diffs)

    def test_masked_fields_are_exactly_the_compared_text_fields(self):
        # A text field still changes only through the text comparison, not as a structural change.
        self.novo["evidencia"]["codigo"]["indicadores"][0] = "outro indicador"
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("codigo.indicadores[0]" in d for d in diffs), diffs)
        self.assertFalse(any("campo não textual" in d for d in diffs), diffs)

    def test_duplicate_criterion_ids_are_reported(self):
        from helpers import diretriz_valida
        antigo, novo = diretriz_valida(), diretriz_valida()
        antigo["criterios"] = [self.antigo]
        mudado = copy.deepcopy(self.novo)
        mudado["enunciado"] = "outro texto"
        novo["criterios"] = [mudado, self.novo]
        diffs = comparar_diretriz(antigo, novo, self.g, self.aceitas)
        self.assertTrue(any("duplicado" in d and "D17.1" in d for d in diffs), diffs)
        novo["criterios"] = [self.novo]
        antigo["criterios"] = [self.antigo, copy.deepcopy(self.antigo)]
        diffs = comparar_diretriz(antigo, novo, self.g, self.aceitas)
        self.assertTrue(any("duplicado" in d and "D17.1" in d for d in diffs), diffs)

    def test_pointer_glued_inside_a_word_is_not_stripped(self):
        self.antigo["escala"]["atendido"] = "Todas orientam, classificadas nos termos das definiçõesabc"
        self.novo["escala"]["atendido"] = "Todas orientam, classificadasabc"
        self.assertTrue(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas))

    def test_usadas_collects_the_entries_that_were_applied(self):
        base = self._variante()
        self.aceitas["clausulas"] = [base, {"de": "outra = coisa", "para": "x", "tipo": "equivalente"}]
        self.aceitas["remocoes"].append({"criterio": "D17.1", "clausula": "nada = nada"})
        usadas = set()
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas, usadas=usadas), [])
        # adicoes[0] (from _variante) is not needed once the mapping applies, so it is not used either.
        self.assertEqual(usadas, {"clausulas[0]"})

    def test_frases_substitute_a_phrase_of_the_stage_1_text_only_when_listed(self):
        self.antigo["escala"]["atendido"] = "Todas orientam, nos termos do enunciado"
        self.novo["escala"]["atendido"] = "Todas orientam, nos termos do enunciado e das definições"
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("escala.atendido" in d for d in diffs), diffs)
        frase = {"de": "nos termos do enunciado", "para": "nos termos do enunciado e das definições", "tipo": "decisao", "decisao": 12}
        self.aceitas["frases"] = [frase]
        usadas = set()
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas, usadas=usadas), [])
        self.assertEqual(usadas, {"frases[0]"})
        # A phrase change that no entry lists is still reported, even next to a listed one.
        self.novo["escala"]["atendido"] = "Quase todas orientam, nos termos do enunciado e das definições"
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("escala.atendido" in d and "Quase todas" in d for d in diffs), diffs)

    def test_malformed_frase_entry_is_not_applied(self):
        self.antigo["escala"]["atendido"] = "Todas orientam, nos termos do enunciado"
        self.novo["escala"]["atendido"] = "Todas orientam, nos termos do enunciado e das definições"
        base = {"de": "nos termos do enunciado", "para": "nos termos do enunciado e das definições"}
        ruins = [{"de": base["de"]}, {"para": base["para"]}, dict(base, de=""), dict(base, para=""), dict(base, para=None),
                 dict(base, criterio="D17.1"), dict(base, tipo="decisao"), "nos termos do enunciado"]
        for ruim in ruins:
            self.aceitas["frases"] = [ruim]
            self.assertTrue(validar_aceitas(self.aceitas), ruim)
            diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
            self.assertTrue(any("escala.atendido" in d for d in diffs), (ruim, diffs))
        self.aceitas["frases"] = [base]
        self.assertEqual(validar_aceitas(self.aceitas), [])
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])


class VerifyCliTest(unittest.TestCase):
    """End to end on a throwaway git repo: --base, --only, --catalog, --aceitas, exit code."""

    def setUp(self):
        import shutil
        import subprocess
        import tempfile
        from helpers import diretriz_valida
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        cat = self.tmp / "catalog"
        cat.mkdir()
        shutil.copy(REPO / "catalog" / "definicoes.yaml", cat / "definicoes.yaml")
        d = diretriz_valida()
        d["criterios"][0]["enunciado"] = "Cada missão tem fim; Definições: missão é uma atividade"
        (cat / "D17.yaml").write_text(emit_yaml(d), encoding="utf-8")
        git = ["git", "-C", str(self.tmp), "-c", "user.name=t", "-c", "user.email=t@t", "-c", "commit.gpgsign=false"]
        subprocess.run(["git", "init", "-q", str(self.tmp)], check=True)
        subprocess.run(git + ["add", "."], check=True)
        subprocess.run(git + ["commit", "-q", "-m", "etapa 1"], check=True)
        d["criterios"][0]["enunciado"] = "Cada missão tem fim"
        d["criterios"][0]["definicoes"] = {"glossario": ["missao"]}
        (cat / "D17.yaml").write_text(emit_yaml(d), encoding="utf-8")
        self.cat = cat
        self.aceitas = self.tmp / "aceitas.yaml"
        self.aceitas.write_text(yaml.safe_dump({"clausulas": [{"de": "missão = uma atividade", "para": normalizar_clausula("missão é " + load_definicoes(cat / "definicoes.yaml")["missao"]["texto"]), "tipo": "decisao", "decisao": 1}]}, allow_unicode=True), encoding="utf-8")

    def run_main(self, *args):
        import contextlib
        import io
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = verify_main(["--base", "HEAD", "--catalog", str(self.cat), *args])
        return code, out.getvalue()

    def test_aceitas_default_and_override(self):
        self.assertEqual(Path(_parser().parse_args([]).aceitas), REPO / "scripts" / "definicoes_aceitas.yaml")
        self.assertEqual(_parser().parse_args(["--aceitas", "x.yaml"]).aceitas, "x.yaml")
        code, out = self.run_main()
        self.assertEqual(code, 1, out)
        self.assertIn("missão = uma atividade", out)
        code, out = self.run_main("--aceitas", str(self.aceitas))
        self.assertEqual(code, 0, out)
        self.assertIn("0 diferença", out)

    def test_only_filters_files(self):
        code, out = self.run_main("--only", "D17", "--aceitas", str(self.aceitas))
        self.assertEqual(code, 0, out)
        code, out = self.run_main("--only", "D17,D99", "--aceitas", str(self.aceitas))
        self.assertEqual(code, 1, out)
        self.assertIn("D99", out)
        self.assertIn("1 diferença", out)

    def write_aceitas(self, **listas):
        doc = yaml.safe_load(self.aceitas.read_text(encoding="utf-8"))
        for k, v in listas.items():
            doc[k] = doc.get(k, []) + v
        self.aceitas.write_text(yaml.safe_dump(doc, allow_unicode=True), encoding="utf-8")

    def test_malformed_entry_is_reported(self):
        self.write_aceitas(clausulas=[{"de": "x = y", "para": None, "tipo": "equivalente"}],
                           campos=[{"criterio": "D17.1", "campo": "*", "de": "a", "para": "b"}])
        code, out = self.run_main("--aceitas", str(self.aceitas))
        self.assertEqual(code, 1, out)
        self.assertIn("aceitas: clausulas[1] sem 'para'", out)
        self.assertIn("aceitas: campos[0]", out)

    def test_unused_entries_are_reported(self):
        self.write_aceitas(clausulas=[{"de": "outra = coisa", "para": "x", "tipo": "equivalente"}],
                           adicoes=[{"criterio": "D17.1", "chave": "desafio"}],
                           remocoes=[{"criterio": "D17.1", "clausula": "nada = nada"}],
                           campos=[{"criterio": "D17.1", "campo": "enunciado", "de": "a", "para": "b"}],
                           frases=[{"de": "frase ausente", "para": "outra frase"}])
        code, out = self.run_main("--aceitas", str(self.aceitas))
        self.assertEqual(code, 1, out)
        self.assertIn("aceitas não usadas: clausulas[1] de=outra = coisa", out)
        self.assertIn("aceitas não usadas: adicoes[0]", out)
        self.assertIn("aceitas não usadas: remocoes[0]", out)
        self.assertIn("aceitas não usadas: campos[0]", out)
        self.assertIn("aceitas não usadas: frases[0] de=frase ausente", out)
        self.assertNotIn("clausulas[0]", out)
        self.assertIn("5 diferença", out)
        code, out = self.run_main("--only", "D17", "--aceitas", str(self.aceitas))
        self.assertNotIn("frases[0]", out)

    def test_file_missing_at_base_is_reported(self):
        (self.cat / "D18.yaml").write_text((self.cat / "D17.yaml").read_text(encoding="utf-8"), encoding="utf-8")
        code, out = self.run_main("--only", "D18", "--aceitas", str(self.aceitas))
        self.assertEqual(code, 1, out)
        self.assertIn("D18", out)

    def test_repo_aceitas_file_has_the_known_lists(self):
        doc = yaml.safe_load((REPO / "scripts" / "definicoes_aceitas.yaml").read_text(encoding="utf-8"))
        self.assertLessEqual({"clausulas", "adicoes", "remocoes", "campos"}, set(doc))
        self.assertLessEqual(set(doc), {"clausulas", "adicoes", "remocoes", "campos", "frases"})
