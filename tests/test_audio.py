import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from helpers import REPO
from vygolint_catalog.audio import (
    falas_de_transcricao, hms, montar_registro, parse_silencios, parse_volume, render_registro, trechos_com_som,
)

# ffmpeg output for a real 115 s recording (volumedetect + silencedetect=noise=-50dB:d=1)
STDERR = """
[silencedetect @ 0x1] silence_start: 0
[silencedetect @ 0x1] silence_end: 31.033333 | silence_duration: 31.033333
[silencedetect @ 0x1] silence_start: 38.71625
[silencedetect @ 0x1] silence_end: 60.16875 | silence_duration: 21.4525
[silencedetect @ 0x1] silence_start: 79.001375
[silencedetect @ 0x1] silence_end: 83.328979 | silence_duration: 4.327604
[Parsed_volumedetect_0 @ 0x2] n_samples: 11063232
[Parsed_volumedetect_0 @ 0x2] mean_volume: -51.2 dB
[Parsed_volumedetect_0 @ 0x2] max_volume: -29.5 dB
"""


class ParseTest(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(parse_volume(STDERR), (-51.2, -29.5))
        self.assertEqual(parse_volume("mean_volume: -inf dB\nmax_volume: -inf dB"), (None, None))
        self.assertEqual(parse_volume("nada"), (None, None))

    def test_silences_and_open_tail(self):
        self.assertEqual(parse_silencios(STDERR, 115.242), [(0.0, 31.033333), (38.71625, 60.16875), (79.001375, 83.328979)])
        aberto = "silence_start: 10\nsilence_end: 12.5\nsilence_start: 100.25\n"
        self.assertEqual(parse_silencios(aberto, 115.0), [(10.0, 12.5), (100.25, 115.0)])
        self.assertEqual(parse_silencios("silence_start: -0.01\nsilence_end: 3\n", 5.0), [(0.0, 3.0)])
        self.assertEqual(parse_silencios("", 5.0), [])

    def test_sound_is_the_complement_rounded_outward(self):
        sil = parse_silencios(STDERR, 115.242)
        self.assertEqual(trechos_com_som(sil, 115.242), [(31, 39), (60, 80), (83, 115)])
        self.assertEqual(trechos_com_som([], 10.0), [(0, 10)])
        self.assertEqual(trechos_com_som([(0.0, 10.0)], 10.0), [])
        # blips 0.2 s apart from each other after rounding touch and merge
        self.assertEqual(trechos_com_som([(0.0, 3.2), (3.4, 4.1), (4.3, 9.0)], 9.0), [(3, 5)])

    def test_hms(self):
        self.assertEqual([hms(0), hms(59.9), hms(3725)], ["00:00:00", "00:00:59", "01:02:05"])


class TranscricaoTest(unittest.TestCase):
    def test_whisper_layout(self):
        doc = {"text": "x", "segments": [
            {"start": 19.2, "end": 22.9, "text": " A skua pode atacar. "},
            {"start": 1.0, "end": 2.0, "text": "   "},
            {"start": 3.5, "end": 5.0, "text": "Busque alimento."},
        ]}
        self.assertEqual(falas_de_transcricao(doc), [(3.5, 5.0, "Busque alimento."), (19.2, 22.9, "A skua pode atacar.")])

    def test_whisper_cpp_layout(self):
        doc = {"transcription": [{"timestamps": {"from": "00:00:03,500", "to": "00:00:05,000"},
                                  "offsets": {"from": 3500, "to": 5000}, "text": " Busque alimento."}]}
        self.assertEqual(falas_de_transcricao(doc), [(3.5, 5.0, "Busque alimento.")])

    def test_unknown_layout(self):
        for ruim in ([], {"words": []}, "texto"):
            with self.assertRaises(ValueError):
                falas_de_transcricao(ruim)


class RegistroTest(unittest.TestCase):
    def test_without_transcript(self):
        doc = montar_registro("gameplay/file.mp4", 115.242, True, (-51.2, -29.5), parse_silencios(STDERR, 115.242), -50.0)
        self.assertEqual(doc, {
            "video": "gameplay/file.mp4", "duracao": "00:01:55", "faixa_de_audio": True,
            "volume_medio_db": -51.2, "volume_maximo_db": -29.5, "limiar_silencio_db": -50.0,
            "trechos_com_som": [{"t": "00:00:31", "fim": "00:00:39"}, {"t": "00:01:00", "fim": "00:01:20"}, {"t": "00:01:23", "fim": "00:01:55"}],
            "transcricao": "nao_disponivel",
        })

    def test_with_transcript_and_without_track(self):
        doc = montar_registro("v.mp4", 10.4, True, (-20.0, -3.0), [], -50.0, falas=[(3.5, 5.2, "Olá")], transcritor="whisper small")
        self.assertEqual(doc["transcricao"], "whisper small")
        self.assertEqual(doc["falas"], [{"t": "00:00:03", "fim": "00:00:06", "texto": "Olá"}])
        fim = montar_registro("v.mp4", 10.4, True, (-20.0, -3.0), [(0.0, 10.2)], -50.0, falas=[(9.9, 10.4, "Fim")])
        self.assertEqual(fim["trechos_com_som"], [{"t": "00:00:10", "fim": "00:00:10"}])
        self.assertEqual(fim["falas"], [{"t": "00:00:09", "fim": "00:00:10", "texto": "Fim"}])

    def test_rendered_times_are_quoted(self):
        doc = montar_registro("v.mp4", 36001.0, True, (-20.0, -3.0), [(0.0, 36000.0)], -50.0, falas=[(36000.2, 36000.9, "Olá: tudo bem?")])
        texto = render_registro(doc)
        self.assertTrue(texto.startswith("# ARQUIVO GERADO"))
        for linha in ('duracao: "10:00:01"', '- t: "10:00:00"', '  fim: "10:00:01"'):
            self.assertIn(linha, texto)
        self.assertNotRegex(texto, r"(?m)^\s*(?:- )?(?:t|fim|duracao): \d")
        self.assertEqual(yaml.safe_load(texto), doc)
        self.assertEqual(montar_registro("v.mp4", 10.4, True, (None, None), [], -50.0, falas=[])["falas"], [])
        mudo = montar_registro("v.mp4", 10.4, False, (None, None), [], -50.0)
        self.assertEqual(mudo, {"video": "v.mp4", "duracao": "00:00:10", "faixa_de_audio": False,
                                "trechos_com_som": [], "transcricao": "sem_faixa_de_audio"})


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg não instalado")
class CliTest(unittest.TestCase):
    """End to end on synthetic media: 2 s of silence, 2 s of tone, 2 s of silence."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.cmd = [sys.executable, str(REPO / "scripts" / "vygolint_audio.py")]

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def _midia(self, nome, com_audio=True):
        alvo = self.tmp / nome
        cmd = ["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "color=c=black:s=64x64:d=6:r=5"]
        if com_audio:
            cmd += ["-f", "lavfi", "-i", "aevalsrc='if(between(t,2,4),0.5*sin(2*PI*440*t),0)':d=6:s=16000", "-c:a", "aac"]
        r = subprocess.run(cmd + ["-c:v", "mpeg4", str(alvo)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        return alvo

    def test_sound_map(self):
        video = self._midia("s.mp4")
        r = subprocess.run(self.cmd + [str(video), "--out", str(self.tmp / "o")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        texto = (self.tmp / "o" / "registro_audio_s.yaml").read_text(encoding="utf-8")
        self.assertTrue(texto.startswith("# ARQUIVO GERADO"))
        doc = yaml.safe_load(texto)
        self.assertTrue(doc["faixa_de_audio"])
        self.assertEqual(doc["trechos_com_som"], [{"t": "00:00:02", "fim": "00:00:04"}])
        self.assertEqual(doc["transcricao"], "nao_disponivel")
        self.assertIn("sem transcrição", r.stdout)

    def test_transcript_is_merged(self):
        video = self._midia("s.mp4")
        tr = self.tmp / "t.json"
        tr.write_text(json.dumps({"segments": [{"start": 2.1, "end": 3.8, "text": " Tom de teste "}]}), encoding="utf-8")
        r = subprocess.run(self.cmd + [str(video), "--out", str(self.tmp / "o"), "--nome", "x", "--transcricao", str(tr),
                                       "--transcritor", "whisper small"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        doc = yaml.safe_load((self.tmp / "o" / "registro_audio_x.yaml").read_text(encoding="utf-8"))
        self.assertEqual(doc["falas"], [{"t": "00:00:02", "fim": "00:00:04", "texto": "Tom de teste"}])
        self.assertEqual(doc["transcricao"], "whisper small")

    def test_no_audio_track_and_errors(self):
        video = self._midia("mudo.mp4", com_audio=False)
        r = subprocess.run(self.cmd + [str(video), "--out", str(self.tmp / "o")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        doc = yaml.safe_load((self.tmp / "o" / "registro_audio_mudo.yaml").read_text(encoding="utf-8"))
        self.assertEqual((doc["faixa_de_audio"], doc["transcricao"]), (False, "sem_faixa_de_audio"))
        r = subprocess.run(self.cmd + [str(self.tmp / "nao.mp4")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        ruim = self.tmp / "ruim.json"
        ruim.write_text("{", encoding="utf-8")
        r = subprocess.run(self.cmd + [str(video), "--transcricao", str(ruim), "--out", str(self.tmp / "o")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertIn("ilegível", r.stderr)
