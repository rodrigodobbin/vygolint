---
name: using-vygolint
description: Use when a session starts with the vygolint plugin installed - explains what vygolint evaluates, which skill to use for evaluating a game, grading one criterion or turning gameplay video into evidence, and where the catalog and rules live
---

# Usando o vygolint

O vygolint avalia um jogo educacional digital contra 43 critérios derivados das 40 diretrizes de Carvalho (2020) para jogos sociointeracionistas, com níveis A, AA e AAA no modelo das WCAG. Entradas: código, documentação (GDD ou documento equivalente) e vídeos de gameplay.

> O resultado de uma avaliação vygolint expressa conformidade com as diretrizes de Carvalho (2020) e não classifica o jogo como sociointeracionista.

## Raiz do plugin

`${VYGOLINT_ROOT}` é a pasta que contém `skills/`, `catalog/` e `scripts/`.

Descubra a raiz nesta ordem; se um passo não der caminho, use o seguinte:

1. A linha `VYGOLINT_ROOT=…` injetada no início da sessão.
2. Em Claude Code, `${CLAUDE_PLUGIN_ROOT}`, se não estiver vazia.
3. A pasta pai de `skills/` do SKILL.md que você carregou.

Depois:

1. Confirme com `ls "${VYGOLINT_ROOT}/catalog/D01.yaml"`.
2. Em todo comando, substitua `${VYGOLINT_ROOT}` pelo caminho absoluto da raiz (ou prefixe o comando com `VYGOLINT_ROOT=/caminho/absoluto`); o shell não guarda variáveis entre comandos.

## Qual skill usar

| Pedido | Skill |
|---|---|
| "avalie este jogo", "relatório de conformidade", "quais diretrizes o jogo atende" | `vygolint-avaliar` |
| graduar um critério isolado (ex.: "o jogo atende D17.1?") | `vygolint-criterio` |
| há vídeo de gameplay bruto para usar como evidência | `vygolint-video` (chamada por `vygolint-avaliar`) |

## Onde está cada coisa

- Catálogo: `${VYGOLINT_ROOT}/catalog/D01.yaml` … `D40.yaml`; glossário em `${VYGOLINT_ROOT}/catalog/definicoes.yaml`; categorias em `${VYGOLINT_ROOT}/catalog/categorias.yaml`; versão legível em `${VYGOLINT_ROOT}/docs/catalogo.md`.
- Regras de grau, nível, agregação e relatório: `${VYGOLINT_ROOT}/docs/conformidade.md`.
- Esqueleto da avaliação: `python3 "${VYGOLINT_ROOT}/scripts/vygolint_scaffold.py" --help` (cabeçalho e as 43 entradas de `avaliacao.yaml`).
- Áudio de um vídeo: `python3 "${VYGOLINT_ROOT}/scripts/vygolint_audio.py" <vídeo> --out <pasta>` (trechos com som; chamado por `vygolint-video`).
- Relatório: `python3 "${VYGOLINT_ROOT}/scripts/vygolint_report.py" <pasta>/avaliacao.yaml` (precisa de Python 3 e PyYAML); valida, confere o lugar das provas e gera os relatórios.

## Regras fixas

1. O agente julga grau e provas por critério; nunca calcula nível, contagem ou bloqueio: isso é do script.
2. Toda prova aponta um lugar: `arquivo:linha`, `documento p. N` ou `vídeo hh:mm:ss`.
3. Não existe "não se aplica" por falta de recurso; só `fora_do_contexto` por aplicabilidade (D22, sala de aula) e `nao_avaliado` por falta de evidência, sempre com razão.
4. O relatório nunca rotula o jogo; repita a cláusula acima ao entregar.
