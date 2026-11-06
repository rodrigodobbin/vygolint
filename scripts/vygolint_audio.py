#!/usr/bin/env python3
"""Write registro_audio_<nome>.yaml for a gameplay video: stretches with sound and, with --transcricao, what is said."""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vygolint_catalog.audio import (  # noqa: E402
    falas_de_transcricao, montar_registro, parse_silencios, parse_volume, render_registro,
)


def _rodar(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", help="arquivo de vídeo, com o caminho como está em contexto.artefatos")
    parser.add_argument("--out", default="vygolint-out", help="pasta de saída (padrão: vygolint-out)")
    parser.add_argument("--nome", default=None, help="sufixo do arquivo de saída (padrão: nome do vídeo sem extensão)")
    parser.add_argument("--limiar", type=float, default=-50.0, help="nível, em dB, abaixo do qual é silêncio (padrão: -50)")
    parser.add_argument("--transcricao", default=None, help="JSON de um reconhecedor de fala (whisper ou whisper.cpp)")
    parser.add_argument("--transcritor", default=None, help="nome e modelo do reconhecedor, para constar no registro")
    args = parser.parse_args(argv)

    ffmpeg, ffprobe = shutil.which("ffmpeg"), shutil.which("ffprobe")
    if not ffmpeg or not ffprobe:
        print("ffmpeg e ffprobe são necessários para medir o áudio.", file=sys.stderr)
        return 1
    video = Path(args.video)
    if not video.is_file():
        print(f"{video}: arquivo não encontrado", file=sys.stderr)
        return 1
    r = _rodar([ffprobe, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video)])
    try:
        duracao = float(r.stdout.strip())
    except ValueError:
        print(f"{video}: não foi possível ler a duração: {r.stderr.strip()[-200:]}", file=sys.stderr)
        return 1
    r = _rodar([ffprobe, "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", str(video)])
    tem_faixa = bool(r.stdout.strip())
    volume, silencios = (None, None), []
    if tem_faixa:
        filtro = f"volumedetect,silencedetect=noise={args.limiar}dB:d=1"
        r = _rodar([ffmpeg, "-hide_banner", "-i", str(video), "-vn", "-af", filtro, "-f", "null", "-"])
        if r.returncode != 0:
            print(f"{video}: ffmpeg falhou ao medir o áudio: {r.stderr.strip()[-300:]}", file=sys.stderr)
            return 1
        volume = parse_volume(r.stderr)
        silencios = parse_silencios(r.stderr, duracao)
    falas = None
    if args.transcricao:
        try:
            falas = falas_de_transcricao(json.loads(Path(args.transcricao).read_text(encoding="utf-8")))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            print(f"{args.transcricao}: transcrição ilegível: {exc}", file=sys.stderr)
            return 1
    doc = montar_registro(args.video, duracao, tem_faixa, volume, silencios, args.limiar, falas, args.transcritor)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    alvo = out / f"registro_audio_{args.nome or video.stem}.yaml"
    alvo.write_text(render_registro(doc), encoding="utf-8")
    resumo = f"{len(doc['trechos_com_som'])} trecho(s) com som"
    if falas is not None:
        resumo += f", {len(doc['falas'])} fala(s)"
    elif tem_faixa:
        resumo += ", sem transcrição"
    else:
        resumo = "sem faixa de áudio"
    print(f"OK: {alvo} ({resumo})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
