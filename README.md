# vygolint

Ferramenta de avaliação de conformidade de jogos educacionais digitais: um
catálogo de 43 critérios testáveis, com níveis A, AA e AAA, e um plugin para
agentes de código que avalia um jogo a partir do código, da documentação e de
vídeos de gameplay e gera o relatório.

Criado e mantido por Rodrigo Dobbin Fellows. Os critérios derivam das 40
diretrizes sociointeracionistas de Carvalho (2020); ver
[Autoria e fontes](#autoria-e-fontes).

## O que há aqui

| Caminho | Conteúdo |
|---|---|
| `catalog/D01.yaml` … `D40.yaml` | uma diretriz por arquivo: texto literal, critérios, níveis, evidências, escalas, recomendações por via (documentação, design, código) |
| `catalog/schema.yaml` | esquema validado pelo build |
| `catalog/definicoes.yaml` | glossário: definições compartilhadas pelos critérios, impressas uma vez por critério |
| `catalog/categorias.yaml` | 12 categorias e a ressalva de Carvalho (2020) sobre elas |
| `docs/catalogo.md` | catálogo completo, gerado |
| `docs/catalogo.tex` | tabela resumo para LaTeX, gerada |
| `docs/conformidade.md` | regras de nível, grau, agregação e relatório; §6 descreve cada arquivo e script da avaliação |
| `docs/experimentos/` | experimentos com o fluxo (ex.: critérios graduados por subagentes) |
| `CHANGELOG.md` | o que mudou em cada versão |
| `LICENSE`, `LICENSE-CONTENT.md`, `NOTICE`, `CITATION.cff` | licenças (código e conteúdo), material de terceiros e como citar |
| `scripts/build_catalog.py` | valida o catálogo e regenera os docs |
| `scripts/vygolint_scaffold.py` | gera o esqueleto de `avaliacao.yaml`: cabeçalho (artefatos como arquivos ou pastas; uma pasta põe no escopo tudo o que está dentro) e uma entrada por critério do catálogo; gera também o de `inventario.md`, com uma linha por arquivo do escopo |
| `scripts/vygolint_report.py` | valida `avaliacao.yaml`, confere o lugar citado em cada prova e a cobertura do escopo declarado (avisos; `--strict` os trata como erro e é a execução final da entrega) e gera `relatorio.md`, `relatorio.html` (página navegável por público) e `resultado.yaml`; `--status` só diz quantos critérios estão preenchidos e qual é o próximo |
| `scripts/vygolint_juntar.py` | grava em `avaliacao.yaml` as entradas graduadas em partes (um `.yaml` por categoria ou por subagente), conferindo os ids contra o catálogo |
| `scripts/vygolint_diff.py` | compara dois `resultado.yaml` (antes e depois): nível, contagem por grau e cada critério que mudou de grau, classificado como melhora, piora, passou/deixou de ser avaliado ou entrou/saiu do contexto |
| `scripts/vygolint_audio.py` | mede a faixa de áudio de um vídeo e gera `registro_audio_<nome>.yaml`: trechos com som e, com a transcrição de um reconhecedor de fala, as falas |
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
4. Receba, em `vygolint-out/`:
   - `avaliacao.yaml`: o julgamento do agente, critério a critério, com as provas (lugar em arquivo, página ou instante do vídeo);
   - `inventario.md`: missões, minijogos, cenários jogáveis, objetivos de aprendizagem e a classificação de cada documento lido;
   - `registro_video_<nome>.yaml` e `registro_audio_<nome>.yaml`: eventos com instante e trechos com som (e falas, quando há reconhecedor) de cada vídeo;
   - `relatorio.md`, `relatorio.html` e `resultado.yaml`, gerados por `scripts/vygolint_report.py`. O `relatorio.html` abre em qualquer navegador e organiza o mesmo conteúdo em abas para professor, equipe de desenvolvimento e coordenação, com filtros por grau, nível e categoria; o `relatorio.md` serve para anexar em issue ou versionar; o `resultado.yaml` alimenta `scripts/vygolint_diff.py` para comparar com outra avaliação (versão anterior do jogo, ou avaliação humana).

O fluxo que a skill segue, com o script de cada passo:

| Passo | O que acontece | Script |
|---|---|---|
| 1. Contexto | nome, sala de aula, fontes e artefatos (arquivos ou pastas); esqueleto de `avaliacao.yaml` e de `inventario.md` | `vygolint_scaffold.py` |
| 2. Inventário | leitura das fontes; vídeo vira registro de eventos e de áudio | `vygolint_audio.py` (+ ffmpeg) |
| 3. Critérios | um grau e provas por critério, gravados no esqueleto; opcionalmente em partes por subagente | `vygolint_juntar.py`; `vygolint_report.py --status` para retomar |
| 4. Relatório | validação, lint de provas e cobertura do escopo, relatórios | `vygolint_report.py` |
| 5. Entrega | execução final com `--strict`, comparação com avaliação anterior se houver | `vygolint_report.py --strict`; `vygolint_diff.py` |

As skills exigem Python 3 com PyYAML disponível ao agente (para os scripts); o hook de início de sessão procura um interpretador que importe `yaml` (`python3`, depois `.venv` do plugin, depois `python`) e injeta o caminho como `VYGOLINT_PYTHON`, junto com a presença de ffmpeg e de um reconhecedor de fala; ffmpeg é opcional (extração de quadros e medição do áudio do vídeo); um reconhecedor de fala como o `openai-whisper` é opcional (transcrição das falas).

## Como funciona o nível

Cada critério declara essencialidade teórica e viabilidade; o nível sai de uma
tabela fixa (ver `docs/conformidade.md`). O build falha se o YAML declarar outro
nível. O resultado de uma avaliação expressa conformidade com os critérios do
vygolint, não um rótulo de "jogo sociointeracionista".

## Autoria e fontes

O vygolint foi criado e é mantido por **Rodrigo Dobbin Fellows**. São do vygolint:

- os 43 critérios testáveis e seus enunciados;
- o nível de cada critério e a regra que o deriva (essencialidade teórica × viabilidade);
- o glossário de definições, os procedimentos e indicadores de evidência por fonte (código, documentação, vídeo) e as escalas de grau;
- as dependências entre critérios e as recomendações por via (documentação, design, código);
- as regras de conformidade (`docs/conformidade.md`), os scripts, as skills e os relatórios.

O que vem de outros trabalhos:

- **Diretrizes.** O texto das 40 diretrizes (campo `diretriz` de cada `catalog/Dnn.yaml`, com a fonte em `fonte`), as 12 categorias e a ressalva sobre elas são de: CARVALHO, Diego Marques. *Diretrizes para o desenvolvimento de jogos educacionais digitais embasados na teoria sociointeracionista de Lev Semionovich Vigotski*. Dissertação (Mestrado em Ciência da Computação), UFABC, 2020. O vygolint não altera esse texto; ele o desdobra em critérios verificáveis.
- **Níveis.** A divisão em A, AA e AAA, com cada nível exigindo os anteriores, segue o modelo de conformidade das WCAG (W3C). O vygolint não é extensão das WCAG e não trata de acessibilidade.
- **Adaptadores de harness.** A estrutura de manifestos e hooks foi adaptada do [superpowers](https://github.com/obra/superpowers) (MIT).

Detalhes e avisos de licença de terceiros em `NOTICE`.

### Como citar

> FELLOWS, Rodrigo Dobbin. **vygolint**: avaliação de conformidade de jogos educacionais digitais com critérios sociointeracionistas. Versão 0.3.0. 2026. Disponível em: <https://github.com/rodrigodobbin/vygolint>.

`CITATION.cff` traz os mesmos dados em formato legível por máquina (o GitHub mostra "Cite this repository"). Quem usar o texto das diretrizes cita também Carvalho (2020).

## Licença

- Código (`scripts/`, `hooks/`, `skills/`, `tests/`, manifestos): [Apache License 2.0](LICENSE).
- Conteúdo (`catalog/`, `docs/`): [CC BY 4.0](LICENSE-CONTENT.md). O texto das diretrizes de Carvalho (2020) fica fora dessa licença.

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
