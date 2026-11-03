"""Load, validate and render the whole catalog."""

from pathlib import Path

import yaml

from .render import render_latex, render_markdown
from .validate import load_yaml, validate_catalogo, validate_diretriz


def build(catalog_dir, docs_dir):
    """Return a list of errors. On success (empty list) writes catalogo.md and catalogo.tex."""
    catalog_dir = Path(catalog_dir)
    docs_dir = Path(docs_dir)
    schema = load_yaml(catalog_dir / "schema.yaml")
    categorias = load_yaml(catalog_dir / "categorias.yaml")
    errors = []
    diretrizes = []
    for path in sorted(catalog_dir.glob("D*.yaml")):
        try:
            d = load_yaml(path)
        except yaml.YAMLError as exc:
            errors.append(f"{path.name}: YAML inválido: {exc}")
            continue
        errs = validate_diretriz(d, schema, categorias)
        errs = [path.name + e[1:] if e.startswith("?:") else e for e in errs]
        if not errs and path.name != f"{d['id']}.yaml":
            errs.append(f"{path.name}: nome do arquivo não corresponde ao id {d['id']}")
        errors.extend(errs)
        if not errs:
            diretrizes.append(d)
    if errors:
        return errors
    errors = validate_catalogo(diretrizes)
    if errors:
        return errors
    docs_dir.mkdir(parents=True, exist_ok=True)
    (docs_dir / "catalogo.md").write_text(render_markdown(diretrizes, categorias), encoding="utf-8")
    (docs_dir / "catalogo.tex").write_text(render_latex(diretrizes, categorias), encoding="utf-8")
    return []


def contagem(catalog_dir):
    """Return (n_diretrizes, n_criterios) for a catalog directory, without validating."""
    n_d = n_c = 0
    for path in sorted(Path(catalog_dir).glob("D*.yaml")):
        d = load_yaml(path)
        n_d += 1
        n_c += len(d.get("criterios") or [])
    return n_d, n_c
