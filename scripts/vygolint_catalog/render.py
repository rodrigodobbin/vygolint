"""Render validated catalog dicts to Markdown and LaTeX. Pure functions, no I/O."""

import re

GENERATED_MD = "<!-- ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão. -->"
GENERATED_TEX = "% ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão."

_FONTES = (("codigo", "Código"), ("documentacao", "Documentação"), ("video", "Vídeo"))
_EIXOS = {"alta": "alta", "media": "média", "baixa": "baixa"}
_GRAUS = (("atendido", "Atendido"), ("parcial", "Parcial"), ("nao_atendido", "Não atendido"))
_VIAS = (("documentacao", "Documentação"), ("design", "Design"), ("codigo", "Código"))


def _nome_categoria(chave, categorias):
    for c in categorias["categorias"]:
        if c["chave"] == chave:
            return c["nome"]
    return chave


def _ordenadas(diretrizes):
    return sorted(diretrizes, key=lambda d: d["id"])


def _criterios_resumo(d):
    return ", ".join(f"{c['id']} ({c['nivel']})" for c in d["criterios"])


def _depende_de(c):
    if not c["depende_de"]:
        return "—"
    return " e ".join("(" + " ou ".join(g) + ")" for g in c["depende_de"])


def _bloco_recomendacoes(c):
    rec = c.get("recomendacao")
    if not rec:
        return []
    linhas = ["", "**Recomendações.**"]
    for chave, nome in _VIAS:
        texto = rec.get(chave)
        linhas.append(f"- {nome}: {texto if texto else 'não se aplica'}")
    return linhas


def _bloco_definicoes(c, glossario):
    defs = c.get("definicoes") or {}
    itens = []
    for chave in defs.get("glossario") or []:
        e = glossario[chave]
        itens.append(f"- *{e['termo']}*: {e['texto']}")
    for termo, texto in (defs.get("locais") or {}).items():
        itens.append(f"- *{termo}*: {texto}")
    for termo, just in (defs.get("termos_comuns") or {}).items():
        itens.append(f"- *{termo}* (sentido corrente): {just}")
    if not itens:
        return []
    return ["**Definições.**", ""] + itens + [""]


def _secao_glossario(glossario):
    if not glossario:
        return []
    linhas = ["## Glossário", "", "Definições compartilhadas, referenciadas pelos critérios em `definicoes.glossario`.", ""]
    for e in glossario.values():
        linhas.append(f"- **{e['termo']}** (âncora {e['ancora']}; gatilhos: {', '.join(e['gatilhos'])}): {e['texto']}")
    return linhas + [""]


def render_markdown(diretrizes, categorias, glossario=None):
    glossario = glossario or {}
    linhas = [
        GENERATED_MD,
        "# Catálogo vygolint — diretrizes e critérios de conformidade",
        "",
        "Fonte das diretrizes: CARVALHO, Diego Marques. *Diretrizes para o desenvolvimento de jogos "
        "educacionais digitais embasados na teoria sociointeracionista de Lev Semionovich Vigotski*. "
        "Dissertação (Mestrado), UFABC, 2020. Quadro 3.",
        "",
        "> " + categorias["ressalva"].strip().replace("\n", " "),
        "",
    ]
    linhas += _secao_glossario(glossario)
    linhas += [
        "## Resumo",
        "",
        "| ID | Categoria | Diretriz | Critérios |",
        "|---|---|---|---|",
    ]
    ordenadas = _ordenadas(diretrizes)
    for d in ordenadas:
        linhas.append(
            f"| {d['id']} | {_nome_categoria(d['categoria'], categorias)} | {d['diretriz']} | {_criterios_resumo(d)} |"
        )
    linhas += ["", "## Diretrizes", ""]
    for d in ordenadas:
        linhas += [
            f"### {d['id']} — {d['diretriz']}",
            "",
            f"- Categoria: {_nome_categoria(d['categoria'], categorias)}",
            f"- Modalidade: {d['modalidade']}",
            f"- Aplicabilidade: {d['aplicabilidade'] or '—'}",
            f"- Fonte: {d['fonte']}",
            "",
        ]
        for c in d["criterios"]:
            nj = c["nivel_justificativa"]
            linhas += [f"#### {c['id']} — Nível {c['nivel']}", ""]
            linhas += _bloco_definicoes(c, glossario)
            linhas += [
                f"**Enunciado.** {c['enunciado']}",
                "",
                f"**Justificativa do nível.** essencialidade {_EIXOS[nj['essencialidade']]}, "
                f"viabilidade {_EIXOS[nj['viabilidade']]}. {nj['texto']}",
                "",
                "**Evidência.**",
            ]
            for chave, nome in _FONTES:
                fonte = c["evidencia"][chave]
                if fonte is None:
                    linhas.append(f"- {nome}: não se aplica")
                else:
                    linhas.append(f"- {nome}: {fonte['procedimento']}")
                    linhas += [f"  - {ind}" for ind in fonte["indicadores"]]
            linhas += ["", "**Escala.**"]
            for chave, nome in _GRAUS:
                linhas.append(f"- {nome}: {c['escala'][chave]}")
            linhas += _bloco_recomendacoes(c)
            linhas += ["", f"**Depende de.** {_depende_de(c)}", ""]
    return "\n".join(linhas).rstrip() + "\n"


_LATEX_MAP = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}
_LATEX_RE = re.compile("|".join(re.escape(k) for k in _LATEX_MAP))


def escape_latex(text):
    """Single-pass escape so replacements never re-escape each other."""
    return _LATEX_RE.sub(lambda m: _LATEX_MAP[m.group()], text)


def render_latex(diretrizes, categorias):
    cab = r"\textbf{ID} & \textbf{Categoria} & \textbf{Diretriz} & \textbf{Critérios} \\"
    linhas = [
        GENERATED_TEX,
        r"\begin{longtable}{p{1.1cm}p{2.6cm}p{7.2cm}p{2.6cm}}",
        r"\caption{Diretrizes de Carvalho (2020) e critérios de conformidade do vygolint}"
        r"\label{tab:catalogo_vygolint}\\",
        r"\hline",
        cab,
        r"\hline",
        r"\endfirsthead",
        r"\hline",
        cab,
        r"\hline",
        r"\endhead",
        r"\hline",
        r"\endfoot",
    ]
    for d in _ordenadas(diretrizes):
        linhas.append(
            f"{d['id']} & {escape_latex(_nome_categoria(d['categoria'], categorias))} & "
            f"{escape_latex(d['diretriz'])} & {escape_latex(_criterios_resumo(d))} \\\\"
        )
    linhas.append(r"\end{longtable}")
    return "\n".join(linhas) + "\n"
