"""Structural and cross-file validation of catalog YAML (spec sections 5 and 6)."""

import re
from pathlib import Path

import yaml

from .levels import derive_nivel


def load_yaml(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def _is_text(value):
    return isinstance(value, str) and value.strip() != ""


def _check_evidencia_fonte(prefix, nome, fonte, errors):
    if fonte is None:
        return False
    if not isinstance(fonte, dict):
        errors.append(f"{prefix}: evidencia.{nome} deve ser null ou mapa")
        return False
    if not _is_text(fonte.get("procedimento")):
        errors.append(f"{prefix}: evidencia.{nome}.procedimento ausente ou vazio")
    indicadores = fonte.get("indicadores")
    if not isinstance(indicadores, list) or not indicadores or not all(_is_text(i) for i in indicadores):
        errors.append(f"{prefix}: evidencia.{nome}.indicadores deve ser lista não vazia de textos")
    return True


_INLINE_RE = re.compile(r"Defini(ções|ção):")


def textos_do_criterio(c):
    """Return [(campo, texto)] for every text field the lint covers (not nivel_justificativa)."""
    out = []
    if _is_text(c.get("enunciado")):
        out.append(("enunciado", c["enunciado"]))
    ev = c.get("evidencia") if isinstance(c.get("evidencia"), dict) else {}
    for nome in ("codigo", "documentacao", "video"):
        fonte = ev.get(nome)
        if isinstance(fonte, dict):
            if _is_text(fonte.get("procedimento")):
                out.append((f"{nome}.procedimento", fonte["procedimento"]))
            for i, ind in enumerate(fonte.get("indicadores") or []):
                if _is_text(ind):
                    out.append((f"{nome}.indicadores[{i}]", ind))
    esc = c.get("escala") if isinstance(c.get("escala"), dict) else {}
    for grau in ("atendido", "parcial", "nao_atendido"):
        if _is_text(esc.get(grau)):
            out.append((f"escala.{grau}", esc[grau]))
    return out


def _validate_definicoes_criterio(c, prefix, schema, glossario, errors):
    defs = c.get("definicoes", {})
    if defs is None:
        defs = {}
    if not isinstance(defs, dict):
        errors.append(f"{prefix}: definicoes deve ser mapa")
        return
    permitidas = set(schema["criterio"]["definicoes"]["chaves"])
    extras = set(defs) - permitidas
    if extras:
        errors.append(f"{prefix}: definicoes com chaves desconhecidas: {sorted(extras)}")
    chaves = defs.get("glossario") or []
    if not isinstance(chaves, list) or not all(isinstance(k, str) for k in chaves):
        errors.append(f"{prefix}: definicoes.glossario deve ser lista de chaves")
        chaves = []
    for k in chaves:
        if k not in glossario:
            errors.append(f"{prefix}: definicoes.glossario cita chave inexistente: {k}")
    if len(set(chaves)) != len(chaves):
        errors.append(f"{prefix}: definicoes.glossario com chave repetida")
    locais = defs.get("locais") or {}
    if not isinstance(locais, dict) or not all(_is_text(k) and _is_text(v) for k, v in locais.items()):
        errors.append(f"{prefix}: definicoes.locais deve ser mapa termo -> texto não vazio")
        locais = {}
    comuns = defs.get("termos_comuns") or {}
    if not isinstance(comuns, dict) or not all(_is_text(k) and _is_text(v) for k, v in comuns.items()):
        errors.append(f"{prefix}: definicoes.termos_comuns deve ser mapa gatilho -> justificativa não vazia")
        comuns = {}
    gatilho_para_chave = {g: e["chave"] for e in glossario.values() for g in e["gatilhos"]}
    for g in comuns:
        if g not in gatilho_para_chave:
            errors.append(f"{prefix}: definicoes.termos_comuns cita gatilho desconhecido: {g!r}")
        elif gatilho_para_chave[g] in chaves:
            errors.append(
                f"{prefix}: definicoes.termos_comuns lista {g!r} mas glossario também lista {gatilho_para_chave[g]}"
            )
    campos = textos_do_criterio(c)
    for campo, texto in campos:
        if _INLINE_RE.search(texto):
            errors.append(f"{prefix}: {campo} contém definição inline ('Definição:'/'Definições:'); use o campo definicoes")
        for e in glossario.values():
            if e["texto"] in texto:
                errors.append(f"{prefix}: {campo} repete o texto do glossário de {e['chave']}; use definicoes.glossario")
    corpus_proprio = " ".join(t for _, t in campos).lower()
    corpus_base = corpus_proprio + " " + " ".join(locais.values()).lower()
    for e in glossario.values():
        # A key's own text never counts as use of its own trigger; other listed keys' texts do (cascade).
        corpus = corpus_base + " " + " ".join(
            glossario[k]["texto"].lower() for k in chaves if k in glossario and k != e["chave"]
        )
        usados = [g for g in e["gatilhos"] if g.lower() in corpus]
        listado = e["chave"] in chaves
        comum = any(g in comuns for g in e["gatilhos"])
        if usados and not listado and not comum:
            errors.append(
                f"{prefix}: texto usa \"{usados[0]}\" mas definicoes.glossario não lista \"{e['chave']}\""
            )
        if listado and not usados:
            errors.append(f"{prefix}: definicoes.glossario lista \"{e['chave']}\" mas nenhum gatilho aparece no texto")
    for g in comuns:
        if g.lower() not in corpus_proprio:
            errors.append(f"{prefix}: definicoes.termos_comuns lista {g!r} mas o termo não aparece no texto")


def _validate_criterio(c, diretriz_id, schema, errors, glossario=None):
    cs = schema["criterio"]
    cid = c.get("id") if isinstance(c, dict) else None
    prefix = f"{diretriz_id}/{cid or '?'}"
    if not isinstance(c, dict):
        errors.append(f"{prefix}: criterio deve ser mapa")
        return
    for campo in cs["obrigatorios"]:
        if campo not in c:
            errors.append(f"{prefix}: campo obrigatório ausente: {campo}")
    if "id" in c:
        if not isinstance(cid, str) or not re.fullmatch(cs["id_padrao"], cid):
            errors.append(f"{prefix}: id de critério fora do padrão")
        elif not cid.startswith(f"{diretriz_id}."):
            errors.append(f"{prefix}: id de critério não pertence à diretriz {diretriz_id}")
    if "nivel" in c and c["nivel"] not in cs["nivel"]:
        errors.append(f"{prefix}: nivel inválido: {c['nivel']!r}")
    if "enunciado" in c and not _is_text(c["enunciado"]):
        errors.append(f"{prefix}: enunciado vazio")
    nj = c.get("nivel_justificativa")
    if "nivel_justificativa" in c:
        if not isinstance(nj, dict):
            errors.append(f"{prefix}: nivel_justificativa deve ser mapa")
        else:
            if nj.get("essencialidade") not in cs["essencialidade"]:
                errors.append(f"{prefix}: essencialidade inválida: {nj.get('essencialidade')!r}")
            if nj.get("viabilidade") not in cs["viabilidade"]:
                errors.append(f"{prefix}: viabilidade inválida: {nj.get('viabilidade')!r}")
            if not _is_text(nj.get("texto")):
                errors.append(f"{prefix}: nivel_justificativa.texto vazio")
    ev = c.get("evidencia")
    if "evidencia" in c:
        if not isinstance(ev, dict):
            errors.append(f"{prefix}: evidencia deve ser mapa")
        else:
            presentes = 0
            for nome in cs["fontes_evidencia"]:
                if nome not in ev:
                    errors.append(f"{prefix}: evidencia.{nome} ausente (use null se não se aplica)")
                    continue
                if _check_evidencia_fonte(prefix, nome, ev[nome], errors):
                    presentes += 1
            extras = set(ev) - set(cs["fontes_evidencia"])
            if extras:
                errors.append(f"{prefix}: evidencia com chaves desconhecidas: {sorted(extras)}")
            if presentes == 0:
                errors.append(f"{prefix}: evidencia precisa de ao menos uma fonte não nula")
    esc = c.get("escala")
    if "escala" in c:
        if not isinstance(esc, dict):
            errors.append(f"{prefix}: escala deve ser mapa")
        else:
            for grau in cs["escala"]:
                if not _is_text(esc.get(grau)):
                    errors.append(f"{prefix}: escala.{grau} ausente ou vazio")
    dep = c.get("depende_de")
    if "depende_de" in c:
        ok = isinstance(dep, list) and all(
            isinstance(g, list) and g and all(isinstance(i, str) for i in g) for g in dep
        )
        if not ok:
            errors.append(f"{prefix}: depende_de deve ser lista de grupos (lista de listas de ids)")
    if glossario is not None:
        _validate_definicoes_criterio(c, prefix, schema, glossario, errors)


def validate_diretriz(d, schema, categorias, glossario=None):
    """Return a list of error strings for one guideline dict. Empty list means valid."""
    errors = []
    ds = schema["diretriz"]
    did = d.get("id") if isinstance(d, dict) else None
    prefix = did or "?"
    if not isinstance(d, dict):
        return [f"{prefix}: diretriz deve ser mapa"]
    for campo in ds["obrigatorios"]:
        if campo not in d:
            errors.append(f"{prefix}: campo obrigatório ausente: {campo}")
    if "id" in d and (not isinstance(did, str) or not re.fullmatch(ds["id_padrao"], did)):
        errors.append(f"{prefix}: id de diretriz fora do padrão Dnn")
    chaves = {c["chave"] for c in categorias["categorias"]}
    if "categoria" in d and not (isinstance(d["categoria"], str) and d["categoria"] in chaves):
        errors.append(f"{prefix}: categoria desconhecida: {d['categoria']!r}")
    if "diretriz" in d and not _is_text(d["diretriz"]):
        errors.append(f"{prefix}: texto da diretriz vazio")
    if "fonte" in d and not _is_text(d["fonte"]):
        errors.append(f"{prefix}: fonte vazia")
    if "modalidade" in d and d["modalidade"] not in ds["modalidade"]:
        errors.append(f"{prefix}: modalidade inválida: {d['modalidade']!r}")
    if "aplicabilidade" in d and d["aplicabilidade"] is not None and not _is_text(d["aplicabilidade"]):
        errors.append(f"{prefix}: aplicabilidade deve ser null ou texto não vazio")
    crit = d.get("criterios")
    if "criterios" in d:
        if not isinstance(crit, list) or not crit:
            errors.append(f"{prefix}: criterios deve ser lista não vazia")
        elif isinstance(did, str):
            for c in crit:
                _validate_criterio(c, did, schema, errors, glossario)
    return errors


def validate_catalogo(diretrizes):
    """Cross-file checks over structurally valid guidelines."""
    errors = []
    vistos_d = set()
    vistos_c = set()
    for d in diretrizes:
        if d["id"] in vistos_d:
            errors.append(f"{d['id']}: id de diretriz duplicado")
        vistos_d.add(d["id"])
        for c in d["criterios"]:
            if c["id"] in vistos_c:
                errors.append(f"{d['id']}/{c['id']}: id de critério duplicado")
            vistos_c.add(c["id"])
    for d in diretrizes:
        for c in d["criterios"]:
            prefix = f"{d['id']}/{c['id']}"
            nj = c["nivel_justificativa"]
            esperado = derive_nivel(nj["essencialidade"], nj["viabilidade"], d["modalidade"])
            if c["nivel"] != esperado:
                errors.append(
                    f"{prefix}: nivel declarado {c['nivel']} mas esperado {esperado} "
                    f"(essencialidade {nj['essencialidade']}, viabilidade {nj['viabilidade']}, modalidade {d['modalidade']})"
                )
            for grupo in c["depende_de"]:
                for alvo in grupo:
                    if alvo == c["id"]:
                        errors.append(f"{prefix}: depende_de aponta para si mesmo")
                    elif alvo not in vistos_c:
                        errors.append(f"{prefix}: depende_de aponta para critério inexistente: {alvo}")
    return errors


_CHAVE_RE = re.compile(r"^[a-z][a-z0-9_]*$")


def validate_definicoes(doc):
    """Return a list of error strings for the glossary document (catalog/definicoes.yaml)."""
    errors = []
    if not isinstance(doc, dict) or not isinstance(doc.get("termos"), list):
        return ["definicoes.yaml: documento deve ser mapa com lista `termos`"]
    chaves = set()
    gatilhos = {}
    for i, e in enumerate(doc["termos"]):
        prefix = f"definicoes.yaml/{e.get('chave') if isinstance(e, dict) else i}"
        if not isinstance(e, dict):
            errors.append(f"{prefix}: entrada deve ser mapa")
            continue
        for campo in ("chave", "termo", "gatilhos", "ancora", "texto"):
            if campo not in e:
                errors.append(f"{prefix}: campo obrigatório ausente: {campo}")
        chave = e.get("chave")
        if not isinstance(chave, str) or not _CHAVE_RE.fullmatch(chave):
            errors.append(f"{prefix}: chave fora do padrão [a-z][a-z0-9_]*")
        elif chave in chaves:
            errors.append(f"{prefix}: chave duplicada: {chave}")
        else:
            chaves.add(chave)
        for campo in ("termo", "ancora", "texto"):
            if campo in e and not _is_text(e[campo]):
                errors.append(f"{prefix}: {campo} vazio")
        gs = e.get("gatilhos")
        if "gatilhos" in e and (not isinstance(gs, list) or not gs or not all(_is_text(g) for g in gs)):
            errors.append(f"{prefix}: gatilhos deve ser lista não vazia de textos")
        elif isinstance(gs, list):
            for g in gs:
                if g in gatilhos:
                    errors.append(f"{prefix}: gatilho {g!r} já usado por {gatilhos[g]}")
                gatilhos[g] = chave
    return errors


def load_definicoes(path):
    """Load catalog/definicoes.yaml and return {chave: entrada}. Assumes validate_definicoes passed."""
    doc = load_yaml(path)
    return {e["chave"]: e for e in doc["termos"]}
