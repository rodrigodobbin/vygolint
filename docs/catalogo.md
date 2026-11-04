<!-- ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão. -->
# Catálogo vygolint — diretrizes e critérios de conformidade

Fonte das diretrizes: CARVALHO, Diego Marques. *Diretrizes para o desenvolvimento de jogos educacionais digitais embasados na teoria sociointeracionista de Lev Semionovich Vigotski*. Dissertação (Mestrado), UFABC, 2020. Quadro 3.

> Carvalho (2020, seção 4.4) suprimiu as categorias na apresentação final das diretrizes por considerar que rotular, classificar e ordenar requisitos pode gerar a falsa impressão de que a teoria de Vigotski também pode ser classificada assim. O vygolint usa as categorias apenas como instrumento de organização e de relatório, não como taxonomia da teoria.

## Glossário

Definições compartilhadas, referenciadas pelos critérios em `definicoes.glossario`.

- **missão** (âncora D28; gatilhos: missão, missões): uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- **minijogo** (âncora D37; gatilhos: minijogo): uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- **desafio** (âncora D19; gatilhos: desafio): cada missão ou minijogo
- **cenário jogável** (âncora D29; gatilhos: cenário): cada espaço do jogo (mapa, sala ou fase) em que o jogador executa ações e em que há uma missão em curso; cenário em que nenhuma missão está em curso (hub, sandbox) não tem caminho obrigatório e não é cenário jogável
- **caminho obrigatório (caminho da missão)** (âncora D05; gatilhos: caminho obrigatório, caminho da missão): a sequência de objetivos exigidos para completar a missão em curso, e fora do caminho obrigatório é tudo o que nenhum desses objetivos exige
- **situação-problema** (âncora D01; gatilhos: situação-problema): uma situação com estado inicial, objetivo e mais de uma ação possível, cuja resolução exige uma decisão do jogador, e não apenas a repetição de uma mesma ação; escolher entre alternativas prontas, sem estado inicial a ser transformado pelas ações do jogador, não conta como situação-problema
- **GDD ou documento equivalente** (âncora D22 (texto novo); gatilhos: GDD, documento equivalente): o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- **objetivo de aprendizagem** (âncora D31; gatilhos: objetivo de aprendizagem, objetivos de aprendizagem): cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados
- **sessão de jogo** (âncora D36 (texto novo); gatilhos: sessão de jogo): o período contínuo entre o jogador iniciar o jogo, ou carregar um estado salvo, e encerrá-lo (fechar o jogo ou voltar ao menu inicial)

## Resumo

| ID | Categoria | Diretriz | Critérios |
|---|---|---|---|
| D01 | Interação | Os desafios do jogo devem ser direcionados a resolução de problemas | D01.1 (A) |
| D02 | Interação | Avaliar os conteúdos ensinados no jogo de forma a transcender o contexto que eles foram abordados, possibilitando a transposição dos conceitos para resolução de outras situações-problema | D02.1 (A) |
| D03 | Interação | O desenvolvimento das atividades/missões/minijogos deve ser autorregulado pelo jogador | D03.1 (A), D03.2 (A), D03.3 (A) |
| D04 | Interação | O jogador deve interagir com os objetos dos cenários | D04.1 (A) |
| D05 | Interação | O jogador deve explorar livremente o cenário | D05.1 (A) |
| D06 | Interação | O jogador deve trocar informações com outros jogadores por comunicação síncrona | D06.1 (AAA) |
| D07 | Interação | O jogador deve trocar informações com outros jogadores por meio de comunicação assíncrona | D07.1 (AA) |
| D08 | Interação | O jogador deve trocar informações com os mecanismos do jogo | D08.1 (A) |
| D09 | Interação | O jogador deve se comunicar por linguagem escrita | D09.1 (AA) |
| D10 | Interação | O jogo deve viabilizar o comportamento ativo do jogador | D10.1 (A) |
| D11 | Interação | O jogador deve coletar informações | D11.1 (A) |
| D12 | Interação | O jogo deve fornecer mecanismos para o jogador construir coisas | D12.1 (AAA) |
| D13 | Interação | O jogo permite o desenvolvimento de tarefas e missões em grupo | D13.1 (AAA) |
| D14 | Interação | O jogador deve conseguir inserir comentários no jogo que ficarão disponíveis para outros jogadores | D14.1 (AA) |
| D15 | Interação | O jogo deve estimular a interação entre jogadores por diversas ferramentas de comunicação | D15.1 (AAA) |
| D16 | Mediação | O jogo deve fornecer meios do jogador solicitar ajuda de outros jogadores | D16.1 (AA) |
| D17 | Mediação | O jogo deve exibir feedback construtivo para as ações do jogador | D17.1 (A) |
| D18 | Mediação | O jogo deve exibir feedback individualizado para as ações do jogador | D18.1 (A) |
| D19 | Mediação | Os desafios devem proporcionar o desenvolvimento de competências no uso das ferramentas mentais | D19.1 (A) |
| D20 | Mediação | O jogo pode fornecer pista para o jogador resolver problemas | D20.1 (AA) |
| D21 | Mediação | O jogo pode fornecer simulações de formas para resolver o problema | D21.1 (AA) |
| D22 | Mediação | O jogo, quando aplicado em sala de aula, cria oportunidades para o professor atuar como mediador / facilitador | D22.1 (AA), D22.2 (AAA) |
| D23 | Mediação | A narrativa do jogo deve viabilizar reflexões críticas ao trabalhar os conteúdos | D23.1 (A) |
| D24 | Autonomia | O jogador decide quais recursos utilizar | D24.1 (A) |
| D25 | Autonomia | O jogador decide, com base em seus interesses e motivações, qual conteúdo explorar | D25.1 (AA) |
| D26 | Socialização | O jogo deve aproximar os jogadores pela competição | D26.1 (AAA) |
| D27 | Socialização | O jogo deve aproximar os jogadores pela colaboração | D27.1 (AAA) |
| D28 | Lúdico | A proposta de narrativa deve despertar a curiosidade | D28.1 (AA) |
| D29 | Lúdico | O jogo deve fornecer desafios motivadores, que estimulem o jogador a explorar | D29.1 (A) |
| D30 | Realismo | O jogo deve colocar o jogador em uma situação realística | D30.1 (AA) |
| D31 | Realismo | O jogo contextualiza o conteúdo com situações reais | D31.1 (A) |
| D32 | Realismo | O jogo deve ter objetos do cotidiano com os quais o jogador pode se familiarizar | D32.1 (AA) |
| D33 | Personalização | Os desafios devem ser personalizados de acordo com o desempenho do jogador | D33.1 (AAA) |
| D34 | Personalização | Os desafios devem ser personalizados de acordo com as ações do jogador | D34.1 (AAA) |
| D35 | Personalização | O jogo deve permitir que o jogador crie desafios para outros jogadores | D35.1 (AAA) |
| D36 | Organização | O jogador deve organizar informações | D36.1 (A) |
| D37 | Resolução de problemas | O jogo, suas missões e mini jogos devem apresentar a situação-problema ao jogador de maneira explícita | D37.1 (A) |
| D38 | Linguagem | O jogo deve fornecer informações escritas ao jogador | D38.1 (A) |
| D39 | Atenção | O mundo do jogo deve exigir do jogador a percepção de detalhes | D39.1 (AA) |
| D40 | Aprendizado | O jogo deve viabilizar o aprendizado também pelos erros do jogador com mensagens textuais, sons e animações | D40.1 (A) |

## Diretrizes

### D01 — Os desafios do jogo devem ser direcionados a resolução de problemas

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D01.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *situação-problema*: uma situação com estado inicial, objetivo e mais de uma ação possível, cuja resolução exige uma decisão do jogador, e não apenas a repetição de uma mesma ação; escolher entre alternativas prontas, sem estado inicial a ser transformado pelas ações do jogador, não conta como situação-problema
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta

**Enunciado.** Cada missão ou minijogo apresenta uma situação-problema cuja resolução exige uma decisão do jogador, e não apenas a repetição de uma mesma ação

**Justificativa do nível.** essencialidade alta, viabilidade alta. Para Vigotski a aprendizagem nasce da atividade do sujeito sobre um problema, e o conhecimento é construído quando o jogador precisa operar com os conceitos, não quando os reproduz. Em um desafio de repetição mecânica o jogador executa a mesma ação sem escolher entre alternativas, de modo que a atividade não exige operar com o conteúdo. Estruturar desafios como situações-problema é uma decisão de projeto, sem custo técnico adicional.

**Evidência.**
- Código: não se aplica
- Documentação: Listar no documento de design (GDD) ou documento equivalente cada missão e minijogo e identificar a situação-problema (estado inicial, objetivo e ações possíveis) e as decisões previstas
  - cada missão ou minijogo descreve uma situação-problema
  - a resolução descrita exige uma decisão do jogador e não se reduz a repetir uma mesma ação nem a escolher entre alternativas prontas, sem estado inicial a ser transformado pelas ações do jogador
- Vídeo: Registrar o início e o fim de cada missão ou minijogo observado, anotar o estado inicial, o objetivo e as ações disponíveis ao jogador e anotar qual decisão ele tomou para concluí-lo
  - todas as missões e minijogos presentes no vídeo foram registrados (mínimo 1)
  - cada um apresenta uma situação-problema, com estado inicial visível, objetivo e mais de uma ação disponível ao jogador
  - o jogador resolve a situação por ações que transformam o estado inicial, e não apenas escolhendo entre alternativas prontas
  - concluir o desafio não depende de repetir a mesma ação até o fim

**Escala.**
- Atendido: Todas as missões e minijogos observados ou documentados apresentam uma situação-problema, nos termos do enunciado e das definições, cuja resolução exige uma decisão do jogador
- Parcial: Ao menos uma missão ou minijogo apresenta uma situação-problema, nos termos do enunciado e das definições, e ao menos outra não apresenta, por se resolver repetindo uma ação ou escolhendo entre alternativas prontas sem estado inicial a ser transformado
- Não atendido: Nenhuma missão ou minijogo apresenta uma situação-problema, nos termos do enunciado e das definições

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente, para cada missão e minijogo, a situação-problema com estado inicial, objetivo e ações possíveis. Registrar também a decisão do jogador que a resolução exige
- Design: Converter cada missão ou minijogo que se resolve repetindo uma ação ou escolhendo entre alternativas prontas em situação-problema, com estado inicial a ser transformado pelas ações do jogador, objetivo e mais de uma ação disponível. Condicionar a conclusão a uma decisão do jogador entre essas ações
- Código: não se aplica

**Depende de.** —

### D02 — Avaliar os conteúdos ensinados no jogo de forma a transcender o contexto que eles foram abordados, possibilitando a transposição dos conceitos para resolução de outras situações-problema

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D02.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *objetivo de aprendizagem*: cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados
- *cenário* (sentido corrente): lugar ou situação do jogo em que o conceito é introduzido ou cobrado («missão ou cenário», «aparência do cenário»), e não o cenário jogável

**Enunciado.** Cada conceito listado como objetivo de aprendizagem no GDD ou documento equivalente é cobrado ao menos uma vez em uma missão ou cenário com estrutura de problema diferente daquela em que foi introduzido

**Justificativa do nível.** essencialidade alta, viabilidade média. Em Vigotski, conceitos científicos se consolidam quando o sujeito os generaliza e os usa de modo consciente em situações novas, e não quando os repete no contexto de origem. Avaliar apenas na situação de introdução mede memorização do contexto, não domínio do conceito. Exige planejar variações de situação para cada conteúdo, o que aumenta o esforço de conteúdo e de design; viabilidade média.

**Evidência.**
- Código: não se aplica
- Documentação: Extrair do GDD ou documento equivalente a lista de objetivos de aprendizagem e mapear, para cada conceito, a missão ou cenário de introdução e as missões ou cenários em que ele é cobrado. Se o documento não lista objetivos de aprendizagem, registrar a ausência e classificar o critério como nao_atendido. Considerar estrutura de problema diferente quando mudam o objetivo da missão ou o conjunto de objetos ou dados que o jogador manipula; mudar apenas o mapa ou a aparência do cenário não conta
  - tabela ou lista associando cada conceito do GDD ou documento equivalente, a missão ou cenário de introdução e a missão ou cenário de avaliação
  - para cada conceito, a missão de avaliação tem objetivo ou conjunto de objetos ou dados manipulados diferente do da missão de introdução
- Vídeo: Para cada conceito listado no GDD ou documento equivalente, registrar a missão e o momento em que ele é introduzido e a missão em que o mesmo conceito é cobrado depois, comparando o objetivo e os objetos manipulados nas duas
  - o conceito aparece em duas missões ou cenários diferentes
  - o desafio da segunda missão só se resolve aplicando o conceito apresentado na primeira e tem objetivo ou objetos manipulados diferentes

**Escala.**
- Atendido: Todos os conceitos listados como objetivo de aprendizagem no GDD ou documento equivalente são cobrados ao menos uma vez em missão ou cenário com estrutura de problema diferente da de introdução
- Parcial: Ao menos um conceito listado é cobrado em missão ou cenário com estrutura de problema diferente da de introdução, e ao menos outro conceito listado não é cobrado fora da situação em que foi apresentado (inclui o conceito que não é cobrado em nenhuma missão ou cenário)
- Não atendido: Nenhum conceito listado é cobrado fora da situação em que foi introduzido (inclui o conceito que não é cobrado em nenhuma missão ou cenário), ou o GDD ou documento equivalente não lista objetivos de aprendizagem

**Recomendações.**
- Documentação: Listar no GDD ou documento equivalente os objetivos de aprendizagem. Registrar, para cada conceito listado, a missão ou cenário de introdução e a missão ou cenário de avaliação, com o objetivo e os objetos ou dados manipulados em cada uma
- Design: Incluir, para cada conceito listado como objetivo de aprendizagem que não é cobrado fora da situação de introdução, ao menos uma missão ou cenário em que ele seja cobrado com objetivo ou conjunto de objetos ou dados manipulados diferente do da introdução
- Código: não se aplica

**Depende de.** —

### D03 — O desenvolvimento das atividades/missões/minijogos deve ser autorregulado pelo jogador

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D03.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *cenário* (sentido corrente): ambiente do jogo em que as atividades aparecem disponíveis («menu, mapa ou cenário»), o que inclui hub sem missão em curso, e não o cenário jogável

**Enunciado.** Em ao menos um ponto do jogo, o jogador pode escolher entre duas ou mais atividades, missões ou minijogos disponíveis ao mesmo tempo e iniciar a escolhida

**Justificativa do nível.** essencialidade alta, viabilidade média. Em Vigotski, a autorregulação é o movimento em que o controle da própria ação passa do outro para o aprendiz, e decidir o que fazer a seguir é parte desse controle. Num jogo estritamente linear a ordem é decidida pelo sistema, e o jogador apenas executa a sequência. Oferecer atividades em paralelo exige estrutura de progressão não linear e conteúdo que não dependa de uma ordem fixa; viabilidade média.

**Evidência.**
- Código: Localizar a lógica de desbloqueio de missões e minijogos e verificar se há algum estado do jogo em que duas ou mais atividades estão desbloqueadas ao mesmo tempo e selecionáveis. Verificar também, dentro de cada atividade, se o código aceita mais de uma ordem para executar as ações (objetos, perguntas ou etapas)
  - existe estado do jogo em que duas ou mais atividades estão desbloqueadas simultaneamente
  - a atividade iniciada é determinada por entrada do jogador (menu, mapa, interação), não por ordem fixa no código
  - dentro de ao menos uma atividade, o código aceita mais de uma ordem para executar as ações (objetos, perguntas ou etapas), sem impor sequência fixa
- Documentação: não se aplica
- Vídeo: Registrar os pontos em que o jogo oferece atividades e anotar quantas estão disponíveis e qual o jogador inicia. Registrar também, dentro de cada atividade, se a interface apresenta duas ou mais ações (objetos, perguntas ou etapas) disponíveis ao mesmo tempo e em que ordem o jogador as executa
  - ao menos um ponto em que duas ou mais atividades aparecem disponíveis ao mesmo tempo (menu, mapa ou cenário)
  - o jogador inicia uma delas; a outra pode permanecer disponível, ser iniciada depois ou ficar indisponível após a escolha (escolha excludente)
  - dentro de ao menos uma atividade, a interface apresenta duas ou mais ações (objetos, perguntas ou etapas) disponíveis ao mesmo tempo e o jogador escolhe a ordem de execução

**Escala.**
- Atendido: Em ao menos um ponto, o jogador escolhe entre duas ou mais atividades, missões ou minijogos disponíveis ao mesmo tempo
- Parcial: O jogador não escolhe entre atividades, missões ou minijogos, mas escolhe a ordem das ações dentro de uma atividade (como objetos, perguntas ou etapas)
- Não atendido: As atividades, missões e minijogos se sucedem numa única ordem definida pelo jogo, e dentro de cada uma a ordem das ações também é fixa

**Recomendações.**
- Documentação: não se aplica
- Design: Definir ao menos um ponto do jogo em que duas ou mais atividades, missões ou minijogos fiquem disponíveis ao mesmo tempo e o jogador escolha qual iniciar
- Código: Alterar a lógica de desbloqueio para que exista um estado do jogo com duas ou mais atividades desbloqueadas ao mesmo tempo. Determinar a atividade iniciada pela entrada do jogador (menu, mapa ou interação), e não por ordem fixa no código

**Depende de.** —

#### D03.2 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela

**Enunciado.** O jogador inicia cada atividade, missão ou minijogo por uma ação própria e o jogo não avança de uma para a próxima sem essa ação

**Justificativa do nível.** essencialidade alta, viabilidade alta. Atividade, em Vigotski, é conduzida pelo sujeito; a autorregulação inclui decidir o momento de passar de uma etapa à seguinte. Se o jogo encadeia as etapas sozinho, o controle da transição permanece no sistema. Basta condicionar a transição a uma ação do jogador, o que não exige recurso técnico especial.

**Evidência.**
- Código: Localizar as transições entre missões e minijogos e verificar o que as dispara
  - a transição é disparada por entrada do jogador (botão, escolha, interação)
  - não há transição disparada apenas por temporizador ou por término automático da etapa anterior
- Documentação: não se aplica
- Vídeo: Registrar cada transição entre atividades e anotar se houve ação do jogador antes da mudança
  - todas as transições presentes no vídeo foram registradas (mínimo 1)
  - cada transição é precedida por ação do jogador

**Escala.**
- Atendido: Todas as transições observadas ou identificadas no código dependem de ação do jogador
- Parcial: Ao menos uma transição depende de ação do jogador e ao menos outra ocorre automaticamente
- Não atendido: As atividades se sucedem automaticamente, sem ação do jogador

**Recomendações.**
- Documentação: não se aplica
- Design: Prever, ao fim de cada atividade, missão ou minijogo, uma ação do jogador que dispare a passagem para a seguinte
- Código: Substituir cada transição disparada por temporizador ou por término automático da etapa anterior por uma transição disparada por entrada do jogador (botão, escolha ou interação)

**Depende de.** —

#### D03.3 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *limite obrigatório*: um temporizador cujo esgotamento encerra ou reprova a atividade

**Enunciado.** Nenhuma atividade tem limite de tempo obrigatório para ser concluída, ou o limite pode ser desativado ou ampliado pelo jogador

**Justificativa do nível.** essencialidade alta, viabilidade alta. Em Vigotski, a mediação precisa responder ao ritmo com que o aprendiz elabora a tarefa, e esse ritmo não é conhecido de antemão pelo jogo. Um temporizador obrigatório impõe a todos o mesmo ritmo e leva o jogador a responder antes de elaborar. Remover o limite ou torná-lo opcional é de baixo custo.

**Evidência.**
- Código: Procurar temporizadores associados a missões e minijogos e verificar o que ocorre quando o tempo se esgota e se há opção de desativá-los
  - existência de temporizador com consequência de falha ao esgotar
  - existência de configuração que desativa ou amplia o temporizador
- Documentação: Verificar no GDD as regras de tempo de cada atividade
  - indicação de quais atividades têm limite de tempo
  - indicação de opção do jogador para alterar o limite
- Vídeo: Observar cada atividade registrando se há contador de tempo visível, o que ocorre quando ele chega a zero e se o jogador pode permanecer na atividade sem limite
  - todas as atividades presentes no vídeo foram observadas (mínimo 1)
  - o jogador permanece na atividade sem ser interrompido por esgotamento de tempo
  - não há contador de tempo visível cujo esgotamento encerre ou reprove a atividade; se há contador visível e o vídeo mostra seu esgotamento, a atividade não termina nem falha

**Escala.**
- Atendido: Nenhuma atividade tem limite de tempo obrigatório, ou o jogador pode desativar ou ampliar o limite
- Parcial: Ao menos uma atividade tem limite de tempo obrigatório e ao menos outra não tem
- Não atendido: Todas as atividades têm limite de tempo obrigatório que o jogador não pode alterar

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente as regras de tempo de cada atividade, indicando quais têm limite de tempo. Registrar, para cada atividade com limite, a opção do jogador que o desativa ou amplia
- Design: Retirar o limite de tempo obrigatório de cada atividade que o tem, ou prever uma opção do jogador que o desative ou amplie
- Código: Remover a consequência de falha de cada temporizador de atividade, ou acrescentar uma configuração do jogador que o desative ou amplie

**Depende de.** —

### D04 — O jogador deve interagir com os objetos dos cenários

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D04.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *cenário jogável*: cada espaço do jogo (mapa, sala ou fase) em que o jogador executa ações e em que há uma missão em curso; cenário em que nenhuma missão está em curso (hub, sandbox) não tem caminho obrigatório e não é cenário jogável
- *caminho obrigatório (caminho da missão)*: a sequência de objetivos exigidos para completar a missão em curso, e fora do caminho obrigatório é tudo o que nenhum desses objetivos exige
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *objetivo de aprendizagem*: cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados

**Enunciado.** Ao menos um objeto de cada cenário responde à interação do jogador com mudança de estado ou informação que se relaciona a um objetivo de aprendizagem listado no GDD (ou documento equivalente)

**Justificativa do nível.** essencialidade alta, viabilidade alta. Para Vigotski o conhecimento é construído na atividade sobre objetos e instrumentos, e interagir com o ambiente é a forma pela qual o jogador exerce essa atividade. Um cenário apenas contemplativo reduz o jogador a espectador, e um objeto que responde sem relação com o conteúdo mantém a interação fora da atividade de aprender. Programar resposta a clique, toque ou colisão é recurso básico de qualquer motor de jogo.

**Evidência.**
- Código: Listar os objetos de cada cenário que têm manipulador de evento (handler) de interação (clique, toque, colisão, uso de item) e o efeito de cada manipulador, e comparar o efeito com os objetivos de aprendizagem do GDD. Considerar que o efeito se relaciona a um objetivo quando a informação exibida ou o novo estado enuncia, exemplifica ou testa um conceito listado, ou é dado necessário para resolver um desafio ligado a ele
  - cada cenário tem ao menos um objeto com manipulador de evento de interação
  - o efeito do manipulador é mudança de estado ou exibição de informação que se relaciona a um objetivo de aprendizagem do GDD
- Documentação: não se aplica
- Vídeo: Percorrer cada cenário observado registrando os objetos com os quais o jogador interage e a resposta obtida, e comparar a resposta com os objetivos de aprendizagem do GDD. Considerar que a resposta se relaciona a um objetivo quando a informação exibida ou o novo estado enuncia, exemplifica ou testa um conceito listado, ou é dado necessário para resolver um desafio ligado a ele
  - ao menos um objeto interagido por cenário
  - o objeto muda de estado ou exibe informação que se relaciona a um objetivo de aprendizagem do GDD

**Escala.**
- Atendido: Todos os cenários têm ao menos um objeto que responde à interação com mudança de estado ou informação que se relaciona a um objetivo de aprendizagem do GDD
- Parcial: Ao menos um cenário tem objeto que responde nesse sentido e ao menos outro cenário não tem
- Não atendido: Nenhum cenário tem objeto que responda à interação do jogador com mudança de estado ou informação que se relaciona a um objetivo de aprendizagem do GDD

**Recomendações.**
- Documentação: não se aplica
- Design: Definir, para cada cenário, ao menos um objeto que responda à interação do jogador com mudança de estado ou informação que enuncie, exemplifique ou teste um objetivo de aprendizagem do GDD, ou que seja dado necessário para resolver um desafio ligado a ele
- Código: Acrescentar, em cada cenário, ao menos um objeto com manipulador de evento (handler) de interação (clique, toque, colisão ou uso de item). Fazer o manipulador mudar o estado do objeto ou exibir informação que enuncie, exemplifique ou teste um objetivo de aprendizagem do GDD, ou que seja dado necessário para resolver um desafio ligado a ele

**Depende de.** —

### D05 — O jogador deve explorar livremente o cenário

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D05.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *cenário jogável*: cada espaço do jogo (mapa, sala ou fase) em que o jogador executa ações e em que há uma missão em curso; cenário em que nenhuma missão está em curso (hub, sandbox) não tem caminho obrigatório e não é cenário jogável
- *caminho obrigatório (caminho da missão)*: a sequência de objetivos exigidos para completar a missão em curso, e fora do caminho obrigatório é tudo o que nenhum desses objetivos exige
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta

**Enunciado.** Em todos os cenários jogáveis, o jogador alcança áreas ou objetos que não pertencem ao caminho da missão em curso, sem que o jogo o impeça ou o conduza de volta ao objetivo

**Justificativa do nível.** essencialidade alta, viabilidade média. Em Vigotski o conhecimento se constrói na atividade do sujeito sobre o meio, e é o jogador quem decide o que investigar. Um cenário reduzido ao caminho da missão limita essa atividade ao que o jogo prescreve e converte a exploração em seguimento de instruções. Construir áreas além do caminho principal acrescenta trabalho de arte e de nível; viabilidade média.

**Evidência.**
- Código: Localizar, em cada cenário jogável, os acessos a áreas ou objetos que nenhum objetivo da missão exige (portas, colisores, gatilhos, verificações do estado da missão) e verificar se alguma condição impede o acesso, interrompe o jogador ou o reposiciona no caminho da missão
  - existem áreas ou objetos fora do caminho da missão com acesso ou interação ativos
  - nenhuma verificação do estado da missão bloqueia o acesso a essas áreas ou objetos
  - nenhuma lógica interrompe o jogador ou o reposiciona no caminho da missão quando ele se afasta dele
- Documentação: Identificar no GDD ou nos mapas de nível, para cada cenário, os objetivos que compõem o caminho da missão e as áreas ou objetos que nenhum desses objetivos exige
  - o GDD ou mapa descreve áreas ou objetos acessíveis fora do caminho da missão
  - o GDD descreve o deslocamento do jogador até essas áreas durante a missão
  - o GDD descreve essas áreas ou objetos como acessíveis em qualquer estado da missão e descreve que o jogador pode sair do caminho e voltar a ele sem ser interrompido nem reposicionado
- Vídeo: Nos momentos em que o jogador deixa o caminho da missão, registrar o que o jogo faz em seguida. O vídeo só confirma a evidência de código ou documentação: a ausência de saída do caminho no vídeo não é evidência de restrição nem de liberdade, e interrupção, bloqueio ou reposicionamento observados valem como evidência de restrição
  - em cada saída do caminho da missão registrada no vídeo (mínimo 0), o jogo não interrompe, bloqueia nem reposiciona o jogador

**Escala.**
- Atendido: Todos os cenários jogáveis têm áreas ou objetos fora do caminho da missão acessíveis sem bloqueio
- Parcial: Ao menos um cenário tem áreas ou objetos acessíveis fora do caminho da missão e ao menos outro cenário restringe o jogador ao caminho
- Não atendido: Nenhum cenário permite alcançar áreas ou objetos fora do caminho da missão em curso

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente, para cada cenário jogável, os objetivos que compõem o caminho da missão e as áreas ou objetos que nenhum desses objetivos exige. Descrever o deslocamento do jogador até essas áreas durante a missão. Registrar que essas áreas ou objetos são acessíveis em qualquer estado da missão e que o jogador sai do caminho e volta a ele sem ser interrompido nem reposicionado
- Design: Incluir, em cada cenário jogável que restringe o jogador ao caminho da missão, áreas ou objetos que nenhum objetivo da missão exige. Permitir o acesso a essas áreas ou objetos em qualquer estado da missão, sem interromper nem reposicionar o jogador
- Código: Ativar o acesso ou a interação das áreas ou objetos fora do caminho da missão. Remover as verificações do estado da missão que bloqueiam esse acesso. Remover a lógica que interrompe o jogador ou o reposiciona no caminho da missão quando ele se afasta dele

**Depende de.** —

### D06 — O jogador deve trocar informações com outros jogadores por comunicação síncrona

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D06.1 — Nível AAA

**Definições.**

- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta

**Enunciado.** Durante a sessão, o jogador envia e recebe mensagens de texto ou voz de outros jogadores em tempo real

**Justificativa do nível.** essencialidade média, viabilidade baixa. Socialização entre pares é constitutiva do sociointeracionismo, mas a interação social também pode ocorrer de forma assíncrona (D07) ou fora do jogo (D22); por isso essencialidade média. Comunicação síncrona exige infraestrutura de rede e sessão multijogador, rara em jogos educacionais; viabilidade baixa.

**Evidência.**
- Código: Procurar módulo de rede, chat ou voz e verificar se envia e recebe mensagens entre clientes durante a partida
  - existe canal de mensagens entre jogadores conectados
  - mensagens chegam sem exigir fim da sessão
- Documentação: Verificar no GDD a seção de multijogador ou comunicação
  - especificação de chat, voz ou mensagens em tempo real
- Vídeo: Observar sessão com dois ou mais jogadores e registrar trocas de mensagens
  - ao menos uma troca de mensagem com resposta na mesma sessão

**Escala.**
- Atendido: Canal síncrono existe e o vídeo mostra troca de mensagens livres entre jogadores
- Parcial: Canal existe, mas limitado a mensagens prontas, emotes ou sinais sem conteúdo livre
- Não atendido: Não há comunicação entre jogadores durante a sessão

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente o canal de chat, voz ou mensagens em tempo real entre jogadores e o conteúdo livre que ele transmite
- Design: Prever uma sessão com dois ou mais jogadores e um canal em que eles troquem mensagens de texto ou voz em tempo real. Permitir no canal mensagens de conteúdo livre, e não apenas mensagens prontas, emotes ou sinais
- Código: Implementar um canal de mensagens de texto ou voz entre clientes conectados que entregue as mensagens durante a partida. Aceitar no canal conteúdo digitado ou falado pelo jogador, e não apenas mensagens prontas, emotes ou sinais

**Depende de.** —

### D07 — O jogador deve trocar informações com outros jogadores por meio de comunicação assíncrona

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D07.1 — Nível AA

**Definições.**

- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta

**Enunciado.** O jogo persiste mensagens ou registros deixados por um jogador e os exibe a outros jogadores em sessões posteriores

**Justificativa do nível.** essencialidade média, viabilidade média. Mesma base de D06: socialização entre pares. A forma assíncrona exige apenas persistência de dados e um ponto de leitura no jogo, viável sem sessão multijogador simultânea.

**Evidência.**
- Código: Procurar persistência de mensagens, comentários ou registros de jogador e o ponto onde outros jogadores os leem
  - escrita de mensagem associada a jogador e contexto
  - leitura de mensagens de outros jogadores em sessão distinta
- Documentação: Verificar no GDD mecânicas de mural, bilhetes, diário compartilhado ou similar
  - mecânica descrita com autor, local e leitor da mensagem
- Vídeo: Observar se o jogador encontra registros deixados por outro jogador ou deixa um registro
  - registro de outro jogador visível na sessão

**Escala.**
- Atendido: Jogador deixa e lê mensagens de outros jogadores em sessões distintas
- Parcial: Jogador só lê registros de outros, sem poder deixar os seus, ou o inverso
- Não atendido: Não há troca assíncrona entre jogadores

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a mecânica de troca assíncrona (mural, bilhetes, diário compartilhado ou similar), com o autor, o local e o leitor da mensagem
- Design: Prever uma mecânica em que o jogador deixe mensagens ou registros e leia os deixados por outros jogadores em sessões posteriores
- Código: Gravar de forma persistente a mensagem do jogador, associada ao jogador e ao contexto em que foi deixada. Ler e exibir, em sessão distinta, as mensagens gravadas por outros jogadores

**Depende de.** —

### D08 — O jogador deve trocar informações com os mecanismos do jogo

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D08.1 — Nível A

**Enunciado.** Em ao menos uma situação do jogo, um personagem não jogável ou mecanismo entrega informação ao jogador e em seguida recebe dele uma resposta, escolha ou item que altera o que o jogo exibe a seguir

**Justificativa do nível.** essencialidade alta, viabilidade alta. Em Vigotski, a interação com o meio é mediada por signos e instrumentos, e uma troca de mão dupla com o jogo faz do sistema um interlocutor, e não um painel de exibição. Se o jogo só emite informação, o jogador permanece receptor. Uma situação com troca de mão dupla já estabelece essa relação, e diálogos com escolhas e entrega de itens são mecânicas comuns e de baixo custo.

**Evidência.**
- Código: Localizar diálogos, quadros de pergunta e mecanismos de entrega ou recebimento de itens e verificar se a resposta do jogador é registrada e muda o estado ou o conteúdo seguinte; confirmar no código que duas entradas diferentes levam a saídas diferentes
  - o mecanismo emite informação ao jogador
  - a entrada do jogador (escolha, resposta, item) é lida pelo mecanismo
  - a entrada do jogador altera a próxima saída do mecanismo ou o estado do jogo, com ao menos duas entradas possíveis levando a saídas diferentes
- Documentação: não se aplica
- Vídeo: Registrar uma troca entre o jogador e personagem ou mecanismo em duas tentativas (ou duas gravações) com entradas diferentes, anotando a informação recebida, a entrada do jogador e o que o jogo exibe depois em cada tentativa
  - uma troca completa observada (informação recebida, entrada do jogador, resposta do jogo)
  - a mesma troca repetida com outra entrada do jogador
  - o que o jogo exibe depois difere entre as duas tentativas

**Escala.**
- Atendido: Em ao menos uma situação, o mecanismo entrega informação, recebe a entrada do jogador e altera o que o jogo exibe a seguir conforme essa entrada
- Parcial: Em ao menos uma situação, o mecanismo recebe a entrada do jogador, mas o que o jogo exibe a seguir é o mesmo para qualquer entrada
- Não atendido: Os mecanismos apenas emitem informação ao jogador, sem receber entrada dele

**Recomendações.**
- Documentação: não se aplica
- Design: Definir ao menos uma situação em que um personagem não jogável ou mecanismo entregue informação ao jogador e receba dele uma resposta, escolha ou item. Prever, para essa situação, duas ou mais entradas possíveis do jogador que levem a saídas diferentes do jogo
- Código: Ler no diálogo ou mecanismo a entrada do jogador (escolha, resposta ou item). Fazer a próxima saída do mecanismo ou o estado do jogo depender dessa entrada, com ao menos duas entradas levando a saídas diferentes

**Depende de.** —

### D09 — O jogador deve se comunicar por linguagem escrita

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D09.1 — Nível AA

**Definições.**

- *texto livre*: uma sequência de caracteres digitada pelo jogador em campo de entrada (ou em teclado exibido na tela que permita qualquer sequência), sem ser escolhida de lista de opções prontas, e recebida pelo jogo
- *composição por seleção*: escolher, em lista fechada oferecida pelo jogo, palavras ou frases prontas que o jogo exibe ou envia como mensagem do jogador sem avaliá-las como certas ou erradas (opção de diálogo, chat rápido, montagem de frase por palavras), e não conta como texto livre
- *alternativa de múltipla escolha*: uma opção que o jogo avalia como certa ou errada para uma pergunta ou tarefa; escolher uma alternativa de múltipla escolha, com texto escrito ou não, não é composição por seleção nem produção de texto
- *opção avaliada como certa ou errada*: se o jogo avalia a opção escolhida como certa ou errada, ela é múltipla escolha, mesmo quando o texto também é exibido ou enviado como mensagem do jogador (por exemplo, montagem de frase por palavras com correção e opção de diálogo avaliada como certa ou errada)

**Enunciado.** Em ao menos um ponto do jogo, o jogador produz texto livre, como em chat, resposta aberta, anotação ou nome de item

**Justificativa do nível.** essencialidade média, viabilidade alta. Em Vigotski, a linguagem é instrumento de mediação que organiza o pensamento, e a escrita exige que o sujeito formule por conta própria o que quer dizer. Quando o jogador apenas lê, seleciona frases prontas ou escolhe alternativas, o jogo dispensa essa formulação. A essencialidade é média porque a comunicação também ocorre por fala (D06) ou por ação no jogo. Um campo de entrada de texto é recurso padrão das ferramentas de desenvolvimento; viabilidade alta.

**Evidência.**
- Código: Localizar campos de entrada de texto (input fields, teclados exibidos na tela) e verificar se aceitam qualquer sequência de caracteres digitada pelo jogador ou se o conteúdo é escolhido de uma lista fechada de opções. Verificar também se o jogo lê o conteúdo digitado. Nas listas fechadas, classificar cada uma: primeiro verificar se o jogo avalia a opção escolhida como certa ou errada: se avalia, é alternativa de múltipla escolha, mesmo que o texto também seja exibido ou enviado como mensagem do jogador; se não avalia e o jogo exibe ou envia a opção como mensagem do jogador, é composição por seleção
  - existe campo de entrada de texto ou teclado na tela que aceita qualquer sequência de caracteres digitada pelo jogador, sem lista fechada de opções
  - um manipulador de evento (handler) ou função do jogo lê o texto digitado e o usa (exibe, guarda, envia ou avalia)
  - se não há campo desse tipo, existe lista fechada de palavras ou frases que o jogo exibe ou envia como mensagem do jogador e não avalia como certas ou erradas (composição por seleção; indica o estado parcial)
  - se não há campo desse tipo nem composição por seleção, as únicas listas fechadas são alternativas de múltipla escolha (incluindo opções avaliadas como certas ou erradas, mesmo exibidas como mensagem do jogador) ou opções não textuais (indica o estado nao_atendido)
- Documentação: não se aplica
- Vídeo: O vídeo só confirma a evidência de código: a ausência de digitação no vídeo não prova que o jogo não oferece texto livre. Registrar os momentos em que o jogador digita ou escolhe texto e anotar se ele digita caracteres de sua escolha, compõe mensagem por seleção ou escolhe alternativa de múltipla escolha
  - ao menos um momento em que o jogador digita caracteres de sua escolha em campo de entrada e o texto aparece no jogo
  - nos momentos de escolha de texto registrados (mínimo 0), o jogador compõe mensagem por seleção, sem avaliação do jogo como certa ou errada, em vez de digitar (indica o estado parcial)
  - nos momentos de escolha registrados (mínimo 0), o jogador escolhe apenas alternativas de múltipla escolha, incluindo opções avaliadas como certas ou erradas mesmo quando exibidas como mensagem do jogador (não contam como produção de texto)

**Escala.**
- Atendido: Em ao menos um ponto do jogo, o jogador digita texto livre, nos termos do enunciado e das definições, e o jogo recebe esse texto
- Parcial: O jogador compõe mensagens por seleção, nos termos do enunciado e das definições, sem digitar texto livre em nenhum ponto do jogo
- Não atendido: O jogador não digita texto livre nem compõe mensagem por seleção em nenhum ponto do jogo; só lê, escolhe alternativas de múltipla escolha (incluindo opções avaliadas como certas ou erradas, mesmo exibidas como mensagem do jogador), escolhe opções não textuais ou age sobre objetos

**Recomendações.**
- Documentação: não se aplica
- Design: Prever ao menos um ponto do jogo em que o jogador digite texto livre, como em chat, resposta aberta, anotação ou nome de item
- Código: Acrescentar um campo de entrada de texto ou teclado na tela que aceite qualquer sequência de caracteres, sem lista fechada de opções. Ler o texto digitado em um manipulador de evento (handler) ou função que o exiba, guarde, envie ou avalie

**Depende de.** —

### D10 — O jogo deve viabilizar o comportamento ativo do jogador

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D10.1 — Nível A

**Definições.**

- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *trecho passivo*: um intervalo contínuo do jogo em que a interface não oferece ao jogador nenhuma ação que altere o estado do jogo (mover-se, selecionar, manipular objeto, responder, construir), restando apenas assistir, ler, avançar texto ou pular cena
- *avançar texto e pular cena*: ações que não alteram o estado do jogo e não tornam o trecho ativo
- *comprimento integral*: o tempo que o próprio jogo leva para exibir o trecho inteiro: para cena ou animação, a duração de sua reprodução completa, mesmo quando o jogo permite pulá-la; para sequência de texto em que a única ação oferecida é avançar, a soma das esperas que o jogo impõe antes de aceitar cada avanço (inclui o efeito de digitação do texto), isto é, o tempo medido quando o jogador avança na primeira oportunidade que o jogo oferece; o trecho que o jogador pula termina no pulo, mas conta pelo seu comprimento integral e não pelo tempo até o pulo
- *partes avaliadas*: as cobertas pelas fontes de evidência fornecidas: no vídeo, só o que foi gravado; no código e na documentação, o jogo descrito; partes não gravadas nem descritas não são avaliadas
- *sequência de diálogo sem espera*: sequência de diálogo em que o jogo não impõe nenhuma espera antes do avanço tem comprimento integral próximo de 0 e passa neste critério por construção, pois a validade dessa sequência é tratada por outras diretrizes (por exemplo, D03 e D04)

**Enunciado.** Nenhum trecho passivo das partes avaliadas do jogo tem comprimento integral maior que 120 segundos

**Justificativa do nível.** essencialidade alta, viabilidade alta. Para Vigotski, o conhecimento se constrói na atividade do sujeito, e não na recepção de informação pronta. Longos trechos em que o jogador só assiste ou lê o tornam espectador e interrompem a atividade que sustenta a aprendizagem. A teoria justifica a existência de um limite, não o seu valor: os 120 segundos são uma convenção operacional do vygolint, fixa e igual para qualquer jogo. O limite é absoluto, e não uma fração da gravação, porque uma fração dependeria da duração da sessão gravada e faria o mesmo jogo receber graus diferentes conforme o tempo jogado. O comprimento é medido pelo conteúdo do jogo e não pelo ritmo do jogador gravado, para que gravações diferentes do mesmo jogo cheguem ao mesmo grau. Encurtar cenas e textos corridos ou intercalar ações do jogador é decisão de projeto, sem custo técnico especial; viabilidade alta.

**Evidência.**
- Código: Localizar cenas, animações, vídeos e sequências de texto ou diálogo, nos dados de cena e de diálogo, nas durações de linhas do tempo (timeline), clipes e animações, e nos marcadores de pular cena (skip flags). Para cada uma, verificar nos manipuladores de entrada ativos durante ela se o jogador tem alguma ação que altere o estado do jogo; se não tem, é trecho passivo. Calcular o comprimento integral: duração total da cena, ou soma das esperas mínimas antes de cada avanço de texto, ignorando o marcador de pular. Regra de desempate: se as fontes divergirem sobre o comprimento integral de um mesmo trecho, vale o valor do código; sem código, o do GDD; sem ambos, a medida do vídeo; código que existe mas não traz dado sobre o trecho conta como sem código para esse trecho, e GDD que não descreve o trecho conta como sem GDD para esse trecho
  - todas as cenas, animações, vídeos e sequências de texto sem ação do jogador que altere o estado do jogo foram listadas, cada uma com a duração de sua linha do tempo, clipe ou animação ou com a soma das esperas mínimas antes de cada avanço (mínimo 0 trechos)
  - o marcador de pular cena de cada trecho foi anotado, e o comprimento integral foi calculado ignorando o marcador
  - o comprimento integral de cada trecho listado é de no máximo 120 segundos
- Documentação: Verificar no GDD ou documento equivalente a descrição das cenas, animações, vídeos e sequências de texto sem ação do jogador, a duração declarada de cada uma e se podem ser puladas. A duração declarada é o comprimento integral, mesmo para cena que pode ser pulada. Regra de desempate: se as fontes divergirem sobre o comprimento integral de um mesmo trecho, vale o valor do código; sem código, o do GDD; sem ambos, a medida do vídeo; código que existe mas não traz dado sobre o trecho conta como sem código para esse trecho, e GDD que não descreve o trecho conta como sem GDD para esse trecho
  - o GDD descreve cada cena, animação, vídeo ou sequência de texto em que o jogador não tem ação que altere o estado do jogo e declara o comprimento integral de cada uma (mínimo 0 trechos)
  - o comprimento integral declarado de cada trecho descrito é de no máximo 120 segundos
- Vídeo: Assistir a toda a gravação e registrar os intervalos em que a interface não oferece ao jogador nenhuma ação que altere o estado do jogo, restando apenas assistir, ler, avançar texto ou pular cena. A classificação depende do que a interface oferece, não de o jogador agir ou não: um intervalo em que há ações disponíveis e o jogador não as usa não é trecho passivo. Medir o comprimento integral de cada trecho: em cena ou animação exibida até o fim, pelos marcadores de tempo do vídeo; em sequência de texto, para cada avanço da sequência, o tempo desde o instante em que o texto (ou o segmento de cena) aparece até o instante em que o jogo aceita o avanço pela primeira vez (aparece o indicador de continuar ou a entrada passa a ser aceita), sem contar o tempo que o jogador gravado leva depois disso; o comprimento da sequência é a soma dessas esperas, e as pausas do jogador gravado entre um avanço e o seguinte não entram na soma; em trecho pulado, pelo comprimento integral determinável (o comprimento integral de trecho pulado é determinável quando está visível na gravação (barra de progresso, contador, ou a mesma cena exibida inteira em outro ponto) ou declarado no GDD ou no código; se não for determinável por nenhuma fonte fornecida, o trecho fica registrado como não determinado e não é contado como maior que 120 segundos). Limitação conhecida: o trecho pulado cujo comprimento integral não pode ser determinado é registrado como "não determinado"; por isso duas gravações do mesmo jogo podem diferir quando uma assiste a uma cena longa até o fim e a outra a pula; evidência de código ou do GDD resolve essa diferença. Regra de desempate: se as fontes divergirem sobre o comprimento integral de um mesmo trecho, vale o valor do código; sem código, o do GDD; sem ambos, a medida do vídeo; código que existe mas não traz dado sobre o trecho conta como sem código para esse trecho, e GDD que não descreve o trecho conta como sem GDD para esse trecho. Intervalo ocioso: em intervalo no qual o jogador não age e nenhum controle ou indicação de ação é visível, o intervalo é trecho passivo, salvo se código ou GDD mostrarem ação disponível nele
  - todos os trechos passivos registrados no vídeo foram anotados com início, fim e comprimento integral (para sequência de texto, a soma das esperas de cada avanço, do aparecimento do texto até o jogo aceitar o avanço; mínimo 0)
  - o comprimento integral de cada trecho passivo registrado é de no máximo 120 segundos
  - cada trecho pulado teve o comprimento integral determinado ou foi registrado como não determinado

**Escala.**
- Atendido: Nenhum trecho passivo das partes avaliadas tem comprimento integral maior que 120 segundos, nos termos do enunciado e das definições
- Parcial: Um único trecho passivo das partes avaliadas tem comprimento integral maior que 120 segundos, nos termos do enunciado e das definições
- Não atendido: Dois ou mais trechos passivos das partes avaliadas têm, cada um, comprimento integral maior que 120 segundos, nos termos do enunciado e das definições

**Recomendações.**
- Documentação: Descrever no GDD ou documento equivalente cada cena, animação, vídeo ou sequência de texto em que o jogador não tem ação que altere o estado do jogo. Declarar o comprimento integral de cada um desses trechos, inclusive dos que podem ser pulados
- Design: Encurtar para no máximo 120 segundos cada trecho passivo com comprimento integral maior que esse limite, ou dividi-lo com ações do jogador que alterem o estado do jogo, de modo que nenhum trecho passivo resultante tenha comprimento integral maior que 120 segundos
- Código: Reduzir a duração da linha do tempo, clipe ou animação, ou a soma das esperas mínimas antes de cada avanço de texto, de cada trecho passivo com comprimento integral maior que 120 segundos. Acrescentar, nos trechos que não forem reduzidos, manipuladores de entrada que ofereçam ao jogador ação que altere o estado do jogo, de modo que nenhum trecho passivo resultante tenha comprimento integral maior que 120 segundos

**Depende de.** —

### D11 — O jogador deve coletar informações

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D11.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *objetivo de aprendizagem*: cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados
- *informação*: um item, dado, texto, imagem ou medida relativo a ao menos um objetivo de aprendizagem listado no GDD ou documento equivalente; é relativo a um objetivo quando o GDD ou documento equivalente, ou a marcação do item no código (campo, identificador ou etiqueta de objetivo), o associa a esse objetivo
- *coletar*: obter a informação por ação própria de modo que o jogo a guarde (inventário, diário, caderno ou painel) para consulta ou uso posterior
- *uso posterior*: um trecho de missão ou desafio posterior ao momento da coleta que só pode ser resolvido ou avançado com a posse, o valor ou o conteúdo dessa informação

**Enunciado.** O jogador coleta ao menos uma informação e ao menos uma informação coletada é usada depois em missão ou desafio

**Justificativa do nível.** essencialidade alta, viabilidade alta. Em Vigotski, as funções psicológicas superiores, como a memória e a atenção voluntárias, se desenvolvem com apoio de instrumentos e signos externos, e registros guardados funcionam como esse apoio. A coleta é o ato pelo qual o jogador se apropria desses signos e instrumentos: sem ela o conteúdo é entregue pronto pelo jogo, e não construído pelo jogador. Coletar informação que será necessária mais tarde, em missão ou desafio com objetivo e condição de conclusão próprios, obriga o jogador a selecionar, reter e relacionar dados em vez de reagir ao que está na tela. Um mecanismo de inventário ou de registro é padrão no desenvolvimento de jogos; viabilidade alta.

**Evidência.**
- Código: Localizar a mecânica de coleta (inventário, diário, caderno, painel) e as verificações dessas estruturas nas missões e desafios. Verificar, para cada item guardado, se o código o associa a objetivo de aprendizagem (campo, identificador ou etiqueta) ou se o GDD, quando fornecido, o associa
  - uma ação do jogador (interação, seleção, resposta) adiciona uma informação a uma estrutura persistente do jogo (inventário, diário, caderno ou painel)
  - a informação coletada é relativa a ao menos um objetivo de aprendizagem do GDD ou documento equivalente, ou está marcada no código com esse objetivo
  - uma condição de missão ou desafio posterior à coleta verifica a posse, o valor ou o conteúdo da informação coletada
  - se existe estrutura de guarda mas nenhum item guardado é relativo a objetivo de aprendizagem, anotar (indica o estado nao_atendido)
- Documentação: Verificar no GDD ou documento equivalente a mecânica de coleta e o uso das informações coletadas
  - o GDD descreve o que o jogador coleta, como o jogo o guarda e a qual objetivo de aprendizagem a informação é relativa
  - o GDD descreve a missão ou desafio posterior que exige a posse, o valor ou o conteúdo da informação coletada
  - se o GDD descreve itens guardados que não são relativos a nenhum objetivo de aprendizagem listado, anotar (indica o estado nao_atendido)
- Vídeo: O vídeo só confirma a evidência de código ou documentação: a ausência de coleta ou de uso no vídeo não prova que o jogo não os tem, e o vídeo não decide se a informação é relativa a objetivo de aprendizagem, o que vem do código ou da documentação. Registrar os momentos de coleta e os momentos em que a informação coletada é exigida
  - ao menos um momento em que o jogador obtém por ação própria uma informação e ela passa a constar em inventário, diário, caderno ou painel
  - ao menos um momento posterior em que uma missão ou desafio exige a posse, o valor ou o conteúdo da informação coletada para ser resolvido ou avançado
  - a relação da informação coletada com objetivo de aprendizagem foi verificada no código ou na documentação e não no vídeo

**Escala.**
- Atendido: O jogador coleta ao menos uma informação, nos termos do enunciado e das definições, e ao menos uma informação coletada é usada depois em missão ou desafio, nos termos do enunciado e das definições
- Parcial: O jogador coleta ao menos uma informação, nos termos do enunciado e das definições, mas nenhuma informação coletada é usada depois em missão ou desafio, nos termos do enunciado e das definições
- Não atendido: O jogador não coleta nenhuma informação, nos termos do enunciado e das definições: nada é obtido por ação própria e guardado pelo jogo, ou o que é guardado não é relativo a objetivo de aprendizagem

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente o que o jogador coleta, como o jogo o guarda e a qual objetivo de aprendizagem cada informação é relativa. Registrar a missão ou desafio posterior que exige a posse, o valor ou o conteúdo da informação coletada
- Design: Definir ao menos uma informação relativa a um objetivo de aprendizagem que o jogador obtenha por ação própria e que o jogo guarde em inventário, diário, caderno ou painel. Incluir, em missão ou desafio posterior à coleta, uma condição que exija a posse, o valor ou o conteúdo dessa informação
- Código: Fazer uma ação do jogador adicionar a informação a uma estrutura persistente (inventário, diário, caderno ou painel). Marcar o item guardado com o objetivo de aprendizagem a que se relaciona (campo, identificador ou etiqueta). Acrescentar a uma condição de missão ou desafio posterior à coleta a verificação da posse, do valor ou do conteúdo dessa informação

**Depende de.** —

### D12 — O jogo deve fornecer mecanismos para o jogador construir coisas

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D12.1 — Nível AAA

**Definições.**

- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *elemento*: uma peça, item, bloco, valor ou outro objeto disponível ao jogador
- *artefato novo*: um objeto, estrutura ou configuração inexistente no estado do jogo antes da combinação e identificável como unidade
- *persiste*: quando permanece disponível ao jogador depois de concluída a ação de combinar e só deixa de existir se o jogador o remover ou o consumir em uso posterior
- *cenário* (sentido corrente): lugar do jogo em que o artefato fica disponível («no cenário, inventário ou lista»), e não o cenário jogável

**Enunciado.** O jogador combina dois ou mais elementos por ação própria e obtém um artefato novo que persiste no jogo

**Justificativa do nível.** essencialidade baixa, viabilidade média. Em Vigotski, a atividade humana é mediada por instrumentos, e construir é agir sobre objetos com esses instrumentos para produzir um artefato que o sujeito pode examinar e usar depois (mediação por instrumentos). A essencialidade é baixa porque a atividade do jogador pode se dar por outras vias, como resolver problemas (D01), explorar o cenário (D05) ou coletar informações (D11). Implementar combinação e persistência de objetos criados pelo jogador exige regras e estado adicionais; viabilidade média.

**Evidência.**
- Código: Localizar a lógica de combinação, criação ou montagem de objetos e verificar se o resultado é registrado no estado do jogo. Elemento é uma peça, item, bloco, valor ou outro objeto disponível ao jogador; artefato novo é um objeto, estrutura ou configuração inexistente no estado do jogo antes da combinação e identificável como unidade; persiste quando permanece disponível depois da ação de combinar e só deixa de existir se o jogador o remover ou o consumir em uso posterior
  - uma ação do jogador combina dois ou mais elementos e instancia um objeto, estrutura ou configuração identificável como unidade que não existia antes
  - o artefato criado é adicionado ao estado do jogo (cenário, inventário ou lista) e não é destruído ao fim da ação de combinar
  - o artefato só é removido por ação do jogador ou consumido em uso posterior
- Documentação: Verificar no GDD ou documento equivalente a mecânica de construção. Elemento é uma peça, item, bloco, valor ou outro objeto disponível ao jogador; artefato novo é um objeto, estrutura ou configuração inexistente no estado do jogo antes da combinação e identificável como unidade; persiste quando permanece disponível depois da ação de combinar e só deixa de existir se o jogador o remover ou o consumir em uso posterior
  - o GDD descreve quais elementos o jogador combina e qual artefato resulta da combinação
  - o GDD descreve onde o artefato permanece disponível depois de criado e em que condições deixa de existir
- Vídeo: O vídeo só confirma a evidência de código ou documentação: a ausência de construção no vídeo não prova que o jogo não a oferece. Registrar o momento em que o jogador combina elementos e verificar, em momentos posteriores da gravação, se o artefato resultante continua disponível
  - ao menos um momento em que o jogador combina dois ou mais elementos e um objeto, estrutura ou configuração novo, identificável como unidade, passa a existir
  - em momento posterior da gravação, o artefato continua disponível ao jogador (no cenário, inventário ou lista)

**Escala.**
- Atendido: O jogador combina dois ou mais elementos por ação própria e obtém um artefato novo, nos termos do enunciado e das definições, que persiste no jogo
- Parcial: O jogador combina dois ou mais elementos por ação própria, mas o resultado não permanece disponível depois da ação de combinar (por exemplo, a combinação é apenas avaliada como correta ou incorreta e descartada)
- Não atendido: O jogador não combina elementos para obter resultado novo; as ações disponíveis só manipulam elementos já existentes no jogo

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente quais elementos o jogador combina e qual artefato resulta de cada combinação. Registrar onde o artefato permanece disponível depois de criado e em que condições deixa de existir
- Design: Definir ao menos uma combinação de dois ou mais elementos, feita por ação do jogador, que produza um artefato novo. Manter esse artefato disponível ao jogador depois da combinação, até que ele o remova ou o consuma
- Código: Instanciar, na ação de combinar, o objeto, estrutura ou configuração resultante como unidade. Adicionar o artefato ao estado do jogo (cenário, inventário ou lista) sem destruí-lo ao fim da ação. Removê-lo só por ação do jogador ou por consumo em uso posterior

**Depende de.** —

### D13 — O jogo permite o desenvolvimento de tarefas e missões em grupo

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D13.1 — Nível AAA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *jogador*: uma pessoa que joga, e personagem não jogável não conta
- *missão exige mais de um jogador*: quando a conclusão só é registrada depois da ação prevista de cada um de ao menos dois jogadores diferentes
- *missão aceita dois ou mais jogadores*: quando o jogo permite que dois ou mais jogadores diferentes atuem nela, na mesma sessão ou em sessões diferentes

**Enunciado.** Existe ao menos uma missão que só se conclui quando cada um de dois ou mais jogadores diferentes realiza ao menos uma ação prevista para ela, na mesma sessão ou em sessões diferentes

**Justificativa do nível.** essencialidade média, viabilidade baixa. Em Vigotski, a interação social é a origem das funções psicológicas superiores, e uma missão que só se conclui com a ação de mais de um jogador cria a situação em que a ZDP entre pares pode se formar. A essencialidade é média porque a interação também ocorre por comunicação entre jogadores (D06, D07) e fora do jogo. Exige multijogador, estado compartilhado entre jogadores e uma condição de conclusão que dependa de mais de uma pessoa, com identificação de cada jogador; viabilidade baixa.

**Evidência.**
- Código: Localizar a condição de conclusão das missões e verificar se ela lê ações ou contribuições de mais de um identificador de jogador
  - existe missão cuja condição de conclusão verifica ações de dois ou mais identificadores de jogador diferentes
  - se a missão aceita dois ou mais jogadores mas a condição de conclusão verifica a ação de apenas um deles, anotar (indica o estado parcial)
  - a conclusão não é registrada se a ação prevista de algum desses jogadores não ocorreu
  - existe sessão, sala ou registro compartilhado que aceita dois ou mais jogadores diferentes na mesma missão
- Documentação: Verificar no GDD ou documento equivalente as missões em grupo
  - o GDD descreve missão com ações previstas para dois ou mais jogadores
  - o GDD descreve que a missão só se conclui depois da ação prevista de cada um desses jogadores
  - se o GDD descreve missão que aceita dois ou mais jogadores mas cuja conclusão depende da ação de apenas um deles, anotar (indica o estado parcial)
- Vídeo: O vídeo só confirma a evidência de código ou documentação: ele não mostra que a conclusão exige mais de um jogador. Registrar missão em que dois ou mais jogadores diferentes atuam, na mesma gravação ou em gravações distintas, as ações de cada um e o momento da conclusão
  - dois ou mais jogadores diferentes atuam na mesma missão, na mesma gravação ou em gravações distintas
  - a conclusão da missão é registrada depois da ação de cada um desses jogadores
  - se a conclusão é registrada com a ação de apenas um dos jogadores que a missão aceita, anotar (indica o estado parcial)

**Escala.**
- Atendido: Existe ao menos uma missão que só se conclui depois da ação prevista de cada um de dois ou mais jogadores diferentes, nos termos do enunciado e das definições
- Parcial: Existe missão que aceita dois ou mais jogadores, nos termos do enunciado e das definições, mas o jogo registra a conclusão com a ação de apenas um deles
- Não atendido: Nenhuma missão aceita dois ou mais jogadores, nos termos do enunciado e das definições

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a missão em grupo, com as ações previstas para cada um dos dois ou mais jogadores. Registrar que a missão só se conclui depois da ação prevista de cada um deles
- Design: Definir ao menos uma missão com ações previstas para dois ou mais jogadores diferentes. Condicionar a conclusão dessa missão à ação prevista de cada um deles, na mesma sessão ou em sessões diferentes
- Código: Criar sessão, sala ou registro compartilhado que aceite dois ou mais jogadores na mesma missão. Fazer a condição de conclusão verificar as ações de cada identificador de jogador previsto. Impedir o registro da conclusão enquanto a ação prevista de algum desses jogadores não ocorrer

**Depende de.** (D06.1 ou D07.1)

### D14 — O jogador deve conseguir inserir comentários no jogo que ficarão disponíveis para outros jogadores

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D14.1 — Nível AA

**Definições.**

- *comentário*: um texto digitado pelo jogador
- *outro jogador*: um jogador com perfil ou conta diferente do autor
- *sessão posterior*: uma sessão iniciada depois do término da sessão em que o comentário foi escrito

**Enunciado.** O jogador escreve um comentário associado a um local ou objeto do jogo e o jogo o exibe a outro jogador, em sessão posterior, quando este alcança esse local ou objeto

**Justificativa do nível.** essencialidade média, viabilidade média. Em Vigotski, os signos produzidos por uma pessoa mediam a atividade de outras, e um comentário deixado num local do jogo funciona como mediação entre jogadores que nem precisam estar presentes juntos. A essencialidade é média porque a interação entre jogadores também ocorre em tempo real (D06) e por trocas assíncronas sem local associado (D07). Exige persistência de dados fora da sessão, associação ao local ou objeto e distinção entre perfis; viabilidade média.

**Evidência.**
- Código: Localizar a escrita e a leitura de comentários e verificar onde são guardados e como são exibidos
  - existe campo de entrada que grava o texto digitado junto com um identificador de local ou objeto e o identificador do autor
  - o comentário é guardado fora do estado da sessão (arquivo, banco de dados ou servidor) e sobrevive ao fim dela
  - ao jogador alcançar o local ou objeto, o jogo lê e exibe comentários de autores com perfil diferente do jogador atual
  - se a leitura não filtra por local ou objeto e exibe os comentários numa lista geral, anotar (indica o estado parcial)
- Documentação: não se aplica
- Vídeo: O vídeo só confirma a evidência de código: a ausência do comentário no vídeo não prova que o jogo não o persiste. Exigir duas gravações: uma em que um jogador escreve o comentário em um local ou objeto e outra, de sessão posterior e com perfil diferente, em que o outro jogador alcança o mesmo local ou objeto
  - na primeira gravação, o jogador digita um comentário e o associa a um local ou objeto
  - na segunda gravação, de sessão posterior e com perfil diferente, o jogador alcança o mesmo local ou objeto e o comentário é exibido
  - se, na segunda gravação, o comentário de outro jogador aparece numa lista geral, sem o jogador ter alcançado local ou objeto associado, anotar (indica o estado parcial)

**Escala.**
- Atendido: Comentário escrito por um jogador, associado a um local ou objeto, é exibido a outro jogador em sessão posterior, quando este alcança esse local ou objeto
- Parcial: Comentário escrito por um jogador é exibido a outros jogadores em sessão posterior, mas não está associado a local ou objeto do jogo (por exemplo, aparece numa lista geral)
- Não atendido: Nenhum comentário escrito por um jogador é exibido a outros jogadores em sessão posterior

**Recomendações.**
- Documentação: não se aplica
- Design: Prever que o jogador escreva comentários associados a um local ou objeto do jogo. Definir que o jogo exiba esses comentários a outro jogador, em sessão posterior, quando este alcança esse local ou objeto
- Código: Acrescentar um campo de entrada de texto associado ao local ou objeto. Gravar o texto digitado junto com o identificador do local ou objeto e o identificador do autor. Guardar o comentário fora do estado da sessão (arquivo, banco de dados ou servidor). Ler e exibir, quando o jogador alcança o local ou objeto, os comentários associados a ele cujo autor tem perfil diferente do jogador atual

**Depende de.** —

### D15 — O jogo deve estimular a interação entre jogadores por diversas ferramentas de comunicação

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D15.1 — Nível AAA

**Definições.**

- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *ferramenta de comunicação*: um recurso do jogo pelo qual um jogador envia conteúdo a outro jogador
- *ferramentas distintas*: duas ferramentas que diferem no meio (texto, voz ou sinais predefinidos) ou na temporalidade (entrega em tempo real ou registro lido em sessão posterior); dois canais de mesmo meio e mesma temporalidade, como um chat geral e um chat privado, ou um chat rápido e uma roda de frases, contam como uma única ferramenta
- *texto*: sequência de caracteres digitada pelo jogador em campo de entrada
- *sinais predefinidos*: conteúdo que o jogador escolhe em lista fechada oferecida pelo jogo, sem digitar, como emotes, marcadores e frases prontas (chat rápido, roda de frases)
- *relação com D06.1*: a ferramenta conta para este critério mesmo quando o critério D06.1 a graduaria como parcial

**Enunciado.** O jogo oferece ao menos duas ferramentas distintas de comunicação entre jogadores

**Justificativa do nível.** essencialidade média, viabilidade baixa. Em Vigotski, a linguagem é instrumento de mediação, e diferentes instrumentos semióticos (fala, escrita, sinais) dão ao jogador mais de um meio de se fazer entender e de entender o outro. A essencialidade é média porque um único canal já sustenta a interação social (D06, D07). Manter dois ou mais canais, com infraestrutura de rede e de persistência para cada um, é custo elevado para jogos educacionais; viabilidade baixa.

**Evidência.**
- Código: Localizar os módulos de comunicação entre jogadores (chat de texto, voz, mensagens persistidas, sinais predefinidos) e classificar cada um por meio e temporalidade: módulo em que o jogador digita é texto; módulo em que o jogador escolhe conteúdo de lista fechada, incluindo chat rápido e roda de frases, é sinais predefinidos. Contar as ferramentas distintas
  - existe módulo que envia conteúdo de um jogador a outro jogador
  - cada módulo foi classificado por meio (texto, voz ou sinais predefinidos) e por temporalidade (tempo real ou sessão posterior)
  - há ao menos dois módulos que diferem no meio ou na temporalidade
- Documentação: Verificar no GDD ou documento equivalente a lista de ferramentas de comunicação entre jogadores e classificar cada uma por meio e temporalidade: ferramenta em que o jogador digita é texto; ferramenta em que o jogador escolhe conteúdo de lista fechada, incluindo chat rápido e roda de frases, é sinais predefinidos
  - o GDD descreve cada ferramenta de comunicação, seu meio e sua temporalidade
  - o GDD descreve ao menos duas ferramentas que diferem no meio ou na temporalidade
- Vídeo: não se aplica

**Escala.**
- Atendido: O jogo oferece duas ou mais ferramentas de comunicação entre jogadores distintas, nos termos do enunciado e das definições
- Parcial: O jogo oferece uma única ferramenta de comunicação entre jogadores, nos termos do enunciado e das definições
- Não atendido: O jogo não oferece ferramenta de comunicação entre jogadores, nos termos do enunciado e das definições

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente cada ferramenta de comunicação entre jogadores, com seu meio (texto, voz ou sinais predefinidos) e sua temporalidade (tempo real ou sessão posterior)
- Design: Prever ao menos duas ferramentas de comunicação entre jogadores que difiram no meio ou na temporalidade
- Código: Implementar ao menos dois módulos que enviem conteúdo de um jogador a outro e difiram no meio (texto, voz ou sinais predefinidos) ou na temporalidade (tempo real ou sessão posterior)

**Depende de.** (D06.1 ou D07.1)

### D16 — O jogo deve fornecer meios do jogador solicitar ajuda de outros jogadores

- Categoria: Mediação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D16.1 — Nível AA

**Definições.**

- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta

**Enunciado.** Existe uma ação explícita de pedir ajuda que encaminha a solicitação do jogador a outro jogador

**Justificativa do nível.** essencialidade média, viabilidade média. Mediação por pares é a forma mais direta da zona de desenvolvimento proximal entre jogadores, mas a mediação também é oferecida pelo próprio jogo (D17 a D21). Exige um canal entre jogadores (D06 ou D07) e uma ação dedicada; viabilidade média.

**Evidência.**
- Código: Localizar ação, botão ou comando de pedir ajuda e verificar para onde a solicitação é enviada
  - ação de ajuda distinta do chat geral
  - solicitação chega a outro jogador, não só ao sistema
- Documentação: Verificar no GDD a mecânica de pedido de ajuda
  - fluxo descrito: quem pede, quem recebe, o que acontece
- Vídeo: Observar o jogador acionar o pedido de ajuda e o que ocorre em seguida
  - pedido de ajuda enviado a outro jogador

**Escala.**
- Atendido: Ação de pedir ajuda existe e chega a outro jogador
- Parcial: Ação existe, mas a resposta vem só do sistema ou de personagem não jogável
- Não atendido: Não há meio de pedir ajuda a outros jogadores

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a ação de pedir ajuda, com quem pede, quem recebe e o que acontece depois do pedido. Registrar que a solicitação chega a outro jogador, e não só ao sistema ou a personagem não jogável
- Design: Definir uma ação de pedir ajuda, distinta do chat geral, que encaminhe a solicitação do jogador a outro jogador, e não só ao sistema ou a personagem não jogável
- Código: Acrescentar uma ação, botão ou comando de pedir ajuda distinto do chat geral. Fazer o manipulador de evento (handler) dessa ação enviar a solicitação a outro jogador, e não só ao sistema ou a personagem não jogável

**Depende de.** (D06.1 ou D07.1)

### D17 — O jogo deve exibir feedback construtivo para as ações do jogador

- Categoria: Mediação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D17.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta

**Enunciado.** Toda ação incorreta do jogador recebe mensagem que indica o que fazer em seguida, e não apenas que errou

**Justificativa do nível.** essencialidade alta, viabilidade alta. Mediação é o núcleo da zona de desenvolvimento proximal: o jogo faz o papel do outro mais experiente. Feedback que só sinaliza acerto ou erro é reforço behaviorista, exatamente o que as diretrizes querem afastar. Implementação de baixo custo em qualquer motor de jogo.

**Evidência.**
- Código: Localizar os tratadores de erro ou falha de missão e minijogo e listar o texto exibido em cada um
  - mensagem contém orientação de próxima ação
  - mensagem referencia o conteúdo ou objeto envolvido no erro
- Documentação: Verificar no documento de design (GDD) a especificação de feedback por tipo de erro
  - tabela ou lista de erros com a mensagem orientadora correspondente
- Vídeo: Registrar o timestamp de cada erro cometido pelo jogador e classificar o feedback exibido
  - ao menos 3 ocorrências de erro observadas
  - cada ocorrência mostra orientação, não só sinal de erro

**Escala.**
- Atendido: Todas as ocorrências de erro observadas recebem feedback que orienta a próxima ação
- Parcial: Algumas ocorrências orientam; outras só sinalizam erro ou não recebem feedback
- Não atendido: O feedback só sinaliza acerto ou erro, ou não existe

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a tabela de ações incorretas previstas com a mensagem exibida em cada uma e a próxima ação que essa mensagem indica
- Design: Definir, para cada ação incorreta prevista, a próxima ação que a mensagem indica ao jogador
- Código: Trocar, em cada manipulador de erro, a mensagem que só sinaliza o erro por uma que indica a próxima ação. Acrescentar, em cada manipulador de erro que não exibe mensagem, uma mensagem que indica a próxima ação

**Depende de.** —

### D18 — O jogo deve exibir feedback individualizado para as ações do jogador

- Categoria: Mediação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D18.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *ponto de feedback*: cada missão, minijogo ou tipo de interação em que o jogo exibe, em texto ou fala, mensagem em resposta a uma ação do jogador
- *ação específica*: o que o jogador de fato fez no ponto de feedback (a alternativa escolhida, o objeto usado, a resposta digitada ou o local acionado)
- *histórico*: o conjunto de ações anteriores do mesmo jogador, na sessão ou em sessões salvas (número de tentativas, erros anteriores, acertos anteriores)
- *feedback individualizado*: o de um ponto de feedback em que existem ao menos duas ações específicas diferentes, ou dois históricos diferentes, que levam ao mesmo resultado (acerto ou erro) e produzem mensagens que diferem em ao menos uma informação que cita ou descreve o que o jogador fez (a resposta dada, o objeto usado, o tipo de erro, o número da tentativa); não contam como diferença o resultado (acerto ou erro) sozinho, o nome do jogador, a pontuação, sinônimos de elogio ou de erro que não citam a ação e a escolha de mensagem por sorteio sem uso da ação ou do histórico
- *ponto avaliado*: o ponto de feedback sobre o qual há evidência determinada: no código e no GDD, todo ponto de feedback descrito; no vídeo, só o ponto com duas ocorrências comparáveis, isto é, duas ocorrências com o mesmo resultado e ações específicas diferentes ou números de tentativa diferentes
- *escopo*: este critério avalia só se a mensagem varia: a orientação da próxima ação é tratada em D17, e a mudança do desafio conforme o desempenho é tratada em D33 e D34

**Enunciado.** Existe ao menos um ponto de feedback avaliado e todo ponto de feedback avaliado exibe feedback individualizado, isto é, a mensagem varia conforme a ação específica do jogador ou conforme o histórico dele, e não é a mesma para qualquer ação com o mesmo resultado

**Justificativa do nível.** essencialidade alta, viabilidade média. Na mediação vigotskiana, o outro mais experiente ajusta o apoio ao que o aprendiz fez e já fez, e é esse ajuste que orienta a atuação na zona de desenvolvimento proximal. Uma mensagem igual para ações diferentes não mostra ao jogador que o jogo identificou o que ele fez, o que a aproxima do reforço genérico que as diretrizes querem afastar. Este critério trata só da variação da mensagem (a orientação é D17), por isso não depende de D17.1: uma mensagem pode variar sem orientar. Viabilidade média: exige escrever mais de uma mensagem por ponto e, para variar pelo histórico, registrar tentativas e erros do jogador.

**Evidência.**
- Código: Localizar os manipuladores de evento (handlers) e funções que exibem mensagens de feedback em texto ou fala em resposta a ações do jogador e listar cada ponto de feedback. Em cada um, verificar se o texto é escolhido ou montado a partir da ação específica (valor escolhido, objeto, resposta) ou do histórico (contadores de tentativas ou de erros, registro de ações anteriores) e se há ao menos dois ramos, ou um texto que insere o dado da ação, que produzem mensagens diferentes para o mesmo resultado. Regra de desempate: se as fontes divergirem sobre um ponto de feedback, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o ponto conta como sem código para esse ponto, e GDD que não descreve o ponto conta como sem GDD para esse ponto; a ausência de variação no vídeo não prova que o jogo não varia, porque depende de o jogador gravado ter feito ações diferentes, e por isso o ponto sem ocorrências comparáveis no vídeo não é ponto avaliado
  - todos os pontos de feedback foram listados, cada um com o trecho de código que escolhe ou monta a mensagem (mínimo 0 pontos)
  - em cada ponto listado, a mensagem é escolhida ou montada a partir da ação específica ou do histórico, e não por sorteio nem apenas pelo resultado
  - em cada ponto listado, existem ao menos duas ações específicas diferentes, ou dois históricos diferentes, com o mesmo resultado, que produzem mensagens diferentes em informação que cita ou descreve o que o jogador fez
  - os pontos listados que não atendem aos dois itens anteriores foram anotados (indica o estado parcial quando ao menos um ponto atende)
- Documentação: Verificar no documento de design (GDD) ou documento equivalente a especificação das mensagens de feedback por ponto de feedback e o que seleciona cada mensagem. Regra de desempate: se as fontes divergirem sobre um ponto de feedback, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o ponto conta como sem código para esse ponto, e GDD que não descreve o ponto conta como sem GDD para esse ponto; a ausência de variação no vídeo não prova que o jogo não varia, porque depende de o jogador gravado ter feito ações diferentes, e por isso o ponto sem ocorrências comparáveis no vídeo não é ponto avaliado
  - o GDD lista, por ponto de feedback, as mensagens previstas e a ação específica ou o histórico que seleciona cada uma (mínimo 0 pontos)
  - em cada ponto listado, ao menos duas ações específicas diferentes, ou dois históricos diferentes, com o mesmo resultado, têm mensagens previstas que diferem em informação que cita ou descreve o que o jogador fez
  - os pontos listados que não atendem ao item anterior foram anotados (indica o estado parcial quando ao menos um ponto atende)
- Vídeo: O vídeo só confirma a evidência de código ou do GDD. Registrar o timestamp de cada mensagem de feedback, a ação específica que a gerou, o resultado e o número da tentativa, agrupando as ocorrências por ponto de feedback e identificando as ocorrências comparáveis. Regra de desempate: se as fontes divergirem sobre um ponto de feedback, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o ponto conta como sem código para esse ponto, e GDD que não descreve o ponto conta como sem GDD para esse ponto; a ausência de variação no vídeo não prova que o jogo não varia, porque depende de o jogador gravado ter feito ações diferentes, e por isso o ponto sem ocorrências comparáveis no vídeo não é ponto avaliado
  - todo ponto de feedback com duas ocorrências comparáveis no vídeo foi registrado, cada ocorrência com timestamp, ação específica, resultado e texto ou fala da mensagem (mínimo 0 pontos)
  - nos pontos registrados, as mensagens de ocorrências comparáveis diferem em informação que cita ou descreve o que o jogador fez
  - os pontos registrados em que ocorrências comparáveis recebem a mesma mensagem, ou mensagens que diferem só pelo resultado, pelo nome do jogador, pela pontuação ou por sinônimos, foram anotados (indica o estado parcial quando ao menos um ponto atende ao item anterior)

**Escala.**
- Atendido: Existe ao menos um ponto de feedback avaliado e todos os pontos de feedback avaliados exibem feedback individualizado, nos termos do enunciado e das definições
- Parcial: Ao menos um ponto de feedback avaliado exibe feedback individualizado, nos termos do enunciado e das definições, e ao menos outro ponto de feedback avaliado não o exibe, nos termos do enunciado e das definições
- Não atendido: Nenhum ponto de feedback avaliado exibe feedback individualizado, nos termos do enunciado e das definições, ou não existe ponto de feedback avaliado

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente, para cada ponto de feedback, as mensagens previstas e a ação específica ou o histórico que seleciona cada uma. Registrar, em cada ponto de feedback, ao menos duas ações específicas diferentes, ou dois históricos diferentes, com o mesmo resultado, cujas mensagens previstas diferem em informação que cita ou descreve o que o jogador fez
- Design: Definir ao menos uma mensagem, em texto ou fala, que o jogo exiba em resposta a uma ação do jogador. Definir, em cada ponto de feedback, mensagens diferentes para ao menos duas ações específicas diferentes, ou dois históricos diferentes, com o mesmo resultado, que difiram em informação que cita ou descreve o que o jogador fez
- Código: Acrescentar ao menos um manipulador de evento (handler) que exiba, em texto ou fala, mensagem de feedback em resposta a uma ação do jogador. Fazer cada ponto de feedback escolher ou montar a mensagem a partir da ação específica (valor escolhido, objeto, resposta) ou do histórico (contadores de tentativas ou de erros, registro de ações anteriores), e não por sorteio nem apenas pelo resultado. Acrescentar, em cada ponto de feedback, ao menos dois ramos, ou um texto que insira o dado da ação, que produzam para o mesmo resultado mensagens que diferem em informação que cita ou descreve o que o jogador fez

**Depende de.** —

### D19 — Os desafios devem proporcionar o desenvolvimento de competências no uso das ferramentas mentais

- Categoria: Mediação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D19.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *objetivo de aprendizagem*: cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados
- *funções psicológicas superiores avaliadas*: cinco, e uma função é exigida por um desafio quando ele não pode ser concluído sem a operação descrita
- *memória*: usar, na ação exigida, informação que o jogo exibiu antes e que deixou de estar visível ou audível no momento da ação
- *atenção voluntária*: identificar, entre dois ou mais estímulos exibidos ao mesmo tempo (objetos, sons ou trechos de texto), o estímulo que a ação correta exige usar, sem que o jogo o destaque ou o indique
- *planejamento*: escolher e ordenar, antes de agir, ao menos duas ações dependentes entre si (a segunda só é possível, ou só tem efeito, depois da primeira), sem que o jogo dite a sequência passo a passo
- *linguagem*: obter de texto ou fala a informação que define qual ação resolve o desafio (e não apenas como operar os controles), ou produzir texto ou fala que o jogo usa ou avalia
- *formação de conceitos*: classificar, comparar ou agrupar objetos, situações ou exemplos segundo um conceito dos objetivos de aprendizagem, ou aplicar esse conceito a um caso novo, de modo que a ação correta depende da propriedade do conceito
- *um elemento por função*: cada função conta por um elemento do desafio próprio dela, e um mesmo elemento não conta para duas funções
- *exigir duas funções*: atender ao teste de duas das cinco funções, cada uma por um elemento diferente do mesmo desafio

**Enunciado.** Cada desafio exige ao menos duas das funções psicológicas superiores memória, atenção voluntária, planejamento, linguagem e formação de conceitos, cada uma por um elemento diferente do desafio

**Justificativa do nível.** essencialidade alta, viabilidade média. Para Vigotski, as funções psicológicas superiores (memória mediada, atenção voluntária, pensamento em conceitos, linguagem, planejamento) se formam pelo uso de instrumentos e signos como mediadores e se desenvolvem na atividade que as exige. Um desafio que pede só reação imediata ou reprodução de uma resposta não exige o uso dessas ferramentas mentais. O limite de duas funções é uma convenção operacional do vygolint: Vigotski trata as funções superiores como sistemas inter-relacionados, e uma função isolada também é exigida por tarefas de reprodução, como memorizar e repetir. Viabilidade média: exige projetar cada desafio com elementos que exijam as funções e registrá-los no GDD.

**Evidência.**
- Código: não se aplica
- Documentação: Listar no GDD ou documento equivalente cada desafio e, para cada função que o documento declara, verificar se ele descreve o elemento do desafio que a exige e se esse elemento atende ao teste da definição; a função só conta se o elemento descrito atende ao teste, e não basta o documento nomear a função. Regra de desempate: se o GDD e o vídeo divergirem sobre um desafio gravado, vale o vídeo, que mostra o desafio como é jogado; desafio não gravado vale pelo GDD, e GDD que não descreve o desafio conta como sem GDD para esse desafio
  - todos os desafios foram listados (mínimo 1)
  - cada desafio listado nomeia ao menos duas funções e descreve, para cada uma, o elemento que a exige (informação exibida e depois ocultada, estímulos simultâneos, ações dependentes, texto ou fala que define a ação, objetos ou exemplos a classificar)
  - o elemento descrito para cada função atende ao teste da definição e não é o mesmo elemento descrito para outra função do mesmo desafio
- Vídeo: Assistir a cada desafio gravado e registrar, com timestamp, os elementos que atendem ao teste de cada função: a informação exibida e depois oculta antes da ação em que é usada, os estímulos simultâneos sem destaque, as ações dependentes sem sequência ditada, o texto ou a fala que define a ação, os objetos ou exemplos a classificar. A classificação depende da estrutura do desafio mostrada na interface, e não do desempenho do jogador gravado. Regra de desempate: se o GDD e o vídeo divergirem sobre um desafio gravado, vale o vídeo, que mostra o desafio como é jogado; desafio não gravado vale pelo GDD, e GDD que não descreve o desafio conta como sem GDD para esse desafio
  - todos os desafios presentes no vídeo foram registrados (mínimo 1)
  - para cada desafio registrado, foram anotados os elementos que atendem ao teste de cada função, com timestamp
  - cada desafio registrado tem elementos diferentes para ao menos duas funções, nos termos da definição

**Escala.**
- Atendido: Todos os desafios documentados ou gravados exigem ao menos duas funções psicológicas superiores, nos termos do enunciado e das definições
- Parcial: Ao menos um desafio documentado ou gravado exige ao menos duas funções psicológicas superiores, nos termos do enunciado e das definições, e ao menos outro exige menos de duas
- Não atendido: Nenhum desafio documentado ou gravado exige ao menos duas funções psicológicas superiores, nos termos do enunciado e das definições

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente cada desafio e ao menos duas das funções psicológicas superiores (memória, atenção voluntária, planejamento, linguagem e formação de conceitos) que o desafio exige. Registrar, para cada uma dessas funções, o elemento do desafio que a exige (informação exibida e depois ocultada, estímulos simultâneos, ações dependentes, texto ou fala que define a ação, objetos ou exemplos a classificar), diferente do elemento de outra função do mesmo desafio
- Design: Incluir, em cada desafio que exige menos de duas funções psicológicas superiores, elementos diferentes que exijam ao menos duas das funções: informação exibida e depois ocultada antes da ação que a usa (memória), estímulos simultâneos sem destaque entre os quais a ação correta exige escolher (atenção voluntária), ações dependentes entre si sem sequência ditada pelo jogo (planejamento), texto ou fala que define qual ação resolve o desafio (linguagem), objetos ou exemplos a classificar segundo um conceito dos objetivos de aprendizagem (formação de conceitos)
- Código: não se aplica

**Depende de.** —

### D20 — O jogo pode fornecer pista para o jogador resolver problemas

- Categoria: Mediação
- Modalidade: pode
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D20.1 — Nível AA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *mecanismo de ajuda*: uma ação explícita do jogador dedicada a obter ajuda (botão ou comando de dica, interação com personagem ou objeto que só oferece ajuda) ou um disparo automático do jogo por critério acumulado (número de tentativas ou tempo sem progresso no desafio) que exibe ao jogador, durante um desafio em curso, informação sobre como resolvê-lo; mensagem exibida em reação a uma única ação incorreta é feedback (D17) e ajuda de outro jogador é tratada em D16, e nenhuma das duas é mecanismo de ajuda
- *solução completa*: a resposta final do desafio ou a sequência inteira de ações que o conclui; a informação de um mecanismo entrega a solução completa quando, depois de exibida, concluir o desafio só exige reproduzi-la, sem nenhuma decisão do jogador (inclui reduzir as opções a uma só e inclui o jogo executar a solução)
- *pista*: a informação de um mecanismo de ajuda que não entrega a solução completa

**Enunciado.** Em ao menos um desafio existe um mecanismo de ajuda que fornece pista, isto é, informação sobre como resolver o desafio que não entrega a solução completa

**Justificativa do nível.** essencialidade média, viabilidade alta. Na zona de desenvolvimento proximal o jogador resolve com ajuda o que ainda não resolve sozinho, e a ajuda cumpre esse papel quando indica um caminho sem realizar a tarefa por ele; uma pista que entrega a resposta substitui a atividade do jogador. A diretriz é opcional na redação de Carvalho (pode), por isso o nível nunca é A, e a essencialidade é média porque outras formas de mediação (D16, D17, D18, D21 e D22) também aproximam o jogador da solução. Botão de dica com um texto por desafio é recurso de baixo custo; viabilidade alta.

**Evidência.**
- Código: Localizar, em cada desafio, botões ou comandos de dica, personagens ou objetos de ajuda e disparos automáticos por contagem de tentativas ou por tempo (contadores de tentativas, temporizadores de inatividade). Para cada mecanismo, ler o conteúdo da informação exibida (texto, imagem, destaque, execução de ações) e verificar se, depois dela, concluir o desafio exige decisão do jogador ou se a informação é a resposta final ou executa a solução (por exemplo, exibe o valor guardado como gabarito, destaca a única opção restante ou aciona as ações finais). Regra de desempate: se o código e o vídeo divergirem sobre um mecanismo, vale o código; o vídeo comprova um mecanismo observado, mas a ausência de mecanismo no vídeo não prova que o jogo não o oferece
  - todos os mecanismos de ajuda foram listados, cada um com o desafio em que ocorre, a forma de acionamento (jogador ou disparo automático) e o critério do disparo, se houver (mínimo 0 mecanismos)
  - a informação exibida por cada mecanismo foi registrada e classificada como pista (concluir o desafio ainda exige decisão do jogador) ou como entrega da solução completa
  - ao menos um mecanismo listado é pista, nos termos da definição (indica o estado atendido); se todos os mecanismos listados entregam a solução completa, indica o estado parcial
- Documentação: não se aplica
- Vídeo: O vídeo só confirma a evidência de código. Observar, em cada desafio gravado, os momentos em que o jogador aciona um mecanismo de ajuda ou o jogo o dispara e o que ocorre depois: se o desafio segue em curso e o jogador ainda precisa decidir, ou se o jogo exibe a resposta final ou executa a solução. Regra de desempate: se o código e o vídeo divergirem sobre um mecanismo, vale o código; o vídeo comprova um mecanismo observado, mas a ausência de mecanismo no vídeo não prova que o jogo não o oferece
  - cada mecanismo de ajuda observado foi registrado com timestamp, forma de acionamento e informação exibida (mínimo 0 mecanismos)
  - para cada mecanismo registrado, foi anotado se o desafio segue em curso e o jogador ainda precisa decidir (pista) ou se o jogo exibe a resposta final ou executa a solução (entrega da solução completa)

**Escala.**
- Atendido: Em ao menos um desafio existe um mecanismo de ajuda cuja informação é pista, nos termos do enunciado e das definições
- Parcial: Existe ao menos um mecanismo de ajuda, mas todos os mecanismos de ajuda existentes entregam a solução completa, nos termos do enunciado e das definições
- Não atendido: Não existe mecanismo de ajuda, nos termos do enunciado e das definições, em nenhum desafio

**Recomendações.**
- Documentação: não se aplica
- Design: Definir, em ao menos um desafio, um mecanismo de ajuda (botão ou comando de dica, personagem ou objeto que só oferece ajuda, ou disparo automático por número de tentativas ou por tempo sem progresso) que exiba informação sobre como resolver o desafio. Definir essa informação de modo que, depois de exibida, concluir o desafio ainda exija decisão do jogador, sem exibir a resposta final, reduzir as opções a uma só nem executar a solução
- Código: Acrescentar, em ao menos um desafio, um botão ou comando de dica, ou um disparo automático por contador de tentativas ou por temporizador de inatividade, que exiba informação sobre como resolver o desafio. Limitar a informação exibida por esse mecanismo de modo que concluir o desafio ainda exija decisão do jogador, sem exibir o valor guardado como gabarito, destacar a única opção restante nem acionar as ações finais

**Depende de.** —

### D21 — O jogo pode fornecer simulações de formas para resolver o problema

- Categoria: Mediação
- Modalidade: pode
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D21.1 — Nível AA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *forma de resolver o desafio*: uma sequência de ações que leva do estado inicial ao objetivo do desafio
- *simulação*: a execução, pelo próprio jogo (personagem, animação ou repetição gravada), de ao menos uma ação de uma forma de resolver o desafio sobre o estado do desafio, com a mudança de estado visível ao jogador, acionada pelo jogador ou exibida pelo jogo antes ou durante o desafio; descrição por texto ou imagem estática, sem execução de ações, é pista (D20) e não é simulação, e a demonstração de como operar os controles, sem avançar o estado do desafio rumo ao objetivo, também não é simulação
- *simulação substitui a ação do jogador*: quando, ao fim dela, o jogo registra o desafio como concluído (concede conclusão, pontuação ou progresso do desafio) sem que o jogador tenha agido, ou o jogador não pode mais jogar o desafio depois dela

**Enunciado.** Em ao menos um desafio existe uma simulação de uma forma de resolver o desafio que não substitui a ação do jogador, isto é, depois dela o desafio continua a ser resolvido pelas ações do jogador

**Justificativa do nível.** essencialidade média, viabilidade média. Para Vigotski, na zona de desenvolvimento proximal o aprendiz realiza por imitação, ou em colaboração, o que ainda não realiza sozinho, e ver uma forma de resolução executada é o apoio que a imitação pressupõe. Se a simulação conclui o desafio pelo jogador, a imitação não ocorre e a atividade é substituída. A diretriz é opcional na redação de Carvalho (pode), por isso o nível nunca é A, e a essencialidade é média porque outras formas de mediação (D16 a D20 e D22) também apoiam a resolução. Viabilidade média: exige criar, por desafio, uma execução automática ou animada de ações, mais custosa que um texto de dica.

**Evidência.**
- Código: Localizar modos de demonstração, repetições gravadas, tutoriais animados, personagens ou rotinas que executam as ações de um desafio (por exemplo, chamadas automáticas das mesmas funções que as ações do jogador executam). Verificar se o estado do desafio muda durante a execução, se ao fim é chamada a rotina que registra conclusão, pontuação ou progresso do desafio e se o jogador pode jogar o desafio depois. Regra de desempate: se as fontes divergirem sobre uma simulação, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a simulação conta como sem código para essa simulação, e GDD que não a descreve conta como sem GDD para essa simulação; a ausência de simulação no vídeo não prova que o jogo não a oferece
  - todas as simulações foram listadas, cada uma com o desafio em que ocorre e a forma de acionamento (mínimo 0 simulações)
  - cada simulação listada executa ao menos uma ação sobre o estado do desafio, e não apenas texto, imagem estática ou demonstração dos controles
  - ao menos uma simulação listada não chama, ao fim, a rotina que registra a conclusão, a pontuação ou o progresso do desafio, e o jogador pode jogar o desafio depois dela (indica o estado atendido); se todas as simulações listadas a chamam ou impedem jogar o desafio depois, indica o estado parcial
- Documentação: Verificar no documento de design (GDD) ou documento equivalente a descrição de modo de demonstração, repetição gravada ou tutorial animado de um desafio: quando é acionado, qual forma de resolver é mostrada e o que acontece com o desafio depois. Regra de desempate: se as fontes divergirem sobre uma simulação, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a simulação conta como sem código para essa simulação, e GDD que não a descreve conta como sem GDD para essa simulação; a ausência de simulação no vídeo não prova que o jogo não a oferece
  - o GDD descreve, por desafio, a simulação, a forma de acionamento e a ação executada sobre o estado do desafio (mínimo 0 simulações)
  - o GDD declara, para cada simulação descrita, se o jogo registra o desafio como concluído ao fim dela e se o jogador pode jogar o desafio depois
  - ao menos uma simulação descrita não registra a conclusão e permite jogar o desafio depois (indica o estado atendido); se todas registram a conclusão ou impedem jogar o desafio depois, indica o estado parcial
- Vídeo: O vídeo só confirma a evidência de código ou do GDD: a ausência de simulação no vídeo não prova que o jogo não a oferece. Registrar os momentos em que uma simulação é exibida e anotar se o estado do desafio muda durante ela, se pontuação, conclusão ou progresso do desafio mudam ao fim dela e se o jogador passa a controlar o desafio depois. Regra de desempate: se as fontes divergirem sobre uma simulação, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a simulação conta como sem código para essa simulação, e GDD que não a descreve conta como sem GDD para essa simulação; a ausência de simulação no vídeo não prova que o jogo não a oferece
  - cada simulação observada foi registrada com timestamp, forma de acionamento e ação executada sobre o estado do desafio (mínimo 0 simulações)
  - ao fim de cada simulação registrada, foi anotado se conclusão, pontuação ou progresso do desafio mudam sem que o jogador tenha agido
  - depois de cada simulação registrada, foi anotado se o jogador passa a controlar o desafio

**Escala.**
- Atendido: Em ao menos um desafio existe uma simulação que não substitui a ação do jogador, nos termos do enunciado e das definições
- Parcial: Existe ao menos uma simulação, mas todas as simulações existentes substituem a ação do jogador, nos termos do enunciado e das definições
- Não atendido: Não existe simulação, nos termos do enunciado e das definições, em nenhum desafio

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente, para cada desafio com simulação, a simulação, a forma de acionamento e a ação executada sobre o estado do desafio. Registrar que, ao fim de ao menos uma simulação, o jogo não registra a conclusão do desafio e o jogador pode jogar o desafio depois
- Design: Definir, em ao menos um desafio, uma simulação em que o próprio jogo (personagem, animação ou repetição gravada) executa ao menos uma ação de uma forma de resolver o desafio, com a mudança no estado do desafio visível ao jogador. Definir que, ao fim dessa simulação, o jogo não registre conclusão, pontuação ou progresso do desafio e que o jogador possa jogar o desafio em seguida
- Código: Acrescentar, em ao menos um desafio, uma rotina de demonstração que execute, chamando as mesmas funções que as ações do jogador executam, ao menos uma ação de uma forma de resolver o desafio, com a mudança no estado do desafio visível ao jogador. Fazer essa rotina terminar sem chamar a rotina que registra conclusão, pontuação ou progresso do desafio. Devolver ao jogador o controle do desafio ao fim da rotina de demonstração

**Depende de.** —

### D22 — O jogo, quando aplicado em sala de aula, cria oportunidades para o professor atuar como mediador / facilitador

- Categoria: Mediação
- Modalidade: deve
- Aplicabilidade: Somente quando o jogo é aplicado em sala de aula
- Fonte: Carvalho (2020), Quadro 3

#### D22.1 — Nível AA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *objetivo de aprendizagem*: cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados
- *documentação*: o GDD ou documento equivalente
- *intervenção do professor*: uma ação do professor sobre os jogadores durante a sessão, em sala de aula, dentro ou fora do jogo, presencialmente ou por qualquer canal (perguntar, explicar, orientar ou discutir o resultado), e não exige canal de comunicação dentro do jogo (D06 e D07)
- *momento de mediação*: um ponto da sessão que a documentação identifica (por exemplo, ao falhar no desafio, ao concluí-lo ou em pausa indicada), com a intervenção do professor prevista nesse ponto e o objetivo de aprendizagem que a intervenção trabalha; descrição que cite só o ponto, sem a intervenção do professor ou sem o objetivo de aprendizagem, não é momento de mediação

**Enunciado.** A documentação descreve, para cada desafio, ao menos um momento de mediação, isto é, um ponto da sessão com a intervenção do professor prevista e o objetivo de aprendizagem que ela trabalha

**Justificativa do nível.** essencialidade média, viabilidade alta. Na zona de desenvolvimento proximal, o professor é o outro mais experiente que ajusta o apoio ao que o aluno ainda não faz sozinho, e a mediação fora do jogo é a leitura de D22 adotada também em D06. A exigência de um momento por desafio é uma convenção operacional do vygolint: cada desafio tem objetivo de aprendizagem e dificuldade próprios, e uma intervenção descrita para um desafio não prevê a ajuda de que outro precisa. A essencialidade é média porque o jogo também medeia por si (D17 a D21). Escrever momentos de intervenção em um guia ou no GDD não exige mudança no jogo; viabilidade alta.

**Evidência.**
- Código: não se aplica
- Documentação: Listar os desafios descritos na documentação e, para cada um, localizar os momentos de mediação descritos, verificando os três elementos de cada momento: o ponto da sessão, a intervenção do professor e o objetivo de aprendizagem
  - todos os desafios descritos na documentação foram listados (mínimo 1)
  - cada desafio listado tem ao menos um momento de mediação descrito com os três elementos: ponto da sessão, intervenção do professor e objetivo de aprendizagem
  - o objetivo de aprendizagem citado em cada momento de mediação consta da lista de objetivos de aprendizagem da documentação
- Vídeo: não se aplica

**Escala.**
- Atendido: Todos os desafios descritos na documentação têm ao menos um momento de mediação, nos termos do enunciado e das definições
- Parcial: Ao menos um desafio descrito na documentação tem ao menos um momento de mediação, nos termos do enunciado e das definições, e ao menos outro desafio não tem
- Não atendido: Nenhum desafio descrito na documentação tem momento de mediação, nos termos do enunciado e das definições

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente, para cada desafio, ao menos um momento de mediação com o ponto da sessão, a intervenção do professor prevista nesse ponto e o objetivo de aprendizagem que essa intervenção trabalha, escolhido da lista de objetivos de aprendizagem do documento
- Design: Definir, para cada desafio, ao menos um ponto da sessão em sala de aula (ao falhar no desafio, ao concluí-lo ou em pausa indicada) em que o professor intervém. Definir, para cada um desses pontos, a intervenção do professor (perguntar, explicar, orientar ou discutir o resultado) e o objetivo de aprendizagem que essa intervenção trabalha
- Código: não se aplica

**Depende de.** —

#### D22.2 — Nível AAA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *documentação*: o GDD ou documento equivalente
- *recurso de acompanhamento do professor*: uma tela, painel ou relatório (exibido no jogo ou em outra ferramenta, ou exportado em arquivo) destinado ao professor, e não ao jogador, que mostra dados por jogador ou por grupo, e não apenas agregados da turma
- *resultado por desafio*: o registro de se o jogador ou o grupo concluiu cada desafio
- *dado de dificuldade*: o número de tentativas, a lista de erros ou o tempo gasto em cada desafio

**Enunciado.** O jogo oferece ao professor um recurso de acompanhamento que mostra, por jogador ou por grupo, o resultado por desafio e ao menos um dado de dificuldade

**Justificativa do nível.** essencialidade média, viabilidade baixa. A mediação do professor na zona de desenvolvimento proximal depende de saber o que cada aluno já faz sozinho e onde precisa de ajuda; com uma turma inteira jogando, o professor não observa cada jogador, e um registro de resultado e de dificuldade por desafio indica onde intervir. A essencialidade é média porque o professor pode mediar por observação direta, que D22.1 já trata. Viabilidade baixa: exige guardar registros por jogador além da sessão e uma tela ou exportação própria para o professor, que a maioria dos jogos educacionais não tem.

**Evidência.**
- Código: Procurar telas, rotas, funções ou exportações restritas ao professor (perfil de professor, senha ou modo docente) que leiam registros por jogador ou por grupo, e listar os campos que elas exibem ou exportam. Verificar se há resultado por desafio e ao menos um dado de dificuldade por jogador ou grupo. Regra de desempate: se o código e a documentação divergirem sobre o recurso, vale o código; sem código, a documentação; código que existe mas não traz dado sobre o recurso conta como sem código para esse recurso, e documentação que não o descreve conta como sem documentação para esse recurso
  - o recurso de acompanhamento foi localizado, com a tela, rota, função ou exportação que o implementa e a restrição de acesso ao professor (mínimo 0 recursos)
  - o recurso lista dados por jogador ou por grupo, e não apenas agregados da turma
  - o recurso lista o resultado por desafio e ao menos um dado de dificuldade (indica o estado atendido); se lista só um dos dois, indica o estado parcial
- Documentação: Verificar na documentação a descrição de tela, painel ou relatório para o professor e dos campos que ele traz por jogador ou por grupo. Regra de desempate: se o código e a documentação divergirem sobre o recurso, vale o código; sem código, a documentação; código que existe mas não traz dado sobre o recurso conta como sem código para esse recurso, e documentação que não o descreve conta como sem documentação para esse recurso
  - a documentação descreve o recurso de acompanhamento, quem o acessa e como é acessado (mínimo 0 recursos)
  - a documentação lista os campos do recurso e indica que são por jogador ou por grupo
  - os campos listados incluem o resultado por desafio e ao menos um dado de dificuldade (indica o estado atendido); se incluem só um dos dois, indica o estado parcial
- Vídeo: não se aplica

**Escala.**
- Atendido: O jogo oferece recurso de acompanhamento do professor que mostra, por jogador ou por grupo, o resultado por desafio e ao menos um dado de dificuldade, nos termos do enunciado e das definições
- Parcial: O jogo oferece recurso de acompanhamento do professor que mostra dados por jogador ou por grupo e inclui o resultado por desafio ou um dado de dificuldade, mas não os dois, nos termos do enunciado e das definições
- Não atendido: O jogo não oferece recurso de acompanhamento do professor, ou o recurso mostra apenas agregados da turma, ou mostra dados por jogador ou por grupo sem resultado por desafio nem dado de dificuldade, nos termos do enunciado e das definições

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente o recurso de acompanhamento do professor, quem o acessa e como é acessado. Registrar os campos do recurso, indicando que são por jogador ou por grupo e que incluem o resultado por desafio e ao menos um dado de dificuldade (número de tentativas, lista de erros ou tempo gasto em cada desafio)
- Design: Definir uma tela, painel ou relatório destinado ao professor que mostre, por jogador ou por grupo, e não apenas em agregados da turma, o resultado por desafio e ao menos um dado de dificuldade (número de tentativas, lista de erros ou tempo gasto em cada desafio)
- Código: Acrescentar uma tela, rota, função ou exportação com acesso restrito ao professor (perfil de professor, senha ou modo docente). Gravar, por jogador ou por grupo, o resultado por desafio e ao menos um dado de dificuldade (número de tentativas, lista de erros ou tempo gasto em cada desafio). Exibir ou exportar nesse recurso esses dados por jogador ou por grupo, e não apenas agregados da turma

**Depende de.** —

### D23 — A narrativa do jogo deve viabilizar reflexões críticas ao trabalhar os conteúdos

- Categoria: Mediação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D23.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *objetivo de aprendizagem*: cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados
- *narrativa*: a sequência de eventos, cenas, personagens e diálogos que o jogo apresenta ao jogador
- *conteúdo de aprendizagem*: o listado no documento de design (GDD) ou documento equivalente
- *situação trata de um objetivo de aprendizagem*: quando o texto, a fala ou a cena da situação cita ou descreve conceito, fato ou procedimento listado entre os objetivos de aprendizagem
- *posição*: uma opção ou resposta (escolhida ou digitada) do jogador, numa situação, que o jogo não avalia como certa ou errada, isto é, que não concede, retira nem condiciona pontuação, progresso ou conclusão do desafio conforme a opção ou resposta; alternativa que o jogo avalia como certa ou errada é múltipla escolha e não é posição
- *consequência narrativa*: o evento, a fala de personagem ou a mudança no cenário ou na história, exibido depois da posição, que retoma ou depende da posição escolhida (no código ou no GDD, um ramo diferente para cada posição; no vídeo, conteúdo exibido que cita ou responde à posição escolhida)
- *dilema*: uma situação da narrativa que trata de um objetivo de aprendizagem, em que o jogador toma uma posição entre ao menos duas e o jogo usa a posição tomada para exibir a consequência narrativa dela
- *cenário* (sentido corrente): em «mudança no cenário ou na história» (local consequência narrativa), cenário está no sentido corrente de ambientação da história, e não no de cenário jogável (D29)

**Enunciado.** A narrativa apresenta ao menos um dilema, isto é, uma situação sobre o conteúdo em que o jogador toma uma posição entre ao menos duas e o jogo exibe a consequência narrativa da posição tomada

**Justificativa do nível.** essencialidade alta, viabilidade média. Para Vigotski, os conceitos científicos se formam quando o sujeito os opera de modo consciente e deliberado, e não quando os recebe prontos. Uma narrativa que só informa o conteúdo mantém o jogador como receptor, enquanto um dilema o obriga a tomar posição sobre o conteúdo e a ver o resultado dessa posição, o que torna o conteúdo objeto de reflexão. Basta um dilema porque a diretriz exige que a narrativa viabilize a reflexão, e não que toda cena a produza; exigir todas as cenas dependeria de delimitar o que é uma cena. Viabilidade média: exige escrever ramos de história com consequências diferentes e ligá-los aos objetivos de aprendizagem.

**Evidência.**
- Código: Localizar os pontos da narrativa em que o jogador escolhe ou digita uma opção (menus de diálogo, escolhas de história, respostas abertas) e, em cada um, verificar quais objetivos de aprendizagem a situação cita, se a escolha altera pontuação, progresso ou conclusão do desafio, e se há ramo, variável ou evento diferente para cada opção que decide a consequência exibida. Regra de desempate: se as fontes divergirem sobre uma situação, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a situação conta como sem código para essa situação, e GDD que não a descreve conta como sem GDD para essa situação
  - todos os pontos da narrativa com escolha ou resposta do jogador foram listados, cada um com o objetivo de aprendizagem a que se refere (mínimo 0 pontos)
  - em ao menos um ponto listado, o jogo não avalia as opções como certas ou erradas, isto é, a escolha não concede, retira nem condiciona pontuação, progresso ou conclusão do desafio
  - no mesmo ponto, a escolha do jogador é guardada ou lida pelo jogo e decide um ramo, variável ou evento diferente para cada posição, que exibe a consequência narrativa
- Documentação: Verificar no GDD ou documento equivalente a descrição da narrativa e identificar as situações em que o jogador toma posição: o objetivo de aprendizagem tratado, as posições possíveis, se alguma é avaliada como certa ou errada e a consequência narrativa prevista para cada posição. Regra de desempate: se as fontes divergirem sobre uma situação, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a situação conta como sem código para essa situação, e GDD que não a descreve conta como sem GDD para essa situação
  - o GDD lista as situações da narrativa em que o jogador toma posição, cada uma com o objetivo de aprendizagem tratado (mínimo 0 situações)
  - em ao menos uma situação listada, o GDD descreve ao menos duas posições que o jogo não avalia como certas ou erradas
  - na mesma situação, o GDD descreve uma consequência narrativa diferente para cada posição
- Vídeo: O vídeo só confirma a evidência de código ou do GDD: mostra a opção escolhida e sua consequência, mas não mostra se as outras opções levariam a consequências diferentes, e a ausência de dilema no vídeo não prova que o jogo não o oferece. Registrar as situações da narrativa em que o jogador escolhe ou digita uma opção, as opções visíveis, o que o jogo exibe depois da escolha e se a situação cita objetivo de aprendizagem. Regra de desempate: se as fontes divergirem sobre uma situação, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a situação conta como sem código para essa situação, e GDD que não a descreve conta como sem GDD para essa situação
  - todas as situações da narrativa gravadas em que o jogador escolhe ou digita uma opção foram registradas com timestamp, opções visíveis e objetivo de aprendizagem a que se referem (mínimo 0 situações)
  - em ao menos uma situação registrada, as opções são ao menos duas, e depois da escolha o jogo não exibe sinal de certo ou errado nem muda pontuação, progresso ou conclusão do desafio
  - na mesma situação, o conteúdo exibido depois da escolha cita ou responde à posição escolhida

**Escala.**
- Atendido: A narrativa apresenta ao menos um dilema, nos termos do enunciado e das definições
- Parcial: A narrativa apresenta ao menos uma situação sobre objetivo de aprendizagem em que o jogador escolhe entre ao menos duas opções, mas nenhuma situação é dilema, nos termos do enunciado e das definições (as opções são avaliadas como certas ou erradas, ou a consequência exibida não depende da opção escolhida)
- Não atendido: A narrativa não apresenta nenhuma situação sobre objetivo de aprendizagem em que o jogador escolha entre ao menos duas opções, nos termos do enunciado e das definições (inclui narrativa sem escolha do jogador e narrativa que não trata do conteúdo)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente as situações da narrativa em que o jogador toma posição, cada uma com o objetivo de aprendizagem tratado. Registrar, em ao menos uma dessas situações, ao menos duas posições que o jogo não avalia como certas ou erradas e uma consequência narrativa diferente para cada posição
- Design: Definir ao menos uma situação da narrativa que cite ou descreva um objetivo de aprendizagem e ofereça ao jogador ao menos duas opções. Definir que nenhuma dessas opções seja avaliada como certa ou errada, isto é, que a escolha não conceda, retire nem condicione pontuação, progresso ou conclusão do desafio. Definir, para cada opção, uma consequência narrativa diferente (evento, fala de personagem ou mudança na história) que retome a opção escolhida
- Código: Acrescentar ou usar, em ao menos um ponto da narrativa que cite ou descreva um objetivo de aprendizagem, um menu de diálogo, escolha de história ou resposta aberta com ao menos duas opções. Remover dessa escolha qualquer efeito que conceda, retire ou condicione pontuação, progresso ou conclusão do desafio conforme a opção. Guardar em uma variável a opção escolhida pelo jogador. Acrescentar, para cada opção, um ramo ou evento que leia essa variável e exiba uma consequência narrativa diferente

**Depende de.** —

### D24 — O jogador decide quais recursos utilizar

- Categoria: Autonomia
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D24.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *recurso*: um objeto, ferramenta, item, habilidade ou abordagem (conjunto de ações) que o jogador seleciona por uma ação explícita (menu, inventário, atalho ou interação) para agir no desafio e cuja seleção muda as ações que ele executa ou o efeito delas; escolha só de aparência (cor, avatar) não é recurso, e alternativa de resposta de pergunta (múltipla escolha ou resposta digitada) não é recurso, pois é a própria resposta e não um meio de chegar a ela
- *recursos disponíveis ao mesmo tempo*: recursos que o jogador pode selecionar em um mesmo estado do desafio
- *recursos alternativos válidos*: dois ou mais recursos tais que cada um, usado sem os demais, permite satisfazer a mesma condição de conclusão do desafio; escolher entre desafios diferentes é tratado em D03 e acessar conteúdo opcional, dispensável para concluir a missão, é tratado em D25, e nenhum dos dois é escolha de recurso

**Enunciado.** Em ao menos um desafio o jogador escolhe qual usar entre dois ou mais recursos alternativos válidos disponíveis ao mesmo tempo

**Justificativa do nível.** essencialidade alta, viabilidade alta. Para Vigotski a atividade humana é mediada por instrumentos, e o sujeito se apropria deles ao escolhê-los e usá-los para resolver a tarefa; quando o jogo prescreve um único recurso, a escolha do meio de ação permanece com o sistema. A diretriz trata de meios alternativos para o mesmo desafio, e por isso é distinta de D03.1 (escolha da ordem entre atividades) e de D25 (escolha de conteúdo opcional, dispensável para a missão). Basta um segundo recurso válido em um desafio, decisão de projeto de baixo custo; viabilidade alta.

**Evidência.**
- Código: Localizar, em cada desafio, os recursos que o jogador pode selecionar (inventário, menus de ferramentas, atalhos, objetos interativos, seleção de abordagem) e, para cada um, os manipuladores de evento (handlers) e as condições que levam à conclusão do desafio; verificar se a condição de conclusão pode ser satisfeita por mais de um recurso, cada um sozinho, e se a seleção do recurso depende de entrada do jogador. Regra de desempate: se as fontes divergirem sobre um desafio, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um desafio conta como sem código para esse desafio, e GDD que não descreve um desafio conta como sem GDD para esse desafio
  - todos os desafios foram listados, cada um com os recursos que o jogador pode selecionar e a indicação de quais estão disponíveis ao mesmo tempo (mínimo 0 desafios)
  - em ao menos um desafio listado, dois ou mais recursos disponíveis ao mesmo tempo levam, cada um sozinho, à mesma condição de conclusão do desafio, sem exigir o uso dos demais (indica o estado atendido)
  - nesse desafio, a seleção do recurso é feita por ação explícita do jogador, e não definida automaticamente pelo jogo
  - se existe desafio com dois ou mais recursos disponíveis ao mesmo tempo e em nenhum desses desafios dois recursos diferentes levam, cada um sozinho, à conclusão, anotar (indica o estado parcial; inclui o caso em que apenas um recurso conclui o desafio e o caso em que nenhum conclui sozinho e a conclusão exige a combinação de recursos, como chave e alavanca)
- Documentação: Verificar no GDD ou documento equivalente, para cada desafio, os recursos oferecidos ao jogador, se estão disponíveis ao mesmo tempo, se cada um permite concluir o desafio sozinho e se é o jogador quem seleciona. Regra de desempate: se as fontes divergirem sobre um desafio, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um desafio conta como sem código para esse desafio, e GDD que não descreve um desafio conta como sem GDD para esse desafio
  - o GDD lista os desafios com os recursos que o jogador pode selecionar em cada um (mínimo 0 desafios)
  - em ao menos um desafio, o GDD descreve dois ou mais recursos disponíveis ao mesmo tempo e descreve que cada um permite concluir o desafio sem os demais (indica o estado atendido)
  - no mesmo desafio, o GDD descreve que o jogador seleciona o recurso
  - se o GDD descreve desafio com dois ou mais recursos disponíveis ao mesmo tempo e em nenhum desses desafios descreve dois recursos diferentes que concluem o desafio, cada um sozinho, anotar (indica o estado parcial; inclui o caso em que apenas um recurso conclui o desafio e o caso em que nenhum conclui sozinho e a conclusão exige a combinação de recursos, como chave e alavanca)
- Vídeo: O vídeo só confirma a evidência de código ou do GDD: mostra o que a interface oferece e o recurso que o jogador gravado seleciona, mas não mostra que um recurso não usado também conclui o desafio, e a ausência de escolha no vídeo não prova que o jogo não a oferece. Registrar, em cada desafio gravado, os recursos que a interface oferece ao mesmo tempo, o recurso que o jogador seleciona e como o desafio termina. Regra de desempate: se as fontes divergirem sobre um desafio, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um desafio conta como sem código para esse desafio, e GDD que não descreve um desafio conta como sem GDD para esse desafio
  - cada desafio gravado foi registrado com timestamp e com os recursos que a interface oferece ao mesmo tempo (mínimo 0 desafios)
  - em ao menos um desafio registrado, a interface oferece dois ou mais recursos ao mesmo tempo e o jogador seleciona um deles
  - o vídeo confirma que dois recursos são alternativos válidos quando o mesmo desafio é concluído com recursos diferentes, na mesma gravação ou em gravações distintas; o desafio concluído com um só recurso confirma apenas que esse recurso é válido

**Escala.**
- Atendido: Em ao menos um desafio o jogador escolhe qual usar entre dois ou mais recursos alternativos válidos disponíveis ao mesmo tempo, nos termos do enunciado e das definições
- Parcial: Existe ao menos um desafio com dois ou mais recursos disponíveis ao mesmo tempo, mas em nenhum desses desafios dois recursos alternativos válidos levam à conclusão isoladamente, nos termos do enunciado e das definições (inclui o desafio em que apenas um dos recursos conclui o desafio e o desafio em que nenhum recurso o conclui sozinho e a conclusão exige a combinação de recursos)
- Não atendido: Em nenhum desafio o jogador escolhe entre dois ou mais recursos disponíveis ao mesmo tempo, nos termos do enunciado e das definições (inclui desafio com recurso único e desafio em que o jogo impõe o recurso)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a lista de desafios com os recursos que o jogador pode selecionar em cada um. Registrar, em ao menos um desafio, dois ou mais recursos disponíveis ao mesmo tempo, que cada um desses recursos permite concluir o desafio sem os demais e que o jogador seleciona o recurso
- Design: Definir, em ao menos um desafio, dois ou mais recursos disponíveis ao mesmo tempo que levem, cada um sozinho, à mesma condição de conclusão do desafio, sem exigir o uso dos demais. Definir que o jogador selecione o recurso nesse desafio por ação explícita (menu, inventário, atalho ou interação), e não que o jogo o imponha
- Código: Acrescentar, em ao menos um desafio, recursos selecionáveis até que dois ou mais estejam disponíveis no mesmo estado do desafio. Alterar a condição de conclusão desse desafio para que seja satisfeita por cada um desses recursos sozinho, sem exigir o uso dos demais. Determinar o recurso usado nesse desafio pela entrada do jogador (menu, inventário, atalho ou interação), e não por seleção automática do jogo

**Depende de.** —

### D25 — O jogador decide, com base em seus interesses e motivações, qual conteúdo explorar

- Categoria: Autonomia
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D25.1 — Nível AA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *caminho obrigatório (caminho da missão)*: a sequência de objetivos exigidos para completar a missão em curso, e fora do caminho obrigatório é tudo o que nenhum desses objetivos exige
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *objetivo de aprendizagem*: cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados
- *conteúdo opcional*: uma parte do jogo (missão secundária, minijogo, texto, glossário, objeto ou área) que trata de um objetivo de aprendizagem, isto é, cita ou descreve conceito, fato ou procedimento listado entre os objetivos de aprendizagem, e cujo acesso nenhum objetivo do caminho da missão em curso exige, de modo que o jogador conclui a missão sem acessá-lo
- *conteúdos opcionais disponíveis ao mesmo tempo*: conteúdos opcionais que o jogador pode acessar em um mesmo estado do jogo, por ação própria (menu, interação ou deslocamento) e não por disparo automático; escolher a ordem de atividades obrigatórias é tratado em D03 e escolher entre recursos para o mesmo desafio é tratado em D24, e nenhum dos dois é escolha de conteúdo opcional

**Enunciado.** Existem ao menos dois conteúdos opcionais disponíveis ao mesmo tempo que tratam de objetivos de aprendizagem diferentes, de modo que o jogador escolhe qual explorar

**Justificativa do nível.** essencialidade média, viabilidade média. Em Vigotski a motivação é função da atividade: o sentido que o jogador atribui ao que faz orienta sua ação, e escolher o que explorar permite que o interesse dirija a atividade em vez de ser dirigido apenas pelo jogo. A essencialidade é média por este argumento: a escolha de meios (D24) e de ordem das atividades (D03.1) já dá ao jogador autonomia sobre como e quando agir dentro da atividade obrigatória, e a escolha de conteúdo opcional acrescenta autonomia sobre o que explorar, mas incide sobre conteúdo dispensável para a missão, de modo que a atividade exigida ocorre sem ela. Exigem-se dois conteúdos opcionais sobre objetivos diferentes porque, com um só, o jogador decide apenas explorar ou não, e não qual conteúdo explorar; o critério verifica a existência da escolha, e não os interesses do jogador, que variam. Por esse mesmo limite D25 não se confunde com D03.1 (ordem entre atividades obrigatórias) nem com D24 (meios para o mesmo desafio). Produzir conteúdo além do exigido pela missão tem custo de roteiro e de arte; viabilidade média.

**Evidência.**
- Código: Localizar as partes do jogo acessíveis fora do caminho da missão (missões secundárias, minijogos, textos, glossários, objetos e áreas) e, para cada uma, o objetivo de aprendizagem que trata, o que a libera e se alguma condição de conclusão da missão em curso lê o acesso a ela. Regra de desempate: se as fontes divergirem sobre um conteúdo, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um conteúdo conta como sem código para esse conteúdo, e GDD que não descreve um conteúdo conta como sem GDD para esse conteúdo
  - todas as partes do jogo acessíveis fora do caminho da missão foram listadas, cada uma com o objetivo de aprendizagem que trata, ou com a anotação nenhum quando não trata objetivo listado, caso em que a parte não é conteúdo opcional (mínimo 0 partes)
  - nenhuma condição de conclusão da missão em curso lê o acesso a essas partes, de modo que são conteúdos opcionais, nos termos da definição
  - ao menos dois conteúdos opcionais que tratam de objetivos de aprendizagem diferentes podem ser acessados em um mesmo estado do jogo, por ação do jogador (indica o estado atendido)
  - se existe ao menos um conteúdo opcional e nenhum par de conteúdos opcionais que tratam de objetivos de aprendizagem diferentes pode ser acessado em um mesmo estado do jogo, anotar (indica o estado parcial; inclui um só conteúdo opcional, conteúdos opcionais que tratam de um único objetivo de aprendizagem e conteúdos opcionais de objetivos diferentes que nunca estão disponíveis ao mesmo tempo)
- Documentação: Verificar no GDD ou documento equivalente os objetivos de aprendizagem e as partes do jogo descritas como não exigidas pelo caminho da missão, o objetivo que cada uma trata e a forma de acesso. Regra de desempate: se as fontes divergirem sobre um conteúdo, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um conteúdo conta como sem código para esse conteúdo, e GDD que não descreve um conteúdo conta como sem GDD para esse conteúdo
  - o GDD lista os objetivos de aprendizagem e as partes do jogo que o caminho da missão não exige, cada uma com o objetivo de aprendizagem que trata, ou com a anotação nenhum quando não trata objetivo listado, caso em que a parte não é conteúdo opcional (mínimo 0 partes)
  - o GDD descreve ao menos dois conteúdos opcionais que tratam de objetivos de aprendizagem diferentes, acessíveis ao mesmo tempo por ação do jogador (indica o estado atendido)
  - o GDD descreve que a missão se conclui sem acessar esses conteúdos
  - se o GDD descreve ao menos um conteúdo opcional e nenhum par de conteúdos opcionais que tratam de objetivos de aprendizagem diferentes acessíveis em um mesmo estado do jogo, anotar (indica o estado parcial; inclui um só conteúdo opcional, conteúdos opcionais que tratam de um único objetivo de aprendizagem e conteúdos opcionais de objetivos diferentes que nunca estão disponíveis ao mesmo tempo)
- Vídeo: O vídeo só confirma a evidência de código ou do GDD: mostra o que a interface oferece, mas não mostra se a missão exigia o conteúdo, e a ausência de conteúdo opcional no vídeo não prova que o jogo não o oferece. Registrar os conteúdos que a interface oferece fora do caminho da missão, o objetivo de aprendizagem que cada um trata e a forma de acesso. Regra de desempate: se as fontes divergirem sobre um conteúdo, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um conteúdo conta como sem código para esse conteúdo, e GDD que não descreve um conteúdo conta como sem GDD para esse conteúdo
  - cada conteúdo oferecido fora do caminho da missão foi registrado com timestamp, objetivo de aprendizagem que trata e forma de acesso (mínimo 0 conteúdos)
  - em ao menos um ponto gravado, a interface oferece ao mesmo tempo o acesso a dois ou mais conteúdos que tratam de objetivos de aprendizagem diferentes
  - o vídeo confirma que um conteúdo é opcional quando mostra a missão em curso concluída sem que o jogador o tenha acessado, estando ele oferecido pela interface; a ausência dessa conclusão no vídeo não prova que o conteúdo seja exigido

**Escala.**
- Atendido: Existem ao menos dois conteúdos opcionais disponíveis ao mesmo tempo que tratam de objetivos de aprendizagem diferentes, nos termos do enunciado e das definições
- Parcial: Existe ao menos um conteúdo opcional, mas não existem dois conteúdos opcionais disponíveis ao mesmo tempo que tratem de objetivos de aprendizagem diferentes, nos termos do enunciado e das definições (inclui um só conteúdo opcional, conteúdos opcionais que tratam de um único objetivo de aprendizagem e conteúdos opcionais de objetivos diferentes que nunca estão disponíveis ao mesmo tempo)
- Não atendido: Não existe nenhum conteúdo opcional, nos termos do enunciado e das definições (inclui o jogo em que todo conteúdo é exigido pelo caminho da missão e o jogo em que as partes não exigidas pelo caminho não tratam de nenhum objetivo de aprendizagem listado)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a lista de objetivos de aprendizagem e as partes do jogo que o caminho da missão não exige, cada uma com o objetivo de aprendizagem que trata. Registrar ao menos dois desses conteúdos opcionais, de objetivos de aprendizagem diferentes, acessíveis ao mesmo tempo por ação do jogador. Registrar que a missão se conclui sem acessar esses conteúdos opcionais
- Design: Incluir conteúdos opcionais (missão secundária, minijogo, texto, glossário, objeto ou área) até que existam ao menos dois que tratem de objetivos de aprendizagem diferentes, sem que nenhum objetivo do caminho da missão exija o acesso a eles. Definir um mesmo estado do jogo em que o jogador acesse esses dois conteúdos opcionais por ação própria (menu, interação ou deslocamento), e não por disparo automático
- Código: Acrescentar, fora do caminho da missão, as partes do jogo (missão secundária, minijogo, texto, glossário, objeto ou área) que faltarem para que existam ao menos dois conteúdos opcionais que tratem de objetivos de aprendizagem diferentes. Remover das condições de conclusão da missão em curso a leitura do acesso a esses conteúdos opcionais. Alterar as condições de liberação desses conteúdos opcionais para que fiquem acessíveis em um mesmo estado do jogo por ação do jogador (menu, interação ou deslocamento), e não por disparo automático

**Depende de.** —

### D26 — O jogo deve aproximar os jogadores pela competição

- Categoria: Socialização
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D26.1 — Nível AAA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *jogador*: uma pessoa que joga, e personagem não jogável não conta
- *resultado*: uma medida que o jogo atribui a cada jogador (pontuação, tempo, posição, quantidade de itens ou de desafios concluídos) e, quando o jogo atribui a medida a uma equipe identificada (nome, cor ou número) de dois ou mais jogadores, o resultado da equipe a que o jogador pertence conta como resultado desse jogador
- *competição*: uma regra do jogo que compara os resultados de dois ou mais jogadores diferentes, na mesma sessão ou em sessões diferentes, para determinar qual tem o melhor resultado (ranking, placar ou disputa); a comparação entre o resultado do jogador e o resultado anterior dele mesmo, ou o de personagem não jogável, não é competição
- *comparação visível*: aquela em que alguma tela do jogo mostra ao jogador o resultado de ao menos um outro jogador identificado (nome, apelido ou número) junto do dele, ou a ordenação dos jogadores por resultado; quando o resultado é de equipe, é aquela em que alguma tela mostra o resultado de ao menos uma outra equipe identificada junto do da equipe do jogador, ou a ordenação das equipes por resultado

**Enunciado.** Existe ao menos uma competição com comparação visível aos jogadores, isto é, uma regra do jogo que compara os resultados de dois ou mais jogadores diferentes e uma tela que exibe essa comparação ao jogador

**Justificativa do nível.** essencialidade média, viabilidade baixa. Para Vigotski a interação social é a origem das funções psicológicas superiores, e na competição o resultado de outro jogador serve de referência para o próprio, o que aproxima os jogadores sem que um precise ajudar o outro. A essencialidade é média porque a competição produz comparação e não necessariamente mediação por pares, que ocorre de modo mais direto na colaboração (D27) e na comunicação entre jogadores (D06, D07). Exige identificar jogadores e guardar ou compartilhar resultados entre eles (servidor, banco de dados ou mesma tela); viabilidade baixa.

**Evidência.**
- Código: Localizar as regras que guardam um resultado por identificador de jogador ou de equipe e as comparam (ordenação, ranking, comparação de pontuações, definição de vencedor) e as telas que leem esses resultados para exibi-los. Regra de desempate: se as fontes divergirem sobre uma competição, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre uma competição conta como sem código para essa competição, e GDD que não descreve uma competição conta como sem GDD para essa competição
  - existe regra que guarda um resultado por identificador de jogador ou de equipe e compara os resultados de dois ou mais jogadores diferentes, diretamente ou por suas equipes (ordenação, placar ou definição de vencedor)
  - a comparação é entre jogadores, ou entre equipes de jogadores, e não entre o jogador e o resultado anterior dele mesmo ou o de personagem não jogável
  - alguma tela lê esses resultados e exibe ao jogador o resultado de ao menos um outro jogador identificado junto do dele, ou a ordenação dos jogadores por resultado; quando o resultado é de equipe, exibe o resultado de ao menos uma outra equipe identificada junto do da equipe do jogador, ou a ordenação das equipes por resultado (indica o estado atendido)
  - se a regra de comparação existe mas nenhuma tela exibe a comparação ao jogador, anotar (indica o estado parcial)
- Documentação: Verificar no GDD ou documento equivalente as regras de competição entre jogadores e as telas descritas para exibi-las. Regra de desempate: se as fontes divergirem sobre uma competição, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre uma competição conta como sem código para essa competição, e GDD que não descreve uma competição conta como sem GDD para essa competição
  - o GDD descreve regra que compara os resultados de dois ou mais jogadores diferentes (ranking, placar ou disputa) para determinar qual tem o melhor resultado
  - o GDD descreve tela que exibe ao jogador o resultado de ao menos um outro jogador identificado junto do dele, ou a ordenação dos jogadores por resultado; quando o resultado é de equipe, descreve tela que exibe o resultado de ao menos uma outra equipe identificada junto do da equipe do jogador, ou a ordenação das equipes por resultado (indica o estado atendido)
  - se o GDD descreve a regra de comparação mas nenhuma tela que a exiba ao jogador, anotar (indica o estado parcial)
- Vídeo: O vídeo só confirma a evidência de código ou do GDD: mostra a tela de comparação, mas não mostra a regra que a produz, e a ausência de comparação no vídeo não prova que o jogo não a oferece. Registrar as telas em que aparecem resultados de mais de um jogador. Regra de desempate: se as fontes divergirem sobre uma competição, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre uma competição conta como sem código para essa competição, e GDD que não descreve uma competição conta como sem GDD para essa competição
  - cada tela gravada que exibe resultados de jogadores foi registrada com timestamp (mínimo 0 telas)
  - em ao menos uma tela registrada, o resultado de ao menos um outro jogador identificado aparece junto do resultado do jogador gravado, ou os jogadores aparecem ordenados por resultado; quando o resultado é de equipe, o resultado de outra equipe identificada aparece junto do da equipe do jogador gravado, ou as equipes aparecem ordenadas por resultado
  - os nomes, apelidos ou números exibidos nessa tela correspondem a jogadores, e não a personagens não jogáveis; se o vídeo não permite verificar essa correspondência, a verificação fica a cargo do código ou do GDD e, sem eles, a tela não confirma o estado atendido

**Escala.**
- Atendido: Existe ao menos uma competição com comparação visível aos jogadores, nos termos do enunciado e das definições
- Parcial: Existe competição, nos termos do enunciado e das definições, mas nenhuma tela do jogo exibe a comparação ao jogador (o jogo compara os resultados de dois ou mais jogadores diferentes sem exibir a comparação)
- Não atendido: O jogo não compara os resultados de dois ou mais jogadores diferentes, nos termos do enunciado e das definições (inclui jogo de um só jogador e jogo em que o resultado é comparado apenas com o anterior do próprio jogador ou com personagem não jogável)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a regra que compara os resultados de dois ou mais jogadores diferentes, ou de suas equipes, para determinar qual tem o melhor resultado. Registrar a tela que exibe ao jogador o resultado de ao menos um outro jogador ou equipe identificados junto do seu, ou a ordenação dos jogadores ou das equipes por resultado (comparação visível, nos termos das definições)
- Design: Definir ao menos uma regra que compare os resultados de dois ou mais jogadores diferentes, ou de suas equipes, para determinar qual tem o melhor resultado, e não o resultado do jogador com o resultado anterior dele mesmo nem com o de personagem não jogável. Definir uma tela que exiba ao jogador o resultado de ao menos um outro jogador ou equipe identificados junto do seu, ou a ordenação dos jogadores ou das equipes por resultado (comparação visível, nos termos das definições)
- Código: Acrescentar, quando não existe, uma regra que guarde o resultado por identificador de jogador ou de equipe e compare os resultados de dois ou mais jogadores diferentes, ou de suas equipes (ordenação, placar ou definição de vencedor). Acrescentar uma tela que leia esses resultados e exiba ao jogador o resultado de ao menos um outro jogador ou equipe identificados junto do seu, ou a ordenação dos jogadores ou das equipes por resultado (comparação visível, nos termos das definições)

**Depende de.** —

### D27 — O jogo deve aproximar os jogadores pela colaboração

- Categoria: Socialização
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D27.1 — Nível AAA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *jogador*: uma pessoa que joga, e personagem não jogável não conta
- *objetivo compartilhado*: o objetivo de uma missão cuja conclusão só é registrada depois da ação prevista de cada um de ao menos dois jogadores diferentes, na mesma sessão ou em sessões diferentes, e cujo êxito (cumprimento da condição de conclusão) é um só, comum a todos os jogadores participantes, e não um êxito separado por jogador, de modo que pontuações ou recompensas individuais não desfazem o objetivo compartilhado quando o êxito é um só
- *ações interdependentes*: aquelas em que a ação de ao menos um jogador participante habilita, libera, fornece ou muda, para outro jogador participante, um acesso, um recurso, uma informação ou as ações que ele pode ou precisa executar para alcançar o objetivo (por exemplo, entregar um item, abrir uma passagem, fornecer uma informação, papéis com ações complementares, em que a ação de um é condição da ação do outro); reduzir a quantidade restante de um total comum, de modo que cada jogador contribui sem que sua ação habilite, libere, forneça ou mude o que o outro pode ou precisa fazer, não é interdependência

**Enunciado.** Existe ao menos uma missão com objetivo compartilhado cujas ações dos jogadores participantes são interdependentes

**Justificativa do nível.** essencialidade média, viabilidade baixa. Em Vigotski a zona de desenvolvimento proximal pode ser constituída entre pares: um jogador medeia a ação do outro ao fornecer-lhe informação, recurso ou passagem, o que só ocorre quando a ação de um habilita, libera, fornece ou muda o que o outro pode fazer. D13.1 garante que a conclusão exige a ação de mais de um jogador; D27 acrescenta o objetivo compartilhado e a interdependência das ações, sem os quais a colaboração se reduz à soma de contribuições individuais. O critério restringe a interdependência à possibilidade ou ao tipo de ação do par, e não à quantidade restante de um total comum, porque reduzir esse total não medeia a ação do outro; e exige êxito único porque o sucesso de um depender do outro é o que torna o objetivo compartilhado, sem que pontuações individuais o desfaçam. A essencialidade é média porque a mediação entre pares também ocorre por comunicação (D06, D07) e por ajuda (D16). Exige multijogador com estado compartilhado e papéis ou recursos distintos entre jogadores; viabilidade baixa.

**Evidência.**
- Código: Localizar a condição de conclusão das missões com mais de um jogador e verificar se o êxito é um só para o grupo (variável ou registro único) ou separado por identificador de jogador, e se a ação de um jogador escreve recurso, informação, acesso ou papel que as condições ou ações de outro jogador leem para habilitar, liberar ou mudar o que ele pode fazer (e não apenas reduz um contador compartilhado). Regra de desempate: se as fontes divergirem sobre uma missão, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre uma missão conta como sem código para essa missão, e GDD que não descreve uma missão conta como sem GDD para essa missão
  - existe missão cuja conclusão só é registrada depois da ação prevista de cada um de dois ou mais identificadores de jogador diferentes
  - nessa missão, o êxito é um só registro comum aos jogadores participantes, e não um registro por jogador; pontuações ou recompensas individuais não alteram essa verificação
  - nessa missão, ao menos uma ação de um jogador escreve recurso, informação, acesso ou papel que as condições ou as ações de outro jogador participante leem para habilitar, liberar ou mudar o que ele pode fazer, e não apenas reduz um contador compartilhado (indica o estado atendido)
  - se o objetivo é compartilhado mas nenhuma ação de um jogador habilita, libera, fornece ou muda o que outro pode ou precisa fazer, anotar (indica o estado parcial; inclui contribuições somadas a um total comum)
- Documentação: Verificar no GDD ou documento equivalente as missões em grupo: o objetivo, o êxito e o que a ação de cada jogador habilita, libera, fornece ou muda para os demais. Regra de desempate: se as fontes divergirem sobre uma missão, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre uma missão conta como sem código para essa missão, e GDD que não descreve uma missão conta como sem GDD para essa missão
  - o GDD descreve missão que só se conclui depois da ação prevista de cada um de dois ou mais jogadores diferentes
  - o GDD descreve um único êxito comum aos jogadores participantes (pontuações ou recompensas individuais não alteram essa verificação)
  - o GDD descreve ao menos uma ação de um jogador que habilita, libera, fornece ou muda um acesso, recurso, informação ou as ações que outro jogador participante pode ou precisa executar (indica o estado atendido)
  - se o GDD descreve objetivo compartilhado mas nenhuma ação que habilite, libere, forneça ou mude o que outro jogador pode ou precisa fazer, anotar (indica o estado parcial; inclui contribuições somadas a um total comum)
- Vídeo: O vídeo só confirma a evidência de código ou do GDD: não mostra que a conclusão exige mais de um jogador, e a ausência de colaboração no vídeo não prova que o jogo não a oferece. Registrar missão em que dois ou mais jogadores diferentes atuam, na mesma gravação ou em gravações distintas, as ações de cada um, o efeito de cada ação sobre o que os demais podem ou precisam fazer e o êxito exibido na conclusão. Regra de desempate: se as fontes divergirem sobre uma missão, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre uma missão conta como sem código para essa missão, e GDD que não descreve uma missão conta como sem GDD para essa missão
  - dois ou mais jogadores diferentes atuam na mesma missão, na mesma gravação ou em gravações distintas (mínimo 0 missões)
  - o jogo exibe, na conclusão, um único êxito comum aos jogadores participantes
  - ao menos uma ação de um jogador habilita, libera, fornece ou muda um acesso, recurso, informação ou as ações que outro jogador participante pode ou precisa executar, com timestamp da ação e do efeito

**Escala.**
- Atendido: Existe ao menos uma missão com objetivo compartilhado cujas ações dos jogadores participantes são interdependentes, nos termos do enunciado e das definições
- Parcial: Existe missão com objetivo compartilhado, nos termos do enunciado e das definições, mas as ações dos jogadores participantes não são interdependentes (cada jogador contribui sem que sua ação habilite, libere, forneça ou mude o que o outro pode ou precisa fazer, o que inclui contribuições somadas a um total comum)
- Não atendido: Nenhuma missão tem objetivo compartilhado, nos termos do enunciado e das definições (inclui jogo de um só jogador e jogo em que cada jogador tem um êxito separado)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente uma missão com ações previstas para dois ou mais jogadores, com o objetivo e as ações previstas para cada um deles. Registrar que essa missão só se conclui depois da ação prevista de cada um desses jogadores e que o êxito é um só, comum aos jogadores participantes. Registrar, para ao menos uma ação de um jogador, o acesso, recurso, informação ou ação que essa ação habilita, libera, fornece ou muda para outro jogador participante
- Design: Definir ao menos uma missão com ações previstas para dois ou mais jogadores diferentes, cuja conclusão só ocorre depois da ação prevista de cada um deles. Definir para essa missão um único êxito comum aos jogadores participantes, e não um êxito separado por jogador. Definir, nessa missão, ao menos uma ação de um jogador que habilite, libere, forneça ou mude, para outro jogador participante, um acesso, um recurso, uma informação ou as ações que esse outro jogador pode ou precisa executar (por exemplo, entregar um item, abrir uma passagem ou papéis com ações complementares), e não apenas reduza a quantidade restante de um total comum
- Código: Criar um registro compartilhado (sessão, sala ou estado comum) que aceite dois ou mais identificadores de jogador na mesma missão. Fazer a condição de conclusão dessa missão verificar a ação prevista de cada identificador de jogador participante. Gravar o êxito dessa missão em um único registro comum aos jogadores participantes, e não em um registro por jogador. Acrescentar, nessa missão, ao menos uma ação de um jogador que escreva recurso, informação, acesso ou papel que as condições ou as ações de outro jogador participante leiam para habilitar, liberar ou mudar o que esse outro jogador pode fazer, e não apenas reduza um contador compartilhado

**Depende de.** (D13.1)

### D28 — A proposta de narrativa deve despertar a curiosidade

- Categoria: Lúdico
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D28.1 — Nível AA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *narrativa*: a sequência de eventos, cenas, personagens e diálogos que o jogo apresenta ao jogador
- *abertura da missão*: o trecho da narrativa (texto, fala, cena ou legenda) exibido antes de o jogador poder executar a primeira ação do objetivo da missão
- *dispositivo*: um destes elementos presentes na abertura: pergunta explícita (frase interrogativa, dirigida ao jogador ou dita por personagem, sobre eventos, personagens ou mundo da narrativa e que a abertura não responde; enunciado de questão que o jogador deve responder como parte do desafio não conta, e pergunta retórica sobre o conteúdo de aprendizagem, e não sobre eventos, personagens ou mundo da narrativa, conta somente se a própria narrativa a responde em trecho liberado depois de o jogador executar ao menos uma ação do objetivo da missão), evento sem desfecho (evento narrado, como um desaparecimento, uma ameaça ou um problema, cujo desfecho a abertura não mostra; o enunciado do objetivo da própria missão, isto é, o que o jogador deve fazer, não conta como evento sem desfecho) ou informação retida (afirmação, na abertura, de que algo é desconhecido ou está oculto, como um segredo ou uma identidade ainda não revelada)
- *resolução do dispositivo*: a resposta, o desfecho ou a revelação, exibida em trecho da narrativa que o jogo libera depois de o jogador executar ao menos uma ação do objetivo da missão, e nunca na abertura
- *desafio* (sentido corrente): em «como parte do desafio» (local dispositivo), desafio está no sentido corrente de tarefa que a missão propõe ao jogador, e não no de unidade do glossário

**Enunciado.** A abertura de cada missão apresenta ao menos um dispositivo cuja resolução só é exibida depois de o jogador executar ao menos uma ação do objetivo da missão

**Justificativa do nível.** essencialidade média, viabilidade alta. Em Vigotski a situação imaginária define o jogo e cria uma zona de desenvolvimento, e a motivação é função da atividade; a narrativa sustenta esse papel quando deixa em aberto algo que a própria atividade resolve. A diretriz fala em despertar curiosidade, que é reação do jogador e varia entre jogadores, por isso o critério não mede curiosidade: verifica a presença de um dispositivo de projeto (pergunta explícita, evento sem desfecho ou informação retida) que só se resolve ao jogar. A essencialidade é média porque a motivação também vem dos desafios (D29) e das escolhas do jogador (D24, D25); escrever a abertura de cada missão não exige recurso técnico, viabilidade alta.

**Evidência.**
- Código: não se aplica
- Documentação: Verificar no roteiro da narrativa, no GDD ou em documento equivalente, para cada missão, o texto ou a descrição da abertura e o texto ou a descrição da resolução, anotando em que ponto da missão a resolução é exibida. Regra de desempate: se as fontes divergirem sobre uma missão, vale o GDD; sem GDD, o vídeo; GDD que não descreve a missão conta como sem GDD para essa missão, e o vídeo que mostra a abertura mas não mostra a resolução não confirma o dispositivo
  - o roteiro, GDD ou documento equivalente traz o texto ou a descrição da abertura de cada missão (mínimo 0 missões)
  - em cada missão listada, a abertura contém ao menos um dispositivo (pergunta explícita, evento sem desfecho ou informação retida)
  - para cada dispositivo, o documento descreve a resolução em trecho que o jogo libera depois de o jogador executar ao menos uma ação do objetivo da missão, e não na abertura; dispositivo resolvido na própria abertura não conta
  - se ao menos uma missão tem dispositivo, nos termos da definição, e ao menos outra não tem, anotar (indica o estado parcial)
- Vídeo: O vídeo só confirma a evidência do documento: mostra a abertura e a resolução das missões gravadas, mas a ausência de dispositivo no vídeo não prova que o jogo não o tem, e o vídeo que termina antes da resolução não a mostra. Registrar, em cada missão gravada, a abertura (timestamp e texto ou fala), os dispositivos nela presentes e o trecho posterior em que aparece a resolução. Regra de desempate: se as fontes divergirem sobre uma missão, vale o GDD; sem GDD, o vídeo; GDD que não descreve a missão conta como sem GDD para essa missão, e o vídeo que mostra a abertura mas não mostra a resolução não confirma o dispositivo
  - a abertura de cada missão presente no vídeo foi registrada com timestamp e texto ou fala (mínimo 1 missão)
  - cada abertura registrada contém ao menos um dispositivo (pergunta explícita, evento sem desfecho ou informação retida)
  - a resolução de cada dispositivo não aparece na abertura e aparece em trecho posterior, exibido depois de o jogador executar ao menos uma ação do objetivo da missão; se o vídeo termina antes da resolução, anotar resolução não observada, caso em que o dispositivo não é confirmado pelo vídeo

**Escala.**
- Atendido: A abertura de cada missão apresenta ao menos um dispositivo cuja resolução só é exibida depois de o jogador executar ao menos uma ação do objetivo da missão, nos termos do enunciado e das definições
- Parcial: Ao menos uma missão tem abertura com dispositivo cuja resolução só é exibida depois de o jogador executar ao menos uma ação do objetivo, nos termos do enunciado e das definições, e ao menos outra missão não tem
- Não atendido: Nenhuma missão tem abertura com dispositivo cuja resolução só seja exibida depois de o jogador executar ao menos uma ação do objetivo, nos termos do enunciado e das definições (inclui abertura sem pergunta, evento sem desfecho ou informação retida, e dispositivo resolvido na própria abertura)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente, para cada missão, o texto ou a descrição da abertura, com ao menos um dispositivo (pergunta explícita, evento sem desfecho ou informação retida). Registrar, para cada dispositivo, o texto ou a descrição da resolução e o ponto da missão em que a resolução é exibida, depois de o jogador executar ao menos uma ação do objetivo da missão
- Design: Incluir na abertura de cada missão ao menos um dispositivo (pergunta explícita, evento sem desfecho ou informação retida) que a própria abertura não resolva. Definir, para cada dispositivo, a resolução (resposta, desfecho ou revelação) em trecho da narrativa exibido depois de o jogador executar ao menos uma ação do objetivo da missão, e nunca na abertura
- Código: não se aplica

**Depende de.** —

### D29 — O jogo deve fornecer desafios motivadores, que estimulem o jogador a explorar

- Categoria: Lúdico
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D29.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *cenário jogável*: cada espaço do jogo (mapa, sala ou fase) em que o jogador executa ações e em que há uma missão em curso; cenário em que nenhuma missão está em curso (hub, sandbox) não tem caminho obrigatório e não é cenário jogável
- *caminho obrigatório (caminho da missão)*: a sequência de objetivos exigidos para completar a missão em curso, e fora do caminho obrigatório é tudo o que nenhum desses objetivos exige
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *objetivo de aprendizagem*: cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados
- *incentivo de exploração*: uma recompensa (item, pontos, desbloqueio ou conquista concedido pelo jogo), uma descoberta (cena, personagem, objeto interativo ou evento do cenário que não existe no caminho obrigatório; a área fora do caminho, por si só, não é descoberta) ou uma informação (texto, fala ou dado do jogo que não é apenas a descrição do objeto ou da área visitados e que cita ou descreve conceito, fato ou procedimento listado entre os objetivos de aprendizagem do GDD ou documento equivalente, ou trata de objetivo, evento ou personagem de uma missão do jogo) que o jogador obtém por ação própria fora do caminho obrigatório e não obtém seguindo apenas o caminho obrigatório; poder acessar áreas fora do caminho é tratado em D05, e o acesso a uma área sem recompensa, descoberta ou informação obtida não é incentivo de exploração

**Enunciado.** Existe ao menos um cenário jogável e todos os cenários jogáveis têm ao menos um incentivo de exploração

**Justificativa do nível.** essencialidade alta, viabilidade alta. Em Vigotski a motivação é função da atividade e o conhecimento se constrói na atividade do sujeito sobre o meio; um cenário que permite explorar (D05), mas nada oferece fora do caminho obrigatório, dá ao jogador razão apenas para seguir a missão. D29 trata do incentivo (recompensa, descoberta ou informação obtida só fora do caminho obrigatório), e não da permissão de acesso (D05) nem da motivação do jogador, que varia e não é medida. Para que o critério não se reduza a D05, a descoberta é conteúdo do cenário que não existe no caminho obrigatório, e não a área em si, e a informação exclui a mera descrição do objeto ou da área visitados e exige relação com objetivo de aprendizagem ou com a missão. Cenário sem missão em curso (hub, sandbox) não tem caminho obrigatório contra o qual medir o incentivo e fica fora do critério. A essencialidade é alta porque a exploração é a atividade pela qual o jogador opera sobre o mundo do jogo. Posicionar ao menos um incentivo em cada cenário é decisão de projeto de baixo custo; viabilidade alta.

**Evidência.**
- Código: Identificar os cenários em que há missão em curso (hub e sandbox sem missão em curso ficam excluídos) e localizar em cada um as recompensas (itens colecionáveis, desbloqueios, conquistas), as descobertas (cenas, personagens, objetos interativos, eventos) e as informações (textos, falas, dados) que ficam fora do caminho obrigatório; verificar, para cada uma, se nenhum objetivo ou condição de conclusão da missão exige obtê-la e se o jogador que segue apenas o caminho obrigatório não a recebe, e verificar ainda se a descoberta não existe no caminho obrigatório e se a informação não é apenas a descrição do objeto ou da área visitados e se relaciona a objetivo de aprendizagem do GDD ou a missão do jogo. Regra de desempate: se as fontes divergirem sobre um cenário, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um cenário conta como sem código para esse cenário, e GDD que não descreve um cenário conta como sem GDD para esse cenário
  - todos os cenários jogáveis (com missão em curso) foram listados, cada um com os incentivos de exploração que contém, e os cenários sem missão em curso foram anotados como excluídos (mínimo 0 incentivos por cenário)
  - em cada cenário listado, ao menos um incentivo de exploração, isto é, recompensa, descoberta (conteúdo que não existe no caminho obrigatório, e não a área em si) ou informação (que não é apenas a descrição do objeto ou da área visitados e se relaciona a objetivo de aprendizagem do GDD ou a missão do jogo) que nenhum objetivo nem condição de conclusão da missão exige obter
  - esse incentivo não é concedido ao jogador que segue apenas o caminho obrigatório
  - se ao menos um cenário tem incentivo de exploração e ao menos outro cenário não tem, anotar (indica o estado parcial)
- Documentação: Verificar no GDD ou nos mapas de nível quais cenários têm missão em curso (os demais, como hub e sandbox, ficam excluídos) e, para cada cenário jogável, os objetivos que compõem o caminho obrigatório e as recompensas, descobertas e informações descritas como obtidas fora dele, com a descoberta e a informação classificadas nos termos das definições. Regra de desempate: se as fontes divergirem sobre um cenário, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um cenário conta como sem código para esse cenário, e GDD que não descreve um cenário conta como sem GDD para esse cenário
  - o GDD ou mapa lista os cenários jogáveis (com missão em curso) e, para cada um, os incentivos de exploração, e anota como excluídos os cenários sem missão em curso (mínimo 0 incentivos por cenário)
  - em cada cenário listado, o GDD descreve ao menos um incentivo de exploração, isto é, recompensa, descoberta (conteúdo que não existe no caminho obrigatório, e não a área em si) ou informação (que não é apenas a descrição do objeto ou da área visitados e se relaciona a objetivo de aprendizagem do GDD ou a missão do jogo) que nenhum objetivo da missão exige
  - o GDD descreve que esse incentivo só é obtido fora do caminho obrigatório
  - se o GDD descreve incentivo em ao menos um cenário e em ao menos outro não descreve, anotar (indica o estado parcial)
- Vídeo: O vídeo só confirma a evidência de código ou do GDD: mostra os incentivos que o jogador gravado obtém, e a ausência de incentivo no vídeo não prova que o jogo não o oferece. Registrar os momentos em que o jogador obtém recompensa, descoberta ou informação, o cenário e se há missão em curso nele, o que foi obtido, a classificação da obtenção como recompensa, descoberta ou informação nos termos das definições e se o objetivo da missão em curso exigia o que foi obtido (objetivo listado no GDD ou, sem GDD, o anunciado pelo jogo). Regra de desempate: se as fontes divergirem sobre um cenário, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um cenário conta como sem código para esse cenário, e GDD que não descreve um cenário conta como sem GDD para esse cenário
  - cada obtenção de recompensa, descoberta ou informação foi registrada com timestamp, cenário e o que foi obtido (mínimo 0 obtenções)
  - cada obtenção registrada foi classificada como incentivo de exploração, quando nenhum objetivo da missão em curso exigia o que foi obtido e o jogador estava fora do caminho obrigatório, ou como obtenção exigida pelo caminho obrigatório; a descoberta só é classificada como incentivo quando o conteúdo não existe no caminho obrigatório, e a informação só quando não é apenas a descrição do objeto ou da área visitados e se relaciona a objetivo de aprendizagem do GDD ou a missão do jogo; só as classificadas como incentivo confirmam o estado atendido para o cenário em que ocorrem, desde que haja missão em curso nele

**Escala.**
- Atendido: Existe ao menos um cenário jogável e todos os cenários jogáveis têm ao menos um incentivo de exploração, nos termos do enunciado e das definições
- Parcial: Ao menos um cenário jogável tem incentivo de exploração, nos termos do enunciado e das definições, e ao menos outro cenário jogável não tem
- Não atendido: Nenhum cenário jogável tem incentivo de exploração, nos termos do enunciado e das definições (inclui cenário em que o acesso fora do caminho obrigatório não rende recompensa, descoberta nem informação, e jogo sem nenhum cenário em que haja missão em curso)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a lista de cenários jogáveis, com os cenários sem missão em curso anotados como excluídos. Registrar, para cada cenário jogável, ao menos um incentivo de exploração (recompensa, descoberta ou informação) que nenhum objetivo da missão exige. Registrar que cada um desses incentivos só é obtido fora do caminho obrigatório
- Design: Definir ao menos um cenário em que haja missão em curso, quando o jogo não tem nenhum. Incluir, em cada cenário jogável, ao menos um incentivo de exploração fora do caminho obrigatório: uma recompensa (item, pontos, desbloqueio ou conquista), uma descoberta (cena, personagem, objeto interativo ou evento que não existe no caminho obrigatório) ou uma informação que não seja apenas a descrição do objeto ou da área visitados e que trate de conceito, fato ou procedimento listado entre os objetivos de aprendizagem ou de uma missão do jogo. Definir que nenhum objetivo nem condição de conclusão da missão exija obter esse incentivo e que o jogador que segue apenas o caminho obrigatório não o receba
- Código: Acrescentar ao menos um cenário em que haja missão em curso, quando o jogo não tem nenhum. Acrescentar, em cada cenário jogável, fora do caminho obrigatório e obtido por ação do jogador, ao menos um incentivo de exploração: um item, pontos, desbloqueio ou conquista; uma cena, personagem, objeto interativo ou evento que não exista no caminho obrigatório; ou um texto, fala ou dado que não seja apenas a descrição do objeto ou da área visitados e que trate de conceito, fato ou procedimento listado entre os objetivos de aprendizagem ou de uma missão do jogo. Remover das condições de conclusão da missão a exigência de obter esse incentivo. Remover a concessão desse incentivo dos trechos do caminho obrigatório

**Depende de.** —

### D30 — O jogo deve colocar o jogador em uma situação realística

- Categoria: Realismo
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D30.1 — Nível AA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *premissa do jogo*: a situação em que o jogador é colocado no início da primeira missão (papel do jogador, local, tarefa e problema a resolver)
- *referente real*: uma situação, prática, profissão, fenômeno ou projeto que existe ou ocorre fora do jogo e que o GDD ou documento equivalente identifica por nome ou descrição específica (por exemplo, um projeto de pesquisa nomeado, uma profissão, um processo ambiental documentado); não contam cenário ou enredo fictício, lugar real usado só como pano de fundo sem que a tarefa do jogador corresponda a algo do referente, e descrição genérica como "o mundo real" ou "o dia a dia"; a premissa corresponde ao referente real quando o GDD indica ao menos um elemento da premissa (papel do jogador, local, tarefa ou problema a resolver) que descreve como o mesmo elemento do referente (mesmo papel, local, tarefa ou problema)
- *correspondência da premissa ao referente real*: um elemento é o mínimo que liga a premissa ao referente, e a diretriz não fixa quantidade maior
- *fonte do referente*: documento externo ao jogo que o GDD cita para descrever o referente (referência bibliográfica, página do projeto ou da instituição, norma, relatório ou registro de entrevista com profissionais), identificado por autoria ou endereço; menção sem identificação, como "segundo especialistas", não é fonte
- *documento equivalente neste critério*: sem GDD, a tela de abertura, a tela de créditos ou a tela Sobre do jogo conta como documento equivalente para este critério
- *escopo*: esta diretriz avalia só a premissa e o referente: a presença do conteúdo em situações do jogo é tratada em D31 e os objetos do cotidiano são tratados em D32
- *cenário* (sentido corrente): em «cenário ou enredo fictício» (local referente real), cenário está no sentido corrente de ambientação inventada, e não no de cenário jogável (D29)

**Enunciado.** O GDD ou documento equivalente nomeia um referente real para a premissa do jogo, indica ao menos um elemento da premissa que corresponde a esse referente e cita a fonte do referente

**Justificativa do nível.** essencialidade média, viabilidade alta. Em Vigotski o desenvolvimento ocorre no contexto sócio-histórico, e os conceitos científicos ganham sentido quando se ligam à prática social em que são usados; uma premissa com referente nomeado e documentado permite ao jogador relacionar o que faz no jogo a uma prática que existe fora dele. O critério avalia a existência do referente, da correspondência e da fonte, e não se o jogo parece verossímil, por isso o grau não depende de impressão do avaliador. A essencialidade é média porque a ligação com a vida fora do jogo também se dá pelo conteúdo em situação (D31) e pelos objetos do cotidiano (D32), sem que a premissa tenha referente. Nomear o referente e citar a fonte no GDD é decisão de projeto de baixo custo; viabilidade alta.

**Evidência.**
- Código: não se aplica
- Documentação: Verificar no GDD ou documento equivalente a descrição da premissa do jogo e localizar o referente real que ela nomeia, o elemento da premissa que o GDD descreve como o mesmo do referente e a fonte citada para o referente. Regra de desempate: se as fontes divergirem, vale o GDD; sem GDD, vale o vídeo, caso em que a tela de abertura, a tela de créditos ou a tela Sobre do jogo gravado conta como documento equivalente; GDD que existe mas não descreve a premissa conta como sem GDD
  - o GDD descreve a premissa do jogo (papel do jogador, local, tarefa e problema a resolver) e nomeia um referente real, por nome ou descrição específica
  - o GDD indica ao menos um elemento da premissa que descreve como o mesmo elemento do referente
  - o GDD cita fonte do referente, identificada por autoria ou endereço
  - se o GDD nomeia o referente e indica a correspondência mas não cita fonte, anotar (indica o estado parcial)
- Vídeo: Com GDD, o vídeo só confirma o GDD: mostra o que o jogo exibe na abertura, e a ausência da fonte no vídeo não prova que o GDD não a cita. Sem GDD, a tela de abertura, a tela de créditos ou a tela Sobre do jogo gravado é o documento equivalente, o vídeo é a evidência desse documento, e fonte do referente não exibida nessas telas deixa o vídeo no estado parcial; referente real não exibido nessas telas deixa o vídeo no estado não atendido, por falta de evidência. Registrar, com timestamp, o início da primeira missão e o que o jogo exibe nele em texto, fala ou tela, além da tela de créditos ou Sobre quando alcançada. Regra de desempate: se as fontes divergirem, vale o GDD; sem GDD, vale o vídeo, caso em que a tela de abertura, a tela de créditos ou a tela Sobre do jogo gravado conta como documento equivalente; GDD que existe mas não descreve a premissa conta como sem GDD
  - o início da primeira missão (ou do jogo, se não houver missões) foi registrado com o que o jogo exibe: nome ou descrição do referente, papel do jogador, local, tarefa ou problema (mínimo 1 registro)
  - o jogo exibe a correspondência entre premissa e referente real: o nome ou a descrição do referente e ao menos um elemento da premissa (papel do jogador, local, tarefa ou problema) apresentado como o mesmo elemento do referente; havendo GDD, o referente e o elemento exibidos são os que o GDD nomeia e indica
  - o jogo exibe a fonte do referente, identificada por autoria ou endereço, na abertura, nos créditos ou na tela Sobre; com GDD, fonte exibida confirma a fonte que o GDD cita e fonte não exibida não altera o grau do GDD; sem GDD, fonte exibida leva ao estado atendido e fonte não exibida leva ao estado parcial, desde que o referente e a correspondência estejam exibidos

**Escala.**
- Atendido: O GDD ou documento equivalente nomeia um referente real para a premissa do jogo, indica ao menos um elemento da premissa que corresponde a esse referente e cita a fonte do referente, nos termos do enunciado e das definições
- Parcial: O GDD nomeia um referente real para a premissa e indica ao menos um elemento da premissa que corresponde a esse referente, nos termos do enunciado e das definições, mas não cita a fonte do referente
- Não atendido: O GDD não nomeia referente real para a premissa, ou nomeia mas não indica elemento da premissa que corresponda a ele, nos termos do enunciado e das definições (inclui premissa fictícia, lugar real só como pano de fundo, descrição genérica do referente e ausência de GDD ou documento equivalente)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a premissa do jogo (papel do jogador, local, tarefa e problema a resolver) e o referente real dessa premissa, por nome ou descrição específica. Registrar ao menos um elemento da premissa descrito como o mesmo elemento do referente real. Registrar a fonte do referente real, identificada por autoria ou endereço
- Design: Definir para a premissa do jogo um referente real, nos termos das definições. Definir ao menos um elemento da premissa (papel do jogador, local, tarefa ou problema a resolver) como o mesmo elemento do referente real. Incluir na tela de abertura, de créditos ou Sobre o nome ou a descrição do referente real, o elemento da premissa apresentado como o mesmo elemento do referente e a fonte do referente, identificada por autoria ou endereço
- Código: não se aplica

**Depende de.** —

### D31 — O jogo contextualiza o conteúdo com situações reais

- Categoria: Realismo
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D31.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *objetivo de aprendizagem*: cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados
- *referente real*: uma situação, prática, profissão, fenômeno ou projeto que existe ou ocorre fora do jogo e que o GDD ou documento equivalente identifica por nome ou descrição específica
- *situação do jogo*: uma missão, um evento do cenário ou um diálogo com personagem em que há um propósito dentro do jogo (objetivo de missão, problema a resolver ou pedido de personagem); não contam como situação do jogo o verbete de glossário ou de enciclopédia, o menu de ajuda, a tela de texto de conteúdo sem personagem, evento nem problema de missão, a pergunta de quiz que só pede o nome ou a definição do conceito sem citar personagem, objeto ou problema da situação, e o material fora do jogo (livro, aula, folha de atividade)
- *situação real do jogo*: a situação do jogo que o GDD ou documento equivalente descreve como correspondente a uma situação, prática ou fenômeno real que existe ou ocorre fora do jogo (identificado por nome ou descrição específica), ou como reprodução do referente real nomeado para a premissa do jogo (D30); a situação fictícia que carrega o objetivo de aprendizagem não é situação real do jogo, e a classificação de uma situação do jogo como real vem só do GDD ou documento equivalente; o objetivo de aprendizagem é apresentado em uma situação real do jogo quando o conceito, fato ou procedimento é mencionado, demonstrado ou exigido dentro dela e ligado a um elemento da própria situação (personagem, objeto, ação ou problema da missão), de modo que o jogador o encontra no curso do propósito da situação
- *objetivo avaliado*: o objetivo de aprendizagem listado sobre o qual há evidência determinada: no código e no GDD, todo objetivo listado; no vídeo, só o objetivo cuja apresentação aparece na gravação, de modo que o vídeo não avalia o objetivo que não mostra, e a ausência de um objetivo no vídeo não prova que o jogo não o apresenta
- *confirmação pelo vídeo*: o vídeo sozinho confirma o estado atendido só quando todo objetivo listado é observado em situação real do jogo; sem código nem GDD que descrevam onde os objetivos aparecem, e sem essa confirmação pelo vídeo, o resultado é registrado como não confirmado e o grau é não atendido, por falta de evidência; o desempate entre fontes vale objetivo a objetivo, e o objetivo sem dado de código nem de GDD pode ser confirmado pelo vídeo para esse objetivo, de modo que a regra de que o vídeo só confirma atendido quando observa todo objetivo vale só quando nenhum objetivo tem dado de código ou de GDD
- *escopo*: esta diretriz avalia a apresentação situada de cada objetivo em situação real do jogo, com referente real por objetivo: D30 avalia só a premissa do jogo e seu referente, e os objetos do cotidiano são tratados em D32
- *cenário* (sentido corrente): em «evento do cenário» (local situação do jogo), cenário está no sentido corrente de ambiente do jogo, e não no de cenário jogável (D29), que restringiria a situação do jogo aos espaços com missão em curso

**Enunciado.** Existe ao menos um objetivo de aprendizagem listado no GDD ou documento equivalente e todo objetivo de aprendizagem listado é apresentado em ao menos uma situação real do jogo

**Justificativa do nível.** essencialidade alta, viabilidade alta. Em Vigotski os conceitos científicos se formam na relação com os conceitos cotidianos da experiência do sujeito e na prática social em que são usados, e um conceito apresentado só como definição, ou dentro de uma situação inventada sem ligação com essa prática, fica separado dessa experiência; dentro de uma situação que o GDD liga a uma prática ou fenômeno real, o jogador encontra o conceito em uso, mediado por uma situação com personagem, objeto e propósito. Este critério mede a apresentação situada com referente real por objetivo (cada objetivo listado em ao menos uma situação real do jogo), e D30 mede só a premissa do jogo e seu referente; um jogo pode ter premissa com referente real e objetivos apresentados em situações fictícias, e o inverso. Basta uma situação real por objetivo porque a diretriz trata da presença da contextualização, e não de quantas vezes ela se repete. A essencialidade é alta porque o conteúdo a aprender é a razão de ser do jogo educacional e a situação real é o meio pelo qual ele chega ao jogador. Associar cada objetivo a uma situação do jogo e descrever no GDD a prática ou o fenômeno real a que ela corresponde é decisão de roteiro e de documentação, sem custo técnico especial; viabilidade alta. O nível ordena a essencialidade teórica e não a dificuldade, e apresentar o conteúdo em situações reais é o núcleo do contexto sócio-histórico, e por isso o nível é A, enquanto a premissa de D30, isolada, é média. A dependência do GDD para classificar a situação como real é custo de documentação e não custo técnico, e por isso a viabilidade continua alta.

**Evidência.**
- Código: Com a lista de objetivos de aprendizagem do GDD e a classificação das situações como reais feita pelo GDD, localizar em diálogos, scripts de missão, eventos e bancos de perguntas as ocorrências de cada conceito, fato ou procedimento e, para cada ocorrência, a missão, o evento ou o diálogo em que está, o elemento da situação (personagem, objeto, ação ou problema) a que se liga e se o GDD descreve essa situação como real. Regra de desempate: a lista de objetivos de aprendizagem e a classificação de uma situação como real vêm só do GDD ou documento equivalente, e sem lista não há objetivo avaliado; para decidir onde um objetivo aparece no jogo, se as fontes divergirem vale o código; sem código, o GDD; sem ambos, o vídeo, aplicado objetivo a objetivo: o objetivo sem dado de código nem de GDD pode ser confirmado pelo vídeo para esse objetivo, e a regra de que o vídeo só confirma o estado atendido quando observa todo objetivo listado em situação real do jogo vale só quando nenhum objetivo tem dado de código ou de GDD; código que existe mas não traz dado sobre um objetivo conta como sem código para esse objetivo, e GDD que não descreve onde um objetivo aparece conta como sem GDD para esse objetivo
  - todos os objetivos de aprendizagem do GDD foram listados, cada um com as ocorrências encontradas no código ou nos dados do jogo (mínimo 0 ocorrências por objetivo)
  - para cada objetivo listado, ao menos uma ocorrência está em situação real do jogo, isto é, é mencionada, demonstrada ou exigida dentro de missão, evento ou diálogo, ligada a elemento da própria situação, e o GDD descreve essa situação como correspondente a situação, prática ou fenômeno real fora do jogo ou como reprodução do referente da premissa
  - as ocorrências em verbete de glossário ou de enciclopédia, menu de ajuda, tela de texto sem situação, pergunta de quiz que só pede nome ou definição e em situação que o GDD não descreve como real foram anotadas e não contadas
  - se ao menos um objetivo tem ocorrência em situação real do jogo e ao menos outro objetivo não tem, anotar (indica o estado parcial)
- Documentação: Verificar no GDD ou documento equivalente a lista de objetivos de aprendizagem e, para cada um, a missão, o evento ou o diálogo em que o GDD descreve que ele é apresentado, o elemento da situação a que se liga e a situação, prática ou fenômeno real fora do jogo (ou o referente da premissa) a que o GDD diz que a situação corresponde. Regra de desempate: a lista de objetivos de aprendizagem e a classificação de uma situação como real vêm só do GDD ou documento equivalente, e sem lista não há objetivo avaliado; para decidir onde um objetivo aparece no jogo, se as fontes divergirem vale o código; sem código, o GDD; sem ambos, o vídeo, aplicado objetivo a objetivo: o objetivo sem dado de código nem de GDD pode ser confirmado pelo vídeo para esse objetivo, e a regra de que o vídeo só confirma o estado atendido quando observa todo objetivo listado em situação real do jogo vale só quando nenhum objetivo tem dado de código ou de GDD; código que existe mas não traz dado sobre um objetivo conta como sem código para esse objetivo, e GDD que não descreve onde um objetivo aparece conta como sem GDD para esse objetivo
  - o GDD lista os objetivos de aprendizagem (mínimo 0 objetivos)
  - para cada objetivo listado, o GDD descreve ao menos uma situação do jogo em que ele é apresentado, ligado a elemento da própria situação, e descreve essa situação como correspondente a situação, prática ou fenômeno real fora do jogo, identificado por nome ou descrição específica, ou como reprodução do referente da premissa
  - os objetivos que o GDD descreve só como glossário, menu de ajuda, tela de texto sem situação, pergunta de quiz que só pede nome ou definição, material fora do jogo ou situação fictícia foram anotados e não contados
  - se o GDD descreve situação real para ao menos um objetivo e para ao menos outro não descreve, anotar (indica o estado parcial)
- Vídeo: O vídeo só confirma o código ou o GDD e só avalia os objetivos que mostra: o objetivo que a gravação não mostra não é avaliado pelo vídeo, e a ausência dele no vídeo não prova que o jogo não o apresenta; o vídeo sozinho confirma o estado atendido só quando todo objetivo listado no GDD é observado em situação real do jogo, e, sem código nem GDD que descrevam onde os objetivos aparecem, qualquer outro resultado do vídeo é registrado como não confirmado e o grau é não atendido, por falta de evidência. Registrar, com timestamp, cada momento em que o jogo apresenta conceito, fato ou procedimento da lista do GDD, o objetivo correspondente, a situação em que ocorre e se o GDD descreve essa situação como real. Regra de desempate: a lista de objetivos de aprendizagem e a classificação de uma situação como real vêm só do GDD ou documento equivalente, e sem lista não há objetivo avaliado; para decidir onde um objetivo aparece no jogo, se as fontes divergirem vale o código; sem código, o GDD; sem ambos, o vídeo, aplicado objetivo a objetivo: o objetivo sem dado de código nem de GDD pode ser confirmado pelo vídeo para esse objetivo, e a regra de que o vídeo só confirma o estado atendido quando observa todo objetivo listado em situação real do jogo vale só quando nenhum objetivo tem dado de código ou de GDD; código que existe mas não traz dado sobre um objetivo conta como sem código para esse objetivo, e GDD que não descreve onde um objetivo aparece conta como sem GDD para esse objetivo
  - cada apresentação de conceito, fato ou procedimento observada foi registrada com timestamp, objetivo de aprendizagem correspondente da lista do GDD e missão, evento ou diálogo em que ocorre (mínimo 0 registros)
  - cada registro foi classificado como apresentado em situação real do jogo, quando é mencionado, demonstrado ou exigido dentro de missão, evento ou diálogo, ligado a elemento da própria situação, e o GDD descreve essa situação como real, ou como apresentação isolada ou em situação não descrita como real; só os classificados como em situação real confirmam o objetivo
  - os objetivos da lista do GDD que a gravação não mostra foram anotados como não avaliados pelo vídeo, e os observados só em apresentação isolada ou em situação não descrita como real foram anotados; o vídeo sozinho só indica atendido quando todos os objetivos listados estão confirmados em situação real, e sem código nem GDD o resultado diferente disso é não confirmado; havendo código ou GDD para algum objetivo, o vídeo confirma o objetivo que não tem esse dado, objetivo a objetivo

**Escala.**
- Atendido: Existe ao menos um objetivo de aprendizagem listado e todo objetivo de aprendizagem listado é apresentado em ao menos uma situação real do jogo, nos termos do enunciado e das definições
- Parcial: Ao menos um objetivo de aprendizagem listado é apresentado em ao menos uma situação real do jogo, nos termos do enunciado e das definições, e ao menos outro objetivo listado não é
- Não atendido: Nenhum objetivo de aprendizagem é apresentado em situação real do jogo, nos termos do enunciado e das definições (inclui conteúdo só em glossário, menu de ajuda, tela de texto, pergunta de quiz que só pede nome ou definição ou situação fictícia, e GDD ou documento equivalente sem lista de objetivos de aprendizagem). Sem código nem GDD que descrevam onde os objetivos aparecem, e sem confirmação de todo objetivo listado pelo vídeo, o resultado é não confirmado e, por falta de evidência, o grau padrão é não atendido

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a lista de objetivos de aprendizagem, com ao menos um objetivo. Registrar, para cada objetivo de aprendizagem listado, ao menos uma missão, evento ou diálogo em que o objetivo é apresentado e o elemento dessa situação (personagem, objeto, ação ou problema) a que se liga. Registrar, para cada uma dessas situações, a situação, prática ou fenômeno real fora do jogo a que corresponde, identificado por nome ou descrição específica, ou que ela reproduz o referente real da premissa do jogo
- Design: Definir ao menos um objetivo de aprendizagem para o jogo. Incluir cada objetivo de aprendizagem listado no GDD ou documento equivalente em ao menos uma missão, evento ou diálogo que corresponda a uma situação, prática ou fenômeno real fora do jogo ou que reproduza o referente real da premissa do jogo. Ligar, em cada uma dessas situações, o objetivo de aprendizagem a um personagem, objeto, ação ou problema da própria situação, nos termos das definições
- Código: Acrescentar ou usar, em diálogos, scripts de missão, eventos ou bancos de perguntas, para cada objetivo de aprendizagem listado no GDD ou documento equivalente, ao menos uma ocorrência dentro de uma missão, evento ou diálogo que o GDD ou documento equivalente descreve como situação real. Ligar cada uma dessas ocorrências a um personagem, objeto, ação ou problema da própria situação, e não a verbete de glossário ou de enciclopédia, menu de ajuda, tela de texto sem situação ou pergunta de quiz que só pede nome ou definição

**Depende de.** —

### D32 — O jogo deve ter objetos do cotidiano com os quais o jogador pode se familiarizar

- Categoria: Realismo
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D32.1 — Nível AA

**Definições.**

- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *público-alvo*: o grupo de jogadores que o GDD ou documento equivalente descreve (faixa etária, série ou perfil), e sem essa descrição nenhum objeto pode ser classificado como item do cotidiano do público-alvo
- *item do cotidiano do público-alvo*: um objeto físico que o GDD ou documento equivalente cita pelo nome entre os objetos da rotina do público-alvo, ou entre os objetos de um local da rotina que o GDD atribui ao público-alvo (casa, escola, bairro, transporte), e que o jogo representa com o nome e a função que o objeto tem fora do jogo; não contam objeto fantástico ou inventado, objeto representado com função diferente da que tem fora do jogo, ícone ou elemento de interface (botão, menu, barra) e objeto de ambiente especializado que o GDD não atribui à rotina do público-alvo
- *objeto interativo*: um objeto do jogo sobre o qual o jogador executa ao menos uma ação (pegar, usar, abrir, mover, combinar ou selecionar) e ao qual o jogo responde com mudança de estado ou com mensagem; objeto que o jogador apenas vê, sem ação possível, é elemento visual do cenário e não é objeto interativo
- *cenário*: neste critério, o ambiente visual em que os objetos aparecem (a ambientação), e não o cenário jogável de D29
- *escopo*: esta diretriz avalia só os objetos: a premissa com referente real é tratada em D30 e o conteúdo em situações do jogo é tratado em D31
- *cenário* (sentido corrente): cenário tem neste critério o sentido do local «cenário» (ambientação), e não o de cenário jogável (D29)

**Enunciado.** Ao menos um objeto interativo do jogo é item do cotidiano do público-alvo descrito no GDD ou documento equivalente

**Justificativa do nível.** essencialidade média, viabilidade alta. Para Vigotski os conceitos cotidianos se formam na experiência do sujeito em seu contexto sócio-histórico e são a base sobre a qual os conceitos científicos se desenvolvem; objetos que o jogador já conhece do cotidiano e com os quais age no jogo ligam a atividade a essa experiência. A familiarização vem da ação sobre o objeto, por isso o objeto só visto no cenário não atende; um objeto interativo é o mínimo que permite essa ação, e a diretriz não fixa quantidade maior, de modo que um limite numérico seria arbitrário. A essencialidade é média porque a ligação com o cotidiano também se dá pela premissa (D30) e pelo conteúdo em situação (D31). Escolher objetos comuns para a interação é decisão de projeto de baixo custo; viabilidade alta.

**Evidência.**
- Código: Localizar os objetos do jogo sobre os quais há manipulador de evento (handler) de ação do jogador (pegar, usar, abrir, mover, combinar, selecionar) e a resposta do jogo, listar o nome e a função de cada um e compará-los com a lista de itens do cotidiano que o GDD atribui ao público-alvo; listar também os objetos de cenário sem manipulador de evento de ação do jogador (nome e função de cada um), para que o estado parcial possa ser avaliado. Regra de desempate: a classificação de um objeto como item do cotidiano do público-alvo vem só do GDD ou documento equivalente; para decidir se o objeto existe no jogo e é interativo, se as fontes divergirem vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um objeto conta como sem código para esse objeto, e GDD que não descreve um objeto conta como sem GDD para esse objeto
  - todos os objetos interativos foram listados, cada um com o manipulador de evento da ação do jogador e a resposta do jogo (mínimo 0 objetos)
  - todos os objetos de cenário sem manipulador de evento de ação do jogador foram listados, cada um com nome e função (mínimo 0 objetos)
  - ao menos um objeto interativo listado é representado com o nome e a função que tem fora do jogo e consta no GDD como item do cotidiano do público-alvo
  - se ao menos um objeto de cenário listado sem manipulador de evento é item do cotidiano do público-alvo, nos termos do enunciado e das definições, e nenhum objeto interativo é item do cotidiano, anotar (indica o estado parcial)
- Documentação: Verificar no GDD ou documento equivalente a descrição do público-alvo, a lista de itens do cotidiano dele e os objetos do jogo com a ação que o jogador executa sobre cada um. Regra de desempate: a classificação de um objeto como item do cotidiano do público-alvo vem só do GDD ou documento equivalente; para decidir se o objeto existe no jogo e é interativo, se as fontes divergirem vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um objeto conta como sem código para esse objeto, e GDD que não descreve um objeto conta como sem GDD para esse objeto
  - o GDD descreve o público-alvo (faixa etária, série ou perfil) e cita os itens do cotidiano dele, ou os objetos de um local da rotina atribuído a ele
  - ao menos um objeto do jogo descrito no GDD é item do cotidiano do público-alvo e o GDD descreve a ação que o jogador executa sobre ele e a resposta do jogo
  - se o GDD descreve item do cotidiano do público-alvo só como elemento visual do cenário e nenhum como objeto interativo, anotar (indica o estado parcial)
- Vídeo: O vídeo só confirma o código ou o GDD: mostra o que aparece na gravação, e a ausência do objeto no vídeo não prova que o jogo não o tem. Registrar, com timestamp, os objetos sobre os quais o jogador executa ação e os objetos vistos no cenário sem ação, com o nome exibido pelo jogo e a resposta do jogo à ação. Regra de desempate: a classificação de um objeto como item do cotidiano do público-alvo vem só do GDD ou documento equivalente; para decidir se o objeto existe no jogo e é interativo, se as fontes divergirem vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre um objeto conta como sem código para esse objeto, e GDD que não descreve um objeto conta como sem GDD para esse objeto
  - cada objeto sobre o qual o jogador executa ação foi registrado com timestamp, nome exibido, ação executada e resposta do jogo (mínimo 0 objetos)
  - ao menos um objeto registrado é interativo, é representado com o nome e a função que tem fora do jogo e consta no GDD como item do cotidiano do público-alvo; o vídeo sem GDD não classifica o objeto como item do cotidiano do público-alvo
  - os itens do cotidiano do público-alvo vistos só como elemento visual do cenário, sem ação do jogador, foram anotados (indica o estado parcial quando nenhum objeto interativo é item do cotidiano)

**Escala.**
- Atendido: Ao menos um objeto interativo do jogo é item do cotidiano do público-alvo descrito no GDD ou documento equivalente, nos termos do enunciado e das definições
- Parcial: O jogo representa ao menos um item do cotidiano do público-alvo, nos termos do enunciado e das definições, mas nenhum desses itens é objeto interativo (aparecem só como elemento visual do cenário)
- Não atendido: O jogo não representa item do cotidiano do público-alvo, nos termos do enunciado e das definições (inclui objetos só fantásticos ou de interface, objetos de ambiente especializado não atribuído à rotina do público-alvo e GDD ou documento equivalente sem descrição do público-alvo)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente o público-alvo (faixa etária, série ou perfil) e os itens do cotidiano do público-alvo, citados pelo nome, ou os objetos de um local da rotina atribuído ao público-alvo (casa, escola, bairro, transporte). Registrar ao menos um objeto do jogo que é item do cotidiano do público-alvo, com a ação que o jogador executa sobre esse objeto e a resposta do jogo
- Design: Incluir no jogo ao menos um item do cotidiano do público-alvo, nos termos das definições, ou usar um que já aparece só como elemento visual. Definir ao menos uma ação do jogador sobre esse item (pegar, usar, abrir, mover, combinar ou selecionar) e a resposta do jogo a essa ação, com mudança de estado ou mensagem
- Código: Acrescentar ou usar um objeto do jogo com o nome e a função de um item do cotidiano do público-alvo citado no GDD ou documento equivalente. Acrescentar a esse objeto um manipulador de evento (handler) de ação do jogador (pegar, usar, abrir, mover, combinar ou selecionar) que responda com mudança de estado ou mensagem

**Depende de.** —

### D33 — Os desafios devem ser personalizados de acordo com o desempenho do jogador

- Categoria: Personalização
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D33.1 — Nível AAA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *métrica de desempenho*: um valor que o jogo calcula e guarda durante a partida a partir do resultado do jogador nos desafios (pontuação, número de acertos ou de erros, taxa de acerto, tempo gasto ou número de tentativas); não contam escolha entre opções que o jogo não avalia como acerto ou erro (tratada em D34), nível de dificuldade escolhido pelo jogador, dado informado antes do jogo (idade, perfil) e valor que o jogo não guarda
- *parâmetro do desafio*: um valor que define o que o jogador enfrenta no desafio: a dificuldade (nível, velocidade, tolerância a erro), a quantidade (de itens, de perguntas, de tentativas permitidas), o tempo disponível, a meta de conclusão ou o conteúdo (qual pergunta, objetivo ou situação é apresentado); não contam texto de feedback, dica ou orientação (tratados em D17 e D18), aparência (cor, avatar, tema visual) e pontuação ou recompensa concedida
- *desafio posterior*: o desafio, a rodada ou a nova tentativa que começa depois do registro da métrica de desempenho do jogador, no mesmo desafio ou em outro
- *desafio personalizado por desempenho*: quando o valor de um parâmetro do desafio posterior é definido por regra que lê a métrica de desempenho registrada do jogador e produz ao menos dois valores diferentes do parâmetro para ao menos dois valores diferentes da métrica, sendo esses valores de um parâmetro do desafio apresentado (nos termos da definição de parâmetro do desafio); avançar para o próximo desafio ou repetir o mesmo desafio conforme o resultado não conta como personalização, porque nenhum valor de parâmetro do desafio apresentado difere entre os dois casos; aumento de parâmetro por ordem fixa dos desafios, igual para todo jogador, e escolha manual do parâmetro pelo jogador não são personalização por desempenho
- *regra de desempenho ou de ação*: se a regra lê acerto, erro, tempo, pontuação ou número de tentativas, a personalização é de desempenho (D33); se lê qual opção, item, caminho ou modo de agir foi usado, é de ação (D34); regra que lê os dois conta nas duas diretrizes
- *escopo*: a mudança só do texto de feedback é tratada em D18

**Enunciado.** Em ao menos um desafio, ao menos um parâmetro do desafio posterior é definido por regra que lê uma métrica de desempenho registrada do jogador e produz valores diferentes conforme a métrica

**Justificativa do nível.** essencialidade baixa, viabilidade baixa. Na zona de desenvolvimento proximal de Vigotski, a tarefa deve ficar entre o que o aprendiz faz sozinho e o que faz com apoio, e quem media ajusta a tarefa ao que ele mostrou fazer; um desafio de parâmetros fixos fica igual para jogadores com desempenhos diferentes. O critério exige um parâmetro que muda por regra sobre métrica registrada, e distingue-se de D18 (só a mensagem muda) e de D34 (a regra lê a escolha ou a ação, e não o resultado); basta um desafio porque exigir todos faria o grau depender do número de desafios do jogo. A decisão entre avançar para o próximo desafio e repetir o mesmo não muda o que o desafio exige do jogador, e por isso não conta como personalização. A essencialidade é baixa porque a mediação também se dá por feedback e orientação (D17, D18), e a viabilidade é baixa porque exige medir o desempenho, definir os limites de mudança e produzir variantes de conteúdo por faixa; AAA.

**Evidência.**
- Código: Localizar as variáveis que guardam métricas de desempenho (pontuação, acertos, erros, tempo, tentativas) e as funções que definem parâmetros de desafio (nos termos da definição de parâmetro do desafio) e verificar se algum parâmetro é atribuído por regra que lê a métrica, com ao menos dois ramos ou valores. Rastrear a indireção: de cada atribuição de parâmetro de desafio, seguir para trás até as entradas que a definem, e de cada métrica guardada, seguir para frente até todos os leitores dela, atravessando apelidos de variável, estado salvo ou persistido, eventos ou mensagens e tabelas de dados (JSON, arquivos de fases). Regra de desempate: se as fontes divergirem sobre um desafio, vale o código; sem código, o GDD; código que existe mas não traz dado sobre um desafio conta como sem código para esse desafio, e GDD que não descreve um desafio conta como sem GDD para esse desafio
  - todas as métricas de desempenho guardadas foram listadas, cada uma com o trecho de código que a calcula e guarda (mínimo 0 métricas)
  - a indireção foi rastreada: de cada métrica listada foram enumerados todos os leitores (incluindo os alcançados por apelido, estado salvo ou persistido, evento ou mensagem e tabela de dados), e de cada atribuição de parâmetro de desafio foram seguidas as entradas que a definem
  - existe, em ao menos um desafio, um parâmetro do desafio posterior atribuído por regra que lê uma métrica listada, e o valor do parâmetro difere entre dois valores da métrica (nos termos da definição de parâmetro do desafio), e não apenas a decisão entre avançar e repetir o desafio
  - se existe métrica guardada e os leitores enumerados só exibem pontuação, relatório ou mensagem de feedback, ou só decidem entre avançar para o próximo desafio e repetir o mesmo desafio, anotar os leitores verificados (indica o estado parcial)
- Documentação: Verificar no GDD ou documento equivalente as métricas de desempenho que o jogo registra e as regras de adaptação, isto é, qual parâmetro do desafio muda, para qual valor da métrica e para qual valor do parâmetro. Regra de desempate: se as fontes divergirem sobre um desafio, vale o código; sem código, o GDD; código que existe mas não traz dado sobre um desafio conta como sem código para esse desafio, e GDD que não descreve um desafio conta como sem GDD para esse desafio
  - o GDD lista as métricas de desempenho registradas (mínimo 0 métricas)
  - o GDD descreve, em ao menos um desafio, um parâmetro do desafio posterior (nos termos da definição de parâmetro do desafio) e a regra que o define a partir de uma métrica, com ao menos dois valores do parâmetro para dois valores da métrica; a regra que só decide entre avançar para o próximo desafio e repetir o mesmo desafio não conta
  - se o GDD descreve métrica registrada e nenhuma regra de parâmetro que a use, ou só regra que decide entre avançar e repetir, anotar (indica o estado parcial)
- Vídeo: não se aplica

**Escala.**
- Atendido: Em ao menos um desafio, ao menos um parâmetro do desafio posterior é definido por regra que lê uma métrica de desempenho registrada do jogador e produz valores diferentes conforme a métrica, nos termos do enunciado e das definições
- Parcial: O jogo registra ao menos uma métrica de desempenho, nos termos do enunciado e das definições, mas nenhum parâmetro de desafio posterior é definido por regra que a leia (inclui métrica usada só para exibir pontuação, relatório ou mensagem de feedback e métrica usada só para decidir entre avançar para o próximo desafio e repetir o mesmo desafio)
- Não atendido: O jogo não registra métrica de desempenho, nos termos do enunciado e das definições (inclui jogo que não guarda pontuação, acertos, erros, tempo nem tentativas)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente as métricas de desempenho que o jogo registra. Registrar, em ao menos um desafio, o parâmetro do desafio posterior definido a partir de uma métrica de desempenho e a regra que o define, com ao menos dois valores do parâmetro para dois valores da métrica
- Design: Definir ou usar ao menos uma métrica de desempenho que o jogo registre (pontuação, acertos, erros, tempo ou tentativas). Definir, em ao menos um desafio, uma regra que atribua a um parâmetro do desafio posterior, nos termos das definições, valores diferentes para ao menos dois valores dessa métrica, e não apenas a decisão entre avançar para o próximo desafio e repetir o mesmo desafio
- Código: Acrescentar ou usar uma variável que calcule e guarde uma métrica de desempenho do jogador (pontuação, acertos, erros, tempo ou tentativas). Acrescentar, na função que define um parâmetro do desafio posterior, nos termos das definições, uma regra que leia essa métrica e atribua ao parâmetro ao menos dois valores diferentes para dois valores da métrica, e não apenas exiba pontuação, relatório ou feedback nem decida só entre avançar para o próximo desafio e repetir o mesmo desafio

**Depende de.** —

### D34 — Os desafios devem ser personalizados de acordo com as ações do jogador

- Categoria: Personalização
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D34.1 — Nível AAA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *ação anterior do jogador*: uma escolha ou ação deliberada do jogador, feita antes do desafio posterior, que o jogo guarda (em variável, marcador de estado, inventário ou histórico) e cujo valor identifica qual opção, item, caminho ou modo de agir o jogador usou (escolha de diálogo, objeto ou personagem escolhido, caminho seguido, forma de resolver uma situação), sendo caminho seguido a sequência de opções ou ramos que o jogador escolheu; não contam valor que mede o resultado do jogador (pontuação, acertos, erros, tempo, tentativas), tratado em D33, e a seleção direta, por menu, do próprio desafio ou do seu nível de dificuldade
- *parâmetro do desafio*: um valor que define o que o jogador enfrenta no desafio: a dificuldade (nível, velocidade, tolerância a erro), a quantidade (de itens, de perguntas, de tentativas permitidas), o tempo disponível, a meta de conclusão ou o conteúdo (qual pergunta, objetivo ou situação é apresentado); não contam texto de feedback, dica ou orientação (tratados em D17 e D18), aparência (cor, avatar, tema visual) e pontuação ou recompensa concedida
- *desafio posterior*: o desafio, a rodada ou a nova tentativa que começa depois da ação anterior do jogador, no mesmo desafio ou em outro
- *desafio personalizado pelas ações do jogador*: quando o valor de um parâmetro do desafio posterior é definido por regra que lê o valor da ação anterior do jogador e produz ao menos dois valores diferentes do parâmetro para ao menos dois valores diferentes da ação; mudança só do enredo, da aparência ou do texto de feedback não é personalização do desafio, e a ramificação apenas entre avançar para o próximo desafio e repetir o mesmo desafio também não é; a missão X em vez da missão Y conta só se o objetivo, os itens, a quantidade ou o tempo do desafio diferem entre elas, e não se diferem só no enredo; os valores diferentes do parâmetro são valores de um parâmetro do desafio apresentado, nos termos da definição de parâmetro do desafio
- *regra de desempenho ou de ação*: se a regra lê acerto, erro, tempo, pontuação ou número de tentativas, a personalização é de desempenho (D33); se lê qual opção, item, caminho ou modo de agir foi usado, é de ação (D34); regra que lê os dois conta nas duas diretrizes
- *escopo*: a mudança só do texto de feedback é tratada em D18

**Enunciado.** Em ao menos um desafio, ao menos um parâmetro do desafio posterior é definido por regra que lê uma ação anterior do jogador e produz valores diferentes conforme a ação

**Justificativa do nível.** essencialidade baixa, viabilidade baixa. Em Vigotski o sujeito aprende agindo sobre o meio por meio de instrumentos e signos; quando o desafio seguinte reflete o que o jogador escolheu fazer, e não só o resultado que obteve, a escolha passa a ter consequência na atividade. O critério exige que a regra leia a ação (qual opção, item, caminho ou modo de agir), e distingue-se de D33 (a regra lê o resultado), de D18 (só a mensagem muda) e de D03 (escolha direta da atividade); basta um desafio pelo mesmo motivo de D33, a existência da regra. A ramificação entre avançar e repetir, e a missão que difere só no enredo, não mudam o que o desafio exige do jogador, e por isso não contam como personalização. A essencialidade é baixa porque as ações do jogador já condicionam o progresso (D10) e as escolhas de ordem (D03), e a viabilidade é baixa porque exige guardar o estado das escolhas e produzir variantes de desafio para cada uma; AAA.

**Evidência.**
- Código: Localizar as variáveis, marcadores de estado e históricos que guardam escolhas e ações do jogador (escolha de diálogo, objeto ou personagem escolhido, caminho seguido) e as funções que definem parâmetros de desafio, e verificar se algum parâmetro é atribuído por regra que lê o valor guardado, com ao menos dois ramos ou valores. Rastrear a indireção: de cada atribuição de parâmetro de desafio, seguir para trás até as entradas que a definem, e de cada escolha ou ação guardada, seguir para frente até todos os leitores dela, atravessando apelidos de variável, estado salvo ou persistido, eventos ou mensagens e tabelas de dados (JSON, arquivos de fases). Regra de desempate: se as fontes divergirem sobre um desafio, vale o código; sem código, o GDD; sem ambos, o vídeo, que só confirma o estado atendido por par de ocorrências comparáveis; sem código, GDD nem confirmação no vídeo, o resultado é registrado como não confirmado; código que existe mas não traz dado sobre um desafio conta como sem código para esse desafio, e GDD que não descreve um desafio conta como sem GDD para esse desafio
  - todas as ações anteriores guardadas foram listadas, cada uma com o trecho de código que a guarda (mínimo 0 ações)
  - a indireção foi rastreada: de cada ação listada foram enumerados todos os leitores (incluindo os alcançados por apelido, estado salvo ou persistido, evento ou mensagem e tabela de dados), e de cada atribuição de parâmetro de desafio foram seguidas as entradas que a definem
  - existe, em ao menos um desafio, um parâmetro do desafio posterior atribuído por regra que lê uma ação anterior listada, e o valor do parâmetro difere entre dois valores da ação (nos termos da definição de parâmetro do desafio), e não apenas a ramificação entre avançar e repetir o desafio nem a diferença só de enredo entre missões
  - se existe ação anterior guardada e os leitores enumerados só alteram enredo, aparência ou texto de feedback, ou só decidem entre avançar para o próximo desafio e repetir o mesmo desafio, anotar os leitores verificados (indica o estado parcial)
- Documentação: Verificar no GDD ou documento equivalente as escolhas e ações do jogador que o jogo guarda e as regras que ligam cada uma a um parâmetro de desafio posterior, isto é, qual parâmetro muda, para qual valor da ação e para qual valor do parâmetro. Regra de desempate: se as fontes divergirem sobre um desafio, vale o código; sem código, o GDD; sem ambos, o vídeo, que só confirma o estado atendido por par de ocorrências comparáveis; sem código, GDD nem confirmação no vídeo, o resultado é registrado como não confirmado; código que existe mas não traz dado sobre um desafio conta como sem código para esse desafio, e GDD que não descreve um desafio conta como sem GDD para esse desafio
  - o GDD lista as escolhas e ações do jogador que o jogo guarda (mínimo 0 ações)
  - o GDD descreve, em ao menos um desafio, um parâmetro do desafio posterior (nos termos da definição de parâmetro do desafio) e a regra que o define a partir de uma ação anterior, com ao menos dois valores do parâmetro para dois valores da ação; a ramificação apenas entre avançar e repetir, e a missão X em vez da missão Y que difere só no enredo, não contam
  - se o GDD descreve ação guardada e nenhuma regra de parâmetro que a use, ou só regra que decide entre avançar e repetir, anotar (indica o estado parcial)
- Vídeo: O vídeo só confirma o estado atendido, por par de ocorrências comparáveis, e os estados parcial e não atendido são decididos por código e GDD: ele mostra o que o jogador gravado fez, e uma única gravação não mostra que outra ação levaria a outro valor do parâmetro. Registrar, no mesmo ponto de decisão, duas ocorrências com ações anteriores diferentes (na mesma gravação ou em gravações distintas) e o valor observável do parâmetro no desafio posterior de cada uma. Regra de desempate: se as fontes divergirem sobre um desafio, vale o código; sem código, o GDD; sem ambos, o vídeo, que só confirma o estado atendido por par de ocorrências comparáveis; sem código, GDD nem confirmação no vídeo, o resultado é registrado como não confirmado; código que existe mas não traz dado sobre um desafio conta como sem código para esse desafio, e GDD que não descreve um desafio conta como sem GDD para esse desafio
  - cada par de ocorrências do mesmo ponto de decisão com ações anteriores diferentes foi registrado, com timestamp, ação anterior e valor observável do parâmetro do desafio posterior (mínimo 0 pares)
  - em ao menos um par registrado, o valor do parâmetro do desafio posterior difere entre as duas ocorrências; a diferença confirma o estado atendido, e a ausência de diferença ou de par não prova que o jogo não personaliza

**Escala.**
- Atendido: Em ao menos um desafio, ao menos um parâmetro do desafio posterior é definido por regra que lê uma ação anterior do jogador e produz valores diferentes conforme a ação, nos termos do enunciado e das definições
- Parcial: O jogo guarda ao menos uma ação anterior do jogador, nos termos do enunciado e das definições, mas nenhum parâmetro de desafio posterior é definido por regra que a leia (inclui ação que só altera o enredo, a aparência ou o texto de feedback e ação que só decide entre avançar para o próximo desafio e repetir o mesmo desafio)
- Não atendido: O jogo não guarda ação anterior do jogador, nos termos do enunciado e das definições (inclui jogo que não guarda escolhas nem ações do jogador, e jogo que guarda só métrica de desempenho ou só a seleção direta do desafio ou do nível). Por falta de evidência (sem código, GDD nem confirmação no vídeo), o grau padrão é não atendido

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente as escolhas e ações do jogador que o jogo guarda. Registrar, em ao menos um desafio, o parâmetro do desafio posterior definido a partir de uma ação anterior do jogador e a regra que o define, com ao menos dois valores do parâmetro para dois valores da ação
- Design: Definir ou usar ao menos uma ação anterior do jogador que o jogo guarde (escolha de diálogo, objeto ou personagem escolhido, caminho seguido ou forma de resolver uma situação). Definir, em ao menos um desafio, uma regra que atribua a um parâmetro do desafio posterior, nos termos das definições, valores diferentes para ao menos dois valores dessa ação, e não apenas mudança de enredo, aparência ou texto de feedback nem a decisão entre avançar para o próximo desafio e repetir o mesmo desafio
- Código: Acrescentar ou usar uma variável, marcador de estado ou histórico que guarde uma ação anterior do jogador (escolha de diálogo, objeto ou personagem escolhido, caminho seguido). Acrescentar, na função que define um parâmetro do desafio posterior, nos termos das definições, uma regra que leia esse valor guardado e atribua ao parâmetro ao menos dois valores diferentes para dois valores da ação, e não apenas altere enredo, aparência ou texto de feedback nem decida só entre avançar para o próximo desafio e repetir o mesmo desafio

**Depende de.** —

### D35 — O jogo deve permitir que o jogador crie desafios para outros jogadores

- Categoria: Personalização
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D35.1 — Nível AAA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *desafio criado pelo jogador*: um desafio que o jogador monta com ao menos um elemento de conteúdo que o jogo não fornece pronto (pergunta ou resposta digitadas, elementos do desafio posicionados ou combinados pelo jogador, ou regra montada por ele) e com a condição de conclusão definida por ele (resposta correta, ponto de chegada ou meta); não contam escolher um desafio pronto, alterar só a dificuldade, a aparência ou a ordem de desafios prontos, e construir objeto ou estrutura sem condição de conclusão (tratado em D12)
- *outro jogador*: uma pessoa diferente do autor do desafio que joga e que o jogo identifica por uma identidade de jogador diferente da do autor (perfil, conta ou nome de usuário, local ou remota); o compartilhamento no mesmo dispositivo conta só se o desafio fica guardado sob uma identidade de jogador diferente da do autor, e passar o dispositivo a outra pessoa sem guardar o desafio sob outra identidade não conta; outra instalação ou outro dispositivo que abre o desafio por código, arquivo ou servidor de compartilhamento conta como identidade de jogador distinta da do autor, e a restrição de mesmo dispositivo vale só para a mesma instalação sob a mesma identidade; o próprio autor e o personagem não jogável não contam
- *disponibilização a outro jogador*: o jogo disponibiliza o desafio criado a outro jogador quando o guarda em armazenamento compartilhado entre jogadores (servidor, arquivo ou código de compartilhamento) e oferece ao outro jogador uma ação do jogo para abri-lo (lista, convite, importação ou código) e jogá-lo; desafio que só o autor pode abrir não é disponibilizado

**Enunciado.** Existe uma mecânica em que o jogador cria um desafio e o jogo o disponibiliza a outro jogador para que o jogue

**Justificativa do nível.** essencialidade baixa, viabilidade baixa. Em Vigotski a interação social entre pares cria a zona de desenvolvimento proximal, e quem cria um desafio para outro assume o papel de organizar a tarefa do par e antecipar o que ele consegue fazer, o que é uma forma de mediação entre jogadores. O critério exige que o artefato criado seja um desafio com condição de conclusão e que chegue a outro jogador, o que o distingue de D12 (construir objetos persistentes, sem exigir que outro os jogue). Um elemento de conteúdo definido pelo jogador é o mínimo que distingue o desafio criado de um desafio pronto, e a diretriz não fixa quantidade maior. A dependência de D07.1 existe porque disponibilizar o desafio a outro jogador exige persistir o que um jogador criou e exibi-lo a outros jogadores em sessões posteriores, o mecanismo que D07.1 mede; sem esse mecanismo, o desafio criado não chega a outro jogador. A essencialidade é baixa porque a interação entre jogadores também ocorre por comunicação (D06, D07) e por tarefas em grupo (D13); a viabilidade é baixa porque exige editor, serialização do desafio, armazenamento compartilhado e verificação de que o desafio criado pode ser concluído.

**Evidência.**
- Código: Localizar o editor ou a lógica de criação de desafio, a serialização do desafio criado (arquivo, registro ou código de compartilhamento), o armazenamento compartilhado entre jogadores e o carregador que abre no jogo o desafio criado por outro jogador. Regra de desempate: se as fontes divergirem sobre uma mecânica de criação, vale o código; sem código, o GDD; sem ambos, o vídeo, que só confirma o estado atendido; sem código, GDD nem confirmação no vídeo, o resultado é registrado como não confirmado; código que existe mas não traz dado sobre a mecânica conta como sem código para essa mecânica, e GDD que não a descreve conta como sem GDD para essa mecânica
  - existe lógica em que o jogador define ao menos um elemento de conteúdo e a condição de conclusão de um desafio e o jogo guarda o resultado como desafio jogável
  - o desafio criado é gravado em armazenamento compartilhado entre jogadores (servidor, arquivo ou código de compartilhamento)
  - existe lógica que lista, importa ou abre, para um jogador diferente do autor, o desafio criado e o executa como desafio jogável
  - se o desafio criado só pode ser aberto pelo autor, anotar (indica o estado parcial)
- Documentação: Verificar no GDD ou documento equivalente a mecânica de criação de desafio: o que o jogador define, como o desafio é compartilhado e como outro jogador o abre e o joga. Regra de desempate: se as fontes divergirem sobre uma mecânica de criação, vale o código; sem código, o GDD; sem ambos, o vídeo, que só confirma o estado atendido; sem código, GDD nem confirmação no vídeo, o resultado é registrado como não confirmado; código que existe mas não traz dado sobre a mecânica conta como sem código para essa mecânica, e GDD que não a descreve conta como sem GDD para essa mecânica
  - o GDD descreve o que o jogador define ao criar o desafio (elemento de conteúdo e condição de conclusão)
  - o GDD descreve como o desafio criado chega a outro jogador (armazenamento compartilhado e ação de abri-lo) e que o outro jogador o joga
  - se o GDD descreve a criação do desafio mas só o autor o joga, anotar (indica o estado parcial)
- Vídeo: O vídeo só confirma o estado atendido, e os estados parcial e não atendido são decididos por código e GDD: a ausência da criação no vídeo não prova que o jogo não a oferece, e uma única gravação pode mostrar só um lado. Registrar o momento em que o jogador cria um desafio e o momento em que outro jogador abre e joga um desafio criado, na mesma gravação ou em gravações distintas. Regra de desempate: se as fontes divergirem sobre uma mecânica de criação, vale o código; sem código, o GDD; sem ambos, o vídeo, que só confirma o estado atendido; sem código, GDD nem confirmação no vídeo, o resultado é registrado como não confirmado; código que existe mas não traz dado sobre a mecânica conta como sem código para essa mecânica, e GDD que não a descreve conta como sem GDD para essa mecânica
  - ao menos um momento em que o jogador define elemento de conteúdo e condição de conclusão de um desafio e o jogo o guarda foi registrado, com timestamp
  - ao menos um momento em que um jogador abre e joga, dentro do jogo, desafio criado por outro jogador foi registrado, com timestamp; o desafio aberto confirma a disponibilização quando é o mesmo desafio criado em momento registrado por jogador diferente do que o abre, ou quando o jogo exibe como autor um jogador diferente do que o abre

**Escala.**
- Atendido: Existe uma mecânica em que o jogador cria um desafio e o jogo o disponibiliza a outro jogador para que o jogue, nos termos do enunciado e das definições
- Parcial: O jogador cria um desafio, nos termos do enunciado e das definições, mas o jogo não o disponibiliza a outro jogador (só o autor o joga, ou outra pessoa o joga na mesma instalação e sob a mesma identidade de jogador do autor, sem que o desafio fique guardado sob outra identidade de jogador)
- Não atendido: O jogador não cria desafio, nos termos do enunciado e das definições (inclui construção de objetos sem condição de conclusão e escolha ou configuração de desafios prontos). Por falta de evidência (sem código, GDD nem confirmação no vídeo), o grau padrão é não atendido

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a mecânica de criação de desafio, com o elemento de conteúdo e a condição de conclusão que o jogador define. Registrar como o desafio criado chega a outro jogador, com o armazenamento compartilhado entre jogadores e a ação que abre o desafio criado, e que o outro jogador joga esse desafio
- Design: Definir uma mecânica em que o jogador crie um desafio, nos termos das definições, com ao menos um elemento de conteúdo e a condição de conclusão definidos pelo jogador. Definir que o jogo guarde o desafio criado em armazenamento compartilhado entre jogadores (servidor, arquivo ou código de compartilhamento). Definir uma ação do jogo (lista, convite, importação ou código) pela qual outro jogador, nos termos das definições, abra e jogue o desafio criado
- Código: Acrescentar ou usar um editor ou lógica de criação em que o jogador defina ao menos um elemento de conteúdo e a condição de conclusão de um desafio e que guarde o resultado como desafio jogável. Acrescentar a gravação do desafio criado em armazenamento compartilhado entre jogadores (servidor, arquivo ou código de compartilhamento). Acrescentar uma lógica que liste, importe ou abra o desafio criado para um jogador com identidade de jogador diferente da do autor e o execute como desafio jogável

**Depende de.** (D07.1)

### D36 — O jogador deve organizar informações

- Categoria: Organização
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D36.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *objetivo de aprendizagem*: cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados
- *sessão de jogo*: o período contínuo entre o jogador iniciar o jogo, ou carregar um estado salvo, e encerrá-lo (fechar o jogo ou voltar ao menu inicial)
- *informação*: um item, dado, texto, imagem ou medida relativo a ao menos um objetivo de aprendizagem listado no GDD ou documento equivalente, coletado pelo jogador ou fornecido pelo jogo; é relativo a um objetivo quando o GDD ou documento equivalente, ou a marcação do item no código (campo, identificador ou etiqueta de objetivo), o associa a esse objetivo
- *operação de organização*: uma ação do jogador que define, para ao menos uma informação, a categoria, o grupo, a posição, a ordem ou o rótulo com que o jogo a guarda, escolhido pelo jogador entre ao menos duas possibilidades oferecidas pelo jogo (classificar em categorias, agrupar, ordenar, posicionar em mapa, quadro, diário ou inventário, rotular); não contam como operação de organização o preenchimento automático de inventário, diário ou lista em que o jogo decide a posição, o grupo e a ordem (a coleta é tratada em D11), a ordenação aplicada por critério fixo do jogo, mesmo quando acionada por botão do jogador, e o texto livre digitado em campo de anotação sem categoria, grupo, posição ou ordem escolhidos pelo jogador (a produção de texto é tratada em D09)
- *estado organizado*: o conjunto de categorias, grupos, posições, ordens ou rótulos resultante das operações de organização do jogador; o estado organizado persiste quando o jogo o mantém guardado depois de o jogador sair da tela ou do momento em que operou, até o fim da sessão de jogo ou até o jogador desfazê-lo
- *consulta posterior*: o jogador abrir ou ver o estado organizado, ou uma missão ou desafio ler esse estado, depois de ter saído da tela ou do momento em que operou
- *escopo*: este critério avalia a operação do jogador e a persistência e consulta do resultado, e não a coleta da informação, tratada em D11

**Enunciado.** O jogador executa ao menos uma operação de organização sobre informações, e o estado organizado persiste e é consultado depois

**Justificativa do nível.** essencialidade alta, viabilidade média. Em Vigotski, a memória mediada e a atenção voluntária, funções psicológicas superiores, se apoiam em signos e instrumentos externos, e organizar informações em categorias, grupos ou ordem é operar com esses signos; os conceitos científicos, por sua vez, formam-se como parte de um sistema de relações, e não como itens soltos. Quando o jogo preenche sozinho o inventário ou o diário, o sistema é do jogo e o jogador apenas o consulta; este critério exige que a estrutura seja escolhida pelo jogador e persista para ser consultada depois, e se distingue de D11, que trata só de coletar. Viabilidade média: exige interface de escolha, estrutura de dados que persista e uma consulta posterior, o que é mais trabalho que um inventário automático.

**Evidência.**
- Código: Localizar as mecânicas de inventário, diário, caderno, mapa, quadro, classificação ou agrupamento e, em cada uma, o trecho de código que grava a categoria, o grupo, a posição, a ordem ou o rótulo. Verificar se esse dado é escolhido pelo jogador entre ao menos duas possibilidades ou definido pelo jogo, se é guardado em estrutura que sobrevive à saída da tela (estado global ou dado de salvamento) ou descartado ao fechá-la, e se há tela, painel ou leitura em missão ou desafio que o exibe ou lê depois, verificando também se a informação organizada é relativa a objetivo de aprendizagem. Regra de desempate: se as fontes divergirem, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a operação de organização conta como sem código para ela, e GDD que não a descreve conta como sem GDD para ela. Sem código nem GDD, o vídeo decide só pelo que mostra: o grau é atendido quando o vídeo mostra a operação e mostra o estado organizado de novo depois de o jogador sair da tela ou do momento em que operou (o que mostra persistência e consulta posterior), e nao_atendido nos demais casos, anotando que o grau decorre da falta de evidência; o vídeo isolado não estabelece o estado parcial, porque não mostra persistência sem consulta posterior
  - uma ação do jogador grava categoria, grupo, posição, ordem ou rótulo escolhido entre ao menos duas possibilidades para ao menos uma informação relativa a objetivo de aprendizagem do GDD ou documento equivalente, ou marcada no código com esse objetivo (mínimo 0 operações)
  - o dado gravado fica em estrutura que sobrevive à saída da tela ou do momento da operação e não é descartado ao fechá-la
  - existe tela, painel ou leitura em missão ou desafio que exibe ou lê o estado organizado em momento posterior à operação
  - se existe operação e persistência e nenhuma exibição ou leitura posterior, anotar (indica o estado parcial)
  - se o jogo decide a posição, o grupo e a ordem sem escolha do jogador, ou descarta o estado ao fechar a tela, anotar (indica o estado nao_atendido)
- Documentação: Verificar no GDD ou documento equivalente a mecânica de organização: o que o jogador organiza, como (classificar, agrupar, ordenar, posicionar, rotular), quem escolhe a categoria, o grupo, a posição, a ordem ou o rótulo, se o estado organizado fica guardado e onde é consultado depois. Regra de desempate: se as fontes divergirem, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a operação de organização conta como sem código para ela, e GDD que não a descreve conta como sem GDD para ela. Sem código nem GDD, o vídeo decide só pelo que mostra: o grau é atendido quando o vídeo mostra a operação e mostra o estado organizado de novo depois de o jogador sair da tela ou do momento em que operou (o que mostra persistência e consulta posterior), e nao_atendido nos demais casos, anotando que o grau decorre da falta de evidência; o vídeo isolado não estabelece o estado parcial, porque não mostra persistência sem consulta posterior
  - o GDD descreve ao menos uma operação em que o jogador escolhe categoria, grupo, posição, ordem ou rótulo, entre ao menos duas possibilidades, para informação relativa a objetivo de aprendizagem listado (mínimo 0 operações)
  - o GDD descreve que o estado organizado fica guardado depois de o jogador sair da tela ou do momento da operação
  - o GDD descreve a tela, o painel ou a missão ou desafio que exibe ou lê o estado organizado depois
  - se o GDD descreve operação e persistência sem consulta posterior, anotar (indica o estado parcial)
  - se o GDD descreve inventário, diário ou lista preenchidos automaticamente, sem escolha do jogador, anotar (indica o estado nao_atendido)
- Vídeo: O vídeo só confirma a evidência de código ou do GDD: a ausência de operação ou de consulta no vídeo não prova que o jogo não as tem, e o vídeo não decide se a informação é relativa a objetivo de aprendizagem, o que vem do código ou da documentação. Registrar com timestamp cada operação do jogador (o que ele escolhe, entre quais possibilidades) e cada momento posterior em que o estado organizado aparece de novo. Regra de desempate: se as fontes divergirem, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a operação de organização conta como sem código para ela, e GDD que não a descreve conta como sem GDD para ela. Sem código nem GDD, o vídeo decide só pelo que mostra: o grau é atendido quando o vídeo mostra a operação e mostra o estado organizado de novo depois de o jogador sair da tela ou do momento em que operou (o que mostra persistência e consulta posterior), e nao_atendido nos demais casos, anotando que o grau decorre da falta de evidência; o vídeo isolado não estabelece o estado parcial, porque não mostra persistência sem consulta posterior
  - ao menos um momento em que o jogador escolhe categoria, grupo, posição, ordem ou rótulo para uma informação, entre ao menos duas possibilidades oferecidas pelo jogo (mínimo 0 operações)
  - ao menos um momento posterior em que o estado organizado aparece de novo, depois de o jogador sair da tela ou do momento em que operou
  - a relação da informação com objetivo de aprendizagem foi verificada no código ou na documentação e não no vídeo

**Escala.**
- Atendido: O jogador executa ao menos uma operação de organização, o estado organizado persiste e é consultado depois, nos termos do enunciado e das definições
- Parcial: O jogador executa ao menos uma operação de organização e o estado organizado persiste, mas nenhuma consulta posterior existe, nos termos do enunciado e das definições
- Não atendido: O jogador não executa nenhuma operação de organização, ou o estado organizado não persiste, nos termos do enunciado e das definições (inclui inventário, diário ou lista preenchidos automaticamente pelo jogo e anotação em texto livre sem estrutura escolhida)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente ao menos uma operação de organização, com a informação relativa a objetivo de aprendizagem listado que o jogador organiza e a categoria, o grupo, a posição, a ordem ou o rótulo que o jogador escolhe entre ao menos duas possibilidades. Registrar que o estado organizado fica guardado depois de o jogador sair da tela ou do momento da operação. Registrar a tela, o painel, a missão ou o desafio que exibe ou lê o estado organizado depois da operação
- Design: Definir ao menos uma operação de organização, nos termos das definições, sobre informação relativa a um objetivo de aprendizagem listado no GDD ou documento equivalente, com escolha do jogador entre ao menos duas possibilidades, e não preenchimento automático, ordenação por critério fixo do jogo nem texto livre sem estrutura escolhida. Definir que o estado organizado fique guardado depois de o jogador sair da tela ou do momento da operação. Incluir uma tela, painel, missão ou desafio que exiba ou leia o estado organizado depois da operação
- Código: Acrescentar ou usar uma ação do jogador que grave, para ao menos uma informação relativa a objetivo de aprendizagem do GDD ou documento equivalente ou marcada no código com esse objetivo, a categoria, o grupo, a posição, a ordem ou o rótulo escolhido pelo jogador entre ao menos duas possibilidades. Trocar a estrutura que guarda esse dado, quando descartada ao fechar a tela, por estado global ou dado de salvamento. Acrescentar ou usar uma tela, painel ou leitura em missão ou desafio que exiba ou leia o estado organizado depois da operação

**Depende de.** —

### D37 — O jogo, suas missões e mini jogos devem apresentar a situação-problema ao jogador de maneira explícita

- Categoria: Resolução de problemas
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D37.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *situação-problema*: uma situação com estado inicial, objetivo e mais de uma ação possível, cuja resolução exige uma decisão do jogador, e não apenas a repetição de uma mesma ação; escolher entre alternativas prontas, sem estado inicial a ser transformado pelas ações do jogador, não conta como situação-problema
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *unidade*: cada missão ou minijogo
- *abertura da unidade*: o trecho de texto, fala ou legenda exibido antes de o jogador poder executar a primeira ação do objetivo da unidade; a abertura apresenta a situação-problema da unidade quando declara, em texto ou fala, o estado inicial (o que há ou ocorre no ponto de partida da unidade) e o objetivo (o que o jogador deve alcançar ou resolver); não contam como declaração o título ou o nome da unidade sozinho, a instrução de controles ou de interface sozinha (teclas, botões), a ilustração, o ícone ou a cena sem texto nem fala, e o objetivo declarado só depois de o jogador executar uma ação do objetivo
- *fala*: áudio cujo conteúdo é determinável por transcrição, legenda, roteiro, GDD ou audição no vídeo, e o áudio de conteúdo não determinável conta como sem declaração
- *unidade avaliada*: a unidade sobre a qual há evidência: no código e no GDD, toda missão e todo minijogo existente ou descrito; no vídeo, só a unidade cuja abertura foi gravada inteira, e a abertura que o jogador gravado pulou antes de ela ser exibida inteira não é avaliada no vídeo
- *escopo*: este critério avalia só se o estado inicial e o objetivo são declarados antes da ação: o número de ações possíveis e a decisão do jogador, que a abertura não declara, e portanto se a unidade é de fato uma situação-problema, são tratados em D01, e a abertura com dispositivo de curiosidade é tratada em D28

**Enunciado.** A abertura de cada missão e de cada minijogo apresenta a situação-problema ao jogador, em texto ou fala, declarando o estado inicial e o objetivo antes de o jogador poder executar a primeira ação do objetivo

**Justificativa do nível.** essencialidade alta, viabilidade alta. Para Vigotski a atividade humana é mediada por signos, e a palavra, escrita ou falada, organiza a atenção voluntária e a intenção do sujeito antes da ação. Uma unidade que começa sem declarar o estado inicial e o objetivo leva o jogador a agir por tentativa, sem saber que problema deve resolver; declará-los em texto ou fala é a mediação mínima que permite planejar a ação. O critério trata só da apresentação, e não de a unidade ser uma situação-problema (D01). Escrever ou gravar a abertura de cada unidade é decisão de projeto de baixo custo; viabilidade alta.

**Evidência.**
- Código: Listar as missões e minijogos e, em cada uma, localizar o texto, a legenda ou a fala exibidos antes de a primeira ação do objetivo poder ser executada (scripts de abertura, caixas de diálogo de início, painéis de missão). Verificar se esse trecho declara o estado inicial e o objetivo da unidade e se o objetivo só é declarado depois de uma ação do jogador. Regra de desempate: se as fontes divergirem sobre uma unidade, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a abertura da unidade (inclui fala em arquivo de áudio sem transcrição) conta como sem código para essa unidade, e GDD que não descreve a abertura da unidade conta como sem GDD para essa unidade; o vídeo não depende de escolha do jogador gravado, porque a abertura é exibida antes da primeira ação, e a unidade cuja abertura não foi gravada não é avaliada no vídeo
  - todas as missões e minijogos foram listados, cada um com o trecho de código ou o recurso que exibe a abertura (mínimo 1 unidade, pois o jogo sem divisão em missões conta como uma única missão)
  - em cada unidade listada existe abertura em texto ou fala, exibida antes de o jogador poder executar a primeira ação do objetivo
  - em cada unidade listada a abertura declara o estado inicial e o objetivo, e não se limita a título, instrução de controles ou cena sem texto nem fala
  - se ao menos uma unidade atende aos itens anteriores e ao menos outra não, anotar (indica o estado parcial)
- Documentação: Verificar no GDD, roteiro ou documento equivalente, para cada missão e minijogo, o texto ou a fala de abertura e o que ele declara. Regra de desempate: se as fontes divergirem sobre uma unidade, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a abertura da unidade (inclui fala em arquivo de áudio sem transcrição) conta como sem código para essa unidade, e GDD que não descreve a abertura da unidade conta como sem GDD para essa unidade; o vídeo não depende de escolha do jogador gravado, porque a abertura é exibida antes da primeira ação, e a unidade cuja abertura não foi gravada não é avaliada no vídeo
  - o GDD lista as missões e minijogos e, em cada uma, descreve o texto ou a fala de abertura (mínimo 1 unidade)
  - o GDD descreve que a abertura declara o estado inicial e o objetivo da unidade antes da primeira ação do objetivo
  - se o GDD descreve abertura que declara estado inicial e objetivo em ao menos uma unidade e em ao menos outra não, anotar (indica o estado parcial)
- Vídeo: O vídeo só confirma a evidência de código ou do GDD: a ausência de abertura no vídeo não prova que o jogo não a tem, e a unidade cuja abertura não foi gravada não é avaliada. Registrar o início de cada missão e minijogo gravado desde o começo, o texto ou a fala exibido antes da primeira ação do objetivo (transcrito) e o instante da primeira ação. Regra de desempate: se as fontes divergirem sobre uma unidade, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre a abertura da unidade (inclui fala em arquivo de áudio sem transcrição) conta como sem código para essa unidade, e GDD que não descreve a abertura da unidade conta como sem GDD para essa unidade; o vídeo não depende de escolha do jogador gravado, porque a abertura é exibida antes da primeira ação, e a unidade cuja abertura não foi gravada não é avaliada no vídeo
  - todas as missões e minijogos com abertura gravada inteira foram registrados, cada um com o texto ou a fala de abertura transcrito (mínimo 0 unidades)
  - em cada unidade registrada, o texto ou a fala exibido antes da primeira ação do objetivo declara o estado inicial e o objetivo
  - as unidades registradas cuja abertura não declara estado inicial e objetivo foram anotadas (indica o estado parcial quando ao menos uma unidade atende)

**Escala.**
- Atendido: Existe ao menos uma unidade avaliada e todas as unidades avaliadas apresentam a situação-problema na abertura, em texto ou fala, nos termos do enunciado e das definições
- Parcial: Ao menos uma unidade avaliada apresenta a situação-problema na abertura, em texto ou fala, nos termos do enunciado e das definições, e ao menos outra unidade avaliada não apresenta
- Não atendido: Nenhuma unidade avaliada apresenta a situação-problema na abertura, em texto ou fala, nos termos do enunciado e das definições, ou não existe unidade avaliada

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a lista de missões e minijogos. Registrar, para cada missão e minijogo, o texto ou a fala de abertura e que essa abertura declara o estado inicial e o objetivo antes da primeira ação do objetivo
- Design: Incluir, em cada missão e minijogo sem abertura ou cuja abertura não declara o estado inicial e o objetivo, um texto ou fala de abertura que declare o estado inicial e o objetivo, nos termos das definições. Definir que essa abertura seja exibida antes de o jogador poder executar a primeira ação do objetivo
- Código: Acrescentar ou usar, em cada missão e minijogo, um script de abertura, caixa de diálogo de início ou painel de missão que exiba em texto, legenda ou fala transcrita o estado inicial e o objetivo, e não só título, instrução de controles ou cena sem texto nem fala. Acrescentar uma condição que impeça a primeira ação do objetivo antes de essa abertura ser exibida

**Depende de.** —

### D38 — O jogo deve fornecer informações escritas ao jogador

- Categoria: Linguagem
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D38.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *item do conjunto mínimo*: cada instrução de missão, cada diálogo com personagem não jogável (NPC) e cada descrição de objeto interativo
- *instrução de missão*: o conteúdo que o jogo fornece ao jogador, em texto ou em áudio, dizendo o que fazer na missão, uma por missão
- *diálogo com NPC*: a sequência de falas de um ou mais NPCs dirigidas ao jogador, iniciada por interação do jogador ou por evento da missão
- *objeto interativo*: um elemento do cenário sobre o qual o jogador pode agir (examinar, pegar, usar, acionar)
- *descrição de objeto interativo*: o conteúdo que o jogo fornece, em texto ou em áudio, quando o jogador interage com o objeto, dizendo o que o objeto é ou faz, e o texto que é apenas o nome do objeto ou da missão não é descrição nem instrução
- *forma escrita*: texto exibido na tela e legível sem áudio (balão, caixa de diálogo, painel, legenda, inclusive a legenda que o jogador pode ativar nas opções, e texto embutido em imagem) que contém todas as ações, nomes e números que o áudio do mesmo item informa; não contam como forma escrita o ícone, o pictograma, a ilustração e a animação sem texto
- *item sem forma escrita*: o item fornecido só em áudio (fala, narração ou som) e a instrução de missão que o jogo não fornece em forma alguma, e o diálogo ou a descrição que o jogo não fornece em forma alguma não é item, pois nada é fornecido
- *item avaliado*: o item sobre o qual há evidência: no código e no GDD, todo item existente ou descrito, incluindo a instrução de cada missão; no vídeo, só o item cuja apresentação foi gravada inteira (a instrução da missão cuja abertura foi gravada, e os diálogos e descrições exibidos no vídeo)
- *escopo*: este critério avalia só se o conteúdo fornecido existe por escrito: a produção de texto pelo jogador é tratada em D09
- *cenário* (sentido corrente): em «elemento do cenário» (local objeto interativo), cenário está no sentido corrente de ambiente visual do jogo, e não no de cenário jogável (D29)

**Enunciado.** Cada missão tem instrução em forma escrita, e todo diálogo com NPC e toda descrição de objeto interativo que o jogo fornece têm forma escrita, isto é, texto na tela e não apenas áudio

**Justificativa do nível.** essencialidade alta, viabilidade alta. Em Vigotski, a linguagem escrita é um sistema de signos que medeia o pensamento e, ao contrário da fala, permanece disponível para releitura, o que apoia a memória mediada e a atenção voluntária do aprendiz ao longo da atividade. Instrução, diálogo ou descrição fornecidos só em áudio obrigam o jogador a reter o que ouviu, sem poder consultá-lo de novo. O conjunto mínimo (instruções de missão, diálogos com NPC e descrições de objetos interativos) é o conteúdo pelo qual o jogo media a ação do jogador, e produzir texto é papel do jogador, tratado em D09. Exibir texto em caixa de diálogo é recurso básico dos motores de jogo; viabilidade alta.

**Evidência.**
- Código: Listar as instruções de missão, os diálogos com NPC e as descrições de objetos interativos, e em cada item verificar se existe texto exibido na tela (campo de texto, caixa de diálogo, legenda, imagem com texto) e se há áudio sem texto correspondente. Verificar se a legenda é ativável nas opções e se o texto contém as ações, nomes e números do áudio. Regra de desempate: se as fontes divergirem sobre um item, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o item conta como sem código para esse item, e GDD que não descreve o item conta como sem GDD para esse item; legenda que o código ou o GDD mostram ser ativável pelo jogador prevalece sobre vídeo gravado com a legenda desativada; o vídeo avalia só os itens que mostra, a ausência de diálogo ou descrição no vídeo não prova que o jogo não os tem, e sem item observado, o grau pelo vídeo é nao_atendido por falta de evidência, anotado como tal
  - todas as missões foram listadas, cada uma com o recurso que fornece sua instrução (texto, áudio ou nenhum) (mínimo 1 missão)
  - todos os diálogos com NPC e todas as descrições de objetos interativos existentes foram listados, cada um com o recurso de texto e o de áudio, se houver (mínimo 0 itens)
  - cada item listado tem forma escrita, isto é, texto na tela que contém as ações, nomes e números do áudio do mesmo item, quando há áudio
  - os itens listados sem forma escrita (só áudio, ou instrução de missão não fornecida) foram anotados (indica o estado parcial quando ao menos um item tem forma escrita)
- Documentação: Verificar no GDD ou documento equivalente as instruções de cada missão, os diálogos com NPC e as descrições de objetos interativos e se cada um é descrito com texto na tela, só com áudio ou com ambos. Regra de desempate: se as fontes divergirem sobre um item, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o item conta como sem código para esse item, e GDD que não descreve o item conta como sem GDD para esse item; legenda que o código ou o GDD mostram ser ativável pelo jogador prevalece sobre vídeo gravado com a legenda desativada; o vídeo avalia só os itens que mostra, a ausência de diálogo ou descrição no vídeo não prova que o jogo não os tem, e sem item observado, o grau pelo vídeo é nao_atendido por falta de evidência, anotado como tal
  - o GDD descreve a instrução de cada missão e o meio em que ela é fornecida (mínimo 1 missão)
  - o GDD descreve os diálogos com NPC e as descrições de objetos interativos e o meio de cada um (mínimo 0 itens)
  - o GDD descreve cada item listado com forma escrita; os itens descritos só com áudio, ou a missão sem instrução descrita, foram anotados (indica o estado parcial quando ao menos um item tem forma escrita)
- Vídeo: O vídeo só confirma a evidência de código ou do GDD: a ausência de item no vídeo não prova que o jogo não o tem. Registrar, em cada missão gravada desde a abertura, a instrução (texto, áudio ou nenhum) e, nos diálogos e descrições exibidos, se há texto na tela, só áudio ou ambos, anotando quais ações, nomes e números cada meio informa. Regra de desempate: se as fontes divergirem sobre um item, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o item conta como sem código para esse item, e GDD que não descreve o item conta como sem GDD para esse item; legenda que o código ou o GDD mostram ser ativável pelo jogador prevalece sobre vídeo gravado com a legenda desativada; o vídeo avalia só os itens que mostra, a ausência de diálogo ou descrição no vídeo não prova que o jogo não os tem, e sem item observado, o grau pelo vídeo é nao_atendido por falta de evidência, anotado como tal
  - todas as instruções de missão, diálogos com NPC e descrições de objetos interativos exibidos no vídeo foram registrados, cada um com o meio (texto, áudio) e o instante (mínimo 0 itens)
  - cada item registrado tem texto na tela que contém as ações, nomes e números do áudio do mesmo item
  - os itens registrados sem texto na tela foram anotados, conferindo antes no código ou no GDD se há legenda ativável (indica o estado parcial quando ao menos um item tem forma escrita)

**Escala.**
- Atendido: Existe ao menos um item avaliado e todos os itens avaliados têm forma escrita, nos termos do enunciado e das definições
- Parcial: Ao menos um item avaliado tem forma escrita, nos termos do enunciado e das definições, e ao menos outro item avaliado não tem (item sem forma escrita, nos termos do enunciado e das definições)
- Não atendido: Nenhum item avaliado tem forma escrita, nos termos do enunciado e das definições, ou não existe item avaliado

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente a instrução de cada missão, os diálogos com NPC e as descrições de objetos interativos. Registrar que cada um desses itens é fornecido com texto na tela que contém as ações, nomes e números do áudio do mesmo item, quando há áudio
- Design: Incluir, em cada missão sem instrução de missão, uma instrução em forma escrita, nos termos das definições. Incluir forma escrita em cada instrução de missão, diálogo com NPC e descrição de objeto interativo fornecidos só em áudio. Incluir no texto na tela de cada item as ações, nomes e números que o áudio do mesmo item informa e o texto omite
- Código: Acrescentar, em cada missão sem instrução, um campo de texto, caixa de diálogo ou painel que exiba a instrução da missão. Acrescentar texto na tela (caixa de diálogo, legenda ou painel) a cada instrução de missão, diálogo com NPC e descrição de objeto interativo que só toca áudio. Trocar o texto de cada item que omite ações, nomes ou números do áudio do mesmo item por um texto que os contenha

**Depende de.** —

### D39 — O mundo do jogo deve exigir do jogador a percepção de detalhes

- Categoria: Atenção
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D39.1 — Nível AA

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *cenário jogável*: cada espaço do jogo (mapa, sala ou fase) em que o jogador executa ações e em que há uma missão em curso; cenário em que nenhuma missão está em curso (hub, sandbox) não tem caminho obrigatório e não é cenário jogável
- *caminho obrigatório (caminho da missão)*: a sequência de objetivos exigidos para completar a missão em curso, e fora do caminho obrigatório é tudo o que nenhum desses objetivos exige
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *detalhe*: um elemento visível de um cenário jogável (objeto, forma, cor, posição, quantidade, inscrição ou mudança de estado de um objeto) cujo valor ou cuja presença o jogador precisa para resolver o desafio, e não são detalhe o elemento da interface (menu, painel, inventário, barra de status) nem o texto do enunciado da questão ou da instrução do jogo; o desafio exige o detalhe quando a condição de conclusão do desafio depende do valor ou da presença do detalhe (uma resposta, um código ou uma ação sobre o elemento) e o jogo não fornece a mesma informação por outro meio, isto é, por texto, fala, dica ou item do jogo que a informe, e a tentativa e erro sem essa informação não é outro meio; o detalhe é sinalizado explicitamente quando o jogo dá ao elemento, antes de o jogador agir sobre ele, ao menos um destes sinais: marcador (ícone, seta, ponto em mapa ou bússola), destaque (brilho, contorno, mudança de cor, animação ou partícula no elemento, exibidos desde o início ou por proximidade) ou instrução, dica ou fala que cita o elemento e informa onde ele está ou qual valor deve ser lido dele; a instrução que só nomeia a categoria do que procurar (como "procure pistas") não sinaliza o elemento, e o realce exibido só depois de o jogador apontar o cursor para o elemento ou tocá-lo não é sinalização

**Enunciado.** Ao menos um desafio do jogo exige um detalhe do cenário jogável que não é sinalizado explicitamente

**Justificativa do nível.** essencialidade média, viabilidade alta. A atenção voluntária é, em Vigotski, uma função psicológica superior que se forma pela mediação de signos: o sujeito aprende a dirigir a atenção ao que o meio e o outro lhe indicam. Um desafio que exige notar um detalhe não sinalizado dá ao jogador a tarefa de selecionar sozinho o que é relevante no cenário, o que exercita essa função, ao passo que seguir marcadores só a delega ao jogo. A essencialidade é média porque a aprendizagem também ocorre em desafios sinalizados; por isso basta que ao menos um desafio exija o detalhe, o mínimo que mostra que o mundo do jogo demanda essa percepção. Colocar um elemento sem marcador e fazer a conclusão depender dele é decisão de projeto de baixo custo; viabilidade alta.

**Evidência.**
- Código: Listar os desafios cuja condição de conclusão lê o valor, a presença ou a interação com um elemento do cenário (comparação com atributo de objeto, código digitado que consta em inscrição do cenário, objeto que precisa ser achado, mudança de estado a observar). Em cada elemento, verificar se existe marcador, destaque ou instrução, dica ou fala que o cite e informe onde está ou o valor a ler, e se o jogo fornece a mesma informação por outro meio (texto, fala, dica, item). Regra de desempate: se as fontes divergirem sobre um desafio, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o desafio conta como sem código para esse desafio, e GDD que não descreve o desafio conta como sem GDD para esse desafio. O vídeo mostra os sinais exibidos ao jogador gravado, mas a dica pedida pelo jogador não aparece se ele não a pediu; por isso o vídeo confirma a sinalização quando a mostra e não prova a ausência de sinalização. Sem código nem GDD, o vídeo decide só pelo que mostra: o grau é atendido quando o vídeo mostra um desafio resolvido pela ação sobre um detalhe ao qual nenhum sinal visto ou ouvido no vídeo se refere, anotando que dicas não pedidas pelo jogador gravado podem existir; parcial quando mostra desafio resolvido pela ação sobre um detalhe e mostra sinal que o aponta; nao_atendido nos demais casos, anotando que o grau decorre da falta de evidência
  - os desafios cuja condição de conclusão depende do valor, da presença ou da ação sobre um elemento do cenário jogável foram listados, cada um com o elemento exigido (mínimo 0 desafios)
  - em ao menos um desafio listado, o elemento exigido não tem marcador nem destaque no código (sem componente, ícone, contorno, brilho, partícula ou animação que o assinale antes da ação do jogador) e nenhum texto, dica ou fala do jogo o cita informando onde está ou qual valor ler
  - em ao menos um desafio listado, o jogo não fornece por outro meio (texto, fala, dica ou item) a informação que o elemento contém
  - se existem desafios que exigem detalhe e todos os detalhes são sinalizados, anotar (indica o estado parcial)
  - se nenhuma condição de conclusão depende de elemento do cenário, anotar (indica o estado nao_atendido)
- Documentação: Verificar no GDD ou documento equivalente os desafios que dependem de um elemento do cenário, o detalhe exigido e o que o jogo apresenta ao jogador sobre esse detalhe. Regra de desempate: se as fontes divergirem sobre um desafio, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o desafio conta como sem código para esse desafio, e GDD que não descreve o desafio conta como sem GDD para esse desafio. O vídeo mostra os sinais exibidos ao jogador gravado, mas a dica pedida pelo jogador não aparece se ele não a pediu; por isso o vídeo confirma a sinalização quando a mostra e não prova a ausência de sinalização. Sem código nem GDD, o vídeo decide só pelo que mostra: o grau é atendido quando o vídeo mostra um desafio resolvido pela ação sobre um detalhe ao qual nenhum sinal visto ou ouvido no vídeo se refere, anotando que dicas não pedidas pelo jogador gravado podem existir; parcial quando mostra desafio resolvido pela ação sobre um detalhe e mostra sinal que o aponta; nao_atendido nos demais casos, anotando que o grau decorre da falta de evidência
  - o GDD descreve ao menos um desafio cuja conclusão depende de um detalhe do cenário jogável e identifica o detalhe (mínimo 0 desafios)
  - o GDD descreve que o detalhe é deixado para o jogador perceber, sem marcador, destaque, instrução, dica ou fala que o aponte
  - o GDD descreve que a informação do detalhe não é fornecida por outro meio
  - se o GDD descreve desafio que depende de detalhe e descreve que todo detalhe tem marcador, destaque, instrução ou dica que o aponta, anotar (indica o estado parcial)
- Vídeo: O vídeo só confirma a evidência de código ou do GDD, e a ausência de sinalização no vídeo não prova que o jogo não a tem. Registrar cada desafio resolvido no vídeo, o elemento do cenário sobre o qual o jogador agiu ou do qual leu um valor e, nos instantes anteriores à ação, os marcadores, destaques, textos ou falas exibidos que se refiram a esse elemento. Regra de desempate: se as fontes divergirem sobre um desafio, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o desafio conta como sem código para esse desafio, e GDD que não descreve o desafio conta como sem GDD para esse desafio. O vídeo mostra os sinais exibidos ao jogador gravado, mas a dica pedida pelo jogador não aparece se ele não a pediu; por isso o vídeo confirma a sinalização quando a mostra e não prova a ausência de sinalização. Sem código nem GDD, o vídeo decide só pelo que mostra: o grau é atendido quando o vídeo mostra um desafio resolvido pela ação sobre um detalhe ao qual nenhum sinal visto ou ouvido no vídeo se refere, anotando que dicas não pedidas pelo jogador gravado podem existir; parcial quando mostra desafio resolvido pela ação sobre um detalhe e mostra sinal que o aponta; nao_atendido nos demais casos, anotando que o grau decorre da falta de evidência
  - os desafios resolvidos no vídeo por ação sobre um elemento do cenário ou leitura de valor nele foram registrados, cada um com o elemento e o instante (mínimo 0 desafios)
  - em ao menos um desafio registrado, nenhum marcador, destaque, texto ou fala visto ou ouvido no vídeo se refere ao elemento antes da ação do jogador
  - os desafios registrados em que o vídeo mostra sinal que aponta o elemento foram anotados (indica o estado parcial quando todo detalhe observado é sinalizado)

**Escala.**
- Atendido: Existe ao menos um desafio que exige um detalhe do cenário jogável não sinalizado explicitamente, nos termos do enunciado e das definições
- Parcial: Existe ao menos um desafio que exige um detalhe do cenário jogável, nos termos do enunciado e das definições, mas todo detalhe exigido é sinalizado explicitamente
- Não atendido: Nenhum desafio exige um detalhe do cenário jogável, nos termos do enunciado e das definições (inclui desafio resolvido sem notar elemento do cenário e desafio cuja informação o jogo fornece também por texto, fala, dica ou item)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente ao menos um desafio cuja conclusão depende de um detalhe do cenário jogável, com o detalhe identificado. Registrar que esse detalhe é deixado para o jogador perceber, sem marcador, destaque, instrução, dica ou fala que o aponte. Registrar que a informação desse detalhe não é fornecida por outro meio
- Design: Definir, em ao menos um desafio, uma condição de conclusão que dependa do valor ou da presença de um detalhe do cenário jogável, nos termos das definições. Definir que esse detalhe não tenha marcador, destaque nem instrução, dica ou fala que informe onde o detalhe está ou qual valor ler desse detalhe. Definir que o jogo não forneça a informação desse detalhe por texto, fala, dica ou item
- Código: Acrescentar ou usar, em ao menos um desafio, uma condição de conclusão que leia o valor, a presença ou a interação com um elemento do cenário jogável. Remover desse elemento o componente, ícone, contorno, brilho, partícula ou animação que o assinale antes da ação do jogador. Remover os textos, dicas e falas que citem esse elemento informando onde o elemento está ou qual valor ler desse elemento. Remover o texto, a fala, a dica ou o item que forneça por outro meio a informação que esse elemento contém

**Depende de.** —

### D40 — O jogo deve viabilizar o aprendizado também pelos erros do jogador com mensagens textuais, sons e animações

- Categoria: Aprendizado
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D40.1 — Nível A

**Definições.**

- *missão*: uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão
- *minijogo*: uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela
- *desafio*: cada missão ou minijogo
- *GDD ou documento equivalente*: o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta
- *erro*: uma ação do jogador que o jogo avalia como incorreta em relação ao objetivo da missão ou do desafio (resposta errada, objeto ou ordem errados, violação de regra) e à qual responde, e não são erro a inação do jogador nem o esgotamento do tempo sem ação incorreta
- *resposta ao erro*: tudo o que o jogo exibe ou toca em consequência do erro, do momento em que o avalia até o jogador poder agir de novo
- *modalidade*: cada um destes canais: texto (palavras escritas exibidas na tela), som (efeito sonoro, música ou fala audíveis, disparados pelo erro) e animação (mudança visual em movimento, de posição, forma, cor ou tamanho, de elemento do cenário ou da interface, disparada pelo erro e que se desenrola no tempo; a imagem estática, como um ícone fixo, não conta); a resposta usa uma modalidade quando ao menos um elemento dela pertence a essa modalidade, e a fala que lê em voz alta um texto conta como som, além de o texto contar como texto
- *informação sobre o erro*: o que estava errado (cita ou mostra qual resposta, objeto ou ação estava incorreto, ou por quê) ou o que fazer em seguida (ação, conteúdo a rever ou dica específica ao erro), comunicado por ao menos uma das modalidades usadas (texto ou fala que o diz, animação que mostra o elemento incorreto ou o efeito do erro)
- *sinal de falha*: o que só indica que houve erro (mensagem como "Errou" ou "Tente novamente", X ou cor vermelha fixos, buzina ou outro efeito sonoro sem fala, piscar da tela, perda de pontos) e não é informação sobre o erro, e o som cujo conteúdo não pode ser determinado (áudio sem transcrição, no código, no GDD ou no vídeo) conta como sinal de falha
- *tipo de erro*: cada ramo ou condição que o jogo avalia como incorreta, em cada missão, minijogo ou tipo de interação
- *resposta avaliada*: a resposta a um erro sobre o qual há evidência: no código e no GDD, a resposta a cada tipo de erro tratado ou descrito; no vídeo, toda resposta a erro observada
- *escopo*: este critério avalia a multimodalidade da resposta e a presença de informação sobre o erro: a orientação da próxima ação, que D17.1 exige, e a variação da mensagem conforme a ação ou o histórico do jogador, tratada em D18, não são avaliadas aqui
- *cenário* (sentido corrente): em «elemento do cenário ou da interface» (local modalidade), cenário está no sentido corrente de ambiente visual do jogo, e não no de cenário jogável (D29)

**Enunciado.** Existe ao menos uma resposta avaliada a erro do jogador e todas as respostas avaliadas usam ao menos duas modalidades (texto, som, animação) e carregam informação sobre o erro

**Justificativa do nível.** essencialidade alta, viabilidade alta. Na mediação vigotskiana, o outro mais experiente ajusta o apoio ao que o aprendiz ainda não faz sozinho, e o erro é o ponto em que esse apoio é necessário. Som de falha ou X sinalizam que houve erro sem dizer o que rever, e uma resposta em um único canal fica sem alternativa quando o jogador não a percebe; por isso o critério exige ao menos duas das três modalidades, o menor número que dá redundância de canal, e que a resposta carregue informação sobre o erro. D40.1 depende de D17.1 porque, no jogo que cumpre D17.1, a informação transmitida pelas modalidades é a mensagem de orientação que ela exige; sem ela, texto, som e animação tendem a repetir só o sinal de falha. Associar texto, som e animação ao evento de erro é recurso comum nos motores de jogo; viabilidade alta.

**Evidência.**
- Código: Localizar os ramos de erro e falha de missão, minijogo e interação (condições avaliadas como incorretas e seus manipuladores de evento, ou handlers) e, em cada um, listar o que é exibido (texto), tocado (som, fala) e animado em resposta. Verificar se ao menos uma modalidade comunica o que estava errado ou o que fazer, e se o conteúdo do som é determinável. Regra de desempate: se as fontes divergirem sobre um tipo de erro, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o tipo de erro conta como sem código para esse tipo, e GDD que não descreve esse tipo conta como sem GDD para esse tipo; o vídeo só traz respostas a erros que o jogador gravado cometeu, e a ausência de erro no vídeo não prova que o jogo não responde; sem resposta observada no vídeo, o grau pelo vídeo é nao_atendido por falta de evidência, anotado como tal
  - todos os tipos de erro tratados no código foram listados, cada um com as respostas por modalidade (texto, som, animação) (mínimo 0 tipos)
  - em cada tipo de erro listado, a resposta usa ao menos duas modalidades
  - em cada tipo de erro listado, ao menos uma modalidade usada comunica o que estava errado ou o que fazer em seguida, e não só sinal de falha
  - os tipos de erro cuja resposta tem uma só modalidade, ou só sinal de falha, foram anotados (indica o estado parcial quando ao menos um tipo atende aos dois itens anteriores)
- Documentação: Verificar no GDD ou documento equivalente a especificação da resposta a cada tipo de erro: o texto, o som e a animação previstos e o que cada um informa. Regra de desempate: se as fontes divergirem sobre um tipo de erro, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o tipo de erro conta como sem código para esse tipo, e GDD que não descreve esse tipo conta como sem GDD para esse tipo; o vídeo só traz respostas a erros que o jogador gravado cometeu, e a ausência de erro no vídeo não prova que o jogo não responde; sem resposta observada no vídeo, o grau pelo vídeo é nao_atendido por falta de evidência, anotado como tal
  - o GDD lista os tipos de erro e, em cada um, as respostas por modalidade (texto, som, animação) (mínimo 0 tipos)
  - em cada tipo de erro listado, o GDD descreve resposta em ao menos duas modalidades
  - em cada tipo de erro listado, o GDD descreve que ao menos uma modalidade comunica o que estava errado ou o que fazer em seguida
  - os tipos de erro descritos com uma só modalidade, ou só com sinal de falha, foram anotados (indica o estado parcial quando ao menos um tipo atende aos dois itens anteriores)
- Vídeo: O vídeo só confirma a evidência de código ou do GDD. Registrar o instante de cada erro cometido pelo jogador gravado e, na resposta do jogo, as modalidades usadas (texto exibido, som ou fala audíveis, animação), transcrevendo o texto e a fala e descrevendo a animação. Regra de desempate: se as fontes divergirem sobre um tipo de erro, vale o código; sem código, o GDD; sem ambos, o vídeo; código que existe mas não traz dado sobre o tipo de erro conta como sem código para esse tipo, e GDD que não descreve esse tipo conta como sem GDD para esse tipo; o vídeo só traz respostas a erros que o jogador gravado cometeu, e a ausência de erro no vídeo não prova que o jogo não responde; sem resposta observada no vídeo, o grau pelo vídeo é nao_atendido por falta de evidência, anotado como tal
  - todas as respostas a erro observadas no vídeo foram registradas, cada uma com instante, modalidades, texto ou fala transcritos e animação descrita (mínimo 0 respostas)
  - cada resposta registrada usa ao menos duas modalidades
  - cada resposta registrada tem ao menos uma modalidade que comunica o que estava errado ou o que fazer em seguida, e não só sinal de falha
  - as respostas registradas com uma só modalidade, ou só com sinal de falha, foram anotadas (indica o estado parcial quando ao menos uma resposta atende aos dois itens anteriores)

**Escala.**
- Atendido: Existe ao menos uma resposta avaliada a erro do jogador e todas as respostas avaliadas usam ao menos duas modalidades e carregam informação sobre o erro, nos termos do enunciado e das definições
- Parcial: Ao menos uma resposta avaliada usa ao menos duas modalidades e carrega informação sobre o erro, nos termos do enunciado e das definições, e ao menos outra resposta avaliada não atende a esses dois requisitos
- Não atendido: Nenhuma resposta avaliada usa ao menos duas modalidades e carrega informação sobre o erro, nos termos do enunciado e das definições, ou não existe resposta avaliada (inclui resposta só com sinal de falha)

**Recomendações.**
- Documentação: Registrar no GDD ou documento equivalente os tipos de erro e, em cada um, a resposta em ao menos duas modalidades (texto, som, animação). Registrar, em cada tipo de erro, a modalidade que comunica o que estava errado ou o que fazer em seguida
- Design: Definir ao menos um tipo de erro do jogador com resposta do jogo. Definir, para cada tipo de erro, uma resposta com ao menos duas modalidades (texto, som, animação). Incluir em cada resposta, em ao menos uma das modalidades usadas, informação sobre o erro, nos termos das definições, e não só sinal de falha
- Código: Acrescentar ou usar ao menos um ramo de erro com manipulador de evento (handler) que responda a uma ação avaliada como incorreta. Acrescentar, em cada ramo de erro de missão, minijogo e interação, a modalidade que falta para que a resposta use ao menos duas (texto exibido, som ou fala tocados, animação disparada pelo erro). Acrescentar ou usar, em cada ramo de erro, ao menos uma modalidade que comunique o que estava errado ou o que fazer em seguida, e não só sinal de falha. Acrescentar a transcrição de cada fala usada para comunicar essa informação

**Depende de.** (D17.1)
