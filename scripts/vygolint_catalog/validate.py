"""Structural and cross-file validation of catalog YAML (spec sections 5 and 6)."""

import re
from pathlib import Path

import yaml


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


def _validate_criterio(c, diretriz_id, schema, errors):
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
        if not isinstance(cid, str) or not re.match(cs["id_padrao"], cid):
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


def validate_diretriz(d, schema, categorias):
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
    if "id" in d and (not isinstance(did, str) or not re.match(ds["id_padrao"], did)):
        errors.append(f"{prefix}: id de diretriz fora do padrão Dnn")
    chaves = {c["chave"] for c in categorias["categorias"]}
    if "categoria" in d and d["categoria"] not in chaves:
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
                _validate_criterio(c, did, schema, errors)
    return errors
