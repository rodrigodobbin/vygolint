# vygolint — Catálogo de conformidade sociointeracionista (etapa 1)

Data: 2026-11-03
Status: implementado (etapa 1 concluída em 2026-11-03); revisão final aplicada; glossário de definições (2026-11-03); campo recomendacao (2026-11-04)

## 1. Objetivo

Transformar as 40 diretrizes de Carvalho (2020) para jogos educacionais digitais (JED) sociointeracionistas em um catálogo de **critérios testáveis** com **níveis de conformidade A, AA e AAA**, seguindo o modelo de conformidade das WCAG (W3C). O catálogo é a fonte única que, na etapa 2, as skills do plugin vygolint leem para avaliar um jogo a partir de código, documentação e vídeos de gameplay.

Fonte das diretrizes: CARVALHO, Diego Marques. *Diretrizes para o desenvolvimento de jogos educacionais digitais embasados na teoria sociointeracionista de Lev Semionovich Vigotski*. Dissertação (Mestrado em Ciência da Computação), UFABC, Santo André, 2020. Orientadora: Silvia Cristina Dotta. Quadro 3 (D1 a D40).

## 2. Escopo da etapa 1

Entrega:

- `catalog/`: `schema.yaml`, `categorias.yaml`, `D01.yaml` … `D40.yaml`
- `docs/catalogo.md` e `docs/catalogo.tex` (gerados)
- `docs/conformidade.md` (regras de nível e agregação, escrito à mão)
- `scripts/build_catalog.py`, `tests/`, CI
- `README.md`

Fora do escopo da etapa 1: skills, agentes, manifestos de harness, parser de vídeo, relatório automático. A pasta `skills/` nasce vazia só para fixar o layout.

## 3. Decisões tomadas

| Decisão | Escolha | Alternativas descartadas |
|---|---|---|
| Entradas que o plugin avaliará | código, documentação, vídeos de gameplay | só código; só jogo rodando |
| Lógica de nível | híbrida: essencialidade teórica define o nível base, viabilidade desempata | só essencialidade; só viabilidade |
| Pontuação por critério | híbrida: três graus (atendido, parcial, não atendido) no relatório; conformidade exige atendido pleno | binário WCAG puro; três graus puros |
| Formato | YAML por diretriz como fonte única; Markdown e LaTeX gerados | só documento; só máquina |
| Estrutura | WCAG enxuta: categoria > diretriz > critério (1 a 3 por diretriz); procedimentos dentro do critério por fonte de evidência | WCAG fiel com camada de técnicas; rubrica por diretriz sem critérios |
| Repositórios | `vygolint` (plugin e catálogo) separado de `mestrado` (DSR e dissertação) | tudo no repo do mestrado |
| Plataforma alvo | plugin portável no modelo do superpowers: `skills/` com `SKILL.md` + um manifesto por harness | plugin só para Claude Code |

## 4. Estrutura de pastas

```
vygolint/
  catalog/
    schema.yaml            # esquema do YAML de diretriz
    categorias.yaml        # 12 categorias de Carvalho, ordem, descrição, ressalva
    definicoes.yaml        # glossário: definições compartilhadas pelos critérios
    D01.yaml … D40.yaml    # uma diretriz por arquivo
  docs/
    catalogo.md            # GERADO
    catalogo.tex           # GERADO (longtable para abntex2)
    conformidade.md        # regras de nível e agregação
    superpowers/specs/     # este documento
  scripts/
    build_catalog.py
  tests/
  skills/                  # etapa 2
  requirements.txt         # pyyaml
  README.md
```

Fonte de verdade é o YAML. `docs/catalogo.md` e `docs/catalogo.tex` nunca são editados à mão.

## 5. Esquema de uma diretriz

```yaml
id: D17
categoria: mediacao            # chave em categorias.yaml
diretriz: "O jogo deve exibir feedback construtivo para as ações do jogador"
fonte: "Carvalho (2020), Quadro 3"
modalidade: deve               # deve | pode  (D20 e D21 usam "pode")
aplicabilidade: null           # null ou condição de contexto (ex.: D22 só quando aplicado em sala de aula)
criterios:
  - id: D17.1
    nivel: A                   # A | AA | AAA, derivado pela tabela da seção 6
    enunciado: "Toda ação incorreta do jogador recebe mensagem que indica o que fazer, não só que errou"
    nivel_justificativa:
      essencialidade: alta     # alta | media | baixa
      viabilidade: alta        # alta | media | baixa
      texto: "Mediação é núcleo da ZDP; feedback que só sinaliza acerto/erro é reforço behaviorista. Implementação de baixo custo."
    evidencia:                 # cada chave é null quando a fonte não serve para este critério
      codigo:
        procedimento: "Localizar tratadores de erro/falha e verificar o texto exibido"
        indicadores: ["mensagem contém orientação de próxima ação", "mensagem referencia o conteúdo envolvido"]
      documentacao:
        procedimento: "Verificar no GDD a especificação de feedback por tipo de erro"
        indicadores: ["tabela de erros com mensagem orientadora"]
      video:
        procedimento: "Registrar timestamp de cada erro do jogador e classificar o feedback exibido"
        indicadores: ["ao menos 3 ocorrências de erro", "cada ocorrência mostra orientação"]
    escala:
      atendido: "Todas as ocorrências observadas orientam o jogador"
      parcial: "Algumas ocorrências orientam, outras só sinalizam erro"
      nao_atendido: "Feedback só sinaliza acerto/erro ou inexiste"
    recomendacao:              # obrigatório; o que fazer para chegar a atendido, por via; null quando a via não serve
      documentacao: "Registrar no GDD ou documento equivalente a tabela de ações incorretas previstas com a mensagem exibida em cada uma e a próxima ação que ela indica"
      design: "Definir, para cada ação incorreta prevista, a próxima ação que a mensagem indica ao jogador"
      codigo: "Trocar, em cada manipulador de erro, a mensagem que só sinaliza o erro por uma que indica a próxima ação"
    depende_de: []             # lista de grupos; ex.: [[D06.1, D07.1]] = D06.1 ou D07.1
    definicoes:                # opcional; obrigatório quando o texto usa um gatilho do glossário
      glossario: [missao]      # chaves de catalog/definicoes.yaml, impressas uma vez por critério
      locais:                  # definições só deste critério: termo -> texto (predicado, sem "termo é")
        "ponto de feedback": "o momento em que o jogo responde a uma ação avaliada"
      termos_comuns:           # gatilho usado no sentido corrente, com justificativa
        "cenário": "sentido corrente de situação; não é o cenário jogável do glossário"
```

Regras do esquema:

- Texto da diretriz é literal do Quadro 3 de Carvalho (2020).
- `id` de critério no formato `Dnn.k`, único no catálogo.
- `categoria` precisa existir em `categorias.yaml`.
- Pelo menos uma fonte de evidência não nula por critério.
- `depende_de` é uma lista de grupos; cada grupo é uma lista de ids de critérios existentes. Todos os grupos precisam ser satisfeitos; dentro de um grupo basta um critério atendido. `[[D06.1, D07.1]]` significa "D06.1 ou D07.1"; `[[D06.1], [D09.1]]` significa "D06.1 e D09.1". Lista vazia quando não há dependência.
- `recomendacao` é obrigatório: mapa com exatamente as chaves `documentacao`, `design` e `codigo`, cada uma texto não vazio ou `null`, ao menos uma não nula. Cada texto diz o que fazer para sair de `nao_atendido` ou `parcial` para `atendido`, em termos dos indicadores e da escala do critério, sem distinguir os dois estados e sem criar exigência nova. `documentacao` = registrar no GDD ou documento equivalente o que o jogo faz; `design` = mudar regra, conteúdo ou estrutura do jogo no projeto; `codigo` = mudar a implementação. `null` só quando a via não contribui para levar o critério a `atendido`; as vias são complementares (`design` muda o projeto, `documentacao` registra a mudança). Regras de autoria: `docs/superpowers/specs/2026-11-04-recomendacao-design.md`, seção 6.
- Definição compartilhada existe uma vez, em `catalog/definicoes.yaml` (`chave`, `termo`, `gatilhos`, `ancora`, `texto`). O texto de um critério (enunciado, procedimentos, indicadores, escala) não repete definições. É erro de build o campo conter `Definição:`/`Definições:` (sem distinguir maiúsculas) ou repetir uma definição do glossário na forma `<termo ou gatilho> é|são <texto do glossário>` (sem distinguir maiúsculas nem espaçamento); o texto do glossário solto, no meio de uma frase comum, é permitido.
- Lint: se o texto de um critério contém um gatilho de um termo do glossário, `definicoes.glossario` precisa listar a chave (ou `termos_comuns` precisa justificar o uso no sentido corrente). Chave listada sem gatilho no texto também é erro. `termos_comuns` não pode citar gatilho de chave listada em `glossario` nem gatilho ausente do texto (enunciado, evidências, escala, recomendação e locais). O texto das definições listadas conta como texto do critério (uma definição que cita "missão" exige `missao`). O lint cobre também as três vias de `recomendacao`.
- O renderizador imprime `**Definições.**` uma vez por critério, antes do enunciado, e uma seção `## Glossário` no início de `docs/catalogo.md` (antes de `## Resumo`). Imprime também um bloco `**Recomendações.**` (uma linha por via, "não se aplica" quando `null`) depois da escala e antes de `**Depende de.**`.
- Divergências de redação encontradas na migração e decisões respondidas: `docs/superpowers/specs/2026-11-03-definicoes-divergencias.md`.
- Critério testável: dois avaliadores com as mesmas evidências chegam ao mesmo grau. Descritores da escala devem ser observáveis. Proibido descritor do tipo "o jogo é motivador".

`categorias.yaml` lista as 12 categorias de Carvalho (interacao, mediacao, autonomia, socializacao, ludico, realismo, personalizacao, organizacao, resolucao_de_problemas, linguagem, atencao, aprendizado) com descrição curta e a ressalva da seção 4.4 da dissertação: categorias são instrumento de organização, não taxonomia da teoria de Vigotski.

## 6. Regras de nível

Nível de cada critério sai da tabela, nunca de opinião solta:

| Essencialidade | Viabilidade alta ou média | Viabilidade baixa |
|---|---|---|
| alta: sem isso o jogo é behaviorista | A | AA |
| média: socialização, mediação por pares, escolha | AA | AAA |
| baixa: criação, adaptação, extras | AAA | AAA |

Regra adicional: `modalidade: pode` nunca gera A. Se a tabela der A para um critério de diretriz "pode", o nível sobe para AA.

Definições operacionais dos eixos:

- **Essencialidade alta:** o critério materializa um princípio sem o qual a mecânica é behaviorista (resolução de problemas, interação ativa com objetos, mediação por feedback orientador, atividade do jogador).
- **Essencialidade média:** o critério materializa socialização, mediação entre pares, autonomia de escolha, contextualização realista.
- **Essencialidade baixa:** o critério materializa criação de conteúdo pelo jogador, personalização adaptativa, recursos complementares.
- **Viabilidade alta:** implementável em qualquer JED com mecânicas comuns, baixo custo.
- **Viabilidade média:** exige sistema dedicado (persistência, comunicação assíncrona, perfil de desempenho).
- **Viabilidade baixa:** exige infraestrutura rara em JED (multiplayer síncrono, editor de conteúdo, adaptação em tempo real).

Cada critério registra os dois eixos e um texto de justificativa ancorado em Vigotski ou no capítulo 5 de Carvalho (2020). O script recalcula o nível e falha se o YAML declarar outro.

## 7. Conformidade e agregação

**Por critério.** O avaliador registra o grau (atendido, parcial, não atendido) e, para cada fonte usada, as provas (trecho de código, página do documento, timestamp do vídeo). Grau final = pior grau entre fontes conflitantes, salvo justificativa escrita. Vídeo prevalece sobre documentação: documentação promete, vídeo confirma.

**Por diretriz.** Atendida no nível N quando todos os seus critérios de nível N ou inferior estão atendidos plenamente. Parcial não conta.

**Por jogo:**

| Nível do jogo | Exigência |
|---|---|
| A | todos os critérios A atendidos |
| AA | A + todos os critérios AA atendidos |
| AAA | AA + todos os critérios AAA atendidos |
| sem conformidade | qualquer critério A não atendido ou parcial |

**Relatório** (formato definido na etapa 2, mas o conteúdo é fixado aqui):

- cláusula obrigatória
- nível alcançado
- cobertura por nível: contagem de atendido, parcial, não atendido (dos quais N não avaliados) e fora do contexto, para A, AA e AAA
- cobertura por categoria: mesma contagem para cada uma das 12
- bloqueios: critérios que impedem o próximo nível, com a `recomendacao` do critério na via que cabe à evidência disponível (código avaliado: `codigo`; só documentação: `documentacao` e `design`; só vídeo: `design` e `codigo`; via escolhida nula: as demais vias não nulas)
- parciais: o que falta para pleno, com a `recomendacao` do critério contextualizada pelos itens que a avaliação encontrou fora do estado atendido
- provas por critério

**Dependências.** Critério cujo `depende_de` não está satisfeito recebe automaticamente não atendido, sem avaliação manual. Critério que depende de um critério não avaliado é registrado como não avaliado por dependência e conta como não atendido para fins de nível.

**Evidência insuficiente.** Quando nenhuma fonte disponível permite avaliar um critério (por exemplo, só há vídeo e o vídeo não mostra o ponto avaliado), o relatório registra **não avaliado** com a razão; para fins de conformidade de nível, o critério conta como não atendido.

**Sem "não se aplica" por ausência de recurso.** Jogo sem multiplayer não atende D6. Vigotski exige interação social e é isso que o catálogo mede. `aplicabilidade` serve só para dependência de contexto de uso (D22, sala de aula).

**Aplicabilidade.** Critério cuja `aplicabilidade` não é satisfeita no contexto declarado da avaliação (ex.: D22 quando o jogo não é aplicado em sala de aula) é registrado como **fora do contexto**, fica fora das exigências de nível e é listado no relatório com a razão. O contexto de uso é declarado no início da avaliação.

**Cláusula obrigatória.** Todo relatório e `docs/conformidade.md` abrem com: o resultado expressa conformidade com as diretrizes de Carvalho (2020) e não classifica o jogo como sociointeracionista. Isso responde à ressalva da seção 4.4 e das considerações finais da dissertação de origem.

## 8. Gerador, validação e testes

Stack: Python 3 + PyYAML. Testes com `unittest`. `requirements.txt` com uma linha.

`scripts/build_catalog.py`, nesta ordem, parando na primeira falha:

1. **Valida estrutura** contra `schema.yaml`: campos obrigatórios, enums, ids únicos no formato `Dnn.k`, categoria existente, `depende_de` resolvível, ao menos uma evidência não nula.
   Valida também `definicoes.yaml` (chaves únicas, gatilhos sem colisão) e, por critério, o lint de `definicoes` descrito na seção 5 (gatilho sem chave listada, chave sem gatilho, definição inline ou repetida).
2. **Valida coerência de nível** pela tabela da seção 6 mais a regra "pode nunca é A". Divergência gera erro apontando arquivo e critério.
3. **Gera** `docs/catalogo.md` (tabela resumo + seção por diretriz com critérios, evidências e escalas) e `docs/catalogo.tex` (`longtable` com o resumo). Ambos com cabeçalho "arquivo gerado, não edite". Saída determinística.

Testes em `tests/`: fixtures válidas e inválidas; um teste por regra de validação; tabela de níveis coberta nas 9 combinações mais a regra "pode"; verificação de sincronia dos docs gerados no CI (git diff --exit-code).

CI (GitHub Actions): roda testes, roda o build e `git diff --exit-code docs/`. Doc desatualizado quebra o build.

## 9. Ordem de escrita do catálogo

1. `schema.yaml`, `categorias.yaml`, script, testes, CI.
2. Piloto com duas diretrizes: D17 (simples, uma fonte de evidência forte em vídeo) e D06 com D16 (dependência entre critérios). Revisão humana do formato.
3. Demais diretrizes em lotes por categoria, cada lote validado pelo script e revisado.
4. `docs/conformidade.md`.
5. README com instalação do build e explicação do catálogo.

## 10. Relação com a DSR

A DSR v2 do mestrado (`mestrado/dsr/v2/passo_a_passo.md`) define o vygolint como artefato e usa este catálogo na Avaliação 1 (artefato válido: cobre as 40, níveis derivados, script valida) e como instrumento das Avaliações 2 e 3. A análise que Carvalho (2020) fez de Expedição Antártica (atendida, parcial, não atendida para as 40) serve de baseline humano para medir concordância com o plugin na etapa 2.
