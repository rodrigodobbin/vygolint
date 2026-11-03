#!/usr/bin/env python3
"""One-shot check: the migrated catalog differs from the stage-1 text only by accepted changes.

Usage: python3 scripts/verify_definicoes.py [--base main] [--only D28,D39] [--catalog DIR] [--aceitas FILE]

For every criterion it checks that
  1. the text outside the definitions is unchanged (after removing the stage-1 definition blocks with
     the same extractor the migration used, and ignoring ", nos termos das definições" on both sides),
     except for the accepted `campos` edits;
  2. the set of definition clauses is unchanged (stage-1 blocks vs. glossary keys + `locais`), except
     for the accepted `clausulas` substitutions, `adicoes` and `remocoes`;
  3. nothing else in the criterion or the diretriz changed (nivel, nivel_justificativa, depende_de, …).

Clauses are compared in a canonical form, `termo = corpo`, where `termo`/`corpo` come from the same
parser the migration used to build the `locais` keys (`_definicao`), so a local definition created by
`migrate_definicoes.py` always verifies against the clause it came from. Clauses that open no term are
compared as written (whitespace collapsed, final period dropped). Accepted entries use this form; the
messages print it ready to paste.

Exit 1 on any unaccepted difference.
"""

import argparse
import copy
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from migrate_definicoes import _definicao, clausulas, extrair_blocos  # noqa: E402
from vygolint_catalog.validate import load_definicoes, textos_do_criterio  # noqa: E402

_PONTEIRO_RE = re.compile(r",? nos termos das definições")


def _ws(s):
    return re.sub(r"\s+", " ", s).strip()


def _norm_campo(s):
    return _ws(s).rstrip(".;:, ").strip()


def _norm_clausula(s):
    return _ws(s).rstrip(".").strip()


def _canon(cl):
    """Canonical form of one stage-1 clause: 'termo = corpo' when it opens a definition, else as written."""
    termo, corpo = _definicao(_ws(cl))
    return _norm_clausula(f"{termo} = {corpo}" if termo else cl)


def _clausulas_de_corpo(corpo):
    return [_canon(c) for c in clausulas(corpo)]


def _clausulas_de_definicao(termo, texto):
    """Clauses of a stored definition (glossary entry or local): the first one gets the term."""
    cls = clausulas(texto)
    if not cls:
        return [_norm_clausula(f"{termo} =")]
    return [_norm_clausula(f"{termo} = {cls[0]}")] + [_canon(c) for c in cls[1:]]


def _termo_glossario(entrada):
    return entrada["termo"].split(" (")[0]


def _clausulas_da_chave(glossario, chave):
    return _clausulas_de_definicao(_termo_glossario(glossario[chave]), glossario[chave]["texto"])


def _defs(c):
    defs = c.get("definicoes")
    return defs if isinstance(defs, dict) else {}


def _clausulas_novas(c, glossario, cid, diffs):
    """{clausula: origem} for the new format; unknown glossary keys are reported, not raised."""
    out = {}
    defs = _defs(c)
    for k in defs.get("glossario") or []:
        if k not in glossario:
            diffs.append(f"{cid}: chave do glossário inexistente: {k}")
            continue
        for cl in _clausulas_da_chave(glossario, k):
            out.setdefault(cl, f"glossario: {k}")
    for termo, texto in (defs.get("locais") or {}).items():
        for cl in _clausulas_de_definicao(str(termo), str(texto)):
            out.setdefault(cl, f"locais: {termo}")
    return out


def _aplica(a, cid, padrao=None):
    """Entry applies to criterion cid. Only `clausulas` may omit `criterio` (padrao "*")."""
    return a.get("criterio", padrao) in ("*", cid)


def _estrutura(c):
    """Criterion without its text fields and definitions: what must not change at all."""
    c = copy.deepcopy(c)
    c.pop("definicoes", None)
    if isinstance(c.get("enunciado"), str):
        c["enunciado"] = "…"
    for fonte in (c.get("evidencia") or {}).values() if isinstance(c.get("evidencia"), dict) else []:
        if isinstance(fonte, dict):
            if isinstance(fonte.get("procedimento"), str):
                fonte["procedimento"] = "…"
            if isinstance(fonte.get("indicadores"), list):
                fonte["indicadores"] = ["…" if isinstance(i, str) else i for i in fonte["indicadores"]]
    if isinstance(c.get("escala"), dict):
        c["escala"] = {g: "…" if isinstance(v, str) else v for g, v in c["escala"].items()}
    return c


def comparar_criterio(antigo, novo, glossario, aceitas):
    """Unaccepted differences between a stage-1 criterion and its migrated version ([] when they match)."""
    cid = novo.get("id") or antigo.get("id")
    diffs = []
    campos_ac = [a for a in aceitas.get("campos") or [] if _aplica(a, cid)]

    # 3. Non-text fields.
    ea, en = _estrutura(antigo), _estrutura(novo)
    for k in list(ea) + [k for k in en if k not in ea]:
        if ea.get(k) != en.get(k):
            diffs.append(f"{cid} {k}: campo não textual mudou\n  etapa 1: {ea.get(k)!r}\n  agora:   {en.get(k)!r}")

    # 1. Text outside the definitions; collect the stage-1 clauses on the way.
    antigos = dict(textos_do_criterio(antigo))
    novos = dict(textos_do_criterio(novo))
    velhas = {}  # clausula -> campo de origem
    removidos = set()
    for campo in list(antigos) + [c for c in novos if c not in antigos]:
        texto = antigos.get(campo, "")
        for i, a in enumerate(campos_ac):
            if "remover" in a and a.get("campo") in ("*", campo) and a["remover"] and a["remover"] in texto:
                texto = texto.replace(a["remover"], "")
                removidos.add(i)
                for cl in _clausulas_de_corpo(a["remover"].strip(" ,;.").removeprefix("e ")):
                    velhas.setdefault(cl, campo)
        sem_defs, blocos = extrair_blocos(texto, cadeia=(campo == "enunciado"))
        for b in blocos:
            for cl in _clausulas_de_corpo(b):
                velhas.setdefault(cl, campo)
        # The pointer is stripped on both sides: stage 1 already used it outside the blocks (D29).
        esperado = _norm_campo(_PONTEIRO_RE.sub("", sem_defs)) if campo in antigos else "(campo inexistente)"
        obtido = _norm_campo(_PONTEIRO_RE.sub("", novos[campo])) if campo in novos else "(campo inexistente)"
        if esperado != obtido:
            ok = any(
                "de" in a and a.get("campo") == campo and _norm_campo(a["de"]) == esperado and _norm_campo(a.get("para", "")) == obtido
                for a in campos_ac
            )
            if not ok:
                diffs.append(f"{cid} {campo}: texto fora das definições mudou\n  etapa 1: {esperado}\n  agora:   {obtido}")
    for i, a in enumerate(campos_ac):
        if "remover" in a and i not in removidos:
            diffs.append(f"{cid}: remover aceito não encontrado (campo {a.get('campo')}): {a['remover']!r}")

    # 2. Definition clauses.
    mapa = {}
    for a in aceitas.get("clausulas") or []:
        if _aplica(a, cid, "*") and a.get("de"):
            para = a.get("para")
            mapa[_norm_clausula(a["de"])] = [para] if isinstance(para, str) else list(para or [])
    mapeadas = {}  # clausula -> clausula da etapa 1 que a originou
    for v in velhas:
        for p in mapa.get(v, [v]):
            mapeadas.setdefault(_norm_clausula(p), v)
    novas = _clausulas_novas(novo, glossario, cid, diffs)
    remocoes = {_norm_clausula(a["clausula"]) for a in aceitas.get("remocoes") or [] if _aplica(a, cid) and a.get("clausula")}
    adicoes = set()
    for a in aceitas.get("adicoes") or []:
        if not _aplica(a, cid):
            continue
        if a.get("chave") in glossario:
            adicoes |= set(_clausulas_da_chave(glossario, a["chave"]))
        elif a.get("clausula"):
            adicoes.add(_norm_clausula(a["clausula"]))
    for m in sorted(set(mapeadas) - set(novas)):
        if m not in remocoes:
            origem = mapeadas[m]
            via = f" (mapeada de: {origem})" if origem != m else ""
            diffs.append(f"{cid}: definição da etapa 1 sem correspondente [{velhas[origem]}]: {m}{via}")
    for n in sorted(set(novas) - set(mapeadas)):
        if n not in adicoes:
            diffs.append(f"{cid}: definição nova não aceita [{novas[n]}]: {n}")
    return diffs


def comparar_diretriz(antigo, novo, glossario, aceitas):
    """Diretriz-level fields must not change; criteria are paired by id and compared one by one."""
    did = novo.get("id") or antigo.get("id")
    diffs = []
    for k in list(antigo) + [k for k in novo if k not in antigo]:
        if k != "criterios" and antigo.get(k) != novo.get(k):
            diffs.append(f"{did} {k}: campo da diretriz mudou\n  etapa 1: {antigo.get(k)!r}\n  agora:   {novo.get(k)!r}")
    velhos = {c.get("id"): c for c in antigo.get("criterios") or []}
    novos = {c.get("id"): c for c in novo.get("criterios") or []}
    for cid in velhos:
        if cid not in novos:
            diffs.append(f"{cid}: critério da etapa 1 ausente no catálogo")
    for cid, c in novos.items():
        if cid not in velhos:
            diffs.append(f"{cid}: critério novo, inexistente na etapa 1")
        else:
            diffs += comparar_criterio(velhos[cid], c, glossario, aceitas)
    if [i for i in velhos if i in novos] != [i for i in novos if i in velhos]:
        diffs.append(f"{did}: ordem dos critérios mudou")
    return diffs


def _git_show(catalog, base, nome):
    """File `nome` of the catalog directory at revision `base`, or None if it does not exist there."""
    r = subprocess.run(["git", "-C", str(catalog), "show", f"{base}:./{nome}"], capture_output=True)
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


def _git_ls(catalog, base):
    r = subprocess.run(["git", "-C", str(catalog), "ls-tree", "--name-only", base, "--", "."], capture_output=True, check=True)
    return {Path(p).name for p in r.stdout.decode("utf-8").split()}


def _parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="main", help="git revision with the stage-1 catalog (default: main)")
    ap.add_argument("--only", default="", help="comma-separated diretriz ids, e.g. D28,D39")
    ap.add_argument("--catalog", default=str(REPO / "catalog"), help="catalog directory (inside a git work tree)")
    ap.add_argument("--aceitas", default=str(REPO / "scripts" / "definicoes_aceitas.yaml"), help="accepted-differences file")
    return ap


def main(argv=None):
    args = _parser().parse_args(argv)
    catalog = Path(args.catalog)
    glossario = load_definicoes(catalog / "definicoes.yaml")
    aceitas = yaml.safe_load(Path(args.aceitas).read_text(encoding="utf-8")) or {}
    only = {s.strip() for s in args.only.split(",") if s.strip()}
    atuais = {p.name for p in catalog.glob("D*.yaml")}
    base_nomes = {n for n in _git_ls(catalog, args.base) if re.fullmatch(r"D.*\.yaml", n)}
    total = 0
    for nome in sorted(atuais | base_nomes):
        stem = nome.removesuffix(".yaml")
        if only and stem not in only:
            continue
        if nome not in atuais:
            diffs = [f"{stem}: arquivo existe em {args.base} mas não no catálogo"]
        else:
            texto_antigo = _git_show(catalog, args.base, nome)
            if texto_antigo is None:
                diffs = [f"{stem}: arquivo não existe em {args.base}"]
            else:
                antigo = yaml.safe_load(texto_antigo)
                novo = yaml.safe_load((catalog / nome).read_text(encoding="utf-8"))
                diffs = comparar_diretriz(antigo, novo, glossario, aceitas)
        for d in diffs:
            print(d)
        total += len(diffs)
    print(f"{total} diferença(s) não aceita(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
