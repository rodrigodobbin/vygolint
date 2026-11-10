# Changelog

Formato de [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/); versões seguem [SemVer](https://semver.org/lang/pt-BR/). A versão vale para o catálogo, os scripts, as skills e os manifestos de todos os harnesses (`tests/test_manifests.py` falha se divergirem).

## [0.4.0] — 2026-11-10

Autoria, licenças e fontes declaradas; a cláusula passa a nomear os critérios do vygolint. Primeira versão com licença.

### Adicionado

- `LICENSE` (Apache-2.0, código), `LICENSE-CONTENT.md` (CC BY 4.0, catálogo e docs), `NOTICE` (autoria, texto das diretrizes de Carvalho (2020) fora das licenças, modelo de níveis das WCAG, adaptadores do superpowers sob MIT) e `CITATION.cff`.
- README: seções "Autoria e fontes", "Como citar" e "Licença".
- Rodapé de autoria em `relatorio.md` e `relatorio.html`; linha de autoria dos critérios em `docs/catalogo.md`.

### Alterado

- Cláusula: "O resultado de uma avaliação vygolint expressa conformidade com os critérios do vygolint, derivados das diretrizes de Carvalho (2020), e não classifica o jogo como sociointeracionista." (antes: "conformidade com as diretrizes de Carvalho (2020)"). Vale para relatórios, skills, `docs/conformidade.md` e `vygolint_diff.py`, que agora lê a cláusula de `report.py`.
- Descrição dos manifestos apresenta o vygolint pelos 43 critérios e níveis A, AA e AAA; a fonte das diretrizes fica na descrição longa. Palavra-chave `wcag` removida; campo `license` acrescentado.
- Cabeçalho do `relatorio.html`: "Relatório vygolint".

## [0.3.0] — 2026-11-09

Fluxo de avaliação completo e conferível: esqueleto, inventário, vídeo com áudio, lint de provas, relatório HTML, retomada, comparação entre avaliações.

### Adicionado

- `relatorio.html` gerado junto com `relatorio.md` e `resultado.yaml`: página navegável sem servidor, com abas Resumo, Para o professor, Para quem desenvolve, Para a equipe e Todos os critérios, filtros por grau, nível e categoria e a tabela de fontes a entregar para decidir os critérios não avaliados (#4).
- `scripts/vygolint_scaffold.py`: esqueleto de `avaliacao.yaml` (cabeçalho e as 43 entradas com comentário por critério, `PREENCHER` onde falta julgar) e de `inventario.md` (seções fixas e uma linha por arquivo de documentação e de vídeo do escopo) (#5, #7).
- Lint de provas em `vygolint_report.py`: confere que cada prova aponta um lugar que existe (`arquivo:linha` dentro do arquivo, `documento p. N`, `vídeo hh:mm:ss` dentro da duração, medida com `ffprobe` quando há), que o arquivo citado está nos artefatos da fonte e que o escopo declarado foi coberto (vídeo com registro ou prova; documento com prova ou classificado em `inventario.md`; prova não cita documento classificado "não conta"). Avisos não mudam grau; `--strict` os trata como erro (#5, #7).
- Artefatos como pastas em `contexto.artefatos`: uma pasta põe no escopo tudo o que está dentro dela. `contexto.fontes_externas` para fonte usada que não está na máquina (#5).
- `scripts/vygolint_audio.py`: mede a faixa de áudio do vídeo (`volumedetect`, `silencedetect`) e gera `registro_audio_<nome>.yaml` com os trechos com som; com a transcrição de um reconhecedor de fala (`openai-whisper`, `whisper.cpp`), as falas ajustadas aos trechos com som (#8).
- `scripts/vygolint_juntar.py` e a seção "Passo 3 em partes, com subagentes" de `vygolint-avaliar`: critérios graduados em partes (um `.yaml` por categoria ou por subagente) gravados no esqueleto com conferência de ids; experimento registrado em `docs/experimentos/2026-11-06-subagente-por-categoria.md` (#9).
- `scripts/vygolint_diff.py`: compara dois `resultado.yaml` (nível, contagem por grau, critérios que mudaram de grau classificados como melhora, piora, passou/deixou de ser avaliado, entrou/saiu do contexto; notas alteradas, graus sobrescritos pelo script e ids presentes em um só arquivo à parte) (#11).
- `vygolint_report.py --status`: quantos critérios estão preenchidos, por categoria, os `PREENCHER` que sobraram e o próximo critério a graduar; não valida nem gera nada (#12).
- Hook de início de sessão injeta `VYGOLINT_PYTHON` (interpretador com PyYAML: `python3`, `.venv` do plugin, `python`), `VYGOLINT_FFMPEG` e `VYGOLINT_TRANSCRITOR`; as skills usam `"${VYGOLINT_PYTHON}"` em todo comando e não instalam nada por conta própria (#10).

### Alterado

- `vygolint-video`: folhas de contato (um quadro por segundo, mosaico 4x5) lidas como imagem em vez de quadros soltos; cortes de cena listados com `select='gt(scene,0.4)',showinfo` sem `-vsync` (rejeitado pelo ffmpeg 9); passo de áudio com `som: nao|inicia|continua` e `fala` por evento; seção de transcrição; variante para vídeo longo mantida (#6, #8).
- `vygolint-criterio`: evidência de áudio (`som`/`fala`) e regra de fronteira: sem evidência o grau é `nao_avaliado`, salvo quando o próprio critério diz o grau para a falta de evidência; cobertura total da gravação e desempate não são exceções (#8, #9).
- `vygolint-avaliar`: começa pelo esqueleto; inventário a partir do esqueleto; tabela de avisos com a correção de cada um; retomada por `--status`; a execução final da entrega é com `--strict`, e aviso sem correção possível é explicado ao usuário junto com o relatório (#5, #7, #12).
- `docs/conformidade.md` §6 descreve todos os arquivos e scripts da avaliação.

## [0.2.0] — 2026-11-04

- Skills portáveis `using-vygolint`, `vygolint-avaliar`, `vygolint-criterio` e `vygolint-video`.
- `scripts/vygolint_report.py`: valida `avaliacao.yaml` contra o catálogo, aplica dependências e aplicabilidade, calcula nível e escreve `relatorio.md` e `resultado.yaml`.
- Campo `recomendacao` por critério (vias documentação, design e código) no catálogo.
- Manifestos por harness: Claude Code, Codex, Cursor, Kimi, OpenCode, Pi, Antigravity, Gemini CLI, Factory Droid, GitHub Copilot CLI (#3).

## [0.1.0] — 2026-11-03

Sem tag; corresponde ao commit `98b78bb`.

- Catálogo: 40 diretrizes de Carvalho (2020) em 43 critérios com nível A, AA ou AAA derivado de essencialidade e viabilidade; glossário `definicoes.yaml`; 12 categorias; validação cruzada e `docs/catalogo.md` e `docs/catalogo.tex` gerados por `scripts/build_catalog.py`.

[0.4.0]: https://github.com/rodrigodobbin/vygolint/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/rodrigodobbin/vygolint/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/rodrigodobbin/vygolint/compare/98b78bb...v0.2.0
[0.1.0]: https://github.com/rodrigodobbin/vygolint/commits/98b78bb
