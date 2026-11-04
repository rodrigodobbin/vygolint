import json
import os
import unittest

from helpers import REPO
import vygolint_catalog

MANIFESTOS = (
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    ".kimi-plugin/plugin.json",
    "gemini-extension.json",
    "package.json",
)
ARQUIVOS = MANIFESTOS + (
    ".claude-plugin/marketplace.json",
    ".agents/plugins/marketplace.json",
    ".opencode/plugins/vygolint.js",
    ".opencode/INSTALL.md",
    ".pi/extensions/vygolint.ts",
    "GEMINI.md",
    "hooks/hooks.json",
    "hooks/hooks-cursor.json",
    "hooks/run-hook.cmd",
    "hooks/session-start",
)


def _json(rel):
    return json.loads((REPO / rel).read_text(encoding="utf-8"))


class ManifestsTest(unittest.TestCase):
    def test_all_files_exist(self):
        for rel in ARQUIVOS:
            with self.subTest(rel=rel):
                self.assertTrue((REPO / rel).exists(), rel)

    def test_versions_match_package(self):
        for rel in MANIFESTOS:
            with self.subTest(rel=rel):
                self.assertEqual(_json(rel)["version"], vygolint_catalog.__version__)
        self.assertEqual(_json(".claude-plugin/marketplace.json")["plugins"][0]["version"], vygolint_catalog.__version__)

    def test_names(self):
        for rel in MANIFESTOS:
            with self.subTest(rel=rel):
                self.assertEqual(_json(rel)["name"], "vygolint")

    def test_skills_dir_references(self):
        for rel in (".codex-plugin/plugin.json", ".cursor-plugin/plugin.json", ".kimi-plugin/plugin.json"):
            self.assertEqual(_json(rel)["skills"], "./skills/")
        self.assertEqual(_json("package.json")["pi"]["skills"], ["./skills"])
        self.assertTrue((REPO / "skills" / "using-vygolint" / "SKILL.md").exists())

    def test_hooks_reference_existing_executable_script(self):
        hooks = _json("hooks/hooks.json")
        cmd = hooks["hooks"]["SessionStart"][0]["hooks"][0]["command"]
        self.assertIn("run-hook.cmd", cmd)
        self.assertIn("session-start", cmd)
        for nome in ("run-hook.cmd", "session-start"):
            self.assertTrue(os.access(REPO / "hooks" / nome, os.X_OK), nome)
        self.assertEqual(_json(".cursor-plugin/plugin.json")["hooks"], "./hooks/hooks-cursor.json")
        self.assertEqual(_json(".kimi-plugin/plugin.json")["sessionStart"], {"skill": "using-vygolint"})

    def test_gemini_points_to_bootstrap(self):
        self.assertEqual(_json("gemini-extension.json")["contextFileName"], "GEMINI.md")
        self.assertIn("skills/using-vygolint/SKILL.md", (REPO / "GEMINI.md").read_text(encoding="utf-8"))

    def test_bootstrap_sources_point_to_using_vygolint(self):
        for rel in (".opencode/plugins/vygolint.js", ".pi/extensions/vygolint.ts", "hooks/session-start"):
            with self.subTest(rel=rel):
                self.assertIn("using-vygolint", (REPO / rel).read_text(encoding="utf-8"))
