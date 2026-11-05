#!/usr/bin/env python3
"""Validate an avaliacao.yaml against the vygolint catalog and write relatorio.md, relatorio.html and resultado.yaml."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vygolint_catalog.report import build_report, load_avaliacao  # noqa: E402
from vygolint_catalog.catalog import load_catalog  # noqa: E402
from vygolint_catalog.report import aggregate  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("avaliacao", help="caminho de avaliacao.yaml")
    parser.add_argument("--catalog", default=str(REPO / "catalog"))
    parser.add_argument("--out", default=None, help="pasta de saída (padrão: pasta do avaliacao.yaml)")
    parser.add_argument("--strict", action="store_true", help="trata avisos do lint de provas como erro")
    args = parser.parse_args(argv)
    out = Path(args.out) if args.out else Path(args.avaliacao).resolve().parent
    avisos = []
    errors = build_report(args.avaliacao, args.catalog, out, strict=args.strict, warnings=avisos)
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        motivo = " (--strict: avisos contam como erro)" if args.strict and errors == avisos else ""
        print(f"{len(errors)} erro(s){motivo}. Nada foi gerado.", file=sys.stderr)
        return 1
    for a in avisos:
        print(a, file=sys.stderr)
    catalog, _ = load_catalog(args.catalog)
    nivel = aggregate(load_avaliacao(args.avaliacao), catalog)["nivel"]
    sufixo = f" ({len(avisos)} aviso{'s' if len(avisos) != 1 else ''})" if avisos else ""
    print(f"OK: nível {nivel} -> {out}/relatorio.md, {out}/relatorio.html, {out}/resultado.yaml{sufixo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
