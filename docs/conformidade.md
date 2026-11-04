# Regras de conformidade do vygolint

> O resultado de uma avaliação vygolint expressa **conformidade com as diretrizes de
> Carvalho (2020)** e **não classifica o jogo como sociointeracionista**. Carvalho (2020,
> seção 4.4 e considerações finais) alerta que rotular o jogo e ordenar as diretrizes pode
> distorcer a teoria de Vigotski. Os níveis abaixo ordenam critérios de verificação, não
> a teoria.

## 1. Nível de cada critério

O nível é derivado de dois eixos declarados no catálogo, pela tabela:

| Essencialidade | Viabilidade alta ou média | Viabilidade baixa |
|---|---|---|
| alta | A | AA |
| média | AA | AAA |
| baixa | AAA | AAA |

Regra adicional: diretriz com `modalidade: pode` (D20, D21) nunca gera critério A; o
resultado A sobe para AA.

Definições:

- **Essencialidade alta:** o critério materializa um princípio sem o qual a mecânica é
  behaviorista (resolução de problemas, interação ativa com objetos, mediação por feedback
  orientador, atividade do jogador).
- **Essencialidade média:** socialização, mediação entre pares, autonomia de escolha,
  contextualização realista.
- **Essencialidade baixa:** criação de conteúdo pelo jogador, personalização adaptativa,
  recursos complementares.
- **Viabilidade alta:** implementável em qualquer jogo educacional com mecânicas comuns,
  baixo custo.
- **Viabilidade média:** exige sistema dedicado (persistência, comunicação assíncrona,
  perfil de desempenho).
- **Viabilidade baixa:** exige infraestrutura rara (multijogador síncrono, editor de
  conteúdo, adaptação em tempo real).

`scripts/build_catalog.py` recalcula o nível de todo critério e falha se o YAML declarar
outro.

## 2. Grau de cada critério

| Grau | Significado |
|---|---|
| atendido | todas as evidências observadas satisfazem o descritor "atendido" |
| parcial | evidências satisfazem só em parte; ver descritor "parcial" |
| não atendido | descritor "não atendido", ou dependência não satisfeita |

Regras:

- O avaliador registra, por fonte usada (código, documentação, vídeo), as provas: trecho,
  página, timestamp.
- Fontes em conflito: vale o pior grau, salvo justificativa escrita. Vídeo prevalece sobre
  documentação.
- Critério com `depende_de` não satisfeito recebe **não atendido** automaticamente.
  `depende_de` é lista de grupos: todos os grupos precisam ser satisfeitos; dentro de um
  grupo basta um critério atendido.
- Grupo de `depende_de` sem critério atendido: se ao menos um critério do grupo está **não avaliado** e nenhum está atendido, o dependente fica **não avaliado por dependência**; se todos os critérios do grupo estão não atendidos ou parciais, o dependente fica **não atendido por dependência**. A nota do relatório cita os critérios de cada grupo não satisfeito.
- Não existe "não se aplica" por ausência de recurso. Jogo sem multijogador não atende D06.
  `aplicabilidade` só restringe por contexto de uso (D22).
- Critério cuja `aplicabilidade` não é satisfeita no contexto declarado da avaliação (ex.: D22 quando o jogo não é aplicado em sala de aula) é registrado como **fora do contexto**, fica fora das exigências de nível e é listado no relatório com a razão. O contexto de uso é declarado no início da avaliação.
- Quando nenhuma fonte disponível permite avaliar um critério (por exemplo, só há vídeo e o vídeo não mostra o ponto avaliado), o relatório registra **não avaliado** com a razão; para fins de conformidade de nível, o critério conta como não atendido.

## 2a. Definições

Todo termo que decide o grau de um critério tem definição apontável. As compartilhadas
(missão, minijogo, desafio, cenário jogável, caminho obrigatório, situação-problema,
GDD ou documento equivalente, objetivo de aprendizagem, sessão de jogo) existem uma
vez em `catalog/definicoes.yaml` e aparecem no bloco **Definições** de cada critério que
as usa; as específicas de um critério ficam em `definicoes.locais`. O avaliador aplica
a definição impressa no critério, igual para código, documentação e vídeo. Uma palavra
marcada como "sentido corrente" não carrega a definição do glossário.

## 2b. Recomendações

Todo critério traz, no catálogo, uma recomendação por via (`documentacao`, `design`,
`codigo`): o que fazer para sair de não atendido ou parcial para atendido, nos termos dos
seus indicadores. A via é `null` quando não contribui para levar o critério a atendido. O relatório
reproduz o texto do catálogo e o contextualiza com os itens encontrados; não inventa
recomendação nova. As vias são complementares: `design` muda o projeto e `documentacao`
registra a mudança no GDD ou documento equivalente; o relatório apresenta as vias não nulas
que cabem à evidência disponível (seção 5).

## 3. Diretriz

Diretriz atendida no nível N quando todos os seus critérios de nível N ou inferior estão
**atendidos**. Parcial não conta.

## 4. Jogo

| Nível do jogo | Exigência |
|---|---|
| A | todos os critérios A atendidos |
| AA | A + todos os critérios AA atendidos |
| AAA | AA + todos os critérios AAA atendidos |
| sem conformidade | qualquer critério A não atendido ou parcial |

Critérios **fora do contexto** (seção 2) não entram nas exigências desta tabela.

## 5. Relatório

O relatório é gerado por `scripts/vygolint_report.py` a partir de `avaliacao.yaml` (seção 6); o avaliador não o edita.

Todo relatório contém, nesta ordem:

1. a cláusula do início deste documento;
2. o nível alcançado;
3. cobertura por nível: contagem de atendido, parcial, não atendido (dos quais N não avaliados) e
   fora do contexto, para A, AA e AAA;
4. cobertura por categoria: mesma contagem para cada uma das 12 categorias;
5. bloqueios: critérios que impedem o próximo nível, cada um com a `recomendacao` do catálogo
   na via que cabe à evidência disponível (código avaliado: `codigo`; só documentação:
   `documentacao` e `design`; só vídeo: `design` e `codigo`; documentação e vídeo: as três;
   via escolhida nula: as demais não nulas); bloqueio causado por dependência não satisfeita
   cita o critério de que depende, sem recomendação própria;
6. parciais: o que falta para pleno, com a `recomendacao` do critério contextualizada pelos
   itens que a avaliação encontrou fora do estado atendido;
7. provas por critério.

Critério que depende de um critério não avaliado é registrado como não avaliado por dependência e conta como não atendido para fins de nível.

## 6. Arquivos da avaliação

`avaliacao.yaml` é escrito pelo avaliador (agente ou humano), um por jogo:

- `jogo`, `avaliador`, `data` (AAAA-MM-DD);
- `contexto.sala_de_aula` (true/false: decide a aplicabilidade de D22), `contexto.fontes` (subconjunto de `codigo`, `documentacao`, `video`), `contexto.artefatos` (fonte → lista de caminhos);
- `criterios`: uma entrada por critério do catálogo (os 43), com `grau` (`atendido`, `parcial`, `nao_atendido`, `nao_avaliado`, `fora_do_contexto`), `fontes` (por fonte usada: `grau`, `provas`, `observacao` opcional), `razao` (obrigatória para `nao_avaliado` e `fora_do_contexto`) e `justificativa_conflito` (obrigatória quando `grau` difere do grau esperado pelas fontes).

Grau esperado pelas fontes: o pior entre as fontes usadas, ignorando a documentação quando há vídeo (vídeo prevalece sobre documentação). Fonte só pode ser usada se existe na `evidencia` do critério e em `contexto.fontes`. Prova: `arquivo:linha — trecho`, `documento p. N — trecho` ou `arquivo hh:mm:ss[-hh:mm:ss] — observação` (vídeo). `fontes` só existe em entradas com grau `atendido`, `parcial` ou `nao_atendido`; `nao_avaliado` e `fora_do_contexto` levam só `razao`.

`scripts/vygolint_report.py <pasta>/avaliacao.yaml` valida o arquivo contra o catálogo, aplica as seções 2 a 4 e escreve `relatorio.md` (seção 5), `relatorio.html` e `resultado.yaml` (grau efetivo e grau declarado por critério, nível alcançado), que serve à comparação com avaliação humana. O `relatorio.html` apresenta o mesmo conteúdo da seção 5 (cláusula, nível, coberturas, bloqueios com vias, parciais, provas) em página navegável, com leituras por público (professor, desenvolvimento, equipe) e uma tabela de fontes a entregar para decidir os critérios não avaliados; ele não acrescenta grau, nível nem recomendação fora do catálogo. Exemplo em `docs/exemplo/`.
