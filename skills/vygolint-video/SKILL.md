---
name: vygolint-video
description: Use when a gameplay video must become evidence for a vygolint evaluation - extracts one thumbnail per second with ffmpeg, tiles them into contact sheets, reads the sheets as images, measures where the audio track has sound and writes registro_video.yaml with timestamped events; accepts a hand-written log when ffmpeg is missing
---

# Transformar vídeo de gameplay em evidência

> O resultado de uma avaliação vygolint expressa conformidade com as diretrizes de Carvalho (2020) e não classifica o jogo como sociointeracionista.

Você não assiste vídeo: você extrai quadros, monta folhas de contato, lê as folhas como imagens e escreve um registro com timestamps. O registro (`registro_video.yaml`) é a prova que os critérios citam no formato `arquivo hh:mm:ss[-hh:mm:ss] — observação`.

Entrada: um arquivo de vídeo e a pasta de saída da avaliação (`<pasta>`, padrão `vygolint-out/`). Saída: `<pasta>/registro_video.yaml` (com mais de um vídeo, `<pasta>/registro_video_<nome>.yaml`, um por vídeo) e `<pasta>/registro_audio_<nome>.yaml`, que diz em que trechos a faixa de áudio tem som e, havendo reconhecedor de fala, o que é dito.

## 1. Verifique as ferramentas

1. Rode `command -v ffmpeg ffprobe`.
2. Se os dois caminhos aparecem, siga para a seção 2.
3. Se algum falta, vá para a seção 6 (sem ffmpeg).

## 2. Extraia os quadros

Cada bloco abaixo é autônomo: o shell não guarda variáveis entre comandos. Substitua os valores de `VIDEO`, `OUT` e `NOME` pelos reais em todo bloco.

1. Leia a duração (em segundos):

```bash
VIDEO="gameplay/sessao1.mp4"; OUT="vygolint-out"; NOME="sessao1"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$VIDEO"
```

2. Converta a duração para hh:mm:ss e anote em `duracao`.
3. Extraia uma miniatura por segundo e monte as folhas de contato (cada folha é uma grade de 4 colunas por 5 linhas, isto é, 20 s de vídeo em uma imagem):

```bash
VIDEO="gameplay/sessao1.mp4"; OUT="vygolint-out"; NOME="sessao1"
mkdir -p "$OUT/frames/$NOME/sec" "$OUT/frames/$NOME/folhas"
ffmpeg -y -i "$VIDEO" -vf "fps=1,scale=640:-2" "$OUT/frames/$NOME/sec/s%05d.png"
ffmpeg -y -i "$OUT/frames/$NOME/sec/s%05d.png" -vf "tile=4x5:padding=4:margin=4" "$OUT/frames/$NOME/folhas/f%03d.png"
```

4. Para vídeo com mais de 30 minutos (1800 s), troque nos dois comandos: `fps=1/2,scale=480:-2` (uma miniatura a cada 2 s) e `tile=5x6` (60 s por folha). Anote o passo (1 ou 2 s) e a grade que usou.
5. Liste os instantes de mudança de cena. O comando não grava imagens, só os instantes; por isso não leva `-vsync` nem `-fps_mode` (versões recentes do ffmpeg recusam `-vsync`):

```bash
VIDEO="gameplay/sessao1.mp4"
ffmpeg -hide_banner -i "$VIDEO" -vf "select='gt(scene,0.4)',showinfo" -an -f null - 2>&1 | grep -o "pts_time:[0-9.]*"
```

6. Se não sair nenhum instante, confira primeiro se o ffmpeg imprimiu erro (rode sem o `grep`). Se o comando funcionou e saiu menos de um instante por minuto de vídeo, repita com `gt(scene,0.2)`.
7. Meça o áudio. Os quadros não mostram se uma legenda também é falada nem se um erro toca um som; a faixa de áudio mostra:

```bash
VIDEO="gameplay/sessao1.mp4"; OUT="vygolint-out"
python3 "${VYGOLINT_ROOT}/scripts/vygolint_audio.py" "$VIDEO" --out "$OUT"
```

   O script grava `$OUT/registro_audio_<nome>.yaml` (`<nome>` é o nome do vídeo sem extensão) com:
   - `faixa_de_audio`: se o arquivo tem áudio;
   - `trechos_com_som`: intervalos `t`–`fim` em que o áudio passa do limiar de silêncio (−50 dB, ajustável com `--limiar`). O trecho diz que há som, não o que ele é: pode ser fala, música ou efeito;
   - `transcricao`: `nao_disponivel` até você juntar uma transcrição (seção 7), ou `sem_faixa_de_audio`.

   Fora dos trechos com som não há fala nem efeito: isso é fato medido, e vale como evidência de ausência de som naquele instante.
   Quando um único trecho cobre quase todo o vídeo (música ou ambiente contínuo), o mapa não separa efeito de fundo: marque `continua` nos eventos e não conclua nada sobre efeito sonoro. Subir o limiar (`--limiar -35 --nome <nome>_alto`) às vezes isola os sons mais altos; trate o resultado como indício, não como prova.

Instante de cada quadro (PASSO é 1 s, ou 2 s no vídeo longo; COLS x LINS é a grade, 4x5 ou 5x6):

- `sNNNNN.png` (miniaturas): o arquivo de índice k mostra o instante (k − 1) × PASSO s. Ex.: `s00047.png` com PASSO 1 = 46 s = 00:00:46.
- `fNNN.png` (folhas): na folha de índice F, a miniatura da linha r e coluna c (contadas a partir de 1, da esquerda para a direita e de cima para baixo) é a de índice k = (F − 1) × COLS × LINS + (r − 1) × COLS + c. Ex. com grade 4x5 e PASSO 1: folha 3, linha 2, coluna 3 → k = 40 + 4 + 3 = 47 → 00:00:46. A primeira miniatura da folha F mostra (F − 1) × COLS × LINS × PASSO s: a folha 3 começa em 00:00:40.
- A última folha pode terminar com miniaturas pretas: são posições vazias, não quadros do vídeo.
- Mudanças de cena: cada `pts_time` impresso é um instante, em segundos.
- Converta segundos em hh:mm:ss com `python3 -c "import sys; s=int(float(sys.argv[1])); print(f'{s//3600:02d}:{s%3600//60:02d}:{s%60:02d}')" 750`.

## 3. Leia as folhas em ordem

Ler folhas custa bem menos do que ler quadros um a um: um vídeo de 2 minutos são 6 folhas. A folha serve para saber o que está na tela e quando muda; o texto se lê no quadro em resolução cheia.

1. Liste as folhas: `OUT="vygolint-out"; NOME="sessao1"; ls "$OUT/frames/$NOME/folhas"`.
2. Leia as folhas em ordem, de 2 a 4 por vez. Em cada uma, percorra as miniaturas na ordem de leitura e anote, com o instante, o que muda de uma para a outra: troca de tela, cartão de texto, início e fim de missão, feedback, cena sem interação.
3. Confira com os instantes de mudança de cena: cada um deve cair em uma mudança que você anotou. Se um instante cai entre duas miniaturas iguais, extraia aquele segundo (item 4) e veja o que aconteceu.
4. Para ler texto (créditos, balões, HUD, instruções, mensagens de feedback), extraia o quadro em resolução cheia no instante e leia dele. Não transcreva de miniatura quando alguma letra não está nítida:

```bash
VIDEO="gameplay/sessao1.mp4"; OUT="vygolint-out"; NOME="sessao1"
ffmpeg -y -ss 00:04:05 -i "$VIDEO" -frames:v 1 "$OUT/frames/$NOME/x000405.png"
```

5. Para achar o segundo exato de uma transição (início de missão, momento de um feedback) quando o passo é de 2 s, extraia um quadro por segundo do trecho: `VIDEO="gameplay/sessao1.mp4"; OUT="vygolint-out"; NOME="sessao1"; ffmpeg -y -ss 00:04:05 -t 10 -i "$VIDEO" -vf "fps=1" "$OUT/frames/$NOME/x0405_%02d.png"` (o quadro k mostra 00:04:05 + (k − 1) s).
6. Transcreva o texto da tela literalmente; não parafraseie mensagens de feedback.
7. Cruze cada evento com `trechos_com_som` do registro de áudio e anote o campo `som` (seção 4).
8. Plano B, se o harness não lê imagens grandes ou as folhas saem ilegíveis: extraia um quadro em resolução cheia a cada 5 s (10 s no vídeo longo) com `ffmpeg -y -i "$VIDEO" -vf "fps=1/5" "$OUT/frames/$NOME/t%05d.png"` e leia em lotes de 10 a 20; o quadro de índice k mostra (k − 1) × 5 s, com erro de até 2,5 s.

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

Áudio de cada evento, a partir de `registro_audio_<nome>.yaml`:

- `som`: `nao` quando o evento cai inteiro fora dos trechos com som; `inicia` quando um trecho com som começa no evento (até 1 s antes ou depois do `t` do evento); `continua` quando o som já tocava antes do evento e segue por ele. Só `inicia` indica som disparado pelo evento; `continua` costuma ser música ou ambiente de fundo.
- `fala`: o texto literal das falas da transcrição que caem no intervalo do evento, quando há transcrição (seção 7). Sem transcrição, não escreva `fala` e não suponha que uma legenda é narrada.
- Registre `som` em todo evento `feedback`, `texto` e `passivo`; nos demais, quando ajudar.

Medidas de tempo seguem o conteúdo, não o ritmo do jogador gravado (regra 14 de autoria do catálogo):

1. A duração de uma cena ou trecho passivo vai do início até a primeira oportunidade de avançar (botão "continuar", fim da animação), não até o momento em que o jogador avançou.
2. Se o jogador demorou a avançar, registre `fim` na primeira oportunidade e anote a espera na `descricao`.
3. Se o vídeo não mostra quando surgiu a opção de avançar, escreva isso na `descricao`; o critério usará código ou documentação como fallback.
4. O que o jogador não fez (área não visitada, missão não alcançada) não é evidência de que o jogo não permite: registre só o que aparece.

## 5. Formato de `registro_video.yaml`

```yaml
video: "gameplay/sessao1.mp4"
duracao: "00:12:31"
quadros: "vygolint-out/frames/sessao1"   # pasta raiz dos quadros (sec/, folhas/, x*.png), quando extraídos
audio: "vygolint-out/registro_audio_sessao1.yaml"   # registro de áudio, quando medido
eventos:
  - t: "00:00:40"
    fim: "00:03:50"
    tipo: missao            # missao | minijogo | feedback | texto | escolha | passivo | outro
    descricao: "Missão 1: coletar amostras; estado inicial visível, três ações disponíveis"
  - t: "00:03:12"
    tipo: feedback
    descricao: "erro na balança; texto: 'Some as massas antes de pesar'; indica a próxima ação"
    som: inicia             # nao | inicia | continua
    fala: "Some as massas antes de pesar."   # só com transcrição
```

1. Todo tempo no formato "hh:mm:ss", entre aspas.
2. `fim` só nos eventos com duração.
3. Confira o YAML do arquivo que você gravou (use o mesmo `ARQ` do nome do arquivo: `registro_video.yaml` ou `registro_video_<nome>.yaml`): `OUT="vygolint-out"; ARQ="registro_video.yaml"; python3 -c "import sys, yaml; yaml.safe_load(open(sys.argv[1], encoding='utf-8'))" "$OUT/$ARQ"`.
4. Nas provas de `avaliacao.yaml`, cite o arquivo de vídeo e o tempo do evento, nunca o arquivo de quadro nem a folha de contato. O que a prova afirma sobre som ou fala vem dos campos `som` e `fala` do evento.
5. Em `observacoes_gerais` (lista opcional de textos no topo do registro), diga se o áudio foi medido e se foi transcrito, e com qual reconhecedor.

## 6. Sem ffmpeg

1. Diga ao usuário que o ffmpeg não está instalado e que há duas saídas: instalar o ffmpeg ou escrever o registro à mão.
2. Para o registro à mão, mostre ao usuário o formato da seção 5 e a tabela de tipos da seção 4, e peça um `registro_video.yaml` por vídeo, com `quadros` omitido.
3. Ao receber o registro, confira o YAML e siga a avaliação usando-o como fonte `video`.
4. Se o usuário não puder fornecer nem ffmpeg nem registro, retire `video` de `contexto.fontes` e de `contexto.artefatos` em `avaliacao.yaml` e avise que os critérios que dependem só de vídeo ficarão `nao_avaliado`.

## 7. Transcreva a fala (opcional)

Só faz sentido quando `trechos_com_som` não está vazio. A transcrição depende de um reconhecedor de fala instalado na máquina.

1. Procure um reconhecedor: `command -v whisper whisper-cli mlx_whisper`.
2. Se nenhum caminho aparece, não instale nada por conta própria: siga sem transcrição (`transcricao: nao_disponivel` já está no registro), não preencha `fala` em nenhum evento e, na entrega, diga ao usuário que há som no vídeo que não foi transcrito e que um reconhecedor de fala (por exemplo, o `openai-whisper`) permite transcrevê-lo.
3. Com o `whisper` (pacote `openai-whisper`), extraia o áudio, transcreva e junte a transcrição ao registro de áudio. Troque `pt` pelo idioma das falas do jogo:

```bash
VIDEO="gameplay/sessao1.mp4"; OUT="vygolint-out"; NOME="sessao1"
mkdir -p "$OUT/frames/$NOME"
ffmpeg -y -i "$VIDEO" -vn -ac 1 -ar 16000 "$OUT/frames/$NOME/audio.wav"
whisper "$OUT/frames/$NOME/audio.wav" --language pt --model small --output_format json --output_dir "$OUT/frames/$NOME"
python3 "${VYGOLINT_ROOT}/scripts/vygolint_audio.py" "$VIDEO" --out "$OUT" --transcricao "$OUT/frames/$NOME/audio.json" --transcritor "openai-whisper small"
```

4. Outro reconhecedor serve, desde que gere um JSON em um destes formatos: `segments: [{start, end, text}]` com tempos em segundos (openai-whisper, faster-whisper, mlx-whisper) ou `transcription: [{offsets: {from, to}, text}]` com tempos em milissegundos (saída `-oj` do whisper.cpp). Passe o arquivo em `--transcricao` e o nome e o modelo em `--transcritor`.
5. O registro de áudio passa a ter `falas` (`t`, `fim`, `texto`). Copie para o campo `fala` de cada evento as falas que caem no intervalo dele.
6. Transcrição automática erra. Confira cada fala com o texto exibido na tela no mesmo instante: para nomes próprios e termos do jogo, vale a grafia da tela; se a fala diz algo que a tela não mostra, ou o contrário, registre os dois na `descricao` do evento. Trecho com som e sem fala reconhecida é música ou efeito: não invente texto.

Não rotule o jogo nas descrições: registre o que a tela mostra.
