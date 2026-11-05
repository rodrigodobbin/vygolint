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


_CLASSES = "`documento equivalente` (GDD, roteiro, guia do professor, plano de aula, mapa de nível ou especificação), `não conta` (material de divulgação ou de loja, ou sem conteúdo do jogo) ou `não abriu`"


def render_inventario(jogo, fontes, artefatos, externas=None, arquivos=None):
    """Skeleton of inventario.md: the lists every criterion counts from, and one row per file in scope.

    `arquivos` maps source -> labels of the video and document files in scope (see lint.arquivos_do_escopo).
    The lint reads the Classificação column of the documentation table.
    """
    fontes = [f for f in FONTES if f in fontes]
    externas = externas or {}
    arquivos = arquivos or {}
    p = PLACEHOLDER
    linhas = [
        f"# Inventário — {jogo}",
        "",
        # The comment must not contain the placeholder itself: the lint counts every occurrence in the file.
        "<!-- Esqueleto gerado por scripts/vygolint_scaffold.py. Troque cada célula marcada para preencher. Onde não houver",
        "item, apague a tabela e escreva \"Nenhum observado\". Cada item diz onde aparece: arquivo:linha, documento p. N ou vídeo hh:mm:ss.",
        "Aplique as definições de catalog/definicoes.yaml antes de contar. -->",
        "",
        "## Missões",
        "",
        "| # | Missão | Onde aparece | Objetivo | Condição de conclusão |",
        "|---|---|---|---|---|",
        f"| 1 | {p} | {p} | {p} | {p} |",
        "",
        "## Minijogos",
        "",
        "| # | Minijogo | Onde aparece | Regras e objetivo |",
        "|---|---|---|---|",
        f"| 1 | {p} | {p} | {p} |",
        "",
        "## Cenários jogáveis",
        "",
        "| # | Cenário | Onde aparece | Missão em curso |",
        "|---|---|---|---|",
        f"| 1 | {p} | {p} | {p} |",
        "",
        "## Objetivos de aprendizagem",
        "",
        "Só a lista do GDD ou documento equivalente define os objetivos avaliados. Sem esse documento, escreva",
        "\"Nenhum objetivo de aprendizagem listado\" e o motivo.",
        "",
        "| # | Objetivo | Documento e página |",
        "|---|---|---|",
        f"| 1 | {p} | {p} |",
        "",
        "## Fontes lidas",
        "",
    ]
    if "documentacao" in fontes:
        linhas += [
            "### Documentação",
            "",
            "Uma linha por documento do escopo. Estar no escopo não faz do arquivo evidência: leia cada um e classifique como",
            _CLASSES + ". Só documento equivalente é citado em prova.",
            "",
            "| Arquivo | Classificação | Motivo ou conteúdo |",
            "|---|---|---|",
        ]
        docs = list(arquivos.get("documentacao") or [])
        linhas += [f"| `{d}` | {p} | |" for d in docs]
        if not docs:
            pastas = ", ".join(f"`{a}`" for a in artefatos.get("documentacao") or []) or "(sem artefato local)"
            linhas.append(f"| _nenhum documento encontrado em {pastas}_ | | |")
        linhas.append("")
    if "video" in fontes:
        linhas += [
            "### Vídeo",
            "",
            "Uma linha por vídeo do escopo, com o registro gerado pela skill vygolint-video.",
            "",
            "| Arquivo | Registro |",
            "|---|---|",
        ]
        videos = list(arquivos.get("video") or [])
        linhas += [f"| `{v}` | {p} |" for v in videos]
        if not videos:
            pastas = ", ".join(f"`{a}`" for a in artefatos.get("video") or []) or "(sem artefato local)"
            linhas.append(f"| _nenhum arquivo de vídeo encontrado em {pastas}_ | |")
        linhas.append("")
    if "codigo" in fontes:
        linhas += ["### Código", "", "Por pasta ou arquivo declarado: módulos, cenas, telas, manipuladores de entrada e de rede, persistência e textos exibidos ao jogador que você leu.", ""]
        linhas += [f"- `{a}`: {p}" for a in artefatos.get("codigo") or []] or ["- (sem artefato local)"]
        linhas.append("")
    com_externa = [f for f in fontes if externas.get(f)]
    if com_externa:
        linhas += ["### Fontes externas", "", "Fontes usadas que não estão nesta máquina; diga o que foi consultado em cada uma.", ""]
        for f in com_externa:
            linhas += [f"- {f}: {texto} — {p}" for texto in externas[f]]
        linhas.append("")
    linhas += ["## Fontes que não foi possível abrir", "", f"{p} (ou \"Nenhuma\")", ""]
    return "\n".join(linhas)
