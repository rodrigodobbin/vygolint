"""Lint the places cited by the proofs of an avaliacao.yaml.

validate_avaliacao checks the shape of the evaluation; this module checks whether each proof points
to something that exists: the cited file, the line inside it, the instant inside the video. It also
flags placeholders left by the scaffold. Findings are warnings: they never change a grade, and the
report is still generated unless the caller asks for strict mode.
"""

import re
import shutil
import subprocess
from pathlib import Path

from .report import FONTES
from .scaffold import PLACEHOLDER

_SEP = re.compile(r"\s+[—–]\s+|\s+-\s+")
_TS = r"\d{1,2}:\d{2}:\d{2}"
_CODIGO = re.compile(r"(.+?):(\d+)(?:-(\d+))?")
_DOC = re.compile(r"\s+pp?\.\s*\d+|,\s*se[cç][aã]o\b|\s+§")
_MAX_IDS = 5


def _lugar(prova):
    """Text before the dash that separates the place from the observation."""
    return _SEP.split(prova, maxsplit=1)[0].strip()


def _resolver(caminho, bases):
    p = Path(caminho).expanduser()
    if p.is_absolute():
        return p if p.exists() else None
    for base in bases:
        alvo = Path(base) / p
        if alvo.exists():
            return alvo
    return None


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


def lint_avaliacao(av, bases, duracao=duracao_ffprobe):
    """Return warning strings (`aviso ...`). `bases` are the folders relative paths are tried against."""
    if not isinstance(av, dict):
        return []
    avisos = []
    for campo in ("jogo", "avaliador"):
        if isinstance(av.get(campo), str) and PLACEHOLDER in av[campo]:
            avisos.append(f"aviso avaliacao: {campo} ainda contém {PLACEHOLDER}")
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
                if caminho and _resolver(caminho, bases) is None:
                    ausentes.setdefault(caminho, []).append(cid)
    for caminho, cids in ausentes.items():
        unicos = list(dict.fromkeys(cids))
        ids = ", ".join(unicos[:_MAX_IDS]) + (", …" if len(unicos) > _MAX_IDS else "")
        n = len(cids)
        avisos.append(f"aviso avaliacao: arquivo citado não encontrado: {caminho} ({n} prova{'s' if n != 1 else ''}: {ids})")
    return avisos
