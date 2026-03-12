"""
Causal inference engine for firmware update agent model.

This module implements causal effect estimation using DoWhy to identify
the causal effect of Update_Command on Update_Success, controlling for
confounders identified in the causal graph.
"""

import pandas as pd
import numpy as np
import networkx as nx
from typing import Dict, Tuple, Optional
from dowhy import CausalModel
from dowhy.causal_identifier import IdentifiedEstimand
import warnings
import io
from networkx.drawing.nx_pydot import write_dot

warnings.filterwarnings("ignore")


class CausalInferenceEngine:
    """
    Engine for estimating causal effects in the firmware update domain.

    Uses DoWhy to:
    - Build causal model from graph and data
    - Identify appropriate adjustment sets
    - Estimate average treatment effects (ATE)
    - Provide confidence intervals
    - Validate backdoor criteria
    """

    def __init__(self, graph: nx.DiGraph, data: pd.DataFrame):
        """
        Initialize the causal inference engine.

        Args:
            graph: NetworkX DiGraph representing causal structure
            data: DataFrame containing all variables in the graph
        """
        self.graph = graph
        self.data = data
        self.model: Optional[CausalModel] = None
        self.identified_estimand = None
        self.estimate_result = None
        self.backdoor_adjustment_set = None

    def _graph_to_dot(self, graph: nx.DiGraph) -> str:
        """Convert NetworkX graph to DOT string for DoWhy."""
        buf = io.StringIO()
        write_dot(graph, buf)
        return buf.getvalue()

    def build_model(
        self, treatment: str = "Update_Command", outcome: str = "Update_Success"
    ) -> CausalModel:
        """
        Build DoWhy causal model from graph and data.

        Args:
            treatment: Name of treatment variable
            outcome: Name of outcome variable

        Returns:
            Configured CausalModel instance
        """
        # Convert NetworkX graph to DOT string format
        graph_dot = self._graph_to_dot(self.graph)

        # Create DoWhy model using DOT graph
        self.model = CausalModel(
            data=self.data, treatment=treatment, outcome=outcome, graph=graph_dot
        )

        return self.model

    def identify_effect(self, method: str = "backdoor") -> IdentifiedEstimand:
        """
        Identify causal effect using backdoor criterion.

        Args:
            method: Identification method ("backdoor", "frontdoor", etc.)

        Returns:
            Identified estimand object
        """
        if self.model is None:
            self.build_model()

        self.identified_estimand = self.model.identify_effect(
            proceed_when_unidentifiable=False
        )

        # Extract backdoor adjustment set if available
        if hasattr(self.identified_estimand, "backdoor_variables"):
            self.backdoor_adjustment_set = getattr(
                self.identified_estimand, "backdoor_variables", []
            )

        return self.identified_estimand

    def estimate_ate(
        self,
        method: str = "linear_regression",
        confidence_intervals: bool = True,
        **kwargs,
    ) -> Dict:
        """
        Estimate Average Treatment Effect (ATE).

        Args:
            method: Estimation method ("linear_regression", "propensity_score_matching", etc.)
            confidence_intervals: Whether to compute confidence intervals
            **kwargs: Additional arguments passed to the estimator

        Returns:
            Dictionary with effect estimate, standard error, and confidence intervals
        """
        if self.identified_estimand is None:
            self.identify_effect()

        # Choose estimator based on method
        if method == "linear_regression":
            estimate = self.model.estimate_effect(
                self.identified_estimand,
                method_name="backdoor.linear_regression",
                confidence_intervals=confidence_intervals,
                **kwargs,
            )
        elif method == "propensity_score_matching":
            estimate = self.model.estimate_effect(
                self.identified_estimand,
                method_name="backdoor.propensity_score_matching",
                confidence_intervals=confidence_intervals,
                **kwargs,
            )
        elif method == "propensity_score_stratification":
            estimate = self.model.estimate_effect(
                self.identified_estimand,
                method_name="backdoor.propensity_score_stratification",
                confidence_intervals=confidence_intervals,
                **kwargs,
            )
        else:
            raise ValueError(f"Unsupported method: {method}")

        self.estimate_result = estimate

        # Extract results into dictionary
        result_dict = {
            "ate": estimate.value,
            "method": method,
            "treatment": self.model._treatment,
            "outcome": self.model._outcome,
        }

        if hasattr(estimate, "std_error") and estimate.std_error is not None:
            result_dict["std_error"] = estimate.std_error

        if (
            hasattr(estimate, "confidence_intervals")
            and estimate.confidence_intervals is not None
        ):
            result_dict["ci_lower"] = estimate.confidence_intervals[0]
            result_dict["ci_upper"] = estimate.confidence_intervals[1]

        return result_dict

    def get_backdoor_adjustment_set(self) -> list:
        """
        Get the set of variables needed to adjust for backdoor confounding.

        Returns:
            List of variable names to adjust for
        """
        if self.backdoor_adjustment_set is None:
            self.identify_effect()
        return self.backdoor_adjustment_set if self.backdoor_adjustment_set else []

    def validate_backdoor_criterion(
        self, treatment: str = "Update_Command", outcome: str = "Update_Success"
    ) -> Dict:
        """
        Validate that the backdoor criterion is satisfied.

        Returns:
            Dictionary with validation results
        """
        validation = {
            "is_dag": nx.is_directed_acyclic_graph(self.graph),
            "treatment_has_outgoing_to_outcome": outcome
            in self.graph.successors(treatment),
            "confounders_identified": len(self.get_backdoor_adjustment_set()) > 0,
            "adjustment_set": self.get_backdoor_adjustment_set(),
        }

        # Check if any backdoor paths exist (paths from outcome to treatment)
        # In a proper DAG with confounders, there should be backdoor paths that need closing
        try:
            all_paths = list(
                nx.all_simple_paths(self.graph.to_undirected(), treatment, outcome)
            )
            # Simple paths of length > 1 (direct edge doesn't count)
            backdoor_paths = [
                p
                for p in all_paths
                if len(p) > 2 and p[0] == outcome and p[-1] == treatment
            ]
            validation["backdoor_paths_found"] = len(backdoor_paths)
        except Exception as e:
            validation["backdoor_paths_found"] = 0

        return validation

    def run_full_analysis(
        self,
        treatment: str = "Update_Command",
        outcome: str = "Update_Success",
        estimation_methods: list = None,
        method: str = None,
    ) -> Dict:
        """
        Run complete causal analysis pipeline.

        Args:
            treatment: Treatment variable name
            outcome: Outcome variable name
            estimation_methods: List of estimation methods to try
            method: Single estimation method (convenience parameter)

        Returns:
            Dictionary with all results
        """
        if method is not None:
            estimation_methods = [method]
        if estimation_methods is None:
            # Default to fast methods only; propensity score methods can be very slow
            estimation_methods = ["linear_regression"]

        # Build model
        self.build_model(treatment, outcome)

        # Identify effect
        self.identify_effect()

        # Get validation results
        validation = self.validate_backdoor_criterion(treatment, outcome)

        # Estimate with multiple methods
        results = {}
        for method in estimation_methods:
            try:
                result = self.estimate_ate(method=method)
                results[method] = result
            except Exception as e:
                results[method] = {"error": str(e)}

        return {
            "validation": validation,
            "estimates": results,
            "backdoor_adjustment_set": self.get_backdoor_adjustment_set(),
        }
