# vygolint

Catálogo de conformidade e plugin de avaliação de jogos educacionais digitais
contra as 40 diretrizes sociointeracionistas de Carvalho (2020), com níveis
A, AA e AAA no modelo das WCAG.

Fonte das diretrizes: CARVALHO, Diego Marques. *Diretrizes para o desenvolvimento
de jogos educacionais digitais embasados na teoria sociointeracionista de Lev
Semionovich Vigotski*. Dissertação (Mestrado em Ciência da Computação), UFABC, 2020.

## O que há aqui

| Caminho | Conteúdo |
|---|---|
| `catalog/D01.yaml` … `D40.yaml` | uma diretriz por arquivo: texto literal, critérios, níveis, evidências, escalas, recomendações por via (documentação, design, código) |
| `catalog/schema.yaml` | esquema validado pelo build |
| `catalog/definicoes.yaml` | glossário: definições compartilhadas pelos critérios, impressas uma vez por critério |
| `catalog/categorias.yaml` | 12 categorias e a ressalva de Carvalho (2020) |
| `docs/catalogo.md` | catálogo completo, gerado |
| `docs/catalogo.tex` | tabela resumo para LaTeX, gerada |
| `docs/conformidade.md` | regras de nível, grau, agregação e relatório |
| `scripts/build_catalog.py` | valida o catálogo e regenera os docs |
| `skills/` | etapa 2: skills portáveis entre agentes de código (vazio por ora) |

## Como funciona o nível

Cada critério declara essencialidade teórica e viabilidade; o nível sai de uma
tabela fixa (ver `docs/conformidade.md`). O build falha se o YAML declarar outro
nível. O resultado de uma avaliação expressa conformidade com as diretrizes, não
um rótulo de "jogo sociointeracionista".

## Desenvolvimento

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=scripts python3 -m unittest discover -s tests -v
python3 scripts/build_catalog.py
```

`docs/catalogo.md` e `docs/catalogo.tex` nunca são editados à mão. O CI falha se
estiverem desatualizados. As regras de lint de `definicoes` (gatilho sem chave,
chave sem gatilho, definição repetida) estão na seção 5 do spec. O lint cobre também o campo `recomendacao` (três vias, ao menos uma não nula; ver `docs/superpowers/specs/2026-11-04-recomendacao-design.md`).

## Documentos de projeto

- Spec: `docs/superpowers/specs/2026-11-03-catalogo-conformidade-design.md`
- Plano: `docs/superpowers/plans/2026-11-03-catalogo-conformidade.md`
- Divergências de definições: `docs/superpowers/specs/2026-11-03-definicoes-divergencias.md`
- Plano do glossário: `docs/superpowers/plans/2026-11-03-definicoes-glossario.md`
- Spec do campo `recomendacao`: `docs/superpowers/specs/2026-11-04-recomendacao-design.md`
- Plano do campo `recomendacao`: `docs/superpowers/plans/2026-11-04-recomendacao.md`
