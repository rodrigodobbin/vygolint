#!/usr/bin/env python3
"""Write the criterion entries graded in parts (one YAML file per category or per sitting) into avaliacao.yaml."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vygolint_catalog.catalog import load_catalog  # noqa: E402
from vygolint_catalog.merge import injetar, ler_partes  # noqa: E402
from vygolint_catalog.scaffold import PLACEHOLDER  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("avaliacao", help="caminho de avaliacao.yaml (gerado por vygolint_scaffold.py)")
    parser.add_argument("--partes", default=None, help="pasta com um .yaml por parte (padrão: <pasta do avaliacao>/partes)")
    parser.add_argument("--catalog", default=str(REPO / "catalog"))
    args = parser.parse_args(argv)

    alvo = Path(args.avaliacao)
    pasta = Path(args.partes) if args.partes else alvo.resolve().parent / "partes"
    catalog, errors = load_catalog(args.catalog)
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    if not alvo.is_file():
        print(f"{alvo}: arquivo não encontrado; gere o esqueleto com vygolint_scaffold.py", file=sys.stderr)
        return 1
    arquivos = sorted(pasta.glob("*.yaml")) if pasta.is_dir() else []
    if not arquivos:
        print(f"{pasta}: nenhuma parte (.yaml) encontrada", file=sys.stderr)
        return 1
    partes = {a.stem: a.read_text(encoding="utf-8") for a in arquivos}
    entradas, erros, notas = ler_partes(partes, catalog)
    texto, fora = injetar(alvo.read_text(encoding="utf-8"), entradas)
    erros += [f"{cid}: id não está em {alvo.name}; gere o esqueleto com vygolint_scaffold.py" for cid in fora]
    for n in notas:
        print(f"nota {n}", file=sys.stderr)
    if erros:
        for e in erros:
            print(e, file=sys.stderr)
        print(f"{len(erros)} erro(s). {alvo.name} não foi alterado.", file=sys.stderr)
        return 1
    alvo.write_text(texto, encoding="utf-8")
    pendentes = [c for c in sorted(catalog["criterios"]) if c not in entradas]
    resto = texto.count(f'razao: "{PLACEHOLDER}"') + texto.count(f"razao: {PLACEHOLDER}")
    print(
        f"OK: {len(entradas)} entrada(s) de {len(arquivos)} parte(s) gravadas em {alvo}; "
        f"{len(pendentes)} critério(s) sem parte" + (f" ({resto} ainda {PLACEHOLDER})" if resto else "")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
