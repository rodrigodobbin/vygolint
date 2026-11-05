"""Render the skeleton of an avaliacao.yaml: header plus one entry per catalog criterion.

The skeleton is a valid evaluation (it passes validate_avaliacao): every criterion starts as
`nao_avaliado`, or `fora_do_contexto` when the guideline has `aplicabilidade` and the game is not
used in a classroom. The evaluator replaces each entry in place. Pure function, no I/O.
"""

import json

from .report import FONTES

PLACEHOLDER = "PREENCHER"
_RAZAO_SALA = "o jogo não é aplicado em sala de aula no contexto declarado (sala_de_aula: false)"


def _q(texto):
    """Double-quoted YAML scalar (a JSON string is one)."""
    return json.dumps(str(texto), ensure_ascii=False)


def _lista(itens):
    return "[" + ", ".join(_q(i) for i in itens) + "]"


def _aceitas(criterio):
    return [f for f in FONTES if (criterio.get("evidencia") or {}).get(f) is not None]


_MAX_LISTADOS = 30


def render_scaffold(catalog, jogo, sala_de_aula, fontes, artefatos, avaliador, data, externas=None, arquivos=None):
    """`artefatos` maps source -> files or folders; `externas` maps source -> texts for sources that
    are not on this machine; `arquivos` maps source -> labels of the files the folders put in scope,
    printed as comments under the source so the evaluator sees what must be accounted for."""
    fontes = [f for f in FONTES if f in fontes]
    externas = externas or {}
    arquivos = arquivos or {}
    linhas = [
        "# Esqueleto gerado por scripts/vygolint_scaffold.py. Edite este arquivo: troque cada entrada",
        f"# pelo grau e pelas provas do critério (skill vygolint-criterio). Onde está \"{PLACEHOLDER}\", ou",
        "# o critério foi graduado e a entrada reescrita, ou a razao diz qual fonte faltou ou o que ela",
        "# não mostrou. Depois rode scripts/vygolint_report.py neste arquivo.",
        f"jogo: {_q(jogo)}",
        "contexto:",
        f"  sala_de_aula: {'true' if sala_de_aula else 'false'}",
        "  fontes: [" + ", ".join(fontes) + "]",
        "  # artefatos: arquivos ou pastas; uma pasta põe no escopo todos os arquivos dentro dela.",
    ]
    com_artefato = [f for f in fontes if artefatos.get(f)]
    linhas.append("  artefatos:" if com_artefato else "  artefatos: {}")
    for f in com_artefato:
        linhas.append(f"    {f}: {_lista(artefatos[f])}")
        listados = list(arquivos.get(f) or [])
        for rotulo in listados[:_MAX_LISTADOS]:
            linhas.append(f"    #   {rotulo}")
        if len(listados) > _MAX_LISTADOS:
            linhas.append(f"    #   … e mais {len(listados) - _MAX_LISTADOS}")
    com_externa = [f for f in fontes if externas.get(f)]
    if com_externa:
        linhas.append("  # fontes_externas: fontes usadas que não estão nesta máquina (não entram no escopo do lint).")
        linhas.append("  fontes_externas:")
        for f in com_externa:
            linhas.append(f"    {f}: {_lista(externas[f])}")
    linhas += [f"avaliador: {_q(avaliador)}", f"data: {_q(data)}", "criterios:"]
    for cid in sorted(catalog["criterios"]):
        item = catalog["criterios"][cid]
        criterio, diretriz = item["criterio"], item["diretriz"]
        aceitas = _aceitas(criterio)
        no_contexto = [f for f in aceitas if f in fontes]
        linhas.append(f"  # {cid} ({criterio['nivel']}) — {criterio['enunciado']}")
        if diretriz.get("aplicabilidade") and not sala_de_aula:
            linhas.append(f"  # aplicabilidade: {diretriz['aplicabilidade']}")
            grau, razao = "fora_do_contexto", _RAZAO_SALA
        elif no_contexto:
            linhas.append("  # fontes deste contexto que o critério aceita: " + ", ".join(no_contexto))
            grau, razao = "nao_avaliado", PLACEHOLDER
        else:
            linhas.append("  # nenhuma fonte deste contexto é aceita pelo critério")
            grau = "nao_avaliado"
            razao = (
                f"o critério só aceita {', '.join(aceitas)} como fonte e o contexto só tem {', '.join(fontes)}"
            )
        linhas += [f"  {cid}:", f"    grau: {grau}", f"    razao: {_q(razao)}"]
    return "\n".join(linhas) + "\n"
