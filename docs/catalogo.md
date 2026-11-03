<!-- ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão. -->
# Catálogo vygolint — diretrizes e critérios de conformidade

Fonte das diretrizes: CARVALHO, Diego Marques. *Diretrizes para o desenvolvimento de jogos educacionais digitais embasados na teoria sociointeracionista de Lev Semionovich Vigotski*. Dissertação (Mestrado), UFABC, 2020. Quadro 3.

> Carvalho (2020, seção 4.4) suprimiu as categorias na apresentação final das diretrizes por considerar que rotular, classificar e ordenar requisitos pode gerar a falsa impressão de que a teoria de Vigotski também pode ser classificada assim. O vygolint usa as categorias apenas como instrumento de organização e de relatório, não como taxonomia da teoria.

## Resumo

| ID | Categoria | Diretriz | Critérios |
|---|---|---|---|
| D01 | Interação | Os desafios do jogo devem ser direcionados a resolução de problemas | D01.1 (A) |
| D02 | Interação | Avaliar os conteúdos ensinados no jogo de forma a transcender o contexto que eles foram abordados, possibilitando a transposição dos conceitos para resolução de outras situações-problema | D02.1 (A) |
| D03 | Interação | O desenvolvimento das atividades/missões/minijogos deve ser autorregulado pelo jogador | D03.1 (A), D03.2 (A) |
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

**Justificativa do nível.** essencialidade alta, viabilidade alta. Para Vigotski a aprendizagem nasce da atividade do sujeito sobre um problema, e o conhecimento é construído quando o jogador precisa operar com os conceitos, não quando os reproduz. Desafios de repetição mecânica reduzem o jogo a treino de estímulo e resposta, o que Carvalho (2020) busca afastar. Estruturar desafios como situações-problema é uma decisão de projeto, sem custo técnico adicional.

**Evidência.**
- Código: não se aplica
- Documentação: Listar no documento de design (GDD) cada missão e minijogo e identificar a situação-problema e as alternativas de decisão previstas. Indicadores: cada missão ou minijogo descreve uma situação-problema; há ao menos duas alternativas de resolução ou uma decisão a ser tomada pelo jogador
- Vídeo: Registrar o início e o fim de cada missão ou minijogo observado e anotar qual decisão o jogador tomou para concluí-lo. Indicadores: ao menos 3 missões ou minijogos observados; em cada um, o jogador escolhe ou combina elementos para resolver a situação; concluir o desafio não depende de repetir a mesma ação até o fim

**Escala.**
- Atendido: Todas as missões e minijogos observados ou documentados exigem uma decisão do jogador para serem resolvidos
- Parcial: Parte das missões e minijogos exige decisão; os demais se resolvem repetindo uma ação
- Não atendido: Nenhuma missão ou minijogo exige decisão do jogador além de repetir uma ação

**Depende de.** —

### D02 — Avaliar os conteúdos ensinados no jogo de forma a transcender o contexto que eles foram abordados, possibilitando a transposição dos conceitos para resolução de outras situações-problema

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D02.1 — Nível A

**Enunciado.** Existe ao menos um desafio que exige aplicar um conceito já apresentado em um cenário ou situação diferente daquele em que o conceito foi introduzido

**Justificativa do nível.** essencialidade alta, viabilidade media. Em Vigotski, conceitos científicos se consolidam quando o sujeito os generaliza e os usa de modo consciente em situações novas, e não quando os repete no contexto de origem. Avaliar apenas no cenário de introdução mede memorização do contexto, não domínio do conceito. Exige planejar variações de cenário para o mesmo conteúdo, o que aumenta o esforço de conteúdo e de design; viabilidade média.

**Evidência.**
- Código: não se aplica
- Documentação: Mapear no GDD, para cada conceito, o cenário de introdução e os cenários em que ele é cobrado em desafios. Indicadores: tabela ou lista associando conceito, cenário de introdução e cenário de avaliação; ao menos um conceito é cobrado em cenário distinto do de introdução
- Vídeo: Registrar o cenário e o momento em que cada conceito é introduzido e o cenário em que o mesmo conceito é cobrado depois. Indicadores: ao menos um conceito aparece em dois cenários ou missões diferentes; o desafio do segundo cenário só se resolve aplicando o conceito apresentado no primeiro

**Escala.**
- Atendido: Todos os conceitos centrais do jogo são cobrados ao menos uma vez em cenário diferente do de introdução
- Parcial: Ao menos um conceito é cobrado em cenário diferente do de introdução, mas outros conceitos centrais são cobrados só no cenário em que foram apresentados
- Não atendido: Todos os conceitos são cobrados apenas no cenário em que foram introduzidos

**Depende de.** —

### D03 — O desenvolvimento das atividades/missões/minijogos deve ser autorregulado pelo jogador

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D03.1 — Nível A

**Enunciado.** O jogador inicia cada atividade, missão ou minijogo por uma ação própria e o jogo não avança de uma para a próxima sem essa ação

**Justificativa do nível.** essencialidade alta, viabilidade alta. Atividade, em Vigotski, é conduzida pelo sujeito; a autorregulação é o movimento em que o controle da própria ação passa do outro para o aprendiz. Se o jogo conduz o jogador de uma etapa à seguinte, o controle permanece no sistema. Basta condicionar a transição a uma ação do jogador, o que não exige recurso técnico especial.

**Evidência.**
- Código: Localizar as transições entre missões e minijogos e verificar o que as dispara. Indicadores: a transição é disparada por entrada do jogador (botão, escolha, interação); não há transição disparada apenas por temporizador ou por término automático da etapa anterior
- Documentação: não se aplica
- Vídeo: Registrar cada transição entre atividades e anotar se houve ação do jogador antes da mudança. Indicadores: ao menos 3 transições observadas; cada transição é precedida por ação do jogador

**Escala.**
- Atendido: Todas as transições observadas ou identificadas no código dependem de ação do jogador
- Parcial: Parte das transições depende de ação do jogador; outras ocorrem automaticamente
- Não atendido: As atividades se sucedem automaticamente, sem ação do jogador

**Depende de.** —

#### D03.2 — Nível A

**Enunciado.** O jogador conclui cada atividade em seu próprio ritmo: nenhuma atividade tem limite de tempo obrigatório para ser concluída, ou o limite pode ser desativado ou ampliado pelo jogador

**Justificativa do nível.** essencialidade alta, viabilidade alta. Regular a própria atividade inclui decidir quando agir e quanto tempo dedicar a uma tarefa; cronômetro imposto desloca essa decisão para o sistema e pressiona o jogador a responder antes de elaborar. A zona de desenvolvimento proximal difere entre jogadores, então o ritmo também difere. Remover ou tornar opcional o limite de tempo é de baixo custo.

**Evidência.**
- Código: Procurar temporizadores associados a missões e minijogos e verificar o que ocorre quando o tempo se esgota e se há opção de desativá-los. Indicadores: existência de temporizador com consequência de falha ao esgotar; existência de configuração que desativa ou amplia o temporizador
- Documentação: Verificar no GDD as regras de tempo de cada atividade. Indicadores: indicação de quais atividades têm limite de tempo; indicação de opção do jogador para alterar o limite
- Vídeo: Observar cada atividade registrando se há contador de tempo visível e se o jogador pode permanecer nela sem limite. Indicadores: ao menos 3 atividades observadas; o jogador permanece na atividade sem ser interrompido por esgotamento de tempo

**Escala.**
- Atendido: Nenhuma atividade tem limite de tempo obrigatório, ou o jogador pode desativar ou ampliar o limite
- Parcial: Parte das atividades tem limite de tempo obrigatório; as demais não têm
- Não atendido: Todas as atividades têm limite de tempo obrigatório que o jogador não pode alterar

**Depende de.** —

### D04 — O jogador deve interagir com os objetos dos cenários

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D04.1 — Nível A

**Enunciado.** Ao menos um objeto de cada cenário responde à interação do jogador com mudança de estado ou com informação relacionada ao conteúdo do jogo

**Justificativa do nível.** essencialidade alta, viabilidade alta. Para Vigotski o conhecimento é construído na atividade sobre objetos e instrumentos, e interagir com o ambiente é a forma pela qual o jogador exerce essa atividade. Um cenário apenas contemplativo reduz o jogador a espectador. Programar resposta a clique, toque ou colisão é recurso básico de qualquer motor de jogo.

**Evidência.**
- Código: Listar os objetos de cada cenário que têm tratador de interação (clique, toque, colisão, uso de item) e o efeito de cada tratador. Indicadores: cada cenário tem ao menos um objeto com tratador de interação; o efeito do tratador é mudança de estado do objeto ou exibição de informação ligada ao conteúdo
- Documentação: não se aplica
- Vídeo: Percorrer cada cenário observado registrando os objetos com os quais o jogador interage e a resposta obtida. Indicadores: ao menos um objeto interagido por cenário; o objeto muda de estado ou exibe informação ligada ao conteúdo

**Escala.**
- Atendido: Todos os cenários têm ao menos um objeto que responde à interação com mudança de estado ou informação ligada ao conteúdo
- Parcial: Alguns cenários têm objeto interativo; outros não têm, ou o objeto responde sem relação com o conteúdo
- Não atendido: Nenhum objeto dos cenários responde à interação do jogador

**Depende de.** —

### D05 — O jogador deve explorar livremente o cenário

- Categoria: Interação
- Modalidade: deve
- Aplicabilidade: —
- Fonte: Carvalho (2020), Quadro 3

#### D05.1 — Nível A

**Enunciado.** Em ao menos um cenário, o jogador alcança áreas ou objetos que não pertencem ao caminho da missão em curso, sem que o jogo o impeça ou o conduza de volta ao objetivo

**Justificativa do nível.** essencialidade alta, viabilidade media. A exploração é a atividade do jogador sobre o ambiente: é por ela que ele formula hipóteses e descobre relações, em vez de receber um percurso pronto. Um cenário reduzido ao caminho da missão converte a exploração em seguimento de instruções. Construir áreas além do caminho principal acrescenta trabalho de arte e de nível; viabilidade média.

**Evidência.**
- Código: não se aplica
- Documentação: Verificar no GDD ou nos mapas de nível as áreas de cada cenário e se existem regiões fora do caminho da missão. Indicadores: mapa ou descrição que indica áreas fora do caminho da missão; ausência de regra que bloqueie o acesso a essas áreas durante a missão
- Vídeo: Observar o jogador deixando o caminho da missão e registrar o que o jogo faz em seguida. Indicadores: o jogador visita ao menos uma área fora do caminho da missão; o jogo não interrompe, bloqueia nem reposiciona o jogador por causa disso

**Escala.**
- Atendido: Todos os cenários jogáveis têm áreas fora do caminho da missão acessíveis sem bloqueio
- Parcial: Ao menos um cenário tem áreas acessíveis fora do caminho da missão; os demais restringem o jogador ao caminho
- Não atendido: Nenhum cenário permite alcançar áreas fora do caminho da missão em curso

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

**Justificativa do nível.** essencialidade alta, viabilidade alta. Em Vigotski, a interação com o meio é mediada por signos e instrumentos, e uma troca de mão dupla com o jogo faz do sistema um interlocutor, e não um painel de exibição. Se o jogo só emite informação, o jogador permanece receptor. Diálogos com escolhas e entrega de itens são mecânicas comuns e de baixo custo.

**Evidência.**
- Código: Localizar diálogos, quadros de pergunta e mecanismos de entrega ou recebimento de itens e verificar se a resposta do jogador é registrada e muda o estado ou o conteúdo seguinte. Indicadores: o mecanismo emite informação ao jogador; a entrada do jogador (escolha, resposta, item) é lida pelo mecanismo; a entrada do jogador altera a próxima saída do mecanismo ou o estado do jogo
- Documentação: não se aplica
- Vídeo: Registrar cada troca entre o jogador e personagem ou mecanismo, anotando a informação recebida, a entrada do jogador e o que o jogo exibe depois. Indicadores: ao menos uma troca completa observada (informação recebida, entrada do jogador, resposta do jogo); o que o jogo exibe depois difere conforme a entrada do jogador

**Escala.**
- Atendido: O jogo apresenta trocas de dois sentidos com mecanismos, e a entrada do jogador altera a resposta do jogo, em mais de uma situação
- Parcial: Há uma única situação de troca de dois sentidos, ou as trocas existem mas a entrada do jogador não altera a resposta do jogo
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
