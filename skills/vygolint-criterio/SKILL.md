---
name: vygolint-criterio
description: Use when grading one vygolint criterion from code, documentation or gameplay video evidence - how to read the criterion's definitions, procedures and indicators, record proofs per source, pick the final grade and write the avaliacao.yaml entry
---

# Graduar um critério do vygolint

> O resultado de uma avaliação vygolint expressa conformidade com as diretrizes de Carvalho (2020) e não classifica o jogo como sociointeracionista.

Entrada: um id de critério (ex.: `D17.1`), as fontes disponíveis e, quando houver, `inventario.md` e `registro_video.yaml` (ver `vygolint-avaliar` e `vygolint-video`). Saída: a entrada YAML do critério para `avaliacao.yaml`. Você grava grau e provas; nível, dependências e recomendação são do script `scripts/vygolint_report.py`.

## 1. Leia o critério inteiro

1. Abra `${VYGOLINT_ROOT}/catalog/Dnn.yaml` e localize o critério pelo `id`.
2. Leia primeiro as **Definições**: a versão impressa está em `${VYGOLINT_ROOT}/docs/catalogo.md`, seção `#### Dnn.k`. No YAML, `definicoes.glossario` lista chaves de `${VYGOLINT_ROOT}/catalog/definicoes.yaml`; `definicoes.locais` define termos só deste critério; `definicoes.termos_comuns` marca palavras usadas no sentido corrente, que não carregam a definição do glossário.
3. Leia o `enunciado`: ele já traz o limiar de atendido.
4. Leia `evidencia`: para cada fonte (`codigo`, `documentacao`, `video`), um `procedimento` e uma lista de `indicadores`. Fonte `null` não serve para este critério.
5. Leia a `escala`: `atendido`, `parcial` e `nao_atendido` são os únicos descritores de grau.
6. Ignore `recomendacao`, `nivel` e `nivel_justificativa`: não decidem grau.
7. Se o critério tem `depende_de`, não faça nada com isso: o script aplica as dependências.
8. Aplique as definições igual nas três fontes. "Missão" no código é a mesma "missão" do vídeo.

## 2. Avalie cada fonte

Faça, para cada fonte não nula no critério e disponível no contexto (`contexto.fontes` de `avaliacao.yaml`):

1. Execute o `procedimento` daquela fonte.
2. Verifique cada indicador, um por um, e anote se é satisfeito e onde.
3. Use as listas de `inventario.md` (missões, minijogos, cenários jogáveis, objetivos de aprendizagem) quando o critério contar algo.
4. Anote as provas no formato abaixo.
5. Atribua o grau da fonte comparando o que achou com os descritores da `escala`: `atendido`, `parcial` ou `nao_atendido`.
6. Em vídeo, o que você afirma sobre áudio vem do registro (`som` e `fala` de cada evento, ver `vygolint-video`): `fala` é fala de conteúdo determinado, e serve onde o critério aceita "texto ou fala" ou compara o texto com o áudio; `som: nao` prova que o evento não tem som; `som: inicia` sem `fala` é som de conteúdo não determinado (efeito ou música disparado pelo evento); `som: continua` é fundo e não conta como resposta ao evento. Sem registro de áudio, não afirme nada sobre som ou fala e diga isso na `observacao`.
7. Se a fonte existe mas não mostra o ponto avaliado (ex.: o vídeo não chega à missão em questão), não a use nesta entrada e anote o motivo para a `razao` ou para a `observacao` de outra fonte.

Formato das `provas` (uma lista de textos por fonte, ao menos um; texto livre após o travessão):

| Fonte | Formato | Exemplo |
|---|---|---|
| codigo | `arquivo:linha — trecho ou resumo` | `src/feedback.js:42 — erro exibe "Tente de novo" sem próxima ação` |
| documentacao | `documento p. N — trecho` ou `documento, seção X — trecho` | `docs/gdd.pdf p. 12 — tabela de erros com mensagem orientadora` |
| video | `arquivo hh:mm:ss[-hh:mm:ss] — observação` | `gameplay/sessao1.mp4 00:04:10-00:06:30 — missão 2 resolvida repetindo a mesma ação` |

Cite só arquivos que estão nos artefatos da fonte (`contexto.artefatos` de `avaliacao.yaml`: o próprio arquivo ou um arquivo dentro de uma pasta declarada), com o caminho escrito como lá; o script avisa quando uma prova aponta para fora.

Use `observacao` (opcional, uma por fonte) para o que ajuda a ler as provas, como itens que satisfazem o critério ao lado dos que não satisfazem.

## 3. Grau final

1. Grau final = o pior grau entre as fontes usadas (`nao_atendido` < `parcial` < `atendido`).
2. Vídeo prevalece sobre documentação: documentação promete, vídeo confirma. Se a entrada tem a fonte `video`, a documentação não entra no cálculo do pior grau.
3. Código e vídeo sempre entram no cálculo.
4. Para gravar um grau final diferente do calculado (para melhor ou para pior), escreva `justificativa_conflito` com o motivo e as provas que o sustentam. Exemplo: o código tem um manipulador de erro sem orientação, mas nenhuma cena o chama, e o vídeo mostra orientação em todos os erros. Sem `justificativa_conflito`, o script rejeita a entrada.
5. Quando a fonte disponível não mostra o que o critério avalia, o grau é `nao_avaliado`, com `razao` que diz qual fonte faltou ou o que ela não mostrou. Há uma única exceção: o próprio critério traz grau por falta de evidência. Procure na `escala` e no `procedimento` da fonte frases como "por falta de evidência, o grau padrão é não atendido", "sem item observado, o grau pelo vídeo é nao_atendido", ou um descritor de `nao_atendido` que nomeia a falta (por exemplo, "o GDD não lista objetivos de aprendizagem", "GDD sem descrição do público-alvo"). Se o critério traz isso, grave `nao_atendido` na fonte usada, com a prova do que foi olhado e, na `observacao`, "grau por falta de evidência".
   - Não é exceção a gravação que cobre o jogo do menu à tela final: ela mostra o que o jogador gravado fez, não tudo o que o jogo oferece.
   - Não é exceção a regra de desempate do critério ("sem código nem GDD, vale o vídeo"): ela decide entre fontes que divergem sobre algo observado e não transforma ausência em evidência.
   - Fonte que o critério não aceita (`null` no catálogo), sem outra disponível: `nao_avaliado`.
   - Para o nível, o script conta `nao_avaliado` como não atendido; a diferença é o que o relatório diz ao leitor: "não vimos" ou "vimos que não faz".
6. Use `fora_do_contexto` só quando a diretriz tem `aplicabilidade` não nula e o contexto declarado não a satisfaz (hoje só D22, com `sala_de_aula: false`); `razao` obrigatória. Falta de recurso nunca é `fora_do_contexto`: jogo sem multijogador não atende D06.

## 4. Proibições

- Não inferir grau de nome de arquivo, de nome de função ou de intenção declarada sem o comportamento que a realiza.
- Não usar evidência negativa de documentação: o documento não proibir X não prova que o jogo faz X. A documentação prova só o que descreve.
- Não contar como missão, minijogo, desafio, cenário jogável ou situação-problema o que não satisfaz a definição impressa no critério.
- Não decidir pelo ritmo do jogador gravado: tempos em vídeo seguem o conteúdo (ver `vygolint-video`).
- Não escrever recomendação, nível ou nota de dependência na entrada.
- Não rotular o jogo (sociointeracionista, behaviorista ou outro) em provas, observações ou razões.

## 5. Entrada YAML

Grave sob `criterios:` em `avaliacao.yaml`, com dois espaços de recuo antes do id. Quando o arquivo veio do esqueleto (`scripts/vygolint_scaffold.py`), o id já existe: substitua as linhas `grau` e `razao` dele pela entrada, sem duplicar o id:

```yaml
  D17.1:
    grau: parcial
    fontes:
      codigo:
        grau: parcial
        provas:
          - "src/quiz.js:88 — erro de cálculo exibe dica com a próxima ação"
          - "src/mapa.js:140 — erro de rota só toca som de falha"
      video:
        grau: parcial
        provas: ["gameplay/sessao1.mp4 00:03:12 — erro na balança mostra 'Some as massas antes de pesar'"]
        observacao: "erro de rota em 00:07:45 sem mensagem"
  D06.1:
    grau: nao_avaliado
    razao: "não há código nem vídeo com dois jogadores; a documentação não cita multijogador"
```

Com divergência justificada:

```yaml
  D17.1:
    grau: atendido
    justificativa_conflito: "o único manipulador sem orientação (src/legado/erro.js:12) não é chamado por nenhuma cena; os manipuladores alcançáveis e o vídeo orientam a próxima ação"
    fontes:
      codigo:
        grau: parcial
        provas:
          - "src/quiz.js:88 — erro de cálculo exibe dica com a próxima ação"
          - "src/legado/erro.js:12 — mensagem 'Errado!' sem próxima ação; nenhuma referência ao módulo"
      video:
        grau: atendido
        provas: ["gameplay/sessao1.mp4 00:03:12 — erro na balança mostra 'Some as massas antes de pesar'"]
```

Ponha entre aspas toda prova, razão e observação. Mais regras: `${VYGOLINT_ROOT}/docs/conformidade.md`, seção 2.
