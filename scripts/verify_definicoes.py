#!/usr/bin/env python3
"""One-shot check: the migrated catalog differs from the stage-1 text only by accepted changes.

Usage: python3 scripts/verify_definicoes.py [--base main] [--only D28,D39] [--catalog DIR] [--aceitas FILE]

For every criterion it checks that
  1. the text outside the definitions is unchanged (after removing the stage-1 definition blocks with
     the same extractor the migration used, and ignoring ", nos termos das definições" on both sides),
     except for the accepted `campos` edits and the global `frases` substitutions (each `de` phrase of
     the stage-1 text, after the definition blocks are removed, is replaced by its `para` before comparing);
  2. the set of definition clauses is unchanged (stage-1 blocks vs. glossary keys + `locais`), except
     for the accepted `clausulas` substitutions, `adicoes` and `remocoes`;
  3. nothing else in the criterion or the diretriz changed (nivel, nivel_justificativa, depende_de, …).

Clauses are compared in a canonical form, `termo = corpo`, where `termo`/`corpo` come from the same
parser the migration used to build the `locais` keys (`_definicao`), so a local definition created by
`migrate_definicoes.py` always verifies against the clause it came from. Clauses that open no term are
compared as written (whitespace collapsed, final period dropped). Accepted entries use this form; the
messages print it ready to paste.

Accepted entries are validated up front: a malformed entry (e.g. a `clausulas` entry without `para`,
an unknown `tipo`, `tipo: decisao` without `decisao`, a `frases` entry with `criterio`) is reported and
never applied. Every entry that was never used in the run is reported too ("aceitas não usadas"); with
--only, entries scoped to "*" (`frases` included) or to a diretriz outside --only are not checked for use.

Exit 1 on any unaccepted difference, malformed or unused accepted entry, or --only id without a file.
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

_PONTEIRO_RE = re.compile(r",? \bnos termos das definições\b")
_LISTAS = ("clausulas", "adicoes", "remocoes", "campos", "frases")
_TIPOS = ("equivalente", "decisao")


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


def _str(v):
    return isinstance(v, str) and v.strip() != ""


def _erro_entrada(lista, a):
    """Why accepted entry `a` of `lista` is malformed, or None when it is well formed."""
    if not isinstance(a, dict):
        return "não é mapa"
    if lista == "frases":
        if "criterio" in a:
            return "frases são globais (sem 'criterio')"
    elif "criterio" in a or lista != "clausulas":
        if not _str(a.get("criterio")):
            return "sem 'criterio'"
    if "tipo" in a or lista == "clausulas":
        if a.get("tipo") not in _TIPOS:
            return f"'tipo' deve ser {' ou '.join(_TIPOS)}: {a.get('tipo')!r}"
        if a["tipo"] == "decisao" and (a.get("decisao") is None or a.get("decisao") == ""):
            return "tipo decisao sem 'decisao'"
    if lista == "clausulas":
        if not _str(a.get("de")):
            return "sem 'de'"
        para = a.get("para")
        if not (_str(para) or (isinstance(para, list) and para and all(_str(x) for x in para))):
            return "sem 'para'"
    elif lista == "adicoes":
        if not (_str(a.get("chave")) or _str(a.get("clausula"))):
            return "sem 'chave' nem 'clausula'"
    elif lista == "remocoes":
        if not _str(a.get("clausula")):
            return "sem 'clausula'"
    elif lista == "campos":
        if not _str(a.get("campo")):
            return "sem 'campo'"
        if "remover" in a:
            if "de" in a or "para" in a:
                return "'remover' junto com 'de'/'para'"
            if not _str(a["remover"]):
                return "sem 'remover'"
        else:
            if a["campo"] == "*":
                return "campo '*' só com 'remover'"
            if not _str(a.get("de")):
                return "sem 'de'"
            if not isinstance(a.get("para"), str):
                return "sem 'para'"
    elif lista == "frases":
        if not _str(a.get("de")):
            return "sem 'de'"
        if not _str(a.get("para")):
            return "sem 'para'"
    return None


def validar_aceitas(aceitas):
    """Messages for every malformed accepted entry (and non-list sections); [] when all are well formed."""
    if not isinstance(aceitas, dict):
        return ["aceitas: o arquivo deve ser um mapa"]
    erros = []
    for lista in _LISTAS:
        itens = aceitas.get(lista)
        if itens is None:
            continue
        if not isinstance(itens, list):
            erros.append(f"aceitas: {lista} não é lista")
            continue
        for i, a in enumerate(itens):
            erro = _erro_entrada(lista, a)
            if erro:
                erros.append(f"aceitas: {lista}[{i}] {erro}")
    return erros


def _entradas(aceitas, lista):
    """[(id, entrada)] for the well-formed entries of `lista`; malformed ones are skipped (main reports them)."""
    itens = aceitas.get(lista) if isinstance(aceitas, dict) else None
    if not isinstance(itens, list):
        return []
    return [(f"{lista}[{i}]", a) for i, a in enumerate(itens) if _erro_entrada(lista, a) is None]


def _descreve(a):
    campos = ("criterio", "campo", "de", "chave", "clausula", "remover")
    return " ".join(f"{k}={a[k]}" for k in campos if k in a)


def _aplica(a, cid, padrao=None):
    """Entry applies to criterion cid. Only `clausulas` may omit `criterio` (padrao "*")."""
    return a.get("criterio", padrao) in ("*", cid)


def _caminho(campo):
    """Path inside the criterion of a field name from textos_do_criterio ("codigo.indicadores[1]", …)."""
    partes = []
    for p in campo.split("."):
        m = re.fullmatch(r"(.+)\[(\d+)\]", p)
        partes += [m.group(1), int(m.group(2))] if m else [p]
    return partes if partes[0] in ("enunciado", "escala") else ["evidencia"] + partes


def _estrutura(c):
    """Criterion without its definitions and with exactly the compared text fields blanked: what must not change."""
    textos = textos_do_criterio(c)
    c = copy.deepcopy(c)
    c.pop("definicoes", None)
    for campo, _ in textos:
        *pais, folha = _caminho(campo)
        alvo = c
        for k in pais:
            alvo = alvo[k]
        alvo[folha] = "…"
    return c


def comparar_criterio(antigo, novo, glossario, aceitas, usadas=None):
    """Unaccepted differences between a stage-1 criterion and its migrated version ([] when they match).

    Malformed accepted entries are not applied (see validar_aceitas). When `usadas` is a set, the ids
    ("clausulas[0]", …) of the accepted entries this criterion used are added to it.
    """
    cid = novo.get("id") or antigo.get("id")
    diffs = []
    usadas = set() if usadas is None else usadas
    campos_ac = [(eid, a) for eid, a in _entradas(aceitas, "campos") if _aplica(a, cid)]
    frases = _entradas(aceitas, "frases")

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
        for eid, a in campos_ac:
            if "remover" in a and a.get("campo") in ("*", campo) and a["remover"] in texto:
                texto = texto.replace(a["remover"], "")
                removidos.add(eid)
                for cl in _clausulas_de_corpo(a["remover"].strip(" ,;.").removeprefix("e ")):
                    velhas.setdefault(cl, campo)
        sem_defs, blocos = extrair_blocos(texto, cadeia=(campo == "enunciado"))
        for b in blocos:
            for cl in _clausulas_de_corpo(b):
                velhas.setdefault(cl, campo)
        for eid, a in frases:
            de = _ws(a["de"])
            if de in _ws(sem_defs):
                sem_defs = _ws(sem_defs).replace(de, _ws(a["para"]))
                usadas.add(eid)
        # The pointer is stripped on both sides: stage 1 already used it outside the blocks (D29).
        esperado = _norm_campo(_PONTEIRO_RE.sub("", sem_defs)) if campo in antigos else "(campo inexistente)"
        obtido = _norm_campo(_PONTEIRO_RE.sub("", novos[campo])) if campo in novos else "(campo inexistente)"
        if esperado != obtido:
            ok = [
                eid for eid, a in campos_ac
                if "de" in a and a["campo"] == campo and _norm_campo(a["de"]) == esperado and _norm_campo(a["para"]) == obtido
            ]
            usadas.update(ok)
            if not ok:
                diffs.append(f"{cid} {campo}: texto fora das definições mudou\n  etapa 1: {esperado}\n  agora:   {obtido}")
    for eid, a in campos_ac:
        if "remover" in a:
            # A remover that applies is accounted for here: either it matched, or its miss is reported now.
            usadas.add(eid)
            if eid not in removidos:
                diffs.append(f"{cid}: remover aceito não encontrado (campo {a.get('campo')}): {a['remover']!r}")

    # 2. Definition clauses.
    mapa = {}  # clausula da etapa 1 -> (id da entrada, [clausulas novas])
    for eid, a in _entradas(aceitas, "clausulas"):
        if _aplica(a, cid, "*"):
            para = a["para"]
            mapa[_norm_clausula(a["de"])] = (eid, [para] if isinstance(para, str) else list(para))
    mapeadas = {}  # clausula -> clausula da etapa 1 que a originou
    for v in velhas:
        if v in mapa:
            usadas.add(mapa[v][0])
        for p in mapa[v][1] if v in mapa else [v]:
            mapeadas.setdefault(_norm_clausula(p), v)
    novas = _clausulas_novas(novo, glossario, cid, diffs)
    remocoes = {}  # clausula -> ids das entradas que a aceitam
    for eid, a in _entradas(aceitas, "remocoes"):
        if _aplica(a, cid):
            remocoes.setdefault(_norm_clausula(a["clausula"]), []).append(eid)
    adicoes = {}
    for eid, a in _entradas(aceitas, "adicoes"):
        if not _aplica(a, cid):
            continue
        if a.get("chave") in glossario:
            cls = _clausulas_da_chave(glossario, a["chave"])
        elif _str(a.get("clausula")):
            cls = [_norm_clausula(a["clausula"])]
        else:
            cls = []
        for cl in cls:
            adicoes.setdefault(cl, []).append(eid)
    for m in sorted(set(mapeadas) - set(novas)):
        if m in remocoes:
            usadas.update(remocoes[m])
        else:
            origem = mapeadas[m]
            via = f" (mapeada de: {origem})" if origem != m else ""
            diffs.append(f"{cid}: definição da etapa 1 sem correspondente [{velhas[origem]}]: {m}{via}")
    for n in sorted(set(novas) - set(mapeadas)):
        if n in adicoes:
            usadas.update(adicoes[n])
        else:
            diffs.append(f"{cid}: definição nova não aceita [{novas[n]}]: {n}")
    return diffs


def comparar_diretriz(antigo, novo, glossario, aceitas, usadas=None):
    """Diretriz-level fields must not change; criteria are paired by id and compared one by one."""
    did = novo.get("id") or antigo.get("id")
    diffs = []
    for k in list(antigo) + [k for k in novo if k not in antigo]:
        if k != "criterios" and antigo.get(k) != novo.get(k):
            diffs.append(f"{did} {k}: campo da diretriz mudou\n  etapa 1: {antigo.get(k)!r}\n  agora:   {novo.get(k)!r}")
    for lado, d in (("etapa 1", antigo), ("catálogo", novo)):
        ids = [c.get("id") for c in d.get("criterios") or []]
        for cid in sorted({i for i in ids if ids.count(i) > 1}, key=str):
            diffs.append(f"{cid}: id de critério duplicado ({lado}, {ids.count(cid)}x); só o último é comparado")
    velhos = {c.get("id"): c for c in antigo.get("criterios") or []}
    novos = {c.get("id"): c for c in novo.get("criterios") or []}
    for cid in velhos:
        if cid not in novos:
            diffs.append(f"{cid}: critério da etapa 1 ausente no catálogo")
    for cid, c in novos.items():
        if cid not in velhos:
            diffs.append(f"{cid}: critério novo, inexistente na etapa 1")
        else:
            diffs += comparar_criterio(velhos[cid], c, glossario, aceitas, usadas=usadas)
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
    erros = validar_aceitas(aceitas)
    for e in erros:
        print(e)
    total += len(erros)
    stems = {n.removesuffix(".yaml") for n in atuais | base_nomes}
    for sid in sorted(only - stems):
        print(f"{sid}: --only não corresponde a nenhum arquivo")
        total += 1
    usadas = set()
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
                diffs = comparar_diretriz(antigo, novo, glossario, aceitas, usadas=usadas)
        for d in diffs:
            print(d)
        total += len(diffs)
    for lista in _LISTAS:
        for eid, a in _entradas(aceitas, lista):
            crit = a.get("criterio", "*")
            if only and (crit == "*" or crit.split(".")[0] not in only):
                continue  # may be used by a diretriz outside --only
            if eid not in usadas:
                print(f"aceitas não usadas: {eid} {_descreve(a)}")
                total += 1
    print(f"{total} diferença(s) não aceita(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
