"""Describe the audio track of a gameplay video: where there is sound and, when a transcript is given, what is said.

The video skill reads frames, so by itself it cannot tell whether a caption is also spoken or whether
an error plays a sound. This module turns ffmpeg's measurements into `registro_audio_<nome>.yaml`:

- whether the file has an audio track, its mean and peak level;
- the stretches with sound (the complement of what `silencedetect` reports);
- the spoken segments, when a transcript produced by a speech recognizer is passed in.

Parsing, assembly and rendering are pure functions; the CLI (scripts/vygolint_audio.py) runs ffmpeg.
"""

import math
import re

import yaml

GENERATED = "# ARQUIVO GERADO por scripts/vygolint_audio.py. Não edite à mão; rode o script de novo."
_VOLUME = re.compile(r"(mean|max)_volume:\s*(-?\d+(?:\.\d+)?|-inf) dB")
_SILENCIO = re.compile(r"silence_(start|end):\s*(-?\d+(?:\.\d+)?)")


def hms(segundos):
    s = max(0, int(segundos))
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def parse_volume(stderr):
    """(mean dB, peak dB) from `volumedetect` output; None for a value that is missing or -inf."""
    achados = {}
    for nome, valor in _VOLUME.findall(stderr):
        achados[nome] = None if valor == "-inf" else float(valor)
    return achados.get("mean"), achados.get("max")


def parse_silencios(stderr, duracao):
    """[(start, end)] in seconds from `silencedetect` output; a silence still open at the end runs to `duracao`."""
    silencios, inicio = [], None
    for tipo, valor in _SILENCIO.findall(stderr):
        t = max(0.0, float(valor))
        if tipo == "start":
            inicio = t
        elif inicio is not None:
            silencios.append((inicio, min(t, duracao)))
            inicio = None
    if inicio is not None:
        silencios.append((inicio, duracao))
    return silencios


def trechos_com_som(silencios, duracao):
    """Stretches with sound as [(t, fim)] in whole seconds: the complement of the silences, rounded outward and merged."""
    trechos, cursor = [], 0.0
    for ini, fim in sorted(silencios):
        if ini > cursor:
            trechos.append((cursor, ini))
        cursor = max(cursor, fim)
    if cursor < duracao:
        trechos.append((cursor, duracao))
    teto = math.floor(duracao)  # the last instant hms() can name, so no stretch ends past `duracao`
    unidos = []
    for ini, fim in trechos:
        if fim - ini <= 0:
            continue
        a = min(math.floor(ini), teto)
        b = max(a, min(teto, math.ceil(fim)))
        if unidos and a <= unidos[-1][1]:
            unidos[-1] = (unidos[-1][0], max(unidos[-1][1], b))
        else:
            unidos.append((a, b))
    return unidos


def falas_de_transcricao(doc):
    """Spoken segments as [(start s, end s, text)] from a recognizer's JSON.

    Two layouts are accepted: `segments: [{start, end, text}]` in seconds (openai-whisper,
    faster-whisper, mlx-whisper) and `transcription: [{offsets: {from, to}, text}]` in milliseconds
    (whisper.cpp). Anything else raises ValueError.
    """
    if not isinstance(doc, dict):
        raise ValueError("transcrição deve ser um objeto JSON")
    falas = []
    if isinstance(doc.get("segments"), list):
        for seg in doc["segments"]:
            if isinstance(seg, dict) and isinstance(seg.get("text"), str) and seg["text"].strip():
                falas.append((float(seg["start"]), float(seg["end"]), seg["text"].strip()))
    elif isinstance(doc.get("transcription"), list):
        for seg in doc["transcription"]:
            off = seg.get("offsets") if isinstance(seg, dict) else None
            if isinstance(off, dict) and isinstance(seg.get("text"), str) and seg["text"].strip():
                falas.append((float(off["from"]) / 1000, float(off["to"]) / 1000, seg["text"].strip()))
    else:
        raise ValueError("transcrição sem `segments` nem `transcription`")
    return sorted(falas)


def montar_registro(video, duracao, tem_faixa, volume, silencios, limiar_db, falas=None, transcritor=None):
    """The document written to registro_audio_<nome>.yaml."""
    medio, maximo = volume
    doc = {
        "video": video,
        "duracao": hms(duracao),
        "faixa_de_audio": bool(tem_faixa),
    }
    if not tem_faixa:
        doc["trechos_com_som"] = []
        doc["transcricao"] = "sem_faixa_de_audio"
        return doc
    doc["volume_medio_db"] = medio
    doc["volume_maximo_db"] = maximo
    doc["limiar_silencio_db"] = limiar_db
    doc["trechos_com_som"] = [{"t": hms(a), "fim": hms(b)} for a, b in trechos_com_som(silencios, duracao)]
    if falas is None:
        doc["transcricao"] = "nao_disponivel"
    else:
        doc["transcricao"] = transcritor or "transcritor não informado"
        doc["falas"] = [
            {"t": hms(math.floor(a)), "fim": hms(min(math.floor(duracao), math.ceil(b))), "texto": texto}
            for a, b, texto in falas
        ]
    return doc


_TEMPO_SEM_ASPAS = re.compile(r"^(\s*(?:- )?(?:t|fim|duracao): )'?(\d{2}:\d{2}:\d{2})'?$", re.M)


def render_registro(doc):
    """YAML text of the registro with every time double-quoted, like in registro_video.yaml.

    PyYAML leaves 00:01:55 bare and single-quotes 10:00:00 (a number in YAML 1.1); one form is easier to read and grep.
    """
    texto = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False)
    return GENERATED + "\n" + _TEMPO_SEM_ASPAS.sub(r'\1"\2"', texto)
