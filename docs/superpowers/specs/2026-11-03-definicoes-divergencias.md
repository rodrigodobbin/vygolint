# Definições compartilhadas — divergências encontradas e decisões pendentes

Data: 2026-11-03. Origem: migração do catálogo para `catalog/definicoes.yaml` (plano `docs/superpowers/plans/2026-11-03-definicoes-glossario.md`). Enquanto uma decisão está pendente, o catálogo usa a redação do arquivo âncora, indicada em cada item; a decisão 12 já foi aplicada (pode ser revertida). A lista legível por máquina está em `scripts/definicoes_aceitas.yaml`: cada entrada com `tipo: decisao` traz em `decisao` o número do item abaixo.

"Etapa 1" é o texto do catálogo em `main`, antes da migração. Cada decisão pode ser respondida com uma de três opções:

- **aceitar âncora**: o catálogo fica como está;
- **adotar variante**: volta o sentido da etapa 1 (o item diz como, quase sempre por um local no critério, sem mexer no glossário);
- **nova redação**: o usuário redige outro texto (o item traz uma sugestão quando há).

## 1. Decisões pendentes

| nº | termo | critérios | o que muda |
|---|---|---|---|
| 1 | `desafio` | D39.1 | a etapa interna de uma missão, sem regras próprias, deixa de contar como desafio |
| 2 | `missao` + `desafio` | D11.1 | «missão ou desafio» deixa de ser um termo só; fase, capítulo e nível passam a contar como missão, o jogo sem divisão conta como uma missão e o minijogo conta como desafio |
| 3 | `missao` («missão ou tarefa») | D13.1, D27.1 | «tarefa» fica sem definição; o jogo sem divisão em missões passa a contar como uma missão |
| 4 | `minijogo` | 24 critérios em 23 arquivos | a definição de D37 passa a valer onde a palavra era usada no sentido corrente: minijogo exige regras, objetivo e condição de conclusão próprios e conta à parte da missão em que está |
| 5 | `cenario_jogavel` | D04.1 | «cada cenário» passa a excluir hub e sandbox sem missão em curso |
| 6 | `situacao_problema` (indicador de vídeo) | D01.1 | o indicador ainda redefine o termo com «visível» e «disponível ao jogador» |
| 7 | `documentacao_equivalente` | 37 critérios | texto novo: o documento precisa descrever o conteúdo do jogo, e material de divulgação ou de loja deixa de contar |
| 8 | `objetivo_de_aprendizagem` | D22.1, D04.1, D11.1, D36.1 | de «o listado na documentação» (ou sem definição) para «conceito, fato ou procedimento listado» |
| 9 | `objetivo_de_aprendizagem` + local `conteúdo de aprendizagem` | D19.1, D23.1, D25.1 | o termo composto «conteúdo e objetivo de aprendizagem» é dividido; o objetivo fica restrito como no item 8 |
| 10 | `sessao_de_jogo` | D36.1 | texto novo: voltar ao menu inicial encerra a sessão, e carregar um estado salvo inicia outra |
| 11 | `persiste` (local) | D12.1 | das duas redações do mesmo critério, fica a do enunciado («ao jogador», «concluída») |
| 12 | «nos termos do enunciado» nas escalas | 30 arquivos | **aplicada**: o ponteiro passou a «nos termos do enunciado e das definições» em todo o catálogo |
| 13 | `documentacao_equivalente` × regra de D30 | D30.1 | sem GDD, as telas de abertura, créditos ou Sobre contam como documento equivalente só em D30; local novo explicita a exceção |
| 14 | `missao` acrescentada | 21 critérios | o jogo sem divisão em missões passa a contar como uma missão, e fase, capítulo ou nível com objetivo e conclusão próprios passam a contar como missão |

### Decisão 1 — `desafio`: incluir "etapa com condição de conclusão própria"?

- **Âncora aplicada:** D19 — «desafio é cada missão ou minijogo». Por cascata, D39.1 passa a listar `missao` e `minijogo`.
- **Variante da etapa 1:** D39.1 (enunciado, três procedimentos e três escalas) — «desafio é uma unidade do jogo com objetivo e condição de conclusão próprios (missão, minijogo ou etapa com condição de conclusão própria), e o jogo sem divisão em missões conta como uma única missão».
- **O que muda:** em D39 uma etapa dentro de uma missão, como um enigma dentro de uma fase, contava como desafio. Com a âncora, só a missão inteira ou o minijogo contam. Uma etapa que tenha regras, objetivo e condição de conclusão próprios continua contando, porque é minijogo (a definição de minijogo inclui «jogada dentro de uma missão»). A etapa sem regras próprias só conta através da missão. Isso muda o grau só quando a etapa é opcional: o detalhe é exigido pela etapa, mas a missão se conclui sem ela.
- **Critérios afetados:** D39.1. Lista de aceitas: `clausulas` D39.1 (`decisao: 1`).
- **Proposta:** aceitar âncora. Adotar variante seria acrescentar a D39.1 o local «desafio, neste critério, inclui também a etapa com condição de conclusão própria dentro de uma missão», sem mudar `desafio` no glossário, que D19, D33–D35 e D40 usam como unidade inteira.

### Decisão 2 — `missao` + `desafio` em D11: «missão ou desafio» como termo único

- **Âncora aplicada:** `missao` (D28) — «uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão»; `desafio` (D19) — «cada missão ou minijogo»; `minijogo` por cascata.
- **Variante da etapa 1:** D11.1 (enunciado e três procedimentos) — «missão ou desafio é uma unidade do jogo com objetivo e condição de conclusão próprios».
- **O que muda:** (i) fase, capítulo ou nível com objetivo e condição de conclusão próprios passam a contar explicitamente como missão; (ii) o minijogo passa a contar como desafio; (iii) o jogo sem divisão em missões conta como uma missão. Com (iii), num jogo de missão única o local `uso posterior` («uma missão ou desafio posterior ao momento da coleta que só pode ser resolvido ou avançado com…») fica ambíguo: a missão em que a informação foi coletada continua depois da coleta, e não há «missão posterior».
- **Critérios afetados:** D11.1. Lista de aceitas: `clausulas` D11.1 (`decisao: 2`).
- **Proposta:** aceitar âncora e, como nova redação do local `uso posterior`, «um trecho de missão ou desafio posterior ao momento da coleta que só pode ser resolvido ou avançado com a posse, o valor ou o conteúdo dessa informação», para cobrir o jogo de missão única. Adotar variante seria um local em D11.1 com o texto da etapa 1 no lugar de `missao` e `desafio`.

### Decisão 3 — `missao` em D13 e D27: «missão ou tarefa»

- **Âncora aplicada:** `missao` (D28), texto citado na decisão 2.
- **Variante da etapa 1:** D13.1 e D27.1 — «missão ou tarefa é uma unidade do jogo com objetivo e condição de conclusão próprios».
- **O que muda:** (i) «tarefa» continua no texto («existe ao menos uma missão ou tarefa…», «o objetivo de uma missão ou tarefa…»), mas sem definição, e é lida no sentido corrente; (ii) o jogo sem divisão em missões passa a contar como uma missão. Em D13.1, um jogo sem missões cuja conclusão exige a ação de dois jogadores passa a atender. Em D27.1, o mesmo para um jogo sem missões com objetivo comum e ações interdependentes.
- **Critérios afetados:** D13.1, D27.1. Lista de aceitas: `clausulas` D13.1 e D27.1 (`decisao: 3`).
- **Proposta:** aceitar âncora e, como nova redação, retirar «ou tarefa» do texto de D13 e D27 (enunciado, procedimentos, indicadores, escalas e locais). Um sinônimo `tarefa` no glossário colidiria com outros usos: em D30 «tarefa» é parte da premissa («papel do jogador, local, tarefa e problema a resolver») e em D28 é a tarefa que a missão propõe. Adotar variante seria um local `tarefa`: «o mesmo que missão» em D13.1 e D27.1.

### Decisão 4 — `minijogo`: a definição de D37 passa a valer em todo o catálogo

- **Âncora aplicada:** D37 — «uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela».
- **Variante da etapa 1:** nenhuma redação diferente; a palavra era usada sem definição em 15 arquivos (D01, D03, D17, D18, D19, D20, D21, D22, D24, D25, D33, D34, D35, D39, D40). Só D37 a definia.
- **O que muda:** (i) uma atividade sem regras, objetivo ou condição de conclusão próprios (uma tela de pergunta avulsa, uma animação interativa) deixa de ser minijogo; (ii) o minijogo jogado dentro de uma missão conta como unidade à parte, de modo que, nos critérios que avaliam «cada missão e minijogo» (D01, D03, D37, D39, D40 e outros), uma missão com um minijogo dentro são duas unidades; (iii) por cascata de `desafio` («cada missão ou minijogo»), o minijogo passa a contar como desafio também em D02, D04, D11, D23, D26 e D36, que não usavam a palavra.
- **Critérios afetados:** D01.1, D02.1, D03.1, D03.2, D03.3, D04.1, D11.1, D17.1, D18.1, D19.1, D20.1, D21.1, D22.1, D22.2, D23.1, D24.1, D25.1, D26.1, D33.1, D34.1, D35.1, D36.1, D39.1, D40.1. Lista de aceitas: as 24 entradas `adicoes` com `chave: minijogo` (`decisao: 4`).
- **Proposta:** aceitar âncora. Adotar variante seria tirar `minijogo` desses critérios e declará-lo em `termos_comuns` (sentido corrente), o que deixaria `desafio` remetendo a um termo sem definição.

### Decisão 5 — `cenario_jogavel` em D04: «cada cenário»

- **Âncora aplicada:** D29 — «cada espaço do jogo (mapa, sala ou fase) em que o jogador executa ações e em que há uma missão em curso; cenário em que nenhuma missão está em curso (hub, sandbox) não tem caminho obrigatório e não é cenário jogável». Por cascata entra `caminho_obrigatorio`.
- **Variante da etapa 1:** sem definição — «Ao menos um objeto de cada cenário responde à interação do jogador…», «cada cenário observado» (enunciado, procedimentos, indicadores e escalas de D04.1).
- **O que muda:** «cada cenário» passa a excluir hub e sandbox sem missão em curso. Um hub sem objeto interativo ligado a objetivo de aprendizagem deixa de reprovar o critério.
- **Critérios afetados:** D04.1. Lista de aceitas: `adicoes` D04.1 `cenario_jogavel` e `caminho_obrigatorio` (`decisao: 5`).
- **Proposta:** aceitar âncora (é a mesma unidade de D05 e D29). Adotar variante seria tirar as duas chaves de D04.1 e declarar `termos_comuns: {cenário: …}` com o sentido de qualquer espaço do jogo, hub incluído.

### Decisão 6 — `situacao_problema`: indicador de vídeo de D01

- **Âncora aplicada:** D01 (o glossário é o texto do enunciado da etapa 1) — «uma situação com estado inicial, objetivo e mais de uma ação possível, cuja resolução exige uma decisão do jogador, e não apenas a repetição de uma mesma ação; escolher entre alternativas prontas, sem estado inicial a ser transformado pelas ações do jogador, não conta como situação-problema».
- **Variante da etapa 1:** D01.1 `video.indicadores[1]`, mantida sem mudança — «cada um apresenta uma situação-problema: estado inicial visível, objetivo e mais de uma ação disponível ao jogador».
- **O que muda:** nada no texto; o problema é de leitura. Com os dois-pontos, o indicador parece redefinir o termo e diverge do glossário: «visível» e «disponível ao jogador» no lugar de «possível», e sem a decisão do jogador nem a exclusão das alternativas prontas. Lido como operacionalização do vídeo (o que se pode observar na gravação), está correto. O verificador não acusa, porque o texto é igual ao da etapa 1.
- **Critérios afetados:** D01.1. Sem entrada na lista de aceitas.
- **Proposta:** nova redação, que mantém o teste observável e tira a forma de definição: «cada um apresenta uma situação-problema, com estado inicial visível, objetivo e mais de uma ação disponível ao jogador». Aceitar âncora seria reduzir o indicador a «cada um apresenta uma situação-problema», como já está `documentacao.indicadores[0]`; adotar variante é deixar como está.

### Decisão 7 — `documentacao_equivalente`: texto novo do glossário

- **Âncora aplicada:** `documentacao_equivalente` (âncora nominal D22, mas o texto é novo) — «o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta». Em D22.1 e D22.2, um local-ponte liga a palavra do texto ao termo: `documentação` = «o GDD ou documento equivalente».
- **Variante da etapa 1:** D22.1 e D22.2 — «documentação é o documento de design (GDD), o guia do professor, o plano de aula ou outro documento equivalente que acompanha o jogo». Nos demais arquivos, «GDD», «GDD (ou documento equivalente)» ou «GDD, roteiro ou documento equivalente» sem definição.
- **O que muda:** (i) o documento precisa ser de projeto e descrever o conteúdo do jogo; (ii) material de divulgação ou de loja deixa de contar (a etapa 1 não dizia isso em nenhum arquivo); (iii) roteiro, mapa de nível e especificação entram como exemplos; (iv) a definição passa a valer em 37 critérios onde «GDD» não era definido. Um material de divulgação que a etapa 1 aceitaria em D22 como «outro documento equivalente» deixa de valer.
- **Critérios afetados:** todos os que usam «GDD» ou «documento equivalente»: D01.1, D02.1, D03.3, D04.1, D05.1, D06.1, D07.1, D10.1, D11.1, D12.1, D13.1, D15.1, D16.1, D17.1, D18.1, D19.1, D21.1, D22.1, D22.2, D23.1, D24.1, D25.1, D26.1, D27.1, D28.1–D40.1 (ficam de fora D03.1, D03.2, D08.1, D09.1, D14.1 e D20.1, que não usam o termo). Lista de aceitas: `clausulas` D22.1 e D22.2 e o item global `adicoes` `criterio: "*"` (`decisao: 7`).
- **Proposta:** aceitar âncora e manter o local-ponte em D22. Adotar variante seria trocar o texto do glossário pelo de D22 (sem «descreve seu conteúdo» e sem a exclusão de divulgação e loja). Alternativa de redação para D22: trocar «documentação» por «GDD ou documento equivalente» no texto de D22 e retirar o local-ponte.

### Decisão 8 — `objetivo_de_aprendizagem` em D22: «o listado na documentação»

- **Âncora aplicada:** D31 — «cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados».
- **Variante da etapa 1:** D22.1 — «objetivo de aprendizagem é o listado na documentação». Em D04.1, D11.1 e D36.1 o termo era usado sem definição, no sentido de «o que o GDD lista como objetivo».
- **O que muda:** o objetivo fica restrito a conceito, fato ou procedimento. Um objetivo listado na documentação que seja outra coisa (uma atitude, um valor, uma competência socioemocional) deixa de contar, e o momento de mediação que só trabalha esse objetivo deixa de valer em D22.1. A mesma restrição chega, pela chave acrescentada, a três critérios que não definiam o termo: em D04.1, o objeto cuja resposta só se relaciona a um objetivo desse tipo deixa de contar; em D11.1 e D36.1, o local `informação` («… relativo a ao menos um objetivo de aprendizagem listado no GDD …») encolhe junto, e a informação ligada só a uma atitude ou valor deixa de ser informação para o critério.
- **Critérios afetados:** D22.1, D04.1, D11.1, D36.1. Lista de aceitas: `clausulas` D22.1 e `adicoes` D04.1, D11.1 e D36.1 com `chave: objetivo_de_aprendizagem` (`decisao: 8`). D02.1 e D29.1 também receberam a chave sem decisão: D02.1 já conta por conceito («cada conceito listado como objetivo»), e em D29.1 a informação vale também quando se relaciona à missão.
- **Proposta:** aceitar âncora (é a mesma restrição que D31 já impõe aos demais critérios). Adotar variante seria um local em D22.1, `objetivo de aprendizagem`: «o listado na documentação», no lugar da chave do glossário, e um local equivalente («o listado no GDD ou documento equivalente») em D04.1, D11.1 e D36.1.

### Decisão 9 — `objetivo_de_aprendizagem` e `conteúdo` em D19, D23 e D25

- **Âncora aplicada:** `objetivo_de_aprendizagem` (D31), texto citado na decisão 8; «conteúdo» vira o local `conteúdo de aprendizagem`: «o listado no documento de design (GDD) ou documento equivalente» (D23.1, D25.1).
- **Variante da etapa 1:** D19.1, D23.1, D25.1 — «conteúdo e objetivo de aprendizagem são os listados no documento de design (GDD) ou documento equivalente».
- **O que muda:** para o objetivo, o mesmo que a decisão 8 (restrição a conceito, fato ou procedimento). Para «conteúdo», só a forma (plural → singular), sem mudança de sentido. Em D19.1 a definição de «conteúdo» some, sem efeito, porque a palavra não é usada fora dela. Em D25.1 «conteúdo» também aparece no sentido de parte do jogo («conteúdo opcional», «todo conteúdo é exigido pelo caminho da missão»), e o local cobre só o sentido de conteúdo de aprendizagem.
- **Extensão (b4, revisão de conteúdo):** o local se chamava `conteúdo`, mas D23.1 e D25.1 também usam «conteúdo» no sentido de parte do jogo («conteúdo opcional», «todo conteúdo é exigido pelo caminho da missão», «o conteúdo exibido depois da escolha»), e a chave parecia definir também esses usos. A chave passou a `conteúdo de aprendizagem`, com o texto sem mudança. Em D23.1, «situação sobre o conteúdo» e «narrativa que não trata do conteúdo» continuam no sentido de conteúdo de aprendizagem, que agora o nome do local indica; em D25.1 nenhum trecho usa a palavra nesse sentido, e o local poderia sair.
- **Critérios afetados:** D19.1, D23.1, D25.1. Lista de aceitas: `clausulas` D19.1, D23.1 e D25.1 (`decisao: 9`); a troca de nome tem par `remocoes`/`adicoes` (`tipo: equivalente`) em D23.1 e D25.1.
- **Proposta:** aceitar âncora. Ver também o candidato `conteúdo` na seção 5. Adotar variante seria restaurar o local composto da etapa 1 nos três critérios.

### Decisão 10 — `sessao_de_jogo`: texto novo do glossário

- **Âncora aplicada:** `sessao_de_jogo` (âncora nominal D36, mas o texto é novo) — «o período contínuo entre o jogador iniciar o jogo, ou carregar um estado salvo, e encerrá-lo (fechar o jogo ou voltar ao menu inicial)».
- **Variante da etapa 1:** nenhuma; D36.1 usava o termo sem definir, no local `estado organizado`: «… persiste quando o jogo o mantém guardado depois de o jogador sair da tela ou do momento em que operou, até o fim da sessão de jogo ou até o jogador desfazê-lo».
- **O que muda:** o glossário fixa onde a sessão termina. Voltar ao menu inicial encerra a sessão, então um jogo que descarta o estado organizado ao voltar ao menu atende à persistência de D36.1 (o estado precisa durar só «até o fim da sessão de jogo»); quem lesse «sessão» como «até fechar o jogo» daria nao_atendido ou parcial ao mesmo jogo. Carregar um estado salvo inicia nova sessão. É uma adição que muda o grau, por isso tem decisão própria.
- **Critérios afetados:** D36.1 (único critério com o gatilho «sessão de jogo»). D06, D07, D10, D13, D14, D15, D18, D22, D26 e D27 usam «sessão» sozinha, que não é gatilho e não muda. Lista de aceitas: `adicoes` D36.1 `sessao_de_jogo` (`decisao: 10`).
- **Proposta:** aceitar âncora. Nova redação, se o estado deve sobreviver à volta ao menu: «… e encerrá-lo fechando o jogo; voltar ao menu inicial não encerra a sessão».

### Decisão 11 — `persiste` (local de D12): duas redações no mesmo critério

- **Âncora aplicada:** a redação do enunciado de D12.1 (local) — «quando permanece disponível ao jogador depois de concluída a ação de combinar e só deixa de existir se o jogador o remover ou o consumir em uso posterior».
- **Variante da etapa 1:** D12.1 `video.procedimento` — «persiste quando permanece disponível depois da ação de combinar e só deixa de existir…».
- **O que muda:** a redação do vídeo era mais ampla (sem «ao jogador» e sem «concluída»). Um artefato que existe no estado do jogo mas não fica acessível ao jogador, ou que some antes de a ação terminar, poderia passar pelo vídeo e não pelo enunciado. Agora vale só a do enunciado.
- **Critérios afetados:** D12.1. Lista de aceitas: `clausulas` D12.1 (`decisao: 11`).
- **Proposta:** aceitar âncora (já era a redação do enunciado do critério).

### Decisão 12 — escalas: «nos termos do enunciado» passa a «nos termos do enunciado e das definições» (aplicada)

- **Aplicado:** em todo campo de texto de todo critério, a expressão exata «nos termos do enunciado» foi trocada por «nos termos do enunciado e das definições»: 95 ocorrências em 91 campos de 30 arquivos (D01, D09–D13, D15, D18–D40), 94 nas escalas e 1 em D32.1 `codigo.indicadores[3]`. Nenhum enunciado tinha a expressão.
- **Por quê:** na etapa 1 as definições ficavam no enunciado; agora ficam no bloco **Definições** do critério, e o ponteiro ficaria solto. Em ao menos 13 pontos ele nomeia um termo que não está mais no enunciado, por exemplo D15.1 escalas parcial e não atendido, D24.1 e D25.1 escala não atendido, D32.1 `codigo.indicadores[3]`, D36.1 escala parcial e as três escalas de D37.1 e de D38.1. O plano (item 3) pede que escalas e evidências remetam às definições.
- **Variante:** «nos termos das definições», que D29 já usava em dois procedimentos na etapa 1; não foi adotada sozinha porque os limiares e as condições de cada estado continuam no enunciado.
- **Critérios afetados:** os 91 campos acima. Lista de aceitas: uma entrada na lista `frases` (substituição global aplicada ao texto da etapa 1 antes da comparação, `decisao: 12`), no lugar de 91 entradas `campos`.
- **Reverter:** trocar a expressão de volta em `catalog/D*.yaml` e retirar a entrada `frases`.

### Decisão 13 — `documentacao_equivalente` × regra de D30: telas do jogo como documento equivalente

- **Âncora aplicada:** `documentacao_equivalente` (glossário) — «o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (…); material de divulgação ou de loja não conta».
- **Variante:** D30.1 `video.procedimento` e a regra de desempate de `documentacao.procedimento` e `video.procedimento` — «sem GDD, a tela de abertura, a tela de créditos ou a tela Sobre do jogo gravado é o documento equivalente» (texto da etapa 1, sem mudança).
- **O que muda:** a tela de abertura, de créditos ou Sobre não é documento de projeto, então, lendo só o glossário, um jogo sem GDD cairia em «ausência de GDD ou documento equivalente» (escala não atendido); pela regra de D30 as telas valem e o vídeo pode chegar a atendido ou parcial. Dois avaliadores podiam graduar o mesmo jogo de modo diferente. O texto do critério não mudou; foi acrescentado a D30.1 o local `documento equivalente neste critério`: «sem GDD, a tela de abertura, a tela de créditos ou a tela Sobre do jogo conta como documento equivalente para este critério», que deixa a exceção no bloco **Definições** ao lado da chave do glossário.
- **Critérios afetados:** D30.1. Lista de aceitas: `adicoes` D30.1 (`decisao: 13`).
- **Proposta:** manter a exceção como regra do critério (o local acrescentado), porque só D30 a usa. Alternativa: acrescentar ao texto do glossário uma cláusula de exceções («salvo quando o critério diz que outra fonte conta como documento equivalente») e retirar o local.

### Decisão 14 — `missao` acrescentada a critérios que não definiam o termo

- **Âncora aplicada:** `missao` (D28), texto citado na decisão 2, que traz «o jogo sem divisão em missões conta como uma única missão».
- **Variante da etapa 1:** nenhuma redação; estes critérios usavam «missão» sem definição, no sentido corrente, e a chave entrou porque o texto usa o gatilho ou por cascata de `desafio` («cada missão ou minijogo») e de `cenario_jogavel`.
- **O que muda:** (i) o jogo sem divisão em missões passa a contar como uma missão, de modo que os critérios que avaliam cada missão passam a valer para o jogo inteiro: em D01.1, um jogo sem missões precisa apresentar uma situação-problema para o jogo como um todo (antes, o avaliador podia considerar que não havia unidade a avaliar); em D05.1, o caminho obrigatório desse jogo é a sequência de objetivos exigidos para concluí-lo; em D03.2, o jogo é uma unidade que o jogador inicia por ação própria. (ii) Fase, capítulo ou nível com objetivo e condição de conclusão próprios passam a contar como missão: nos critérios que pedem algo de cada missão (D01.1, D03.2 e, por `desafio`, D19.1) há mais unidades avaliadas, e o grau pode baixar quando uma fase não cumpre o que o critério pede; nos que pedem ao menos uma ou contam as missões disponíveis (D03.1, D20.1, D21.1, D24.1), o grau pode subir.
- **Critérios afetados:** D01.1, D02.1, D03.1, D03.2, D03.3, D04.1, D05.1, D17.1, D18.1, D19.1, D20.1, D21.1, D22.1, D22.2, D23.1, D24.1, D25.1, D26.1, D36.1, D39.1, D40.1. Fica de fora D29.1, que já dizia na etapa 1 que «o jogo sem divisão em missões conta como uma única missão». Lista de aceitas: as 21 entradas `adicoes` com `chave: missao` (`decisao: 14`).
- **Proposta:** aceitar âncora: é o sentido que D28, D30, D31 e D33–D35 já usavam explicitamente, e impede que um jogo sem missões escape dos critérios que contam por missão. Adotar variante seria declarar `missão` em `termos_comuns` nesses critérios, o que deixaria `desafio` («cada missão ou minijogo») remetendo a um termo em sentido corrente, como na decisão 4.

## 2. Normalizações aplicadas sem decisão (redação equivalente)

Variantes que dizem o mesmo que a âncora com outras palavras. Na lista de aceitas, `tipo: equivalente`.

| termo | variante da etapa 1 | âncora | critérios |
|---|---|---|---|
| `situacao_problema` | enunciado: «situação-problema, isto é, uma situação com estado inicial, objetivo e mais de uma ação possível, cuja resolução exige…; escolher entre alternativas prontas … não conta como situação-problema» | D01 | D01.1 (enunciado) |
| `situacao_problema` | «Situação-problema exige estado inicial, objetivo e mais de uma ação possível; escolher entre alternativas prontas, sem estado inicial a ser transformado pelas ações do jogador, não conta» | D01 | D01.1 (documentacao.procedimento, video.procedimento: frase removida) |
| `situacao_problema` | «situação-problema, isto é, uma situação com estado inicial, objetivo e mais de uma ação possível» | D01 | D01.1 (documentacao.indicadores[0]) |
| `caminho_obrigatorio` | «caminho da missão é a sequência de objetivos exigidos para completá-la» | D05 | D05.1, D25.1 |
| `caminho_obrigatorio` | «fora do caminho da missão, isto é, que nenhum objetivo da missão exige» | D05 | D05.1 (documentacao.indicadores[0]) |
| `caminho_obrigatorio` | «caminho obrigatório, o mesmo que caminho da missão em D05, é a sequência de objetivos exigidos para completar a missão em curso no cenário, e fora do caminho obrigatório…» | D05 | D29.1 |
| `missao` | «missão é uma atividade com objetivo e condição de conclusão próprios, e o jogo sem divisão em missões conta como uma única missão» | D28 | D31.1, D33.1, D34.1, D35.1 |
| `missao` | a mesma oração dentro do local `premissa do jogo` («…, e missão é uma atividade…, de modo que o jogo sem divisão em missões conta como uma única missão») | D28 | D30.1 |
| `cenario_jogavel` | «… em que há uma missão em curso, e o jogo sem divisão em missões conta como uma única missão» (a regra do jogo sem divisão vem agora de `missao`) | D29 | D29.1 |
| `cenario_jogavel` | «… e o cenário em que nenhuma missão está em curso (hub, sandbox) não é cenário jogável» (o glossário acrescenta «não tem caminho obrigatório») | D29 | D39.1 |
| `comentário` (local) | «Comentário é um texto digitado pelo jogador», com maiúscula, repetido em `codigo.procedimento` junto com «outro jogador» e «sessão posterior» (cadeia removida) | enunciado de D14.1 | D14.1 |
| `competição` (local) | escala `nao_atendido` repetia a definição sem «(ranking, placar ou disputa)» | enunciado de D26.1 | D26.1 |
| `dispositivo` (local) | escala parcial: forma abreviada «… conforme definidos no enunciado» | definição completa do enunciado | D28.1 |
| personalização (local) | escala parcial que juntava duas cláusulas do enunciado («a ramificação apenas entre avançar … não é personalização do desafio, e a missão X em vez da missão Y conta só se…») | as duas cláusulas do enunciado | D34.1 |

## 3. Definições adicionadas a critérios que não as tinham

O critério passou a listar a chave do glossário porque o texto usa o gatilho, e a etapa 1 não definia o termo ali. Na lista de aceitas, `adicoes` (com `decisao` quando o item é uma decisão da seção 1).

- `documentacao_equivalente`: 37 critérios (decisão 7).
- `missao`: D01.1, D02.1, D03.1, D03.2, D03.3, D04.1, D05.1, D17.1, D18.1, D19.1, D20.1, D21.1, D22.1, D22.2, D23.1, D24.1, D25.1, D26.1, D29.1, D36.1, D39.1, D40.1 (todos menos D29.1 na decisão 14). Quase sempre por cascata do texto de `desafio` ou de `cenario_jogavel`; em D29.1 o critério já dizia «o jogo sem divisão em missões conta como uma única missão», e o glossário acrescenta «unidade do jogo… (fase, capítulo ou nível…)». Em D36.1 e D40.1, «missão ou desafio» fica redundante, com o mesmo sentido. Efeito geral: fase, capítulo ou nível com objetivo e conclusão próprios contam como missão, e o jogo sem divisão conta como uma missão.
- `minijogo`: 24 critérios (decisão 4).
- `desafio`: D01.1 («concluir o desafio»), D02.1 («o desafio da segunda missão»), D04.1 («resolver um desafio ligado a ele»), D18.1, D23.1, D25.1, D26.1, D36.1, D40.1. Todos no sentido de unidade, e não no corrente.
- `cenario_jogavel`: D05.1 («cenários jogáveis» já era o termo, sem definição no texto); D04.1 (decisão 5).
- `caminho_obrigatorio`: D04.1 (cascata, decisão 5), D39.1 (cascata do texto de `cenario_jogavel`).
- `objetivo_de_aprendizagem`: D02.1, D04.1, D11.1, D29.1, D36.1. Efeito: «só essa lista define os objetivos avaliados», e o objetivo fica restrito a conceito, fato ou procedimento (decisão 8 para D04.1, D11.1 e D36.1). Em D19.1, D22.1, D23.1 e D25.1 o termo substitui variante (decisões 8 e 9).
- `sessao_de_jogo`: D36.1 (decisão 10).

Reorganização de definições locais (sem mudança de sentido; cada caso tem par `remocoes`/`adicoes` na lista de aceitas quando a cláusula passou a abrir outro local):

- notas de escopo tiradas de dentro de um termo para o local `escopo`: D18, D30, D31, D32, D33, D34, D36, D37, D38, D40;
- regras de critério tiradas de dentro de um termo para um local próprio: D09.1 `opção avaliada como certa ou errada` (antes `precedência`), D10.1 `sequência de diálogo sem espera`, D12.1 `persiste`, D15.1 `relação com D06.1`, D19.1 `um elemento por função`, D30.1 `correspondência da premissa ao referente real` (antes `quantidade de elementos`; é um complemento da regra de correspondência do local `referente real`), D31.1 `confirmação pelo vídeo`, D33.1/D34.1 `regra de desempenho ou de ação`;
- termos desmembrados ou renomeados: D15.1 `ferramentas distintas`; D23.1/D25.1 `conteúdo de aprendizagem` (antes `conteúdo`, decisão 9); D19.1 `funções psicológicas superiores avaliadas` e `memória`; D21.1 `simulação substitui a ação do jogador`; D23.1 `situação trata de um objetivo de aprendizagem`; D33.1 `desafio personalizado por desempenho`; D34.1 `desafio personalizado pelas ações do jogador`; D35.1 `disponibilização a outro jogador`.

## 4. Termos usados no sentido corrente (`termos_comuns`)

O texto usa o gatilho de um termo do glossário em outro sentido; o critério declara isso em `definicoes.termos_comuns` e não lista a chave.

| critério | gatilho | sentido declarado |
|---|---|---|
| D02.1 | cenário | lugar ou situação do jogo em que o conceito é introduzido ou cobrado («missão ou cenário», «aparência do cenário») |
| D03.1 | cenário | ambiente em que as atividades aparecem disponíveis («menu, mapa ou cenário»), o que inclui hub sem missão em curso |
| D12.1 | cenário | lugar do jogo em que o artefato fica disponível («no cenário, inventário ou lista») |
| D23.1 | cenário | ambientação da história («mudança no cenário ou na história») |
| D28.1 | desafio | tarefa que a missão propõe ao jogador («como parte do desafio», no local `dispositivo`) |
| D30.1 | cenário | ambientação inventada («cenário ou enredo fictício») |
| D31.1 | cenário | ambiente do jogo («evento do cenário»); o sentido de D29 restringiria a situação do jogo aos espaços com missão em curso |
| D32.1 | cenário | o local `cenário` do critério (ambientação) |
| D38.1 | cenário | ambiente visual do jogo («elemento do cenário») |
| D40.1 | cenário | ambiente visual do jogo («elemento do cenário ou da interface») |

## 5. Candidatos a novos termos do glossário

Não migrados nesta PR. Os de texto idêntico podem entrar sem decisão; os de texto diferente exigem escolher a redação.

- **`jogador`** (texto idêntico): D13.1, D26.1, D27.1 — «uma pessoa que joga, e personagem não jogável não conta». Candidato forte.
- **`parâmetro do desafio`** e **`regra de desempenho ou de ação`** (texto idêntico): D33.1, D34.1.
- **`conteúdo de aprendizagem`** (texto idêntico, vem da decisão 9): D23.1, D25.1 — «o listado no documento de design (GDD) ou documento equivalente». Em D23.1 e D25.1 «conteúdo» sozinho também tem o sentido de parte do jogo, por isso a chave local não se chama mais `conteúdo`; decidir se o termo deve existir (em D25.1 ele não é usado).
- **`narrativa`** (texto idêntico): D23.1, D28.1 — «a sequência de eventos, cenas, personagens e diálogos que o jogo apresenta ao jogador».
- **`referente real`** (cláusula comum): D30.1 e D31.1 compartilham «uma situação, prática, profissão, fenômeno ou projeto que existe ou ocorre fora do jogo e que o GDD ou documento equivalente identifica por nome ou descrição específica»; D30 acrescenta exemplos e exclusões. Proposta dos lotes: glossário com a cláusula comum mais os exemplos e exclusões de D30, e a correspondência premissa–referente como local de D30.
- **`informação`** (texto diferente): D11.1 e D36.1; D36 acrescenta «coletado pelo jogador ou fornecido pelo jogo». Um termo único precisaria da forma ampla de D36, com D11 restrito pelo local `coletar`.
- **`objeto interativo`** (texto diferente): D32.1 exige resposta do jogo (mudança de estado ou mensagem) e não lista «examinar»; D38.1 lista «examinar» e não exige resposta.
- **`abertura`** (texto diferente): D28.1 `abertura da missão` inclui «cena»; D37.1 `abertura da unidade` não.
- **`sessão posterior`** (só D14.1 define; D15.1 usa «registro lido em sessão posterior» sem definição): relação com `sessao_de_jogo` a decidir.
- **`outro jogador`** (texto diferente): D14.1 («um jogador com perfil ou conta diferente do autor») e D35.1; só o nome coincide.
- **`unidade`** (D37.1): «cada missão ou minijogo» é o texto de `desafio`. Fica como local porque «unidade» é o nome usado nos indicadores e escalas de D37.
- **`tarefa`**: ver decisão 3 (a proposta é não criar o termo).
- Padrão de redação, não termo: «X avaliado» (D31.1 `objetivo avaliado`, D37.1 `unidade avaliada`, D38.1 `item avaliado`, D40.1 `resposta avaliada`) tem a mesma estrutura com textos diferentes; caberia no guia de redação do schema.

## Observações

- Três linhas do `docs/catalogo.md` renderizado passam de 1.500 caracteres. São textos da etapa 1, não tocados pela migração: D10.1, procedimento de vídeo (2.160 caracteres, com a «Limitação conhecida» e a «Regra de desempate»; na etapa 1 o campo tinha 3.521); D31.1, **Justificativa do nível** (1.665); D31.1, procedimento de vídeo (1.506).
- Glosas «isto é» de termos locais foram mantidas onde já estavam fora dos blocos de definição na etapa 1 (D18, D20, D21, D22, D23, D26, D29, D31, D33, D34, D38, D39). A de D38.1 no enunciado («têm forma escrita, isto é, texto na tela e não apenas áudio») resume o local `forma escrita` e poderia sair com uma entrada `campos` com `remover`; não foi feito.
- Em D25.1, a oração do local `conteúdo opcional` «trata de um objetivo de aprendizagem, isto é, cita ou descreve conceito, fato ou procedimento listado…» foi mantida: define «tratar de», e não o objetivo de aprendizagem.
- Relatórios dos lotes, com o detalhe de cada critério: `.superpowers/sdd/definicoes-lote-a.md` (D01–D13), `definicoes-lote-b.md` (D14–D27), `definicoes-lote-c.md` (D28–D40); são notas locais, não versionadas. Correspondência dos ids dos lotes com os números deste documento: c1 → 1, a2 → 2, a3 e b3 → 3, a5 → 5, a1 → 6, b1 → 7, b2 → 8, b4 → 9, a4 → 11; as decisões 4, 7 (parte global), 10 e 12 não tinham id nos lotes; 13 e 14 vieram da revisão de conteúdo posterior aos lotes.
