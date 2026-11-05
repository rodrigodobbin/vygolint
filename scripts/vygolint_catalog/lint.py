"""Lint the places cited by the proofs of an avaliacao.yaml and the scope declared in its header.

validate_avaliacao checks the shape of the evaluation; this module checks it against the disk:

- each proof points to something that exists (the cited file, the line inside it, the instant
  inside the video);
- each proof cites a file inside the scope of its source. `contexto.artefatos` lists files or
  folders, and a folder puts every file inside it in scope;
- every video and document in scope is accounted for: cited by a proof, or covered by a
  registro_video file (video) or classified in inventario.md (document: the Classificação cell
  of its row, or a free-text mention of its path when the file has no row). Code has no
  per-file coverage;
- no proof cites a document that inventario.md classifies as "não conta";
- no placeholder left by the scaffold remains, in avaliacao.yaml or in inventario.md.

Findings are warnings: they never change a grade, and the report is still generated unless the
caller asks for strict mode.
"""

import os
import re
import shutil
import subprocess
from pathlib import Path

import yaml

from .report import FONTES
from .scaffold import PLACEHOLDER

_SEP = re.compile(r"\s+[—–]\s+|\s+-\s+")
_TS = r"\d{1,2}:\d{2}:\d{2}"
_CODIGO = re.compile(r"(.+?):(\d+)(?:-(\d+))?")
_DOC = re.compile(r"\s+pp?\.\s*\d+|,\s*se[cç][aã]o\b|\s+§")
_MAX_IDS = 5
_EXT = {
    "video": {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"},
    "documentacao": {
        ".md", ".markdown", ".txt", ".pdf", ".doc", ".docx", ".odt", ".rtf", ".html", ".htm", ".tex",
        ".ppt", ".pptx", ".odp",
    },
}
_PULAR = {"node_modules", "__pycache__", "Library", "Temp", "obj", "bin", "build", "dist"}
_MAX_ARQUIVOS = 20000


def _lugar(prova):
    """Text before the dash that separates the place from the observation."""
    return _SEP.split(prova, maxsplit=1)[0].strip()


def _resolver_com_base(caminho, bases):
    """(path, base it was found under) or (None, None). The base is None for absolute paths."""
    p = Path(caminho).expanduser()
    if p.is_absolute():
        return (p, None) if p.exists() else (None, None)
    for base in bases:
        alvo = Path(base) / p
        if alvo.exists():
            return alvo, Path(base)
    return None, None


def _resolver(caminho, bases):
    return _resolver_com_base(caminho, bases)[0]


def _rotulo(arquivo, base):
    """Path as the evaluator would write it: relative to the base, with forward slashes."""
    if base is None:
        return str(arquivo)
    return Path(os.path.relpath(arquivo, base)).as_posix()


def _textos(valor):
    return [v for v in valor if isinstance(v, str) and v.strip()] if isinstance(valor, list) else []


def _dentro(arquivo, raizes):
    return any(arquivo == r or r in arquivo.parents for r in raizes)


def arquivos_do_escopo(fonte, artefatos, bases, excluir=()):
    """Files a source's artefatos put in scope, as [(resolved path, label)], plus the artefatos not found.

    A file artefato is in scope as given. A folder artefato contributes every file inside it whose
    extension fits the source (video or document); hidden entries, dependency and build folders and
    the folders in `excluir` are skipped. Code has no per-file scope, so its list is always empty.
    """
    arquivos, ausentes, vistos = [], [], set()
    excluidos = {Path(e).resolve() for e in excluir}
    for caminho in _textos(artefatos):
        alvo, base = _resolver_com_base(caminho, bases)
        if alvo is None:
            ausentes.append(caminho)
            continue
        if fonte not in _EXT:
            continue
        if alvo.is_file():
            candidatos = [alvo]
        else:
            candidatos = []
            for raiz, pastas, nomes in os.walk(alvo):
                pastas[:] = sorted(
                    d for d in pastas
                    if not d.startswith(".") and d not in _PULAR and (Path(raiz) / d).resolve() not in excluidos
                )
                for nome in sorted(nomes):
                    if not nome.startswith(".") and Path(nome).suffix.lower() in _EXT[fonte]:
                        candidatos.append(Path(raiz) / nome)
                if len(candidatos) > _MAX_ARQUIVOS:
                    break
        for c in candidatos:
            real = c.resolve()
            if real not in vistos:
                vistos.add(real)
                arquivos.append((real, _rotulo(c, base)))
    return arquivos, ausentes


def _norm(caminho):
    """Path as a comparable key: forward slashes, no leading ./"""
    s = Path(caminho).as_posix()
    while s.startswith("./"):
        s = s[2:]
    return s


_LINHA_ARQUIVO = re.compile(r"^`([^`]+)`$")


def _ler_inventario(pasta):
    """(text, {file key: Classificação cell}) of inventario.md in the evaluation folder.

    Only table rows whose first cell is a backticked path, under a header with a column starting
    with "Classifica", are returned in the map; anything else in the file counts as free text.
    """
    try:
        texto = (Path(pasta) / "inventario.md").read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return "", {}
    linhas, coluna = {}, None
    for linha in texto.splitlines():
        linha = linha.strip()
        if not linha.startswith("|"):
            coluna = None
            continue
        celulas = [c.strip() for c in linha.strip("|").split("|")]
        cabecalho = [i for i, c in enumerate(celulas) if c.lower().startswith("classifica")]
        if cabecalho:
            coluna = cabecalho[0]
            continue
        m = _LINHA_ARQUIVO.match(celulas[0]) if celulas else None
        if m and coluna is not None:
            linhas[_norm(m.group(1))] = celulas[coluna] if coluna < len(celulas) else ""
    return texto, linhas


def _nao_conta(classificacao):
    c = classificacao.strip().lower()
    return c.startswith("não conta") or c.startswith("nao conta")


def _videos_com_registro(pasta, bases):
    """Videos named by the `video` field of the registro_video*.yaml files in the evaluation folder."""
    cobertos = set()
    for reg in sorted(Path(pasta).glob("registro_video*.yaml")):
        try:
            doc = yaml.safe_load(reg.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError, UnicodeDecodeError):
            continue
        video = doc.get("video") if isinstance(doc, dict) else None
        alvo = _resolver(video, bases) if isinstance(video, str) and video.strip() else None
        if alvo is not None:
            cobertos.add(alvo.resolve())
    return cobertos


def _segundos(ts):
    h, m, s = (int(x) for x in ts.split(":"))
    return h * 3600 + m * 60 + s


def _valido(ts):
    _, m, s = (int(x) for x in ts.split(":"))
    return m < 60 and s < 60


def _hms(segundos):
    s = int(segundos)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def duracao_ffprobe(path):
    """Duration of a media file in seconds, or None when ffprobe is missing or cannot read it."""
    exe = shutil.which("ffprobe")
    if not exe:
        return None
    try:
        r = subprocess.run(
            [exe, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
            capture_output=True, text=True, timeout=30,
        )
        return float(r.stdout.strip()) if r.returncode == 0 else None
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def _contar_linhas(path):
    try:
        with open(path, "rb") as fh:
            dados = fh.read()
    except OSError:
        return None
    if not dados:
        return 0
    return dados.count(b"\n") + (0 if dados.endswith(b"\n") else 1)


def _lint_codigo(lugar, bases, _duracao):
    m = _CODIGO.fullmatch(lugar)
    if not m:
        return None, [f"lugar deve ter a forma arquivo:linha (recebido {lugar!r})"]
    caminho, ini, fim = m.group(1).strip(), int(m.group(2)), m.group(3)
    msgs = []
    ultima = ini
    if fim is not None:
        if int(fim) < ini:
            msgs.append(f"intervalo de linhas {ini}-{fim} termina antes de começar")
        ultima = max(ini, int(fim))
    alvo = _resolver(caminho, bases)
    if alvo is not None and alvo.is_file():
        n = _contar_linhas(alvo)
        if n is not None and ultima > n:
            msgs.append(f"linha {ultima} não existe: {caminho} tem {n} linhas")
    return caminho, msgs


def _lint_documentacao(lugar, bases, _duracao):
    m = _DOC.search(lugar)
    if not m:
        return lugar, ["lugar deve citar página ou seção (documento p. N ou documento, seção X)"]
    return lugar[: m.start()].strip(), []


def _lint_video(lugar, bases, duracao):
    m = re.search(_TS, lugar)
    if not m:
        return lugar, ["lugar deve citar o instante em hh:mm:ss (arquivo hh:mm:ss[-hh:mm:ss])"]
    caminho, resto = lugar[: m.start()].strip(), lugar[m.start():]
    msgs = []
    instantes = list(dict.fromkeys(re.findall(_TS, resto)))
    for ts in instantes:
        if not _valido(ts):
            msgs.append(f"instante {ts} inválido (minutos e segundos vão até 59)")
    for a, b in re.findall(rf"({_TS})\s*-\s*({_TS})", resto):
        if _valido(a) and _valido(b) and _segundos(b) < _segundos(a):
            msgs.append(f"intervalo {a}-{b} termina antes de começar")
    alvo = _resolver(caminho, bases) if caminho else None
    if alvo is not None and alvo.is_file():
        total = duracao(alvo)
        if total is not None:
            for ts in instantes:
                if _valido(ts) and _segundos(ts) > total + 1:
                    msgs.append(f"instante {ts} fica depois do fim do vídeo ({_hms(total)})")
    return caminho, msgs


_POR_FONTE = {"codigo": _lint_codigo, "documentacao": _lint_documentacao, "video": _lint_video}


def lint_avaliacao(av, bases, duracao=duracao_ffprobe, pasta=None):
    """Return warning strings (`aviso ...`).

    `bases` are the folders relative paths are tried against. `pasta` is the evaluation folder
    (where registro_video*.yaml and inventario.md live); without it, coverage counts proofs only.
    """
    if not isinstance(av, dict):
        return []
    avisos = []
    for campo in ("jogo", "avaliador"):
        if isinstance(av.get(campo), str) and PLACEHOLDER in av[campo]:
            avisos.append(f"aviso avaliacao: {campo} ainda contém {PLACEHOLDER}")
    contexto = av.get("contexto")
    artefatos = contexto.get("artefatos") if isinstance(contexto, dict) else None
    artefatos = artefatos if isinstance(artefatos, dict) else {}
    excluir = [pasta] if pasta is not None else []
    raizes, escopo = {}, {}
    for fonte in FONTES:
        declarados = _textos(artefatos.get(fonte))
        escopo[fonte], ausentes_art = arquivos_do_escopo(fonte, declarados, bases, excluir)
        for caminho in ausentes_art:
            avisos.append(f"aviso avaliacao: artefato de {fonte} não encontrado: {caminho}")
        if declarados and not ausentes_art:
            raizes[fonte] = [_resolver(c, bases).resolve() for c in declarados]
    citados = {f: set() for f in FONTES}
    fora = {}
    docs_citados = {}
    cache = {}

    def duracao_cache(path):
        if path not in cache:
            cache[path] = duracao(path)
        return cache[path]

    ausentes = {}
    criterios = av.get("criterios")
    for cid in sorted(criterios) if isinstance(criterios, dict) else ():
        entrada = criterios[cid]
        if not isinstance(entrada, dict):
            continue
        if isinstance(entrada.get("razao"), str) and PLACEHOLDER in entrada["razao"]:
            avisos.append(f"aviso {cid}: razao ainda contém {PLACEHOLDER}; gradue o critério ou escreva a razão")
        fontes = entrada.get("fontes")
        if not isinstance(fontes, dict):
            continue
        for fonte in FONTES:
            dados = fontes.get(fonte)
            provas = dados.get("provas") if isinstance(dados, dict) else None
            if not isinstance(provas, list):
                continue
            for i, prova in enumerate(provas, start=1):
                if not isinstance(prova, str) or not prova.strip():
                    continue
                caminho, msgs = _POR_FONTE[fonte](_lugar(prova), bases, duracao_cache)
                for msg in msgs:
                    avisos.append(f"aviso {cid}: fonte {fonte}: prova {i}: {msg}")
                if not caminho:
                    continue
                alvo = _resolver(caminho, bases)
                if alvo is None:
                    ausentes.setdefault(caminho, []).append(cid)
                    continue
                real = alvo.resolve()
                citados[fonte].add(real)
                if fonte == "documentacao":
                    docs_citados.setdefault(_norm(caminho), []).append(cid)
                if fonte in raizes and not _dentro(real, raizes[fonte]):
                    fora.setdefault((fonte, caminho), []).append(cid)

    def _provas(cids):
        unicos = list(dict.fromkeys(cids))
        ids = ", ".join(unicos[:_MAX_IDS]) + (", …" if len(unicos) > _MAX_IDS else "")
        return f"{len(cids)} prova{'s' if len(cids) != 1 else ''}: {ids}"

    for caminho, cids in ausentes.items():
        avisos.append(f"aviso avaliacao: arquivo citado não encontrado: {caminho} ({_provas(cids)})")
    for (fonte, caminho), cids in fora.items():
        avisos.append(f"aviso avaliacao: arquivo citado fora dos artefatos de {fonte}: {caminho} ({_provas(cids)})")
    registros = _videos_com_registro(pasta, bases) if pasta is not None else set()
    for real, rotulo in escopo["video"]:
        if real not in citados["video"] and real not in registros:
            avisos.append(f"aviso avaliacao: vídeo do escopo sem registro_video nem prova: {rotulo}")
    inventario, classificados = _ler_inventario(pasta) if pasta is not None else ("", {})
    for chave, cids in docs_citados.items():
        if _nao_conta(classificados.get(chave, "")):
            avisos.append(
                "aviso avaliacao: documento citado como prova mas classificado \"não conta\" no inventario.md: "
                f"{chave} ({_provas(cids)})"
            )
    for real, rotulo in escopo["documentacao"]:
        if real in citados["documentacao"]:
            continue
        chave = _norm(rotulo)
        if chave in classificados:
            classe = classificados[chave]
            if not classe or PLACEHOLDER in classe:
                avisos.append(f"aviso avaliacao: documento do escopo sem classificação no inventario.md: {rotulo}")
        elif rotulo not in inventario:
            avisos.append(f"aviso avaliacao: documento do escopo sem prova nem menção no inventario.md: {rotulo}")
    restantes = inventario.count(PLACEHOLDER)
    if restantes:
        avisos.append(f"aviso inventario: ainda contém {PLACEHOLDER} ({restantes} ocorrência{'s' if restantes != 1 else ''})")
    return avisos
