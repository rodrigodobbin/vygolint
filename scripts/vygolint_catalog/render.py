"""Render validated catalog dicts to Markdown and LaTeX. Pure functions, no I/O."""

GENERATED_MD = "<!-- ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão. -->"
GENERATED_TEX = "% ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão."

_FONTES = (("codigo", "Código"), ("documentacao", "Documentação"), ("video", "Vídeo"))
_GRAUS = (("atendido", "Atendido"), ("parcial", "Parcial"), ("nao_atendido", "Não atendido"))


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


def render_markdown(diretrizes, categorias):
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
            linhas += [
                f"#### {c['id']} — Nível {c['nivel']}",
                "",
                f"**Enunciado.** {c['enunciado']}",
                "",
                f"**Justificativa do nível.** essencialidade {nj['essencialidade']}, "
                f"viabilidade {nj['viabilidade']}. {nj['texto']}",
                "",
                "**Evidência.**",
            ]
            for chave, nome in _FONTES:
                fonte = c["evidencia"][chave]
                if fonte is None:
                    linhas.append(f"- {nome}: não se aplica")
                else:
                    linhas.append(
                        f"- {nome}: {fonte['procedimento']}. Indicadores: " + "; ".join(fonte["indicadores"])
                    )
            linhas += ["", "**Escala.**"]
            for chave, nome in _GRAUS:
                linhas.append(f"- {nome}: {c['escala'][chave]}")
            linhas += ["", f"**Depende de.** {_depende_de(c)}", ""]
    return "\n".join(linhas).rstrip() + "\n"
