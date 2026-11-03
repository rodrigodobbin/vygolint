import copy
import unittest

from helpers import REPO, glossario_valido
from vygolint_catalog.validate import load_definicoes, validate_definicoes


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
