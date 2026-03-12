"""
Causal graph definition for firmware update agent model.

This module defines the causal variables and their relationships in a DAG
representing the firmware update process.
"""

import networkx as nx
from typing import Dict, List, Tuple


def create_causal_graph() -> nx.DiGraph:
    """
    Create and return the causal DAG for the firmware update system.

    Returns:
        nx.DiGraph: Directed acyclic graph representing causal relationships
    """
    G = nx.DiGraph()

    # Define nodes (causal variables)
    nodes = [
        # Root causes / exogenous variables
        "Update_Trigger",  # What initiates the update (manual, auto, emergency)
        "Network_Stability",  # Quality of network connection
        "Device_Resources",  # Available CPU, memory, storage
        "Device_Health",  # Battery level, temperature, hardware status
        "Firmware_Version",  # Current version (older may be harder to update)
        "Device_Configuration",  # Settings, encryption, security policies
        # Intermediate variables
        "Update_Command",  # The actual update command issued
        # Outcome variables
        "Update_Success",  # Whether update completed successfully
        "Rollback_Needed",  # Whether rollback was required after failure
        "Device_Downtime",  # Time device was unavailable during update
    ]

    G.add_nodes_from(nodes)

    # Define edges (causal relationships)
    edges = [
        # Update_Trigger influences Update_Command directly
        ("Update_Trigger", "Update_Command"),
        # Network_Stability directly affects Update_Success
        ("Network_Stability", "Update_Success"),
        # Device_Resources directly affect Update_Success
        ("Device_Resources", "Update_Success"),
        # Device_Health directly affects Update_Success
        ("Device_Health", "Update_Success"),
        # Device_Configuration may affect both command and success
        ("Device_Configuration", "Update_Command"),
        ("Device_Configuration", "Update_Success"),
        # Firmware_Version may affect both command and success
        ("Firmware_Version", "Update_Command"),
        ("Firmware_Version", "Update_Success"),
        # Update_Command directly affects Update_Success (main treatment effect)
        ("Update_Command", "Update_Success"),
        # Update_Success determines Rollback_Needed
        ("Update_Success", "Rollback_Needed"),
        # Update_Success influences Device_Downtime
        ("Update_Success", "Device_Downtime"),
        # Network_Stability also affects downtime via reconnection attempts
        ("Network_Stability", "Device_Downtime"),
    ]

    G.add_edges_from(edges)

    return G


def get_variable_descriptions() -> Dict[str, str]:
    """
    Get human-readable descriptions of each causal variable.

    Returns:
        Dict mapping variable names to descriptions
    """
    return {
        "Update_Trigger": "What initiates the update (manual, automatic, emergency)",
        "Network_Stability": "Quality of network connection (0-1 score)",
        "Device_Resources": "Available system resources (CPU, memory, storage)",
        "Device_Health": "Battery level, temperature, hardware status",
        "Firmware_Version": "Current firmware version (older versions harder to update)",
        "Device_Configuration": "Device settings, encryption, security policies",
        "Update_Command": "Binary: whether update command was issued (treatment)",
        "Update_Success": "Binary: whether update completed successfully (outcome)",
        "Rollback_Needed": "Binary: whether rollback was required after failure",
        "Device_Downtime": "Time device was unavailable during update (seconds)",
    }


def get_causal_effect_hypotheses() -> Dict[Tuple[str, str], str]:
    """
    Get hypothesized causal effects between variables.

    Returns:
        Dict mapping (cause, effect) pairs to hypothesis descriptions
    """
    return {
        (
            "Update_Command",
            "Update_Success",
        ): "Main effect: Issuing update command increases success probability, but magnitude depends on network, resources, and device health.",
        (
            "Network_Stability",
            "Update_Success",
        ): "Better network stability increases update success probability by reducing connection drops and corruption.",
        (
            "Device_Resources",
            "Update_Success",
        ): "More available resources (CPU, memory, storage) improve update success by allowing proper installation.",
        (
            "Device_Health",
            "Update_Success",
        ): "Good device health (battery, temperature) is critical for successful update completion.",
        (
            "Update_Trigger",
            "Update_Command",
        ): "Different trigger types may lead to different update command patterns (e.g., emergency triggers more frequently).",
        (
            "Firmware_Version",
            "Update_Success",
        ): "Older firmware versions may be harder to update due to compatibility issues.",
    }


if __name__ == "__main__":
    # Quick test: create graph and print info
    G = create_causal_graph()
    print(
        f"Causal graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges"
    )
    print("\nNodes:", list(G.nodes()))
    print("\nEdges:", list(G.edges()))
    print("\nVariable descriptions:")
    for var, desc in get_variable_descriptions().items():
        print(f"  {var}: {desc}")
