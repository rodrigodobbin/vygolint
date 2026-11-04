# vygolint — Etapa 2: skills, relatório e manifestos por harness

Data: 2026-11-04
Status: implementado (2026-11-04)

## 1. Objetivo

Fazer do vygolint um plugin portável entre agentes de código, no modelo do superpowers, que avalia qualquer jogo educacional digital contra o catálogo (43 critérios, níveis A/AA/AAA) a partir de código, documentação e vídeos de gameplay, e produz o relatório de conformidade definido em `docs/conformidade.md`, seção 5, com as recomendações do catálogo nos itens "bloqueios" e "parciais".

Divisão de trabalho: **julgamento no agente, agregação em código**. As skills dizem ao agente como ler o catálogo, inspecionar as evidências e registrar grau e provas por critério em `avaliacao.yaml`. Um script valida esse arquivo contra o catálogo, aplica as regras de conformidade (dependências, aplicabilidade, não avaliado, nível, coberturas, bloqueios, parciais) e gera `relatorio.md` e `resultado.yaml` de forma determinística e testada. O agente nunca calcula nível nem contagem.

Relação com a DSR v2 (`mestrado/dsr/v2/passo_a_passo.md`): Avaliação 1, requisito 5 (portabilidade: instala e executa em ao menos dois harnesses); Avaliação 2 (aplicação a Expedição Antártica e Rota do Plástico; relatório interpretável); Avaliação 3, C3 (kappa entre `resultado.yaml` e avaliação humana).

Fora do escopo: aplicar o plugin a um jogo real (Avaliação 2); transcrição de áudio; instalação efetiva nos harnesses (o Rodrigo verifica em dois harnesses, Avaliação 1.5); avaliação paralela por subagentes (a skill pode sugerir, não exige).

## 2. Decisões tomadas

| Decisão | Escolha | Alternativa descartada | Motivo |
|---|---|---|---|
| Arquitetura | skills em prosa + script de relatório | só skills em prosa; skill por fonte | agregação reprodutível e testável; o kappa da Avaliação 3 precisa de saída estável |
| Vídeo | quadros extraídos com ffmpeg lidos como imagens + `registro_video.yaml` com timestamps; sem ffmpeg, registro escrito pelo humano | só registro escrito; transcrição de áudio | agente lê imagens e texto, não vídeo; registro é a prova citável |
| Harnesses | todos os do superpowers (Claude Code, Codex, Cursor, Kimi, Gemini, OpenCode, Pi, Antigravity/Copilot via marketplace) | só dois | manifestos são pequenos; a DSR exige ao menos dois |
| Bootstrap | skill `using-vygolint` injetada no início da sessão pelo hook (como `using-superpowers`) | sem bootstrap, só descoberta por descrição | harnesses sem auto-trigger de skills precisam saber que o plugin existe |
| Saída | `avaliacao.yaml` (escrito pelo agente) → `relatorio.md` + `resultado.yaml` (gerados) | relatório escrito pelo agente | o relatório segue um formato fixo; o agente contribui só o julgamento |
| Dependência de runtime | Python 3 + PyYAML (já exigidos pelo build); ffmpeg opcional | zero dependências | o catálogo é YAML; não vale reescrever um parser |

## 3. Estrutura de pastas

```
vygolint/
  skills/
    using-vygolint/SKILL.md        # bootstrap: o que é, quando usar cada skill, cláusula
    vygolint-avaliar/SKILL.md      # orquestra a avaliação de um jogo
    vygolint-criterio/SKILL.md     # gradua um critério a partir das evidências
    vygolint-video/SKILL.md        # transforma vídeo em registro_video.yaml
  scripts/
    vygolint_report.py             # CLI: avaliacao.yaml -> relatorio.md + resultado.yaml
    vygolint_catalog/
      report.py                    # validação de avaliacao.yaml, agregação, render do relatório
      catalog.py                   # carrega o catálogo validado (reuso de build.py sem escrever docs)
  hooks/
    hooks.json                     # Claude Code: SessionStart -> run-hook.cmd session-start
    hooks-cursor.json
    run-hook.cmd
    session-start                  # injeta skills/using-vygolint/SKILL.md
  .claude-plugin/plugin.json, marketplace.json
  .codex-plugin/plugin.json
  .cursor-plugin/plugin.json
  .kimi-plugin/plugin.json
  .agents/plugins/marketplace.json
  .opencode/plugins/vygolint.js, INSTALL.md
  .pi/extensions/vygolint.ts
  gemini-extension.json, GEMINI.md
  package.json                     # type module; pi.extensions e pi.skills
  tests/
    test_report.py, test_manifests.py, test_skills.py
    fixtures/avaliacao_valida.yaml
  docs/
    conformidade.md                # + seção 6: formato de avaliacao.yaml e de resultado.yaml
    README.<harness>.md            # instalação por harness quando o README principal não basta
```

`vygolint_catalog/build.py` continua gerando `docs/catalogo.md`; `catalog.py` extrai dele a parte "carregar e validar" para que `report.py` leia o catálogo sem escrever docs.

## 4. Skills

Todas em português, frontmatter `name` e `description` (a descrição começa com "Use when…" em inglês curto seguido do português, como o superpowers faz para o trigger funcionar em qualquer harness). Caminhos relativos à raiz do plugin: nas skills, `${VYGOLINT_ROOT}` significa a pasta que contém `skills/`; a skill explica como descobri-la (pasta pai de `skills/` do próprio SKILL.md; em Claude Code, `${CLAUDE_PLUGIN_ROOT}`).

### 4.1 `using-vygolint`

Texto curto (até 40 linhas): o que o vygolint é; a cláusula de Carvalho (o resultado expressa conformidade com as diretrizes de Carvalho (2020) e não classifica o jogo como sociointeracionista); quando usar cada skill (pedido de avaliar um jogo → `vygolint-avaliar`; graduar um critério isolado → `vygolint-criterio`; vídeo bruto → `vygolint-video`); onde está o catálogo (`catalog/Dnn.yaml`, `catalog/definicoes.yaml`, `catalog/categorias.yaml`) e as regras (`docs/conformidade.md`); o agente nunca calcula nível ou contagem, roda `scripts/vygolint_report.py`.

### 4.2 `vygolint-avaliar`

Passos, na ordem:

1. **Contexto.** Perguntar (ou ler do pedido) nome do jogo, se é aplicado em sala de aula (aplicabilidade de D22), quais fontes existem (código, documentação, vídeo) e onde estão. Criar a pasta de saída (padrão `vygolint-out/` no diretório de trabalho) e escrever o cabeçalho de `avaliacao.yaml`.
2. **Inventário.** Código: listar módulos, cenas, telas, manipuladores de entrada e de rede; documentação: listar documentos e seções, identificar o GDD ou documento equivalente (nos termos do glossário) e a lista de objetivos de aprendizagem; vídeo: para cada arquivo, usar `vygolint-video` e obter `registro_video.yaml`. Gravar o inventário em `inventario.md` (lista de missões, minijogos, cenários jogáveis e objetivos de aprendizagem encontrados, com onde cada um aparece), porque muitos critérios contam sobre essas listas.
3. **Critérios.** Para D01 a D40, em ordem: ler `catalog/Dnn.yaml` inteiro; para cada critério, aplicar `vygolint-criterio` e acrescentar a entrada em `avaliacao.yaml`. Gravar após cada diretriz (retomável). Critério cuja `aplicabilidade` não vale no contexto declarado: registrar `grau: fora_do_contexto` com `razao`. Critério cujas fontes necessárias não existem ou não mostram o ponto avaliado: `grau: nao_avaliado` com `razao`.
4. **Relatório.** Rodar `python3 ${VYGOLINT_ROOT}/scripts/vygolint_report.py <pasta>/avaliacao.yaml` (gera `relatorio.md` e `resultado.yaml` na mesma pasta). Se o script apontar erros (grau inconsistente com as fontes sem justificativa, prova vazia, id inexistente), corrigir `avaliacao.yaml` e rodar de novo; nunca editar `relatorio.md`.
5. **Revisão.** Ler `relatorio.md` e checar: cláusula presente; cada bloqueio cita a via certa; nenhum texto do agente rotula o jogo. Entregar ao usuário os três arquivos.

A skill não exige subagentes; diz que, em harness com subagentes, cada categoria pode ser avaliada por um subagente que recebe o inventário e devolve as entradas da categoria, e que o controlador junta tudo em `avaliacao.yaml`.

### 4.3 `vygolint-criterio`

Como graduar um critério:

- Ler o bloco **Definições** do critério e aplicá-las igual às três fontes.
- Para cada fonte não nula no critério e disponível no contexto: seguir `procedimento`, verificar cada `indicadores[i]`, anotar as provas (formato na seção 6) e atribuir o grau da fonte pelos descritores da `escala`.
- Grau final: o pior entre as fontes usadas. Para divergir (por exemplo, código mostra o recurso e o vídeo não o alcançou), escrever `justificativa_conflito`; sem ela o script rejeita. Vídeo prevalece sobre documentação: documentação promete, vídeo confirma.
- `nao_avaliado`: quando nenhuma fonte disponível permite decidir (só há vídeo e o vídeo não mostra o ponto avaliado); `razao` obrigatória.
- Proibido: inferir grau de nome de arquivo ou de intenção declarada sem o comportamento; usar evidência negativa de documentação (regra 6 de autoria); contar como "missão" o que não satisfaz a definição.
- O agente não escreve recomendação: o script copia `recomendacao` do catálogo.

### 4.4 `vygolint-video`

Entrada: um arquivo de vídeo. Procedimento: verificar `ffmpeg` no PATH; obter duração (`ffprobe`); extrair um quadro a cada N segundos (N = 5 por padrão, ajustável) e nas mudanças de cena (`select='gt(scene,0.4)'`) para `<pasta>/frames/<video>/hhmmss.png`; ler os quadros em ordem; escrever `registro_video.yaml` (formato na seção 6) com uma entrada por evento observável (início e fim de missão ou minijogo, feedback exibido, texto na tela, escolha do jogador, trecho passivo com início e fim). Sem ffmpeg: pedir ao usuário um registro no mesmo formato e seguir. A skill lembra que as medidas de tempo seguem a regra 14 de autoria (comprimento do conteúdo, não ritmo do jogador) e que o registro é a prova citada pelos critérios.

## 5. Script de relatório (`scripts/vygolint_report.py`, módulo `vygolint_catalog/report.py`)

Entrada: caminho de `avaliacao.yaml`; opções `--catalog` (padrão `<raiz>/catalog`), `--out` (padrão: pasta do arquivo de entrada). Saída: `relatorio.md` e `resultado.yaml`; código 1 e lista de erros em stderr quando a avaliação é inválida; nada é escrito nesse caso.

### 5.1 Validação de `avaliacao.yaml`

- Cabeçalho: `jogo` texto; `contexto.sala_de_aula` booleano; `contexto.fontes` subconjunto não vazio de `[codigo, documentacao, video]`; `contexto.artefatos` mapa fonte → lista de caminhos ou textos; `avaliador` texto; `data` ISO.
- `criterios`: mapa id → entrada. Todo id existe no catálogo; todo critério do catálogo tem entrada (ausente é erro, com mensagem "use nao_avaliado com razao").
- Entrada: `grau` em `[atendido, parcial, nao_atendido, nao_avaliado, fora_do_contexto]`; `razao` obrigatória para `nao_avaliado` e `fora_do_contexto`; `fora_do_contexto` só é aceito em critério cuja diretriz tem `aplicabilidade` não nula e quando `contexto.sala_de_aula` é falso (para D22); o inverso (D22 com sala de aula verdadeiro e `fora_do_contexto`) é erro.
- `fontes`: mapa com chaves em `[codigo, documentacao, video]`; cada chave usada precisa ser não nula em `evidencia` do critério e estar em `contexto.fontes`; cada fonte tem `grau` em `[atendido, parcial, nao_atendido]`, `provas` lista não vazia de textos, `observacao` opcional. Grau `atendido`/`parcial`/`nao_atendido` exige ao menos uma fonte.
- Coerência: grau final esperado = pior grau entre as fontes consideradas (`nao_atendido` < `parcial` < `atendido`), e a documentação não entra no cálculo quando há fonte `video` na entrada (vídeo prevalece sobre documentação: documentação promete, vídeo confirma; regra de `conformidade.md` seção 2). `grau` declarado diferente do esperado, para melhor ou para pior, exige `justificativa_conflito`; sem ela é erro.

### 5.2 Agregação

Ordem fixa:

1. **Aplicabilidade**: critérios `fora_do_contexto` saem das exigências de nível.
2. **Dependências**: para cada critério com `depende_de`, cada grupo precisa de ao menos um critério com grau efetivo `atendido`. Grupo não satisfeito → grau efetivo `nao_atendido`, com nota "por dependência (ids)". Se o grupo falha só por critérios `nao_avaliado`, o grau efetivo é `nao_avaliado` com nota "por dependência de não avaliado (ids)". Propagação em ordem topológica; ciclo é erro de catálogo (não ocorre hoje; o teste cobre).
3. **Nível do jogo**: A se todos os critérios A (fora `fora_do_contexto`) têm grau efetivo `atendido`; AA se A e todos os AA; AAA idem; senão "sem conformidade". `nao_avaliado` conta como não atendido.
4. **Cobertura por nível**: para A, AA, AAA: atendido, parcial, não atendido (dos quais N não avaliados), fora do contexto.
5. **Cobertura por categoria**: mesma contagem para as 12 categorias, na ordem de `categorias.yaml`.
6. **Bloqueios**: critérios do próximo nível não alcançado (se "sem conformidade", os A; se A, os AA; se AA, os AAA; se AAA, nenhum) com grau efetivo diferente de `atendido`, com a `recomendacao` do catálogo nas vias escolhidas pela regra: `codigo` em `contexto.fontes` → `codigo`; só documentação → `documentacao` e `design`; só vídeo → `design` e `codigo`; via escolhida nula → as demais não nulas. Bloqueio por dependência cita o critério de que depende em vez de recomendação própria.
7. **Parciais**: todos os critérios com grau efetivo `parcial`, com o descritor `escala.parcial` e o `escala.atendido` do catálogo (o que falta) e a `recomendacao` pela mesma regra de via.
8. **Provas**: por critério, por fonte, as provas e a observação; `justificativa_conflito` e `razao` quando houver.

### 5.3 `relatorio.md`

Cabeçalho gerado ("ARQUIVO GERADO por scripts/vygolint_report.py"), título com o nome do jogo, data, avaliador, contexto (sala de aula sim/não; fontes). Seções numeradas 1 a 7 na ordem de `docs/conformidade.md` seção 5. Tabelas Markdown para coberturas. Cada bloqueio: `#### Dnn.k — Nível N — <grau efetivo>` seguido do enunciado, do grau e das vias de recomendação (`- Documentação: …`). Determinístico (ordem por id; sem data de geração além da `data` da avaliação).

### 5.4 `resultado.yaml`

```yaml
jogo: ...
data: ...
avaliador: ...
nivel: AA | A | AAA | sem_conformidade
criterios:
  D01.1: {nivel: A, grau: atendido, grau_declarado: atendido, nota: null}
  D22.1: {nivel: AA, grau: fora_do_contexto, grau_declarado: fora_do_contexto, nota: "..."}
```

`grau` é o grau efetivo (após dependências); `grau_declarado` o do agente. Serve ao cálculo do kappa contra a avaliação humana e ao baseline de Carvalho (2020) para Expedição Antártica.

## 6. Formatos de entrada

### 6.1 `avaliacao.yaml`

```yaml
jogo: "Nome do jogo"
contexto:
  sala_de_aula: false
  fontes: [codigo, documentacao, video]
  artefatos:
    codigo: ["./src"]
    documentacao: ["docs/gdd.pdf", "docs/guia-professor.md"]
    video: ["gameplay/sessao1.mp4"]
avaliador: "Claude Code (claude-fable-5-1) com vygolint 0.2.0"
data: 2026-11-04
criterios:
  D01.1:
    grau: parcial
    fontes:
      documentacao:
        grau: parcial
        provas: ["docs/gdd.pdf p. 12 — missão 2 descrita como sequência de cliques sem estado inicial"]
      video:
        grau: parcial
        provas: ["gameplay/sessao1.mp4 00:04:10-00:06:30 — missão 2 resolvida repetindo a mesma ação"]
        observacao: "missão 1 (00:00:40-00:03:50) apresenta situação-problema"
  D22.1:
    grau: fora_do_contexto
    razao: "o jogo não é aplicado em sala de aula no contexto declarado"
  D06.1:
    grau: nao_avaliado
    razao: "não há código nem vídeo com dois jogadores; a documentação não cita multijogador"
```

Formato das provas: `arquivo:linha — trecho ou resumo` (código); `documento p. N — trecho` ou `documento, seção X — trecho` (documentação); `arquivo hh:mm:ss[-hh:mm:ss] — observação` (vídeo). Texto livre após o travessão; o script só exige texto não vazio.

### 6.2 `registro_video.yaml`

```yaml
video: "gameplay/sessao1.mp4"
duracao: "00:12:31"
quadros: "vygolint-out/frames/sessao1"   # pasta dos quadros, quando extraídos
eventos:
  - t: "00:00:40"
    fim: "00:03:50"
    tipo: missao            # missao | minijogo | feedback | texto | escolha | passivo | outro
    descricao: "Missão 1: coletar amostras; estado inicial visível, três ações disponíveis"
```

## 7. Manifestos e bootstrap

Uma versão (`0.2.0`) em todos os manifestos e em `package.json`; `tests/test_manifests.py` falha se divergirem. Conteúdo adaptado do superpowers: nome `vygolint`, descrição em inglês curto ("Conformance evaluation of educational games against Carvalho (2020) socio-interactionist guidelines, WCAG-style levels"), autor Rodrigo Dobbin Fellows, licença do repositório, `skills: "./skills/"` onde o formato aceita, hooks de início de sessão onde existem. `.opencode/plugins/vygolint.js` e `.pi/extensions/vygolint.ts` registram `skills/` e injetam `using-vygolint` (código portado do superpowers com o mapeamento de ferramentas reduzido ao que as skills usam: ler arquivos, rodar shell, ler imagens). `hooks/session-start` injeta `using-vygolint` (mesma lógica de formatos por plataforma). `GEMINI.md` aponta para `skills/using-vygolint/SKILL.md`.

README: seção "Instalação" por harness (comandos copiados do superpowers com o repositório `rodrigodobbin/vygolint`), seção "Como avaliar um jogo" (três linhas: instalar, pedir "avalie este jogo com o vygolint", receber a pasta `vygolint-out/`).

## 8. Testes

- `tests/test_report.py`: fixture `tests/fixtures/avaliacao_valida.yaml` cobrindo os 43 critérios com o catálogo real; um teste por regra de validação da seção 5.1; agregação: dependência não satisfeita, dependência de não avaliado, fora do contexto fora das contagens, nível por cada degrau, coberturas, bloqueios com a via certa em cada um dos quatro casos de fontes, parciais, determinismo (duas execuções, bytes iguais), `resultado.yaml` com grau efetivo e declarado.
- `tests/test_manifests.py`: todo JSON parseia; versões iguais entre manifestos e `package.json`; `skills` aponta para pasta existente; hook referenciado existe e é executável.
- `tests/test_skills.py`: todo `skills/*/SKILL.md` tem frontmatter com `name` igual ao nome da pasta e `description` não vazia; `using-vygolint` contém a cláusula literal; `vygolint-avaliar` cita `vygolint_report.py`.
- CLI: `tests/test_report.py` roda `scripts/vygolint_report.py` em subprocesso: código 0 com fixture válida, 1 com inválida, nada escrito no erro.
- Os 93 testes existentes continuam verdes.

## 9. Documentação

- `docs/conformidade.md`: seção 6 "Arquivos da avaliação" com os formatos da seção 6 desta spec e a regra de coerência entre grau e fontes; seção 5 ganha a frase "gerado por `scripts/vygolint_report.py` a partir de `avaliacao.yaml`".
- Spec do catálogo (`2026-11-03-catalogo-conformidade-design.md`): seção 7, "Relatório (formato definido na etapa 2…)" aponta para esta spec.
- README: tabela "O que há aqui" com `skills/`, `scripts/vygolint_report.py`, manifestos; instalação por harness; uso.
- `.superpowers/sdd/authoring-rules.md` (não versionado) ganha regras 25 a 28 para skills: imperativo, uma ação por linha, caminhos relativos à raiz do plugin, nunca pedir ao agente que calcule nível.

## 10. Pronto quando

- As quatro skills existem e passam `tests/test_skills.py`.
- `scripts/vygolint_report.py tests/fixtures/avaliacao_valida.yaml --out <tmp>` gera `relatorio.md` com as 7 seções e `resultado.yaml` com 43 entradas.
- Manifestos de todos os harnesses da seção 3, mesma versão, testados.
- `python3 scripts/build_catalog.py` continua imprimindo `OK: 40 diretrizes, 43 critérios`; todos os testes verdes; CI verde.
- README com instalação por harness e uso; `docs/conformidade.md` seção 6.
- PR aberto contra `main`.
