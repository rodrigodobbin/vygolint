import json
import os
import subprocess
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

    def test_authorship_license_and_citation(self):
        for rel in ("LICENSE", "LICENSE-CONTENT.md", "NOTICE", "CITATION.cff"):
            with self.subTest(rel=rel):
                self.assertTrue((REPO / rel).exists(), rel)
        self.assertIn("Apache License", (REPO / "LICENSE").read_text(encoding="utf-8"))
        notice = (REPO / "NOTICE").read_text(encoding="utf-8")
        for trecho in ("Rodrigo Dobbin Fellows", "CARVALHO, Diego Marques", "WCAG", "Jesse Vincent"):
            self.assertIn(trecho, notice)
        import yaml
        cff = yaml.safe_load((REPO / "CITATION.cff").read_text(encoding="utf-8"))
        self.assertEqual(str(cff["version"]), vygolint_catalog.__version__)
        self.assertEqual(cff["authors"][0]["family-names"], "Fellows")
        self.assertEqual(cff["references"][0]["authors"][0]["family-names"], "Carvalho")
        for rel in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json", ".cursor-plugin/plugin.json", ".kimi-plugin/plugin.json"):
            with self.subTest(rel=rel):
                m = _json(rel)
                self.assertEqual(m["author"]["name"], "Rodrigo Dobbin Fellows")
                self.assertEqual(m["license"], "Apache-2.0 AND CC-BY-4.0")
                self.assertNotIn("wcag", m["keywords"])
                self.assertTrue(m["description"].startswith("Conformance evaluation of educational games against 43"))

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

    def test_session_start_injects_plugin_root(self):
        env = {k: v for k, v in os.environ.items() if k not in ("CLAUDE_PLUGIN_ROOT", "CURSOR_PLUGIN_ROOT", "COPILOT_CLI")}
        out = subprocess.run(
            ["bash", "hooks/run-hook.cmd", "session-start"], cwd=REPO, env=env, capture_output=True, text=True, check=True
        )
        contexto = json.loads(out.stdout)["additionalContext"]
        self.assertIn(f"VYGOLINT_ROOT={REPO}", contexto)
        for chave in ("VYGOLINT_PYTHON=", "VYGOLINT_FFMPEG=", "VYGOLINT_TRANSCRITOR="):
            self.assertIn(chave, contexto)

    def test_session_start_finds_a_python_with_yaml(self):
        import shutil
        import stat
        import sys
        import tempfile

        from pathlib import Path

        tmp = Path(tempfile.mkdtemp())
        try:
            # a copy of the plugin without .venv, and a PATH whose python3 is the test interpreter (has PyYAML)
            copia = tmp / "plugin"
            (copia / "hooks").mkdir(parents=True)
            (copia / "skills" / "using-vygolint").mkdir(parents=True)
            for nome in ("run-hook.cmd", "session-start"):
                shutil.copy(REPO / "hooks" / nome, copia / "hooks" / nome)
            shutil.copy(REPO / "skills" / "using-vygolint" / "SKILL.md", copia / "skills" / "using-vygolint" / "SKILL.md")
            caminho = tmp / "bin"
            caminho.mkdir()
            envoltorio = caminho / "python3"
            envoltorio.write_text(f'#!/bin/sh\nexec "{sys.executable}" "$@"\n', encoding="utf-8")
            envoltorio.chmod(envoltorio.stat().st_mode | stat.S_IEXEC)
            env = {"PATH": f"{caminho}:/usr/bin:/bin", "HOME": os.environ.get("HOME", "/")}
            out = subprocess.run(["bash", str(copia / "hooks" / "run-hook.cmd"), "session-start"], env=env,
                                 capture_output=True, text=True, check=True)
            contexto = json.loads(out.stdout)["additionalContext"]
            self.assertIn(f"VYGOLINT_PYTHON={envoltorio}", contexto)
            # python3 and python without PyYAML, and no .venv: the line says so and tells the agent to ask, not to install
            # (both are shadowed: CI runners ship a /usr/bin/python that imports yaml)
            for nome in ("python3", "python"):
                falso = caminho / nome
                falso.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
                falso.chmod(falso.stat().st_mode | stat.S_IEXEC)
            out = subprocess.run(["bash", str(copia / "hooks" / "run-hook.cmd"), "session-start"], env=env,
                                 capture_output=True, text=True, check=True)
            contexto = json.loads(out.stdout)["additionalContext"]
            self.assertIn("VYGOLINT_PYTHON= (nenhum interpretador com PyYAML", contexto)
            self.assertIn("não instale por conta própria", contexto)
        finally:
            shutil.rmtree(tmp)

    def test_bootstrap_sources_inject_plugin_root(self):
        for rel in (".opencode/plugins/vygolint.js", ".pi/extensions/vygolint.ts", "hooks/session-start"):
            with self.subTest(rel=rel):
                self.assertIn("VYGOLINT_ROOT=", (REPO / rel).read_text(encoding="utf-8"))
