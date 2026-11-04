---
name: vygolint-avaliar
description: Use when asked to evaluate an educational game against the Carvalho (2020) guidelines or to produce a vygolint conformance report - orchestrates context, inventory, per-criterion grading, avaliacao.yaml and the report script
---

# Avaliar um jogo com o vygolint

> O resultado de uma avaliação vygolint expressa conformidade com as diretrizes de Carvalho (2020) e não classifica o jogo como sociointeracionista.

Use esta skill quando pedirem "avalie este jogo com o vygolint" ou um relatório de conformidade. Ao final, o usuário recebe uma pasta com `avaliacao.yaml`, `relatorio.md` e `resultado.yaml`.

**Divisão de trabalho.** Você julga, critério a critério, o grau e as provas e grava isso em `avaliacao.yaml`. O script `scripts/vygolint_report.py` valida o arquivo, aplica dependências e aplicabilidade e calcula nível, coberturas, bloqueios e parciais. O agente nunca calcula nível, contagem nem bloqueio: grava grau e provas e roda o script.

`${VYGOLINT_ROOT}` é a raiz do plugin (ver `using-vygolint`). Regras completas de grau e relatório: `${VYGOLINT_ROOT}/docs/conformidade.md`.

## Passo 1 — Contexto

1. Leia do pedido o que já foi dito; pergunte ao usuário só o que faltar, numa única mensagem:
   - Qual é o nome do jogo?
   - O jogo é aplicado em sala de aula (com professor mediando)? Responda sim ou não.
   - Onde está o código-fonte (pasta ou repositório), se houver?
   - Onde está a documentação (GDD, roteiro, guia do professor, plano de aula), se houver?
   - Onde estão os vídeos de gameplay, se houver?
2. Considere fonte disponível só a que o usuário apontou e que você consegue abrir. Material de divulgação ou de loja não é documentação.
3. Pare e avise o usuário se não houver nenhuma fonte.
4. Crie a pasta de saída: `mkdir -p vygolint-out` no diretório de trabalho (ou a pasta que o usuário indicar). Chame-a de `<pasta>` daqui em diante.
5. Escreva o cabeçalho de `<pasta>/avaliacao.yaml`:

```yaml
jogo: "Nome do jogo"
contexto:
  sala_de_aula: false            # true se o jogo é aplicado em sala de aula
  fontes: [codigo, documentacao, video]   # só as fontes disponíveis
  artefatos:
    codigo: ["./src"]
    documentacao: ["docs/gdd.pdf", "docs/guia-professor.md"]
    video: ["gameplay/sessao1.mp4"]
avaliador: "Claude Code (claude-fable-5-1) com vygolint 0.2.0"
data: "2026-11-04"
criterios:
```

6. Em `fontes` e `artefatos`, deixe só as chaves das fontes disponíveis.
7. Em `avaliador`, escreva o harness, o modelo e a versão do vygolint (campo `version` de `${VYGOLINT_ROOT}/package.json`; se `package.json` não existir ou não tiver `version`, escreva `versão desconhecida`).
8. Em `data`, escreva a data de hoje no formato AAAA-MM-DD, entre aspas.

## Passo 2 — Inventário

1. Código: liste módulos, cenas, telas, manipuladores de entrada (handlers) e de rede, persistência e textos exibidos ao jogador.
2. Documentação: liste os documentos e suas seções; identifique o GDD ou documento equivalente (definição em `${VYGOLINT_ROOT}/catalog/definicoes.yaml`, chave `documentacao_equivalente`) e a lista de objetivos de aprendizagem.
3. Vídeo: para cada arquivo de vídeo, aplique a skill `vygolint-video` e obtenha `<pasta>/registro_video.yaml` (um por vídeo; com mais de um vídeo, `<pasta>/registro_video_<nome>.yaml`).
4. Leia `${VYGOLINT_ROOT}/catalog/definicoes.yaml` antes de contar qualquer coisa.
5. Escreva `<pasta>/inventario.md` com estas seções, cada item com onde aparece (`arquivo:linha`, `documento p. N` ou `vídeo hh:mm:ss`):
   - Missões (nos termos da definição de missão)
   - Minijogos
   - Cenários jogáveis
   - Objetivos de aprendizagem
   - Fontes lidas e fontes que não foi possível abrir
6. Use essas listas em todos os critérios que contam missões, minijogos, cenários ou objetivos; não recontar por critério evita contagens divergentes.

## Passo 3 — Critérios

1. Liste os critérios do catálogo: `grep -h "^  - id:" "${VYGOLINT_ROOT}"/catalog/D*.yaml` (devem ser 43).
2. Para cada diretriz de D01 a D40, em ordem:
   1. Leia `${VYGOLINT_ROOT}/catalog/Dnn.yaml` inteiro.
   2. Leia o bloco **Definições** de cada critério em `${VYGOLINT_ROOT}/docs/catalogo.md` (seção `#### Dnn.k`), onde o texto do glossário já vem impresso.
   3. Se a diretriz tem `aplicabilidade` não nula e o contexto não a satisfaz (hoje só D22, quando `sala_de_aula: false`), grave `grau: fora_do_contexto` com `razao` e passe à próxima.
   4. Para cada critério, aplique a skill `vygolint-criterio` e obtenha a entrada.
   5. Acrescente as entradas da diretriz ao fim de `<pasta>/avaliacao.yaml`, sob `criterios:`.
   6. Confira que o arquivo continua YAML válido: `python3 -c "import sys, yaml; yaml.safe_load(open(sys.argv[1], encoding='utf-8'))" <pasta>/avaliacao.yaml`.
3. Grave após cada diretriz. Se a sessão cair, releia `avaliacao.yaml` e retome na primeira diretriz sem entrada.
4. Todo critério do catálogo precisa de entrada. Sem fonte que decida, use `grau: nao_avaliado` com `razao`.
5. Não grave `recomendacao`, nível nem nota de dependência: o script os tira do catálogo. `depende_de` também é do script.

Entrada completa de um critério (formato de `docs/conformidade.md`, seção 6, e o exemplo em `docs/exemplo/avaliacao.yaml`):

```yaml
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

**Subagentes (opcional).** Em harness com subagentes, você pode avaliar cada categoria (`${VYGOLINT_ROOT}/catalog/categorias.yaml`; a categoria de cada diretriz está no campo `categoria`) em um subagente. Entregue a ele `inventario.md`, os registros de vídeo, os caminhos das fontes e as skills `vygolint-criterio` e `vygolint-video`; peça de volta só as entradas YAML da categoria. Junte tudo em `avaliacao.yaml` na ordem dos ids.

## Passo 4 — Relatório

1. Rode: `python3 "${VYGOLINT_ROOT}/scripts/vygolint_report.py" <pasta>/avaliacao.yaml`
2. Saída esperada: `OK: nível ... -> <pasta>/relatorio.md, <pasta>/resultado.yaml`.
3. Se aparecer `ModuleNotFoundError: No module named 'yaml'`, peça ao usuário para instalar o PyYAML (`python3 -m pip install pyyaml`) e rode de novo.
4. Se o script sair com código 1, ele lista um erro por linha e não gera nada. Corrija `avaliacao.yaml` e rode de novo até sair `OK`:

| Erro | O que fazer |
|---|---|
| `Dnn.k: critério sem entrada (use grau nao_avaliado com razao)` | Avalie o critério; se nenhuma fonte decide, grave `nao_avaliado` com `razao`. |
| `Dnn.k: grau X diverge do esperado pelas fontes (Y); escreva justificativa_conflito` | Corrija o grau final para Y, ou mantenha X e escreva `justificativa_conflito` (ver `vygolint-criterio`). |
| `Dnn.k: fonte F não existe na evidencia do critério` | Retire a fonte F da entrada: o critério não a usa. |
| `Dnn.k: fonte F não está em contexto.fontes` | Retire a fonte F da entrada, ou acrescente F ao cabeçalho se ela de fato foi usada. |
| `Dnn.k: ao menos uma fonte é obrigatória para o grau ...` | Acrescente `fontes` com grau e provas, ou troque o grau para `nao_avaliado` com `razao`. |
| `Dnn.k: fonte F precisa de provas` | Escreva ao menos uma prova com lugar (`arquivo:linha`, `documento p. N`, `vídeo hh:mm:ss`). |
| `Dnn.k: razao obrigatória para grau ...` | Escreva a `razao`. |
| `Dnn.k: fora_do_contexto ...` | Use `fora_do_contexto` só em D22 com `sala_de_aula: false`; nos outros casos, gradue o critério. |
| `avaliacao: ...` | Corrija o cabeçalho (passo 1). |
| qualquer outra mensagem `Dnn.k: …` | Corrija o campo que a mensagem nomeia na entrada de `avaliacao.yaml`; mensagens `avaliacao: …` apontam o cabeçalho. |

5. Nunca edite `relatorio.md` nem `resultado.yaml`: eles são gerados. Toda correção vai em `avaliacao.yaml`.

## Passo 5 — Revisão e entrega

Leia `<pasta>/relatorio.md` e confira:

- [ ] A cláusula de Carvalho (2020) está na seção 1.
- [ ] `avaliacao.yaml` tem 43 entradas, uma por critério do catálogo.
- [ ] Toda prova aponta um lugar verificável e o lugar existe.
- [ ] Todo `nao_avaliado` e `fora_do_contexto` tem `razao` que diz qual fonte faltou ou qual contexto não vale.
- [ ] Cada bloqueio e cada parcial traz ao menos uma via de recomendação (o script escolhe as vias pela evidência disponível; não recalcule).
- [ ] Nenhum texto seu (provas, observações, razões, mensagem de entrega) rotula o jogo como sociointeracionista, behaviorista ou outro rótulo teórico.

Entregue ao usuário:

1. Os caminhos de `avaliacao.yaml`, `relatorio.md` e `resultado.yaml` (e de `inventario.md` e dos registros de vídeo).
2. O nível alcançado como o script o imprimiu, sem reinterpretá-lo.
3. Os bloqueios e parciais, remetendo ao relatório.
4. A cláusula, literal: "O resultado de uma avaliação vygolint expressa conformidade com as diretrizes de Carvalho (2020) e não classifica o jogo como sociointeracionista."
