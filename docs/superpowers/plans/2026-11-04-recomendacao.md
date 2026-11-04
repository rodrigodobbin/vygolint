# Campo `recomendacao` por critério — Plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Cada um dos 43 critérios do catálogo ganha um campo obrigatório `recomendacao` (mapa `documentacao`/`design`/`codigo`, texto ou `null`), validado pelo build, lintado contra o glossário e impresso em `docs/catalogo.md`.

**Architecture:** `validate.py` ganha o bloco de validação do campo no mesmo padrão de `evidencia` e `textos_do_criterio` passa a incluir as vias, de modo que o lint do glossário cobre a recomendação sem código novo. `render.py` imprime um bloco `**Recomendações.**` entre `**Escala.**` e `**Depende de.**`. O conteúdo é escrito em quatro lotes por categoria; enquanto os lotes não terminam, o campo fica em `opcionais` do esquema para que o build do catálogo real continue verde a cada commit; a última tarefa de código o move para `obrigatorios`.

**Tech Stack:** Python 3.12+, PyYAML, `unittest`, GitHub Actions. Sem dependências novas.

Spec: `docs/superpowers/specs/2026-11-04-recomendacao-design.md`.

## Global Constraints

- Branch `recomendacao`, criado a partir de `main` (já existe). PR contra `main`.
- Conteúdo do catálogo e docs em português. Código, nomes de função e mensagens de commit em inglês. Todo commit termina com `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
- Ambiente: `cd /Users/dobbin/projects/personal/vygolint && source .venv/bin/activate`.
- Testes: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v`. Execução focada: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_<modulo>.py -v`. Build: `python3 scripts/build_catalog.py` deve terminar com `OK: 40 diretrizes, 43 critérios`.
- `docs/catalogo.md` e `docs/catalogo.tex` são gerados; nunca editar à mão. Regenerar e commitar sempre que render ou catálogo mudarem.
- Nenhum campo existente de critério (enunciado, nível, justificativa, evidência, escala, depende_de) muda de texto. A única mudança permitida fora de `recomendacao` é acrescentar chaves a `definicoes.glossario` quando a recomendação usa um gatilho do glossário.
- Os 80 testes existentes continuam verdes. A fixture `diretriz_valida()` muda (ganha `recomendacao`) e o teste `test_unknown_criterio_field_is_rejected` continua valendo porque `definicao` segue desconhecido.
- `.superpowers/sdd/authoring-rules.md` não é versionado (está em `.git/info/exclude`); as regras novas entram nele e também na spec (já estão na seção 6).

## File Structure

```
catalog/
  schema.yaml                      # + recomendacao em opcionais (Task 1) e depois em obrigatorios (Task 8); + recomendacao.vias; + campos_lint recomendacao.*
  D01.yaml … D40.yaml              # + recomendacao em cada critério (Tasks 3 a 6)
scripts/vygolint_catalog/
  validate.py                      # + vias em textos_do_criterio; + bloco recomendacao em _validate_criterio
  render.py                        # + bloco Recomendações
tests/
  helpers.py                       # fixture com recomendacao
  test_validate.py                 # + RecomendacaoTest
  test_render.py                   # + testes do bloco
docs/
  catalogo.md                      # regenerado
  conformidade.md                  # seção 5
  superpowers/specs/2026-11-03-catalogo-conformidade-design.md   # seções 5 e 7
README.md
.superpowers/sdd/authoring-rules.md  # regras 19 a 24 (não versionado)
```

---

### Task 1: Esquema, validação e lint do campo `recomendacao`

**Files:**
- Modify: `catalog/schema.yaml`
- Modify: `scripts/vygolint_catalog/validate.py` (funções `textos_do_criterio` e `_validate_criterio`)
- Modify: `tests/helpers.py` (`_DIRETRIZ`)
- Test: `tests/test_validate.py`

**Interfaces:**
- Produces: `schema["criterio"]["recomendacao"]["vias"] == ["documentacao", "design", "codigo"]`; `textos_do_criterio(c)` devolve, além dos campos atuais, `("recomendacao.documentacao", texto)`, `("recomendacao.design", texto)`, `("recomendacao.codigo", texto)` para cada via com texto; `validate_diretriz` devolve erros com prefixo `Dnn/Dnn.k` para campo malformado.

- [x] **Step 1: Fixture com `recomendacao`**

Em `tests/helpers.py`, dentro de `_DIRETRIZ["criterios"][0]`, entre `"escala"` e `"depende_de"`:

```python
            "recomendacao": {
                "documentacao": "Registrar no documento de design a tabela de erros com a mensagem exibida em cada um e a próxima ação que ela indica",
                "design": "Definir, para cada ação incorreta prevista, a próxima ação que a mensagem indica ao jogador",
                "codigo": "Trocar, em cada manipulador de erro, a mensagem que só sinaliza o erro por uma que indica a próxima ação",
            },
```

(Não usar "GDD" nem "documento equivalente" na fixture: são gatilhos do glossário e a fixture não lista `definicoes`.)

- [x] **Step 2: Testes que falham**

Acrescentar ao fim de `tests/test_validate.py`:

```python
class RecomendacaoTest(unittest.TestCase):
    def setUp(self):
        self.schema = schema_valido()
        self.categorias = categorias_validas()
        self.g = _glossario()

    def check(self, d):
        return validate_diretriz(d, self.schema, self.categorias, self.g)

    def test_schema_lists_vias(self):
        self.assertEqual(self.schema["criterio"]["recomendacao"]["vias"], ["documentacao", "design", "codigo"])
        self.assertIn("recomendacao.*", self.schema["criterio"]["definicoes"]["campos_lint"])

    def test_valid_fixture_passes(self):
        self.assertEqual(self.check(diretriz_valida()), [])

    def test_must_be_map(self):
        d = diretriz_valida()
        d["criterios"][0]["recomendacao"] = "texto"
        self.assertTrue(any("D17.1" in e and "recomendacao deve ser mapa" in e for e in self.check(d)))

    def test_each_via_required_null_allowed(self):
        d = diretriz_valida()
        del d["criterios"][0]["recomendacao"]["design"]
        self.assertTrue(any("recomendacao.design ausente" in e for e in self.check(d)))
        d = diretriz_valida()
        d["criterios"][0]["recomendacao"]["design"] = None
        self.assertEqual(self.check(d), [])

    def test_via_must_be_text_or_null(self):
        d = diretriz_valida()
        d["criterios"][0]["recomendacao"]["codigo"] = ""
        self.assertTrue(any("recomendacao.codigo" in e and "texto não vazio ou null" in e for e in self.check(d)))
        d = diretriz_valida()
        d["criterios"][0]["recomendacao"]["codigo"] = ["x"]
        self.assertTrue(any("recomendacao.codigo" in e for e in self.check(d)))

    def test_unknown_via(self):
        d = diretriz_valida()
        d["criterios"][0]["recomendacao"]["video"] = "x"
        self.assertTrue(any("recomendacao" in e and "desconhecidas" in e and "video" in e for e in self.check(d)))

    def test_at_least_one_via(self):
        d = diretriz_valida()
        for via in ("documentacao", "design", "codigo"):
            d["criterios"][0]["recomendacao"][via] = None
        self.assertTrue(any("recomendacao precisa de ao menos uma via não nula" in e for e in self.check(d)))

    def test_textos_do_criterio_includes_vias_in_order(self):
        from vygolint_catalog.validate import textos_do_criterio
        c = diretriz_valida()["criterios"][0]
        c["recomendacao"]["design"] = None
        campos = [campo for campo, _ in textos_do_criterio(c)]
        self.assertEqual(
            [x for x in campos if x.startswith("recomendacao.")],
            ["recomendacao.documentacao", "recomendacao.codigo"],
        )
        self.assertLess(campos.index("escala.nao_atendido"), campos.index("recomendacao.documentacao"))

    def test_gatilho_in_recomendacao_requires_key(self):
        d = diretriz_valida()
        d["criterios"][0]["recomendacao"]["design"] = "Acrescentar a cada missão uma mensagem orientadora"
        errors = self.check(d)
        self.assertTrue(any('"missão"' in e and "missao" in e for e in errors), errors)
        d["criterios"][0]["definicoes"] = {"glossario": ["missao"]}
        self.assertEqual(self.check(d), [])

    def test_inline_definition_in_recomendacao_is_error(self):
        d = diretriz_valida()
        d["criterios"][0]["recomendacao"]["codigo"] += ". Definição: manipulador é a função chamada no erro"
        self.assertTrue(any("recomendacao.codigo" in e and "Definição" in e for e in self.check(d)))
```

- [x] **Step 3: Rodar e ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_validate.py -v 2>&1 | tail -20`
Expected: `RecomendacaoTest` falha (`KeyError: 'recomendacao'` em `test_schema_lists_vias`; "campo desconhecido: recomendacao" nos demais, porque a fixture agora traz o campo e o esquema não o conhece).

- [x] **Step 4: Esquema**

`catalog/schema.yaml`, bloco `criterio`, passa a ser:

```yaml
criterio:
  obrigatorios: [id, nivel, enunciado, nivel_justificativa, evidencia, escala, depende_de]
  id_padrao: '^D(0[1-9]|[1-3][0-9]|40)\.[1-9]$'
  nivel: [A, AA, AAA]
  essencialidade: [alta, media, baixa]
  viabilidade: [alta, media, baixa]
  fontes_evidencia: [codigo, documentacao, video]
  escala: [atendido, parcial, nao_atendido]
  opcionais: [definicoes, recomendacao]   # recomendacao passa a obrigatorios quando os 43 critérios o tiverem (plano, Task 8)
  recomendacao:
    vias: [documentacao, design, codigo]   # cada via: texto não vazio ou null; ao menos uma não nula
  definicoes:
    chaves: [glossario, locais, termos_comuns]   # glossario: lista de chaves de definicoes.yaml; locais: {termo: texto}; termos_comuns: {gatilho: justificativa}
    # campos_lint: documentation only (the validator hardcodes the fields in textos_do_criterio)
    campos_lint: [enunciado, evidencia.*.procedimento, evidencia.*.indicadores, escala.*, recomendacao.*]
```

- [x] **Step 5: `textos_do_criterio`**

Em `scripts/vygolint_catalog/validate.py`, acrescentar antes do `return out` de `textos_do_criterio`:

```python
    rec = c.get("recomendacao") if isinstance(c.get("recomendacao"), dict) else {}
    for via in ("documentacao", "design", "codigo"):
        if _is_text(rec.get(via)):
            out.append((f"recomendacao.{via}", rec[via]))
```

Atualizar a docstring: `"""Return [(campo, texto)] for every text field the lint covers (enunciado, evidencia, escala, recomendacao; not nivel_justificativa)."""`

- [x] **Step 6: Validação do campo**

Em `_validate_criterio`, depois do bloco de `escala` e antes do bloco de `depende_de`:

```python
    rec = c.get("recomendacao")
    if "recomendacao" in c:
        if not isinstance(rec, dict):
            errors.append(f"{prefix}: recomendacao deve ser mapa")
        else:
            vias = cs["recomendacao"]["vias"]
            presentes = 0
            for via in vias:
                if via not in rec:
                    errors.append(f"{prefix}: recomendacao.{via} ausente (use null se a via não leva a atendido)")
                    continue
                valor = rec[via]
                if valor is None:
                    continue
                if not _is_text(valor):
                    errors.append(f"{prefix}: recomendacao.{via} deve ser texto não vazio ou null")
                    continue
                presentes += 1
            extras = set(rec) - set(vias)
            if extras:
                errors.append(f"{prefix}: recomendacao com chaves desconhecidas: {sorted(extras)}")
            if presentes == 0 and not extras:
                errors.append(f"{prefix}: recomendacao precisa de ao menos uma via não nula")
```

- [x] **Step 7: Rodar e ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v 2>&1 | tail -5`
Expected: `Ran 90 tests` … `OK` (80 existentes + 10 novos).

- [x] **Step 8: Build do catálogo real continua verde**

Run: `python3 scripts/build_catalog.py && git diff --stat -- docs/`
Expected: `OK: 40 diretrizes, 43 critérios` e nenhum diff em `docs/` (o campo é opcional e nenhum critério o tem ainda).

- [x] **Step 9: Commit**

```bash
git add catalog/schema.yaml scripts/vygolint_catalog/validate.py tests/helpers.py tests/test_validate.py
git commit -m "feat(schema): recomendacao field per criterion, validated and linted" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 2: Bloco `**Recomendações.**` no Markdown

**Files:**
- Modify: `scripts/vygolint_catalog/render.py` (`render_markdown`)
- Test: `tests/test_render.py`

**Interfaces:**
- Consumes: `c["recomendacao"]` como validado na Task 1 (mapa com as três vias; pode estar ausente enquanto o campo é opcional).
- Produces: em `docs/catalogo.md`, por critério, o bloco abaixo entre `**Escala.**` e `**Depende de.**`.

- [x] **Step 1: Testes que falham**

Acrescentar à classe `RenderMarkdownTest` em `tests/test_render.py`:

```python
    def test_recomendacoes_block_between_escala_and_depende_de(self):
        out = render_markdown([diretriz_valida()], self.cats)
        bloco = (
            "- Não atendido: Feedback só sinaliza acerto/erro ou inexiste\n\n"
            "**Recomendações.**\n"
            "- Documentação: Registrar no documento de design a tabela de erros com a mensagem exibida em cada um e a próxima ação que ela indica\n"
            "- Design: Definir, para cada ação incorreta prevista, a próxima ação que a mensagem indica ao jogador\n"
            "- Código: Trocar, em cada manipulador de erro, a mensagem que só sinaliza o erro por uma que indica a próxima ação\n\n"
            "**Depende de.** —"
        )
        self.assertIn(bloco, out)

    def test_recomendacao_null_via_renders_nao_se_aplica(self):
        d = diretriz_valida()
        d["criterios"][0]["recomendacao"]["codigo"] = None
        out = render_markdown([d], self.cats)
        self.assertIn("- Código: não se aplica\n\n**Depende de.**", out)

    def test_no_recomendacoes_block_when_field_absent(self):
        d = diretriz_valida()
        del d["criterios"][0]["recomendacao"]
        out = render_markdown([d], self.cats)
        self.assertNotIn("**Recomendações.**", out)
        self.assertIn("- Não atendido: Feedback só sinaliza acerto/erro ou inexiste\n\n**Depende de.** —", out)
```

- [x] **Step 2: Rodar e ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_render.py -v 2>&1 | tail -8`
Expected: os dois primeiros testes novos falham (`AssertionError`); o terceiro passa.

- [x] **Step 3: Implementação**

Em `scripts/vygolint_catalog/render.py`, depois de `_GRAUS`:

```python
_VIAS = (("documentacao", "Documentação"), ("design", "Design"), ("codigo", "Código"))
```

Nova função, depois de `_depende_de`:

```python
def _bloco_recomendacoes(c):
    rec = c.get("recomendacao")
    if not rec:
        return []
    linhas = ["", "**Recomendações.**"]
    for chave, nome in _VIAS:
        texto = rec.get(chave)
        linhas.append(f"- {nome}: {texto if texto else 'não se aplica'}")
    return linhas
```

Em `render_markdown`, trocar:

```python
            linhas += ["", f"**Depende de.** {_depende_de(c)}", ""]
```

por:

```python
            linhas += _bloco_recomendacoes(c)
            linhas += ["", f"**Depende de.** {_depende_de(c)}", ""]
```

- [x] **Step 4: Rodar e ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v 2>&1 | tail -5`
Expected: `Ran 93 tests` … `OK`.

- [x] **Step 5: Build e diff**

Run: `python3 scripts/build_catalog.py && git diff --stat -- docs/`
Expected: `OK: 40 diretrizes, 43 critérios`; nenhum diff (nenhum critério tem o campo ainda).

- [x] **Step 6: Commit**

```bash
git add scripts/vygolint_catalog/render.py tests/test_render.py
git commit -m "feat(render): Recomendações block per criterion in catalogo.md" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Tasks 3 a 6: Escrita das recomendações em lotes

Cada lote segue o mesmo procedimento. É trabalho de autoria: o executor lê cada `catalog/Dnn.yaml` do lote por inteiro (enunciado, indicadores, escala, definições) e escreve o campo. O revisor compara contra as regras abaixo.

**Regras de autoria para recomendações** (regras 19 a 24 de `.superpowers/sdd/authoring-rules.md`; a Task 3, Step 0, as grava lá):

19. A recomendação deriva dos indicadores e da escala do critério: cada frase aponta para um indicador que passaria a ser satisfeito. Não cria exigência que o enunciado não faz.
20. Acionável por quem recebe: `documentacao` pelo autor do GDD ou documento equivalente (registrar o que o jogo já faz ou passa a fazer, para gerar a evidência documental); `design` por quem projeta o jogo (mudar regra, conteúdo ou estrutura no projeto); `codigo` pelo desenvolvedor (mudar a implementação). O texto começa com verbo no infinitivo.
21. Uma frase por ação. Mais de uma ação na mesma via: frases separadas por ponto, na ordem em que seriam feitas.
22. Sem adjetivos de valor ("bom", "adequado", "claro") e sem advérbios de intensidade.
23. Sem citar jogo, produto ou motor específico; sem citar Expedição Antártica.
24. `null` só quando a via não leva o critério a `atendido`. Se o critério tem `evidencia.codigo: null`, `codigo` da recomendação costuma ser `null`, mas não é regra: a via pode existir (ex.: mudar o código gera o comportamento que o vídeo mostra).

Regras de forma:

- O campo entra em cada critério **depois de `escala` e antes de `depende_de`**, com a indentação do arquivo (4 espaços para as chaves do critério, 6 para as vias), aspas duplas como nos demais campos, ordem fixa `documentacao`, `design`, `codigo`.
- Um texto por via, válido tanto para `parcial` quanto para `nao_atendido` (não distinguir os dois estados; a skill contextualiza).
- Se o texto usa um gatilho do glossário (missão, missões, minijogo, desafio, cenário, caminho obrigatório, caminho da missão, situação-problema, GDD, documento equivalente, objetivo de aprendizagem, objetivos de aprendizagem, sessão de jogo), a chave correspondente precisa estar em `definicoes.glossario` do critério. Preferir reutilizar os termos que o critério já usa; quando um gatilho novo for mesmo necessário, acrescentar a chave ao final da lista `glossario` (única mudança permitida fora de `recomendacao`). "documentação" sem "GDD" não é gatilho.
- Nenhum outro campo do critério muda.
- Não repetir texto do glossário na forma "termo é …"; não escrever "Definição:".

**Procedimento de cada lote:**

- [x] **Step 1:** Para cada critério do lote, acrescentar `recomendacao` com as três vias (texto ou `null`).
- [x] **Step 2:** Run: `python3 scripts/build_catalog.py`. Expected: `OK: 40 diretrizes, 43 critérios`. Erros de lint do glossário apontam `Dnn/Dnn.k: texto usa "<gatilho>" mas definicoes.glossario não lista "<chave>"`: acrescentar a chave ou reescrever sem o gatilho.
- [x] **Step 3:** Ler a seção de cada critério do lote em `docs/catalogo.md` e checar: bloco `**Recomendações.**` presente, três linhas, cada frase começa com verbo no infinitivo, nenhuma frase cria exigência fora do enunciado.
- [x] **Step 4:** Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests 2>&1 | tail -3` e `git diff --stat -- docs/catalogo.tex`. Expected: `OK`; `catalogo.tex` sem diff (só `catalogo.md` muda).
- [x] **Step 5:** Commit: `git add catalog/ docs/catalogo.md && git commit -m "feat(catalog): recomendacao for <categorias> (<faixa>)" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"`

**Exemplo de referência (D17.1, lote B), já no formato final:**

```yaml
    recomendacao:
      documentacao: "Registrar no GDD ou documento equivalente a tabela de ações incorretas previstas com a mensagem exibida em cada uma e a próxima ação que ela indica"
      design: "Definir, para cada ação incorreta prevista, a próxima ação que a mensagem indica ao jogador"
      codigo: "Trocar, em cada manipulador de erro, a mensagem que só sinaliza o erro por uma que indica a próxima ação"
```

(D17.1 precisa listar `documentacao_equivalente` em `definicoes.glossario` se ainda não lista.)

#### Task 3: Lote A — Interação (D01 a D15, 17 critérios)

- [x] **Step 0 (só nesta task):** Acrescentar as regras 19 a 24 acima ao fim de `.superpowers/sdd/authoring-rules.md`, numeradas, precedidas da linha `Regras para o campo recomendacao (2026-11-04):`. Arquivo não versionado; nada a commitar.
- Steps 1 a 5 do procedimento. Mensagem de commit: `feat(catalog): recomendacao for interacao (D01-D15)`.

#### Task 4: Lote B — Mediação (D16 a D23, 9 critérios: D16.1 a D21.1, D22.1, D22.2, D23.1)

- Steps 1 a 5. Mensagem: `feat(catalog): recomendacao for mediacao (D16-D23)`.
- Atenção: D22.1 só se atende por documentação (`evidencia.codigo` e `evidencia.video` nulos); `codigo: null` é esperado e `design` descreve o que prever no projeto (momentos de mediação por desafio).

#### Task 5: Lote C — Autonomia, socialização e lúdico (D24 a D29, 6 critérios)

- Steps 1 a 5. Mensagem: `feat(catalog): recomendacao for autonomia, socializacao, ludico (D24-D29)`.

#### Task 6: Lote D — Realismo, personalização, organização, resolução de problemas, linguagem, atenção, aprendizado (D30 a D40, 11 critérios)

- Steps 1 a 5. Mensagem: `feat(catalog): recomendacao for realismo to aprendizado (D30-D40)`.

---

### Task 7: Tornar `recomendacao` obrigatório

**Files:**
- Modify: `catalog/schema.yaml`
- Test: `tests/test_validate.py`, `tests/test_render.py`

- [x] **Step 1: Teste que falha**

Acrescentar a `RecomendacaoTest` em `tests/test_validate.py`:

```python
    def test_field_is_required(self):
        d = diretriz_valida()
        del d["criterios"][0]["recomendacao"]
        self.assertTrue(any("D17.1" in e and "campo obrigatório ausente: recomendacao" in e for e in self.check(d)))
        self.assertIn("recomendacao", self.schema["criterio"]["obrigatorios"])
        self.assertNotIn("recomendacao", self.schema["criterio"].get("opcionais", []))
```

- [x] **Step 2: Rodar e ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_validate.py -v 2>&1 | tail -6`
Expected: `test_field_is_required` FAIL.

- [x] **Step 3: Esquema**

Em `catalog/schema.yaml`:

```yaml
  obrigatorios: [id, nivel, enunciado, nivel_justificativa, evidencia, escala, recomendacao, depende_de]
  ...
  opcionais: [definicoes]
```

(remover o comentário "passa a obrigatorios quando…").

- [x] **Step 4: Render sem o campo deixa de ser caso válido**

Em `tests/test_render.py`, apagar `test_no_recomendacoes_block_when_field_absent` (o campo é obrigatório; o render ainda tolera ausência por defesa, mas o caso não é mais contrato). Em `render.py`, manter `_bloco_recomendacoes` como está.

- [x] **Step 5: Rodar tudo**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v 2>&1 | tail -4 && python3 scripts/build_catalog.py && git diff --exit-code -- docs/catalogo.md docs/catalogo.tex && grep -c '^\*\*Recomendações\.\*\*$' docs/catalogo.md`
Expected: `Ran 93 tests … OK`; `OK: 40 diretrizes, 43 critérios`; nenhum diff; `43`.

- [x] **Step 6: Commit**

```bash
git add catalog/schema.yaml tests/test_validate.py tests/test_render.py
git commit -m "feat(schema): recomendacao is required in every criterion" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 8: Documentação

**Files:**
- Modify: `docs/superpowers/specs/2026-11-03-catalogo-conformidade-design.md` (seções 5 e 7)
- Modify: `docs/conformidade.md` (seção 5)
- Modify: `README.md`

- [x] **Step 1: Spec do catálogo, seção 5**

No exemplo YAML, entre o bloco `escala:` e `depende_de: []`, inserir:

```yaml
    recomendacao:              # obrigatório; o que fazer para chegar a atendido, por via; null quando a via não serve
      documentacao: "Registrar no GDD ou documento equivalente a tabela de ações incorretas previstas com a mensagem exibida em cada uma e a próxima ação que ela indica"
      design: "Definir, para cada ação incorreta prevista, a próxima ação que a mensagem indica ao jogador"
      codigo: "Trocar, em cada manipulador de erro, a mensagem que só sinaliza o erro por uma que indica a próxima ação"
```

Na lista "Regras do esquema", depois do item sobre `depende_de`, acrescentar:

```markdown
- `recomendacao` é obrigatório: mapa com exatamente as chaves `documentacao`, `design` e `codigo`, cada uma texto não vazio ou `null`, ao menos uma não nula. Cada texto diz o que fazer para sair de `nao_atendido` ou `parcial` para `atendido`, em termos dos indicadores e da escala do critério, sem distinguir os dois estados e sem criar exigência nova. `documentacao` = registrar no GDD ou documento equivalente o que o jogo faz; `design` = mudar regra, conteúdo ou estrutura do jogo no projeto; `codigo` = mudar a implementação. `null` só quando a via não leva o critério a `atendido`. Regras de autoria: `docs/superpowers/specs/2026-11-04-recomendacao-design.md`, seção 6.
```

No item "Lint:", acrescentar ao final: `O lint cobre também as três vias de `recomendacao`.`

No item "O renderizador imprime…", acrescentar: `e um bloco `**Recomendações.**` (uma linha por via, "não se aplica" quando `null`) depois da escala e antes de `**Depende de.**`.`

- [x] **Step 2: Spec do catálogo, seção 7**

Trocar as duas linhas da lista "Relatório":

```markdown
- bloqueios: critérios que impedem o próximo nível, com recomendação
- parciais: o que falta para pleno
```

por:

```markdown
- bloqueios: critérios que impedem o próximo nível, com a `recomendacao` do critério na via que cabe à evidência disponível (código avaliado: `codigo`; só documentação: `documentacao` e `design`)
- parciais: o que falta para pleno, com a `recomendacao` do critério contextualizada pelos itens que a avaliação encontrou fora do estado atendido
```

Atualizar a linha `Status:` no topo: acrescentar `; campo recomendacao (2026-11-04)`.

- [x] **Step 3: `docs/conformidade.md`, seção 5**

Trocar os itens 5 e 6 por:

```markdown
5. bloqueios: critérios que impedem o próximo nível, cada um com a `recomendacao` do catálogo
   na via que cabe à evidência disponível (código avaliado: `codigo`; só documentação:
   `documentacao` e `design`);
6. parciais: o que falta para pleno, com a `recomendacao` do critério contextualizada pelos
   itens que a avaliação encontrou fora do estado atendido;
```

Depois da seção 2a, acrescentar:

```markdown
## 2b. Recomendações

Todo critério traz, no catálogo, uma recomendação por via (`documentacao`, `design`,
`codigo`): o que fazer para sair de não atendido ou parcial para atendido, nos termos dos
seus indicadores. A via é `null` quando não leva o critério a atendido. O relatório
reproduz o texto do catálogo e o contextualiza com os itens encontrados; não inventa
recomendação nova.
```

- [x] **Step 4: README**

Na tabela "O que há aqui", linha de `catalog/D01.yaml … D40.yaml`, trocar o conteúdo por: `uma diretriz por arquivo: texto literal, critérios, níveis, evidências, escalas, recomendações por via (documentação, design, código)`.

No parágrafo "Desenvolvimento", depois de "estão na seção 5 do spec.", acrescentar: `O lint cobre também o campo `recomendacao` (três vias, ao menos uma não nula; ver `docs/superpowers/specs/2026-11-04-recomendacao-design.md`).`

Na lista "Documentos de projeto", acrescentar:

```markdown
- Spec do campo `recomendacao`: `docs/superpowers/specs/2026-11-04-recomendacao-design.md`
- Plano do campo `recomendacao`: `docs/superpowers/plans/2026-11-04-recomendacao.md`
```

- [x] **Step 5: Spec desta feature**

Em `docs/superpowers/specs/2026-11-04-recomendacao-design.md`, linha `Status:`, trocar por `Status: implementado (2026-11-04)`.

- [x] **Step 6: Verificar e commitar**

Run: `python3 scripts/build_catalog.py && git diff --exit-code -- docs/catalogo.md docs/catalogo.tex`
Expected: OK e sem diff.

```bash
git add docs/superpowers/specs/2026-11-03-catalogo-conformidade-design.md docs/superpowers/specs/2026-11-04-recomendacao-design.md docs/conformidade.md README.md docs/superpowers/plans/2026-11-04-recomendacao.md
git commit -m "docs: recomendacao field in spec, conformidade rules and README" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 9: Verificação final e PR

- [x] **Step 1:** Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v 2>&1 | tail -4 && python3 scripts/build_catalog.py && git diff --exit-code -- docs/catalogo.md docs/catalogo.tex && git status --short`
Expected: `OK`; `OK: 40 diretrizes, 43 critérios`; sem diff; árvore limpa.
- [x] **Step 2:** Run: `grep -c '^\*\*Recomendações\.\*\*$' docs/catalogo.md` → `43`. Run: `grep -n 'Expedição\|Antártica' catalog/*.yaml` → nada.
- [x] **Step 3:** `git push -u origin recomendacao` e `gh pr create --base main --title "Per-criterion recomendacao field" --body-file <corpo>`; corpo em português com: o que muda (esquema, lint, render, 43 recomendações, docs), como validar (comandos), e a cláusula de Carvalho (o resultado expressa conformidade com as diretrizes, não rotula o jogo). Terminar com `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- [x] **Step 4:** Esperar CI verde (`gh pr checks --watch`).
