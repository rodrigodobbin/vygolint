"""Load, validate and render the whole catalog."""

from pathlib import Path

from .catalog import load_catalog
from .render import render_latex, render_markdown
from .validate import load_yaml


def build(catalog_dir, docs_dir):
    """Return a list of errors. On success (empty list) writes catalogo.md and catalogo.tex."""
    docs_dir = Path(docs_dir)
    catalog, errors = load_catalog(catalog_dir)
    if errors:
        return errors
    docs_dir.mkdir(parents=True, exist_ok=True)
    (docs_dir / "catalogo.md").write_text(
        render_markdown(catalog["diretrizes"], catalog["categorias"], catalog["glossario"]), encoding="utf-8"
    )
    (docs_dir / "catalogo.tex").write_text(render_latex(catalog["diretrizes"], catalog["categorias"]), encoding="utf-8")
    return []


def contagem(catalog_dir):
    """Return (n_diretrizes, n_criterios) for a catalog directory, without validating."""
    n_d = n_c = 0
    for path in sorted(Path(catalog_dir).glob("D*.yaml")):
        d = load_yaml(path)
        n_d += 1
        n_c += len(d.get("criterios") or [])
    return n_d, n_c
