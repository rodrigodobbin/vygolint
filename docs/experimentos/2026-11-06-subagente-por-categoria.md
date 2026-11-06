# Experimento: um subagente por categoria

Data: 2026-11-06. Jogo: Corrida Antártica (vídeo de 1 min 55 s; sem código nem GDD). Catálogo: 43 critérios, 12 categorias. vygolint 0.2.0.

## Pergunta

A skill `vygolint-avaliar` dizia que o passo 3 podia ser dividido por categoria entre subagentes. Nunca tinha sido feito. O modo funciona? Os graus coincidem com os da avaliação em sequência?

## Como foi feito

- Avaliação de referência: os 43 critérios graduados em sequência, em um só contexto, a partir de `registro_video.yaml`, `registro_audio_file.yaml` e `inventario.md`.
- Teste: 12 subagentes, um por categoria, em paralelo, mesmo modelo, sem acesso à avaliação de referência nem às partes uns dos outros. Cada um recebeu a lista de ids, o caminho da skill `vygolint-criterio` e do catálogo, o contexto, os mesmos registros e inventário, e a pasta de quadros. Cada um gravou um arquivo YAML com as entradas da categoria.
- As 12 partes foram juntadas no esqueleto de `avaliacao.yaml` e passaram por `vygolint_report.py --strict`.

## Resultado

| Medida | Valor |
|---|---|
| Partes com YAML válido e exatamente os ids pedidos | 12 de 12 |
| Avisos do lint de provas na avaliação juntada | 0 |
| Graus declarados iguais aos da referência | 32 de 43 |
| Iguais quando só importa atendido contra não atendido | 41 de 43 |
| Nível do jogo | o mesmo nas duas (sem conformidade) |
| Tokens somados dos 12 subagentes | cerca de 1,2 milhão |
| Tempo de relógio (o subagente mais lento) | 4 min 20 s |
| Custo do subagente de um só critério | 77 a 110 mil tokens |

As 11 divergências:

| Tipo | Critérios | Referência | Subagente |
|---|---|---|---|
| Fronteira entre não avaliado e não atendido | D07.1, D16.1, D24.1, D25.1, D26.1, D27.1, D29.1 | não avaliado | não atendido |
| Fronteira, no sentido inverso | D02.1 | não atendido | não avaliado |
| Leitura do critério | D03.3 | não avaliado | atendido |
| Leitura do critério | D19.1 | não atendido | atendido |
| Leitura do critério | D30.1 | parcial | não atendido |

## O que o teste mostrou

1. **A mecânica funciona.** Entregar caminhos e pedir um arquivo por parte bastou. Nenhuma parte veio malformada.
2. **A fronteira entre "não avaliado" e "não atendido" não estava decidida.** Oito das onze divergências são dela, e os subagentes divergiram também entre si: um usou não avaliado em D20.1, D21.1 e D23.1 e não atendido em D16.1; outros usaram não atendido em casos do mesmo tipo. Os argumentos a favor de não atendido foram a gravação cobrir o jogo inteiro e a regra de desempate "sem código nem GDD, vale o vídeo". Para o nível não muda nada, porque os dois contam como não atendido; muda o que o relatório afirma.
3. **Subagentes reobservam o vídeo e chegam a fatos diferentes.** Dois descreveram, a partir das folhas a 1 quadro por segundo, uma barra que crescia a cada segundo sem contato com alimento. Um terceiro mediu a barra a 15 quadros por segundo e viu que ela só sobe em degraus, a cada item coletado. A medição quadro a quadro feita depois confirmou o terceiro: 15 subidas em jogo, todas em degrau, nenhuma contínua. A avaliação juntada tinha provas que se contradiziam, e o registro de referência estava vago nesse ponto.
4. **As dúvidas relatadas apontam os critérios certos.** As três divergências de leitura (D03.3, D19.1, D30.1) tinham sido marcadas pelo próprio subagente como o juízo menos seguro da parte.
5. **Dois juízos discutíveis da referência foram repetidos às cegas.** D01.1 e D08.1 saíram atendido nas duas avaliações.
6. **O custo fixo por subagente é alto.** Ler a skill, as regras e os registros custa dezenas de milhares de tokens antes do primeiro critério. Seis das doze categorias têm um único critério.

## O que mudou na ferramenta

- `vygolint-criterio`, seção 3, item 5: regra explícita para a fronteira. Sem evidência, o grau é não avaliado, salvo quando o próprio critério traz grau por falta de evidência; cobertura da gravação e regra de desempate não são exceção.
- `vygolint-avaliar`: o parágrafo sobre subagentes virou uma seção com o que entregar, o agrupamento de categorias pequenas, o relato de achados, a junção por script e a revisão do conjunto.
- `scripts/vygolint_juntar.py`: junta as partes no esqueleto, conferindo ids contra o catálogo.

## Limites

Um jogo, uma gravação, só a fonte vídeo, um modelo, uma execução. Não mede variação entre execuções do mesmo subagente nem o efeito de agrupar categorias, que foi recomendado pelo custo observado e não testado. A referência não é gabarito: foi feita pelo mesmo modelo, e as três divergências de leitura pedem revisão humana.
