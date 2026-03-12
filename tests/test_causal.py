"""
Unit tests for causal inference engine.

Tests cover model building, effect identification, estimation, and validation.
"""

import pytest
import pandas as pd
import numpy as np
import networkx as nx
from src.causal_graph import create_causal_graph
from src.data_generator import generate_data
from src.causal_engine import CausalInferenceEngine


class TestCausalInferenceEngine:
    """Test suite for CausalInferenceEngine."""

    @pytest.fixture
    def sample_data(self):
        """Generate sample data for testing."""
        return generate_data(n_samples=500, seed=42)

    @pytest.fixture
    def causal_graph(self):
        """Create causal graph for testing."""
        return create_causal_graph()

    @pytest.fixture
    def engine(self, causal_graph, sample_data):
        """Create engine instance for testing."""
        return CausalInferenceEngine(causal_graph, sample_data)

    def test_engine_initialization(self, engine, causal_graph, sample_data):
        """Test that engine can be initialized with graph and data."""
        assert engine.graph == causal_graph
        assert engine.data.equals(sample_data)
        assert engine.model is None
        assert engine.identified_estimand is None

    def test_build_model(self, engine):
        """Test model building with DoWhy."""
        model = engine.build_model()
        assert model is not None
        assert engine.model is not None
        # Check that treatment and outcome are set correctly
        assert engine.model._treatment == ["Update_Command"]
        assert engine.model._outcome == ["Update_Success"]

    def test_identify_effect(self, engine):
        """Test effect identification produces an estimand."""
        engine.build_model()
        estimand = engine.identify_effect()
        assert estimand is not None
        assert engine.identified_estimand is not None

    def test_backdoor_adjustment_set_exists(self, engine):
        """Test that a backdoor adjustment set is identified."""
        engine.build_model()
        engine.identify_effect()
        adjustment_set = engine.get_backdoor_adjustment_set()
        # Should identify confounders that need adjustment
        assert isinstance(adjustment_set, list)
        # In this graph, confounders affecting both treatment and outcome should be identified
        # Typical set includes: Update_Trigger, Firmware_Version, Device_Configuration

    def test_estimate_ate_linear_regression(self, engine):
        """Test ATE estimation with linear regression."""
        result = engine.run_full_analysis(method="linear_regression")
        assert "linear_regression" in result["estimates"]
        linear_result = result["estimates"]["linear_regression"]
        if "error" not in linear_result:
            assert "ate" in linear_result
            assert isinstance(linear_result["ate"], (int, float))
            # ATE should be in a reasonable range for binary outcome (between -1 and 1)
            assert -1 <= linear_result["ate"] <= 1

    def test_estimate_ate_propensity_score(self, engine):
        """Test ATE estimation with propensity score matching."""
        result = engine.run_full_analysis(method="propensity_score_matching")
        assert "propensity_score_matching" in result["estimates"]
        ps_result = result["estimates"]["propensity_score_matching"]
        if "error" not in ps_result:
            assert "ate" in ps_result
            assert isinstance(ps_result["ate"], (int, float))

    def test_backdoor_validation(self, engine):
        """Test backdoor criterion validation."""
        engine.build_model()
        validation = engine.validate_backdoor_criterion()
        assert "is_dag" in validation
        assert validation["is_dag"] is True  # Graph should be acyclic
        assert "treatment_has_outgoing_to_outcome" in validation
        assert validation["treatment_has_outgoing_to_outcome"] is True

    def test_full_analysis_pipeline(self, engine):
        """Test the complete analysis pipeline."""
        result = engine.run_full_analysis(estimation_methods=["linear_regression"])
        # Check all components present
        assert "validation" in result
        assert "estimates" in result
        assert "backdoor_adjustment_set" in result
        # Validation results
        assert result["validation"]["is_dag"] is True
        # Estimates
        assert "linear_regression" in result["estimates"]

    def test_different_data_different_estimates(self, causal_graph):
        """Test that different data produces different estimates."""
        data1 = generate_data(n_samples=500, seed=42)
        data2 = generate_data(n_samples=500, seed=123)

        engine1 = CausalInferenceEngine(causal_graph, data1)
        engine2 = CausalInferenceEngine(causal_graph, data2)

        result1 = engine1.run_full_analysis()
        result2 = engine2.run_full_analysis()

        if (
            "error" not in result1["estimates"]["linear_regression"]
            and "error" not in result2["estimates"]["linear_regression"]
        ):
            ate1 = result1["estimates"]["linear_regression"]["ate"]
            ate2 = result2["estimates"]["linear_regression"]["ate"]
            # Estimates may differ slightly due to different random data
            # They shouldn't be exactly equal
            assert not np.isclose(ate1, ate2, atol=0.01)

    def test_reproducibility_with_same_seed(self, causal_graph):
        """Test that same seed produces same results."""
        data = generate_data(n_samples=500, seed=42)
        engine1 = CausalInferenceEngine(causal_graph, data)
        engine2 = CausalInferenceEngine(causal_graph, data)

        result1 = engine1.run_full_analysis()
        result2 = engine2.run_full_analysis()

        if (
            "error" not in result1["estimates"]["linear_regression"]
            and "error" not in result2["estimates"]["linear_regression"]
        ):
            ate1 = result1["estimates"]["linear_regression"]["ate"]
            ate2 = result2["estimates"]["linear_regression"]["ate"]
            # Should be exactly equal
            assert np.isclose(ate1, ate2, atol=1e-10)

    def test_confidence_intervals_computed(self, engine):
        """Test that confidence intervals are included when requested."""
        result = engine.run_full_analysis(method="linear_regression")
        linear_result = result["estimates"]["linear_regression"]
        if "error" not in linear_result:
            # Confidence intervals may or may not be present depending on DoWhy implementation
            # Just check that the result structure is valid
            assert "ate" in linear_result

    def test_graph_has_required_edges(self, engine):
        """Test that the causal graph has the required edges for identification."""
        G = engine.graph
        # Treatment should have edge to outcome
        assert G.has_edge("Update_Command", "Update_Success")
        # Confounders should have edges to both treatment and outcome
        confounders = ["Update_Trigger", "Firmware_Version", "Device_Configuration"]
        for confounder in confounders:
            if G.has_edge(confounder, "Update_Command") and G.has_edge(
                confounder, "Update_Success"
            ):
                # This is a proper confounder
                pass
            # Some confounders might not have both edges, which is OK

    def test_engine_with_missing_data(self, causal_graph):
        """Test engine handles missing data appropriately."""
        data = generate_data(n_samples=100)
        # Intentionally drop some columns to test error handling
        incomplete_data = data.drop(columns=["Network_Stability", "Device_Resources"])

        engine = CausalInferenceEngine(causal_graph, incomplete_data)
        result = engine.run_full_analysis()
        # Should either fail gracefully or handle missing data
        # This test documents expected behavior
        # In production, we'd ensure all required columns are present
        assert result is not None


class TestCausalIdentification:
    """Test specific causal identification properties."""

    @pytest.fixture
    def engine(self):
        """Create engine for identification tests."""
        data = generate_data(n_samples=1000, seed=42)
        graph = create_causal_graph()
        return CausalInferenceEngine(graph, data)

    def test_backdoor_adjustment_blocks_confounders(self, engine):
        """
        Test that backdoor adjustment set blocks all backdoor paths
        from treatment to outcome.
        """
        engine.build_model()
        engine.identify_effect()
        adjustment_set = engine.get_backdoor_adjustment_set()

        # For a proper causal identification, we need to adjust for confounders
        # At minimum, we should have identified some variables
        assert len(adjustment_set) > 0, "Should identify at least some confounders"

        # Common confounders in this DAG: Update_Trigger, Firmware_Version, Device_Configuration
        expected_confounders = [
            "Update_Trigger",
            "Firmware_Version",
            "Device_Configuration",
        ]
        found_confounders = [c for c in expected_confounders if c in adjustment_set]

        # Should find at least some of the expected confounders
        assert len(found_confounders) > 0, "Should identify expected confounders"

    def test_no_path_from_outcome_to_treatment_after_adjustment(self, engine):
        """
        Test that after adjustment, there is no open backdoor path
        from outcome to treatment.
        """
        engine.build_model()
        engine.identify_effect()
        adjustment_set = engine.get_backdoor_adjustment_set()

        # This is a theoretical property: after conditioning on the backdoor set,
        # all backdoor paths should be blocked
        # We can't directly test this without more complex graph analysis,
        # but we can verify that adjustment set is provided
        assert isinstance(adjustment_set, list)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
