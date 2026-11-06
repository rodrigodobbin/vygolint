"""Merge per-part criterion entries into an avaliacao.yaml.

When the criteria are graded in parts (one subagent per category, or one sitting per guideline), each
part is a YAML file mapping criterion id -> entry. This module reads the parts, checks them against
the catalog and writes each entry in place of the block under its id in avaliacao.yaml, keeping the
header and the comments the scaffold wrote. Pure functions; the CLI is scripts/vygolint_juntar.py.
"""

import re

import yaml

_ID = re.compile(r"^  (D\d\d\.\d+):\s*$")


def ids_por_categoria(catalog):
    por = {}
    for cid in sorted(catalog["criterios"]):
        por.setdefault(catalog["criterios"][cid]["diretriz"]["categoria"], []).append(cid)
    return por


def ler_partes(partes, catalog):
    """`partes` maps a part name to its YAML text. Returns (entries by id, errors, notes).

    Errors make the merge unsafe (invalid YAML, unknown id, the same id in two parts, an entry that
    is not a map). Notes are worth reading but do not block: a part wrapped in `criterios:`, and a
    part named after a category that misses criteria of that category or brings criteria of another.
    """
    entradas, origem, erros, notas = {}, {}, [], []
    categorias = ids_por_categoria(catalog)
    for nome in sorted(partes):
        try:
            doc = yaml.safe_load(partes[nome])
        except yaml.YAMLError as exc:
            erros.append(f"{nome}: YAML inválido: {str(exc).splitlines()[0]}")
            continue
        if isinstance(doc, dict) and set(doc) == {"criterios"} and isinstance(doc["criterios"], dict):
            notas.append(f"{nome}: entradas vieram dentro de `criterios:`; usei o conteúdo")
            doc = doc["criterios"]
        if not isinstance(doc, dict):
            erros.append(f"{nome}: o topo deve ser um mapa id -> entrada")
            continue
        for cid, entrada in doc.items():
            if cid not in catalog["criterios"]:
                erros.append(f"{nome}: {cid}: critério inexistente no catálogo")
            elif not isinstance(entrada, dict):
                erros.append(f"{nome}: {cid}: entrada deve ser mapa")
            elif cid in origem:
                erros.append(f"{nome}: {cid}: já veio em {origem[cid]}")
            else:
                entradas[cid] = entrada
                origem[cid] = nome
        if nome in categorias:
            faltam = [c for c in categorias[nome] if c not in doc]
            alheios = [c for c in doc if c in catalog["criterios"] and c not in categorias[nome]]
            if faltam:
                notas.append(f"{nome}: faltam critérios da categoria: {', '.join(faltam)}")
            if alheios:
                notas.append(f"{nome}: traz critérios de outra categoria: {', '.join(alheios)}")
    return entradas, erros, notas


def injetar(texto, entradas):
    """Replace, in the text of avaliacao.yaml, the block under each id by its entry. Returns (text, ids not found)."""
    linhas = texto.split("\n")
    saida, usados, i = [], set(), 0
    while i < len(linhas):
        m = _ID.match(linhas[i])
        if not m or m.group(1) not in entradas:
            saida.append(linhas[i])
            i += 1
            continue
        cid = m.group(1)
        saida.append(linhas[i])
        i += 1
        while i < len(linhas) and (linhas[i].startswith("    ") or (linhas[i].strip() == "" and i + 1 < len(linhas) and linhas[i + 1].startswith("    "))):
            i += 1
        bloco = yaml.safe_dump(entradas[cid], allow_unicode=True, sort_keys=False, width=10000, default_flow_style=False)
        saida += ["    " + linha for linha in bloco.rstrip("\n").split("\n")]
        usados.add(cid)
    return "\n".join(saida), sorted(set(entradas) - usados)
