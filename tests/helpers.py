"""Shared fixtures for catalog tests. Every function returns a fresh copy."""

import copy
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent


def schema_valido():
    return yaml.safe_load((REPO / "catalog" / "schema.yaml").read_text(encoding="utf-8"))


def categorias_validas():
    return yaml.safe_load((REPO / "catalog" / "categorias.yaml").read_text(encoding="utf-8"))


_DIRETRIZ = {
    "id": "D17",
    "categoria": "mediacao",
    "diretriz": "O jogo deve exibir feedback construtivo para as ações do jogador",
    "fonte": "Carvalho (2020), Quadro 3",
    "modalidade": "deve",
    "aplicabilidade": None,
    "criterios": [
        {
            "id": "D17.1",
            "nivel": "A",
            "enunciado": "Toda ação incorreta do jogador recebe mensagem que indica o que fazer, não só que errou",
            "nivel_justificativa": {
                "essencialidade": "alta",
                "viabilidade": "alta",
                "texto": "Mediação é núcleo da ZDP; feedback que só sinaliza acerto/erro é reforço behaviorista.",
            },
            "evidencia": {
                "codigo": {
                    "procedimento": "Localizar tratadores de erro e verificar o texto exibido",
                    "indicadores": ["mensagem contém orientação de próxima ação"],
                },
                "documentacao": None,
                "video": {
                    "procedimento": "Registrar timestamp de cada erro e classificar o feedback",
                    "indicadores": ["ao menos 3 ocorrências de erro", "cada ocorrência mostra orientação"],
                },
            },
            "escala": {
                "atendido": "Todas as ocorrências observadas orientam o jogador",
                "parcial": "Algumas ocorrências orientam, outras só sinalizam erro",
                "nao_atendido": "Feedback só sinaliza acerto/erro ou inexiste",
            },
            "recomendacao": {
                "documentacao": "Registrar no documento de design a tabela de erros com a mensagem exibida em cada um e a próxima ação que ela indica",
                "design": "Definir, para cada ação incorreta prevista, a próxima ação que a mensagem indica ao jogador",
                "codigo": "Trocar, em cada manipulador de erro, a mensagem que só sinaliza o erro por uma que indica a próxima ação",
            },
            "depende_de": [],
        }
    ],
}


def diretriz_valida():
    return copy.deepcopy(_DIRETRIZ)


def glossario_valido():
    return yaml.safe_load((REPO / "catalog" / "definicoes.yaml").read_text(encoding="utf-8"))


def catalogo_real():
    from vygolint_catalog.catalog import load_catalog

    cat, errors = load_catalog(REPO / "catalog")
    assert not errors, errors
    return cat


def avaliacao_valida(fontes=("codigo", "documentacao", "video")):
    """Every criterion atendido, one proof per source the criterion accepts and the context has."""
    cat = catalogo_real()
    fontes = list(fontes)
    criterios = {}
    for cid, item in cat["criterios"].items():
        c = item["criterio"]
        usadas = {}
        for f in fontes:
            if c["evidencia"].get(f) is not None:
                usadas[f] = {"grau": "atendido", "provas": [f"{f} — prova de {cid}"]}
        if usadas:
            criterios[cid] = {"grau": "atendido", "fontes": usadas}
        else:
            criterios[cid] = {"grau": "nao_avaliado", "razao": f"nenhuma fonte disponível avalia {cid}"}
    return {
        "jogo": "Jogo de teste",
        "contexto": {
            "sala_de_aula": True,
            "fontes": fontes,
            "artefatos": {f: [f"./{f}"] for f in fontes},
        },
        "avaliador": "teste",
        "data": "2026-11-04",
        "criterios": criterios,
    }
