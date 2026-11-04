"""Load and validate the whole catalog directory. Pure loading, no doc writing."""

from pathlib import Path

import yaml

from .validate import load_yaml, validate_catalogo, validate_definicoes, validate_diretriz


def load_catalog(catalog_dir):
    """Return (catalog, errors). catalog is None when errors is non-empty.

    catalog = {"schema", "categorias", "glossario", "diretrizes" (sorted by id),
               "criterios": {criterio_id: {"diretriz": d, "criterio": c}}}
    """
    catalog_dir = Path(catalog_dir)
    for nome in ("schema.yaml", "categorias.yaml"):
        if not (catalog_dir / nome).exists():
            return None, [f"{nome}: arquivo ausente"]
    schema = load_yaml(catalog_dir / "schema.yaml")
    categorias = load_yaml(catalog_dir / "categorias.yaml")
    glossario_path = catalog_dir / "definicoes.yaml"
    if not glossario_path.exists():
        return None, ["definicoes.yaml: arquivo ausente"]
    try:
        doc = load_yaml(glossario_path)
    except yaml.YAMLError as exc:
        return None, [f"definicoes.yaml: YAML inválido: {exc}"]
    errors = validate_definicoes(doc)
    if errors:
        return None, errors
    glossario = {e["chave"]: e for e in doc["termos"]}
    diretrizes = []
    for path in sorted(catalog_dir.glob("D*.yaml")):
        try:
            d = load_yaml(path)
        except yaml.YAMLError as exc:
            errors.append(f"{path.name}: YAML inválido: {exc}")
            continue
        errs = validate_diretriz(d, schema, categorias, glossario)
        errs = [path.name + e[1:] if e.startswith("?:") else e for e in errs]
        if not errs and path.name != f"{d['id']}.yaml":
            errs.append(f"{path.name}: nome do arquivo não corresponde ao id {d['id']}")
        errors.extend(errs)
        if not errs:
            diretrizes.append(d)
    if errors:
        return None, errors
    errors = validate_catalogo(diretrizes)
    if errors:
        return None, errors
    diretrizes.sort(key=lambda d: d["id"])
    criterios = {c["id"]: {"diretriz": d, "criterio": c} for d in diretrizes for c in d["criterios"]}
    return {
        "schema": schema,
        "categorias": categorias,
        "glossario": glossario,
        "diretrizes": diretrizes,
        "criterios": criterios,
    }, []
