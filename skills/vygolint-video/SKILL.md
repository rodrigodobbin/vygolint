---
name: vygolint-video
description: Use when a gameplay video must become evidence for a vygolint evaluation - extracts frames with ffmpeg, reads them as images and writes registro_video.yaml with timestamped events; accepts a hand-written log when ffmpeg is missing
---

# Transformar vídeo de gameplay em evidência

> O resultado de uma avaliação vygolint expressa conformidade com as diretrizes de Carvalho (2020) e não classifica o jogo como sociointeracionista.

Você não assiste vídeo: você extrai quadros, lê os quadros como imagens e escreve um registro com timestamps. O registro (`registro_video.yaml`) é a prova que os critérios citam no formato `arquivo hh:mm:ss[-hh:mm:ss] — observação`.

Entrada: um arquivo de vídeo e a pasta de saída da avaliação (`<pasta>`, padrão `vygolint-out/`). Saída: `<pasta>/registro_video.yaml` (com mais de um vídeo, `<pasta>/registro_video_<nome>.yaml`, um por vídeo).

## 1. Verifique as ferramentas

1. Rode `command -v ffmpeg ffprobe`.
2. Se os dois caminhos aparecem, siga para a seção 2.
3. Se algum falta, vá para a seção 6 (sem ffmpeg).

## 2. Extraia os quadros

Cada bloco abaixo é autônomo: o shell não guarda variáveis entre comandos. Substitua os valores de `VIDEO`, `OUT`, `NOME` e `INTERVALO` pelos reais em todo bloco.

1. Leia a duração (em segundos):

```bash
VIDEO="gameplay/sessao1.mp4"; OUT="vygolint-out"; NOME="sessao1"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$VIDEO"
```

2. Converta a duração para hh:mm:ss e anote em `duracao`.
3. Escolha `INTERVALO=5`; para vídeo com mais de 30 minutos (1800 s), escolha `INTERVALO=10`.
4. Extraia um quadro a cada `INTERVALO` s e as mudanças de cena:

```bash
VIDEO="gameplay/sessao1.mp4"; OUT="vygolint-out"; NOME="sessao1"; INTERVALO=5
mkdir -p "$OUT/frames/$NOME"
ffmpeg -y -i "$VIDEO" -vf "fps=1/$INTERVALO" "$OUT/frames/$NOME/t%05d.png"
ffmpeg -y -i "$VIDEO" -vf "select='gt(scene,0.4)',showinfo" -vsync vfr "$OUT/frames/$NOME/cena%04d.png" 2> "$OUT/frames/$NOME/cenas.log"
grep -o "pts_time:[0-9.]*" "$OUT/frames/$NOME/cenas.log"
```

5. Se o ffmpeg recusar `-vsync vfr`, troque por `-fps_mode vfr`.

Timestamp de cada quadro:

- `tNNNNN.png` (quadros periódicos): o quadro `t%05d` de índice k corresponde ao instante (k − 1) × INTERVALO s, com erro de até INTERVALO/2 s; para um instante exato use a extração de quadro único abaixo. Ex. com INTERVALO=5: `t00001.png` = 00:00:00; `t00013.png` = 60 s = 00:01:00.
- `cenaNNNN.png` (mudanças de cena): o instante é o N-ésimo `pts_time` impresso pelo `grep`, em segundos.
- Converta segundos em hh:mm:ss com `python3 -c "import sys; s=int(float(sys.argv[1])); print(f'{s//3600:02d}:{s%3600//60:02d}:{s%60:02d}')" 750`.

## 3. Leia os quadros em ordem

1. Liste os quadros: `OUT="vygolint-out"; NOME="sessao1"; ls "$OUT/frames/$NOME"`.
2. Leia primeiro os quadros `cena*.png` em ordem: eles marcam trocas de tela, missão ou cena.
3. Leia os quadros `t*.png` em ordem, em lotes de 10 a 20, para preencher o que acontece entre as trocas.
4. Para localizar um instante com mais precisão (início de missão, momento de um feedback), extraia quadros extras do trecho (extração de quadro único por segundo): `VIDEO="gameplay/sessao1.mp4"; OUT="vygolint-out"; NOME="sessao1"; ffmpeg -y -ss 00:04:05 -t 10 -i "$VIDEO" -vf "fps=1" "$OUT/frames/$NOME/x0405_%02d.png"` (o quadro k mostra 00:04:05 + (k − 1) s).
5. Transcreva o texto da tela literalmente; não parafraseie mensagens de feedback.

## 4. Registre os eventos

Uma entrada em `eventos` por evento observável, em ordem de tempo. Para cada tipo, registre:

| tipo | `t` e `fim` | `descricao` |
|---|---|---|
| `missao` | início e fim | nome; estado inicial visível; objetivo; ações disponíveis; como foi concluída ou abandonada |
| `minijogo` | início e fim | nome; regras visíveis; objetivo; ações disponíveis; resultado |
| `feedback` | instante | ação que o disparou (acerto ou erro); texto literal exibido; se indica a próxima ação |
| `texto` | instante (e `fim` se longo) | texto literal de instrução, diálogo ou conteúdo; quem fala |
| `escolha` | instante | alternativas visíveis; alternativa escolhida; o que mudou em seguida |
| `passivo` | início e fim | o que o jogador assiste sem agir (cena, animação, texto sem interação); quando surgiu a opção de avançar |
| `outro` | instante (e `fim` se houver) | menus, configurações, pausa, perfil, comunicação com outros jogadores, tudo o que não cabe acima |

Medidas de tempo seguem o conteúdo, não o ritmo do jogador gravado (regra 14 de autoria do catálogo):

1. A duração de uma cena ou trecho passivo vai do início até a primeira oportunidade de avançar (botão "continuar", fim da animação), não até o momento em que o jogador avançou.
2. Se o jogador demorou a avançar, registre `fim` na primeira oportunidade e anote a espera na `descricao`.
3. Se o vídeo não mostra quando surgiu a opção de avançar, escreva isso na `descricao`; o critério usará código ou documentação como fallback.
4. O que o jogador não fez (área não visitada, missão não alcançada) não é evidência de que o jogo não permite: registre só o que aparece.

## 5. Formato de `registro_video.yaml`

```yaml
video: "gameplay/sessao1.mp4"
duracao: "00:12:31"
quadros: "vygolint-out/frames/sessao1"   # pasta dos quadros, quando extraídos
eventos:
  - t: "00:00:40"
    fim: "00:03:50"
    tipo: missao            # missao | minijogo | feedback | texto | escolha | passivo | outro
    descricao: "Missão 1: coletar amostras; estado inicial visível, três ações disponíveis"
  - t: "00:03:12"
    tipo: feedback
    descricao: "erro na balança; texto: 'Some as massas antes de pesar'; indica a próxima ação"
```

1. Todo tempo no formato "hh:mm:ss", entre aspas.
2. `fim` só nos eventos com duração.
3. Confira o YAML do arquivo que você gravou (use o mesmo `ARQ` do nome do arquivo: `registro_video.yaml` ou `registro_video_<nome>.yaml`): `OUT="vygolint-out"; ARQ="registro_video.yaml"; python3 -c "import sys, yaml; yaml.safe_load(open(sys.argv[1], encoding='utf-8'))" "$OUT/$ARQ"`.
4. Nas provas de `avaliacao.yaml`, cite o arquivo de vídeo e o tempo do evento, não o arquivo de quadro.

## 6. Sem ffmpeg

1. Diga ao usuário que o ffmpeg não está instalado e que há duas saídas: instalar o ffmpeg ou escrever o registro à mão.
2. Para o registro à mão, mostre ao usuário o formato da seção 5 e a tabela de tipos da seção 4, e peça um `registro_video.yaml` por vídeo, com `quadros` omitido.
3. Ao receber o registro, confira o YAML e siga a avaliação usando-o como fonte `video`.
4. Se o usuário não puder fornecer nem ffmpeg nem registro, retire `video` de `contexto.fontes` e de `contexto.artefatos` em `avaliacao.yaml` e avise que os critérios que dependem só de vídeo ficarão `nao_avaliado`.

Não rotule o jogo nas descrições: registre o que a tela mostra.
