# vygolint — Campo `recomendacao` por critério

Data: 2026-11-04
Status: implementado (2026-11-04)

## 1. Objetivo

Dar a cada um dos 43 critérios do catálogo uma recomendação escrita uma vez, validada pelo build e impressa em `docs/catalogo.md`, para que a skill de avaliação da etapa 2 selecione e contextualize o texto em vez de inventar uma recomendação a cada avaliação. O relatório de conformidade (`docs/conformidade.md`, seção 5) já exige "bloqueios: critérios que impedem o próximo nível, com recomendação" e "parciais: o que falta para pleno"; este campo é a fonte desses dois itens.

Fora do escopo: a skill que lê o campo; qualquer mudança em enunciado, evidência, escala, nível ou definições dos critérios existentes.

## 2. Decisões tomadas

| Decisão | Escolha | Alternativa descartada | Motivo |
|---|---|---|---|
| Estrutura | um texto por via (`documentacao`, `design`, `codigo`) | sub-estrutura por estado (`parcial`, `nao_atendido`) dentro de cada via | nos 43 critérios, `parcial` é "alguns itens cumprem, outros não" e `nao_atendido` é "nenhum cumpre"; a ação é a mesma, muda só o conjunto de itens, que a skill contextualiza na avaliação |
| Obrigatoriedade | obrigatório desde já | opcional até completar | sem estado intermediário no catálogo; a PR só fecha com os 43 escritos |
| Lint do glossário | `textos_do_criterio` passa a incluir `recomendacao.<via>` | lista separada de campos só para a recomendação | as três regras do glossário (gatilho exige chave, definição inline proibida, definição repetida proibida) valem igual para a recomendação, sem código novo |
| Sentido das vias | `documentacao` = registrar no GDD ou documento equivalente o que o jogo já faz ou passa a fazer (gera a evidência documental); `design` = mudar regra, conteúdo ou estrutura do jogo no projeto; `codigo` = mudar a implementação | uma via por fonte de evidência (código, documentação, vídeo) | vídeo é fonte de evidência, não via de mudança; a recomendação diz o que mudar, não onde observar |
| Tabela LaTeX | inalterada | acrescentar coluna | a tabela é resumo; a recomendação vive no catálogo completo |

## 3. Esquema

`catalog/schema.yaml`:

```yaml
criterio:
  obrigatorios: [id, nivel, enunciado, nivel_justificativa, evidencia, escala, recomendacao, depende_de]
  recomendacao:
    vias: [documentacao, design, codigo]   # cada via: texto não vazio ou null; ao menos uma não nula
  definicoes:
    campos_lint: [enunciado, evidencia.*.procedimento, evidencia.*.indicadores, escala.*, recomendacao.*]
```

Exemplo em um critério:

```yaml
    escala:
      atendido: "Todas as ocorrências observadas orientam o jogador"
      parcial: "Algumas ocorrências orientam, outras só sinalizam erro"
      nao_atendido: "Feedback só sinaliza acerto/erro ou inexiste"
    recomendacao:
      documentacao: "Registrar no GDD ou documento equivalente a tabela de erros com a mensagem exibida em cada um e a próxima ação que ela indica"
      design: "Definir, para cada ação incorreta prevista, a próxima ação que a mensagem indica ao jogador"
      codigo: "Trocar, em cada manipulador de erro, a mensagem que só sinaliza o erro por uma que indica a próxima ação"
    depende_de: []
```

Regras do esquema (acrescentadas à seção 5 da spec do catálogo):

- `recomendacao` é obrigatório em todo critério. É um mapa com exatamente as chaves `documentacao`, `design` e `codigo`; chave ausente ou desconhecida é erro.
- Cada chave é texto não vazio ou `null`. `null` significa que aquela via não leva o critério a `atendido` (ex.: D22.1 só se atende por documentação). Ao menos uma chave não nula.
- O texto de cada via diz o que fazer para sair de `nao_atendido` ou `parcial` para `atendido`, em termos dos indicadores e da escala do próprio critério. Não cria exigência que o enunciado não faz, não cita jogo específico e não distingue os dois estados: a skill contextualiza com os itens que a avaliação encontrou.
- Lint do glossário: `recomendacao.<via>` é campo de texto do critério. Gatilho do glossário usado na recomendação exige a chave em `definicoes.glossario` (ou justificativa em `termos_comuns`); `Definição:`/`Definições:` e repetição do texto do glossário são erro, como nos demais campos.

## 4. Validação (`scripts/vygolint_catalog/validate.py`)

- `textos_do_criterio(c)` acrescenta `("recomendacao.<via>", texto)` para cada via com texto, na ordem `documentacao`, `design`, `codigo`.
- `_validate_criterio` ganha o bloco de `recomendacao`, no mesmo padrão de `evidencia`: não mapa; via ausente ("use null se não se aplica"); via com valor que não é texto não vazio nem `null`; chaves desconhecidas; nenhuma via não nula. Mensagens em português com prefixo `Dnn/Dnn.k`.
- A lista de vias vem de `schema["criterio"]["recomendacao"]["vias"]`, como `fontes_evidencia`.

## 5. Renderização (`scripts/vygolint_catalog/render.py`)

Depois do bloco `**Escala.**` e antes de `**Depende de.**`:

```
**Recomendações.**
- Documentação: <texto ou "não se aplica">
- Design: <texto ou "não se aplica">
- Código: <texto ou "não se aplica">
```

Ordem fixa das três linhas. `render_latex` não muda.

## 6. Conteúdo

Regras de autoria para recomendações (acrescentadas a `.superpowers/sdd/authoring-rules.md`, regras 19 a 24):

19. A recomendação deriva dos indicadores e da escala do critério: cada frase aponta para um indicador que passaria a ser satisfeito. Não cria exigência nova.
20. Acionável por quem recebe: `documentacao` pelo autor do GDD ou documento equivalente; `design` por quem projeta o jogo; `codigo` pelo desenvolvedor. O texto começa com verbo no infinitivo.
21. Uma frase por ação. Mais de uma ação na mesma via: frases separadas por ponto, na ordem em que seriam feitas.
22. Sem adjetivos de valor ("bom", "adequado", "claro") e sem advérbios de intensidade.
23. Sem citar jogo, produto ou motor específico; sem citar Expedição Antártica.
24. `null` só quando a via não leva o critério a `atendido`. Se o critério tem `evidencia.codigo: null`, `codigo` da recomendação costuma ser `null`, mas não é regra: a via pode existir (ex.: mudar o código gera o comportamento que o vídeo mostra).

Lotes de escrita, cada um validado pelo build e revisado por subagente contra as regras 1 a 24:

| Lote | Diretrizes | Critérios |
|---|---|---|
| A | D01 a D15 (interação) | 17 |
| B | D16 a D23 (mediação) | 9 |
| C | D24 a D29 (autonomia, socialização, lúdico) | 6 |
| D | D30 a D40 (realismo, personalização, organização, resolução de problemas, linguagem, atenção, aprendizado) | 11 |

## 7. Documentação

- Spec do catálogo (`2026-11-03-catalogo-conformidade-design.md`): seção 5 ganha o campo no exemplo YAML e as regras da seção 3 acima; seção 7 diz que "bloqueios" e "parciais" do relatório usam `recomendacao` do critério, com a via escolhida pela evidência disponível.
- `docs/conformidade.md`, seção 5: itens 5 e 6 citam o campo e a regra de seleção de via.
- `README.md`: tabela do catálogo menciona recomendações; parágrafo de desenvolvimento cita a regra de lint.
- `docs/catalogo.md` regenerado.

## 8. Testes

- `tests/helpers.py`: `diretriz_valida()` ganha `recomendacao` com as três vias preenchidas.
- `tests/test_validate.py`: campo ausente; não mapa; via ausente; via vazia; via com tipo errado; chave desconhecida; todas nulas; gatilho na recomendação sem chave no glossário; definição inline na recomendação; `textos_do_criterio` lista as vias.
- `tests/test_render.py`: bloco entre Escala e Depende de; três linhas na ordem; `não se aplica` para `null`.
- `tests/test_build.py`: o catálogo real passa (já coberto pelo teste de build existente).
- Os 80 testes existentes continuam verdes; a fixture muda porque o campo é obrigatório.

## 9. Pronto quando

- Os 43 critérios têm `recomendacao` válida.
- `python3 scripts/build_catalog.py` imprime `OK: 40 diretrizes, 43 critérios`.
- `docs/catalogo.md` mostra `**Recomendações.**` em cada critério.
- Spec, `docs/conformidade.md` e README atualizados.
- PR aberto contra `main` com CI verde.
