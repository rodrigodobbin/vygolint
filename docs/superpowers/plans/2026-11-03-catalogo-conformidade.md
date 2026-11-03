# Catálogo de conformidade vygolint — Plano de implementação (etapa 1)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transformar as 40 diretrizes de Carvalho (2020) em um catálogo YAML de critérios testáveis com níveis A/AA/AAA, validado por script e renderizado em Markdown e LaTeX.

**Architecture:** Um arquivo YAML por diretriz em `catalog/`, validado contra `catalog/schema.yaml` por um pacote Python pequeno em `scripts/vygolint_catalog/` (níveis, validação, renderização). `scripts/build_catalog.py` é o ponto de entrada: valida tudo, recalcula níveis e gera `docs/catalogo.md` e `docs/catalogo.tex`. CI roda testes, build e exige docs sincronizados.

**Tech Stack:** Python 3.13 (3.11+ serve), PyYAML, `unittest` da biblioteca padrão, GitHub Actions.

Spec: `docs/superpowers/specs/2026-11-03-catalogo-conformidade-design.md`.

## Global Constraints

- Texto de cada diretriz é literal do Quadro 3 de Carvalho (2020). Hifenização de quebra de linha do PDF deve ser removida (`con- texto` vira `contexto`).
- Ids de diretriz com dois dígitos: `D01` … `D40`. Ids de critério: `Dnn.k`, `k` de 1 a 9.
- Nível de critério nunca é escolhido à mão: sai de `derive_nivel(essencialidade, viabilidade, modalidade)` e o build falha se o YAML divergir.
- `modalidade: pode` apenas em D20 e D21.
- `aplicabilidade` não nula apenas em D22.
- Todo critério tem ao menos uma fonte de evidência não nula. Descritores de escala são observáveis; proibido "o jogo é motivador".
- Não existe "não se aplica" por ausência de recurso.
- `docs/catalogo.md` e `docs/catalogo.tex` são gerados; nunca editar à mão.
- Saída do build é determinística: diretrizes ordenadas por id, sem data ou hora.
- Comandos de teste: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v`. Build: `python3 scripts/build_catalog.py`.
- Todo commit termina com a linha `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
- Idioma dos arquivos de catálogo e docs: português. Código, nomes de função e mensagens de commit: inglês.

## File Structure

```
vygolint/
  .github/workflows/ci.yml          # testes + build + diff de docs
  .gitignore
  README.md
  requirements.txt                  # pyyaml
  catalog/
    schema.yaml                     # campos obrigatórios, enums, padrões de id
    categorias.yaml                 # 12 categorias + ressalva de Carvalho
    D01.yaml … D40.yaml
  docs/
    catalogo.md                     # gerado
    catalogo.tex                    # gerado
    conformidade.md                 # regras de nível e agregação
  scripts/
    build_catalog.py                # entrada CLI; chama vygolint_catalog.build
    vygolint_catalog/
      __init__.py
      levels.py                     # derive_nivel
      validate.py                   # load_yaml, validate_diretriz, validate_catalogo
      render.py                     # render_markdown, render_latex, escape_latex
      build.py                      # build(catalog_dir, docs_dir) -> list[str]
  tests/
    helpers.py                      # diretriz_valida(), categorias_validas(), schema_valido()
    test_levels.py
    test_validate.py
    test_render.py
    test_build.py
```

Responsabilidades: `levels.py` só conhece a tabela de níveis. `validate.py` só conhece o esquema e as regras de coerência. `render.py` só transforma dicionários em texto. `build.py` orquestra e faz I/O. Nada importa de `build.py` exceto a CLI.

---

### Task 1: Esqueleto do repositório e harness de testes

**Files:**
- Create: `.gitignore`, `requirements.txt`, `README.md`, `scripts/vygolint_catalog/__init__.py`, `tests/test_smoke.py`

**Interfaces:**
- Produces: pacote importável `vygolint_catalog` com `__version__ = "0.1.0"`.

- [ ] **Step 1: Criar ambiente e dependência**

```bash
cd ~/projects/personal/vygolint
python3 -m venv .venv
source .venv/bin/activate
printf 'pyyaml>=6.0\n' > requirements.txt
pip install -r requirements.txt
```

Expected: `Successfully installed PyYAML-6.x`.

- [ ] **Step 2: Escrever `.gitignore`**

```
.venv/
__pycache__/
*.pyc
.DS_Store
```

- [ ] **Step 3: Escrever o teste de fumaça**

`tests/test_smoke.py`:

```python
import unittest


class SmokeTest(unittest.TestCase):
    def test_package_imports(self):
        import vygolint_catalog

        self.assertEqual(vygolint_catalog.__version__, "0.1.0")

    def test_yaml_available(self):
        import yaml

        self.assertEqual(yaml.safe_load("a: 1"), {"a": 1})
```

- [ ] **Step 4: Rodar e ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v`
Expected: `ModuleNotFoundError: No module named 'vygolint_catalog'`

- [ ] **Step 5: Criar o pacote**

`scripts/vygolint_catalog/__init__.py`:

```python
"""Validation and rendering of the vygolint conformance catalog."""

__version__ = "0.1.0"
```

- [ ] **Step 6: Rodar e ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v`
Expected: `Ran 2 tests ... OK`

- [ ] **Step 7: README inicial**

`README.md`:

```markdown
# vygolint

Catálogo de conformidade e plugin de avaliação de jogos educacionais digitais
contra as 40 diretrizes sociointeracionistas de Carvalho (2020), com níveis
A, AA e AAA no modelo das WCAG.

Etapa 1 (em andamento): catálogo em `catalog/`, build em `scripts/`.
Etapa 2 (futura): skills portáveis em `skills/`.

## Desenvolvimento

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=scripts python3 -m unittest discover -s tests -v
python3 scripts/build_catalog.py
```

Spec: `docs/superpowers/specs/2026-11-03-catalogo-conformidade-design.md`.
```

- [ ] **Step 8: Commit**

```bash
git add .gitignore requirements.txt README.md scripts/vygolint_catalog/__init__.py tests/test_smoke.py
git commit -m "chore: scaffold catalog package and test harness" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 2: Tabela de níveis (`levels.py`)

**Files:**
- Create: `scripts/vygolint_catalog/levels.py`, `tests/test_levels.py`

**Interfaces:**
- Produces: `derive_nivel(essencialidade: str, viabilidade: str, modalidade: str = "deve") -> str` retornando `"A" | "AA" | "AAA"`; levanta `ValueError` para valores fora dos enums. Constantes `ESSENCIALIDADES = ("alta", "media", "baixa")`, `VIABILIDADES = ("alta", "media", "baixa")`, `MODALIDADES = ("deve", "pode")`, `NIVEIS = ("A", "AA", "AAA")`.

- [ ] **Step 1: Escrever os testes**

`tests/test_levels.py`:

```python
import unittest

from vygolint_catalog.levels import derive_nivel


class DeriveNivelTest(unittest.TestCase):
    def test_table_all_nine_combinations(self):
        expected = {
            ("alta", "alta"): "A",
            ("alta", "media"): "A",
            ("alta", "baixa"): "AA",
            ("media", "alta"): "AA",
            ("media", "media"): "AA",
            ("media", "baixa"): "AAA",
            ("baixa", "alta"): "AAA",
            ("baixa", "media"): "AAA",
            ("baixa", "baixa"): "AAA",
        }
        for (ess, via), nivel in expected.items():
            with self.subTest(ess=ess, via=via):
                self.assertEqual(derive_nivel(ess, via), nivel)

    def test_pode_never_yields_a(self):
        self.assertEqual(derive_nivel("alta", "alta", "pode"), "AA")
        self.assertEqual(derive_nivel("alta", "media", "pode"), "AA")

    def test_pode_keeps_aa_and_aaa(self):
        self.assertEqual(derive_nivel("media", "alta", "pode"), "AA")
        self.assertEqual(derive_nivel("baixa", "alta", "pode"), "AAA")

    def test_invalid_values_raise(self):
        with self.assertRaises(ValueError):
            derive_nivel("altissima", "alta")
        with self.assertRaises(ValueError):
            derive_nivel("alta", "nenhuma")
        with self.assertRaises(ValueError):
            derive_nivel("alta", "alta", "talvez")
```

- [ ] **Step 2: Rodar e ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_levels -v`
Expected: `ModuleNotFoundError: No module named 'vygolint_catalog.levels'`

- [ ] **Step 3: Implementar**

`scripts/vygolint_catalog/levels.py`:

```python
"""Conformance level derivation (spec section 6)."""

ESSENCIALIDADES = ("alta", "media", "baixa")
VIABILIDADES = ("alta", "media", "baixa")
MODALIDADES = ("deve", "pode")
NIVEIS = ("A", "AA", "AAA")

_TABELA = {
    ("alta", "alta"): "A",
    ("alta", "media"): "A",
    ("alta", "baixa"): "AA",
    ("media", "alta"): "AA",
    ("media", "media"): "AA",
    ("media", "baixa"): "AAA",
    ("baixa", "alta"): "AAA",
    ("baixa", "media"): "AAA",
    ("baixa", "baixa"): "AAA",
}


def derive_nivel(essencialidade: str, viabilidade: str, modalidade: str = "deve") -> str:
    """Return the level a criterion must have given its two axes and modality."""
    if essencialidade not in ESSENCIALIDADES:
        raise ValueError(f"essencialidade invalida: {essencialidade!r}")
    if viabilidade not in VIABILIDADES:
        raise ValueError(f"viabilidade invalida: {viabilidade!r}")
    if modalidade not in MODALIDADES:
        raise ValueError(f"modalidade invalida: {modalidade!r}")
    nivel = _TABELA[(essencialidade, viabilidade)]
    if modalidade == "pode" and nivel == "A":
        return "AA"
    return nivel
```

- [ ] **Step 4: Rodar e ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_levels -v`
Expected: `Ran 4 tests ... OK`

- [ ] **Step 5: Commit**

```bash
git add scripts/vygolint_catalog/levels.py tests/test_levels.py
git commit -m "feat: derive conformance level from essentiality and feasibility" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 3: Esquema, categorias e validação estrutural de uma diretriz

**Files:**
- Create: `catalog/schema.yaml`, `catalog/categorias.yaml`, `scripts/vygolint_catalog/validate.py`, `tests/helpers.py`, `tests/test_validate.py`

**Interfaces:**
- Consumes: nada de tarefas anteriores além do pacote.
- Produces:
  - `load_yaml(path: str | Path) -> Any`
  - `validate_diretriz(d: dict, schema: dict, categorias: dict) -> list[str]` (lista vazia = válida; cada erro começa com o id da diretriz ou `"?"` quando ausente)
  - `schema` é o dict carregado de `schema.yaml`; `categorias` é o dict carregado de `categorias.yaml` (chaves `ressalva` e `categorias`).

- [ ] **Step 1: Escrever `catalog/schema.yaml`**

```yaml
# Esquema do catálogo vygolint. Lido por scripts/vygolint_catalog/validate.py.
diretriz:
  obrigatorios: [id, categoria, diretriz, fonte, modalidade, aplicabilidade, criterios]
  id_padrao: '^D(0[1-9]|[1-3][0-9]|40)$'
  modalidade: [deve, pode]
criterio:
  obrigatorios: [id, nivel, enunciado, nivel_justificativa, evidencia, escala, depende_de]
  id_padrao: '^D(0[1-9]|[1-3][0-9]|40)\.[1-9]$'
  nivel: [A, AA, AAA]
  essencialidade: [alta, media, baixa]
  viabilidade: [alta, media, baixa]
  fontes_evidencia: [codigo, documentacao, video]
  escala: [atendido, parcial, nao_atendido]
```

- [ ] **Step 2: Escrever `catalog/categorias.yaml`**

```yaml
# Categorias usadas por Carvalho (2020) para organizar as 40 diretrizes.
ressalva: >-
  Carvalho (2020, seção 4.4) suprimiu as categorias na apresentação final das
  diretrizes por considerar que rotular, classificar e ordenar requisitos pode
  gerar a falsa impressão de que a teoria de Vigotski também pode ser
  classificada assim. O vygolint usa as categorias apenas como instrumento de
  organização e de relatório, não como taxonomia da teoria.
categorias:
  - chave: interacao
    nome: Interação
    descricao: Ação do jogador sobre objetos, mecanismos e outros jogadores; base da aprendizagem como atividade.
  - chave: mediacao
    nome: Mediação
    descricao: Apoio que aproxima o jogador do que ainda não faz sozinho (zona de desenvolvimento proximal), por feedback, pistas, pares ou professor.
  - chave: autonomia
    nome: Autonomia
    descricao: Decisões do jogador sobre recursos e conteúdos; jogador no centro do processo.
  - chave: socializacao
    nome: Socialização
    descricao: Aproximação entre jogadores por competição ou colaboração.
  - chave: ludico
    nome: Lúdico
    descricao: Curiosidade e motivação despertadas pela narrativa e pelos desafios.
  - chave: realismo
    nome: Realismo
    descricao: Situações, contextos e objetos ligados ao mundo real e ao cotidiano do jogador.
  - chave: personalizacao
    nome: Personalização
    descricao: Adaptação dos desafios ao desempenho e às ações do jogador; criação de desafios pelo jogador.
  - chave: organizacao
    nome: Organização
    descricao: Organização de informações pelo jogador.
  - chave: resolucao_de_problemas
    nome: Resolução de problemas
    descricao: Apresentação explícita da situação-problema.
  - chave: linguagem
    nome: Linguagem
    descricao: Informação escrita fornecida ao jogador.
  - chave: atencao
    nome: Atenção
    descricao: Percepção de detalhes exigida pelo mundo do jogo.
  - chave: aprendizado
    nome: Aprendizado
    descricao: Aprendizagem a partir dos erros, com mensagens, sons e animações.
```

- [ ] **Step 3: Escrever `tests/helpers.py`**

```python
"""Shared fixtures for catalog tests. Every function returns a fresh copy."""

import copy
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent


def schema_valido():
    return yaml.safe_load((REPO / "catalog" / "schema.yaml").read_text(encoding="utf-8"))


def categorias_validas():
    return yaml.safe_load((REPO / "catalog" / "categorias.yaml").read_text(encoding="utf-8"))


_DIRETRIZ = {
    "id": "D17",
    "categoria": "mediacao",
    "diretriz": "O jogo deve exibir feedback construtivo para as ações do jogador",
    "fonte": "Carvalho (2020), Quadro 3",
    "modalidade": "deve",
    "aplicabilidade": None,
    "criterios": [
        {
            "id": "D17.1",
            "nivel": "A",
            "enunciado": "Toda ação incorreta do jogador recebe mensagem que indica o que fazer, não só que errou",
            "nivel_justificativa": {
                "essencialidade": "alta",
                "viabilidade": "alta",
                "texto": "Mediação é núcleo da ZDP; feedback que só sinaliza acerto/erro é reforço behaviorista.",
            },
            "evidencia": {
                "codigo": {
                    "procedimento": "Localizar tratadores de erro e verificar o texto exibido",
                    "indicadores": ["mensagem contém orientação de próxima ação"],
                },
                "documentacao": None,
                "video": {
                    "procedimento": "Registrar timestamp de cada erro e classificar o feedback",
                    "indicadores": ["ao menos 3 ocorrências de erro", "cada ocorrência mostra orientação"],
                },
            },
            "escala": {
                "atendido": "Todas as ocorrências observadas orientam o jogador",
                "parcial": "Algumas ocorrências orientam, outras só sinalizam erro",
                "nao_atendido": "Feedback só sinaliza acerto/erro ou inexiste",
            },
            "depende_de": [],
        }
    ],
}


def diretriz_valida():
    return copy.deepcopy(_DIRETRIZ)
```

- [ ] **Step 4: Escrever os testes de validação estrutural**

`tests/test_validate.py`:

```python
import unittest

from helpers import categorias_validas, diretriz_valida, schema_valido
from vygolint_catalog.validate import validate_diretriz


class ValidateDiretrizTest(unittest.TestCase):
    def setUp(self):
        self.schema = schema_valido()
        self.categorias = categorias_validas()

    def check(self, d):
        return validate_diretriz(d, self.schema, self.categorias)

    def test_valid_diretriz_has_no_errors(self):
        self.assertEqual(self.check(diretriz_valida()), [])

    def test_missing_required_field(self):
        d = diretriz_valida()
        del d["fonte"]
        errors = self.check(d)
        self.assertEqual(len(errors), 1)
        self.assertIn("D17", errors[0])
        self.assertIn("fonte", errors[0])

    def test_bad_diretriz_id(self):
        d = diretriz_valida()
        d["id"] = "D7"
        self.assertTrue(any("id" in e for e in self.check(d)))

    def test_unknown_categoria(self):
        d = diretriz_valida()
        d["categoria"] = "magia"
        self.assertTrue(any("categoria" in e for e in self.check(d)))

    def test_bad_modalidade(self):
        d = diretriz_valida()
        d["modalidade"] = "talvez"
        self.assertTrue(any("modalidade" in e for e in self.check(d)))

    def test_aplicabilidade_must_be_null_or_text(self):
        d = diretriz_valida()
        d["aplicabilidade"] = ""
        self.assertTrue(any("aplicabilidade" in e for e in self.check(d)))
        d["aplicabilidade"] = "Somente quando aplicado em sala de aula"
        self.assertEqual(self.check(d), [])

    def test_criterios_must_be_non_empty_list(self):
        d = diretriz_valida()
        d["criterios"] = []
        self.assertTrue(any("criterios" in e for e in self.check(d)))

    def test_criterio_missing_field(self):
        d = diretriz_valida()
        del d["criterios"][0]["escala"]
        errors = self.check(d)
        self.assertTrue(any("D17.1" in e and "escala" in e for e in errors))

    def test_criterio_id_must_match_diretriz(self):
        d = diretriz_valida()
        d["criterios"][0]["id"] = "D18.1"
        self.assertTrue(any("D18.1" in e for e in self.check(d)))

    def test_criterio_bad_nivel(self):
        d = diretriz_valida()
        d["criterios"][0]["nivel"] = "B"
        self.assertTrue(any("nivel" in e for e in self.check(d)))

    def test_justificativa_enums_and_text(self):
        d = diretriz_valida()
        d["criterios"][0]["nivel_justificativa"]["essencialidade"] = "enorme"
        self.assertTrue(any("essencialidade" in e for e in self.check(d)))
        d = diretriz_valida()
        d["criterios"][0]["nivel_justificativa"]["texto"] = ""
        self.assertTrue(any("texto" in e for e in self.check(d)))

    def test_evidencia_requires_all_three_keys(self):
        d = diretriz_valida()
        del d["criterios"][0]["evidencia"]["documentacao"]
        self.assertTrue(any("documentacao" in e for e in self.check(d)))

    def test_evidencia_at_least_one_source(self):
        d = diretriz_valida()
        for k in ("codigo", "documentacao", "video"):
            d["criterios"][0]["evidencia"][k] = None
        self.assertTrue(any("evidencia" in e for e in self.check(d)))

    def test_evidencia_source_shape(self):
        d = diretriz_valida()
        d["criterios"][0]["evidencia"]["codigo"] = {"procedimento": "x", "indicadores": []}
        self.assertTrue(any("indicadores" in e for e in self.check(d)))
        d = diretriz_valida()
        d["criterios"][0]["evidencia"]["codigo"] = {"indicadores": ["a"]}
        self.assertTrue(any("procedimento" in e for e in self.check(d)))

    def test_escala_requires_three_non_empty_descriptors(self):
        d = diretriz_valida()
        d["criterios"][0]["escala"]["parcial"] = ""
        self.assertTrue(any("parcial" in e for e in self.check(d)))
        d = diretriz_valida()
        del d["criterios"][0]["escala"]["nao_atendido"]
        self.assertTrue(any("nao_atendido" in e for e in self.check(d)))

    def test_depende_de_must_be_list_of_lists_of_ids(self):
        d = diretriz_valida()
        d["criterios"][0]["depende_de"] = ["D06.1"]
        self.assertTrue(any("depende_de" in e for e in self.check(d)))
        d = diretriz_valida()
        d["criterios"][0]["depende_de"] = [["D06.1", "D07.1"]]
        self.assertEqual(self.check(d), [])
```

- [ ] **Step 5: Rodar e ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_validate -v`
Expected: `ModuleNotFoundError: No module named 'vygolint_catalog.validate'`

- [ ] **Step 6: Implementar `validate.py`**

`scripts/vygolint_catalog/validate.py`:

```python
"""Structural and cross-file validation of catalog YAML (spec sections 5 and 6)."""

import re
from pathlib import Path

import yaml


def load_yaml(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def _is_text(value):
    return isinstance(value, str) and value.strip() != ""


def _check_evidencia_fonte(prefix, nome, fonte, errors):
    if fonte is None:
        return False
    if not isinstance(fonte, dict):
        errors.append(f"{prefix}: evidencia.{nome} deve ser null ou mapa")
        return False
    if not _is_text(fonte.get("procedimento")):
        errors.append(f"{prefix}: evidencia.{nome}.procedimento ausente ou vazio")
    indicadores = fonte.get("indicadores")
    if not isinstance(indicadores, list) or not indicadores or not all(_is_text(i) for i in indicadores):
        errors.append(f"{prefix}: evidencia.{nome}.indicadores deve ser lista não vazia de textos")
    return True


def _validate_criterio(c, diretriz_id, schema, errors):
    cs = schema["criterio"]
    cid = c.get("id") if isinstance(c, dict) else None
    prefix = f"{diretriz_id}/{cid or '?'}"
    if not isinstance(c, dict):
        errors.append(f"{prefix}: criterio deve ser mapa")
        return
    for campo in cs["obrigatorios"]:
        if campo not in c:
            errors.append(f"{prefix}: campo obrigatório ausente: {campo}")
    if "id" in c:
        if not isinstance(cid, str) or not re.match(cs["id_padrao"], cid):
            errors.append(f"{prefix}: id de critério fora do padrão")
        elif not cid.startswith(f"{diretriz_id}."):
            errors.append(f"{prefix}: id de critério não pertence à diretriz {diretriz_id}")
    if "nivel" in c and c["nivel"] not in cs["nivel"]:
        errors.append(f"{prefix}: nivel inválido: {c['nivel']!r}")
    if "enunciado" in c and not _is_text(c["enunciado"]):
        errors.append(f"{prefix}: enunciado vazio")
    nj = c.get("nivel_justificativa")
    if "nivel_justificativa" in c:
        if not isinstance(nj, dict):
            errors.append(f"{prefix}: nivel_justificativa deve ser mapa")
        else:
            if nj.get("essencialidade") not in cs["essencialidade"]:
                errors.append(f"{prefix}: essencialidade inválida: {nj.get('essencialidade')!r}")
            if nj.get("viabilidade") not in cs["viabilidade"]:
                errors.append(f"{prefix}: viabilidade inválida: {nj.get('viabilidade')!r}")
            if not _is_text(nj.get("texto")):
                errors.append(f"{prefix}: nivel_justificativa.texto vazio")
    ev = c.get("evidencia")
    if "evidencia" in c:
        if not isinstance(ev, dict):
            errors.append(f"{prefix}: evidencia deve ser mapa")
        else:
            presentes = 0
            for nome in cs["fontes_evidencia"]:
                if nome not in ev:
                    errors.append(f"{prefix}: evidencia.{nome} ausente (use null se não se aplica)")
                    continue
                if _check_evidencia_fonte(prefix, nome, ev[nome], errors):
                    presentes += 1
            extras = set(ev) - set(cs["fontes_evidencia"])
            if extras:
                errors.append(f"{prefix}: evidencia com chaves desconhecidas: {sorted(extras)}")
            if presentes == 0:
                errors.append(f"{prefix}: evidencia precisa de ao menos uma fonte não nula")
    esc = c.get("escala")
    if "escala" in c:
        if not isinstance(esc, dict):
            errors.append(f"{prefix}: escala deve ser mapa")
        else:
            for grau in cs["escala"]:
                if not _is_text(esc.get(grau)):
                    errors.append(f"{prefix}: escala.{grau} ausente ou vazio")
    dep = c.get("depende_de")
    if "depende_de" in c:
        ok = isinstance(dep, list) and all(
            isinstance(g, list) and g and all(isinstance(i, str) for i in g) for g in dep
        )
        if not ok:
            errors.append(f"{prefix}: depende_de deve ser lista de grupos (lista de listas de ids)")


def validate_diretriz(d, schema, categorias):
    """Return a list of error strings for one guideline dict. Empty list means valid."""
    errors = []
    ds = schema["diretriz"]
    did = d.get("id") if isinstance(d, dict) else None
    prefix = did or "?"
    if not isinstance(d, dict):
        return [f"{prefix}: diretriz deve ser mapa"]
    for campo in ds["obrigatorios"]:
        if campo not in d:
            errors.append(f"{prefix}: campo obrigatório ausente: {campo}")
    if "id" in d and (not isinstance(did, str) or not re.match(ds["id_padrao"], did)):
        errors.append(f"{prefix}: id de diretriz fora do padrão Dnn")
    chaves = {c["chave"] for c in categorias["categorias"]}
    if "categoria" in d and d["categoria"] not in chaves:
        errors.append(f"{prefix}: categoria desconhecida: {d['categoria']!r}")
    if "diretriz" in d and not _is_text(d["diretriz"]):
        errors.append(f"{prefix}: texto da diretriz vazio")
    if "fonte" in d and not _is_text(d["fonte"]):
        errors.append(f"{prefix}: fonte vazia")
    if "modalidade" in d and d["modalidade"] not in ds["modalidade"]:
        errors.append(f"{prefix}: modalidade inválida: {d['modalidade']!r}")
    if "aplicabilidade" in d and d["aplicabilidade"] is not None and not _is_text(d["aplicabilidade"]):
        errors.append(f"{prefix}: aplicabilidade deve ser null ou texto não vazio")
    crit = d.get("criterios")
    if "criterios" in d:
        if not isinstance(crit, list) or not crit:
            errors.append(f"{prefix}: criterios deve ser lista não vazia")
        elif isinstance(did, str):
            for c in crit:
                _validate_criterio(c, did, schema, errors)
    return errors
```

- [ ] **Step 7: Rodar e ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_validate -v`
Expected: `Ran 16 tests ... OK`

- [ ] **Step 8: Commit**

```bash
git add catalog/schema.yaml catalog/categorias.yaml scripts/vygolint_catalog/validate.py tests/helpers.py tests/test_validate.py
git commit -m "feat: schema, categories and structural validation of a guideline" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 4: Validação cruzada do catálogo (ids únicos, dependências, coerência de nível)

**Files:**
- Modify: `scripts/vygolint_catalog/validate.py` (adicionar função ao fim)
- Modify: `tests/test_validate.py` (adicionar classe ao fim)

**Interfaces:**
- Consumes: `derive_nivel` (Task 2), `validate_diretriz` (Task 3).
- Produces: `validate_catalogo(diretrizes: list[dict]) -> list[str]`. Assume que cada diretriz já passou por `validate_diretriz`. Checa: ids de diretriz únicos, ids de critério únicos, todo id em `depende_de` existe e não é o próprio critério, `nivel` declarado igual a `derive_nivel(essencialidade, viabilidade, modalidade)`.

- [ ] **Step 1: Adicionar testes**

Ao fim de `tests/test_validate.py`:

```python
from vygolint_catalog.validate import validate_catalogo


def _segunda_diretriz():
    d = diretriz_valida()
    d["id"] = "D06"
    d["categoria"] = "interacao"
    d["diretriz"] = "O jogador deve trocar informações com outros jogadores por comunicação síncrona"
    c = d["criterios"][0]
    c["id"] = "D06.1"
    c["nivel"] = "AAA"
    c["nivel_justificativa"]["essencialidade"] = "media"
    c["nivel_justificativa"]["viabilidade"] = "baixa"
    return d


class ValidateCatalogoTest(unittest.TestCase):
    def test_valid_catalog_has_no_errors(self):
        self.assertEqual(validate_catalogo([diretriz_valida(), _segunda_diretriz()]), [])

    def test_duplicate_diretriz_id(self):
        errors = validate_catalogo([diretriz_valida(), diretriz_valida()])
        self.assertTrue(any("duplicado" in e and "D17" in e for e in errors))

    def test_duplicate_criterio_id_across_files(self):
        a = diretriz_valida()
        b = _segunda_diretriz()
        b["criterios"][0]["id"] = "D06.1"
        b["criterios"].append(dict(b["criterios"][0]))
        errors = validate_catalogo([a, b])
        self.assertTrue(any("duplicado" in e and "D06.1" in e for e in errors))

    def test_depende_de_unknown_target(self):
        a = diretriz_valida()
        a["criterios"][0]["depende_de"] = [["D99.1"]]
        errors = validate_catalogo([a])
        self.assertTrue(any("D99.1" in e for e in errors))

    def test_depende_de_self_reference(self):
        a = diretriz_valida()
        a["criterios"][0]["depende_de"] = [["D17.1"]]
        errors = validate_catalogo([a])
        self.assertTrue(any("si mesmo" in e for e in errors))

    def test_depende_de_resolves_across_files(self):
        a = diretriz_valida()
        a["criterios"][0]["depende_de"] = [["D06.1"]]
        self.assertEqual(validate_catalogo([a, _segunda_diretriz()]), [])

    def test_declared_level_must_match_table(self):
        a = diretriz_valida()
        a["criterios"][0]["nivel"] = "AAA"
        errors = validate_catalogo([a])
        self.assertTrue(any("nivel" in e and "esperado A" in e for e in errors))

    def test_pode_rule_applied_in_coherence_check(self):
        a = diretriz_valida()
        a["modalidade"] = "pode"
        errors = validate_catalogo([a])
        self.assertTrue(any("esperado AA" in e for e in errors))
        a["criterios"][0]["nivel"] = "AA"
        self.assertEqual(validate_catalogo([a]), [])
```

- [ ] **Step 2: Rodar e ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_validate -v`
Expected: `ImportError: cannot import name 'validate_catalogo'`

- [ ] **Step 3: Implementar**

Ao fim de `scripts/vygolint_catalog/validate.py` (e adicionar `from .levels import derive_nivel` ao topo, abaixo de `import yaml`):

```python
def validate_catalogo(diretrizes):
    """Cross-file checks over structurally valid guidelines."""
    errors = []
    vistos_d = set()
    vistos_c = set()
    for d in diretrizes:
        if d["id"] in vistos_d:
            errors.append(f"{d['id']}: id de diretriz duplicado")
        vistos_d.add(d["id"])
        for c in d["criterios"]:
            if c["id"] in vistos_c:
                errors.append(f"{d['id']}/{c['id']}: id de critério duplicado")
            vistos_c.add(c["id"])
    for d in diretrizes:
        for c in d["criterios"]:
            prefix = f"{d['id']}/{c['id']}"
            nj = c["nivel_justificativa"]
            esperado = derive_nivel(nj["essencialidade"], nj["viabilidade"], d["modalidade"])
            if c["nivel"] != esperado:
                errors.append(
                    f"{prefix}: nivel declarado {c['nivel']} mas esperado {esperado} "
                    f"(essencialidade {nj['essencialidade']}, viabilidade {nj['viabilidade']}, modalidade {d['modalidade']})"
                )
            for grupo in c["depende_de"]:
                for alvo in grupo:
                    if alvo == c["id"]:
                        errors.append(f"{prefix}: depende_de aponta para si mesmo")
                    elif alvo not in vistos_c:
                        errors.append(f"{prefix}: depende_de aponta para critério inexistente: {alvo}")
    return errors
```

- [ ] **Step 4: Rodar e ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_validate -v`
Expected: `Ran 24 tests ... OK`

- [ ] **Step 5: Commit**

```bash
git add scripts/vygolint_catalog/validate.py tests/test_validate.py
git commit -m "feat: cross-file catalog validation with level coherence" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 5: Renderização Markdown

**Files:**
- Create: `scripts/vygolint_catalog/render.py`, `tests/test_render.py`

**Interfaces:**
- Consumes: dicts de diretriz validados; dict de categorias.
- Produces: `render_markdown(diretrizes: list[dict], categorias: dict) -> str`. Ordena por id. Primeira linha é `<!-- ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão. -->`.

- [ ] **Step 1: Escrever os testes**

`tests/test_render.py`:

```python
import unittest

from helpers import categorias_validas, diretriz_valida
from vygolint_catalog.render import render_markdown


class RenderMarkdownTest(unittest.TestCase):
    def setUp(self):
        self.cats = categorias_validas()

    def test_header_marks_generated_file(self):
        out = render_markdown([diretriz_valida()], self.cats)
        self.assertTrue(out.startswith("<!-- ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão. -->"))

    def test_summary_table_row(self):
        out = render_markdown([diretriz_valida()], self.cats)
        self.assertIn("| D17 | Mediação | O jogo deve exibir feedback construtivo para as ações do jogador | D17.1 (A) |", out)

    def test_detail_section_contains_all_blocks(self):
        out = render_markdown([diretriz_valida()], self.cats)
        for trecho in (
            "### D17 — O jogo deve exibir feedback construtivo para as ações do jogador",
            "#### D17.1 — Nível A",
            "**Enunciado.** Toda ação incorreta",
            "essencialidade alta, viabilidade alta",
            "- Código: Localizar tratadores de erro",
            "- Documentação: não se aplica",
            "- Vídeo: Registrar timestamp",
            "Indicadores: ao menos 3 ocorrências de erro; cada ocorrência mostra orientação",
            "- Atendido: Todas as ocorrências",
            "- Parcial: Algumas ocorrências",
            "- Não atendido: Feedback só sinaliza",
            "**Depende de.** —",
        ):
            with self.subTest(trecho=trecho):
                self.assertIn(trecho, out)

    def test_depende_de_rendering(self):
        d = diretriz_valida()
        d["criterios"][0]["depende_de"] = [["D06.1", "D07.1"], ["D09.1"]]
        out = render_markdown([d], self.cats)
        self.assertIn("**Depende de.** (D06.1 ou D07.1) e (D09.1)", out)

    def test_aplicabilidade_and_modalidade(self):
        d = diretriz_valida()
        d["modalidade"] = "pode"
        d["aplicabilidade"] = "Somente quando aplicado em sala de aula"
        d["criterios"][0]["nivel"] = "AA"
        out = render_markdown([d], self.cats)
        self.assertIn("- Modalidade: pode", out)
        self.assertIn("- Aplicabilidade: Somente quando aplicado em sala de aula", out)

    def test_sorted_by_id_and_deterministic(self):
        a = diretriz_valida()
        b = diretriz_valida()
        b["id"] = "D06"
        b["categoria"] = "interacao"
        b["criterios"][0]["id"] = "D06.1"
        out1 = render_markdown([a, b], self.cats)
        out2 = render_markdown([b, a], self.cats)
        self.assertEqual(out1, out2)
        self.assertLess(out1.index("| D06 |"), out1.index("| D17 |"))

    def test_ressalva_present(self):
        out = render_markdown([diretriz_valida()], self.cats)
        self.assertIn("suprimiu as categorias", out)
```

- [ ] **Step 2: Rodar e ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_render -v`
Expected: `ModuleNotFoundError: No module named 'vygolint_catalog.render'`

- [ ] **Step 3: Implementar**

`scripts/vygolint_catalog/render.py`:

```python
"""Render validated catalog dicts to Markdown and LaTeX. Pure functions, no I/O."""

GENERATED_MD = "<!-- ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão. -->"
GENERATED_TEX = "% ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão."

_FONTES = (("codigo", "Código"), ("documentacao", "Documentação"), ("video", "Vídeo"))
_GRAUS = (("atendido", "Atendido"), ("parcial", "Parcial"), ("nao_atendido", "Não atendido"))


def _nome_categoria(chave, categorias):
    for c in categorias["categorias"]:
        if c["chave"] == chave:
            return c["nome"]
    return chave


def _ordenadas(diretrizes):
    return sorted(diretrizes, key=lambda d: d["id"])


def _criterios_resumo(d):
    return ", ".join(f"{c['id']} ({c['nivel']})" for c in d["criterios"])


def _depende_de(c):
    if not c["depende_de"]:
        return "—"
    return " e ".join("(" + " ou ".join(g) + ")" for g in c["depende_de"])


def render_markdown(diretrizes, categorias):
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
            linhas += [
                f"#### {c['id']} — Nível {c['nivel']}",
                "",
                f"**Enunciado.** {c['enunciado']}",
                "",
                f"**Justificativa do nível.** essencialidade {nj['essencialidade']}, "
                f"viabilidade {nj['viabilidade']}. {nj['texto']}",
                "",
                "**Evidência.**",
            ]
            for chave, nome in _FONTES:
                fonte = c["evidencia"][chave]
                if fonte is None:
                    linhas.append(f"- {nome}: não se aplica")
                else:
                    linhas.append(
                        f"- {nome}: {fonte['procedimento']}. Indicadores: " + "; ".join(fonte["indicadores"])
                    )
            linhas += ["", "**Escala.**"]
            for chave, nome in _GRAUS:
                linhas.append(f"- {nome}: {c['escala'][chave]}")
            linhas += ["", f"**Depende de.** {_depende_de(c)}", ""]
    return "\n".join(linhas).rstrip() + "\n"
```

- [ ] **Step 4: Rodar e ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_render -v`
Expected: `Ran 7 tests ... OK`

- [ ] **Step 5: Commit**

```bash
git add scripts/vygolint_catalog/render.py tests/test_render.py
git commit -m "feat: render catalog to Markdown" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 6: Renderização LaTeX

**Files:**
- Modify: `scripts/vygolint_catalog/render.py` (adicionar ao fim)
- Modify: `tests/test_render.py` (adicionar ao fim)

**Interfaces:**
- Produces: `escape_latex(text: str) -> str`; `render_latex(diretrizes: list[dict], categorias: dict) -> str` gerando um `longtable` com colunas ID, Categoria, Diretriz, Critérios. Primeira linha `% ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão.`

- [ ] **Step 1: Adicionar testes**

Ao fim de `tests/test_render.py`:

```python
from vygolint_catalog.render import escape_latex, render_latex


class RenderLatexTest(unittest.TestCase):
    def test_escape(self):
        self.assertEqual(escape_latex("a & b % c _ d # e"), r"a \& b \% c \_ d \# e")
        self.assertEqual(escape_latex(r"x\y"), r"x\textbackslash{}y")
        self.assertEqual(escape_latex("{a}"), r"\{a\}")

    def test_longtable_structure(self):
        out = render_latex([diretriz_valida()], categorias_validas())
        self.assertTrue(out.startswith("% ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão."))
        self.assertIn(r"\begin{longtable}", out)
        self.assertIn(r"\label{tab:catalogo_vygolint}", out)
        self.assertIn(r"\endfirsthead", out)
        self.assertIn(r"\endhead", out)
        self.assertIn(r"D17 & Mediação & O jogo deve exibir feedback construtivo para as ações do jogador & D17.1 (A) \\", out)
        self.assertIn(r"\end{longtable}", out)

    def test_rows_escaped_and_sorted(self):
        a = diretriz_valida()
        a["diretriz"] = "Texto com & e 100%"
        b = diretriz_valida()
        b["id"] = "D06"
        b["categoria"] = "interacao"
        b["criterios"][0]["id"] = "D06.1"
        out = render_latex([a, b], categorias_validas())
        self.assertIn(r"Texto com \& e 100\%", out)
        self.assertLess(out.index("D06 &"), out.index("D17 &"))
```

- [ ] **Step 2: Rodar e ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_render -v`
Expected: `ImportError: cannot import name 'escape_latex'`

- [ ] **Step 3: Implementar**

Ao fim de `scripts/vygolint_catalog/render.py` (e adicionar `import re` como primeira linha de código do módulo, abaixo da docstring):

```python
_LATEX_MAP = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}
_LATEX_RE = re.compile("|".join(re.escape(k) for k in _LATEX_MAP))


def escape_latex(text):
    """Single-pass escape so replacements never re-escape each other."""
    return _LATEX_RE.sub(lambda m: _LATEX_MAP[m.group()], text)


def render_latex(diretrizes, categorias):
    cab = r"\textbf{ID} & \textbf{Categoria} & \textbf{Diretriz} & \textbf{Critérios} \\"
    linhas = [
        GENERATED_TEX,
        r"\begin{longtable}{p{1.1cm}p{2.6cm}p{7.2cm}p{2.6cm}}",
        r"\caption{Diretrizes de Carvalho (2020) e critérios de conformidade do vygolint}"
        r"\label{tab:catalogo_vygolint}\\",
        r"\hline",
        cab,
        r"\hline",
        r"\endfirsthead",
        r"\hline",
        cab,
        r"\hline",
        r"\endhead",
        r"\hline",
        r"\endfoot",
    ]
    for d in _ordenadas(diretrizes):
        linhas.append(
            f"{d['id']} & {escape_latex(_nome_categoria(d['categoria'], categorias))} & "
            f"{escape_latex(d['diretriz'])} & {escape_latex(_criterios_resumo(d))} \\\\"
        )
    linhas.append(r"\end{longtable}")
    return "\n".join(linhas) + "\n"
```

- [ ] **Step 4: Rodar e ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_render -v`
Expected: `Ran 10 tests ... OK`

- [ ] **Step 5: Commit**

```bash
git add scripts/vygolint_catalog/render.py tests/test_render.py
git commit -m "feat: render catalog summary to LaTeX longtable" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 7: Build e CLI

**Files:**
- Create: `scripts/vygolint_catalog/build.py`, `scripts/build_catalog.py`, `tests/test_build.py`

**Interfaces:**
- Consumes: `load_yaml`, `validate_diretriz`, `validate_catalogo`, `render_markdown`, `render_latex`.
- Produces: `build(catalog_dir: Path, docs_dir: Path) -> list[str]`. Lê `schema.yaml`, `categorias.yaml` e todo `D*.yaml` em ordem de nome; verifica que o nome do arquivo é `<id>.yaml`; acumula erros; se houver erros, não escreve nada e retorna a lista; senão escreve `catalogo.md` e `catalogo.tex` em `docs_dir` e retorna `[]`. CLI `scripts/build_catalog.py [--catalog DIR] [--docs DIR]` imprime erros em stderr e sai com 1, ou imprime `OK: N diretrizes, M critérios` e sai com 0.

- [ ] **Step 1: Escrever os testes**

`tests/test_build.py`:

```python
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from helpers import REPO, diretriz_valida
from vygolint_catalog.build import build


class BuildTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.catalog = self.tmp / "catalog"
        self.docs = self.tmp / "docs"
        self.catalog.mkdir()
        shutil.copy(REPO / "catalog" / "schema.yaml", self.catalog)
        shutil.copy(REPO / "catalog" / "categorias.yaml", self.catalog)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def write(self, d, name=None):
        (self.catalog / (name or f"{d['id']}.yaml")).write_text(
            yaml.safe_dump(d, allow_unicode=True, sort_keys=False), encoding="utf-8"
        )

    def test_valid_catalog_writes_both_docs(self):
        self.write(diretriz_valida())
        self.assertEqual(build(self.catalog, self.docs), [])
        md = (self.docs / "catalogo.md").read_text(encoding="utf-8")
        tex = (self.docs / "catalogo.tex").read_text(encoding="utf-8")
        self.assertIn("| D17 |", md)
        self.assertIn("D17 &", tex)

    def test_invalid_catalog_writes_nothing(self):
        d = diretriz_valida()
        d["criterios"][0]["nivel"] = "AAA"
        self.write(d)
        errors = build(self.catalog, self.docs)
        self.assertTrue(errors)
        self.assertFalse(self.docs.exists())

    def test_filename_must_match_id(self):
        self.write(diretriz_valida(), name="D18.yaml")
        errors = build(self.catalog, self.docs)
        self.assertTrue(any("D18.yaml" in e and "D17" in e for e in errors))

    def test_build_is_deterministic(self):
        self.write(diretriz_valida())
        build(self.catalog, self.docs)
        first = (self.docs / "catalogo.md").read_bytes()
        build(self.catalog, self.docs)
        self.assertEqual(first, (self.docs / "catalogo.md").read_bytes())

    def test_cli_exit_codes(self):
        self.write(diretriz_valida())
        cmd = [sys.executable, str(REPO / "scripts" / "build_catalog.py"), "--catalog", str(self.catalog), "--docs", str(self.docs)]
        ok = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertIn("OK: 1 diretrizes, 1 critérios", ok.stdout)
        d = diretriz_valida()
        del d["fonte"]
        self.write(d)
        bad = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertIn("fonte", bad.stderr)
```

- [ ] **Step 2: Rodar e ver falhar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_build -v`
Expected: `ModuleNotFoundError: No module named 'vygolint_catalog.build'`

- [ ] **Step 3: Implementar `build.py`**

`scripts/vygolint_catalog/build.py`:

```python
"""Load, validate and render the whole catalog."""

from pathlib import Path

from .render import render_latex, render_markdown
from .validate import load_yaml, validate_catalogo, validate_diretriz


def build(catalog_dir, docs_dir):
    """Return a list of errors. On success (empty list) writes catalogo.md and catalogo.tex."""
    catalog_dir = Path(catalog_dir)
    docs_dir = Path(docs_dir)
    schema = load_yaml(catalog_dir / "schema.yaml")
    categorias = load_yaml(catalog_dir / "categorias.yaml")
    errors = []
    diretrizes = []
    for path in sorted(catalog_dir.glob("D*.yaml")):
        d = load_yaml(path)
        errs = validate_diretriz(d, schema, categorias)
        if not errs and path.name != f"{d['id']}.yaml":
            errs.append(f"{path.name}: nome do arquivo não corresponde ao id {d['id']}")
        errors.extend(errs)
        if not errs:
            diretrizes.append(d)
    if errors:
        return errors
    errors = validate_catalogo(diretrizes)
    if errors:
        return errors
    docs_dir.mkdir(parents=True, exist_ok=True)
    (docs_dir / "catalogo.md").write_text(render_markdown(diretrizes, categorias), encoding="utf-8")
    (docs_dir / "catalogo.tex").write_text(render_latex(diretrizes, categorias), encoding="utf-8")
    return []


def contagem(catalog_dir):
    """Return (n_diretrizes, n_criterios) for a catalog directory, without validating."""
    n_d = n_c = 0
    for path in sorted(Path(catalog_dir).glob("D*.yaml")):
        d = load_yaml(path)
        n_d += 1
        n_c += len(d.get("criterios") or [])
    return n_d, n_c
```

- [ ] **Step 4: Implementar a CLI**

`scripts/build_catalog.py`:

```python
#!/usr/bin/env python3
"""Validate the vygolint catalog and regenerate docs/catalogo.md and docs/catalogo.tex."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vygolint_catalog.build import build, contagem  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", default=str(REPO / "catalog"))
    parser.add_argument("--docs", default=str(REPO / "docs"))
    args = parser.parse_args(argv)
    errors = build(args.catalog, args.docs)
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        print(f"{len(errors)} erro(s). Nada foi gerado.", file=sys.stderr)
        return 1
    n_d, n_c = contagem(args.catalog)
    print(f"OK: {n_d} diretrizes, {n_c} critérios -> {args.docs}/catalogo.md, {args.docs}/catalogo.tex")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Rodar e ver passar**

Run: `PYTHONPATH=scripts python3 -m unittest tests.test_build -v`
Expected: `Ran 5 tests ... OK`

- [ ] **Step 6: Rodar a suíte completa**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests -v`
Expected: `Ran 45 tests ... OK`

- [ ] **Step 7: Commit**

```bash
git add scripts/vygolint_catalog/build.py scripts/build_catalog.py tests/test_build.py
git commit -m "feat: build command that validates the catalog and writes docs" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 8: Piloto do catálogo (D06, D07, D16, D17) e docs gerados

**Files:**
- Create: `catalog/D06.yaml`, `catalog/D07.yaml`, `catalog/D16.yaml`, `catalog/D17.yaml`, `docs/catalogo.md`, `docs/catalogo.tex`

**Interfaces:**
- Consumes: `scripts/build_catalog.py`.
- Produces: quatro diretrizes reais que exercitam dependência entre arquivos; primeiros docs gerados commitados.

- [ ] **Step 1: Escrever `catalog/D17.yaml`**

```yaml
id: D17
categoria: mediacao
diretriz: "O jogo deve exibir feedback construtivo para as ações do jogador"
fonte: "Carvalho (2020), Quadro 3"
modalidade: deve
aplicabilidade: null
criterios:
  - id: D17.1
    nivel: A
    enunciado: "Toda ação incorreta do jogador recebe mensagem que indica o que fazer em seguida, e não apenas que errou"
    nivel_justificativa:
      essencialidade: alta
      viabilidade: alta
      texto: "Mediação é o núcleo da zona de desenvolvimento proximal: o jogo faz o papel do outro mais experiente. Feedback que só sinaliza acerto ou erro é reforço behaviorista, exatamente o que as diretrizes querem afastar. Implementação de baixo custo em qualquer motor de jogo."
    evidencia:
      codigo:
        procedimento: "Localizar os tratadores de erro ou falha de missão e minijogo e listar o texto exibido em cada um"
        indicadores:
          - "mensagem contém orientação de próxima ação"
          - "mensagem referencia o conteúdo ou objeto envolvido no erro"
      documentacao:
        procedimento: "Verificar no documento de design (GDD) a especificação de feedback por tipo de erro"
        indicadores:
          - "tabela ou lista de erros com a mensagem orientadora correspondente"
      video:
        procedimento: "Registrar o timestamp de cada erro cometido pelo jogador e classificar o feedback exibido"
        indicadores:
          - "ao menos 3 ocorrências de erro observadas"
          - "cada ocorrência mostra orientação, não só sinal de erro"
    escala:
      atendido: "Todas as ocorrências de erro observadas recebem feedback que orienta a próxima ação"
      parcial: "Algumas ocorrências orientam; outras só sinalizam erro ou não recebem feedback"
      nao_atendido: "O feedback só sinaliza acerto ou erro, ou não existe"
    depende_de: []
```

- [ ] **Step 2: Escrever `catalog/D06.yaml`**

```yaml
id: D06
categoria: interacao
diretriz: "O jogador deve trocar informações com outros jogadores por comunicação síncrona"
fonte: "Carvalho (2020), Quadro 3"
modalidade: deve
aplicabilidade: null
criterios:
  - id: D06.1
    nivel: AAA
    enunciado: "Durante a sessão, o jogador envia e recebe mensagens de texto ou voz de outros jogadores em tempo real"
    nivel_justificativa:
      essencialidade: media
      viabilidade: baixa
      texto: "Socialização entre pares é constitutiva do sociointeracionismo, mas a interação social também pode ocorrer de forma assíncrona (D07) ou fora do jogo (D22); por isso essencialidade média. Comunicação síncrona exige infraestrutura de rede e sessão multijogador, rara em jogos educacionais; viabilidade baixa."
    evidencia:
      codigo:
        procedimento: "Procurar módulo de rede, chat ou voz e verificar se envia e recebe mensagens entre clientes durante a partida"
        indicadores:
          - "existe canal de mensagens entre jogadores conectados"
          - "mensagens chegam sem exigir fim da sessão"
      documentacao:
        procedimento: "Verificar no GDD a seção de multijogador ou comunicação"
        indicadores:
          - "especificação de chat, voz ou mensagens em tempo real"
      video:
        procedimento: "Observar sessão com dois ou mais jogadores e registrar trocas de mensagens"
        indicadores:
          - "ao menos uma troca de mensagem com resposta na mesma sessão"
    escala:
      atendido: "Canal síncrono existe e o vídeo mostra troca de mensagens livres entre jogadores"
      parcial: "Canal existe, mas limitado a mensagens prontas, emotes ou sinais sem conteúdo livre"
      nao_atendido: "Não há comunicação entre jogadores durante a sessão"
    depende_de: []
```

- [ ] **Step 3: Escrever `catalog/D07.yaml`**

```yaml
id: D07
categoria: interacao
diretriz: "O jogador deve trocar informações com outros jogadores por meio de comunicação assíncrona"
fonte: "Carvalho (2020), Quadro 3"
modalidade: deve
aplicabilidade: null
criterios:
  - id: D07.1
    nivel: AA
    enunciado: "O jogo persiste mensagens ou registros deixados por um jogador e os exibe a outros jogadores em sessões posteriores"
    nivel_justificativa:
      essencialidade: media
      viabilidade: media
      texto: "Mesma base de D06: socialização entre pares. A forma assíncrona exige apenas persistência de dados e um ponto de leitura no jogo, viável sem sessão multijogador simultânea."
    evidencia:
      codigo:
        procedimento: "Procurar persistência de mensagens, comentários ou registros de jogador e o ponto onde outros jogadores os leem"
        indicadores:
          - "escrita de mensagem associada a jogador e contexto"
          - "leitura de mensagens de outros jogadores em sessão distinta"
      documentacao:
        procedimento: "Verificar no GDD mecânicas de mural, bilhetes, diário compartilhado ou similar"
        indicadores:
          - "mecânica descrita com autor, local e leitor da mensagem"
      video:
        procedimento: "Observar se o jogador encontra registros deixados por outro jogador ou deixa um registro"
        indicadores:
          - "registro de outro jogador visível na sessão"
    escala:
      atendido: "Jogador deixa e lê mensagens de outros jogadores em sessões distintas"
      parcial: "Jogador só lê registros de outros, sem poder deixar os seus, ou o inverso"
      nao_atendido: "Não há troca assíncrona entre jogadores"
    depende_de: []
```

- [ ] **Step 4: Escrever `catalog/D16.yaml`**

```yaml
id: D16
categoria: mediacao
diretriz: "O jogo deve fornecer meios do jogador solicitar ajuda de outros jogadores"
fonte: "Carvalho (2020), Quadro 3"
modalidade: deve
aplicabilidade: null
criterios:
  - id: D16.1
    nivel: AA
    enunciado: "Existe uma ação explícita de pedir ajuda que encaminha a solicitação do jogador a outro jogador"
    nivel_justificativa:
      essencialidade: media
      viabilidade: media
      texto: "Mediação por pares é a forma mais direta da zona de desenvolvimento proximal entre jogadores, mas a mediação também é oferecida pelo próprio jogo (D17 a D21). Exige um canal entre jogadores (D06 ou D07) e uma ação dedicada; viabilidade média."
    evidencia:
      codigo:
        procedimento: "Localizar ação, botão ou comando de pedir ajuda e verificar para onde a solicitação é enviada"
        indicadores:
          - "ação de ajuda distinta do chat geral"
          - "solicitação chega a outro jogador, não só ao sistema"
      documentacao:
        procedimento: "Verificar no GDD a mecânica de pedido de ajuda"
        indicadores:
          - "fluxo descrito: quem pede, quem recebe, o que acontece"
      video:
        procedimento: "Observar o jogador acionar o pedido de ajuda e o que ocorre em seguida"
        indicadores:
          - "pedido de ajuda enviado a outro jogador"
    escala:
      atendido: "Ação de pedir ajuda existe e chega a outro jogador"
      parcial: "Ação existe, mas a resposta vem só do sistema ou de personagem não jogável"
      nao_atendido: "Não há meio de pedir ajuda a outros jogadores"
    depende_de:
      - [D06.1, D07.1]
```

- [ ] **Step 5: Rodar o build**

Run: `python3 scripts/build_catalog.py`
Expected: `OK: 4 diretrizes, 4 critérios -> .../docs/catalogo.md, .../docs/catalogo.tex`

- [ ] **Step 6: Inspecionar o Markdown gerado**

Run: `sed -n '1,30p' docs/catalogo.md`
Expected: cabeçalho de arquivo gerado, ressalva, tabela com D06, D07, D16, D17 nessa ordem. Abrir `docs/catalogo.md` inteiro e conferir que a seção de D16 mostra `**Depende de.** (D06.1 ou D07.1)`.

- [ ] **Step 7: Revisão humana do formato**

Parar aqui e pedir ao autor do catálogo que leia `docs/catalogo.md`. Ajustes de formato de renderização voltam para Task 5. Ajustes de conteúdo editam o YAML e repetem o build.

- [ ] **Step 8: Commit**

```bash
git add catalog/D06.yaml catalog/D07.yaml catalog/D16.yaml catalog/D17.yaml docs/catalogo.md docs/catalogo.tex
git commit -m "feat(catalog): pilot guidelines D06, D07, D16 and D17 with generated docs" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 9: CI

**Files:**
- Create: `.github/workflows/ci.yml`

**Interfaces:**
- Consumes: comandos de teste e build.
- Produces: job que falha se testes falham, se o catálogo é inválido ou se `docs/catalogo.md` e `docs/catalogo.tex` estão desatualizados.

- [ ] **Step 1: Escrever o workflow**

`.github/workflows/ci.yml`:

```yaml
name: ci
on:
  push:
  pull_request:
jobs:
  catalog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - name: Tests
        run: PYTHONPATH=scripts python3 -m unittest discover -s tests -v
      - name: Build catalog
        run: python3 scripts/build_catalog.py
      - name: Generated docs are up to date
        run: git diff --exit-code -- docs/catalogo.md docs/catalogo.tex
```

- [ ] **Step 2: Verificar localmente o passo de diff**

Run: `python3 scripts/build_catalog.py && git diff --exit-code -- docs/catalogo.md docs/catalogo.tex && echo SYNC`
Expected: `SYNC`

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/ci.yml
git commit -m "ci: run tests, build catalog and check generated docs" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Tasks 10 a 15: Escrita do catálogo em lotes

Cada lote segue o mesmo procedimento. O conteúdo de cada diretriz é trabalho de autoria: o executor escreve o YAML completo no formato de Task 8, usando a tabela de orientação do lote (texto literal, modalidade, eixos sugeridos e ideia de critério). Os eixos sugeridos são ponto de partida defensável, não decisão final: o executor pode mudar, desde que a justificativa textual sustente a mudança e o build passe.

**Procedimento de cada lote:**

- [ ] **Step 1:** Para cada diretriz do lote, criar `catalog/Dnn.yaml` com todos os campos. Regras: texto literal (sem hifenização do PDF); 1 a 3 critérios; cada critério com enunciado observável, `nivel_justificativa` com os dois eixos e texto de 2 a 4 frases ancorado em Vigotski ou no capítulo 5 de Carvalho (2020); as três chaves de evidência presentes (null quando a fonte não serve); escala com três descritores observáveis; `depende_de` como lista de grupos.
- [ ] **Step 2:** Run: `python3 scripts/build_catalog.py`. Expected: `OK: N diretrizes, M critérios`. Se houver erro de nível, ajustar `nivel` para o esperado ou revisar os eixos; nunca ajustar a tabela.
- [ ] **Step 3:** Ler a seção de cada diretriz do lote em `docs/catalogo.md` e checar: o enunciado é verificável por duas pessoas com as mesmas evidências; nenhum descritor de escala usa adjetivo subjetivo ("motivador", "bom", "adequado").
- [ ] **Step 4:** Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests` e `git diff --exit-code -- docs/`. Expected: testes OK e nenhum diff após o build (rodar o build antes do diff).
- [ ] **Step 5:** Commit: `git add catalog/ docs/catalogo.md docs/catalogo.tex && git commit -m "feat(catalog): <categoria> guidelines <faixa>" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"`

#### Task 10: Interação, parte 1 (D01 a D05, D08)

| ID | Diretriz (literal) | Mod. | Ess. | Viab. | Nível | Ideia de critério | Fontes |
|---|---|---|---|---|---|---|---|
| D01 | Os desafios do jogo devem ser direcionados a resolução de problemas | deve | alta | alta | A | Cada missão ou minijogo exige uma decisão do jogador para resolver uma situação-problema, não só repetir uma ação | docs, vídeo |
| D02 | Avaliar os conteúdos ensinados no jogo de forma a transcender o contexto que eles foram abordados, possibilitando a transposição dos conceitos para resolução de outras situações-problema | deve | alta | media | A | Existe ao menos um desafio que aplica um conceito já apresentado em situação distinta daquela em que foi introduzido | docs, vídeo |
| D03 | O desenvolvimento das atividades/missões/minijogos deve ser autorregulado pelo jogador | deve | alta | alta | A | O jogador escolhe ordem ou ritmo das atividades; o jogo não avança sozinho nem impõe cronômetro como única forma de progressão | código, vídeo |
| D04 | O jogador deve interagir com os objetos dos cenários | deve | alta | alta | A | Objetos do cenário respondem à interação com informação ou mudança de estado ligada ao conteúdo | código, vídeo |
| D05 | O jogador deve explorar livremente o cenário | deve | alta | media | A | Há áreas acessíveis fora do caminho da missão atual e o jogador consegue visitá-las sem bloqueio | docs, vídeo |
| D08 | O jogador deve trocar informações com os mecanismos do jogo | deve | alta | alta | A | Personagens não jogáveis ou mecanismos entregam informação ao jogador e recebem informação dele (escolha, resposta, item) | código, vídeo |

#### Task 11: Interação, parte 2 (D09 a D15)

| ID | Diretriz (literal) | Mod. | Ess. | Viab. | Nível | Ideia de critério | Fontes |
|---|---|---|---|---|---|---|---|
| D09 | O jogador deve se comunicar por linguagem escrita | deve | media | alta | AA | O jogador produz texto livre em algum ponto (chat, resposta aberta, anotação, nome de item) | código, vídeo |
| D10 | O jogo deve viabilizar o comportamento ativo do jogador | deve | alta | alta | A | O progresso depende de ação do jogador; trechos passivos (cutscene, texto corrido) não ultrapassam limite definido no critério (ex.: 2 minutos contínuos) | vídeo |
| D11 | O jogador deve coletar informações | deve | alta | alta | A | Existe mecânica de coleta (itens, dados, registros) cujo conteúdo é usado depois em missão ou desafio | código, docs, vídeo |
| D12 | O jogo deve fornecer mecanismos para o jogador construir coisas | deve | baixa | media | AAA | O jogador combina elementos para criar um artefato novo que persiste no jogo | código, docs, vídeo |
| D13 | O jogo permite o desenvolvimento de tarefas e missões em grupo | deve | media | baixa | AAA | Existe missão que exige mais de um jogador para ser concluída. Depende de [[D06.1, D07.1]] | docs, vídeo |
| D14 | O jogador deve conseguir inserir comentários no jogo que ficarão disponíveis para outros jogadores | deve | media | media | AA | Comentário escrito por um jogador fica visível a outro jogador em sessão posterior, ancorado a um local ou objeto | código, vídeo |
| D15 | O jogo deve estimular a interação entre jogadores por diversas ferramentas de comunicação | deve | media | baixa | AAA | Ao menos duas ferramentas distintas de comunicação entre jogadores. Depende de [[D06.1, D07.1]] | código, docs |

#### Task 12: Mediação restante (D18 a D23)

| ID | Diretriz (literal) | Mod. | Ess. | Viab. | Nível | Ideia de critério | Fontes |
|---|---|---|---|---|---|---|---|
| D18 | O jogo deve exibir feedback individualizado para as ações do jogador | deve | alta | media | A | O feedback varia conforme a ação específica ou o histórico do jogador; mesma situação com ações diferentes gera mensagens diferentes | código, vídeo |
| D19 | Os desafios devem proporcionar o desenvolvimento de competências no uso das ferramentas mentais | deve | alta | media | A | Desafios exigem ao menos duas funções psicológicas superiores nomeadas (memória, atenção voluntária, planejamento, linguagem), registradas no GDD e observáveis no vídeo | docs, vídeo |
| D20 | O jogo pode fornecer pista para o jogador resolver problemas | pode | media | alta | AA | Existe mecanismo de pista acionável pelo jogador ou disparado após tentativas, que não entrega a solução completa | código, vídeo |
| D21 | O jogo pode fornecer simulações de formas para resolver o problema | pode | media | media | AA | Existe modo de demonstração ou simulação de uma forma de resolver o problema, sem substituir a ação do jogador | docs, vídeo |
| D22 | O jogo, quando aplicado em sala de aula, cria oportunidades para o professor atuar como mediador / facilitador | deve | media | alta | AA | A documentação prevê momentos, materiais ou painel para o professor intervir; `aplicabilidade: "Somente quando o jogo é aplicado em sala de aula"` | docs |
| D23 | A narrativa do jogo deve viabilizar reflexões críticas ao trabalhar os conteúdos | deve | alta | media | A | A narrativa apresenta ao menos um dilema ou consequência que exige posicionamento do jogador sobre o conteúdo | docs, vídeo |

#### Task 13: Autonomia, Socialização e Lúdico (D24 a D29)

| ID | Diretriz (literal) | Mod. | Ess. | Viab. | Nível | Ideia de critério | Fontes |
|---|---|---|---|---|---|---|---|
| D24 | O jogador decide quais recursos utilizar | deve | alta | alta | A | Para ao menos um desafio existe mais de um recurso válido e o jogador escolhe qual usar | código, vídeo |
| D25 | O jogador decide, com base em seus interesses e motivações, qual conteúdo explorar | deve | media | media | AA | Existem conteúdos opcionais acessíveis por escolha do jogador, não exigidos para concluir a missão | docs, vídeo |
| D26 | O jogo deve aproximar os jogadores pela competição | deve | media | baixa | AAA | Existe mecânica de competição entre jogadores (ranking, disputa) visível a eles | código, docs |
| D27 | O jogo deve aproximar os jogadores pela colaboração | deve | media | baixa | AAA | Existe objetivo compartilhado cujo resultado depende da ação de mais de um jogador. Depende de [[D13.1]] | docs, vídeo |
| D28 | A proposta de narrativa deve despertar a curiosidade | deve | media | alta | AA | Antes de cada missão a narrativa apresenta uma pergunta ou mistério que só se resolve jogando (observável: pergunta explícita ou informação retida) | docs, vídeo |
| D29 | O jogo deve fornecer desafios motivadores, que estimulem o jogador a explorar | deve | alta | alta | A | Existe recompensa ou descoberta acessível só por exploração fora do caminho obrigatório | código, vídeo |

#### Task 14: Realismo e Personalização (D30 a D35)

| ID | Diretriz (literal) | Mod. | Ess. | Viab. | Nível | Ideia de critério | Fontes |
|---|---|---|---|---|---|---|---|
| D30 | O jogo deve colocar o jogador em uma situação realística | deve | media | alta | AA | A premissa do jogo corresponde a uma situação real documentada (projeto, profissão, fenômeno) citada no GDD | docs, vídeo |
| D31 | O jogo contextualiza o conteúdo com situações reais | deve | alta | alta | A | Cada conteúdo conceitual aparece dentro de uma situação do jogo, não como texto isolado de glossário | docs, vídeo |
| D32 | O jogo deve ter objetos do cotidiano com os quais o jogador pode se familiarizar | deve | media | alta | AA | Objetos interativos incluem itens reconhecíveis do cotidiano do público-alvo | docs, vídeo |
| D33 | Os desafios devem ser personalizados de acordo com o desempenho do jogador | deve | baixa | baixa | AAA | Parâmetros de desafio mudam em função de métrica de desempenho registrada | código, docs |
| D34 | Os desafios devem ser personalizados de acordo com as ações do jogador | deve | baixa | baixa | AAA | Escolhas anteriores do jogador alteram desafios posteriores | código, vídeo |
| D35 | O jogo deve permitir que o jogador crie desafios para outros jogadores | deve | baixa | baixa | AAA | Existe editor ou mecânica de criação de desafio que outro jogador pode jogar. Depende de [[D07.1]] | código, docs |

#### Task 15: Organização, Resolução de problemas, Linguagem, Atenção, Aprendizado (D36 a D40)

| ID | Diretriz (literal) | Mod. | Ess. | Viab. | Nível | Ideia de critério | Fontes |
|---|---|---|---|---|---|---|---|
| D36 | O jogador deve organizar informações | deve | alta | media | A | Existe mecânica de inventário, diário, classificação ou agrupamento operada pelo jogador | código, vídeo |
| D37 | O jogo, suas missões e mini jogos devem apresentar a situação-problema ao jogador de maneira explícita | deve | alta | alta | A | Cada missão apresenta o problema em texto ou fala antes de exigir ação | docs, vídeo |
| D38 | O jogo deve fornecer informações escritas ao jogador | deve | alta | alta | A | Diálogos, descrições e instruções existem em forma escrita, não só em áudio | código, vídeo |
| D39 | O mundo do jogo deve exigir do jogador a percepção de detalhes | deve | media | alta | AA | Ao menos um desafio só é resolvido ao notar um detalhe do cenário não sinalizado explicitamente | docs, vídeo |
| D40 | O jogo deve viabilizar o aprendizado também pelos erros do jogador com mensagens textuais, sons e animações | deve | alta | alta | A | Erro do jogador gera resposta em ao menos duas modalidades (texto, som, animação) que carregam informação sobre o erro. Depende de [[D17.1]] | código, vídeo |

Ao fim de Task 15: `python3 scripts/build_catalog.py` deve imprimir `OK: 40 diretrizes, M critérios`.

---

### Task 16: `docs/conformidade.md`

**Files:**
- Create: `docs/conformidade.md`

**Interfaces:**
- Consumes: spec seções 6 e 7.
- Produces: documento de referência que o plugin (etapa 2) e a dissertação citam.

- [ ] **Step 1: Escrever o documento**

`docs/conformidade.md`:

```markdown
# Regras de conformidade do vygolint

> O resultado de uma avaliação vygolint expressa **conformidade com as diretrizes de
> Carvalho (2020)** e **não classifica o jogo como sociointeracionista**. Carvalho (2020,
> seção 4.4 e considerações finais) alerta que rotular o jogo e ordenar as diretrizes pode
> distorcer a teoria de Vigotski. Os níveis abaixo ordenam critérios de verificação, não
> a teoria.

## 1. Nível de cada critério

O nível é derivado de dois eixos declarados no catálogo, pela tabela:

| Essencialidade | Viabilidade alta ou média | Viabilidade baixa |
|---|---|---|
| alta | A | AA |
| média | AA | AAA |
| baixa | AAA | AAA |

Regra adicional: diretriz com `modalidade: pode` (D20, D21) nunca gera critério A; o
resultado A sobe para AA.

Definições:

- **Essencialidade alta:** o critério materializa um princípio sem o qual a mecânica é
  behaviorista (resolução de problemas, interação ativa com objetos, mediação por feedback
  orientador, atividade do jogador).
- **Essencialidade média:** socialização, mediação entre pares, autonomia de escolha,
  contextualização realista.
- **Essencialidade baixa:** criação de conteúdo pelo jogador, personalização adaptativa,
  recursos complementares.
- **Viabilidade alta:** implementável em qualquer jogo educacional com mecânicas comuns.
- **Viabilidade média:** exige sistema dedicado (persistência, comunicação assíncrona,
  perfil de desempenho).
- **Viabilidade baixa:** exige infraestrutura rara (multijogador síncrono, editor de
  conteúdo, adaptação em tempo real).

`scripts/build_catalog.py` recalcula o nível de todo critério e falha se o YAML declarar
outro.

## 2. Grau de cada critério

| Grau | Significado |
|---|---|
| atendido | todas as evidências observadas satisfazem o descritor "atendido" |
| parcial | evidências satisfazem só em parte; ver descritor "parcial" |
| não atendido | descritor "não atendido", ou dependência não satisfeita |

Regras:

- O avaliador registra, por fonte usada (código, documentação, vídeo), as provas: trecho,
  página, timestamp.
- Fontes em conflito: vale o pior grau, salvo justificativa escrita. Vídeo prevalece sobre
  documentação.
- Critério com `depende_de` não satisfeito recebe **não atendido** automaticamente.
  `depende_de` é lista de grupos: todos os grupos precisam ser satisfeitos; dentro de um
  grupo basta um critério atendido.
- Não existe "não se aplica" por ausência de recurso. Jogo sem multijogador não atende D06.
  `aplicabilidade` só restringe por contexto de uso (D22).

## 3. Diretriz

Diretriz atendida no nível N quando todos os seus critérios de nível N ou inferior estão
**atendidos**. Parcial não conta.

## 4. Jogo

| Nível do jogo | Exigência |
|---|---|
| A | todos os critérios A atendidos |
| AA | A + todos os critérios AA atendidos |
| AAA | AA + todos os critérios AAA atendidos |
| sem conformidade | qualquer critério A não atendido ou parcial |

## 5. Relatório

Todo relatório contém, nesta ordem:

1. a cláusula do início deste documento;
2. o nível alcançado;
3. cobertura por nível: contagem de atendido, parcial e não atendido para A, AA e AAA;
4. cobertura por categoria: mesma contagem para cada uma das 12 categorias;
5. bloqueios: critérios que impedem o próximo nível, com recomendação;
6. parciais: o que falta para pleno;
7. provas por critério.
```

- [ ] **Step 2: Conferir coerência com a spec**

Comparar com `docs/superpowers/specs/2026-11-03-catalogo-conformidade-design.md` seções 6 e 7. Tabelas e definições devem ser idênticas.

- [ ] **Step 3: Commit**

```bash
git add docs/conformidade.md
git commit -m "docs: conformance rules (levels, grades, aggregation, report)" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 17: README final da etapa 1

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Substituir o README**

```markdown
# vygolint

Catálogo de conformidade e plugin de avaliação de jogos educacionais digitais
contra as 40 diretrizes sociointeracionistas de Carvalho (2020), com níveis
A, AA e AAA no modelo das WCAG.

Fonte das diretrizes: CARVALHO, Diego Marques. *Diretrizes para o desenvolvimento
de jogos educacionais digitais embasados na teoria sociointeracionista de Lev
Semionovich Vigotski*. Dissertação (Mestrado em Ciência da Computação), UFABC, 2020.

## O que há aqui

| Caminho | Conteúdo |
|---|---|
| `catalog/D01.yaml` … `D40.yaml` | uma diretriz por arquivo: texto literal, critérios, níveis, evidências, escalas |
| `catalog/schema.yaml` | esquema validado pelo build |
| `catalog/categorias.yaml` | 12 categorias e a ressalva de Carvalho (2020) |
| `docs/catalogo.md` | catálogo completo, gerado |
| `docs/catalogo.tex` | tabela resumo para LaTeX, gerada |
| `docs/conformidade.md` | regras de nível, grau, agregação e relatório |
| `scripts/build_catalog.py` | valida o catálogo e regenera os docs |
| `skills/` | etapa 2: skills portáveis entre agentes de código |

## Como funciona o nível

Cada critério declara essencialidade teórica e viabilidade; o nível sai de uma
tabela fixa (ver `docs/conformidade.md`). O build falha se o YAML declarar outro
nível. O resultado de uma avaliação expressa conformidade com as diretrizes, não
um rótulo de "jogo sociointeracionista".

## Desenvolvimento

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=scripts python3 -m unittest discover -s tests -v
python3 scripts/build_catalog.py
```

`docs/catalogo.md` e `docs/catalogo.tex` nunca são editados à mão. O CI falha se
estiverem desatualizados.

## Documentos de projeto

- Spec: `docs/superpowers/specs/2026-11-03-catalogo-conformidade-design.md`
- Plano: `docs/superpowers/plans/2026-11-03-catalogo-conformidade.md`
```

- [ ] **Step 2: Rodar tudo uma última vez**

Run: `PYTHONPATH=scripts python3 -m unittest discover -s tests && python3 scripts/build_catalog.py && git diff --exit-code -- docs/ && echo DONE`
Expected: `OK: 40 diretrizes, M critérios` seguido de `DONE`.

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: README for stage 1 catalog" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

## Self-review (feito ao escrever o plano)

- **Cobertura da spec:** seção 4 (estrutura) em Tasks 1, 3, 8; seção 5 (esquema) em Tasks 3 e 4; seção 6 (níveis) em Tasks 2, 4, 16; seção 7 (conformidade) em Task 16; seção 8 (gerador, testes, CI) em Tasks 5, 6, 7, 9; seção 9 (ordem de escrita) em Tasks 8, 10 a 15, 16, 17. Relatório automático e skills ficam fora da etapa 1 por decisão da spec.
- **Placeholders:** tabelas de lote trazem texto literal, eixos e ideia de critério; o YAML completo é autoria do executor por desenho, com formato fixado em Task 8.
- **Consistência de nomes:** `derive_nivel`, `load_yaml`, `validate_diretriz`, `validate_catalogo`, `render_markdown`, `render_latex`, `escape_latex`, `build`, `contagem` usados com as mesmas assinaturas em todas as tarefas. Contagem de testes esperada: 2 + 4 + 16 + 8 + 7 + 3 + 5 = 45.
