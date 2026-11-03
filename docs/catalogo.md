<!-- ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão. -->
# Catálogo vygolint — diretrizes e critérios de conformidade

Fonte das diretrizes: CARVALHO, Diego Marques. *Diretrizes para o desenvolvimento de jogos educacionais digitais embasados na teoria sociointeracionista de Lev Semionovich Vigotski*. Dissertação (Mestrado), UFABC, 2020. Quadro 3.

> Carvalho (2020, seção 4.4) suprimiu as categorias na apresentação final das diretrizes por considerar que rotular, classificar e ordenar requisitos pode gerar a falsa impressão de que a teoria de Vigotski também pode ser classificada assim. O vygolint usa as categorias apenas como instrumento de organização e de relatório, não como taxonomia da teoria.

## Resumo

| ID | Categoria | Diretriz | Critérios |
|---|---|---|---|
| D06 | Interação | O jogador deve trocar informações com outros jogadores por comunicação síncrona | D06.1 (AAA) |
| D07 | Interação | O jogador deve trocar informações com outros jogadores por meio de comunicação assíncrona | D07.1 (AA) |
| D16 | Mediação | O jogo deve fornecer meios do jogador solicitar ajuda de outros jogadores | D16.1 (AA) |
| D17 | Mediação | O jogo deve exibir feedback construtivo para as ações do jogador | D17.1 (A) |

## Diretrizes

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
