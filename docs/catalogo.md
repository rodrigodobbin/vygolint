<!-- ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão. -->
# Catálogo vygolint — diretrizes e critérios de conformidade

Fonte das diretrizes: CARVALHO, Diego Marques. *Diretrizes para o desenvolvimento de jogos educacionais digitais embasados na teoria sociointeracionista de Lev Semionovich Vigotski*. Dissertação (Mestrado), UFABC, 2020. Quadro 3.

> Carvalho (2020, seção 4.4) suprimiu as categorias na apresentação final das diretrizes por considerar que rotular, classificar e ordenar requisitos pode gerar a falsa impressão de que a teoria de Vigotski também pode ser classificada assim. O vygolint usa as categorias apenas como instrumento de organização e de relatório, não como taxonomia da teoria.

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

## Diretrizes

### D01 — Os desafios do jogo devem ser direcionados a resolução de problemas

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D01.1 — Nível A

**Enunciado.** Cada missão ou minijogo apresenta uma situação-problema, isto é, uma situação com estado inicial, objetivo e mais de uma ação possível, cuja resolução exige uma decisão do jogador, e não apenas a repetição de uma mesma ação; escolher entre alternativas prontas, sem estado inicial a ser transformado pelas ações do jogador, não conta como situação-problema

**Justificativa do nível.** essencialidade alta, viabilidade alta. Para Vigotski a aprendizagem nasce da atividade do sujeito sobre um problema, e o conhecimento é construído quando o jogador precisa operar com os conceitos, não quando os reproduz. Em um desafio de repetição mecânica o jogador executa a mesma ação sem escolher entre alternativas, de modo que a atividade não exige operar com o conteúdo. Estruturar desafios como situações-problema é uma decisão de projeto, sem custo técnico adicional.

**Evidência.**
- Código: não se aplica
- Documentação: Listar no documento de design (GDD) ou documento equivalente cada missão e minijogo e identificar a situação-problema (estado inicial, objetivo e ações possíveis) e as decisões previstas. Situação-problema exige estado inicial, objetivo e mais de uma ação possível; escolher entre alternativas prontas, sem estado inicial a ser transformado pelas ações do jogador, não conta. Indicadores: cada missão ou minijogo descreve uma situação-problema, isto é, uma situação com estado inicial, objetivo e mais de uma ação possível; a resolução descrita exige uma decisão do jogador e não se reduz a repetir uma mesma ação nem a escolher entre alternativas prontas, sem estado inicial a ser transformado pelas ações do jogador
- Vídeo: Registrar o início e o fim de cada missão ou minijogo observado, anotar o estado inicial, o objetivo e as ações disponíveis ao jogador e anotar qual decisão ele tomou para concluí-lo. Situação-problema exige estado inicial, objetivo e mais de uma ação possível; escolher entre alternativas prontas, sem estado inicial a ser transformado pelas ações do jogador, não conta. Indicadores: todas as missões e minijogos presentes no vídeo foram registrados (mínimo 1); cada um apresenta uma situação-problema: estado inicial visível, objetivo e mais de uma ação disponível ao jogador; o jogador resolve a situação por ações que transformam o estado inicial, e não apenas escolhendo entre alternativas prontas; concluir o desafio não depende de repetir a mesma ação até o fim

**Escala.**
- Atendido: Todas as missões e minijogos observados ou documentados apresentam uma situação-problema, nos termos do enunciado, cuja resolução exige uma decisão do jogador
- Parcial: Ao menos uma missão ou minijogo apresenta uma situação-problema, nos termos do enunciado, e ao menos outra não apresenta, por se resolver repetindo uma ação ou escolhendo entre alternativas prontas sem estado inicial a ser transformado
- Não atendido: Nenhuma missão ou minijogo apresenta uma situação-problema, nos termos do enunciado

**Depende de.** —

### D02 — Avaliar os conteúdos ensinados no jogo de forma a transcender o contexto que eles foram abordados, possibilitando a transposição dos conceitos para resolução de outras situações-problema

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D02.1 — Nível A

**Enunciado.** Cada conceito listado como objetivo de aprendizagem no GDD ou documento equivalente é cobrado ao menos uma vez em uma missão ou cenário com estrutura de problema diferente daquela em que foi introduzido

**Justificativa do nível.** essencialidade alta, viabilidade media. Em Vigotski, conceitos científicos se consolidam quando o sujeito os generaliza e os usa de modo consciente em situações novas, e não quando os repete no contexto de origem. Avaliar apenas na situação de introdução mede memorização do contexto, não domínio do conceito. Exige planejar variações de situação para cada conteúdo, o que aumenta o esforço de conteúdo e de design; viabilidade média.

**Evidência.**
- Código: não se aplica
- Documentação: Extrair do GDD ou documento equivalente a lista de objetivos de aprendizagem e mapear, para cada conceito, a missão ou cenário de introdução e as missões ou cenários em que ele é cobrado. Se o documento não lista objetivos de aprendizagem, registrar a ausência e classificar o critério como nao_atendido. Considerar estrutura de problema diferente quando mudam o objetivo da missão ou o conjunto de objetos ou dados que o jogador manipula; mudar apenas o mapa ou a aparência do cenário não conta. Indicadores: tabela ou lista associando cada conceito do GDD ou documento equivalente, a missão ou cenário de introdução e a missão ou cenário de avaliação; para cada conceito, a missão de avaliação tem objetivo ou conjunto de objetos ou dados manipulados diferente do da missão de introdução
- Vídeo: Para cada conceito listado no GDD ou documento equivalente, registrar a missão e o momento em que ele é introduzido e a missão em que o mesmo conceito é cobrado depois, comparando o objetivo e os objetos manipulados nas duas. Indicadores: o conceito aparece em duas missões ou cenários diferentes; o desafio da segunda missão só se resolve aplicando o conceito apresentado na primeira e tem objetivo ou objetos manipulados diferentes

**Escala.**
- Atendido: Todos os conceitos listados como objetivo de aprendizagem no GDD ou documento equivalente são cobrados ao menos uma vez em missão ou cenário com estrutura de problema diferente da de introdução
- Parcial: Ao menos um conceito listado é cobrado em missão ou cenário com estrutura de problema diferente da de introdução, e ao menos outro conceito listado não é cobrado fora da situação em que foi apresentado (inclui o conceito que não é cobrado em nenhuma missão ou cenário)
- Não atendido: Nenhum conceito listado é cobrado fora da situação em que foi introduzido (inclui o conceito que não é cobrado em nenhuma missão ou cenário), ou o GDD ou documento equivalente não lista objetivos de aprendizagem

**Depende de.** —

### D03 — O desenvolvimento das atividades/missões/minijogos deve ser autorregulado pelo jogador

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D03.1 — Nível A

**Enunciado.** Em ao menos um ponto do jogo, o jogador pode escolher entre duas ou mais atividades, missões ou minijogos disponíveis ao mesmo tempo e iniciar a escolhida

**Justificativa do nível.** essencialidade alta, viabilidade media. Em Vigotski, a autorregulação é o movimento em que o controle da própria ação passa do outro para o aprendiz, e decidir o que fazer a seguir é parte desse controle. Num jogo estritamente linear a ordem é decidida pelo sistema, e o jogador apenas executa a sequência. Oferecer atividades em paralelo exige estrutura de progressão não linear e conteúdo que não dependa de uma ordem fixa; viabilidade média.

**Evidência.**
- Código: Localizar a lógica de desbloqueio de missões e minijogos e verificar se há algum estado do jogo em que duas ou mais atividades estão desbloqueadas ao mesmo tempo e selecionáveis. Verificar também, dentro de cada atividade, se o código aceita mais de uma ordem para executar as ações (objetos, perguntas ou etapas). Indicadores: existe estado do jogo em que duas ou mais atividades estão desbloqueadas simultaneamente; a atividade iniciada é determinada por entrada do jogador (menu, mapa, interação), não por ordem fixa no código; dentro de ao menos uma atividade, o código aceita mais de uma ordem para executar as ações (objetos, perguntas ou etapas), sem impor sequência fixa
- Documentação: não se aplica
- Vídeo: Registrar os pontos em que o jogo oferece atividades e anotar quantas estão disponíveis e qual o jogador inicia. Registrar também, dentro de cada atividade, se a interface apresenta duas ou mais ações (objetos, perguntas ou etapas) disponíveis ao mesmo tempo e em que ordem o jogador as executa. Indicadores: ao menos um ponto em que duas ou mais atividades aparecem disponíveis ao mesmo tempo (menu, mapa ou cenário); o jogador inicia uma delas; a outra pode permanecer disponível, ser iniciada depois ou ficar indisponível após a escolha (escolha excludente); dentro de ao menos uma atividade, a interface apresenta duas ou mais ações (objetos, perguntas ou etapas) disponíveis ao mesmo tempo e o jogador escolhe a ordem de execução

**Escala.**
- Atendido: Em ao menos um ponto, o jogador escolhe entre duas ou mais atividades, missões ou minijogos disponíveis ao mesmo tempo
- Parcial: O jogador não escolhe entre atividades, missões ou minijogos, mas escolhe a ordem das ações dentro de uma atividade (como objetos, perguntas ou etapas)
- Não atendido: As atividades, missões e minijogos se sucedem numa única ordem definida pelo jogo, e dentro de cada uma a ordem das ações também é fixa

**Depende de.** —

#### D03.2 — Nível A

**Enunciado.** O jogador inicia cada atividade, missão ou minijogo por uma ação própria e o jogo não avança de uma para a próxima sem essa ação

**Justificativa do nível.** essencialidade alta, viabilidade alta. Atividade, em Vigotski, é conduzida pelo sujeito; a autorregulação inclui decidir o momento de passar de uma etapa à seguinte. Se o jogo encadeia as etapas sozinho, o controle da transição permanece no sistema. Basta condicionar a transição a uma ação do jogador, o que não exige recurso técnico especial.

**Evidência.**
- Código: Localizar as transições entre missões e minijogos e verificar o que as dispara. Indicadores: a transição é disparada por entrada do jogador (botão, escolha, interação); não há transição disparada apenas por temporizador ou por término automático da etapa anterior
- Documentação: não se aplica
- Vídeo: Registrar cada transição entre atividades e anotar se houve ação do jogador antes da mudança. Indicadores: todas as transições presentes no vídeo foram registradas (mínimo 1); cada transição é precedida por ação do jogador

**Escala.**
- Atendido: Todas as transições observadas ou identificadas no código dependem de ação do jogador
- Parcial: Ao menos uma transição depende de ação do jogador e ao menos outra ocorre automaticamente
- Não atendido: As atividades se sucedem automaticamente, sem ação do jogador

**Depende de.** —

#### D03.3 — Nível A

**Enunciado.** Nenhuma atividade tem limite de tempo obrigatório para ser concluída, ou o limite pode ser desativado ou ampliado pelo jogador; limite obrigatório é um temporizador cujo esgotamento encerra ou reprova a atividade

**Justificativa do nível.** essencialidade alta, viabilidade alta. Em Vigotski, a mediação precisa responder ao ritmo com que o aprendiz elabora a tarefa, e esse ritmo não é conhecido de antemão pelo jogo. Um temporizador obrigatório impõe a todos o mesmo ritmo e leva o jogador a responder antes de elaborar. Remover o limite ou torná-lo opcional é de baixo custo.

**Evidência.**
- Código: Procurar temporizadores associados a missões e minijogos e verificar o que ocorre quando o tempo se esgota e se há opção de desativá-los. Indicadores: existência de temporizador com consequência de falha ao esgotar; existência de configuração que desativa ou amplia o temporizador
- Documentação: Verificar no GDD as regras de tempo de cada atividade. Indicadores: indicação de quais atividades têm limite de tempo; indicação de opção do jogador para alterar o limite
- Vídeo: Observar cada atividade registrando se há contador de tempo visível, o que ocorre quando ele chega a zero e se o jogador pode permanecer na atividade sem limite. Indicadores: todas as atividades presentes no vídeo foram observadas (mínimo 1); o jogador permanece na atividade sem ser interrompido por esgotamento de tempo; não há contador de tempo visível cujo esgotamento encerre ou reprove a atividade; se há contador visível e o vídeo mostra seu esgotamento, a atividade não termina nem falha

**Escala.**
- Atendido: Nenhuma atividade tem limite de tempo obrigatório, ou o jogador pode desativar ou ampliar o limite
- Parcial: Ao menos uma atividade tem limite de tempo obrigatório e ao menos outra não tem
- Não atendido: Todas as atividades têm limite de tempo obrigatório que o jogador não pode alterar

**Depende de.** —

### D04 — O jogador deve interagir com os objetos dos cenários

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D04.1 — Nível A

**Enunciado.** Ao menos um objeto de cada cenário responde à interação do jogador com mudança de estado ou informação que se relaciona a um objetivo de aprendizagem listado no GDD (ou documento equivalente)

**Justificativa do nível.** essencialidade alta, viabilidade alta. Para Vigotski o conhecimento é construído na atividade sobre objetos e instrumentos, e interagir com o ambiente é a forma pela qual o jogador exerce essa atividade. Um cenário apenas contemplativo reduz o jogador a espectador, e um objeto que responde sem relação com o conteúdo mantém a interação fora da atividade de aprender. Programar resposta a clique, toque ou colisão é recurso básico de qualquer motor de jogo.

**Evidência.**
- Código: Listar os objetos de cada cenário que têm manipulador de evento (handler) de interação (clique, toque, colisão, uso de item) e o efeito de cada manipulador, e comparar o efeito com os objetivos de aprendizagem do GDD. Considerar que o efeito se relaciona a um objetivo quando a informação exibida ou o novo estado enuncia, exemplifica ou testa um conceito listado, ou é dado necessário para resolver um desafio ligado a ele. Indicadores: cada cenário tem ao menos um objeto com manipulador de evento de interação; o efeito do manipulador é mudança de estado ou exibição de informação que se relaciona a um objetivo de aprendizagem do GDD
- Documentação: não se aplica
- Vídeo: Percorrer cada cenário observado registrando os objetos com os quais o jogador interage e a resposta obtida, e comparar a resposta com os objetivos de aprendizagem do GDD. Considerar que a resposta se relaciona a um objetivo quando a informação exibida ou o novo estado enuncia, exemplifica ou testa um conceito listado, ou é dado necessário para resolver um desafio ligado a ele. Indicadores: ao menos um objeto interagido por cenário; o objeto muda de estado ou exibe informação que se relaciona a um objetivo de aprendizagem do GDD

**Escala.**
- Atendido: Todos os cenários têm ao menos um objeto que responde à interação com mudança de estado ou informação que se relaciona a um objetivo de aprendizagem do GDD
- Parcial: Ao menos um cenário tem objeto que responde nesse sentido e ao menos outro cenário não tem
- Não atendido: Nenhum cenário tem objeto que responda à interação do jogador com mudança de estado ou informação que se relaciona a um objetivo de aprendizagem do GDD

**Depende de.** —

### D05 — O jogador deve explorar livremente o cenário

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D05.1 — Nível A

**Enunciado.** Em todos os cenários jogáveis, o jogador alcança áreas ou objetos que não pertencem ao caminho da missão em curso, sem que o jogo o impeça ou o conduza de volta ao objetivo; caminho da missão é a sequência de objetivos exigidos para completá-la

**Justificativa do nível.** essencialidade alta, viabilidade media. Em Vigotski o conhecimento se constrói na atividade do sujeito sobre o meio, e é o jogador quem decide o que investigar. Um cenário reduzido ao caminho da missão limita essa atividade ao que o jogo prescreve e converte a exploração em seguimento de instruções. Construir áreas além do caminho principal acrescenta trabalho de arte e de nível; viabilidade média.

**Evidência.**
- Código: Localizar, em cada cenário jogável, os acessos a áreas ou objetos que nenhum objetivo da missão exige (portas, colisores, gatilhos, verificações do estado da missão) e verificar se alguma condição impede o acesso, interrompe o jogador ou o reposiciona no caminho da missão. Indicadores: existem áreas ou objetos fora do caminho da missão com acesso ou interação ativos; nenhuma verificação do estado da missão bloqueia o acesso a essas áreas ou objetos; nenhuma lógica interrompe o jogador ou o reposiciona no caminho da missão quando ele se afasta dele
- Documentação: Identificar no GDD ou nos mapas de nível, para cada cenário, os objetivos que compõem o caminho da missão e as áreas ou objetos que nenhum desses objetivos exige. Indicadores: o GDD ou mapa descreve áreas ou objetos acessíveis fora do caminho da missão, isto é, que nenhum objetivo da missão exige; o GDD descreve o deslocamento do jogador até essas áreas durante a missão; o GDD descreve essas áreas ou objetos como acessíveis em qualquer estado da missão e descreve que o jogador pode sair do caminho e voltar a ele sem ser interrompido nem reposicionado
- Vídeo: Nos momentos em que o jogador deixa o caminho da missão, registrar o que o jogo faz em seguida. O vídeo só confirma a evidência de código ou documentação: a ausência de saída do caminho no vídeo não é evidência de restrição nem de liberdade, e interrupção, bloqueio ou reposicionamento observados valem como evidência de restrição. Indicadores: em cada saída do caminho da missão registrada no vídeo (mínimo 0), o jogo não interrompe, bloqueia nem reposiciona o jogador

**Escala.**
- Atendido: Todos os cenários jogáveis têm áreas ou objetos fora do caminho da missão acessíveis sem bloqueio
- Parcial: Ao menos um cenário tem áreas ou objetos acessíveis fora do caminho da missão e ao menos outro cenário restringe o jogador ao caminho
- Não atendido: Nenhum cenário permite alcançar áreas ou objetos fora do caminho da missão em curso

**Depende de.** —

### D06 — O jogador deve trocar informações com outros jogadores por comunicação síncrona

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D06.1 — Nível AAA

**Enunciado.** Durante a sessão, o jogador envia e recebe mensagens de texto ou voz de outros jogadores em tempo real

**Justificativa do nível.** essencialidade media, viabilidade baixa. Socialização entre pares é constitutiva do sociointeracionismo, mas a interação social também pode ocorrer de forma assíncrona (D07) ou fora do jogo (D22); por isso essencialidade média. Comunicação síncrona exige infraestrutura de rede e sessão multijogador, rara em jogos educacionais; viabilidade baixa.

**Evidência.**
- Código: Procurar módulo de rede, chat ou voz e verificar se envia e recebe mensagens entre clientes durante a partida. Indicadores: existe canal de mensagens entre jogadores conectados; mensagens chegam sem exigir fim da sessão
- Documentação: Verificar no GDD a seção de multijogador ou comunicação. Indicadores: especificação de chat, voz ou mensagens em tempo real
- Vídeo: Observar sessão com dois ou mais jogadores e registrar trocas de mensagens. Indicadores: ao menos uma troca de mensagem com resposta na mesma sessão

**Escala.**
- Atendido: Canal síncrono existe e o vídeo mostra troca de mensagens livres entre jogadores
- Parcial: Canal existe, mas limitado a mensagens prontas, emotes ou sinais sem conteúdo livre
- Não atendido: Não há comunicação entre jogadores durante a sessão

**Depende de.** —

### D07 — O jogador deve trocar informações com outros jogadores por meio de comunicação assíncrona

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D07.1 — Nível AA

**Enunciado.** O jogo persiste mensagens ou registros deixados por um jogador e os exibe a outros jogadores em sessões posteriores

**Justificativa do nível.** essencialidade media, viabilidade media. Mesma base de D06: socialização entre pares. A forma assíncrona exige apenas persistência de dados e um ponto de leitura no jogo, viável sem sessão multijogador simultânea.

**Evidência.**
- Código: Procurar persistência de mensagens, comentários ou registros de jogador e o ponto onde outros jogadores os leem. Indicadores: escrita de mensagem associada a jogador e contexto; leitura de mensagens de outros jogadores em sessão distinta
- Documentação: Verificar no GDD mecânicas de mural, bilhetes, diário compartilhado ou similar. Indicadores: mecânica descrita com autor, local e leitor da mensagem
- Vídeo: Observar se o jogador encontra registros deixados por outro jogador ou deixa um registro. Indicadores: registro de outro jogador visível na sessão

**Escala.**
- Atendido: Jogador deixa e lê mensagens de outros jogadores em sessões distintas
- Parcial: Jogador só lê registros de outros, sem poder deixar os seus, ou o inverso
- Não atendido: Não há troca assíncrona entre jogadores

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
- Código: Localizar diálogos, quadros de pergunta e mecanismos de entrega ou recebimento de itens e verificar se a resposta do jogador é registrada e muda o estado ou o conteúdo seguinte; confirmar no código que duas entradas diferentes levam a saídas diferentes. Indicadores: o mecanismo emite informação ao jogador; a entrada do jogador (escolha, resposta, item) é lida pelo mecanismo; a entrada do jogador altera a próxima saída do mecanismo ou o estado do jogo, com ao menos duas entradas possíveis levando a saídas diferentes
- Documentação: não se aplica
- Vídeo: Registrar uma troca entre o jogador e personagem ou mecanismo em duas tentativas (ou duas gravações) com entradas diferentes, anotando a informação recebida, a entrada do jogador e o que o jogo exibe depois em cada tentativa. Indicadores: uma troca completa observada (informação recebida, entrada do jogador, resposta do jogo); a mesma troca repetida com outra entrada do jogador; o que o jogo exibe depois difere entre as duas tentativas

**Escala.**
- Atendido: Em ao menos uma situação, o mecanismo entrega informação, recebe a entrada do jogador e altera o que o jogo exibe a seguir conforme essa entrada
- Parcial: Em ao menos uma situação, o mecanismo recebe a entrada do jogador, mas o que o jogo exibe a seguir é o mesmo para qualquer entrada
- Não atendido: Os mecanismos apenas emitem informação ao jogador, sem receber entrada dele

**Depende de.** —

### D09 — O jogador deve se comunicar por linguagem escrita

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D09.1 — Nível AA

**Enunciado.** Em ao menos um ponto do jogo, o jogador produz texto livre, isto é, digita uma sequência de caracteres de sua escolha em um campo de entrada (ou em teclado exibido na tela que permita qualquer sequência) e o jogo a recebe, como em chat, resposta aberta, anotação ou nome de item; compor a mensagem apenas por seleção de palavras ou frases prontas não conta como texto livre

**Justificativa do nível.** essencialidade media, viabilidade alta. Em Vigotski, a linguagem é instrumento de mediação que organiza o pensamento, e a escrita exige que o sujeito formule por conta própria o que quer dizer. Quando o jogador apenas lê ou seleciona frases prontas, o jogo dispensa essa formulação. A essencialidade é média porque a comunicação também ocorre por fala (D06) ou por ação no jogo. Um campo de entrada de texto é recurso padrão das ferramentas de desenvolvimento; viabilidade alta.

**Evidência.**
- Código: Localizar campos de entrada de texto (input fields, teclados exibidos na tela) e verificar se aceitam qualquer sequência de caracteres digitada pelo jogador ou se o conteúdo é escolhido de uma lista fechada de opções. Texto livre é uma sequência de caracteres digitada pelo jogador em campo de entrada, sem ser escolhida de lista de opções prontas. Verificar também se o jogo lê o conteúdo digitado. Indicadores: existe campo de entrada de texto ou teclado na tela que aceita qualquer sequência de caracteres digitada pelo jogador, sem lista fechada de opções; um manipulador de evento (handler) ou função do jogo lê o texto digitado e o usa (exibe, guarda, envia ou avalia); se não há campo desse tipo, existe composição de mensagem ou resposta apenas por seleção de palavras ou frases prontas (usado para identificar o estado parcial)
- Documentação: não se aplica
- Vídeo: O vídeo só confirma a evidência de código: a ausência de digitação no vídeo não prova que o jogo não oferece texto livre. Registrar os momentos em que o jogador digita ou compõe texto e anotar se ele digita caracteres de sua escolha ou seleciona opções prontas. Texto livre é uma sequência de caracteres digitada pelo jogador em campo de entrada, sem ser escolhida de lista de opções prontas. Indicadores: ao menos um momento em que o jogador digita caracteres de sua escolha em campo de entrada e o texto aparece no jogo; nos momentos de composição de texto registrados (mínimo 0), o jogador seleciona palavras ou frases prontas em vez de digitar (indica o estado parcial)

**Escala.**
- Atendido: Em ao menos um ponto do jogo, o jogador digita texto livre em campo de entrada (ou teclado exibido na tela que permita qualquer sequência) e o jogo o recebe
- Parcial: O jogador compõe mensagens ou respostas apenas por seleção de palavras ou frases prontas oferecidas pelo jogo, sem digitar texto livre
- Não atendido: O jogador não produz texto em nenhum ponto do jogo; só lê, escolhe entre opções não textuais ou age sobre objetos

**Depende de.** —

### D10 — O jogo deve viabilizar o comportamento ativo do jogador

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D10.1 — Nível A

**Enunciado.** Nenhum trecho passivo do jogo dura mais de 120 segundos contínuos; trecho passivo é um intervalo contínuo em que a interface não oferece ao jogador nenhuma ação que altere o estado do jogo (mover-se, selecionar, manipular objeto, responder, construir), restando apenas assistir, ler, avançar texto ou pular cena

**Justificativa do nível.** essencialidade alta, viabilidade alta. Para Vigotski, o conhecimento se constrói na atividade do sujeito, e não na recepção de informação pronta. Longos trechos em que o jogador só assiste ou lê o tornam espectador e interrompem a atividade que sustenta a aprendizagem. Encurtar cenas e textos corridos ou intercalar ações do jogador é decisão de projeto, sem custo técnico especial; viabilidade alta.

**Evidência.**
- Código: não se aplica
- Documentação: não se aplica
- Vídeo: Assistir a toda a gravação e registrar os intervalos em que a interface não oferece ao jogador nenhuma ação que altere o estado do jogo, restando apenas assistir, ler, avançar texto ou pular cena. A classificação depende do que a interface oferece, não de o jogador agir ou não: um intervalo em que há ações disponíveis e o jogador não as usa não é trecho passivo. Medir a duração de cada trecho passivo pelos marcadores de tempo do vídeo. Avaliar somente o que foi gravado. Indicadores: todos os trechos passivos registrados no vídeo foram anotados com início e fim (mínimo 0); a duração contínua de cada trecho passivo, medida pelos marcadores de tempo, é de no máximo 120 segundos

**Escala.**
- Atendido: Nenhum trecho passivo registrado no vídeo dura mais de 120 segundos contínuos
- Parcial: Um único trecho passivo registrado no vídeo dura mais de 120 segundos contínuos
- Não atendido: Dois ou mais trechos passivos registrados no vídeo duram mais de 120 segundos contínuos cada um

**Depende de.** —

### D11 — O jogador deve coletar informações

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D11.1 — Nível A

**Enunciado.** O jogador coleta ao menos uma informação e ao menos uma informação coletada é usada depois em missão ou desafio; informação é um item, dado, texto, imagem ou medida relativo a ao menos um objetivo de aprendizagem listado no GDD ou documento equivalente; coletar é obter a informação por ação própria de modo que o jogo a guarde (inventário, diário, caderno ou painel) para consulta ou uso posterior; uso posterior é uma missão ou desafio posterior ao momento da coleta que só pode ser resolvido ou avançado com a posse, o valor ou o conteúdo dessa informação

**Justificativa do nível.** essencialidade alta, viabilidade alta. Em Vigotski, as funções psicológicas superiores, como a memória e a atenção voluntárias, se desenvolvem com apoio de instrumentos e signos externos, e registros guardados funcionam como esse apoio. Coletar informação que será necessária mais tarde obriga o jogador a selecionar, reter e relacionar dados em vez de reagir ao que está na tela. Um mecanismo de inventário ou de registro é padrão no desenvolvimento de jogos; viabilidade alta.

**Evidência.**
- Código: Localizar a mecânica de coleta (inventário, diário, caderno, painel) e as verificações dessas estruturas nas missões e desafios. Informação é um item, dado, texto, imagem ou medida relativo a ao menos um objetivo de aprendizagem do GDD ou documento equivalente. Coletar é obter por ação do jogador de modo que o jogo guarde a informação; uso posterior é uma missão ou desafio posterior à coleta que só pode ser resolvido ou avançado com a posse, o valor ou o conteúdo da informação. Indicadores: uma ação do jogador (interação, seleção, resposta) adiciona uma informação a uma estrutura persistente do jogo (inventário, diário, caderno ou painel); a informação coletada se relaciona a ao menos um objetivo de aprendizagem do GDD ou documento equivalente; uma condição de missão ou desafio posterior à coleta verifica a posse, o valor ou o conteúdo da informação coletada
- Documentação: Verificar no GDD ou documento equivalente a mecânica de coleta e o uso das informações coletadas. Informação é um item, dado, texto, imagem ou medida relativo a ao menos um objetivo de aprendizagem listado nesse documento. Coletar é obter por ação do jogador de modo que o jogo guarde a informação; uso posterior é uma missão ou desafio posterior à coleta que só pode ser resolvido ou avançado com a posse, o valor ou o conteúdo da informação. Indicadores: o GDD descreve o que o jogador coleta, como o jogo o guarda e a qual objetivo de aprendizagem a informação se relaciona; o GDD descreve a missão ou desafio posterior que exige a posse, o valor ou o conteúdo da informação coletada
- Vídeo: O vídeo só confirma a evidência de código ou documentação: a ausência de coleta ou de uso no vídeo não prova que o jogo não os tem. Registrar os momentos de coleta e os momentos em que a informação coletada é exigida. Informação é um item, dado, texto, imagem ou medida relativo a ao menos um objetivo de aprendizagem do GDD ou documento equivalente. Coletar é obter por ação do jogador de modo que o jogo guarde a informação; uso posterior é uma missão ou desafio posterior à coleta que só pode ser resolvido ou avançado com a posse, o valor ou o conteúdo da informação. Indicadores: ao menos um momento em que o jogador obtém por ação própria uma informação e ela passa a constar em inventário, diário, caderno ou painel; ao menos um momento posterior em que uma missão ou desafio exige a posse, o valor ou o conteúdo da informação coletada para ser resolvido ou avançado

**Escala.**
- Atendido: O jogador coleta ao menos uma informação, nos termos do enunciado, e ao menos uma informação coletada é usada depois em missão ou desafio
- Parcial: O jogador coleta ao menos uma informação, nos termos do enunciado, mas nenhuma informação coletada é usada depois em missão ou desafio
- Não atendido: O jogador não coleta nenhuma informação, nos termos do enunciado: nada é obtido por ação própria e guardado pelo jogo, ou o que é guardado não se relaciona a objetivo de aprendizagem

**Depende de.** —

### D12 — O jogo deve fornecer mecanismos para o jogador construir coisas

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D12.1 — Nível AAA

**Enunciado.** O jogador combina dois ou mais elementos por ação própria e obtém um artefato novo que persiste no jogo; elemento é uma peça, item, bloco, valor ou outro objeto disponível ao jogador; artefato novo é um objeto, estrutura ou configuração inexistente no estado do jogo antes da combinação e identificável como unidade; persiste quando permanece disponível ao jogador depois de concluída a ação de combinar e só deixa de existir se o jogador o remover ou o consumir em uso posterior

**Justificativa do nível.** essencialidade baixa, viabilidade media. Construir é uma forma de atividade sobre objetos e instrumentos, e em Vigotski o sujeito externaliza o que compreende ao produzir algo com eles. A essencialidade é baixa porque a atividade do jogador pode se dar por outras vias, como resolver problemas (D01), explorar o cenário (D05) ou coletar informações (D11). Implementar combinação e persistência de objetos criados pelo jogador exige regras e estado adicionais; viabilidade média.

**Evidência.**
- Código: Localizar a lógica de combinação, criação ou montagem de objetos e verificar se o resultado é registrado no estado do jogo. Elemento é uma peça, item, bloco, valor ou outro objeto disponível ao jogador; artefato novo é um objeto, estrutura ou configuração inexistente no estado do jogo antes da combinação e identificável como unidade; persiste quando permanece disponível depois da ação de combinar e só deixa de existir se o jogador o remover ou o consumir em uso posterior. Indicadores: uma ação do jogador combina dois ou mais elementos e instancia um objeto, estrutura ou configuração identificável como unidade que não existia antes; o artefato criado é adicionado ao estado do jogo (cenário, inventário ou lista) e não é destruído ao fim da ação de combinar; o artefato só é removido por ação do jogador ou consumido em uso posterior
- Documentação: Verificar no GDD ou documento equivalente a mecânica de construção. Elemento é uma peça, item, bloco, valor ou outro objeto disponível ao jogador; artefato novo é um objeto, estrutura ou configuração inexistente no estado do jogo antes da combinação e identificável como unidade; persiste quando permanece disponível depois da ação de combinar e só deixa de existir se o jogador o remover ou o consumir em uso posterior. Indicadores: o GDD descreve quais elementos o jogador combina e qual artefato resulta da combinação; o GDD descreve onde o artefato permanece disponível depois de criado e em que condições deixa de existir
- Vídeo: O vídeo só confirma a evidência de código ou documentação: a ausência de construção no vídeo não prova que o jogo não a oferece. Registrar o momento em que o jogador combina elementos e verificar, em momentos posteriores da gravação, se o artefato resultante continua disponível. Elemento, artefato novo e persistência têm o sentido do enunciado. Indicadores: ao menos um momento em que o jogador combina dois ou mais elementos e um objeto, estrutura ou configuração novo, identificável como unidade, passa a existir; em momento posterior da gravação, o artefato continua disponível ao jogador (no cenário, inventário ou lista)

**Escala.**
- Atendido: O jogador combina dois ou mais elementos por ação própria e obtém um artefato novo, nos termos do enunciado, que persiste no jogo
- Parcial: O jogador combina dois ou mais elementos por ação própria, mas o resultado não permanece disponível depois da ação de combinar (por exemplo, a combinação é apenas avaliada como correta ou incorreta e descartada)
- Não atendido: O jogador não combina elementos para obter resultado novo; as ações disponíveis só manipulam elementos já existentes no jogo

**Depende de.** —

### D13 — O jogo permite o desenvolvimento de tarefas e missões em grupo

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D13.1 — Nível AAA

**Enunciado.** Existe ao menos uma missão ou tarefa que só se conclui quando cada um de dois ou mais jogadores diferentes realiza ao menos uma ação prevista para ela; jogador é uma pessoa que joga, e personagem não jogável não conta; missão ou tarefa é uma unidade do jogo com objetivo e condição de conclusão próprios

**Justificativa do nível.** essencialidade media, viabilidade baixa. Em Vigotski, a interação social é a origem das funções psicológicas superiores, e uma missão que só se conclui com a ação de mais de um jogador cria a situação em que a ZDP entre pares pode se formar. A essencialidade é média porque a interação também ocorre por comunicação entre jogadores (D06, D07) e fora do jogo. Exige multijogador, estado compartilhado entre jogadores e uma condição de conclusão que dependa de mais de uma pessoa, além de grupos reunidos no mesmo momento; viabilidade baixa.

**Evidência.**
- Código: Localizar a condição de conclusão das missões e tarefas e verificar se ela lê ações ou contribuições de mais de um identificador de jogador. Jogador é uma pessoa que joga, e personagem não jogável não conta; missão ou tarefa é uma unidade do jogo com objetivo e condição de conclusão próprios; a missão exige mais de um jogador quando a conclusão só é registrada depois da ação prevista de cada um de ao menos dois jogadores diferentes. Indicadores: existe missão ou tarefa cuja condição de conclusão verifica ações de dois ou mais identificadores de jogador diferentes; se a missão aceita dois ou mais jogadores mas a condição de conclusão verifica a ação de apenas um deles, anotar (indica o estado parcial); a conclusão não é registrada se a ação prevista de algum desses jogadores não ocorreu; existe sessão ou sala que aceita dois ou mais jogadores na mesma missão ou tarefa
- Documentação: Verificar no GDD ou documento equivalente as missões e tarefas em grupo. Jogador é uma pessoa que joga, e personagem não jogável não conta; missão ou tarefa é uma unidade do jogo com objetivo e condição de conclusão próprios; a missão exige mais de um jogador quando a conclusão só é registrada depois da ação prevista de cada um de ao menos dois jogadores diferentes. Indicadores: o GDD descreve missão ou tarefa com ações previstas para dois ou mais jogadores; o GDD descreve que a missão ou tarefa só se conclui depois da ação prevista de cada um desses jogadores; se o GDD descreve missão realizada em conjunto cuja conclusão depende da ação de apenas um dos jogadores, anotar (indica o estado parcial)
- Vídeo: O vídeo só confirma a evidência de código ou documentação: ele não mostra que a conclusão exige mais de um jogador. Registrar sessão com dois ou mais jogadores na mesma missão ou tarefa, as ações de cada um e o momento da conclusão. Jogador é uma pessoa que joga, e personagem não jogável não conta; a missão exige mais de um jogador quando a conclusão só é registrada depois da ação prevista de cada um de ao menos dois jogadores diferentes. Indicadores: dois ou mais jogadores atuam na mesma missão ou tarefa na mesma sessão; a conclusão da missão ou tarefa é registrada depois da ação de cada um desses jogadores; se a conclusão é registrada com a ação de apenas um dos jogadores presentes, anotar (indica o estado parcial)

**Escala.**
- Atendido: Existe ao menos uma missão ou tarefa que só se conclui depois da ação prevista de cada um de dois ou mais jogadores diferentes
- Parcial: Existe missão ou tarefa que dois ou mais jogadores realizam juntos, mas o jogo registra a conclusão com a ação de apenas um deles
- Não atendido: Todas as missões e tarefas são realizadas por um único jogador

**Depende de.** (D06.1 ou D07.1)

### D14 — O jogador deve conseguir inserir comentários no jogo que ficarão disponíveis para outros jogadores

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D14.1 — Nível AA

**Enunciado.** O jogador escreve um comentário associado a um local ou objeto do jogo e o jogo o exibe a outro jogador, em sessão posterior, quando este alcança esse local ou objeto; comentário é um texto digitado pelo jogador; outro jogador é um jogador com perfil ou conta diferente do autor; sessão posterior é uma sessão iniciada depois do término da sessão em que o comentário foi escrito

**Justificativa do nível.** essencialidade media, viabilidade media. Em Vigotski, os signos produzidos por uma pessoa mediam a atividade de outras, e um comentário deixado num local do jogo funciona como mediação entre jogadores que nem precisam estar presentes juntos. A essencialidade é média porque a interação entre jogadores também ocorre em tempo real (D06) e por trocas assíncronas sem local associado (D07). Exige persistência de dados fora da sessão, associação ao local ou objeto e distinção entre perfis; viabilidade média.

**Evidência.**
- Código: Localizar a escrita e a leitura de comentários e verificar onde são guardados e como são exibidos. Comentário é um texto digitado pelo jogador; outro jogador é um jogador com perfil ou conta diferente do autor; sessão posterior é uma sessão iniciada depois do término da sessão em que o comentário foi escrito. Indicadores: existe campo de entrada que grava o texto digitado junto com um identificador de local ou objeto e o identificador do autor; o comentário é guardado fora do estado da sessão (arquivo, banco de dados ou servidor) e sobrevive ao fim dela; ao jogador alcançar o local ou objeto, o jogo lê e exibe comentários de autores com perfil diferente do jogador atual; se a leitura não filtra por local ou objeto e exibe os comentários numa lista geral, anotar (indica o estado parcial)
- Documentação: não se aplica
- Vídeo: O vídeo só confirma a evidência de código: a ausência do comentário no vídeo não prova que o jogo não o persiste. Exigir duas gravações: uma em que um jogador escreve o comentário em um local ou objeto e outra, de sessão posterior e com perfil diferente, em que o outro jogador alcança o mesmo local ou objeto. Comentário, outro jogador e sessão posterior têm o sentido do enunciado. Indicadores: na primeira gravação, o jogador digita um comentário e o associa a um local ou objeto; na segunda gravação, de sessão posterior e com perfil diferente, o jogador alcança o mesmo local ou objeto e o comentário é exibido; se, na segunda gravação, o comentário de outro jogador aparece numa lista geral, sem o jogador ter alcançado local ou objeto associado, anotar (indica o estado parcial)

**Escala.**
- Atendido: Comentário escrito por um jogador, associado a um local ou objeto, é exibido a outro jogador em sessão posterior, quando este alcança esse local ou objeto
- Parcial: Comentário escrito por um jogador é exibido a outros jogadores em sessão posterior, mas não está associado a local ou objeto do jogo (por exemplo, aparece numa lista geral)
- Não atendido: Nenhum comentário escrito por um jogador é exibido a outros jogadores em sessão posterior

**Depende de.** —

### D15 — O jogo deve estimular a interação entre jogadores por diversas ferramentas de comunicação

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D15.1 — Nível AAA

**Enunciado.** O jogo oferece ao menos duas ferramentas distintas de comunicação entre jogadores; ferramenta de comunicação é um recurso do jogo pelo qual um jogador envia conteúdo a outro jogador; duas ferramentas são distintas quando diferem no meio (texto, voz ou sinais predefinidos, como emotes e marcadores) ou na temporalidade (entrega em tempo real ou registro lido em sessão posterior); dois canais de mesmo meio e mesma temporalidade, como um chat geral e um chat privado, contam como uma única ferramenta

**Justificativa do nível.** essencialidade media, viabilidade baixa. Em Vigotski, a linguagem é instrumento de mediação, e diferentes instrumentos semióticos (fala, escrita, sinais) dão ao jogador mais de um meio de se fazer entender e de entender o outro. A essencialidade é média porque um único canal já sustenta a interação social (D06, D07). Manter dois ou mais canais, com infraestrutura de rede e de persistência para cada um, é custo elevado para jogos educacionais; viabilidade baixa.

**Evidência.**
- Código: Localizar os módulos de comunicação entre jogadores (chat de texto, voz, mensagens persistidas, sinais predefinidos) e classificar cada um por meio e temporalidade. Duas ferramentas são distintas quando diferem no meio (texto, voz ou sinais predefinidos) ou na temporalidade (tempo real ou registro lido em sessão posterior); canais de mesmo meio e mesma temporalidade contam como uma única ferramenta. Contar as ferramentas distintas. Indicadores: existe módulo que envia conteúdo de um jogador a outro jogador; cada módulo foi classificado por meio (texto, voz ou sinais predefinidos) e por temporalidade (tempo real ou sessão posterior); há ao menos dois módulos que diferem no meio ou na temporalidade
- Documentação: Verificar no GDD ou documento equivalente a lista de ferramentas de comunicação entre jogadores e classificar cada uma por meio e temporalidade. Duas ferramentas são distintas quando diferem no meio (texto, voz ou sinais predefinidos) ou na temporalidade (tempo real ou registro lido em sessão posterior); canais de mesmo meio e mesma temporalidade contam como uma única ferramenta. Indicadores: o GDD descreve cada ferramenta de comunicação, seu meio e sua temporalidade; o GDD descreve ao menos duas ferramentas que diferem no meio ou na temporalidade
- Vídeo: não se aplica

**Escala.**
- Atendido: O jogo oferece duas ou mais ferramentas de comunicação entre jogadores distintas, nos termos do enunciado
- Parcial: O jogo oferece uma única ferramenta de comunicação entre jogadores, nos termos do enunciado
- Não atendido: O jogo não oferece ferramenta de comunicação entre jogadores

**Depende de.** (D06.1 ou D07.1)

### D16 — O jogo deve fornecer meios do jogador solicitar ajuda de outros jogadores

- Categoria: Mediação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D16.1 — Nível AA

**Enunciado.** Existe uma ação explícita de pedir ajuda que encaminha a solicitação do jogador a outro jogador

**Justificativa do nível.** essencialidade media, viabilidade media. Mediação por pares é a forma mais direta da zona de desenvolvimento proximal entre jogadores, mas a mediação também é oferecida pelo próprio jogo (D17 a D21). Exige um canal entre jogadores (D06 ou D07) e uma ação dedicada; viabilidade média.

**Evidência.**
- Código: Localizar ação, botão ou comando de pedir ajuda e verificar para onde a solicitação é enviada. Indicadores: ação de ajuda distinta do chat geral; solicitação chega a outro jogador, não só ao sistema
- Documentação: Verificar no GDD a mecânica de pedido de ajuda. Indicadores: fluxo descrito: quem pede, quem recebe, o que acontece
- Vídeo: Observar o jogador acionar o pedido de ajuda e o que ocorre em seguida. Indicadores: pedido de ajuda enviado a outro jogador

**Escala.**
- Atendido: Ação de pedir ajuda existe e chega a outro jogador
- Parcial: Ação existe, mas a resposta vem só do sistema ou de personagem não jogável
- Não atendido: Não há meio de pedir ajuda a outros jogadores

**Depende de.** (D06.1 ou D07.1)

### D17 — O jogo deve exibir feedback construtivo para as ações do jogador

- Categoria: Mediação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D17.1 — Nível A

**Enunciado.** Toda ação incorreta do jogador recebe mensagem que indica o que fazer em seguida, e não apenas que errou

**Justificativa do nível.** essencialidade alta, viabilidade alta. Mediação é o núcleo da zona de desenvolvimento proximal: o jogo faz o papel do outro mais experiente. Feedback que só sinaliza acerto ou erro é reforço behaviorista, exatamente o que as diretrizes querem afastar. Implementação de baixo custo em qualquer motor de jogo.

**Evidência.**
- Código: Localizar os tratadores de erro ou falha de missão e minijogo e listar o texto exibido em cada um. Indicadores: mensagem contém orientação de próxima ação; mensagem referencia o conteúdo ou objeto envolvido no erro
- Documentação: Verificar no documento de design (GDD) a especificação de feedback por tipo de erro. Indicadores: tabela ou lista de erros com a mensagem orientadora correspondente
- Vídeo: Registrar o timestamp de cada erro cometido pelo jogador e classificar o feedback exibido. Indicadores: ao menos 3 ocorrências de erro observadas; cada ocorrência mostra orientação, não só sinal de erro

**Escala.**
- Atendido: Todas as ocorrências de erro observadas recebem feedback que orienta a próxima ação
- Parcial: Algumas ocorrências orientam; outras só sinalizam erro ou não recebem feedback
- Não atendido: O feedback só sinaliza acerto ou erro, ou não existe

**Depende de.** —
