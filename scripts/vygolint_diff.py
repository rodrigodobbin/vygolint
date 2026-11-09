#!/usr/bin/env python3
"""Compare two resultado.yaml files written by vygolint_report.py and list which criteria changed grade."""

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vygolint_catalog.diff import comparar, render_diff, resumo  # noqa: E402


def _carregar(caminho):
    p = Path(caminho)
    try:
        doc = yaml.safe_load(p.read_text(encoding="utf-8"))
    except OSError as exc:
        return None, f"{p}: não foi possível ler o arquivo: {exc}"
    except yaml.YAMLError as exc:
        return None, f"{p}: YAML inválido: {exc}"
    if not isinstance(doc, dict) or not isinstance(doc.get("criterios"), dict):
        return None, f"{p}: não é um resultado.yaml (falta o mapa `criterios`)"
    return doc, None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("antes", help="resultado.yaml da avaliação anterior")
    parser.add_argument("depois", help="resultado.yaml da avaliação nova")
    parser.add_argument("--out", default=None, help="grava a comparação em Markdown neste arquivo (além de imprimir o resumo)")
    args = parser.parse_args(argv)

    antes, e1 = _carregar(args.antes)
    depois, e2 = _carregar(args.depois)
    erros = [e for e in (e1, e2) if e]
    if erros:
        for e in erros:
            print(e, file=sys.stderr)
        return 1
    d = comparar(antes, depois)
    for a in d["avisos"]:
        print(f"aviso: {a}", file=sys.stderr)
    texto = render_diff(d)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(texto, encoding="utf-8")
        print(f"OK: nível {d['nivel'][0]} → {d['nivel'][1]}; {resumo(d)}. Comparação em {out}")
    else:
        print(texto, end="")
        print(f"OK: nível {d['nivel'][0]} → {d['nivel'][1]}; {resumo(d)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
