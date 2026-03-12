"""
Causal model for firmware update agent.

This package contains modules for building, testing, and using
the causal inference model for firmware update decisions.
"""

from .causal_graph import (
    create_causal_graph,
    get_variable_descriptions,
    get_causal_effect_hypotheses,
)
from .data_generator import (
    generate_data,
    DataGenerator,
    ALL_VARS,
    TREATMENT,
    OUTCOME,
    SECONDARY_OUTCOMES,
)

__all__ = [
    "create_causal_graph",
    "get_variable_descriptions",
    "get_causal_effect_hypotheses",
    "generate_data",
    "DataGenerator",
    "ALL_VARS",
    "TREATMENT",
    "OUTCOME",
    "SECONDARY_OUTCOMES",
]
