#!/usr/bin/env python3
"""Validate the vygolint catalog and regenerate docs/catalogo.md and docs/catalogo.tex."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vygolint_catalog.build import build, contagem  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", default=str(REPO / "catalog"))
    parser.add_argument("--docs", default=str(REPO / "docs"))
    args = parser.parse_args(argv)
    errors = build(args.catalog, args.docs)
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        print(f"{len(errors)} erro(s). Nada foi gerado.", file=sys.stderr)
        return 1
    n_d, n_c = contagem(args.catalog)
    print(f"OK: {n_d} diretrizes, {n_c} critérios -> {args.docs}/catalogo.md, {args.docs}/catalogo.tex")
    return 0


if __name__ == "__main__":
    sys.exit(main())
