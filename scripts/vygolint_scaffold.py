#!/usr/bin/env python3
"""Write the skeleton of avaliacao.yaml (header and one entry per catalog criterion) into the output folder."""

import argparse
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vygolint_catalog import __version__  # noqa: E402
from vygolint_catalog.catalog import load_catalog  # noqa: E402
from vygolint_catalog.report import FONTES  # noqa: E402
from vygolint_catalog.scaffold import PLACEHOLDER, render_scaffold  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def _bool(valor):
    v = valor.strip().lower()
    if v in ("true", "sim", "s", "1"):
        return True
    if v in ("false", "nao", "não", "n", "0"):
        return False
    raise argparse.ArgumentTypeError(f"use true ou false (recebido {valor!r})")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jogo", required=True, help="nome do jogo")
    parser.add_argument("--sala-de-aula", required=True, type=_bool, help="true se o jogo é aplicado em sala de aula")
    parser.add_argument("--fontes", required=True, help=f"fontes disponíveis, separadas por vírgula, dentro de {', '.join(FONTES)}")
    parser.add_argument("--artefato", action="append", default=[], metavar="fonte=caminho",
                        help="caminho de uma fonte; repita a opção para cada caminho")
    parser.add_argument("--avaliador", default=None, help="harness e modelo que avaliam (a versão do vygolint é acrescentada)")
    parser.add_argument("--data", default=None, help="AAAA-MM-DD (padrão: hoje)")
    parser.add_argument("--out", default="vygolint-out", help="pasta de saída (padrão: vygolint-out)")
    parser.add_argument("--catalog", default=str(REPO / "catalog"))
    parser.add_argument("--force", action="store_true", help="sobrescreve um avaliacao.yaml existente")
    args = parser.parse_args(argv)

    fontes = [f.strip() for f in args.fontes.split(",") if f.strip()]
    invalidas = [f for f in fontes if f not in FONTES]
    if not fontes or invalidas:
        parser.error(f"--fontes deve listar ao menos uma entre {', '.join(FONTES)} (inválidas: {', '.join(invalidas) or 'nenhuma informada'})")
    artefatos = {}
    for item in args.artefato:
        fonte, sep, caminho = item.partition("=")
        fonte, caminho = fonte.strip(), caminho.strip()
        if not sep or not fonte or not caminho:
            parser.error(f"--artefato deve ter a forma fonte=caminho (recebido {item!r})")
        if fonte not in fontes:
            parser.error(f"--artefato {item!r}: a fonte {fonte} não está em --fontes")
        artefatos.setdefault(fonte, []).append(caminho)
    faltam = [f for f in fontes if f not in artefatos]
    if faltam:
        parser.error(f"informe --artefato fonte=caminho para: {', '.join(faltam)}")

    catalog, errors = load_catalog(args.catalog)
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    out = Path(args.out)
    alvo = out / "avaliacao.yaml"
    if alvo.exists() and not args.force:
        print(f"{alvo} já existe; use --force para sobrescrever (o conteúdo atual será perdido).", file=sys.stderr)
        return 1
    avaliador = f"{args.avaliador or PLACEHOLDER + ' (harness e modelo)'} com vygolint {__version__}"
    data = args.data or datetime.date.today().isoformat()
    texto = render_scaffold(catalog, args.jogo, args.sala_de_aula, fontes, artefatos, avaliador, data)
    out.mkdir(parents=True, exist_ok=True)
    alvo.write_text(texto, encoding="utf-8")
    print(f"OK: {alvo} com {len(catalog['criterios'])} critérios; preencha as entradas e rode vygolint_report.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
