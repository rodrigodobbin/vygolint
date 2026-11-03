#!/usr/bin/env python3
"""One-shot migration of inline definitions in catalog/D*.yaml to the `definicoes` field.

Usage:
  python3 scripts/migrate_definicoes.py --dry-run            # Markdown report on stdout, no writes
  python3 scripts/migrate_definicoes.py --write [--only D28,D39]
  python3 scripts/migrate_definicoes.py --roundtrip          # rewrite files unchanged (emitter check)
"""

import argparse
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from vygolint_catalog.validate import load_definicoes, textos_do_criterio  # noqa: E402

# Termo como aparece no texto -> chaves do glossário.
ALIASES = {
    "missão": ["missao"],
    "missões": ["missao"],
    "missão ou tarefa": ["missao"],
    "missão ou desafio": ["missao", "desafio"],
    "minijogo": ["minijogo"],
    "desafio": ["desafio"],
    "cenário jogável": ["cenario_jogavel"],
    "caminho obrigatório": ["caminho_obrigatorio"],
    "caminho da missão": ["caminho_obrigatorio"],
    "situação-problema": ["situacao_problema"],
    "objetivo de aprendizagem": ["objetivo_de_aprendizagem"],
    "objetivos de aprendizagem": ["objetivo_de_aprendizagem"],
    "sessão de jogo": ["sessao_de_jogo"],
    "documentação": ["documentacao_equivalente"],
}

# Cláusulas da etapa 1 declaradas equivalentes ao texto canônico (normalizadas).
# Preenchido na Task 7 a partir do relatório; espelhado em scripts/definicoes_aceitas.yaml.
EQUIVALENTES = set()

_ORDEM_DIRETRIZ = ("id", "categoria", "diretriz", "fonte", "modalidade", "aplicabilidade")
_BARE = {"id", "categoria", "modalidade", "nivel", "essencialidade", "viabilidade"}


def _q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _val(k, v):
    if v is None:
        return "null"
    if k in _BARE:
        return str(v)
    return _q(str(v))


def emit_yaml(d):
    out = [f"{k}: {_val(k, d[k])}" for k in _ORDEM_DIRETRIZ]
    out.append("criterios:")
    for c in d["criterios"]:
        out.append(f"  - id: {c['id']}")
        out.append(f"    nivel: {c['nivel']}")
        out.append(f"    enunciado: {_q(c['enunciado'])}")
        nj = c["nivel_justificativa"]
        out += ["    nivel_justificativa:", f"      essencialidade: {nj['essencialidade']}",
                f"      viabilidade: {nj['viabilidade']}", f"      texto: {_q(nj['texto'])}"]
        out.append("    evidencia:")
        for nome in ("codigo", "documentacao", "video"):
            fonte = c["evidencia"][nome]
            if fonte is None:
                out.append(f"      {nome}: null")
                continue
            out += [f"      {nome}:", f"        procedimento: {_q(fonte['procedimento'])}", "        indicadores:"]
            out += [f"          - {_q(i)}" for i in fonte["indicadores"]]
        out.append("    escala:")
        out += [f"      {g}: {_q(c['escala'][g])}" for g in ("atendido", "parcial", "nao_atendido")]
        if c["depende_de"]:
            out.append("    depende_de:")
            out += ["      - [" + ", ".join(g) + "]" for g in c["depende_de"]]
        else:
            out.append("    depende_de: []")
        defs = c.get("definicoes")
        if defs:
            out.append("    definicoes:")
            if defs.get("glossario"):
                out.append("      glossario: [" + ", ".join(defs["glossario"]) + "]")
            for campo in ("locais", "termos_comuns"):
                if defs.get(campo):
                    out.append(f"      {campo}:")
                    out += [f"        {_q(k)}: {_q(v)}" for k, v in defs[campo].items()]
    return "\n".join(out) + "\n"


_MAIUSCULA = "A-ZÁÉÍÓÚÂÊÔÃÕÇ"
_PREFIXO_RE = re.compile(r"(?P<sep>;\s*|\.\s*|\s+)Defini(?:ções|ção):\s*")
# '<termo> é|são …', optionally with an apposition: '<termo>, o mesmo que X, é …', '<termo>, neste critério, é …'.
_TERMO_RE = re.compile(r"^(?P<termo>[^;:(),]{1,70}?)(?P<ap>, [^,;:()]+,)? (?:é|são) (?P<resto>.+)$", re.S)
_ARTIGOS = {"o", "a", "os", "as", "um", "uma", "é", "são", "não", "se", "e"}
# A term never starts with a conjunction or a deictic ('quando o resultado é de equipe, …', 'esta diretriz é …').
_NAO_INICIA_TERMO = _ARTIGOS | {"quando", "caso", "como", "para", "esta", "este", "isto", "neste", "nesta"}
# 'X é tratado em D05' is a scope note, not a definition of X.
_ESCOPO_PREDICADO_RE = re.compile(r"^tratad[oa]s? em ")
# Untermed conditional definition: '[artigo] <definiendum> quando <condição>'.
_QUANDO_RE = re.compile(r"^(?:(?:o|a|os|as|um|uma) )?(?P<termo>[^;:(),]{1,80}?) (?P<resto>quando .+)$", re.S)
_ESCOPO_RE = re.compile(r"(?:esta diretriz|este critério)\b", re.I)


def _fim_do_bloco(texto, inicio):
    """Index where a definitions body ends: '. ' + capital letter at paren depth 0, or end of text."""
    depth = 0
    i = inicio
    while i < len(texto):
        ch = texto[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif ch == "." and depth == 0:
            m = re.match(r"\.\s+[" + _MAIUSCULA + "]", texto[i:])
            if m:
                return i
        i += 1
    return len(texto)


def _termo_de(clausula):
    m = _TERMO_RE.match(clausula)
    if not m:
        return ""
    termo = m.group("termo").strip()
    palavras = termo.split()
    if (
        not palavras
        or palavras[0].lower() in _NAO_INICIA_TERMO
        or " não" in f" {termo}"
        or len(palavras) > 7
        or _ESCOPO_PREDICADO_RE.match(m.group("resto"))
    ):
        return ""
    return termo


def _definicao(clausula):
    """(termo, corpo) of a clause that opens a definition; ('', clausula) when no term is found.

    '<termo> é X' -> (termo, 'X'); '<termo>, o mesmo que Y, é X' -> (termo, 'o mesmo que Y, X');
    '[artigo] <definiendum> quando C' -> (definiendum, 'quando C').
    """
    termo = _termo_de(clausula)
    if termo:
        m = _TERMO_RE.match(clausula)
        ap = (m.group("ap") or "").strip(", ")
        return termo, (f"{ap}, " if ap else "") + m.group("resto")
    m = _QUANDO_RE.match(clausula)
    if m and len(m.group("termo").split()) <= 10 and m.group("termo").split()[0].lower() not in _NAO_INICIA_TERMO:
        return m.group("termo").strip(), m.group("resto")
    return "", clausula


def clausulas(corpo):
    partes, depth, atual = [], 0, []
    i = 0
    while i < len(corpo):
        ch = corpo[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == ";" and depth == 0 and corpo[i + 1 : i + 2] == " ":
            partes.append("".join(atual).strip())
            atual = []
            i += 2
            continue
        atual.append(ch)
        i += 1
    if "".join(atual).strip():
        partes.append("".join(atual).strip())
    return partes


def agrupar(cls):
    grupos = []
    for cl in cls:
        termo = _termo_de(cl)
        if termo or not grupos:
            grupos.append((termo, [cl]))
        else:
            grupos[-1][1].append(cl)
    return grupos


def _cadeia_final(texto):
    """Trailing '; termo é …' chain of an enunciado without the 'Definições:' prefix.

    The chain starts at the first clause (after the first) that opens a definition and runs to the end:
    stage 1 always put the definitions last, and clauses inside the chain that do not open a term
    ('a missão exige … quando …', 'persiste quando …') continue the previous definition.
    """
    cls = clausulas(texto)
    for i, cl in enumerate(cls):
        if i > 0 and _termo_de(cl):
            pos = texto.rfind("; " + cl)
            if pos < 0:
                return texto, None
            return texto[:pos].rstrip(), texto[pos + 2 :].strip()
    return texto, None


def extrair_blocos(texto, cadeia=True):
    blocos = []
    while True:
        m = _PREFIXO_RE.search(texto)
        if not m:
            break
        fim = _fim_do_bloco(texto, m.end())
        corpo = texto[m.end() : fim].strip().rstrip(".")
        blocos.append(corpo)
        antes = texto[: m.start()].rstrip()
        depois = texto[fim:]
        if depois.startswith("."):
            texto = antes.rstrip(";:,") + depois
        else:
            texto = antes.rstrip(";:,")
    if cadeia and not blocos:
        texto, corpo = _cadeia_final(texto)
        if corpo:
            blocos.append(corpo)
    return texto, blocos


def normalizar_clausula(s):
    s = re.sub(r"\s+", " ", s).strip().rstrip(".").strip()
    return re.sub(r"^(?P<t>[^;:()]{1,70}?)(?P<ap>, o mesmo que [^,]+,)? (?:é|são) ", lambda m: m.group("t") + (m.group("ap") or "") + " = ", s, count=1)


def _canonica(glossario, chave):
    return normalizar_clausula(f"{glossario[chave]['termo'].split(' (')[0]} é {glossario[chave]['texto']}")


def _grupos_locais(cls):
    """Split the clauses left after a glossary definition into local definitions.

    Unlike agrupar, a conditional clause ('a missão exige X quando Y') also opens a new definition here,
    since there is no local definition for it to continue.
    """
    grupos = []
    for cl in cls:
        termo, corpo = _definicao(cl)
        if termo or not grupos:
            grupos.append([termo, [corpo]])
        else:
            grupos[-1][1].append(cl)
    return grupos


def _gatilho_usado(entrada, corpus):
    return next((g for g in entrada["gatilhos"] if g.lower() in corpus), None)


def migrar_criterio(c, glossario, relatorio, did):
    """Mutate criterion in place; append findings to relatorio (dict of lists).

    Item shapes (all start with did, criterion id, campo):
      divergencias / normalizadas: (did, cid, campo, chave, texto da definição no critério)
      sobras: (did, cid, campo, termo, [cláusulas], [chaves locais criadas])
      locais_divergentes: (did, cid, campo, termo, texto mantido, texto descartado)
      adicionadas: (did, cid, onde, chave, gatilho)
      manuais: (did, cid, onde, motivo, trecho)
    """
    cid = c["id"]
    chaves, locais = [], {}

    def add_local(campo, termo, partes):
        chave = termo or partes[0][:60]
        texto = "; ".join(partes)
        if not termo:
            relatorio["manuais"].append((did, cid, campo, "termo da definição local não identificado; chave provisória", partes[0]))
        if chave in locais and locais[chave] != texto:
            relatorio["locais_divergentes"].append((did, cid, campo, chave, locais[chave], texto))
        locais.setdefault(chave, texto)
        return chave

    for campo, texto in textos_do_criterio(c):
        novo, blocos = extrair_blocos(texto, cadeia=campo == "enunciado")
        _set_campo(c, campo, novo)
        for corpo in blocos:
            for termo, cls in agrupar(clausulas(corpo)):
                if termo not in ALIASES:
                    t, corpo0 = _definicao(cls[0])
                    add_local(campo, t, [corpo0] + cls[1:])
                    continue
                ks = ALIASES[termo]
                n = max(len(clausulas(glossario[k]["texto"])) for k in ks)
                definicao, sobra = "; ".join(cls[:n]), cls[n:]
                norm = normalizar_clausula(definicao)
                for k in ks:
                    if k not in chaves:
                        chaves.append(k)
                    if norm != _canonica(glossario, k):
                        destino = "normalizadas" if norm in EQUIVALENTES else "divergencias"
                        relatorio[destino].append((did, cid, campo, k, definicao))
                if sobra:
                    criadas = [add_local(campo, t, partes) for t, partes in _grupos_locais(sobra)]
                    relatorio["sobras"].append((did, cid, campo, termo, sobra, criadas))

    # Mirror the lint: a trigger in the criterion's own text, in a local definition or in the text of
    # another listed key (cascade) requires the key. Iterate to a fixed point.
    proprios = textos_do_criterio(c)
    mudou = True
    while mudou:
        mudou = False
        for e in glossario.values():
            if e["chave"] in chaves:
                continue
            fontes = [(campo, t) for campo, t in proprios]
            fontes += [(f"locais[{k}]", v) for k, v in locais.items()]
            fontes += [(f"texto de {k}", glossario[k]["texto"]) for k in chaves]
            for onde, t in fontes:
                g = _gatilho_usado(e, t.lower())
                if g:
                    chaves.append(e["chave"])
                    relatorio["adicionadas"].append((did, cid, onde, e["chave"], g))
                    mudou = True
                    break
    ordem = list(glossario)
    chaves.sort(key=ordem.index)
    corpus = " ".join([t for _, t in proprios] + list(locais.values())).lower()
    for k in chaves:
        outros = " ".join(glossario[o]["texto"] for o in chaves if o != k).lower()
        if not _gatilho_usado(glossario[k], corpus + " " + outros):
            relatorio["manuais"].append(
                (did, cid, "definicoes.glossario", f"`{k}` listada mas nenhum gatilho ({', '.join(glossario[k]['gatilhos'])}) aparece no texto migrado", "")
            )
    for k in locais:
        partes = {p.strip().lower() for p in re.split(r" e | ou ", k)}
        for e in glossario.values():
            if partes & ({g.lower() for g in e["gatilhos"]} | {t for t, ks in ALIASES.items() if e["chave"] in ks}):
                relatorio["manuais"].append(
                    (did, cid, f"locais[{k}]", f"definição local redefine termo de `{e['chave']}`: usar o glossário ou `termos_comuns`", locais[k])
                )
    defs = {}
    if chaves:
        defs["glossario"] = chaves
    if locais:
        defs["locais"] = locais
    if defs:
        c["definicoes"] = defs


def _set_campo(c, campo, valor):
    if campo == "enunciado":
        c["enunciado"] = valor
    elif campo.startswith("escala."):
        c["escala"][campo.split(".")[1]] = valor
    else:
        fonte, resto = campo.split(".", 1)
        if resto == "procedimento":
            c["evidencia"][fonte]["procedimento"] = valor
        else:
            i = int(resto[len("indicadores["):-1])
            c["evidencia"][fonte]["indicadores"][i] = valor


def _trecho(texto, inicio, fim):
    return ("…" if inicio > 0 else "") + texto[max(0, inicio) : fim] + ("…" if fim < len(texto) else "")


def _prefixo_menos(c, glossario, did, relatorio):
    """Definitions that need manual migration, searched in the migrated texts and in the local definitions.

    - a glossary term defined at the start of a clause ('…, e missão é uma atividade…', '; desafio é …');
    - a glossary term defined inline by 'isto é' ('situação-problema, isto é, uma situação…');
    - a scope note ('esta diretriz…', 'tratado em D05') that ended up inside a local definition.
    """
    cid = c["id"]
    termos = sorted(set(ALIASES) | {g for e in glossario.values() for g in e["gatilhos"]}, key=len, reverse=True)
    alt = "|".join(re.escape(t) for t in termos)
    def_re = re.compile(r"(?:^|[;:.]\s+|,\s+e\s+)(?P<t>" + alt + r") (?:é|são) ", re.I)
    isto_re = re.compile(r"(?<![\w-])(?P<t>" + alt + r"), isto é, ", re.I)
    locais = (c.get("definicoes") or {}).get("locais") or {}
    fontes = textos_do_criterio(c) + [(f"locais[{k}]", v) for k, v in locais.items()]
    for onde, texto in fontes:
        for m in def_re.finditer(texto):
            relatorio["manuais"].append(
                (did, cid, onde, f"definição de «{m.group('t')}» fora de bloco", _trecho(texto, m.start("t") - 40, m.start("t") + 160))
            )
        for m in isto_re.finditer(texto):
            relatorio["manuais"].append(
                (did, cid, onde, f"definição de «{m.group('t')}» por «isto é»", _trecho(texto, m.start("t"), m.end() + 120))
            )
    for onde, texto in textos_do_criterio(c):
        for e in glossario.values():
            if e["texto"] in texto:
                relatorio["manuais"].append(
                    (did, cid, onde, f"texto do glossário de `{e['chave']}` aparece literalmente (o lint rejeita)", e["texto"])
                )
    for k, v in locais.items():
        for cl in clausulas(v):
            sem_parenteses = re.sub(r"\([^()]*\)", "", cl)
            if _ESCOPO_RE.match(cl) or re.search(r"\b(?:é|são) tratad[oa]s? em D\d\d", sem_parenteses):
                relatorio["manuais"].append((did, cid, f"locais[{k}]", "nota de escopo dentro da definição local", cl))


def _agrupar_campos(itens):
    """Merge items equal except for campo (index 2): {(did, cid, *rest): [campos]} in first-seen order."""
    grupos = {}
    for it in itens:
        chave = tuple(str(x) for x in (it[:2] + it[3:]))
        grupos.setdefault(chave, (it, []))[1].append(it[2])
    return list(grupos.values())


def _campos(cs):
    return "; ".join(dict.fromkeys(cs))


def _diferenca(a, b):
    """Short view of where two texts differ: common prefix/suffix elided."""
    p = len(os.path.commonprefix([a, b]))
    p = max(a.rfind(" ", 0, p) + 1, 0) if p < min(len(a), len(b)) else p
    s = len(os.path.commonprefix([a[p:][::-1], b[p:][::-1]]))
    while s and not (a[len(a) - s - 1] == " " and b[len(b) - s - 1] == " "):
        s -= 1
    def corte(t):
        meio = t[p : len(t) - s]
        return ("…" if p else "") + (meio or "(nada)") + ("…" if s else "")
    return corte(a), corte(b)


def relatorio_markdown(rel, glossario):
    out = ["# Relatório da migração de definições", ""]

    def secao(titulo, linhas, nota=None):
        out.extend([f"## {titulo}", ""])
        if nota:
            out.extend([nota, ""])
        out.extend(linhas or ["(nenhuma)"])
        out.append("")

    for titulo, chave in (
        ("Divergências (texto canônico aplicado; decisão pendente)", "divergencias"),
        ("Normalizações (redação equivalente)", "normalizadas"),
    ):
        linhas = []
        por_chave = defaultdict(list)
        for it in rel[chave]:
            por_chave[it[3]].append(it)
        for k in [k for k in glossario if k in por_chave]:
            linhas += [f"### `{k}`", "", f"Canônico ({glossario[k]['ancora']}): «{glossario[k]['termo']} é {glossario[k]['texto']}»", ""]
            for (did, cid, _, _, texto), campos in _agrupar_campos(por_chave[k]):
                linhas.append(f"- {did}/{cid} ({_campos(campos)}): «{texto}»")
            linhas.append("")
        secao(titulo, linhas[:-1] if linhas else linhas)

    por_criterio = defaultdict(list)
    for did, cid, onde, k, g in rel["adicionadas"]:
        por_criterio[(did, cid)].append(f"`{k}` («{g}» em {onde})")
    secao(
        "Definições do glossário adicionadas a critérios que não as tinham",
        [f"- {did}/{cid}: " + ", ".join(v) for (did, cid), v in por_criterio.items()],
        "O gatilho aparece no texto migrado (ou em definição local, ou no texto de outra chave listada), "
        "então o lint exige a chave; quando o sentido é o corrente, trocar por `termos_comuns`.",
    )

    linhas = []
    for (did, cid, _, termo, sobra, criadas), campos in _agrupar_campos(rel["sobras"]):
        movidas = ", ".join(f"`{k}`" for k in criadas)
        linhas.append(f"- {did}/{cid} ({_campos(campos)}) após `{termo}`: " + " | ".join(f"«{s}»" for s in sobra) + f" → movidas para locais: {movidas}")
    secao("Cláusulas que seguiam um termo do glossário (ver se são locais)", linhas)

    linhas = []
    for (did, cid, _, termo, mantido, descartado), campos in _agrupar_campos(rel["locais_divergentes"]):
        a, b = _diferenca(mantido, descartado)
        linhas.append(f"- {did}/{cid} `{termo}`, texto descartado em {_campos(campos)}: mantido «{a}» / descartado «{b}»")
    secao("Definições locais com texto divergente no mesmo critério", linhas, "Mantido: a primeira ocorrência (enunciado, depois evidências, depois escala).")

    linhas = []
    for (did, cid, _, motivo, trecho), campos in _agrupar_campos(rel["manuais"]):
        linhas.append(f"- {did}/{cid} ({_campos(campos)}): {motivo}" + (f": «{trecho}»" if trecho else ""))
    secao("Definições fora de bloco (migração manual)", linhas)
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--catalog", default=str(REPO / "catalog"))
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--write", action="store_true")
    g.add_argument("--roundtrip", action="store_true")
    ap.add_argument("--only", default="")
    args = ap.parse_args(argv)
    catalog = Path(args.catalog)
    glossario = load_definicoes(catalog / "definicoes.yaml")
    only = {s.strip() for s in args.only.split(",") if s.strip()}
    rel = defaultdict(list)
    for path in sorted(catalog.glob("D*.yaml")):
        if only and path.stem not in only:
            continue
        d = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not args.roundtrip:
            for c in d["criterios"]:
                migrar_criterio(c, glossario, rel, d["id"])
                _prefixo_menos(c, glossario, d["id"], rel)
        if args.write or args.roundtrip:
            path.write_text(emit_yaml(d), encoding="utf-8")
    if not args.roundtrip:
        print(relatorio_markdown(rel, glossario))
    return 0


if __name__ == "__main__":
    sys.exit(main())
