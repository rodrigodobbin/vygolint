import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from helpers import REPO, diretriz_valida
from vygolint_catalog.build import build


class BuildTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.catalog = self.tmp / "catalog"
        self.docs = self.tmp / "docs"
        self.catalog.mkdir()
        shutil.copy(REPO / "catalog" / "schema.yaml", self.catalog)
        shutil.copy(REPO / "catalog" / "categorias.yaml", self.catalog)
        shutil.copy(REPO / "catalog" / "definicoes.yaml", self.catalog)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def write(self, d, name=None):
        (self.catalog / (name or f"{d['id']}.yaml")).write_text(
            yaml.safe_dump(d, allow_unicode=True, sort_keys=False), encoding="utf-8"
        )

    def test_missing_glossary_is_error(self):
        (self.catalog / "definicoes.yaml").unlink()
        self.write(diretriz_valida())
        errors = build(self.catalog, self.docs)
        self.assertTrue(any("definicoes.yaml" in e for e in errors))
        self.assertFalse(self.docs.exists())

    def test_invalid_glossary_is_error(self):
        (self.catalog / "definicoes.yaml").write_text("termos: [{chave: x}]\n", encoding="utf-8")
        self.write(diretriz_valida())
        self.assertTrue(any("definicoes.yaml" in e for e in build(self.catalog, self.docs)))

    def test_lint_runs_in_build(self):
        d = diretriz_valida()
        d["criterios"][0]["enunciado"] = "Em cada missão o feedback orienta"
        self.write(d)
        errors = build(self.catalog, self.docs)
        self.assertTrue(any("missao" in e for e in errors), errors)
        d["criterios"][0]["definicoes"] = {"glossario": ["missao"]}
        self.write(d)
        self.assertEqual(build(self.catalog, self.docs), [])
        self.assertIn("**Definições.**", (self.docs / "catalogo.md").read_text(encoding="utf-8"))

    def test_valid_catalog_writes_both_docs(self):
        self.write(diretriz_valida())
        self.assertEqual(build(self.catalog, self.docs), [])
        md = (self.docs / "catalogo.md").read_text(encoding="utf-8")
        tex = (self.docs / "catalogo.tex").read_text(encoding="utf-8")
        self.assertIn("| D17 |", md)
        self.assertIn("D17 &", tex)

    def test_invalid_catalog_writes_nothing(self):
        d = diretriz_valida()
        d["criterios"][0]["nivel"] = "AAA"
        self.write(d)
        errors = build(self.catalog, self.docs)
        self.assertTrue(errors)
        self.assertFalse(self.docs.exists())

    def test_yaml_syntax_error_reports_filename_and_writes_nothing(self):
        (self.catalog / "D17.yaml").write_text("id: D17\ncategoria: [unclosed\n", encoding="utf-8")
        errors = build(self.catalog, self.docs)
        self.assertEqual(len(errors), 1)
        self.assertIn("D17.yaml", errors[0])
        self.assertFalse(self.docs.exists())

    def test_non_map_file_reports_filename(self):
        (self.catalog / "D17.yaml").write_text("- a\n- b\n", encoding="utf-8")
        errors = build(self.catalog, self.docs)
        self.assertTrue(errors)
        self.assertTrue(all("D17.yaml" in e for e in errors))
        self.assertFalse(self.docs.exists())

    def test_filename_must_match_id(self):
        self.write(diretriz_valida(), name="D18.yaml")
        errors = build(self.catalog, self.docs)
        self.assertTrue(any("D18.yaml" in e and "D17" in e for e in errors))

    def test_build_is_deterministic(self):
        self.write(diretriz_valida())
        build(self.catalog, self.docs)
        first = (self.docs / "catalogo.md").read_bytes()
        build(self.catalog, self.docs)
        self.assertEqual(first, (self.docs / "catalogo.md").read_bytes())

    def test_cli_exit_codes(self):
        self.write(diretriz_valida())
        cmd = [sys.executable, str(REPO / "scripts" / "build_catalog.py"), "--catalog", str(self.catalog), "--docs", str(self.docs)]
        ok = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertIn("OK: 1 diretrizes, 1 critérios", ok.stdout)
        d = diretriz_valida()
        del d["fonte"]
        self.write(d)
        bad = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertIn("fonte", bad.stderr)
