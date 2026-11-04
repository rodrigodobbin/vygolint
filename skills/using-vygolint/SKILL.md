---
name: using-vygolint
description: Use when a session starts with the vygolint plugin installed - explains what vygolint evaluates, which skill to use for evaluating a game, grading one criterion or turning gameplay video into evidence, and where the catalog and rules live
---

# Usando o vygolint

O vygolint avalia um jogo educacional digital contra 43 critérios derivados das 40 diretrizes de Carvalho (2020) para jogos sociointeracionistas, com níveis A, AA e AAA no modelo das WCAG. Entradas: código, documentação (GDD ou documento equivalente) e vídeos de gameplay.

> O resultado de uma avaliação vygolint expressa conformidade com as diretrizes de Carvalho (2020) e não classifica o jogo como sociointeracionista.

## Raiz do plugin

`${VYGOLINT_ROOT}` é a pasta que contém `skills/`, `catalog/` e `scripts/`.

1. Em Claude Code, use `${CLAUDE_PLUGIN_ROOT}`.
2. Em outros harnesses, use a pasta pai de `skills/` do SKILL.md que você está lendo.
3. Confirme com `ls "${VYGOLINT_ROOT}/catalog/D01.yaml"`.

## Qual skill usar

| Pedido | Skill |
|---|---|
| "avalie este jogo", "relatório de conformidade", "quais diretrizes o jogo atende" | `vygolint-avaliar` |
| graduar um critério isolado (ex.: "o jogo atende D17.1?") | `vygolint-criterio` |
| há vídeo de gameplay bruto para usar como evidência | `vygolint-video` (chamada por `vygolint-avaliar`) |

## Onde está cada coisa

- Catálogo: `${VYGOLINT_ROOT}/catalog/D01.yaml` … `D40.yaml`; glossário em `catalog/definicoes.yaml`; categorias em `catalog/categorias.yaml`; versão legível em `docs/catalogo.md`.
- Regras de grau, nível, agregação e relatório: `${VYGOLINT_ROOT}/docs/conformidade.md`.
- Relatório: `python3 ${VYGOLINT_ROOT}/scripts/vygolint_report.py <pasta>/avaliacao.yaml` (precisa de Python 3 e PyYAML).

## Regras fixas

1. O agente julga grau e provas por critério; nunca calcula nível, contagem ou bloqueio: isso é do script.
2. Toda prova aponta um lugar: `arquivo:linha`, `documento p. N` ou `vídeo hh:mm:ss`.
3. Não existe "não se aplica" por falta de recurso; só `fora_do_contexto` por aplicabilidade (D22, sala de aula) e `nao_avaliado` por falta de evidência, sempre com razão.
4. O relatório nunca rotula o jogo; repita a cláusula acima ao entregar.
