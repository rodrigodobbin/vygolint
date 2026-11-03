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
- Não existe "não se aplica" por ausência de recurso. Jogo sem multijogador não atende D06.
  `aplicabilidade` só restringe por contexto de uso (D22).
- Critério cuja `aplicabilidade` não é satisfeita no contexto declarado da avaliação (ex.: D22 quando o jogo não é aplicado em sala de aula) é registrado como **fora do contexto**, fica fora das exigências de nível e é listado no relatório com a razão. O contexto de uso é declarado no início da avaliação.
- Quando nenhuma fonte disponível permite avaliar um critério (por exemplo, só há vídeo e o vídeo não mostra o ponto avaliado), o relatório registra **não avaliado** com a razão; para fins de conformidade de nível, o critério conta como não atendido.

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

Todo relatório contém, nesta ordem:

1. a cláusula do início deste documento;
2. o nível alcançado;
3. cobertura por nível: contagem de atendido, parcial, não atendido (dos quais N não avaliados) e
   fora do contexto, para A, AA e AAA;
4. cobertura por categoria: mesma contagem para cada uma das 12 categorias;
5. bloqueios: critérios que impedem o próximo nível, com recomendação;
6. parciais: o que falta para pleno;
7. provas por critério.

Critério que depende de um critério não avaliado é registrado como não avaliado por dependência e conta como não atendido para fins de nível.
