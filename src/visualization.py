"""
Causal graph visualization using Plotly.

Provides functions to visualize the causal DAG with optional effect size annotations.
"""

import plotly.graph_objects as go
import networkx as nx


def plot_causal_graph(
    graph: nx.DiGraph, effect_sizes: dict = None, confidence_intervals: dict = None
) -> go.Figure:
    """
    Create an interactive Plotly figure of the causal graph.

    Args:
        graph: NetworkX DiGraph representing causal structure.
        effect_sizes: Optional dictionary mapping edges (u,v) to numeric effect values.
        confidence_intervals: Optional dictionary mapping edges (u,v) to (lower, upper) tuples.

    Returns:
        Plotly Figure object.
    """
    # Compute node positions using a spring layout (deterministic with seed)
    pos = nx.spring_layout(graph, seed=42)

    # Prepare edge traces (lines)
    edge_x = []
    edge_y = []
    edge_text = []
    for u, v in graph.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        label = f"{u} → {v}"
        if effect_sizes and (u, v) in effect_sizes:
            effect = effect_sizes[(u, v)]
            ci_str = ""
            if confidence_intervals and (u, v) in confidence_intervals:
                low, high = confidence_intervals[(u, v)]
                ci_str = f" (95% CI: {low:.3f} – {high:.3f})"
            label += f": {effect:.3f}{ci_str}"
        edge_text.append(label)

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        line=dict(width=2, color="gray"),
        hoverinfo="text",
        text=edge_text,
        name="Edges",
    )

    # Prepare node trace
    node_x = []
    node_y = []
    node_text = []
    for node in graph.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=node_text,
        textposition="bottom center",
        marker=dict(size=30, color="lightblue", line=dict(width=2, color="darkblue")),
        hoverinfo="text",
        name="Nodes",
    )

    # Create figure
    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        title="Causal Graph",
        showlegend=False,
        hovermode="closest",
        margin=dict(b=20, l=5, r=5, t=40),
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
    )
    return fig
