"""Progress of an avaliacao.yaml being filled in: which criteria still carry the scaffold placeholder."""

from .merge import ids_por_categoria
from .scaffold import PLACEHOLDER

_CABECALHO = ("jogo", "avaliador", "data")


def _pendente(entrada):
    """A criterion is pending when it has no entry, its entry is not a map, or its reason still says PREENCHER."""
    if not isinstance(entrada, dict):
        return True
    razao = entrada.get("razao")
    return isinstance(razao, str) and PLACEHOLDER in razao


def status_avaliacao(av, catalog, inventario=None):
    """Return counts of filled and pending criteria, per category, the next pending id and leftover placeholders.

    `av` is the parsed avaliacao.yaml (it does not need to validate); `inventario` is the text of inventario.md
    when it exists. Nothing here grades or aggregates: it only looks for the scaffold placeholder.
    """
    criterios = av.get("criterios") if isinstance(av, dict) else None
    criterios = criterios if isinstance(criterios, dict) else {}
    por_categoria = ids_por_categoria(catalog)
    preenchidos, pendentes, sem_entrada = [], [], []
    resumo = {}
    for categoria, ids in por_categoria.items():
        feitos = 0
        for cid in ids:
            entrada = criterios.get(cid)
            if cid not in criterios:
                sem_entrada.append(cid)
            if _pendente(entrada):
                pendentes.append(cid)
            else:
                preenchidos.append(cid)
                feitos += 1
        resumo[categoria] = {"preenchidos": feitos, "total": len(ids), "pendentes": [c for c in ids if c in pendentes]}
    pendentes.sort()
    proximo = pendentes[0] if pendentes else None
    cabecalho = [
        campo for campo in _CABECALHO
        if isinstance(av, dict) and isinstance(av.get(campo), str) and PLACEHOLDER in av[campo]
    ]
    return {
        "total": len(catalog["criterios"]),
        "preenchidos": len(preenchidos),
        "pendentes": len(pendentes),
        "ids_preenchidos": sorted(preenchidos),
        "ids_pendentes": pendentes,
        "sem_entrada": sorted(sem_entrada),
        "proximo": proximo,
        "proximo_categoria": catalog["criterios"][proximo]["diretriz"]["categoria"] if proximo else None,
        "por_categoria": resumo,
        "cabecalho_pendente": cabecalho,
        "inventario_pendente": inventario.count(PLACEHOLDER) if isinstance(inventario, str) else None,
    }


def render_status(s):
    linhas = [f"Status: {s['preenchidos']} de {s['total']} critérios preenchidos; {s['pendentes']} pendente(s)."]
    for categoria, r in s["por_categoria"].items():
        resto = f" (faltam {', '.join(r['pendentes'])})" if r["pendentes"] else ""
        linhas.append(f"  {categoria}: {r['preenchidos']}/{r['total']}{resto}")
    if s["sem_entrada"]:
        linhas.append(f"Sem entrada em avaliacao.yaml: {', '.join(s['sem_entrada'])}")
    if s["cabecalho_pendente"]:
        linhas.append(f"Cabeçalho ainda com {PLACEHOLDER}: {', '.join(s['cabecalho_pendente'])}")
    if s["inventario_pendente"]:
        linhas.append(f"inventario.md: {s['inventario_pendente']} {PLACEHOLDER}")
    if s["proximo"]:
        linhas.append(f"Próximo: {s['proximo']} ({s['proximo_categoria']})")
    else:
        linhas.append("Próximo: nenhum critério pendente; rode o relatório.")
    return "\n".join(linhas) + "\n"
