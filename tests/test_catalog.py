import shutil
import tempfile
import unittest
from pathlib import Path

from helpers import REPO, catalogo_real
from vygolint_catalog.catalog import load_catalog


class LoadCatalogTest(unittest.TestCase):
    def test_real_catalog_loads(self):
        cat = catalogo_real()
        self.assertEqual(len(cat["diretrizes"]), 40)
        self.assertEqual(len(cat["criterios"]), 43)
        self.assertEqual(cat["criterios"]["D17.1"]["diretriz"]["id"], "D17")
        self.assertEqual(cat["criterios"]["D17.1"]["criterio"]["nivel"], "A")
        self.assertIn("missao", cat["glossario"])
        self.assertEqual([d["id"] for d in cat["diretrizes"]][:2], ["D01", "D02"])

    def test_missing_glossary_is_error(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            shutil.copy(REPO / "catalog" / "schema.yaml", tmp)
            shutil.copy(REPO / "catalog" / "categorias.yaml", tmp)
            cat, errors = load_catalog(tmp)
            self.assertIsNone(cat)
            self.assertTrue(any("definicoes.yaml" in e for e in errors))
        finally:
            shutil.rmtree(tmp)

    def test_invalid_criterion_is_error(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            for name in ("schema.yaml", "categorias.yaml", "definicoes.yaml"):
                shutil.copy(REPO / "catalog" / name, tmp)
            (tmp / "D17.yaml").write_text("id: D17\ncategoria: mediacao\n", encoding="utf-8")
            cat, errors = load_catalog(tmp)
            self.assertIsNone(cat)
            self.assertTrue(any("D17" in e for e in errors))
        finally:
            shutil.rmtree(tmp)
