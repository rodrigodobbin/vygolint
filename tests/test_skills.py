import re
import unittest

from helpers import REPO

SKILLS = ("using-vygolint", "vygolint-avaliar", "vygolint-criterio", "vygolint-video")
CLAUSULA = (
    "O resultado de uma avaliação vygolint expressa conformidade com as diretrizes de Carvalho (2020) "
    "e não classifica o jogo como sociointeracionista."
)
_FM = re.compile(r"^---\n(.*?)\n---\n", re.S)


def _frontmatter(texto):
    m = _FM.match(texto)
    assert m, "sem frontmatter"
    return dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)


class SkillsTest(unittest.TestCase):
    def _ler(self, nome):
        return (REPO / "skills" / nome / "SKILL.md").read_text(encoding="utf-8")

    def test_all_skills_exist_with_frontmatter(self):
        for nome in SKILLS:
            with self.subTest(nome=nome):
                fm = _frontmatter(self._ler(nome))
                self.assertEqual(fm["name"].strip(), nome)
                self.assertTrue(fm["description"].strip())
                self.assertTrue(fm["description"].strip().startswith("Use when"), fm["description"])

    def test_no_other_entries_in_skills_dir(self):
        pastas = sorted(p.name for p in (REPO / "skills").iterdir() if not p.name.startswith("."))
        self.assertEqual(pastas, sorted(SKILLS))
        self.assertFalse((REPO / "skills" / ".gitkeep").exists())

    def test_clause_in_every_skill(self):
        for nome in SKILLS:
            with self.subTest(nome=nome):
                self.assertIn(CLAUSULA, self._ler(nome))

    def test_avaliar_runs_the_script_and_never_computes_level(self):
        t = self._ler("vygolint-avaliar")
        self.assertIn("scripts/vygolint_report.py", t)
        self.assertIn("avaliacao.yaml", t)
        self.assertIn("vygolint-criterio", t)
        self.assertIn("vygolint-video", t)
        self.assertIn("nunca calcula", t)

    def test_avaliar_starts_from_the_scaffold_and_reads_lint_warnings(self):
        t = self._ler("vygolint-avaliar")
        for trecho in ("scripts/vygolint_scaffold.py", "--artefato", "PREENCHER", "--force", "aviso", "--strict"):
            self.assertIn(trecho, t)
        self.assertIn("vygolint_scaffold.py", self._ler("using-vygolint"))
        self.assertIn("vygolint_scaffold.py", self._ler("vygolint-criterio"))

    def test_avaliar_explains_folder_scope(self):
        t = self._ler("vygolint-avaliar")
        for trecho in ("Uma pasta põe no escopo todos os arquivos dentro dela", "--externa", "fontes_externas",
                       "fora dos artefatos", "sem registro_video nem prova", "inventario.md"):
            self.assertIn(trecho, t)
        self.assertIn("contexto.artefatos", self._ler("vygolint-criterio"))

    def test_avaliar_fills_the_inventory_skeleton(self):
        t = self._ler("vygolint-avaliar")
        for trecho in ("Preencha `<pasta>/inventario.md`", "`Classificação`", "documento equivalente", "não conta",
                       "sem classificação no inventario.md", "aviso inventario: ainda contém PREENCHER"):
            self.assertIn(trecho, t)

    def test_criterio_rules(self):
        t = self._ler("vygolint-criterio")
        for trecho in ("justificativa_conflito", "nao_avaliado", "razao", "Vídeo prevalece sobre documentação", "provas"):
            self.assertIn(trecho, t)

    def test_video_format(self):
        t = self._ler("vygolint-video")
        for trecho in ("ffmpeg", "ffprobe", "registro_video.yaml", "eventos", "hh:mm:ss"):
            self.assertIn(trecho, t)

    def test_video_reads_contact_sheets(self):
        t = self._ler("vygolint-video")
        for trecho in ("fps=1,scale=640:-2", "tile=4x5", "tile=5x6", "folhas/f%03d.png", "gt(scene,0.4)", "gt(scene,0.2)",
                       "-frames:v 1", "fps=1/5"):
            self.assertIn(trecho, t)
        # recent ffmpeg rejects -vsync: no command in the skill may pass it
        for bloco in re.findall(r"```bash\n(.*?)```", t, re.S) + re.findall(r"`([^`\n]*ffmpeg[^`\n]*)`", t):
            self.assertNotIn("-vsync", bloco)

    def test_using_points_to_everything(self):
        t = self._ler("using-vygolint")
        for trecho in ("vygolint-avaliar", "vygolint-criterio", "vygolint-video", "catalog/", "docs/conformidade.md", "VYGOLINT_ROOT"):
            self.assertIn(trecho, t)
        self.assertLess(len(t.splitlines()), 60)
