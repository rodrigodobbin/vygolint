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
| D16 | Mediação | O jogo deve fornecer meios do jogador solicitar ajuda de outros jogadores | D16.1 (AA) |
| D17 | Mediação | O jogo deve exibir feedback construtivo para as ações do jogador | D17.1 (A) |

## Diretrizes

### D01 — Os desafios do jogo devem ser direcionados a resolução de problemas

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D01.1 — Nível A

**Enunciado.** Cada missão ou minijogo apresenta uma situação-problema cuja resolução exige uma decisão do jogador, e não apenas a repetição de uma mesma ação

**Justificativa do nível.** essencialidade alta, viabilidade alta. Para Vigotski a aprendizagem nasce da atividade do sujeito sobre um problema, e o conhecimento é construído quando o jogador precisa operar com os conceitos, não quando os reproduz. Em um desafio de repetição mecânica o jogador executa a mesma ação sem escolher entre alternativas, de modo que a atividade não exige operar com o conteúdo. Estruturar desafios como situações-problema é uma decisão de projeto, sem custo técnico adicional.

**Evidência.**
- Código: não se aplica
- Documentação: Listar no documento de design (GDD) cada missão e minijogo e identificar a situação-problema e as alternativas de decisão previstas. Indicadores: cada missão ou minijogo descreve uma situação-problema, isto é, uma situação com estado inicial, objetivo e mais de uma ação possível; uma pergunta com alternativas de resposta, sem estado inicial a ser transformado pelas ações do jogador, não conta como situação-problema
- Vídeo: Registrar o início e o fim de cada missão ou minijogo observado e anotar qual decisão o jogador tomou para concluí-lo. Indicadores: todas as missões e minijogos presentes no vídeo foram registrados (mínimo 1); em cada um, o jogador escolhe ou combina elementos para resolver a situação; concluir o desafio não depende de repetir a mesma ação até o fim

**Escala.**
- Atendido: Todas as missões e minijogos observados ou documentados exigem uma decisão do jogador para serem resolvidos
- Parcial: Ao menos uma missão ou minijogo exige decisão do jogador, e ao menos outra se resolve repetindo uma ação
- Não atendido: Nenhuma missão ou minijogo exige decisão do jogador além de repetir uma ação

**Depende de.** —

### D02 — Avaliar os conteúdos ensinados no jogo de forma a transcender o contexto que eles foram abordados, possibilitando a transposição dos conceitos para resolução de outras situações-problema

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D02.1 — Nível A

**Enunciado.** Cada conceito listado como objetivo de aprendizagem no GDD (ou documento equivalente) é cobrado ao menos uma vez em uma missão ou cenário com estrutura de problema diferente daquela em que foi introduzido

**Justificativa do nível.** essencialidade alta, viabilidade media. Em Vigotski, conceitos científicos se consolidam quando o sujeito os generaliza e os usa de modo consciente em situações novas, e não quando os repete no contexto de origem. Avaliar apenas na situação de introdução mede memorização do contexto, não domínio do conceito. Exige planejar variações de situação para cada conteúdo, o que aumenta o esforço de conteúdo e de design; viabilidade média.

**Evidência.**
- Código: não se aplica
- Documentação: Extrair do GDD (ou documento equivalente) a lista de objetivos de aprendizagem e mapear, para cada conceito, a missão ou cenário de introdução e as missões ou cenários em que ele é cobrado. Se o documento não lista objetivos de aprendizagem, registrar a ausência e classificar o critério como nao_atendido. Considerar estrutura de problema diferente quando mudam o objetivo da missão ou o conjunto de objetos ou dados que o jogador manipula; mudar apenas o mapa ou a aparência do cenário não conta. Indicadores: tabela ou lista associando cada conceito do GDD, a missão ou cenário de introdução e a missão ou cenário de avaliação; para cada conceito, a missão de avaliação tem objetivo ou conjunto de objetos ou dados manipulados diferente do da missão de introdução
- Vídeo: Para cada conceito listado no GDD, registrar a missão e o momento em que ele é introduzido e a missão em que o mesmo conceito é cobrado depois, comparando o objetivo e os objetos manipulados nas duas. Indicadores: o conceito aparece em duas missões ou cenários diferentes; o desafio da segunda missão só se resolve aplicando o conceito apresentado na primeira e tem objetivo ou objetos manipulados diferentes

**Escala.**
- Atendido: Todos os conceitos listados como objetivo de aprendizagem são cobrados ao menos uma vez em missão ou cenário com estrutura de problema diferente da de introdução
- Parcial: Ao menos um conceito listado é cobrado em missão ou cenário com estrutura de problema diferente da de introdução, e ao menos outro conceito listado é cobrado só na situação em que foi apresentado
- Não atendido: Nenhum conceito listado é cobrado fora da situação em que foi introduzido, ou o GDD não lista objetivos de aprendizagem

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
- Código: Localizar a lógica de desbloqueio de missões e minijogos e verificar se há algum estado do jogo em que duas ou mais atividades estão desbloqueadas ao mesmo tempo e selecionáveis. Indicadores: existe estado do jogo em que duas ou mais atividades estão desbloqueadas simultaneamente; a atividade iniciada é determinada por entrada do jogador (menu, mapa, interação), não por ordem fixa no código
- Documentação: não se aplica
- Vídeo: Registrar os pontos em que o jogo oferece atividades e anotar quantas estão disponíveis e qual o jogador inicia. Indicadores: ao menos um ponto em que duas ou mais atividades aparecem disponíveis ao mesmo tempo (menu, mapa ou cenário); o jogador inicia uma delas e a outra permanece disponível ou é iniciada depois

**Escala.**
- Atendido: Em ao menos um ponto, o jogador escolhe entre duas ou mais atividades, missões ou minijogos disponíveis ao mesmo tempo
- Parcial: O jogador não escolhe entre atividades, missões ou minijogos, mas escolhe a ordem de elementos dentro de uma atividade (como objetos, perguntas ou etapas)
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
- Vídeo: Observar cada atividade registrando se há contador de tempo visível e se o jogador pode permanecer nela sem limite. Indicadores: todas as atividades presentes no vídeo foram observadas (mínimo 1); o jogador permanece na atividade sem ser interrompido por esgotamento de tempo

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
- Vídeo: Percorrer cada cenário observado registrando os objetos com os quais o jogador interage e a resposta obtida, e comparar a resposta com os objetivos de aprendizagem do GDD. Indicadores: ao menos um objeto interagido por cenário; o objeto muda de estado ou exibe informação que se relaciona a um objetivo de aprendizagem do GDD

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
- Código: não se aplica
- Documentação: Identificar no GDD ou nos mapas de nível, para cada cenário, os objetivos que compõem o caminho da missão e as áreas ou objetos que nenhum desses objetivos exige. Indicadores: o GDD ou mapa descreve áreas ou objetos acessíveis fora do caminho da missão, isto é, que nenhum objetivo da missão exige; o GDD descreve o deslocamento do jogador até essas áreas durante a missão
- Vídeo: Observar o jogador deixando o caminho da missão e registrar o que o jogo faz em seguida. Indicadores: o jogador visita ao menos uma área ou objeto fora do caminho da missão em cada cenário observado; o jogo não interrompe, bloqueia nem reposiciona o jogador por causa disso

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
