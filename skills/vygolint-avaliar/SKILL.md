---
name: vygolint-avaliar
description: Use when asked to evaluate an educational game against the Carvalho (2020) guidelines or to produce a vygolint conformance report - orchestrates context, inventory, per-criterion grading, avaliacao.yaml and the report script
---

# Avaliar um jogo com o vygolint

> O resultado de uma avaliação vygolint expressa conformidade com as diretrizes de Carvalho (2020) e não classifica o jogo como sociointeracionista.

Use esta skill quando pedirem "avalie este jogo com o vygolint" ou um relatório de conformidade. Ao final, o usuário recebe uma pasta com `avaliacao.yaml`, `relatorio.md`, `relatorio.html` e `resultado.yaml`.

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
4. Gere o esqueleto de `avaliacao.yaml` na pasta de saída (`vygolint-out` no diretório de trabalho, ou a pasta que o usuário indicar; chame-a de `<pasta>` daqui em diante). O script cria a pasta:

```bash
python3 "${VYGOLINT_ROOT}/scripts/vygolint_scaffold.py" --jogo "Nome do jogo" --sala-de-aula false \
  --fontes codigo,documentacao,video \
  --artefato codigo=./src --artefato documentacao=docs/gdd.pdf --artefato documentacao=docs/guia-professor.md \
  --artefato video=gameplay/sessao1.mp4 \
  --avaliador "Claude Code (claude-fable-5-1)" --out vygolint-out
```

5. Em `--fontes`, liste só as fontes disponíveis; dê ao menos um `--artefato fonte=caminho` por fonte (repita a opção para cada caminho). Escreva os caminhos relativos ao diretório de trabalho: as provas citam os mesmos caminhos.
   - O artefato é um arquivo ou uma pasta. **Uma pasta põe no escopo todos os arquivos dentro dela**: `--artefato documentacao=docs` significa que todo documento em `docs/` deve ser lido, e `--artefato video=gameplay` que todo vídeo em `gameplay/` deve virar registro. O esqueleto lista, em comentário sob cada fonte, os arquivos de vídeo e de documentação que entraram no escopo.
   - Estar no escopo não é contar como evidência: todo documento do escopo é lido e classificado no inventário (passo 2), e só o que é GDD ou documento equivalente serve de prova. Material de divulgação ou de loja é lido, listado como "não conta" e não é citado.
   - Para código, a pasta delimita onde as provas podem apontar; não há conferência arquivo a arquivo. Aponte a pasta do código do jogo, não a raiz com dependências e binários.
   - Fonte que você usou mas não está nesta máquina (repositório sem cópia local, documento visto em outra sessão): `--externa fonte="descrição"`. Ela entra em `contexto.fontes_externas` e fica fora das conferências do script.
6. Em `--avaliador`, escreva o harness e o modelo; o script acrescenta a versão do vygolint e a data de hoje.
7. O esqueleto sai com o cabeçalho e as 43 entradas do catálogo, na ordem dos ids, cada uma precedida de um comentário com o enunciado e as fontes do contexto que o critério aceita:
   - `grau: nao_avaliado` com `razao: "PREENCHER"` nos critérios que alguma fonte do contexto pode decidir;
   - `nao_avaliado` com a razão já escrita nos critérios que nenhuma fonte do contexto pode decidir;
   - `fora_do_contexto` com razão nos critérios de diretriz com `aplicabilidade` (hoje D22) quando `--sala-de-aula false`.
8. O script cria também `<pasta>/inventario.md`, com as seções do passo 2 e uma linha por arquivo de documentação e de vídeo do escopo, tudo marcado `PREENCHER`.
9. O script recusa sobrescrever um `avaliacao.yaml` existente e mantém um `inventario.md` que já exista. Se a sessão caiu, não rode de novo: retome os arquivos que existem (passos 2 e 3). Use `--force` só para descartar a avaliação e recomeçar; ele regrava os dois.

## Passo 2 — Inventário

1. Código: liste módulos, cenas, telas, manipuladores de entrada (handlers) e de rede, persistência e textos exibidos ao jogador.
2. Documentação: liste os documentos e suas seções; identifique o GDD ou documento equivalente (definição em `${VYGOLINT_ROOT}/catalog/definicoes.yaml`, chave `documentacao_equivalente`) e a lista de objetivos de aprendizagem.
3. Vídeo: para cada arquivo de vídeo do escopo (os listados no cabeçalho do esqueleto), aplique a skill `vygolint-video` e obtenha `<pasta>/registro_video.yaml` (um por vídeo; com mais de um vídeo, `<pasta>/registro_video_<nome>.yaml`). O campo `video` de cada registro traz o caminho do arquivo como está nos artefatos. A skill grava também `<pasta>/registro_audio_<nome>.yaml` (trechos com som e, havendo reconhecedor de fala, a transcrição).
4. Leia `${VYGOLINT_ROOT}/catalog/definicoes.yaml` antes de contar qualquer coisa.
5. Preencha `<pasta>/inventario.md`, que o esqueleto criou: troque cada `PREENCHER`, acrescente linhas às tabelas e, onde não há item, apague a tabela e escreva "Nenhum observado". Não renomeie a coluna `Classificação` nem tire as crases dos caminhos: o script lê essa tabela. Seções, cada item com onde aparece (`arquivo:linha`, `documento p. N` ou `vídeo hh:mm:ss`):
   - Missões (nos termos da definição de missão)
   - Minijogos
   - Cenários jogáveis
   - Objetivos de aprendizagem
   - Fontes lidas: na tabela de documentação, uma linha por documento do escopo, com a `Classificação` (`documento equivalente`; `não conta` e o motivo, como material de divulgação; ou `não abriu`); na de vídeo, uma linha por vídeo com o registro correspondente; em código, o que foi lido em cada pasta
   - Fontes que não foi possível abrir
6. Use essas listas em todos os critérios que contam missões, minijogos, cenários ou objetivos; não recontar por critério evita contagens divergentes.

## Passo 3 — Critérios

1. Liste os critérios do catálogo: `grep -h "^  - id:" "${VYGOLINT_ROOT}"/catalog/D*.yaml` (devem ser 43).
2. Para cada diretriz de D01 a D40, em ordem:
   1. Leia `${VYGOLINT_ROOT}/catalog/Dnn.yaml` inteiro.
   2. Leia o bloco **Definições** de cada critério em `${VYGOLINT_ROOT}/docs/catalogo.md` (seção `#### Dnn.k`), onde o texto do glossário já vem impresso.
   3. Se a diretriz tem `aplicabilidade` não nula e o contexto não a satisfaz (hoje só D22, quando `sala_de_aula: false`), o esqueleto já traz `grau: fora_do_contexto` com `razao` em cada critério da diretriz: confira e passe à próxima diretriz.
   4. Para cada critério, aplique a skill `vygolint-criterio` e obtenha a entrada.
   5. Substitua, em `<pasta>/avaliacao.yaml`, a entrada do esqueleto de cada critério da diretriz (as linhas `grau` e `razao` sob o id) pela entrada obtida; mantenha o comentário e a ordem dos ids. Nenhuma `razao` pode continuar `"PREENCHER"`.
   6. Confira que o arquivo continua YAML válido: `python3 -c "import sys, yaml; yaml.safe_load(open(sys.argv[1], encoding='utf-8'))" <pasta>/avaliacao.yaml`.
3. Grave após cada diretriz. Se a sessão cair, releia `avaliacao.yaml` e retome no primeiro critério cuja `razao` ainda é `"PREENCHER"`.
4. Todo critério do catálogo precisa de entrada. Sem fonte que decida, use `grau: nao_avaliado` com `razao` que diz qual fonte faltou ou o que ela não mostrou.
5. Não grave `recomendacao`, nível nem nota de dependência: o script os tira do catálogo. `depende_de` também é do script.

Entrada completa de um critério (formato de `${VYGOLINT_ROOT}/docs/conformidade.md`, seção 6, e o exemplo em `${VYGOLINT_ROOT}/docs/exemplo/avaliacao.yaml`):

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

### Passo 3 em partes, com subagentes (opcional)

Em harness com subagentes, o passo 3 pode ser dividido: cada subagente gradua um grupo de critérios e grava um arquivo; um script junta os arquivos. Os passos 1, 2, 4 e 5 continuam com você. Em teste com um jogo só de vídeo, um subagente por categoria deu os mesmos graus da avaliação em sequência em 32 de 43 critérios, e 41 de 43 quando se olha só atendido contra não atendido; os 12 subagentes somaram cerca de 1,2 milhão de tokens e terminaram em pouco mais de 4 minutos (`${VYGOLINT_ROOT}/docs/experimentos/2026-11-06-subagente-por-categoria.md`). O custo da avaliação em sequência não foi medido, então o teste não diz qual dos dois modos é mais barato.

1. Termine antes os passos 1 e 2. Os subagentes graduam a partir de `inventario.md` e dos registros; sem eles, cada um reconta e reassiste por conta própria.
2. Divida os critérios. Um subagente gasta dezenas de milhares de tokens só para ler a skill, as regras e os registros, mesmo para um critério. Agrupe as categorias pequenas: por exemplo, Interação; Mediação; Autonomia, Socialização, Lúdico e Realismo; Personalização, Organização, Resolução de problemas, Linguagem, Atenção e Aprendizado. A categoria de cada diretriz está no campo `categoria` de `${VYGOLINT_ROOT}/catalog/Dnn.yaml`.
3. Entregue a cada subagente, por escrito, tudo de que ele precisa; ele não vê esta conversa:
   - a lista exata dos ids que ele gradua;
   - o caminho de `${VYGOLINT_ROOT}/skills/vygolint-criterio/SKILL.md`, para ler inteiro e seguir (não conte com a skill estar carregada nele), e os de `${VYGOLINT_ROOT}/catalog/`, `${VYGOLINT_ROOT}/docs/catalogo.md` e `${VYGOLINT_ROOT}/docs/conformidade.md`;
   - o contexto do cabeçalho: `sala_de_aula`, `fontes` e `artefatos`, com os caminhos como estão em `avaliacao.yaml`;
   - os caminhos de `inventario.md`, de cada `registro_video*.yaml` e `registro_audio_*.yaml`, e da pasta de quadros;
   - o arquivo de saída: `<pasta>/partes/<nome>.yaml`, um mapa cujas chaves de topo são os ids (sem `criterios:` em volta), cada um com a entrada no formato de `vygolint-criterio`;
   - o que responder: uma linha `id: grau` por critério, as dúvidas, e os **achados**, descritos no item 4.
4. Os fatos vêm do registro e do inventário, que são os mesmos para todos. O subagente pode abrir quadros para conferir, mas, se vir algo que o registro não traz ou contradiz, não deve só usá-lo nas provas: deve relatar o achado na resposta, com o instante e o que viu. No teste, dois subagentes olharam as mesmas folhas e descreveram uma barra que crescia sozinha; um terceiro mediu quadro a quadro e mostrou que ela só subia em degraus. Sem o relato, o relatório final sairia com provas que se contradizem.
5. Não deixe um subagente ler a parte de outro, nem um `avaliacao.yaml` já preenchido.
6. Junte as partes: `python3 "${VYGOLINT_ROOT}/scripts/vygolint_juntar.py" <pasta>/avaliacao.yaml`. O script lê `<pasta>/partes/*.yaml`, confere cada id contra o catálogo, recusa id repetido em duas partes e grava cada entrada no lugar do bloco do esqueleto, mantendo cabeçalho e comentários. Parte com o nome de uma categoria (`mediacao.yaml`) ganha uma nota se faltar critério dela. Com erro, o script não altera o arquivo.
7. Revise antes do passo 4, porque ninguém além de você viu o conjunto:
   - confira cada achado no vídeo; se procede, corrija `registro_video.yaml` e `inventario.md` e regradue os critérios que citam aquele fato;
   - leia as dúvidas de cada subagente e decida os casos em que ele mesmo apontou a leitura alternativa;
   - compare critérios que julgam o mesmo fato em partes diferentes (os erros do jogador em D17.1 e D40.1; o desafio em D01.1, D08.1 e D19.1) e alinhe as provas;
   - confira `nao_avaliado` contra `nao_atendido` pela regra de `vygolint-criterio` (seção 3, item 5): é onde os subagentes mais divergem entre si.

## Passo 4 — Relatório

1. Rode: `python3 "${VYGOLINT_ROOT}/scripts/vygolint_report.py" <pasta>/avaliacao.yaml`
2. Saída esperada: `OK: nível ... -> <pasta>/relatorio.md, <pasta>/relatorio.html, <pasta>/resultado.yaml`. O `relatorio.html` é a mesma avaliação em página navegável (abas Resumo, Para o professor, Para quem desenvolve, Para a equipe e Todos os critérios), gerada do mesmo `avaliacao.yaml`; abre no navegador sem servidor.
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

5. Nunca edite `relatorio.md`, `relatorio.html` nem `resultado.yaml`: eles são gerados. Toda correção vai em `avaliacao.yaml`; depois rode o script de novo, que regrava os três.
6. Depois de validar, o script confere o lugar citado em cada prova e imprime um aviso por problema (linhas `aviso ...`, com a contagem no fim da linha `OK`). Avisos não impedem o relatório, mas cada um aponta uma prova que o leitor não vai conseguir conferir. Corrija `avaliacao.yaml` e rode de novo até não sobrar aviso:

| Aviso | O que fazer |
|---|---|
| `aviso Dnn.k: razao ainda contém PREENCHER` | Gradue o critério, ou escreva a razão do `nao_avaliado`. |
| `aviso avaliacao: avaliador ainda contém PREENCHER` | Escreva o harness e o modelo no cabeçalho. |
| `aviso avaliacao: arquivo citado não encontrado: X (N provas: ...)` | Corrija o caminho nas provas (relativo ao diretório de trabalho). Se a fonte de fato não está nesta máquina, declare-a em `contexto.fontes_externas` e diga isso ao usuário na entrega. |
| `aviso avaliacao: artefato de F não encontrado: X` | Corrija o caminho em `contexto.artefatos.F`; enquanto um artefato da fonte não é achado, o script não confere o escopo dela. |
| `aviso avaliacao: arquivo citado fora dos artefatos de F: X (N provas: ...)` | A prova cita um arquivo que não foi declarado como fonte F. Se o arquivo é fonte legítima, acrescente-o (ou a pasta dele) a `contexto.artefatos.F`; se não é, troque a prova. |
| `aviso avaliacao: vídeo do escopo sem registro_video nem prova: X` | Aplique `vygolint-video` a X e use o registro nos critérios; ou tire X do escopo declarando arquivos em vez da pasta. |
| `aviso avaliacao: documento do escopo sem prova nem menção no inventario.md: X` | Leia X e acrescente a linha dele à tabela de documentação do `inventario.md`, com a classificação. |
| `aviso avaliacao: documento do escopo sem classificação no inventario.md: X` | A linha de X existe mas a `Classificação` está vazia ou `PREENCHER`: leia X e classifique. |
| `aviso avaliacao: documento citado como prova mas classificado "não conta" no inventario.md: X (N provas: ...)` | Ou a classificação está errada (corrija o inventário), ou as provas citam material que não é GDD nem documento equivalente (troque as provas e regradue os critérios). |
| `aviso inventario: ainda contém PREENCHER (N ocorrências)` | Termine o `inventario.md`: troque cada `PREENCHER` ou apague a tabela vazia e escreva "Nenhum observado". |
| `... prova N: linha L não existe: X tem M linhas` | Releia o arquivo e cite a linha certa. |
| `... prova N: lugar deve ter a forma arquivo:linha` | Reescreva a prova de código como `arquivo:linha — trecho`. |
| `... prova N: lugar deve citar página ou seção` | Reescreva a prova de documentação como `documento p. N — trecho` ou `documento, seção X — trecho`. |
| `... prova N: lugar deve citar o instante em hh:mm:ss` | Reescreva a prova de vídeo como `arquivo hh:mm:ss[-hh:mm:ss] — observação`. |
| `... prova N: instante T inválido` ou `fica depois do fim do vídeo` | Confira o instante no `registro_video.yaml` e corrija. |
| `... prova N: intervalo A-B termina antes de começar` | Inverta ou corrija o intervalo. |

7. Para exigir zero avisos (por exemplo, em CI), rode com `--strict`: avisos passam a contar como erro e nada é gerado. A duração do vídeo só é conferida quando o `ffprobe` está instalado.

## Passo 5 — Revisão e entrega

Leia `<pasta>/relatorio.md` e confira:

- [ ] A cláusula de Carvalho (2020) está na seção 1.
- [ ] `avaliacao.yaml` tem 43 entradas, uma por critério do catálogo.
- [ ] Toda prova aponta um lugar verificável e o lugar existe: a última execução do script não imprimiu avisos, ou cada aviso restante foi explicado ao usuário.
- [ ] Todo `nao_avaliado` e `fora_do_contexto` tem `razao` que diz qual fonte faltou ou qual contexto não vale.
- [ ] Cada bloqueio traz ao menos uma via de recomendação ou uma nota de dependência; cada parcial traz ao menos uma via (o script escolhe as vias pela evidência disponível; não recalcule).
- [ ] Nenhum texto seu (provas, observações, razões, mensagem de entrega) rotula o jogo como sociointeracionista, behaviorista ou outro rótulo teórico.

Entregue ao usuário:

1. Os caminhos de `avaliacao.yaml`, `relatorio.md`, `relatorio.html` e `resultado.yaml` (e de `inventario.md` e dos registros de vídeo e de áudio). Indique o `relatorio.html` para quem vai ler o resultado (professor, equipe de desenvolvimento, coordenação) e o `relatorio.md` para anexar em issue ou versionar.
2. O nível alcançado como o script o imprimiu, sem reinterpretá-lo.
3. Os bloqueios e parciais, remetendo ao relatório.
4. Se algum vídeo tem som e não foi transcrito, diga isso e quais critérios dependeram de áudio.
5. A cláusula, literal: "O resultado de uma avaliação vygolint expressa conformidade com as diretrizes de Carvalho (2020) e não classifica o jogo como sociointeracionista."
