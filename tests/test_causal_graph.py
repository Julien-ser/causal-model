"""
Basic validation tests for the causal graph.

These tests ensure the DAG structure is valid and contains expected components.
"""

import pytest
import networkx as nx
from src.causal_graph import (
    create_causal_graph,
    get_variable_descriptions,
    get_causal_effect_hypotheses,
)


class TestCausalGraph:
    """Test suite for causal graph construction."""

    def test_graph_creation(self):
        """Test that the graph is created successfully."""
        G = create_causal_graph()
        assert isinstance(G, nx.DiGraph)

    def test_node_count(self):
        """Test that the graph has the expected number of nodes."""
        G = create_causal_graph()
        assert G.number_of_nodes() == 10

    def test_edge_count(self):
        """Test that the graph has the expected number of edges."""
        G = create_causal_graph()
        assert G.number_of_edges() == 12

    def test_required_nodes_present(self):
        """Test that all required nodes are present."""
        G = create_causal_graph()
        required_nodes = [
            "Update_Trigger",
            "Network_Stability",
            "Device_Resources",
            "Device_Health",
            "Firmware_Version",
            "Device_Configuration",
            "Update_Command",
            "Update_Success",
            "Rollback_Needed",
            "Device_Downtime",
        ]
        for node in required_nodes:
            assert node in G.nodes(), f"Missing node: {node}"

    def test_treatment_node(self):
        """Test that Update_Command exists as the treatment node."""
        G = create_causal_graph()
        assert "Update_Command" in G.nodes()

    def test_outcome_node(self):
        """Test that Update_Success exists as the outcome node."""
        G = create_causal_graph()
        assert "Update_Success" in G.nodes()

    def test_dag_is_acyclic(self):
        """Test that the graph is a DAG (no cycles)."""
        G = create_causal_graph()
        assert nx.is_directed_acyclic_graph(G), "Graph contains cycles!"

    def test_treatment_has_outgoing_edges(self):
        """Test that Update_Command has outgoing edges (affects outcome)."""
        G = create_causal_graph()
        assert G.out_degree("Update_Command") > 0
        assert "Update_Success" in G.successors("Update_Command")

    def test_confounders_have_edges_to_treatment_and_outcome(self):
        """Test that confounders like Firmware_Version affect both treatment and outcome."""
        G = create_causal_graph()
        # Firmware_Version should lead to both Update_Command and Update_Success
        assert "Update_Command" in G.successors("Firmware_Version")
        assert "Update_Success" in G.successors("Firmware_Version")

    def test_moderators_lead_to_outcome(self):
        """Test that moderators (Network_Stability, Device_Resources, Device_Health) affect Update_Success."""
        G = create_causal_graph()
        moderators = ["Network_Stability", "Device_Resources", "Device_Health"]
        for mod in moderators:
            assert "Update_Success" in G.successors(mod), (
                f"{mod} should affect Update_Success"
            )

    def test_variable_descriptions_complete(self):
        """Test that all nodes have descriptions."""
        descriptions = get_variable_descriptions()
        G = create_causal_graph()
        for node in G.nodes():
            assert node in descriptions, f"Missing description for {node}"
            assert len(descriptions[node]) > 0, f"Empty description for {node}"

    def test_effect_hypotheses_defined(self):
        """Test that causal effect hypotheses are defined for key relationships."""
        hypotheses = get_causal_effect_hypotheses()
        key_edges = [
            ("Update_Command", "Update_Success"),
            ("Network_Stability", "Update_Success"),
            ("Device_Resources", "Update_Success"),
            ("Device_Health", "Update_Success"),
        ]
        for edge in key_edges:
            assert edge in hypotheses, f"Missing hypothesis for {edge}"


if __name__ == "__main__":
    # Run tests manually
    pytest.main([__file__, "-v"])
