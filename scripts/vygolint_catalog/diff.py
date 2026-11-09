"""Compare two resultado.yaml files (the output of vygolint_report.py) criterion by criterion."""

CLAUSULA = (
    "O resultado de uma avaliação vygolint expressa conformidade com as diretrizes de Carvalho (2020) "
    "e não classifica o jogo como sociointeracionista."
)

ESCALA = {"nao_atendido": 0, "parcial": 1, "atendido": 2}
GRAUS = ["atendido", "parcial", "nao_atendido", "nao_avaliado", "fora_do_contexto"]

TIPOS = {
    "melhora": "Melhoras",
    "piora": "Pioras",
    "passou_a_ser_avaliado": "Passaram a ser avaliados",
    "deixou_de_ser_avaliado": "Deixaram de ser avaliados",
    "entrou_no_contexto": "Entraram no contexto",
    "saiu_do_contexto": "Saíram do contexto",
}


def classificar(antes, depois):
    """Name the kind of change between two grades; None when they are equal."""
    if antes == depois:
        return None
    if depois == "fora_do_contexto":
        return "saiu_do_contexto"
    if antes == "fora_do_contexto":
        return "entrou_no_contexto"
    if depois == "nao_avaliado":
        return "deixou_de_ser_avaliado"
    if antes == "nao_avaliado":
        return "passou_a_ser_avaliado"
    return "melhora" if ESCALA.get(depois, -1) > ESCALA.get(antes, -1) else "piora"


def _contagem(criterios):
    cont = {g: 0 for g in GRAUS}
    for c in criterios.values():
        g = (c or {}).get("grau")
        if g in cont:
            cont[g] += 1
    return cont


def _sobrescritos(criterios):
    out = []
    for cid in sorted(criterios):
        c = criterios[cid] or {}
        decl, efet = c.get("grau_declarado"), c.get("grau")
        if decl is not None and decl != efet:
            out.append((cid, decl, efet))
    return out


def comparar(antes, depois):
    """Return a dict describing what changed from `antes` to `depois` (both parsed resultado.yaml)."""
    ca = antes.get("criterios") or {}
    cd = depois.get("criterios") or {}
    comuns = sorted(set(ca) & set(cd))
    mudancas, notas = [], []
    for cid in comuns:
        a, d = ca[cid] or {}, cd[cid] or {}
        tipo = classificar(a.get("grau"), d.get("grau"))
        if tipo:
            mudancas.append({
                "id": cid, "tipo": tipo, "antes": a.get("grau"), "depois": d.get("grau"),
                "nivel": d.get("nivel") or a.get("nivel"),
                "nota_antes": a.get("nota"), "nota_depois": d.get("nota"),
            })
        elif a.get("nota") != d.get("nota"):
            notas.append({"id": cid, "grau": d.get("grau"), "antes": a.get("nota"), "depois": d.get("nota")})
    avisos = []
    if antes.get("jogo") != depois.get("jogo"):
        avisos.append(f"os arquivos avaliam jogos diferentes: {antes.get('jogo')!r} e {depois.get('jogo')!r}")
    return {
        "jogo": (antes.get("jogo"), depois.get("jogo")),
        "data": (antes.get("data"), depois.get("data")),
        "avaliador": (antes.get("avaliador"), depois.get("avaliador")),
        "nivel": (antes.get("nivel"), depois.get("nivel")),
        "contagem": {"antes": _contagem(ca), "depois": _contagem(cd)},
        "mudancas": mudancas,
        "notas": notas,
        "sobrescritos": {"antes": _sobrescritos(ca), "depois": _sobrescritos(cd)},
        "so_antes": sorted(set(ca) - set(cd)),
        "so_depois": sorted(set(cd) - set(ca)),
        "avisos": avisos,
    }


def resumo(d):
    """One line with the counts per kind of change."""
    por_tipo = {}
    for m in d["mudancas"]:
        por_tipo[m["tipo"]] = por_tipo.get(m["tipo"], 0) + 1
    partes = []
    for tipo in TIPOS:
        n = por_tipo.get(tipo)
        if n:
            nome = tipo.replace("_", " ")
            if tipo in ("melhora", "piora") and n > 1:
                nome += "s"
            partes.append(f"{n} {nome}")
    texto = ", ".join(partes) if partes else "nenhuma mudança de grau"
    if d["notas"]:
        texto += f"; {len(d['notas'])} nota(s) alterada(s)"
    return texto


def _seta(par):
    a, b = par
    return f"{a} → {b}" if a != b else f"{a}"


def render_diff(d):
    linhas = ["# Comparação de resultados vygolint", ""]
    linhas.append(f"- Jogo: {_seta(d['jogo'])}")
    linhas.append(f"- Data: {_seta(d['data'])}")
    linhas.append(f"- Avaliador: {_seta(d['avaliador'])}")
    linhas.append(f"- Nível: **{_seta(d['nivel'])}**")
    linhas.append("")
    for a in d["avisos"]:
        linhas.append(f"> Aviso: {a}")
        linhas.append("")
    linhas.append("## Contagem por grau")
    linhas.append("")
    linhas.append("| Grau | Antes | Depois |")
    linhas.append("|---|---|---|")
    for g in GRAUS:
        a, b = d["contagem"]["antes"][g], d["contagem"]["depois"][g]
        delta = b - a
        sinal = f" ({delta:+d})" if delta else ""
        linhas.append(f"| {g} | {a} | {b}{sinal} |")
    linhas.append("")
    linhas.append("## Critérios que mudaram de grau")
    linhas.append("")
    if not d["mudancas"]:
        linhas.append("Nenhum critério mudou de grau.")
        linhas.append("")
    for tipo, titulo in TIPOS.items():
        grupo = [m for m in d["mudancas"] if m["tipo"] == tipo]
        if not grupo:
            continue
        linhas.append(f"### {titulo} ({len(grupo)})")
        linhas.append("")
        linhas.append("| Critério | Nível | Grau | Nota antes | Nota depois |")
        linhas.append("|---|---|---|---|---|")
        for m in grupo:
            linhas.append(
                f"| {m['id']} | {m['nivel'] or ''} | {m['antes']} → {m['depois']} "
                f"| {m['nota_antes'] or ''} | {m['nota_depois'] or ''} |"
            )
        linhas.append("")
    if d["notas"]:
        linhas.append("## Notas alteradas com o mesmo grau")
        linhas.append("")
        linhas.append("| Critério | Grau | Nota antes | Nota depois |")
        linhas.append("|---|---|---|---|")
        for n in d["notas"]:
            linhas.append(f"| {n['id']} | {n['grau']} | {n['antes'] or ''} | {n['depois'] or ''} |")
        linhas.append("")
    for chave, titulo in (("antes", "antes"), ("depois", "depois")):
        lista = d["sobrescritos"][chave]
        if lista:
            linhas.append(f"## Grau declarado sobrescrito pelo script ({titulo})")
            linhas.append("")
            for cid, decl, efet in lista:
                linhas.append(f"- {cid}: declarado {decl}, efetivo {efet}")
            linhas.append("")
    if d["so_antes"] or d["so_depois"]:
        linhas.append("## Critérios presentes em um só arquivo")
        linhas.append("")
        if d["so_antes"]:
            linhas.append(f"- Só antes: {', '.join(d['so_antes'])}")
        if d["so_depois"]:
            linhas.append(f"- Só depois: {', '.join(d['so_depois'])}")
        linhas.append("")
    linhas.append(f"> {CLAUSULA}")
    return "\n".join(linhas) + "\n"
