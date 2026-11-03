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
