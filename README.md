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
