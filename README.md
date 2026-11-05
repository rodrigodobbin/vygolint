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
| `scripts/vygolint_scaffold.py` | gera o esqueleto de `avaliacao.yaml`: cabeçalho (artefatos como arquivos ou pastas; uma pasta põe no escopo tudo o que está dentro) e uma entrada por critério do catálogo |
| `scripts/vygolint_report.py` | valida `avaliacao.yaml`, confere o lugar citado em cada prova e a cobertura do escopo declarado (avisos; `--strict` os trata como erro) e gera `relatorio.md`, `relatorio.html` (página navegável por público) e `resultado.yaml` |
| `skills/` | quatro skills portáveis: `using-vygolint`, `vygolint-avaliar`, `vygolint-criterio`, `vygolint-video` |
| `docs/exemplo/` | avaliação de exemplo e relatório gerado |
| `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `.kimi-plugin/`, `.opencode/`, `.pi/`, `.agents/`, `gemini-extension.json` | manifestos por harness |

## Instalação

A instalação varia por harness; se você usa mais de um, instale o vygolint em cada um. Todas as formas abaixo partem deste repositório.

### Claude Code

- Registre o marketplace:

  ```bash
  /plugin marketplace add rodrigodobbin/vygolint
  ```

- Instale o plugin:

  ```bash
  /plugin install vygolint@vygolint
  ```

### Antigravity

```bash
agy plugin install https://github.com/rodrigodobbin/vygolint
```

### Codex CLI e Codex App

Adicione este repositório como marketplace de plugins do Codex e instale `vygolint` pelo gerenciador de plugins (`/plugins` no CLI; Plugins na barra lateral do app).

### Cursor

O manifesto está em `.cursor-plugin/plugin.json`. O Cursor instala plugins pelo seu marketplace (`/add-plugin`), que ainda não lista o vygolint; instale a partir de uma cópia local deste repositório, conforme a documentação de plugins do Cursor.

### Gemini CLI

```bash
gemini extensions install https://github.com/rodrigodobbin/vygolint
```

### Factory Droid

```bash
droid plugin marketplace add https://github.com/rodrigodobbin/vygolint
droid plugin install vygolint@vygolint
```

### GitHub Copilot CLI

```bash
copilot plugin marketplace add rodrigodobbin/vygolint
copilot plugin install vygolint@vygolint
```

### Kimi Code

```text
/plugins install https://github.com/rodrigodobbin/vygolint
```

### OpenCode

Diga ao OpenCode:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/rodrigodobbin/vygolint/refs/heads/main/.opencode/INSTALL.md
```

### Pi

```bash
pi install git:github.com/rodrigodobbin/vygolint
```

Para desenvolvimento local: `pi -e /caminho/para/vygolint`.

## Como avaliar um jogo

1. Instale o vygolint no seu agente (seção anterior).
2. Abra o agente na pasta do jogo.
3. Peça: "Avalie este jogo com o vygolint", informando onde estão o código, a documentação e os vídeos de gameplay e se o jogo é aplicado em sala de aula.
4. Receba `vygolint-out/avaliacao.yaml` (julgamento do agente, com provas), `relatorio.md`, `relatorio.html` e `resultado.yaml` (gerados por `scripts/vygolint_report.py`). O `relatorio.html` abre em qualquer navegador e organiza o mesmo conteúdo em abas para professor, equipe de desenvolvimento e coordenação, com filtros por grau, nível e categoria.

As skills exigem Python 3 com PyYAML disponível ao agente (para o script do relatório); ffmpeg é opcional (extração de quadros de vídeo).

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
- Spec da etapa 2 (skills, relatório, manifestos): `docs/superpowers/specs/2026-11-04-skills-design.md`
- Plano da etapa 2: `docs/superpowers/plans/2026-11-04-skills.md`
