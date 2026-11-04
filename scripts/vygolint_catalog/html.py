"""Render the HTML report (relatorio.html) from the aggregated result, the evaluation and the catalog.

The page is a static template (relatorio_template.html) with one JSON blob injected at the
`/*__DATA__*/` marker. Everything the page shows comes from that JSON: grades and notes from
`aggregate`, recommendation vias from `vias_para`, texts from the catalog. Pure function, no I/O
besides reading the template next to this file.
"""

import json
from pathlib import Path

from .report import CLAUSULA, FONTES, vias_para

_TEMPLATE = Path(__file__).with_name("relatorio_template.html")
_MARKER = "/*__DATA__*/"
_NOME_FONTE = {"codigo": "código-fonte", "documentacao": "GDD ou documento equivalente", "video": "vídeo de gameplay"}


def _fontes_faltantes(criterio, fontes_ctx):
    """Sources the criterion accepts (evidencia non-null) that the evaluation did not have."""
    ev = criterio.get("evidencia") or {}
    return [f for f in FONTES if ev.get(f) is not None and f not in fontes_ctx]


def _destravas(res, av, catalog):
    """Group non-evaluated and out-of-context criteria by the source that would let them be decided."""
    fontes_ctx = list(av["contexto"]["fontes"])
    grupos = {f: [] for f in FONTES}
    sem_fonte = []
    sala = []
    for cid in sorted(res["criterios"]):
        c = res["criterios"][cid]
        crit = catalog["criterios"][cid]["criterio"]
        if c["grau"] == "fora_do_contexto":
            sala.append(cid)
            continue
        if c["grau_declarado"] != "nao_avaliado":
            continue
        faltam = _fontes_faltantes(crit, fontes_ctx)
        if not faltam:
            sem_fonte.append(cid)
        for f in faltam:
            grupos[f].append(cid)
    linhas = []
    for f in FONTES:
        if grupos[f]:
            linhas.append({"entregar": f"Entregar {_NOME_FONTE[f]}", "criterios": grupos[f]})
    if sem_fonte:
        linhas.append({
            "entregar": "Mais gravações ou outra sessão (critérios cujas fontes já foram usadas mas não mostraram o ponto avaliado)",
            "criterios": sem_fonte,
        })
    if sala:
        linhas.append({
            "entregar": "Declarar uso em sala de aula (sala_de_aula: true) e entregar guia do professor ou plano de aula",
            "criterios": sala,
        })
    return linhas


def build_data(res, av, catalog):
    """Assemble the JSON the page renders. Keys are stable; the template reads only these."""
    fontes_ctx = list(av["contexto"]["fontes"])
    categorias = [
        {"chave": c["chave"], "nome": c["nome"], "descricao": c["descricao"]}
        for c in catalog["categorias"]["categorias"]
    ]
    criterios = []
    for cid in sorted(res["criterios"]):
        c = res["criterios"][cid]
        item = catalog["criterios"][cid]
        crit, dire = item["criterio"], item["diretriz"]
        entrada = av["criterios"][cid]
        fontes = []
        for f in FONTES:
            dados = (entrada.get("fontes") or {}).get(f)
            if dados:
                fontes.append({
                    "fonte": f, "grau": dados["grau"], "provas": list(dados.get("provas") or []),
                    "observacao": dados.get("observacao"),
                })
        por_dependencia = c["nota"] is not None and c["grau_declarado"] != c["grau"]
        vias = [] if por_dependencia else vias_para(fontes_ctx, crit.get("recomendacao") or {})
        criterios.append({
            "id": cid,
            "diretriz": dire["id"],
            "diretriz_texto": dire["diretriz"],
            "modalidade": dire["modalidade"],
            "categoria": dire["categoria"],
            "nivel": c["nivel"],
            "enunciado": crit["enunciado"],
            "escala": crit.get("escala") or {},
            "grau": c["grau"],
            "grau_declarado": c["grau_declarado"],
            "nota": c["nota"],
            "razao": entrada.get("razao"),
            "justificativa_conflito": entrada.get("justificativa_conflito"),
            "fontes": fontes,
            "vias": [{"via": v, "texto": t} for v, t in vias],
            "depende_de": crit.get("depende_de"),
        })
    return {
        "clausula": CLAUSULA,
        "jogo": av["jogo"],
        "data": str(av["data"]),
        "avaliador": av["avaliador"],
        "sala_de_aula": bool(av["contexto"]["sala_de_aula"]),
        "fontes": fontes_ctx,
        "artefatos": {f: list(v) for f, v in (av["contexto"].get("artefatos") or {}).items()},
        "nivel": res["nivel"],
        "cobertura_nivel": res["cobertura_nivel"],
        "cobertura_categoria": res["cobertura_categoria"],
        "bloqueios": [b["id"] for b in res["bloqueios"]],
        "parciais": [p["id"] for p in res["parciais"]],
        "destravas": _destravas(res, av, catalog),
        "categorias": categorias,
        "criterios": criterios,
    }


def render_relatorio_html(res, av, catalog):
    template = _TEMPLATE.read_text(encoding="utf-8")
    if _MARKER not in template:
        raise RuntimeError(f"{_TEMPLATE.name}: marcador {_MARKER} ausente")
    blob = json.dumps(build_data(res, av, catalog), ensure_ascii=False).replace("</", "<\\/")
    return template.replace(_MARKER, blob, 1)
