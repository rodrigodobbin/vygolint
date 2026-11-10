import unittest


class SmokeTest(unittest.TestCase):
    def test_package_imports(self):
        import vygolint_catalog

        self.assertEqual(vygolint_catalog.__version__, "0.4.0")

    def test_yaml_available(self):
        import yaml

        self.assertEqual(yaml.safe_load("a: 1"), {"a": 1})
