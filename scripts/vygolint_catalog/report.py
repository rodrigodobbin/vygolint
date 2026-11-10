"""Validate avaliacao.yaml against the catalog, aggregate grades, render the report (conformidade.md)."""

import re
from pathlib import Path

import yaml

from .validate import _is_text, load_yaml

FONTES = ("codigo", "documentacao", "video")
GRAUS_FONTE = ("atendido", "parcial", "nao_atendido")
GRAUS = GRAUS_FONTE + ("nao_avaliado", "fora_do_contexto")
NIVEIS = ("A", "AA", "AAA")
_ORDEM = {"nao_atendido": 0, "parcial": 1, "atendido": 2}
_DATA_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_avaliacao(path):
    return load_yaml(path)


def grau_esperado(fontes):
    """Worst grade among the sources considered; documentacao is ignored when video is present."""
    consideradas = dict(fontes)
    if "video" in consideradas:
        consideradas.pop("documentacao", None)
    graus = [f["grau"] for f in consideradas.values()]
    if not graus:
        return None
    return min(graus, key=lambda g: _ORDEM[g])


def _validate_cabecalho(av, errors):
    if not _is_text(av.get("jogo")):
        errors.append("avaliacao: jogo ausente ou vazio")
    ctx = av.get("contexto")
    if not isinstance(ctx, dict):
        errors.append("avaliacao: contexto deve ser mapa")
        return [], None
    if not isinstance(ctx.get("sala_de_aula"), bool):
        errors.append("avaliacao: contexto.sala_de_aula deve ser true ou false")
    fontes = ctx.get("fontes")
    if not isinstance(fontes, list) or not fontes or any(f not in FONTES for f in fontes):
        errors.append(f"avaliacao: contexto.fontes deve ser lista não vazia dentro de {list(FONTES)} (recebido {fontes!r})")
        fontes = [f for f in fontes if f in FONTES] if isinstance(fontes, list) else []
    artefatos = ctx.get("artefatos")
    if not isinstance(artefatos, dict) or any(k not in FONTES for k in artefatos):
        errors.append("avaliacao: contexto.artefatos deve ser mapa fonte -> lista de caminhos")
    else:
        for fonte, valor in artefatos.items():
            if not isinstance(valor, list) or not all(_is_text(v) for v in valor):
                errors.append(f"avaliacao: contexto.artefatos.{fonte} deve ser lista de caminhos (arquivo ou pasta)")
    externas = ctx.get("fontes_externas")
    if externas is not None:
        if not isinstance(externas, dict) or any(k not in FONTES for k in externas):
            errors.append("avaliacao: contexto.fontes_externas deve ser mapa fonte -> lista de textos")
        else:
            for fonte, valor in externas.items():
                if not isinstance(valor, list) or not valor or not all(_is_text(v) for v in valor):
                    errors.append(f"avaliacao: contexto.fontes_externas.{fonte} deve ser lista não vazia de textos")
    if not _is_text(av.get("avaliador")):
        errors.append("avaliacao: avaliador ausente ou vazio")
    if not _DATA_RE.fullmatch(str(av.get("data", ""))):
        errors.append("avaliacao: data deve ter o formato AAAA-MM-DD")
    return fontes, ctx.get("sala_de_aula")


def _validate_fontes(cid, entrada, criterio, fontes_ctx, errors):
    fontes = entrada.get("fontes")
    if not isinstance(fontes, dict) or not fontes:
        errors.append(f"{cid}: ao menos uma fonte é obrigatória para o grau {entrada.get('grau')}")
        return {}
    validas = {}
    for nome, f in fontes.items():
        if nome not in FONTES:
            errors.append(f"{cid}: fonte desconhecida: {nome}")
            continue
        if criterio["evidencia"].get(nome) is None:
            errors.append(f"{cid}: fonte {nome} não existe na evidencia do critério")
            continue
        if nome not in fontes_ctx:
            errors.append(f"{cid}: fonte {nome} não está em contexto.fontes")
            continue
        if not isinstance(f, dict):
            errors.append(f"{cid}: fonte {nome} deve ser mapa")
            continue
        if f.get("grau") not in GRAUS_FONTE:
            errors.append(f"{cid}: fonte {nome} com grau inválido: {f.get('grau')!r}")
            continue
        provas = f.get("provas")
        if not isinstance(provas, list) or not provas or not all(_is_text(p) for p in provas):
            errors.append(f"{cid}: fonte {nome} precisa de provas (lista não vazia de textos)")
            continue
        if "observacao" in f and f["observacao"] is not None and not _is_text(f["observacao"]):
            errors.append(f"{cid}: fonte {nome}: observacao deve ser texto não vazio")
        validas[nome] = f
    return validas


def validate_avaliacao(av, catalog):
    """Return a list of error strings; empty means the evaluation can be aggregated."""
    errors = []
    if not isinstance(av, dict):
        return ["avaliacao: documento deve ser mapa"]
    fontes_ctx, sala = _validate_cabecalho(av, errors)
    criterios = av.get("criterios")
    if not isinstance(criterios, dict):
        errors.append("avaliacao: criterios deve ser mapa id -> entrada")
        return errors
    for cid in criterios:
        if cid not in catalog["criterios"]:
            errors.append(f"{cid}: critério inexistente no catálogo")
    for cid in catalog["criterios"]:
        if cid not in criterios:
            errors.append(f"{cid}: critério sem entrada (use grau nao_avaliado com razao)")
    for cid, entrada in criterios.items():
        if cid not in catalog["criterios"]:
            continue
        item = catalog["criterios"][cid]
        if not isinstance(entrada, dict):
            errors.append(f"{cid}: entrada deve ser mapa")
            continue
        grau = entrada.get("grau")
        if grau not in GRAUS:
            errors.append(f"{cid}: grau inválido: {grau!r}")
            continue
        if grau in ("nao_avaliado", "fora_do_contexto"):
            if not _is_text(entrada.get("razao")):
                errors.append(f"{cid}: razao obrigatória para grau {grau}")
            if "fontes" in entrada and entrada["fontes"] is not None and entrada["fontes"] != {}:
                errors.append(f"{cid}: fontes não se aplicam ao grau {grau}; use razao")
        if grau == "fora_do_contexto":
            if item["diretriz"].get("aplicabilidade") is None:
                errors.append(f"{cid}: fora_do_contexto só vale para diretriz com aplicabilidade")
            elif sala is True:
                errors.append(f"{cid}: fora_do_contexto incompatível com contexto.sala_de_aula true")
            continue
        if grau == "nao_avaliado":
            continue
        usadas = _validate_fontes(cid, entrada, item["criterio"], fontes_ctx, errors)
        esperado = grau_esperado(usadas) if usadas else None
        if esperado is not None and esperado != grau and not _is_text(entrada.get("justificativa_conflito")):
            errors.append(
                f"{cid}: grau {grau} diverge do esperado pelas fontes ({esperado}); escreva justificativa_conflito"
            )
    return errors


_VIAS = ("documentacao", "design", "codigo")


def vias_para(fontes_ctx, recomendacao):
    """Pick the recommendation vias for the evidence available (conformidade.md section 5)."""
    if "codigo" in fontes_ctx:
        escolhidas = ["codigo"]
    else:
        escolhidas = ["design"]
        if "documentacao" in fontes_ctx:
            escolhidas.insert(0, "documentacao")
        if "video" in fontes_ctx:
            escolhidas.append("codigo")
    uteis = [v for v in _VIAS if v in escolhidas and recomendacao.get(v)]
    if not uteis:
        uteis = [v for v in _VIAS if recomendacao.get(v)]
    return [(v, recomendacao[v]) for v in uteis]


def _contagem_vazia():
    return {"atendido": 0, "parcial": 0, "nao_atendido": 0, "nao_avaliado": 0, "fora_do_contexto": 0}


def _contar(contagem, grau):
    if grau == "nao_avaliado":
        contagem["nao_atendido"] += 1
        contagem["nao_avaliado"] += 1
    else:
        contagem[grau] += 1


def _resolver_dependencias(declarados, catalog):
    """Return {id: (grau_efetivo, nota)} after applying depende_de. Cycles are rejected by validate_catalogo; the iteration bound is a safety net."""
    efetivo = {cid: (g, None) for cid, g in declarados.items()}
    for _ in range(len(efetivo) + 1):
        mudou = False
        for cid, item in catalog["criterios"].items():
            grau_decl = declarados[cid]
            if grau_decl == "fora_do_contexto":
                continue
            novo = (grau_decl, None)
            falhas_nao_atendido = []
            falhas_nao_avaliado = []
            for grupo in item["criterio"]["depende_de"]:
                estados = [efetivo[alvo][0] for alvo in grupo]
                if "atendido" in estados:
                    continue
                alvos = " ou ".join(grupo)
                if "nao_avaliado" in estados and all(e in ("nao_avaliado", "parcial", "nao_atendido") for e in estados):
                    falhas_nao_avaliado.append(alvos)
                else:
                    falhas_nao_atendido.append(alvos)
            if falhas_nao_atendido:
                novo = ("nao_atendido", f"não atendido por dependência não satisfeita ({'; '.join(falhas_nao_atendido)})")
            elif falhas_nao_avaliado:
                novo = ("nao_avaliado", f"não avaliado por dependência de critério não avaliado ({'; '.join(falhas_nao_avaliado)})")
            if efetivo[cid] != novo:
                efetivo[cid] = novo
                mudou = True
        if not mudou:
            return efetivo
    raise ValueError("depende_de com ciclo no catálogo")


def aggregate(av, catalog):
    """Apply conformidade.md to a validated evaluation. Returns the result dict used by the renderers."""
    fontes_ctx = list(av["contexto"]["fontes"])
    declarados = {cid: av["criterios"][cid]["grau"] for cid in catalog["criterios"]}
    efetivo = _resolver_dependencias(declarados, catalog)
    criterios = {}
    for cid, item in catalog["criterios"].items():
        grau, nota = efetivo[cid]
        criterios[cid] = {
            "nivel": item["criterio"]["nivel"],
            "categoria": item["diretriz"]["categoria"],
            "grau_declarado": declarados[cid],
            "grau": grau,
            "nota": nota,
        }
    nivel = "sem_conformidade"
    for n in NIVEIS:
        pendentes = [c for c in criterios.values() if c["nivel"] == n and c["grau"] not in ("atendido", "fora_do_contexto")]
        if pendentes:
            break
        nivel = n
    cobertura_nivel = {n: _contagem_vazia() for n in NIVEIS}
    chaves_cat = [c["chave"] for c in catalog["categorias"]["categorias"]]
    cobertura_categoria = {k: _contagem_vazia() for k in chaves_cat}
    for c in criterios.values():
        _contar(cobertura_nivel[c["nivel"]], c["grau"])
        _contar(cobertura_categoria[c["categoria"]], c["grau"])
    proximo = {"sem_conformidade": "A", "A": "AA", "AA": "AAA", "AAA": None}[nivel]
    bloqueios = []
    parciais = []
    for cid in sorted(criterios):
        c = criterios[cid]
        crit = catalog["criterios"][cid]["criterio"]
        if c["grau"] == "fora_do_contexto":
            continue
        por_dependencia = c["nota"] is not None and c["grau_declarado"] != c["grau"]
        vias = [] if por_dependencia else vias_para(fontes_ctx, crit["recomendacao"])
        if proximo and c["nivel"] == proximo and c["grau"] != "atendido":
            bloqueios.append({
                "id": cid, "nivel": c["nivel"], "grau": c["grau"], "nota": c["nota"],
                "enunciado": crit["enunciado"], "vias": vias,
            })
        if c["grau"] == "parcial":
            parciais.append({
                "id": cid, "nivel": c["nivel"], "enunciado": crit["enunciado"],
                "escala_parcial": crit["escala"]["parcial"], "escala_atendido": crit["escala"]["atendido"],
                "vias": vias,
            })
    return {
        "criterios": criterios,
        "nivel": nivel,
        "cobertura_nivel": cobertura_nivel,
        "cobertura_categoria": cobertura_categoria,
        "bloqueios": bloqueios,
        "parciais": parciais,
    }


CLAUSULA = (
    "O resultado de uma avaliação vygolint expressa conformidade com os critérios do vygolint, "
    "derivados das diretrizes de Carvalho (2020), e não classifica o jogo como sociointeracionista."
)
RODAPE = (
    "Gerado pelo vygolint (https://github.com/rodrigodobbin/vygolint), de Rodrigo Dobbin Fellows. "
    "Critérios, níveis e recomendações são do vygolint; o texto das diretrizes é de Carvalho (2020)."
)
GENERATED = "<!-- ARQUIVO GERADO por scripts/vygolint_report.py a partir de avaliacao.yaml. Não edite à mão. -->"
_NOME_GRAU = {
    "atendido": "atendido", "parcial": "parcial", "nao_atendido": "não atendido",
    "nao_avaliado": "não avaliado", "fora_do_contexto": "fora do contexto", "sem_conformidade": "sem conformidade",
}
_NOME_FONTE = {"codigo": "Código", "documentacao": "Documentação", "video": "Vídeo"}
_NOME_VIA = {"documentacao": "Documentação", "design": "Design", "codigo": "Código"}


def _nome_categoria(chave, catalog):
    for c in catalog["categorias"]["categorias"]:
        if c["chave"] == chave:
            return c["nome"]
    return chave


def _linha_contagem(rotulo, c):
    return (
        f"| {rotulo} | {c['atendido']} | {c['parcial']} | {c['nao_atendido']} "
        f"(dos quais {c['nao_avaliado']} não avaliados) | {c['fora_do_contexto']} |"
    )


def _vias_md(vias):
    return [f"- {_NOME_VIA[v]}: {t}" for v, t in vias]


def render_relatorio(res, av, catalog):
    ctx = av["contexto"]
    fontes = ", ".join(_NOME_FONTE[f].lower() for f in ctx["fontes"])
    linhas = [
        GENERATED,
        f"# Relatório vygolint — {av['jogo']}",
        "",
        f"- Data: {av['data']}",
        f"- Avaliador: {av['avaliador']}",
        f"- Aplicado em sala de aula: {'sim' if ctx['sala_de_aula'] else 'não'}",
        f"- Fontes de evidência: {fontes}",
        "",
        "## 1. Cláusula",
        "",
        f"> {CLAUSULA}",
        "",
        "## 2. Nível alcançado",
        "",
        f"**Nível alcançado: {_NOME_GRAU.get(res['nivel'], res['nivel'])}**",
        "",
        "## 3. Cobertura por nível",
        "",
        "| Nível | Atendidos | Parciais | Não atendidos | Fora do contexto |",
        "|---|---|---|---|---|",
    ]
    for n in NIVEIS:
        linhas.append(_linha_contagem(n, res["cobertura_nivel"][n]))
    linhas += [
        "",
        "## 4. Cobertura por categoria",
        "",
        "| Categoria | Atendidos | Parciais | Não atendidos | Fora do contexto |",
        "|---|---|---|---|---|",
    ]
    for chave, c in res["cobertura_categoria"].items():
        linhas.append(_linha_contagem(_nome_categoria(chave, catalog), c))
    linhas += ["", "## 5. Bloqueios", ""]
    proximo = {"sem_conformidade": "A", "A": "AA", "AA": "AAA", "AAA": None}[res["nivel"]]
    if proximo is None:
        linhas.append("Nenhum: o jogo alcançou AAA.")
    elif not res["bloqueios"]:
        linhas.append(f"Nenhum critério {proximo} bloqueia o próximo nível.")
    else:
        linhas.append(f"Critérios que impedem o nível {proximo}:")
        for b in res["bloqueios"]:
            linhas += ["", f"#### {b['id']} — Nível {b['nivel']} — {_NOME_GRAU[b['grau']]}", "", f"**Enunciado.** {b['enunciado']}", ""]
            if b["nota"]:
                linhas.append(f"- Nota: {b['nota']}")
            linhas += _vias_md(b["vias"])
    linhas += ["", "## 6. Parciais", ""]
    if not res["parciais"]:
        linhas.append("Nenhum critério parcial.")
    for p in res["parciais"]:
        linhas += [
            f"#### {p['id']} — Nível {p['nivel']}",
            "",
            f"**Enunciado.** {p['enunciado']}",
            "",
            f"- Estado: {p['escala_parcial']}",
            f"- Falta: {p['escala_atendido']}",
        ]
        linhas += _vias_md(p["vias"])
        linhas.append("")
    linhas += ["## 7. Provas por critério", ""]
    for cid in sorted(res["criterios"]):
        c = res["criterios"][cid]
        entrada = av["criterios"][cid]
        linhas.append(f"### {cid} — {_NOME_GRAU[c['grau']]}")
        if c["grau_declarado"] != c["grau"]:
            linhas.append(f"- Grau declarado: {_NOME_GRAU[c['grau_declarado']]}")
        if c["nota"]:
            linhas.append(f"- Nota: {c['nota']}")
        if entrada.get("razao"):
            linhas.append(f"- Razão: {entrada['razao']}")
        if entrada.get("justificativa_conflito"):
            linhas.append(f"- Justificativa do conflito entre fontes: {entrada['justificativa_conflito']}")
        for nome in FONTES:
            f = (entrada.get("fontes") or {}).get(nome)
            if not f:
                continue
            linhas.append(f"- {_NOME_FONTE[nome]} ({_NOME_GRAU[f['grau']]}):")
            linhas += [f"  - {p}" for p in f["provas"]]
            if f.get("observacao"):
                linhas.append(f"  - Observação: {f['observacao']}")
        linhas.append("")
    while linhas and linhas[-1] == "":
        linhas.pop()
    linhas += ["", "---", "", RODAPE]
    return "\n".join(linhas).rstrip() + "\n"


def render_resultado(res, av):
    doc = {
        "jogo": av["jogo"],
        "data": str(av["data"]),
        "avaliador": av["avaliador"],
        "nivel": res["nivel"],
        "criterios": {
            cid: {"nivel": c["nivel"], "grau": c["grau"], "grau_declarado": c["grau_declarado"], "nota": c["nota"]}
            for cid, c in sorted(res["criterios"].items())
        },
    }
    return yaml.safe_dump(doc, allow_unicode=True, sort_keys=False)


def build_report(avaliacao_path, catalog_dir, out_dir, strict=False, warnings=None, bases=None):
    """Return errors; on success writes relatorio.md, relatorio.html and resultado.yaml into out_dir.

    Proof lint findings (lint.py) are appended to `warnings` when a list is given. They do not block
    the report unless `strict` is true, in which case they are returned as errors and nothing is
    written. `bases` are the folders cited paths are tried against (default: the folder of the
    evaluation, its parent and the current directory).
    """
    from .catalog import load_catalog
    from .html import render_relatorio_html
    from .lint import lint_avaliacao

    avaliacao_path = Path(avaliacao_path)
    out_dir = Path(out_dir)
    catalog, errors = load_catalog(catalog_dir)
    if errors:
        return errors
    try:
        av = load_avaliacao(avaliacao_path)
    except OSError as exc:
        return [f"{avaliacao_path.name}: não foi possível ler o arquivo: {exc}"]
    except (yaml.YAMLError, ValueError) as exc:
        return [f"{avaliacao_path.name}: YAML inválido: {exc}"]
    errors = validate_avaliacao(av, catalog)
    if errors:
        return errors
    if bases is None:
        pasta = avaliacao_path.resolve().parent
        bases = list(dict.fromkeys([pasta, pasta.parent, Path.cwd()]))
    avisos = lint_avaliacao(av, bases, pasta=avaliacao_path.resolve().parent)
    if warnings is not None:
        warnings.extend(avisos)
    if strict and avisos:
        return avisos
    res = aggregate(av, catalog)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "relatorio.md").write_text(render_relatorio(res, av, catalog), encoding="utf-8")
    (out_dir / "relatorio.html").write_text(render_relatorio_html(res, av, catalog), encoding="utf-8")
    (out_dir / "resultado.yaml").write_text(render_resultado(res, av), encoding="utf-8")
    return []
