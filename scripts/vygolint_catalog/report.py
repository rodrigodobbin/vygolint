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
        fontes = [f for f in (fontes or []) if f in FONTES]
    artefatos = ctx.get("artefatos")
    if not isinstance(artefatos, dict) or any(k not in FONTES for k in artefatos):
        errors.append("avaliacao: contexto.artefatos deve ser mapa fonte -> lista de caminhos")
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
            errors.append(f"{cid}: fonte {nome} com observacao vazia")
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
        if grau in ("nao_avaliado", "fora_do_contexto") and not _is_text(entrada.get("razao")):
            errors.append(f"{cid}: razao obrigatória para grau {grau}")
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
    """Return {id: (grau_efetivo, nota)} after applying depende_de (fixed point; cycles are a catalog error)."""
    efetivo = {cid: (g, None) for cid, g in declarados.items()}
    for _ in range(len(efetivo) + 1):
        mudou = False
        for cid, item in catalog["criterios"].items():
            grau_decl = declarados[cid]
            if grau_decl == "fora_do_contexto":
                continue
            novo = (grau_decl, None)
            for grupo in item["criterio"]["depende_de"]:
                estados = [efetivo[alvo][0] for alvo in grupo]
                if "atendido" in estados:
                    continue
                alvos = " ou ".join(grupo)
                if "nao_avaliado" in estados and all(e in ("nao_avaliado", "parcial", "nao_atendido") for e in estados):
                    if novo[0] != "nao_atendido":
                        novo = ("nao_avaliado", f"não avaliado por dependência de critério não avaliado ({alvos})")
                else:
                    novo = ("nao_atendido", f"não atendido por dependência não satisfeita ({alvos})")
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
