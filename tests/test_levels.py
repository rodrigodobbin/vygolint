import unittest

from vygolint_catalog.levels import derive_nivel


class DeriveNivelTest(unittest.TestCase):
    def test_table_all_nine_combinations(self):
        expected = {
            ("alta", "alta"): "A",
            ("alta", "media"): "A",
            ("alta", "baixa"): "AA",
            ("media", "alta"): "AA",
            ("media", "media"): "AA",
            ("media", "baixa"): "AAA",
            ("baixa", "alta"): "AAA",
            ("baixa", "media"): "AAA",
            ("baixa", "baixa"): "AAA",
        }
        for (ess, via), nivel in expected.items():
            with self.subTest(ess=ess, via=via):
                self.assertEqual(derive_nivel(ess, via), nivel)

    def test_pode_never_yields_a(self):
        self.assertEqual(derive_nivel("alta", "alta", "pode"), "AA")
        self.assertEqual(derive_nivel("alta", "media", "pode"), "AA")

    def test_pode_keeps_aa_and_aaa(self):
        self.assertEqual(derive_nivel("media", "alta", "pode"), "AA")
        self.assertEqual(derive_nivel("baixa", "alta", "pode"), "AAA")

    def test_invalid_values_raise(self):
        with self.assertRaises(ValueError):
            derive_nivel("altissima", "alta")
        with self.assertRaises(ValueError):
            derive_nivel("alta", "nenhuma")
        with self.assertRaises(ValueError):
            derive_nivel("alta", "alta", "talvez")
