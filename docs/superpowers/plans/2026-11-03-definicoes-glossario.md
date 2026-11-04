# Glossário de definições do catálogo — Plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fazer cada definição compartilhada do catálogo existir uma vez só (`catalog/definicoes.yaml`), referenciada por critério, impressa uma vez por critério e verificada por lint, sem mudar o significado de nenhum critério sem decisão explícita do usuário.

**Architecture:** Um glossário YAML (`catalog/definicoes.yaml`) com entradas `chave`/`termo`/`gatilhos`/`texto`/`ancora`. Cada critério ganha um campo opcional `definicoes` com `glossario` (lista de chaves), `locais` (mapa termo → texto, definições só daquele critério) e `termos_comuns` (mapa gatilho → justificativa, para quando a palavra é usada no sentido corrente). `validate.py` resolve chaves, proíbe definições inline e exige a chave sempre que um gatilho aparece no texto do critério. `render.py` imprime um bloco `**Definições.**` antes do enunciado. Dois scripts de uso único fazem a migração mecânica dos 40 arquivos e verificam, cláusula a cláusula, que o único conteúdo que mudou está na lista de diferenças aceitas.

**Tech Stack:** Python 3.12+, PyYAML, `unittest`, GitHub Actions. Sem dependências novas.

Spec: `docs/superpowers/specs/2026-11-03-catalogo-conformidade-design.md` (seção 5 será atualizada na Task 9). Divergências: `docs/superpowers/specs/2026-11-03-definicoes-divergencias.md` (Task 8).

## Global Constraints

- Branch `definicoes-glossario`, criado a partir de `main`. PR contra `main`.
- Conteúdo do catálogo e docs em português. Código, nomes de função e mensagens de commit em inglês. Todo commit termina com `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
- Ambiente: `cd /Users/dobbin/projects/personal/vygolint && source .venv/bin/activate`.
- Testes: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v`. Execução focada: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_<modulo>.py -v`. Build: `python3 scripts/build_catalog.py` deve terminar com `OK: 40 diretrizes, 43 critérios`.
- `docs/catalogo.md` e `docs/catalogo.tex` são gerados; nunca editar à mão. Regenerar e commitar sempre que render ou catálogo mudarem.
- Nenhum texto de critério muda de significado sem decisão explícita. O que é redação equivalente é normalizado e listado; o que muda significado fica com o texto do arquivo âncora e vira item de decisão no documento de divergências.
- Âncoras de texto: D28 para `missao`, D37 para `minijogo`, D19 para `desafio` ("cada missão ou minijogo"), D29 para `cenario_jogavel`, D05 para `caminho_obrigatorio`, D01 para `situacao_problema`, D31 para `objetivo_de_aprendizagem`, D22 para `documentacao_equivalente`, D36 para `sessao_de_jogo`.
- Os 49 testes existentes continuam verdes, ou são alterados com justificativa escrita no commit.
- Os scripts de migração e verificação são de uso único; ficam em `scripts/` nesta PR e podem ser removidos depois que a PR for aceita.

## File Structure

```
catalog/
  definicoes.yaml                  # NOVO: glossário (termos compartilhados)
  schema.yaml                      # + campo opcional `definicoes` por critério
  D01.yaml … D40.yaml              # migrados: definições inline removidas, campo `definicoes`
scripts/
  vygolint_catalog/
    validate.py                    # + load_definicoes, validate_definicoes, lint por critério
    render.py                      # + seção Glossário, bloco Definições por critério, indicadores em sub-itens
    build.py                       # + carrega e repassa o glossário
  migrate_definicoes.py            # NOVO, uso único: emissor YAML, extrator, migração, relatório
  verify_definicoes.py             # NOVO, uso único: compara etapa 1 (git main) com o novo formato
  definicoes_aceitas.yaml          # NOVO: diferenças aceitas (lido por verify_definicoes.py)
tests/
  helpers.py                       # + glossario_valido()
  test_definicoes.py               # NOVO: glossário, lint, extrator, emissor
  test_validate.py                 # + testes de `definicoes`
  test_render.py                   # ajustes (indicadores em sub-itens, bloco Definições)
  test_build.py                    # + build carrega definicoes.yaml
docs/
  conformidade.md                  # + seção sobre definições
  superpowers/specs/2026-11-03-catalogo-conformidade-design.md   # seção 5 atualizada
  superpowers/specs/2026-11-03-definicoes-divergencias.md        # NOVO: decisões pendentes
README.md                          # + definicoes.yaml na tabela
```

Responsabilidades: `validate.py` conhece o glossário e o lint; `render.py` só imprime; `build.py` orquestra; `migrate_definicoes.py` e `verify_definicoes.py` nunca são importados pelo pacote.

---

### Task 1: Glossário `catalog/definicoes.yaml` e validação do glossário

**Files:**
- Create: `catalog/definicoes.yaml`
- Modify: `scripts/vygolint_catalog/validate.py` (acrescentar no fim)
- Modify: `tests/helpers.py` (acrescentar `glossario_valido`)
- Create: `tests/test_definicoes.py`

**Interfaces:**
- Produces: `load_definicoes(path) -> dict[str, dict]` (chave → entrada), `validate_definicoes(doc) -> list[str]`.
- Formato de uma entrada: `{"chave": str, "termo": str, "gatilhos": [str, ...], "ancora": str, "texto": str}`.

- [ ] **Step 1: Criar o glossário**

```yaml
# Glossário do catálogo vygolint. Cada definição compartilhada existe uma vez aqui.
# Um critério a referencia em `definicoes.glossario` (lista de chaves); o build
# imprime o texto uma vez por critério e falha se o texto do critério usa um
# gatilho sem listar a chave. `ancora` é a diretriz de onde a redação veio.
# Lido por scripts/vygolint_catalog/validate.py.
termos:
  - chave: missao
    termo: missão
    gatilhos: [missão, missões]
    ancora: D28
    texto: "uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão"
  - chave: minijogo
    termo: minijogo
    gatilhos: [minijogo]
    ancora: D37
    texto: "uma atividade com regras, objetivo e condição de conclusão próprios, jogada dentro de uma missão ou à parte dela"
  - chave: desafio
    termo: desafio
    gatilhos: [desafio]
    ancora: D19
    texto: "cada missão ou minijogo"
  - chave: cenario_jogavel
    termo: cenário jogável
    gatilhos: [cenário]
    ancora: D29
    texto: "cada espaço do jogo (mapa, sala ou fase) em que o jogador executa ações e em que há uma missão em curso; cenário em que nenhuma missão está em curso (hub, sandbox) não tem caminho obrigatório e não é cenário jogável"
  - chave: caminho_obrigatorio
    termo: caminho obrigatório (caminho da missão)
    gatilhos: [caminho obrigatório, caminho da missão]
    ancora: D05
    texto: "a sequência de objetivos exigidos para completar a missão em curso, e fora do caminho obrigatório é tudo o que nenhum desses objetivos exige"
  - chave: situacao_problema
    termo: situação-problema
    gatilhos: [situação-problema]
    ancora: D01
    texto: "uma situação com estado inicial, objetivo e mais de uma ação possível, cuja resolução exige uma decisão do jogador, e não apenas a repetição de uma mesma ação; escolher entre alternativas prontas, sem estado inicial a ser transformado pelas ações do jogador, não conta como situação-problema"
  - chave: documentacao_equivalente
    termo: GDD ou documento equivalente
    gatilhos: [GDD, documento equivalente]
    ancora: D22
    texto: "o documento de design do jogo (GDD) ou outro documento de projeto que acompanha o jogo e descreve seu conteúdo (roteiro, guia do professor, plano de aula, mapa de nível ou especificação); material de divulgação ou de loja não conta"
  - chave: objetivo_de_aprendizagem
    termo: objetivo de aprendizagem
    gatilhos: [objetivo de aprendizagem, objetivos de aprendizagem]
    ancora: D31
    texto: "cada conceito, fato ou procedimento listado como conteúdo a ser aprendido no GDD ou documento equivalente, e só essa lista define os objetivos avaliados"
  - chave: sessao_de_jogo
    termo: sessão de jogo
    gatilhos: [sessão de jogo]
    ancora: D36
    texto: "o período contínuo entre o jogador iniciar o jogo, ou carregar um estado salvo, e encerrá-lo (fechar o jogo ou voltar ao menu inicial)"
```

Observação para o relatório (Task 8): os textos de `documentacao_equivalente` e `sessao_de_jogo` não existiam na etapa 1 (D22 definia "documentação" só para o seu contexto; D36 usava "sessão de jogo" sem definir). Ambos entram como decisões pendentes.

- [ ] **Step 2: Escrever os testes que falham**

Em `tests/helpers.py`, acrescentar:

```python
def glossario_valido():
    return yaml.safe_load((REPO / "catalog" / "definicoes.yaml").read_text(encoding="utf-8"))
```

Criar `tests/test_definicoes.py`:

```python
import copy
import unittest

from helpers import REPO, glossario_valido
from vygolint_catalog.validate import load_definicoes, validate_definicoes


class GlossarioTest(unittest.TestCase):
    def test_repo_glossary_is_valid(self):
        self.assertEqual(validate_definicoes(glossario_valido()), [])

    def test_load_returns_map_by_key(self):
        g = load_definicoes(REPO / "catalog" / "definicoes.yaml")
        self.assertIn("missao", g)
        self.assertEqual(g["missao"]["termo"], "missão")
        self.assertIn("missões", g["missao"]["gatilhos"])
        self.assertTrue(g["missao"]["texto"].startswith("uma unidade do jogo"))

    def test_required_fields_and_shapes(self):
        doc = glossario_valido()
        del doc["termos"][0]["texto"]
        self.assertTrue(any("missao" in e and "texto" in e for e in validate_definicoes(doc)))
        doc = glossario_valido()
        doc["termos"][0]["gatilhos"] = []
        self.assertTrue(any("gatilhos" in e for e in validate_definicoes(doc)))
        doc = glossario_valido()
        doc["termos"][0]["chave"] = "Missão"
        self.assertTrue(any("chave" in e for e in validate_definicoes(doc)))

    def test_duplicate_key_and_duplicate_gatilho(self):
        doc = glossario_valido()
        doc["termos"].append(copy.deepcopy(doc["termos"][0]))
        errors = validate_definicoes(doc)
        self.assertTrue(any("duplicad" in e and "missao" in e for e in errors))
        doc = glossario_valido()
        doc["termos"][1]["gatilhos"].append("missão")
        self.assertTrue(any("gatilho" in e and "missão" in e for e in validate_definicoes(doc)))

    def test_non_map_document(self):
        self.assertTrue(validate_definicoes(["x"]))
        self.assertTrue(validate_definicoes({"termos": "x"}))
```

- [ ] **Step 3: Rodar para ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_definicoes.py -v`
Expected: `ImportError: cannot import name 'load_definicoes'`.

- [ ] **Step 4: Implementar no fim de `validate.py`**

```python
_CHAVE_RE = re.compile(r"^[a-z][a-z0-9_]*$")


def validate_definicoes(doc):
    """Return a list of error strings for the glossary document (catalog/definicoes.yaml)."""
    errors = []
    if not isinstance(doc, dict) or not isinstance(doc.get("termos"), list):
        return ["definicoes.yaml: documento deve ser mapa com lista `termos`"]
    chaves = set()
    gatilhos = {}
    for i, e in enumerate(doc["termos"]):
        prefix = f"definicoes.yaml/{e.get('chave') if isinstance(e, dict) else i}"
        if not isinstance(e, dict):
            errors.append(f"{prefix}: entrada deve ser mapa")
            continue
        for campo in ("chave", "termo", "gatilhos", "ancora", "texto"):
            if campo not in e:
                errors.append(f"{prefix}: campo obrigatório ausente: {campo}")
        chave = e.get("chave")
        if not isinstance(chave, str) or not _CHAVE_RE.fullmatch(chave):
            errors.append(f"{prefix}: chave fora do padrão [a-z][a-z0-9_]*")
        elif chave in chaves:
            errors.append(f"{prefix}: chave duplicada: {chave}")
        chaves.add(chave)
        for campo in ("termo", "ancora", "texto"):
            if campo in e and not _is_text(e[campo]):
                errors.append(f"{prefix}: {campo} vazio")
        gs = e.get("gatilhos")
        if "gatilhos" in e and (not isinstance(gs, list) or not gs or not all(_is_text(g) for g in gs)):
            errors.append(f"{prefix}: gatilhos deve ser lista não vazia de textos")
        elif isinstance(gs, list):
            for g in gs:
                if g in gatilhos:
                    errors.append(f"{prefix}: gatilho {g!r} já usado por {gatilhos[g]}")
                gatilhos[g] = chave
    return errors


def load_definicoes(path):
    """Load catalog/definicoes.yaml and return {chave: entrada}. Assumes validate_definicoes passed."""
    doc = load_yaml(path)
    return {e["chave"]: e for e in doc["termos"]}
```

- [ ] **Step 5: Rodar para ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_definicoes.py -v`
Expected: 5 testes OK. Rodar também a suíte completa: 49 + 5 OK.

- [ ] **Step 6: Commit**

```bash
git add catalog/definicoes.yaml scripts/vygolint_catalog/validate.py tests/helpers.py tests/test_definicoes.py
git commit -m "feat(catalog): glossary of shared definitions with validation

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 2: Campo `definicoes` por critério, resolução de chaves e lint

**Files:**
- Modify: `catalog/schema.yaml`
- Modify: `scripts/vygolint_catalog/validate.py` (`validate_diretriz` ganha parâmetro `glossario=None`)
- Modify: `tests/test_validate.py` (acrescentar classe `DefinicoesCriterioTest`)

**Interfaces:**
- Consumes: `load_definicoes`, formato de entrada da Task 1.
- Produces: `validate_diretriz(d, schema, categorias, glossario=None)`. Com `glossario=None` nada do campo `definicoes` é verificado (compatibilidade com os testes antigos). `textos_do_criterio(c) -> list[tuple[str, str]]` (nome do campo, texto) para enunciado, procedimentos, indicadores e escala — reutilizado pelos scripts de migração e verificação.

- [ ] **Step 1: Esquema**

Em `catalog/schema.yaml`, acrescentar dentro de `criterio:`:

```yaml
  opcionais: [definicoes]
  definicoes:
    chaves: [glossario, locais, termos_comuns]   # glossario: lista de chaves de definicoes.yaml; locais: {termo: texto}; termos_comuns: {gatilho: justificativa}
    campos_lint: [enunciado, evidencia.*.procedimento, evidencia.*.indicadores, escala.*]
```

- [ ] **Step 2: Testes que falham** (acrescentar em `tests/test_validate.py`)

```python
from helpers import glossario_valido
from vygolint_catalog.validate import load_definicoes
from helpers import REPO


def _glossario():
    return load_definicoes(REPO / "catalog" / "definicoes.yaml")


class DefinicoesCriterioTest(unittest.TestCase):
    def setUp(self):
        self.schema = schema_valido()
        self.categorias = categorias_validas()
        self.g = _glossario()

    def check(self, d):
        return validate_diretriz(d, self.schema, self.categorias, self.g)

    def _com_missao(self):
        d = diretriz_valida()
        c = d["criterios"][0]
        c["enunciado"] = "Toda ação incorreta do jogador em uma missão recebe mensagem que indica o que fazer"
        c["definicoes"] = {"glossario": ["missao"]}
        return d

    def test_valid_reference_passes(self):
        self.assertEqual(self.check(self._com_missao()), [])

    def test_without_glossary_param_nothing_is_checked(self):
        d = self._com_missao()
        d["criterios"][0]["definicoes"] = {"glossario": ["nao_existe"]}
        self.assertEqual(validate_diretriz(d, self.schema, self.categorias), [])

    def test_unknown_key(self):
        d = self._com_missao()
        d["criterios"][0]["definicoes"]["glossario"] = ["missao", "nao_existe"]
        self.assertTrue(any("nao_existe" in e for e in self.check(d)))

    def test_gatilho_without_key_is_error(self):
        d = self._com_missao()
        d["criterios"][0]["definicoes"] = {}
        errors = self.check(d)
        self.assertTrue(any('"missão"' in e and "missao" in e for e in errors), errors)

    def test_gatilho_in_indicator_and_scale_is_linted(self):
        d = diretriz_valida()
        c = d["criterios"][0]
        c["evidencia"]["codigo"]["indicadores"].append("mensagem cita o desafio")
        self.assertTrue(any("desafio" in e for e in self.check(d)))
        d = diretriz_valida()
        d["criterios"][0]["escala"]["parcial"] = "Alguns cenários orientam"
        self.assertTrue(any("cenario_jogavel" in e for e in self.check(d)))

    def test_justificativa_is_not_linted(self):
        d = diretriz_valida()
        d["criterios"][0]["nivel_justificativa"]["texto"] = "A missão é o centro da ZDP."
        self.assertEqual(self.check(d), [])

    def test_key_listed_but_unused_is_error(self):
        d = diretriz_valida()
        d["criterios"][0]["definicoes"] = {"glossario": ["missao"]}
        self.assertTrue(any("missao" in e and "nenhum gatilho" in e for e in self.check(d)))

    def test_glossary_text_cascades(self):
        # cenario_jogavel's text mentions "missão" and "caminho obrigatório": both keys are required.
        d = diretriz_valida()
        c = d["criterios"][0]
        c["enunciado"] = "Em todo cenário jogável o feedback orienta"
        c["definicoes"] = {"glossario": ["cenario_jogavel"]}
        errors = self.check(d)
        self.assertTrue(any("missao" in e for e in errors), errors)
        self.assertTrue(any("caminho_obrigatorio" in e for e in errors), errors)
        c["definicoes"]["glossario"] += ["missao", "caminho_obrigatorio"]
        self.assertEqual(self.check(d), [])

    def test_locais_shape_and_count_as_usage(self):
        d = diretriz_valida()
        c = d["criterios"][0]
        c["definicoes"] = {"locais": {"dispositivo": "um elemento presente na abertura da missão"}, "glossario": ["missao"]}
        self.assertEqual(self.check(d), [])
        c["definicoes"]["locais"] = {"dispositivo": ""}
        self.assertTrue(any("locais" in e for e in self.check(d)))
        c["definicoes"]["locais"] = ["dispositivo"]
        self.assertTrue(any("locais" in e for e in self.check(d)))

    def test_termos_comuns_silences_lint_with_justification(self):
        d = diretriz_valida()
        c = d["criterios"][0]
        c["escala"]["parcial"] = "O cenário de erro orienta em parte"
        c["definicoes"] = {"termos_comuns": {"cenário": "sentido corrente de situação, não o cenário jogável"}}
        self.assertEqual(self.check(d), [])
        c["definicoes"]["termos_comuns"] = {"cenário": ""}
        self.assertTrue(any("termos_comuns" in e for e in self.check(d)))
        c["definicoes"]["termos_comuns"] = {"foguete": "x"}
        self.assertTrue(any("foguete" in e for e in self.check(d)))
        c["definicoes"] = {"termos_comuns": {"cenário": "x"}, "glossario": ["cenario_jogavel", "missao", "caminho_obrigatorio"]}
        self.assertTrue(any("termos_comuns" in e and "glossario" in e for e in self.check(d)))

    def test_inline_definitions_are_forbidden(self):
        d = self._com_missao()
        c = d["criterios"][0]
        c["escala"]["parcial"] += ". Definição: missão é uma unidade do jogo"
        self.assertTrue(any("Definição" in e for e in self.check(d)))
        d = self._com_missao()
        d["criterios"][0]["enunciado"] += "; missão é " + self.g["missao"]["texto"]
        self.assertTrue(any("glossário" in e and "missao" in e for e in self.check(d)))

    def test_unknown_definicoes_key_and_shape(self):
        d = self._com_missao()
        d["criterios"][0]["definicoes"]["extra"] = 1
        self.assertTrue(any("extra" in e for e in self.check(d)))
        d["criterios"][0]["definicoes"] = "missao"
        self.assertTrue(any("definicoes" in e for e in self.check(d)))
```

- [ ] **Step 3: Rodar para ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_validate.py -v`
Expected: `TypeError: validate_diretriz() takes 3 positional arguments but 4 were given` e falhas de lint.

- [ ] **Step 4: Implementar em `validate.py`**

Acrescentar antes de `_validate_criterio`:

```python
_INLINE_RE = re.compile(r"Defini(ções|ção):")


def textos_do_criterio(c):
    """Yield (campo, texto) for every text field the lint covers (not nivel_justificativa)."""
    out = []
    if _is_text(c.get("enunciado")):
        out.append(("enunciado", c["enunciado"]))
    ev = c.get("evidencia") if isinstance(c.get("evidencia"), dict) else {}
    for nome in ("codigo", "documentacao", "video"):
        fonte = ev.get(nome)
        if isinstance(fonte, dict):
            if _is_text(fonte.get("procedimento")):
                out.append((f"{nome}.procedimento", fonte["procedimento"]))
            for i, ind in enumerate(fonte.get("indicadores") or []):
                if _is_text(ind):
                    out.append((f"{nome}.indicadores[{i}]", ind))
    esc = c.get("escala") if isinstance(c.get("escala"), dict) else {}
    for grau in ("atendido", "parcial", "nao_atendido"):
        if _is_text(esc.get(grau)):
            out.append((f"escala.{grau}", esc[grau]))
    return out


def _validate_definicoes_criterio(c, prefix, schema, glossario, errors):
    defs = c.get("definicoes", {})
    if defs is None:
        defs = {}
    if not isinstance(defs, dict):
        errors.append(f"{prefix}: definicoes deve ser mapa")
        return
    permitidas = set(schema["criterio"]["definicoes"]["chaves"])
    extras = set(defs) - permitidas
    if extras:
        errors.append(f"{prefix}: definicoes com chaves desconhecidas: {sorted(extras)}")
    chaves = defs.get("glossario") or []
    if not isinstance(chaves, list) or not all(isinstance(k, str) for k in chaves):
        errors.append(f"{prefix}: definicoes.glossario deve ser lista de chaves")
        chaves = []
    for k in chaves:
        if k not in glossario:
            errors.append(f"{prefix}: definicoes.glossario cita chave inexistente: {k}")
    if len(set(chaves)) != len(chaves):
        errors.append(f"{prefix}: definicoes.glossario com chave repetida")
    locais = defs.get("locais") or {}
    if not isinstance(locais, dict) or not all(_is_text(k) and _is_text(v) for k, v in locais.items()):
        errors.append(f"{prefix}: definicoes.locais deve ser mapa termo -> texto não vazio")
        locais = {}
    comuns = defs.get("termos_comuns") or {}
    if not isinstance(comuns, dict) or not all(_is_text(k) and _is_text(v) for k, v in comuns.items()):
        errors.append(f"{prefix}: definicoes.termos_comuns deve ser mapa gatilho -> justificativa não vazia")
        comuns = {}
    gatilho_para_chave = {g: e["chave"] for e in glossario.values() for g in e["gatilhos"]}
    for g in comuns:
        if g not in gatilho_para_chave:
            errors.append(f"{prefix}: definicoes.termos_comuns cita gatilho desconhecido: {g!r}")
        elif gatilho_para_chave[g] in chaves:
            errors.append(
                f"{prefix}: definicoes.termos_comuns lista {g!r} mas glossario também lista {gatilho_para_chave[g]}"
            )
    campos = textos_do_criterio(c)
    for campo, texto in campos:
        if _INLINE_RE.search(texto):
            errors.append(f"{prefix}: {campo} contém definição inline ('Definições:'); use o campo definicoes")
        for e in glossario.values():
            if e["texto"] in texto:
                errors.append(f"{prefix}: {campo} repete o texto do glossário de {e['chave']}; use definicoes.glossario")
    corpus_proprio = " ".join(t for _, t in campos).lower()
    corpus = corpus_proprio + " " + " ".join(locais.values()).lower()
    corpus += " " + " ".join(glossario[k]["texto"].lower() for k in chaves if k in glossario)
    for e in glossario.values():
        usados = [g for g in e["gatilhos"] if g.lower() in corpus]
        listado = e["chave"] in chaves
        comum = any(g in comuns for g in e["gatilhos"])
        if usados and not listado and not comum:
            errors.append(
                f"{prefix}: texto usa \"{usados[0]}\" mas definicoes.glossario não lista \"{e['chave']}\""
            )
        if listado and not usados:
            errors.append(f"{prefix}: definicoes.glossario lista \"{e['chave']}\" mas nenhum gatilho aparece no texto")
    for g in comuns:
        if g.lower() not in corpus_proprio:
            errors.append(f"{prefix}: definicoes.termos_comuns lista {g!r} mas o termo não aparece no texto")
```

Em `_validate_criterio(c, diretriz_id, schema, errors)`, mudar a assinatura para `_validate_criterio(c, diretriz_id, schema, errors, glossario=None)` e acrescentar no fim:

```python
    if glossario is not None:
        _validate_definicoes_criterio(c, prefix, schema, glossario, errors)
```

Em `validate_diretriz(d, schema, categorias)`, mudar para `validate_diretriz(d, schema, categorias, glossario=None)` e passar `glossario` na chamada `_validate_criterio(c, did, schema, errors, glossario)`.

- [ ] **Step 5: Rodar para ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v`
Expected: todos OK (49 antigos + 5 da Task 1 + 12 novos).

- [ ] **Step 6: Commit**

```bash
git add catalog/schema.yaml scripts/vygolint_catalog/validate.py tests/test_validate.py
git commit -m "feat(validate): per-criterion definicoes field, key resolution and trigger lint

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 3: Render do bloco Definições, seção Glossário e indicadores em sub-itens

**Files:**
- Modify: `scripts/vygolint_catalog/render.py`
- Modify: `tests/test_render.py`

**Interfaces:**
- Produces: `render_markdown(diretrizes, categorias, glossario=None)`. `render_latex` não muda.
- Formato por critério (antes do enunciado):

```
#### D28.1 — Nível AA

**Definições.**

- *missão*: uma unidade do jogo com objetivo …
- *dispositivo*: um destes elementos presentes na abertura …
- *cenário* (sentido corrente): …justificativa…

**Enunciado.** …
```

- Evidência passa a ser:

```
- Código: Localizar manipuladores de erro e verificar o texto exibido
  - mensagem contém orientação de próxima ação
- Documentação: não se aplica
```

Justificativa da mudança de formato dos indicadores: linhas de `catalogo.md` de até 5.800 caracteres; meta de nenhuma linha acima de 1.500.

- [ ] **Step 1: Ajustar o teste existente e acrescentar novos**

Em `test_detail_section_contains_all_blocks`, trocar o trecho `"Indicadores: ao menos 3 ocorrências de erro; cada ocorrência mostra orientação"` por dois trechos: `"- Vídeo: Registrar timestamp de cada erro e classificar o feedback\n  - ao menos 3 ocorrências de erro\n  - cada ocorrência mostra orientação"`. Acrescentar à classe `RenderMarkdownTest`:

```python
    def test_definicoes_block_before_enunciado(self):
        from helpers import REPO
        from vygolint_catalog.validate import load_definicoes
        g = load_definicoes(REPO / "catalog" / "definicoes.yaml")
        d = diretriz_valida()
        c = d["criterios"][0]
        c["definicoes"] = {
            "glossario": ["missao"],
            "locais": {"dispositivo": "um elemento presente na abertura"},
            "termos_comuns": {"cenário": "sentido corrente"},
        }
        out = render_markdown([d], self.cats, g)
        bloco = (
            "**Definições.**\n\n"
            "- *missão*: " + g["missao"]["texto"] + "\n"
            "- *dispositivo*: um elemento presente na abertura\n"
            "- *cenário* (sentido corrente): sentido corrente\n\n"
            "**Enunciado.**"
        )
        self.assertIn(bloco, out)
        self.assertLess(out.index("**Definições.**"), out.index("**Enunciado.**"))

    def test_no_definicoes_block_when_absent(self):
        out = render_markdown([diretriz_valida()], self.cats, {})
        self.assertNotIn("**Definições.**", out)

    def test_glossary_section(self):
        from helpers import REPO
        from vygolint_catalog.validate import load_definicoes
        g = load_definicoes(REPO / "catalog" / "definicoes.yaml")
        out = render_markdown([diretriz_valida()], self.cats, g)
        self.assertIn("## Glossário", out)
        self.assertIn("- **missão** (âncora D28; gatilhos: missão, missões): " + g["missao"]["texto"], out)
        self.assertLess(out.index("## Glossário"), out.index("## Resumo"))
        self.assertNotIn("## Glossário", render_markdown([diretriz_valida()], self.cats))
```

- [ ] **Step 2: Rodar para ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_render.py -v`
Expected: falhas nos 3 novos testes e no ajustado.

- [ ] **Step 3: Implementar em `render.py`**

Substituir a assinatura e o corpo de `render_markdown`:

```python
def _bloco_definicoes(c, glossario):
    defs = c.get("definicoes") or {}
    itens = []
    for chave in defs.get("glossario") or []:
        e = glossario[chave]
        itens.append(f"- *{e['termo']}*: {e['texto']}")
    for termo, texto in (defs.get("locais") or {}).items():
        itens.append(f"- *{termo}*: {texto}")
    for termo, just in (defs.get("termos_comuns") or {}).items():
        itens.append(f"- *{termo}* (sentido corrente): {just}")
    if not itens:
        return []
    return ["**Definições.**", ""] + itens + [""]


def _secao_glossario(glossario):
    if not glossario:
        return []
    linhas = ["## Glossário", "", "Definições compartilhadas, referenciadas pelos critérios em `definicoes.glossario`.", ""]
    for e in glossario.values():
        linhas.append(f"- **{e['termo']}** (âncora {e['ancora']}; gatilhos: {', '.join(e['gatilhos'])}): {e['texto']}")
    return linhas + [""]


def render_markdown(diretrizes, categorias, glossario=None):
    glossario = glossario or {}
    linhas = [
        GENERATED_MD,
        "# Catálogo vygolint — diretrizes e critérios de conformidade",
        "",
        "Fonte das diretrizes: CARVALHO, Diego Marques. *Diretrizes para o desenvolvimento de jogos "
        "educacionais digitais embasados na teoria sociointeracionista de Lev Semionovich Vigotski*. "
        "Dissertação (Mestrado), UFABC, 2020. Quadro 3.",
        "",
        "> " + categorias["ressalva"].strip().replace("\n", " "),
        "",
    ]
    linhas += _secao_glossario(glossario)
    linhas += [
        "## Resumo",
        "",
        "| ID | Categoria | Diretriz | Critérios |",
        "|---|---|---|---|",
    ]
    ordenadas = _ordenadas(diretrizes)
    for d in ordenadas:
        linhas.append(
            f"| {d['id']} | {_nome_categoria(d['categoria'], categorias)} | {d['diretriz']} | {_criterios_resumo(d)} |"
        )
    linhas += ["", "## Diretrizes", ""]
    for d in ordenadas:
        linhas += [
            f"### {d['id']} — {d['diretriz']}",
            "",
            f"- Categoria: {_nome_categoria(d['categoria'], categorias)}",
            f"- Modalidade: {d['modalidade']}",
            f"- Aplicabilidade: {d['aplicabilidade'] or '—'}",
            f"- Fonte: {d['fonte']}",
            "",
        ]
        for c in d["criterios"]:
            nj = c["nivel_justificativa"]
            linhas += [f"#### {c['id']} — Nível {c['nivel']}", ""]
            linhas += _bloco_definicoes(c, glossario)
            linhas += [
                f"**Enunciado.** {c['enunciado']}",
                "",
                f"**Justificativa do nível.** essencialidade {_EIXOS[nj['essencialidade']]}, "
                f"viabilidade {_EIXOS[nj['viabilidade']]}. {nj['texto']}",
                "",
                "**Evidência.**",
            ]
            for chave, nome in _FONTES:
                fonte = c["evidencia"][chave]
                if fonte is None:
                    linhas.append(f"- {nome}: não se aplica")
                else:
                    linhas.append(f"- {nome}: {fonte['procedimento']}")
                    linhas += [f"  - {ind}" for ind in fonte["indicadores"]]
            linhas += ["", "**Escala.**"]
            for chave, nome in _GRAUS:
                linhas.append(f"- {nome}: {c['escala'][chave]}")
            linhas += ["", f"**Depende de.** {_depende_de(c)}", ""]
    return "\n".join(linhas).rstrip() + "\n"
```

- [ ] **Step 4: Rodar para ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_render.py -v`
Expected: todos OK.

- [ ] **Step 5: Commit** (não regenerar docs ainda; o build ainda não passa o glossário)

```bash
git add scripts/vygolint_catalog/render.py tests/test_render.py
git commit -m "feat(render): definitions block per criterion, glossary section, indicators as sub-items

Indicators were joined on one line, producing lines of up to 5800 characters
in docs/catalogo.md; the target is no line above 1500 characters.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 4: `build.py` carrega o glossário; docs regenerados

**Files:**
- Modify: `scripts/vygolint_catalog/build.py`
- Modify: `tests/test_build.py`
- Regenerate: `docs/catalogo.md`, `docs/catalogo.tex`

**Interfaces:**
- Consumes: `load_definicoes`, `validate_definicoes`, `validate_diretriz(..., glossario)`, `render_markdown(..., glossario)`.
- `build(catalog_dir, docs_dir)` mantém a assinatura. Se `definicoes.yaml` não existir no diretório, erro `definicoes.yaml: arquivo ausente`.

- [ ] **Step 1: Testes** (em `tests/test_build.py`; `setUp` passa a copiar também `definicoes.yaml`)

```python
    # em setUp, depois das duas cópias existentes:
        shutil.copy(REPO / "catalog" / "definicoes.yaml", self.catalog)

    def test_missing_glossary_is_error(self):
        (self.catalog / "definicoes.yaml").unlink()
        self.write(diretriz_valida())
        errors = build(self.catalog, self.docs)
        self.assertTrue(any("definicoes.yaml" in e for e in errors))
        self.assertFalse(self.docs.exists())

    def test_invalid_glossary_is_error(self):
        (self.catalog / "definicoes.yaml").write_text("termos: [{chave: x}]\n", encoding="utf-8")
        self.write(diretriz_valida())
        self.assertTrue(any("definicoes.yaml" in e for e in build(self.catalog, self.docs)))

    def test_lint_runs_in_build(self):
        d = diretriz_valida()
        d["criterios"][0]["enunciado"] = "Em cada missão o feedback orienta"
        self.write(d)
        errors = build(self.catalog, self.docs)
        self.assertTrue(any("missao" in e for e in errors), errors)
        d["criterios"][0]["definicoes"] = {"glossario": ["missao"]}
        self.write(d)
        self.assertEqual(build(self.catalog, self.docs), [])
        self.assertIn("**Definições.**", (self.docs / "catalogo.md").read_text(encoding="utf-8"))
```

- [ ] **Step 2: Rodar para ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_build.py -v`
Expected: 3 falhas.

- [ ] **Step 3: Implementar em `build.py`**

```python
from .validate import load_definicoes, load_yaml, validate_catalogo, validate_definicoes, validate_diretriz
```

e, em `build`, logo depois de carregar `categorias`:

```python
    glossario_path = catalog_dir / "definicoes.yaml"
    if not glossario_path.exists():
        return ["definicoes.yaml: arquivo ausente"]
    try:
        doc = load_yaml(glossario_path)
    except yaml.YAMLError as exc:
        return [f"definicoes.yaml: YAML inválido: {exc}"]
    errors = validate_definicoes(doc)
    if errors:
        return errors
    glossario = {e["chave"]: e for e in doc["termos"]}
```

Passar `glossario` em `validate_diretriz(d, schema, categorias, glossario)` e em `render_markdown(diretrizes, categorias, glossario)`.

- [ ] **Step 4: Rodar a suíte completa, o build e regenerar docs**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v && python3 scripts/build_catalog.py`
Expected: o build FALHA com erros de lint em quase todos os `Dnn.yaml` (gatilhos sem chave e `Definições:` inline). Isso é esperado: os arquivos ainda não foram migrados. Não regenerar docs nesta task.

- [ ] **Step 5: Commit**

```bash
git add scripts/vygolint_catalog/build.py tests/test_build.py
git commit -m "feat(build): load and validate the glossary, pass it to lint and render

The catalog build fails from this commit until the Dnn.yaml files are migrated.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 5: Script de migração (emissor YAML, extrator, relatório)

**Files:**
- Create: `scripts/migrate_definicoes.py`
- Modify: `tests/test_definicoes.py` (acrescentar testes do emissor e do extrator)

**Interfaces:**
- Produces (importadas por `verify_definicoes.py` e pelos testes):
  - `emit_yaml(d: dict) -> str`: escreve uma diretriz no layout do catálogo (chaves na ordem canônica, textos entre aspas duplas).
  - `extrair_blocos(texto: str) -> tuple[str, list[str]]`: devolve `(texto_sem_definicoes, [corpo_do_bloco, ...])` para os blocos `Definições:`/`Definição:` e para a cadeia final `; termo é …` do enunciado.
  - `clausulas(corpo: str) -> list[str]`: divide em `; ` fora de parênteses.
  - `agrupar(clausulas) -> list[tuple[str, list[str]]]`: `(termo, [cláusulas])`, termo `""` quando não identificado.
  - `ALIASES: dict[str, list[str]]` (termo → chaves do glossário).
  - `normalizar_clausula(s) -> str`: strip, espaços colapsados, sem `.` final, ` é `/` são ` logo após o termo viram ` = `.
- CLI: `python3 scripts/migrate_definicoes.py --dry-run` (só relatório em stdout, Markdown), `--write` (reescreve `catalog/D*.yaml`), `--only D28,D39` (subconjunto), `--roundtrip` (reescreve sem migrar; usado para validar o emissor).

- [ ] **Step 1: Testes do emissor e do extrator** (acrescentar a `tests/test_definicoes.py`)

```python
import sys
sys.path.insert(0, str(REPO / "scripts"))
import yaml
from migrate_definicoes import ALIASES, agrupar, clausulas, emit_yaml, extrair_blocos, normalizar_clausula


class EmitYamlTest(unittest.TestCase):
    def test_roundtrip_every_catalog_file(self):
        for path in sorted((REPO / "catalog").glob("D*.yaml")):
            with self.subTest(path=path.name):
                d = yaml.safe_load(path.read_text(encoding="utf-8"))
                self.assertEqual(yaml.safe_load(emit_yaml(d)), d)

    def test_layout_and_quoting(self):
        from helpers import diretriz_valida
        d = diretriz_valida()
        d["criterios"][0]["enunciado"] = 'Texto com "aspas" e \\ barra'
        d["criterios"][0]["depende_de"] = [["D06.1", "D07.1"]]
        d["criterios"][0]["definicoes"] = {"glossario": ["missao"], "locais": {"abertura da missão": "trecho"}}
        out = emit_yaml(d)
        self.assertTrue(out.startswith("id: D17\ncategoria: mediacao\ndiretriz: \"O jogo"))
        self.assertIn('    enunciado: "Texto com \\"aspas\\" e \\\\ barra"', out)
        self.assertIn("      codigo:\n        procedimento: \"Localizar", out)
        self.assertIn("        indicadores:\n          - \"mensagem", out)
        self.assertIn("      documentacao: null\n", out)
        self.assertIn("    depende_de:\n      - [D06.1, D07.1]\n", out)
        self.assertIn("    definicoes:\n      glossario: [missao]\n      locais:\n        \"abertura da missão\": \"trecho\"\n", out)
        self.assertEqual(yaml.safe_load(out), d)


class ExtratorTest(unittest.TestCase):
    def test_block_at_end_of_enunciado(self):
        t = "A abertura apresenta um dispositivo; Definições: missão é uma unidade; dispositivo é um destes elementos (a; b) presentes"
        texto, blocos = extrair_blocos(t)
        self.assertEqual(texto, "A abertura apresenta um dispositivo")
        self.assertEqual(blocos, ["missão é uma unidade; dispositivo é um destes elementos (a; b) presentes"])

    def test_block_in_middle_of_procedimento(self):
        t = "Verificar no GDD cada missão. Definições: missão é uma unidade do jogo. Regra de desempate: vale o GDD"
        texto, blocos = extrair_blocos(t)
        self.assertEqual(texto, "Verificar no GDD cada missão. Regra de desempate: vale o GDD")
        self.assertEqual(blocos, ["missão é uma unidade do jogo"])

    def test_single_definition_in_scale(self):
        t = "Nenhuma missão tem dispositivo, nos termos do enunciado. Definição: abertura da missão é o trecho exibido antes"
        texto, blocos = extrair_blocos(t)
        self.assertEqual(texto, "Nenhuma missão tem dispositivo, nos termos do enunciado")
        self.assertEqual(blocos, ["abertura da missão é o trecho exibido antes"])

    def test_trailing_chain_without_prefix(self):
        t = "O jogador alcança áreas fora do caminho da missão em curso; caminho da missão é a sequência de objetivos exigidos para completá-la"
        texto, blocos = extrair_blocos(t)
        self.assertEqual(texto, "O jogador alcança áreas fora do caminho da missão em curso")
        self.assertEqual(blocos, ["caminho da missão é a sequência de objetivos exigidos para completá-la"])

    def test_no_block(self):
        self.assertEqual(extrair_blocos("Texto simples; outra frase"), ("Texto simples; outra frase", []))

    def test_clausulas_respect_parentheses(self):
        self.assertEqual(clausulas("a é x (p; q); b é y"), ["a é x (p; q)", "b é y"])

    def test_agrupar_merges_clauses_starting_with_article_or_verb(self):
        grupos = agrupar(["detalhe é um elemento", "o desafio exige o detalhe quando X", "o detalhe é sinalizado quando Y", "fala é áudio"])
        self.assertEqual(grupos, [("detalhe", ["detalhe é um elemento", "o desafio exige o detalhe quando X", "o detalhe é sinalizado quando Y"]), ("fala", ["fala é áudio"])])
        self.assertEqual(agrupar(["caminho obrigatório, o mesmo que caminho da missão em D05, é a sequência"]), [("caminho obrigatório", ["caminho obrigatório, o mesmo que caminho da missão em D05, é a sequência"])])
        self.assertEqual(agrupar(["a missão aceita dois jogadores quando o jogo permite"]), [("", ["a missão aceita dois jogadores quando o jogo permite"])])

    def test_aliases_and_normalization(self):
        self.assertEqual(ALIASES["missão ou desafio"], ["missao", "desafio"])
        self.assertEqual(normalizar_clausula("objetivos de aprendizagem são os listados no GDD. "), "objetivos de aprendizagem = os listados no GDD")
        self.assertEqual(normalizar_clausula("missão é  uma unidade"), "missão = uma unidade")
```

- [ ] **Step 2: Rodar para ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_definicoes.py -v`
Expected: `ModuleNotFoundError: No module named 'migrate_definicoes'`.

- [ ] **Step 3: Implementar `scripts/migrate_definicoes.py`**

```python
#!/usr/bin/env python3
"""One-shot migration of inline definitions in catalog/D*.yaml to the `definicoes` field.

Usage:
  python3 scripts/migrate_definicoes.py --dry-run            # Markdown report on stdout, no writes
  python3 scripts/migrate_definicoes.py --write [--only D28,D39]
  python3 scripts/migrate_definicoes.py --roundtrip          # rewrite files unchanged (emitter check)
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from vygolint_catalog.validate import load_definicoes, textos_do_criterio  # noqa: E402

# Termo como aparece no texto -> chaves do glossário.
ALIASES = {
    "missão": ["missao"],
    "missões": ["missao"],
    "missão ou tarefa": ["missao"],
    "missão ou desafio": ["missao", "desafio"],
    "minijogo": ["minijogo"],
    "desafio": ["desafio"],
    "cenário jogável": ["cenario_jogavel"],
    "caminho obrigatório": ["caminho_obrigatorio"],
    "caminho da missão": ["caminho_obrigatorio"],
    "situação-problema": ["situacao_problema"],
    "objetivo de aprendizagem": ["objetivo_de_aprendizagem"],
    "objetivos de aprendizagem": ["objetivo_de_aprendizagem"],
    "sessão de jogo": ["sessao_de_jogo"],
    "documentação": ["documentacao_equivalente"],
}

# Cláusulas da etapa 1 declaradas equivalentes ao texto canônico (normalizadas).
# Preenchido na Task 7 a partir do relatório; espelhado em scripts/definicoes_aceitas.yaml.
EQUIVALENTES = set()

_ORDEM_DIRETRIZ = ("id", "categoria", "diretriz", "fonte", "modalidade", "aplicabilidade")
_BARE = {"id", "categoria", "modalidade", "nivel", "essencialidade", "viabilidade"}


def _q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _val(k, v):
    if v is None:
        return "null"
    if k in _BARE:
        return str(v)
    return _q(str(v))


def emit_yaml(d):
    out = [f"{k}: {_val(k, d[k])}" for k in _ORDEM_DIRETRIZ]
    out.append("criterios:")
    for c in d["criterios"]:
        out.append(f"  - id: {c['id']}")
        out.append(f"    nivel: {c['nivel']}")
        out.append(f"    enunciado: {_q(c['enunciado'])}")
        nj = c["nivel_justificativa"]
        out += ["    nivel_justificativa:", f"      essencialidade: {nj['essencialidade']}",
                f"      viabilidade: {nj['viabilidade']}", f"      texto: {_q(nj['texto'])}"]
        out.append("    evidencia:")
        for nome in ("codigo", "documentacao", "video"):
            fonte = c["evidencia"][nome]
            if fonte is None:
                out.append(f"      {nome}: null")
                continue
            out += [f"      {nome}:", f"        procedimento: {_q(fonte['procedimento'])}", "        indicadores:"]
            out += [f"          - {_q(i)}" for i in fonte["indicadores"]]
        out.append("    escala:")
        out += [f"      {g}: {_q(c['escala'][g])}" for g in ("atendido", "parcial", "nao_atendido")]
        if c["depende_de"]:
            out.append("    depende_de:")
            out += ["      - [" + ", ".join(g) + "]" for g in c["depende_de"]]
        else:
            out.append("    depende_de: []")
        defs = c.get("definicoes")
        if defs:
            out.append("    definicoes:")
            if defs.get("glossario"):
                out.append("      glossario: [" + ", ".join(defs["glossario"]) + "]")
            for campo in ("locais", "termos_comuns"):
                if defs.get(campo):
                    out.append(f"      {campo}:")
                    out += [f"        {_q(k)}: {_q(v)}" for k, v in defs[campo].items()]
    return "\n".join(out) + "\n"


_MAIUSCULA = "A-ZÁÉÍÓÚÂÊÔÃÕÇ"
_PREFIXO_RE = re.compile(r"(?P<sep>;\s*|\.\s*|\s+)Defini(?:ções|ção):\s*")
_TERMO_RE = re.compile(r"^(?P<termo>[^;:()]{1,70}?)(?:, o mesmo que [^,]+,)? (?:é|são) (?P<resto>.+)$", re.S)
_ARTIGOS = {"o", "a", "os", "as", "um", "uma", "é", "são", "não", "se", "e"}


def _fim_do_bloco(texto, inicio):
    """Index where a definitions body ends: '. ' + capital letter at paren depth 0, or end of text."""
    depth = 0
    i = inicio
    while i < len(texto):
        ch = texto[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif ch == "." and depth == 0:
            m = re.match(r"\.\s+[" + _MAIUSCULA + "]", texto[i:])
            if m:
                return i
        i += 1
    return len(texto)


def _termo_de(clausula):
    m = _TERMO_RE.match(clausula)
    if not m:
        return ""
    termo = m.group("termo").strip()
    palavras = termo.split()
    if not palavras or palavras[0].lower() in _ARTIGOS or " não" in f" {termo}" or len(palavras) > 7:
        return ""
    return termo


def clausulas(corpo):
    partes, depth, atual = [], 0, []
    i = 0
    while i < len(corpo):
        ch = corpo[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == ";" and depth == 0 and corpo[i + 1 : i + 2] == " ":
            partes.append("".join(atual).strip())
            atual = []
            i += 2
            continue
        atual.append(ch)
        i += 1
    if "".join(atual).strip():
        partes.append("".join(atual).strip())
    return partes


def agrupar(cls):
    grupos = []
    for cl in cls:
        termo = _termo_de(cl)
        if termo or not grupos:
            grupos.append((termo, [cl]))
        else:
            grupos[-1][1].append(cl)
    return grupos


def _cadeia_final(texto):
    """Trailing '; termo é …' chain of an enunciado without the 'Definições:' prefix."""
    cls = clausulas(texto)
    for i, cl in enumerate(cls):
        if i > 0 and _termo_de(cl):
            if all(_termo_de(c) or not _TERMO_RE.match(c) for c in cls[i:]):
                corpo = "; ".join(cls[i:])
                pos = texto.find(corpo)
                return texto[:pos].rstrip().rstrip(";").rstrip(), corpo
            return texto, None
    return texto, None


def extrair_blocos(texto, cadeia=True):
    blocos = []
    while True:
        m = _PREFIXO_RE.search(texto)
        if not m:
            break
        fim = _fim_do_bloco(texto, m.end())
        corpo = texto[m.end() : fim].strip().rstrip(".")
        blocos.append(corpo)
        antes = texto[: m.start()].rstrip()
        depois = texto[fim:]
        if depois.startswith("."):
            texto = antes.rstrip(";:,") + depois
        else:
            texto = antes.rstrip(";:,")
    if cadeia and not blocos:
        texto, corpo = _cadeia_final(texto)
        if corpo:
            blocos.append(corpo)
    return texto, blocos


def normalizar_clausula(s):
    s = re.sub(r"\s+", " ", s).strip().rstrip(".").strip()
    return re.sub(r"^(?P<t>[^;:()]{1,70}?)(?P<ap>, o mesmo que [^,]+,)? (?:é|são) ", lambda m: m.group("t") + (m.group("ap") or "") + " = ", s, count=1)
```

Continuação do mesmo arquivo (migração e relatório):

```python
def _canonica(glossario, chave):
    return normalizar_clausula(f"{glossario[chave]['termo'].split(' (')[0]} é {glossario[chave]['texto']}")


def migrar_criterio(c, glossario, relatorio, did):
    """Mutate criterion in place; append findings to relatorio (dict of lists)."""
    chaves, locais, vistos = [], {}, {}
    campos = textos_do_criterio(c)
    for campo, texto in campos:
        cadeia = campo == "enunciado"
        novo, blocos = extrair_blocos(texto, cadeia=cadeia)
        _set_campo(c, campo, novo)
        for corpo in blocos:
            for termo, cls in agrupar(clausulas(corpo)):
                primeira = normalizar_clausula(cls[0])
                if termo in ALIASES:
                    for k in ALIASES[termo]:
                        if k not in chaves:
                            chaves.append(k)
                        if primeira != _canonica(glossario, k) and primeira not in EQUIVALENTES:
                            relatorio["divergencias"].append((k, did, c["id"], campo, cls[0]))
                        elif primeira != _canonica(glossario, k):
                            relatorio["normalizadas"].append((k, did, c["id"], campo, cls[0]))
                    if len(cls) > 1:
                        relatorio["sobras"].append((did, c["id"], campo, termo, cls[1:]))
                    continue
                chave_local = termo or cls[0][:60]
                texto_local = "; ".join([cls[0][len(termo):].lstrip() if termo else cls[0]] + cls[1:])
                if termo:
                    texto_local = re.sub(r"^(?:, o mesmo que [^,]+,)?\s*(?:é|são)\s+", "", texto_local, count=1)
                if chave_local in locais and locais[chave_local] != texto_local:
                    relatorio["locais_divergentes"].append((did, c["id"], campo, chave_local, locais[chave_local], texto_local))
                locais.setdefault(chave_local, texto_local)
    # termos ainda usados sem definição inline (lint vai exigir): registrar para a revisão
    corpus = " ".join(t for _, t in textos_do_criterio(c)).lower()
    for e in glossario.values():
        if e["chave"] not in chaves and any(g.lower() in corpus for g in e["gatilhos"]):
            chaves.append(e["chave"])
            relatorio["adicionadas"].append((e["chave"], did, c["id"]))
    defs = {}
    if chaves:
        defs["glossario"] = chaves
    if locais:
        defs["locais"] = locais
    if defs:
        c["definicoes"] = defs


def _set_campo(c, campo, valor):
    if campo == "enunciado":
        c["enunciado"] = valor
    elif campo.startswith("escala."):
        c["escala"][campo.split(".")[1]] = valor
    else:
        fonte, resto = campo.split(".", 1)
        if resto == "procedimento":
            c["evidencia"][fonte]["procedimento"] = valor
        else:
            i = int(resto[len("indicadores["):-1])
            c["evidencia"][fonte]["indicadores"][i] = valor


def _prefixo_menos(c, glossario, did, relatorio):
    """Definitions outside any block ('…, e missão é uma atividade…') that need manual migration."""
    for campo, texto in textos_do_criterio(c):
        for termo in ALIASES:
            for m in re.finditer(r"(?<![\w-])" + re.escape(termo) + r" (?:é|são) ", texto):
                relatorio["manuais"].append((did, c["id"], campo, texto[max(0, m.start() - 40) : m.start() + 160]))


def relatorio_markdown(rel, glossario):
    out = ["# Relatório da migração de definições", ""]
    for titulo, chave, fmt in (
        ("Divergências (texto canônico aplicado; decisão pendente)", "divergencias", "- `{0}` em {1}/{2} ({3}): {4}"),
        ("Normalizações (redação equivalente)", "normalizadas", "- `{0}` em {1}/{2} ({3}): {4}"),
        ("Definições do glossário adicionadas a critérios que não as tinham", "adicionadas", "- `{0}` em {1}/{2}"),
        ("Cláusulas que seguiam um termo do glossário (ver se são locais)", "sobras", "- {0}/{1} ({2}) após `{3}`: {4}"),
        ("Definições locais com texto divergente no mesmo critério", "locais_divergentes", "- {0}/{1} ({2}) `{3}`: {4} ≠ {5}"),
        ("Definições fora de bloco (migração manual)", "manuais", "- {0}/{1} ({2}): …{3}…"),
    ):
        out += [f"## {titulo}", ""]
        itens = rel[chave]
        out += [fmt.format(*i) for i in itens] or ["(nenhuma)"]
        out.append("")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--catalog", default=str(REPO / "catalog"))
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--write", action="store_true")
    g.add_argument("--roundtrip", action="store_true")
    ap.add_argument("--only", default="")
    args = ap.parse_args(argv)
    catalog = Path(args.catalog)
    glossario = load_definicoes(catalog / "definicoes.yaml")
    only = {s.strip() for s in args.only.split(",") if s.strip()}
    rel = defaultdict(list)
    for path in sorted(catalog.glob("D*.yaml")):
        if only and path.stem not in only:
            continue
        d = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not args.roundtrip:
            for c in d["criterios"]:
                migrar_criterio(c, glossario, rel, d["id"])
                _prefixo_menos(c, glossario, d["id"], rel)
        if args.write or args.roundtrip:
            path.write_text(emit_yaml(d), encoding="utf-8")
    if not args.roundtrip:
        print(relatorio_markdown(rel, glossario))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Rodar os testes e o roundtrip**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_definicoes.py -v`
Expected: todos OK.

Run: `python3 scripts/migrate_definicoes.py --roundtrip && git diff --stat catalog/ | tail -1 && python3 -c "import yaml,glob,subprocess; [print(p) for p in sorted(glob.glob('catalog/D*.yaml')) if yaml.safe_load(open(p)) != yaml.safe_load(subprocess.check_output(['git','show','main:'+p]))]"`
Expected: o diff é só de forma (D30–D35 tinham aspas simples; D35 tinha indentação diferente); o comando Python não imprime nenhum arquivo (conteúdo idêntico). Depois: `git checkout catalog/` para descartar o roundtrip.

Run: `python3 scripts/migrate_definicoes.py --dry-run > /tmp/relatorio-migracao.md; wc -l /tmp/relatorio-migracao.md`
Expected: relatório com as seções listadas; as divergências conhecidas aparecem (D31/D33/D34/D35 "atividade" para `missao`; D39 "etapa" para `desafio`; D11 "missão ou desafio"; D13 "missão ou tarefa"; D39 vs D29 para `cenario_jogavel`; D29 "caminho obrigatório, o mesmo que…"; D22 "objetivo de aprendizagem é o listado na documentação"; D22 "documentação é o documento de design…").

- [ ] **Step 5: Commit**

```bash
git add scripts/migrate_definicoes.py tests/test_definicoes.py
git commit -m "feat(scripts): one-shot migration of inline definitions (emitter, extractor, report)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 6: Script de verificação contra a etapa 1

**Files:**
- Create: `scripts/verify_definicoes.py`
- Create: `scripts/definicoes_aceitas.yaml` (vazio de conteúdo nesta task; preenchido na Task 7)
- Modify: `tests/test_definicoes.py` (classe `VerifyTest`)

**Interfaces:**
- Consumes: `extrair_blocos`, `clausulas`, `agrupar`, `normalizar_clausula`, `textos_do_criterio`, `load_definicoes`.
- Produces: `comparar_criterio(antigo, novo, glossario, aceitas) -> list[str]` (lista de diferenças não aceitas, vazia quando tudo bate) e CLI `python3 scripts/verify_definicoes.py [--base main] [--only D28]`, exit 1 se houver diferença não aceita.
- Formato de `scripts/definicoes_aceitas.yaml`:

```yaml
# Diferenças aceitas entre o texto da etapa 1 (git main) e o catálogo com glossário.
# Lido por scripts/verify_definicoes.py. Cada item cita a decisão em
# docs/superpowers/specs/2026-11-03-definicoes-divergencias.md quando tipo == decisao.
clausulas:      # cláusula normalizada da etapa 1 -> cláusula normalizada do novo formato
  - de: "missão = uma atividade com objetivo e condição de conclusão próprios, e o jogo sem divisão em missões conta como uma única missão"
    para: "missão = uma unidade do jogo com objetivo e condição de conclusão próprios (fase, capítulo ou nível, quando têm objetivo e condição de conclusão próprios), e o jogo sem divisão em missões conta como uma única missão"
    tipo: equivalente          # equivalente | decisao
    decisao: null              # número da decisão no documento de divergências
adicoes:        # cláusulas que não existiam na etapa 1
  - criterio: "*"              # "*" = qualquer critério
    chave: documentacao_equivalente
  - criterio: D29.1
    chave: missao
remocoes:       # cláusulas da etapa 1 sem correspondente (ex.: ponteiros "conforme definidos no enunciado")
  - criterio: D28.1
    clausula: "dispositivo = um destes elementos presentes na abertura: pergunta explícita, evento sem desfecho ou informação retida, conforme definidos no enunciado"
campos:         # edições fora das definições
  - criterio: D30.1
    campo: "*"                 # "*" = todos os campos do critério
    remover: ", e missão é uma atividade com objetivo e condição de conclusão próprios, de modo que o jogo sem divisão em missões conta como uma única missão"
  - criterio: D01.1
    campo: video.indicadores[1]
    de: "…"
    para: "…"
```

Regras do comparador, por critério:

1. **Cláusulas.** `O` = conjunto das cláusulas normalizadas de todos os blocos extraídos do texto antigo (mais o que `campos[].remover` removeu, tratado como bloco). `N` = cláusulas normalizadas do novo formato: para cada chave do glossário listada, `"{termo} é {texto}"` dividido em cláusulas (a primeira ganha o termo; as seguintes ficam como estão); para cada local, `"{termo} é {texto}"` idem. Aplicar `clausulas[].de -> para` a `O`. Então `O − N` deve estar contido nas `remocoes` do critério e `N − O` nas `adicoes` do critério (ou `"*"`, comparando pela cláusula canônica da `chave`).
2. **Campos.** Para cada campo de texto: `antigo_sem_defs` = texto antigo após `extrair_blocos` (e após `remover`, se houver). `novo_limpo` = texto novo sem as ocorrências de `, nos termos das definições` e ` nos termos das definições`. Ambos normalizados (espaços colapsados, sem `.;:,` finais). Devem ser iguais, salvo item em `campos` com `de`/`para` que case exatamente.

- [ ] **Step 1: Testes** (acrescentar a `tests/test_definicoes.py`)

```python
from verify_definicoes import comparar_criterio


class VerifyTest(unittest.TestCase):
    def setUp(self):
        from helpers import diretriz_valida
        self.g = load_definicoes(REPO / "catalog" / "definicoes.yaml")
        self.antigo = diretriz_valida()["criterios"][0]
        self.antigo["enunciado"] = "A abertura de cada missão tem um dispositivo; Definições: missão é " + self.g["missao"]["texto"] + "; dispositivo é um elemento da abertura"
        self.antigo["escala"]["parcial"] = "Uma missão tem, outra não. Definição: dispositivo é um elemento da abertura"
        self.novo = diretriz_valida()["criterios"][0]
        self.novo["enunciado"] = "A abertura de cada missão tem um dispositivo"
        self.novo["escala"]["parcial"] = "Uma missão tem, outra não, nos termos das definições"
        self.novo["definicoes"] = {"glossario": ["missao"], "locais": {"dispositivo": "um elemento da abertura"}}
        self.aceitas = {"clausulas": [], "adicoes": [], "remocoes": [], "campos": []}

    def test_equal_after_migration(self):
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_changed_field_text_is_reported(self):
        self.novo["enunciado"] = "A abertura de cada missão tem dois dispositivos"
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("enunciado" in d for d in diffs), diffs)
        self.aceitas["campos"].append({"criterio": "D17.1", "campo": "enunciado", "de": "A abertura de cada missão tem um dispositivo", "para": "A abertura de cada missão tem dois dispositivos"})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_lost_definition_is_reported(self):
        del self.novo["definicoes"]["locais"]
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("dispositivo" in d for d in diffs), diffs)
        self.aceitas["remocoes"].append({"criterio": "D17.1", "clausula": "dispositivo = um elemento da abertura"})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_added_glossary_key_needs_adicao(self):
        self.novo["definicoes"]["glossario"].append("desafio")
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("desafio" in d for d in diffs), diffs)
        self.aceitas["adicoes"].append({"criterio": "*", "chave": "desafio"})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_variant_needs_clausula_mapping(self):
        self.antigo["enunciado"] = self.antigo["enunciado"].replace(self.g["missao"]["texto"], "uma atividade com objetivo próprio")
        diffs = comparar_criterio(self.antigo, self.novo, self.g, self.aceitas)
        self.assertTrue(any("missão = uma atividade" in d for d in diffs), diffs)
        self.aceitas["clausulas"].append({"de": "missão = uma atividade com objetivo próprio", "para": normalizar_clausula("missão é " + self.g["missao"]["texto"]), "tipo": "decisao", "decisao": 1})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])

    def test_remover_in_campos(self):
        self.antigo["escala"]["atendido"] = "Todas orientam, e missão é uma atividade"
        self.novo["escala"]["atendido"] = "Todas orientam"
        self.aceitas["campos"].append({"criterio": "D17.1", "campo": "*", "remover": ", e missão é uma atividade"})
        self.aceitas["clausulas"].append({"de": "missão = uma atividade", "para": normalizar_clausula("missão é " + self.g["missao"]["texto"]), "tipo": "decisao", "decisao": 1})
        self.assertEqual(comparar_criterio(self.antigo, self.novo, self.g, self.aceitas), [])
```

- [ ] **Step 2: Rodar para ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -p test_definicoes.py -v`
Expected: `ModuleNotFoundError: No module named 'verify_definicoes'`.

- [ ] **Step 3: Implementar `scripts/verify_definicoes.py`**

```python
#!/usr/bin/env python3
"""One-shot check: the migrated catalog differs from the stage-1 text only by accepted changes.

Usage: python3 scripts/verify_definicoes.py [--base main] [--only D28,D39]
Reads scripts/definicoes_aceitas.yaml. Exit 1 on any unaccepted difference.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from migrate_definicoes import agrupar, clausulas, extrair_blocos, normalizar_clausula  # noqa: E402
from vygolint_catalog.validate import load_definicoes, textos_do_criterio  # noqa: E402

_PONTEIRO_RE = re.compile(r",? nos termos das definições")


def _norm_campo(s):
    return re.sub(r"\s+", " ", s).strip().rstrip(".;:, ").strip()


def _clausulas_de_corpo(corpo):
    out = []
    for termo, cls in agrupar(clausulas(corpo)):
        out += [normalizar_clausula(c) for c in cls]
    return out


def _clausulas_novas(c, glossario):
    out = set()
    defs = c.get("definicoes") or {}
    for k in defs.get("glossario") or []:
        termo = glossario[k]["termo"].split(" (")[0]
        out |= set(_clausulas_de_corpo(f"{termo} é {glossario[k]['texto']}"))
    for termo, texto in (defs.get("locais") or {}).items():
        out |= set(_clausulas_de_corpo(f"{termo} é {texto}"))
    return out


def _canonica(glossario, chave):
    termo = glossario[chave]["termo"].split(" (")[0]
    return _clausulas_de_corpo(f"{termo} é {glossario[chave]['texto']}")[0]


def _campos_aceitos(aceitas, cid):
    return [a for a in aceitas.get("campos") or [] if a["criterio"] == cid]


def comparar_criterio(antigo, novo, glossario, aceitas):
    cid = novo["id"]
    diffs = []
    mapa = {a["de"]: a["para"] for a in aceitas.get("clausulas") or []}
    campos_ac = _campos_aceitos(aceitas, cid)
    antigos = dict(textos_do_criterio(antigo))
    novos = dict(textos_do_criterio(novo))
    velhas = set()
    for campo, texto in antigos.items():
        for a in campos_ac:
            if "remover" in a and a["campo"] in ("*", campo) and a["remover"] in texto:
                texto = texto.replace(a["remover"], "")
                velhas |= set(_clausulas_de_corpo(a["remover"].strip(" ,;.").removeprefix("e ")))
        sem_defs, blocos = extrair_blocos(texto, cadeia=(campo == "enunciado"))
        for b in blocos:
            velhas |= set(_clausulas_de_corpo(b))
        esperado = _norm_campo(sem_defs)
        obtido = _norm_campo(_PONTEIRO_RE.sub("", novos.get(campo, "")))
        if esperado != obtido:
            ok = any("de" in a and a["campo"] == campo and _norm_campo(a["de"]) == esperado and _norm_campo(a["para"]) == obtido for a in campos_ac)
            if not ok:
                diffs.append(f"{cid} {campo}: texto fora das definições mudou\n  etapa 1: {esperado}\n  agora:   {obtido}")
    velhas = {mapa.get(v, v) for v in velhas}
    novas = _clausulas_novas(novo, glossario)
    remocoes = {a["clausula"] for a in aceitas.get("remocoes") or [] if a["criterio"] == cid}
    adicoes = set()
    for a in aceitas.get("adicoes") or []:
        if a["criterio"] in ("*", cid):
            adicoes.add(_canonica(glossario, a["chave"]) if "chave" in a else a["clausula"])
    for v in sorted(velhas - novas):
        if v not in remocoes:
            diffs.append(f"{cid}: definição da etapa 1 sem correspondente: {v}")
    for n in sorted(novas - velhas):
        if n not in adicoes:
            diffs.append(f"{cid}: definição nova não aceita: {n}")
    return diffs


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default="main")
    ap.add_argument("--only", default="")
    ap.add_argument("--catalog", default=str(REPO / "catalog"))
    args = ap.parse_args(argv)
    catalog = Path(args.catalog)
    glossario = load_definicoes(catalog / "definicoes.yaml")
    aceitas = yaml.safe_load((REPO / "scripts" / "definicoes_aceitas.yaml").read_text(encoding="utf-8")) or {}
    only = {s.strip() for s in args.only.split(",") if s.strip()}
    total = 0
    for path in sorted(catalog.glob("D*.yaml")):
        if only and path.stem not in only:
            continue
        antigo = yaml.safe_load(subprocess.check_output(["git", "-C", str(REPO), "show", f"{args.base}:catalog/{path.name}"]))
        novo = yaml.safe_load(path.read_text(encoding="utf-8"))
        velhos = {c["id"]: c for c in antigo["criterios"]}
        for c in novo["criterios"]:
            for d in comparar_criterio(velhos[c["id"]], c, glossario, aceitas):
                print(d)
                total += 1
    print(f"{total} diferença(s) não aceita(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
```

`scripts/definicoes_aceitas.yaml` nesta task contém só o cabeçalho comentado e as quatro listas vazias (`clausulas: []`, `adicoes: []`, `remocoes: []`, `campos: []`).

- [ ] **Step 4: Rodar para ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v`
Expected: todos OK.

- [ ] **Step 5: Commit**

```bash
git add scripts/verify_definicoes.py scripts/definicoes_aceitas.yaml tests/test_definicoes.py
git commit -m "feat(scripts): verify migrated definitions against stage-1 text, with accepted-diff list

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 7: Migrar os 40 arquivos (três lotes em paralelo, mesmo procedimento)

Lotes: **7a** D01–D13, **7b** D14–D27, **7c** D28–D40. Cada lote é um subagente; os três compartilham `catalog/definicoes.yaml` (somente leitura: NÃO editar; candidatos a termo novo vão para o relatório do lote) e `scripts/definicoes_aceitas.yaml` (cada lote acrescenta só itens dos seus critérios; `clausulas` é global: antes de acrescentar, verificar se já existe item com o mesmo `de`).

**Files:**
- Modify: `catalog/Dnn.yaml` do lote
- Modify: `scripts/definicoes_aceitas.yaml` (acrescentar itens)
- Create: `.superpowers/sdd/definicoes-lote-<a|b|c>.md` (relatório do lote: decisões pendentes encontradas, com termo, variante, arquivos, e proposta de redação canônica)

**Interfaces:**
- Consumes: `migrate_definicoes.py --write --only …`, `verify_definicoes.py --only …`, `build_catalog.py`.
- Produces: arquivos migrados que passam no lint e no verificador.

Procedimento por lote:

- [ ] **Step 1: Migração mecânica**

Run: `python3 scripts/migrate_definicoes.py --write --only D28,D29,…` (ids do lote). Ler o relatório impresso e guardar em `.superpowers/sdd/definicoes-lote-X.md`.

- [ ] **Step 2: Revisar cada arquivo contra a etapa 1**

Para cada `Dnn.yaml` do lote, comparar `git show main:catalog/Dnn.yaml` com o arquivo migrado e aplicar à mão:

1. `definicoes.locais`: conferir que cada termo local ficou com chave legível (`"abertura da missão"`, não `"a missão aceita dois ou mais jogadores"` quando puder ser `"missão que aceita dois ou mais jogadores"`; ao renomear a chave, manter o texto e registrar em `remocoes` + `adicoes` do critério as duas cláusulas) e com o texto completo (incluindo as cláusulas seguintes que o relatório listou em "sobras", quando pertencem ao termo). Texto de local começa pelo predicado (`"um destes elementos…"`), nunca por `"termo é"`.
2. Definições fora de bloco (seção "migração manual" do relatório, mais D01 inteiro, D05, D11, D25, D30): remover do texto a oração de definição e registrar em `campos` com `remover` (ou `de`/`para` quando a frase precisa de reescrita mínima). D01: o enunciado vira `"Cada missão ou minijogo apresenta uma situação-problema cuja resolução exige uma decisão do jogador, e não apenas a repetição de uma mesma ação"`; os procedimentos perdem a frase `"Situação-problema exige … não conta"`; o indicador de vídeo com `"estado inicial visível, objetivo e mais de uma ação disponível ao jogador"` NÃO muda (fica como está e vira decisão no relatório).
3. Gatilho usado no sentido corrente (ex.: `cenário` em D02 "missão ou cenário", D12 "(cenário, inventário ou lista)", D23 "mudança no cenário", D30 "cenário ou enredo fictício", D32 "cenário, neste critério, é o ambiente…", D38 "elemento do cenário"): trocar a chave `cenario_jogavel` que a migração adicionou por `termos_comuns: {cenário: "<justificativa de uma frase>"}`, e registrar em `adicoes` nada (termos_comuns não gera cláusula). Se o arquivo define `cenário` localmente (D32), manter como local e usar `termos_comuns` para silenciar o gatilho.
4. Onde o texto ficou truncado ou sem antecedente depois da remoção (ex.: escala que dizia "conforme definidos no enunciado"), acrescentar `, nos termos das definições` (único ponteiro permitido) e nada mais.
5. Divergências de termo do glossário (seção "Divergências" do relatório): não alterar o glossário; acrescentar em `clausulas` o par `de`/`para` com `tipo: decisao` e `decisao: <n>` (numerar sequencialmente dentro do lote como `a1, a2…`, `b1…`, `c1…`; a Task 8 renumera) ou `tipo: equivalente` quando a redação só muda forma. São equivalentes, sem decisão: "atividade com objetivo e condição de conclusão próprios" → texto de D28 (missão); "de modo que o jogo sem divisão" (D30); "cenário jogável" de D39 → texto de D29; "caminho obrigatório, o mesmo que caminho da missão em D05, é a sequência de objetivos exigidos para completar a missão em curso no cenário, e fora do caminho obrigatório é tudo o que nenhum desses objetivos exige" → texto de D05; "caminho da missão é a sequência de objetivos exigidos para completá-la" → idem; "objetivos de aprendizagem são os listados no documento de design (GDD) ou documento equivalente" → texto de D31. São decisões: `desafio` de D39 ("etapa"), de D11 ("missão ou desafio é uma unidade…"), de D13 ("missão ou tarefa"); `objetivo de aprendizagem é o listado na documentação` (D22); `documentação` de D22; `estado inicial visível` (D01); qualquer outra que mude extensão ou condição.
6. Adições: toda chave do glossário que a migração adicionou (seção "adicionadas") entra em `adicoes` com `criterio: <id>` e `chave`; para `documentacao_equivalente` usar um único item `criterio: "*"` (lote 7a cria; os outros não duplicam).

- [ ] **Step 3: Validar o lote**

Run: `python3 scripts/verify_definicoes.py --only D28,D29,…` até `0 diferença(s) não aceita(s)`.
Run: `python3 - <<'EOF'` com um laço que carrega `schema.yaml`, `categorias.yaml`, o glossário e chama `validate_diretriz` nos arquivos do lote, imprimindo erros; repetir até zero erros do lote (o build completo ainda falha por causa dos outros lotes).

```python
import sys, yaml, glob
sys.path.insert(0, "scripts")
from vygolint_catalog.validate import load_yaml, load_definicoes, validate_diretriz
schema = load_yaml("catalog/schema.yaml"); cats = load_yaml("catalog/categorias.yaml"); g = load_definicoes("catalog/definicoes.yaml")
for p in ["catalog/D28.yaml", "catalog/D29.yaml"]:
    for e in validate_diretriz(load_yaml(p), schema, cats, g): print(e)
EOF
```

- [ ] **Step 4: Relatório do lote**

Escrever `.superpowers/sdd/definicoes-lote-X.md` com: (1) decisões pendentes (termo, variante da etapa 1, arquivos, redação canônica aplicada, o que muda de significado); (2) normalizações aplicadas; (3) termos candidatos a glossário (definidos localmente em 2+ arquivos do lote com texto igual ou quase igual, ex.: `informação` em D11/D36, `objeto interativo` em D32/D38, `narrativa` em D23/D28, `jogador` em D13/D26/D27, `referente real` em D30/D31); (4) `termos_comuns` usados.

- [ ] **Step 5: Commit do lote**

```bash
git add catalog/D28.yaml … scripts/definicoes_aceitas.yaml
git commit -m "refactor(catalog): move inline definitions of D28-D40 to definicoes field

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

Depois dos três lotes (controlador):

- [ ] **Step 6: Build completo, verificação completa e docs**

Run: `python3 scripts/verify_definicoes.py && python3 scripts/build_catalog.py && PYTHONPATH=scripts python3 -m unittest discover -s tests -v`
Expected: `0 diferença(s) não aceita(s)`, `OK: 40 diretrizes, 43 critérios`, testes OK.

Run: `awk '{ if (length($0) > 1500) print FILENAME": "length($0) }' docs/catalogo.md | head; grep -c "Definições:" catalog/D*.yaml | grep -v ":0"`
Expected: nenhuma linha acima de 1.500 e nenhum `Definições:` restante. Se sobrar linha longa, é procedimento com "Regra de desempate" extenso: aceitar e anotar no relatório (não reescrever texto).

```bash
git add docs/catalogo.md docs/catalogo.tex
git commit -m "docs: regenerate catalog with definitions blocks

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 8: Documento de divergências e decisões pendentes

**Files:**
- Create: `docs/superpowers/specs/2026-11-03-definicoes-divergencias.md`
- Modify: `scripts/definicoes_aceitas.yaml` (renumerar `decisao:` para bater com o documento)

- [ ] **Step 1: Consolidar os três relatórios de lote** (`.superpowers/sdd/definicoes-lote-*.md`) em um documento com esta estrutura:

```markdown
# Definições compartilhadas — divergências encontradas e decisões pendentes

Data: 2026-11-03. Origem: migração do catálogo para `catalog/definicoes.yaml` (plano `docs/superpowers/plans/2026-11-03-definicoes-glossario.md`). Enquanto uma decisão está pendente, o catálogo usa a redação do arquivo âncora, indicada em cada item. A lista legível por máquina está em `scripts/definicoes_aceitas.yaml`.

## 1. Decisões pendentes

### Decisão 1 — `desafio`: incluir "etapa com condição de conclusão própria"?
- Âncora aplicada: D19 — "cada missão ou minijogo".
- Variante: D39 — "uma unidade do jogo com objetivo e condição de conclusão próprios (missão, minijogo ou etapa com condição de conclusão própria), e o jogo sem divisão em missões conta como uma única missão".
- O que muda: em D39 uma etapa dentro de uma missão contava como desafio; com a âncora, só missão ou minijogo contam. Afeta o grau quando o único desafio que exige detalhe é uma etapa.
- Arquivos afetados: D39.
- Proposta: …

### Decisão 2 — …
```

Itens obrigatórios: `desafio` (D39 etapa; D11 "missão ou desafio é uma unidade…"; D13 "missão ou tarefa"), `objetivo_de_aprendizagem` (D22 "o listado na documentação"), `documentacao_equivalente` (texto novo; D22 "documentação" incluía guia do professor e plano de aula), `sessao_de_jogo` (texto novo), `minijogo` (definição de D37 passa a valer nos 15 arquivos que usam o termo sem definir), `situacao_problema` em D01 (indicador de vídeo "estado inicial visível … ação disponível" vs enunciado "estado inicial … ação possível"), mais tudo o que os lotes marcaram como decisão.

Seções seguintes: `## 2. Normalizações aplicadas sem decisão (redação equivalente)` (tabela termo | variante | âncora | arquivos); `## 3. Definições adicionadas a critérios que não as tinham` (D29 missão; D36 e D40 missão/desafio; documentacao_equivalente em todos; etc.); `## 4. Termos usados no sentido corrente (termos_comuns)`; `## 5. Candidatos a novos termos do glossário` (não migrados nesta PR).

- [ ] **Step 2: Renumerar `decisao:` em `definicoes_aceitas.yaml`** para os números do documento e rodar `python3 scripts/verify_definicoes.py` (continua `0 diferença(s)`).

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/specs/2026-11-03-definicoes-divergencias.md scripts/definicoes_aceitas.yaml
git commit -m "docs(spec): divergences found in shared definitions and pending decisions

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 9: Documentação do novo formato e fechamento dos itens menores

**Files:**
- Modify: `docs/superpowers/specs/2026-11-03-catalogo-conformidade-design.md` (seção 5)
- Modify: `docs/conformidade.md` (nova seção "Definições")
- Modify: `README.md`
- Modify: `.superpowers/sdd/authoring-rules.md` (regras 11 e 17) e `.superpowers/sdd/progress.md` (não versionados; editar mesmo assim)

- [ ] **Step 1: Spec, seção 5.** No exemplo YAML de D17 acrescentar, depois de `depende_de: []`:

```yaml
    definicoes:                # opcional; obrigatório quando o texto usa um gatilho do glossário
      glossario: [missao]      # chaves de catalog/definicoes.yaml, impressas uma vez por critério
      locais:                  # definições só deste critério: termo -> texto (predicado, sem "termo é")
        "ponto de feedback": "o momento em que o jogo responde a uma ação avaliada"
      termos_comuns:           # gatilho usado no sentido corrente, com justificativa
        "cenário": "sentido corrente de situação; não é o cenário jogável do glossário"
```

E nas "Regras do esquema" acrescentar:

- Definição compartilhada existe uma vez, em `catalog/definicoes.yaml` (`chave`, `termo`, `gatilhos`, `ancora`, `texto`). O texto de um critério (enunciado, procedimentos, indicadores, escala) não repete definições: contém `Definições:` ou o texto de um termo do glossário é erro de build.
- Lint: se o texto de um critério contém um gatilho de um termo do glossário, `definicoes.glossario` precisa listar a chave (ou `termos_comuns` precisa justificar o uso no sentido corrente). Chave listada sem gatilho no texto também é erro. O texto das definições listadas conta como texto do critério (uma definição que cita "missão" exige `missao`).
- O renderizador imprime `**Definições.**` uma vez por critério, antes do enunciado, e uma seção `## Glossário` no início de `docs/catalogo.md`.
- Divergências de redação encontradas na migração e decisões pendentes: `docs/superpowers/specs/2026-11-03-definicoes-divergencias.md`.

Na seção 4 (pastas), acrescentar `definicoes.yaml` em `catalog/`. No status do topo: "glossário de definições (2026-11-03)".

- [ ] **Step 2: `docs/conformidade.md`.** Acrescentar, antes de "## 3. Diretriz", a seção:

```markdown
## 2a. Definições

Todo termo que decide o grau de um critério tem definição apontável. As compartilhadas
(missão, minijogo, desafio, cenário jogável, caminho obrigatório, situação-problema,
GDD ou documento equivalente, objetivo de aprendizagem, sessão de jogo) existem uma
vez em `catalog/definicoes.yaml` e aparecem no bloco **Definições** de cada critério que
as usa; as específicas de um critério ficam em `definicoes.locais`. O avaliador aplica
a definição impressa no critério, igual para código, documentação e vídeo. Uma palavra
marcada como "sentido corrente" não carrega a definição do glossário.
```

- [ ] **Step 3: README.** Na tabela "O que há aqui", acrescentar a linha `| catalog/definicoes.yaml | glossário: definições compartilhadas pelos critérios, impressas uma vez por critério |` logo depois de `schema.yaml`. Em "Documentos de projeto", acrescentar `- Divergências de definições: docs/superpowers/specs/2026-11-03-definicoes-divergencias.md` e `- Plano do glossário: docs/superpowers/plans/2026-11-03-definicoes-glossario.md`.

- [ ] **Step 4: Regras de autoria (local).** Em `.superpowers/sdd/authoring-rules.md`, reescrever a regra 11: "A definição operacional de um termo existe uma vez: no glossário (`catalog/definicoes.yaml`) se compartilhada, em `definicoes.locais` se própria do critério. Enunciado, procedimentos, indicadores e escala usam o termo e, quando preciso, `nos termos das definições`; nunca repetem o texto. O build falha se repetirem." E a regra 17: "Todo critério cujo texto usa missão, minijogo, desafio, cenário, caminho obrigatório/caminho da missão, situação-problema, GDD/documento equivalente, objetivo de aprendizagem ou sessão de jogo lista a chave correspondente em `definicoes.glossario` (o lint exige); `termos_comuns` só quando a palavra está no sentido corrente, com justificativa." Em `progress.md`, acrescentar: "STAGE 2 / Task 0 (glossário): concluída em <commit>; fechados: D29/D36/D40 sem definição de missão/desafio (lint exige agora), D04 'GDD' vs 'GDD ou documento equivalente' (gatilho GDD resolve em `documentacao_equivalente`), D29 parcial/atendido sem definição de incentivo (bloco único por critério)."

- [ ] **Step 5: Testes, build, commit**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v && python3 scripts/build_catalog.py && git status --short`
Expected: testes OK, `OK: 40 diretrizes, 43 critérios`, e `git status` mostra só os docs editados (docs gerados sem mudança).

```bash
git add README.md docs/conformidade.md docs/superpowers/specs/2026-11-03-catalogo-conformidade-design.md
git commit -m "docs: describe the definitions glossary in spec, conformance rules and README

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 10: PR

- [ ] **Step 1:** `git push -u origin definicoes-glossario`
- [ ] **Step 2:** `gh pr create --base main --title "Shared definitions glossary for the catalog" --body-file <arquivo>` com corpo: objetivo, o que muda no esquema, como verificar (`verify_definicoes.py`), link para o documento de divergências com a contagem de decisões pendentes, e a linha final `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- [ ] **Step 3:** Confirmar CI verde (`gh pr checks --watch`).
