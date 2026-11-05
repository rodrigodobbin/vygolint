import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

from helpers import REPO, avaliacao_valida
from vygolint_catalog import lint
from vygolint_catalog.lint import lint_avaliacao
from vygolint_catalog.report import build_report


def _av(criterios, **cabecalho):
    av = {
        "jogo": "Jogo", "avaliador": "teste", "data": "2026-11-05",
        "contexto": {"sala_de_aula": False, "fontes": ["codigo", "documentacao", "video"], "artefatos": {}},
        "criterios": criterios,
    }
    av.update(cabecalho)
    return av


def _fonte(nome, *provas):
    return {"grau": "atendido", "fontes": {nome: {"grau": "atendido", "provas": list(provas)}}}


class LintTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "src").mkdir()
        (self.tmp / "src" / "a.py").write_text("um\ndois\ntres\n", encoding="utf-8")
        (self.tmp / "gameplay").mkdir()
        (self.tmp / "gameplay" / "v.mp4").write_bytes(b"\x00")
        (self.tmp / "docs").mkdir()
        (self.tmp / "docs" / "gdd.md").write_text("# GDD\n", encoding="utf-8")

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp)

    def lint(self, criterios, duracao=lambda p: 100.0, **cab):
        return lint_avaliacao(_av(criterios, **cab), [self.tmp], duracao=duracao)

    def test_clean_evaluation_has_no_warnings(self):
        avisos = self.lint({
            "D01.1": _fonte("codigo", "src/a.py:3 — trecho", "src/a.py:1-2 — outro"),
            "D02.1": _fonte("documentacao", "docs/gdd.md p. 1 — trecho", "docs/gdd.md, seção 2 — trecho"),
            "D03.1": _fonte("video", "gameplay/v.mp4 00:00:10 — x", "gameplay/v.mp4 00:00:31-00:00:44, 00:01:00-00:01:04 — y",
                            "gameplay/v.mp4 00:00:44 e 00:01:04 — z"),
            "D04.1": {"grau": "nao_avaliado", "razao": "sem fonte"},
        })
        self.assertEqual(avisos, [])

    def test_missing_file_is_reported_once_per_file(self):
        avisos = self.lint({
            "D01.1": _fonte("codigo", "src/nao.py:1 — x", "src/nao.py:2 — y"),
            "D02.1": _fonte("codigo", "src/nao.py:9 — z"),
        })
        self.assertEqual(len(avisos), 1)
        self.assertIn("src/nao.py", avisos[0])
        self.assertIn("3 provas", avisos[0])
        self.assertIn("D01.1", avisos[0])
        self.assertIn("D02.1", avisos[0])

    def test_code_line_checks(self):
        avisos = self.lint({"D01.1": _fonte("codigo", "src/a.py:4 — além do fim", "src/a.py — sem linha", "src/a.py:3-2 — invertido")})
        self.assertEqual(len(avisos), 3)
        self.assertTrue(all(a.startswith("aviso D01.1: fonte codigo: prova ") for a in avisos))
        self.assertIn("linha 4", avisos[0])
        self.assertIn("3 linhas", avisos[0])
        self.assertIn("arquivo:linha", avisos[1])
        self.assertIn("3-2", avisos[2])

    def test_documentation_place(self):
        avisos = self.lint({"D02.1": _fonte("documentacao", "docs/gdd.md — sem página")})
        self.assertEqual(len(avisos), 1)
        self.assertIn("p. N", avisos[0])

    def test_video_timestamps(self):
        avisos = self.lint({"D03.1": _fonte(
            "video",
            "gameplay/v.mp4 00:00:61 — segundo inválido",
            "gameplay/v.mp4 00:00:50-00:00:40 — fim antes do início",
            "gameplay/v.mp4 00:02:00 — depois do fim",
            "gameplay/v.mp4 — sem tempo",
        )})
        self.assertEqual(len(avisos), 4)
        self.assertIn("00:00:61", avisos[0])
        self.assertIn("00:00:50-00:00:40", avisos[1])
        self.assertIn("00:02:00", avisos[2])
        self.assertIn("00:01:40", avisos[2])
        self.assertIn("hh:mm:ss", avisos[3])

    def test_unknown_duration_skips_the_end_check(self):
        self.assertEqual(self.lint({"D03.1": _fonte("video", "gameplay/v.mp4 09:00:00 — x")}, duracao=lambda p: None), [])

    def test_placeholders(self):
        avisos = self.lint(
            {"D04.1": {"grau": "nao_avaliado", "razao": "PREENCHER"}},
            avaliador="PREENCHER (harness e modelo) com vygolint 0.2.0",
        )
        self.assertEqual(len(avisos), 2)
        self.assertTrue(any(a.startswith("aviso avaliacao: avaliador") for a in avisos))
        self.assertTrue(any(a.startswith("aviso D04.1: razao") for a in avisos))

    def test_tolerates_malformed_entries(self):
        av = _av({"D01.1": "texto", "D02.1": {"grau": "atendido", "fontes": {"codigo": {"provas": [5, None]}}}, "D03.1": {"grau": "atendido"}})
        self.assertEqual(lint_avaliacao(av, [self.tmp], duracao=lambda p: None), [])
        self.assertEqual(lint_avaliacao("x", [self.tmp]), [])

    def test_ffprobe_missing_or_failing_gives_no_duration(self):
        with mock.patch.object(lint.shutil, "which", return_value=None):
            self.assertIsNone(lint.duracao_ffprobe(self.tmp / "gameplay" / "v.mp4"))
        with mock.patch.object(lint.shutil, "which", return_value="/bin/false"):
            self.assertIsNone(lint.duracao_ffprobe(self.tmp / "gameplay" / "v.mp4"))


class BuildReportLintTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.av = self.tmp / "avaliacao.yaml"
        self.av.write_text(yaml.safe_dump(avaliacao_valida(), allow_unicode=True, sort_keys=False), encoding="utf-8")

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp)

    def test_warnings_do_not_block_the_report(self):
        avisos = []
        self.assertEqual(build_report(self.av, REPO / "catalog", self.tmp, warnings=avisos), [])
        self.assertTrue(avisos)
        self.assertTrue(all(a.startswith("aviso") for a in avisos))
        self.assertTrue((self.tmp / "relatorio.md").exists())

    def test_strict_turns_warnings_into_errors(self):
        erros = build_report(self.av, REPO / "catalog", self.tmp, strict=True)
        self.assertTrue(erros)
        self.assertFalse((self.tmp / "relatorio.md").exists())
        self.assertFalse((self.tmp / "relatorio.html").exists())

    def test_cli_prints_warnings_and_strict_fails(self):
        import subprocess
        import sys

        cmd = [sys.executable, str(REPO / "scripts" / "vygolint_report.py"), str(self.av)]
        ok = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertIn("aviso", ok.stderr)
        self.assertRegex(ok.stdout, r"OK: nível AAA .*\(\d+ avisos?\)")
        bad = subprocess.run(cmd + ["--strict"], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertIn("aviso", bad.stderr)


class EscopoTest(unittest.TestCase):
    """Artefatos are files or folders; a folder puts every file inside it in scope."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        for rel, conteudo in (
            ("src/a.py", "um\ndois\n"), ("src/sub/b.py", "x\n"), ("outro/c.py", "x\n"),
            ("docs/gdd.md", "# GDD\n"), ("docs/press.md", "divulgação\n"), ("docs/extra.pdf", "%PDF"),
            ("docs/capa.png", "png"), ("docs/.oculto.md", "x"), ("README.md", "leia\n"),
            ("gameplay/s1.mp4", "v"), ("gameplay/s2.mp4", "v"), ("gameplay/s3.mov", "v"), ("gameplay/notas.txt", "t"),
        ):
            p = self.tmp / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(conteudo, encoding="utf-8")
        self.out = self.tmp / "vygolint-out"
        self.out.mkdir()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp)

    def lint(self, criterios, artefatos, pasta=True):
        av = _av(criterios)
        av["contexto"]["artefatos"] = artefatos
        return lint_avaliacao(av, [self.tmp], duracao=lambda p: None, pasta=self.out if pasta else None)

    def test_proof_inside_declared_folder_or_file_passes(self):
        avisos = self.lint(
            {
                "D01.1": _fonte("codigo", "src/a.py:1 — x", "src/sub/b.py:1 — y"),
                "D02.1": _fonte("documentacao", "README.md p. 1 — z"),
            },
            {"codigo": ["./src"], "documentacao": ["README.md"]},
        )
        self.assertEqual(avisos, [])

    def test_proof_outside_the_declared_scope_is_reported_once_per_file(self):
        avisos = self.lint(
            {
                "D01.1": _fonte("codigo", "outro/c.py:1 — x", "src/a.py:1 — ok"),
                "D02.1": _fonte("codigo", "outro/c.py:1 — y"),
                "D03.1": _fonte("documentacao", "README.md p. 1 — z", "docs/gdd.md p. 1 — ok"),
            },
            {"codigo": ["src"], "documentacao": ["docs"]},
            pasta=False,
        )
        fora = [a for a in avisos if "fora dos artefatos" in a]
        self.assertEqual(len(fora), 2)
        self.assertIn("fora dos artefatos de codigo: outro/c.py (2 provas: D01.1, D02.1)", fora[0])
        self.assertIn("fora dos artefatos de documentacao: README.md (1 prova: D03.1)", fora[1])

    def test_missing_artefact_is_reported_and_disables_the_scope_check(self):
        avisos = self.lint({"D01.1": _fonte("codigo", "outro/c.py:1 — x")}, {"codigo": ["nao-existe", "src"]})
        self.assertEqual(avisos, ["aviso avaliacao: artefato de codigo não encontrado: nao-existe"])

    def test_video_coverage_needs_a_registro_or_a_proof(self):
        (self.out / "registro_video_s1.yaml").write_text('video: "gameplay/s1.mp4"\neventos: []\n', encoding="utf-8")
        (self.out / "registro_video_ruim.yaml").write_text("video: [", encoding="utf-8")
        avisos = self.lint({"D03.1": _fonte("video", "gameplay/s2.mp4 00:00:01 — x")}, {"video": ["gameplay"]})
        self.assertEqual(avisos, ["aviso avaliacao: vídeo do escopo sem registro_video nem prova: gameplay/s3.mov"])

    def test_document_coverage_needs_a_proof_or_the_inventory(self):
        (self.out / "inventario.md").write_text("Fontes lidas: docs/gdd.md\nNão conta: docs/press.md (divulgação)\n", encoding="utf-8")
        (self.out / "relatorio.html").write_text("<html>", encoding="utf-8")
        avisos = self.lint({"D04.1": {"grau": "nao_avaliado", "razao": "x"}}, {"documentacao": ["docs", "."]})
        self.assertEqual(sorted(avisos), [
            "aviso avaliacao: documento do escopo sem prova nem menção no inventario.md: README.md",
            "aviso avaliacao: documento do escopo sem prova nem menção no inventario.md: docs/extra.pdf",
            "aviso avaliacao: documento do escopo sem prova nem menção no inventario.md: gameplay/notas.txt",
        ])

    def test_code_has_no_per_file_coverage(self):
        self.assertEqual(self.lint({"D01.1": _fonte("codigo", "src/a.py:1 — x")}, {"codigo": ["src", "outro"]}), [])

    def test_scope_listing_for_the_scaffold(self):
        arquivos, ausentes = lint.arquivos_do_escopo("video", ["gameplay", "sumiu"], [self.tmp], excluir=[self.out])
        self.assertEqual([rotulo for _, rotulo in arquivos], ["gameplay/s1.mp4", "gameplay/s2.mp4", "gameplay/s3.mov"])
        self.assertEqual(ausentes, ["sumiu"])
        arquivos, _ = lint.arquivos_do_escopo("documentacao", ["gameplay/notas.txt", "docs/capa.png"], [self.tmp])
        self.assertEqual([rotulo for _, rotulo in arquivos], ["gameplay/notas.txt", "docs/capa.png"])
        self.assertEqual(lint.arquivos_do_escopo("codigo", ["src"], [self.tmp]), ([], []))

    def test_malformed_artefatos_do_not_raise(self):
        for artefatos in ("texto", {"video": "gameplay"}, {"video": [5, None]}, None):
            self.assertEqual(self.lint({"D04.1": {"grau": "nao_avaliado", "razao": "x"}}, artefatos), [])


class InventarioLintTest(EscopoTest):
    """inventario.md rows classify each document in scope; the lint reads the Classificação column."""

    TABELA = "## Fontes lidas\n\n### Documentação\n\n| Arquivo | Classificação | Motivo ou conteúdo |\n|---|---|---|\n"

    def _inventario(self, *linhas):
        (self.out / "inventario.md").write_text(self.TABELA + "\n".join(linhas) + "\n", encoding="utf-8")

    def test_classified_rows_cover_documents(self):
        self._inventario(
            "| `docs/gdd.md` | documento equivalente | GDD |",
            "| `docs/press.md` | não conta | material de divulgação |",
            "| `docs/extra.pdf` | não abriu | arquivo corrompido |",
        )
        self.assertEqual(self.lint({"D04.1": {"grau": "nao_avaliado", "razao": "x"}}, {"documentacao": ["docs"]}), [])

    def test_unclassified_row_does_not_cover_and_placeholders_are_counted(self):
        self._inventario(
            "| `docs/gdd.md` | documento equivalente | GDD |",
            "| `docs/press.md` | PREENCHER | |",
            "| `docs/extra.pdf` |  | |",
        )
        avisos = self.lint({"D04.1": {"grau": "nao_avaliado", "razao": "x"}}, {"documentacao": ["docs"]})
        self.assertEqual(sorted(avisos), [
            "aviso avaliacao: documento do escopo sem classificação no inventario.md: docs/extra.pdf",
            "aviso avaliacao: documento do escopo sem classificação no inventario.md: docs/press.md",
            "aviso inventario: ainda contém PREENCHER (1 ocorrência)",
        ])

    def test_proof_covers_an_unclassified_document(self):
        self._inventario("| `docs/gdd.md` |  | |", "| `docs/press.md` | não conta | divulgação |", "| `docs/extra.pdf` | não conta | vazio |")
        avisos = self.lint({"D02.1": _fonte("documentacao", "docs/gdd.md p. 1 — x")}, {"documentacao": ["docs"]})
        self.assertEqual(avisos, [])

    def test_proof_citing_a_document_that_does_not_count_is_reported(self):
        self._inventario(
            "| `docs/gdd.md` | documento equivalente | GDD |",
            "| `./docs/press.md` | Não conta | divulgação |",
            "| `docs/extra.pdf` | nao conta | vazio |",
        )
        avisos = self.lint(
            {
                "D02.1": _fonte("documentacao", "docs/press.md p. 1 — x", "docs/gdd.md p. 2 — ok"),
                "D03.1": _fonte("documentacao", "./docs/press.md, seção 2 — y", "docs/extra.pdf p. 1 — z"),
            },
            {"documentacao": ["docs"]},
        )
        self.assertEqual(avisos, [
            'aviso avaliacao: documento citado como prova mas classificado "não conta" no inventario.md: docs/press.md (2 provas: D02.1, D03.1)',
            'aviso avaliacao: documento citado como prova mas classificado "não conta" no inventario.md: docs/extra.pdf (1 prova: D03.1)',
        ])

    def test_free_text_mention_still_covers_when_there_is_no_row(self):
        (self.out / "inventario.md").write_text("Fontes lidas: docs/gdd.md, docs/press.md e docs/extra.pdf\n", encoding="utf-8")
        self.assertEqual(self.lint({"D04.1": {"grau": "nao_avaliado", "razao": "x"}}, {"documentacao": ["docs"]}), [])
        (self.out / "inventario.md").write_text("Fontes lidas: gdd.md\n", encoding="utf-8")
        avisos = self.lint({"D04.1": {"grau": "nao_avaliado", "razao": "x"}}, {"documentacao": ["docs/gdd.md"]})
        self.assertEqual(avisos, ["aviso avaliacao: documento do escopo sem prova nem menção no inventario.md: docs/gdd.md"])
