#!/usr/bin/env python
"""Diagnostic script to test causal engine components."""

import sys
import traceback

try:
    import numpy as np
    import pandas as pd
    import networkx as nx

    print("✓ Basic imports successful")
except Exception as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

try:
    from dowhy import CausalModel

    print("✓ DoWhy imported")
except Exception as e:
    print(f"✗ DoWhy import error: {e}")
    sys.exit(1)

try:
    from src.causal_graph import create_causal_graph
    from src.data_generator import generate_data

    print("✓ Project modules imported")
except Exception as e:
    print(f"✗ Project module import error: {e}")
    traceback.print_exc()
    sys.exit(1)

print("\n--- Test 1: Generate graph ---")
try:
    graph = create_causal_graph()
    print(
        f"✓ Graph created: {graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges"
    )
except Exception as e:
    print(f"✗ Graph creation failed: {e}")
    traceback.print_exc()
    sys.exit(1)

print("\n--- Test 2: Generate data ---")
try:
    data = generate_data(n_samples=50)
    print(f"✓ Data generated: {data.shape}")
    print(f"  Columns: {list(data.columns)}")
except Exception as e:
    print(f"✗ Data generation failed: {e}")
    traceback.print_exc()
    sys.exit(1)

print("\n--- Test 3: Convert graph to DOT string ---")
try:
    # Try using networkx to write dot
    import io
    from networkx.drawing.nx_pydot import write_dot
    from networkx.readwrite import json_graph

    # Try pydot
    try:
        from networkx.drawing.nx_pydot import to_pydot

        pydot_graph = to_pydot(graph)
        dot_string = pydot_graph.to_string()
        print(f"✓ Graph converted to DOT via pydot (length: {len(dot_string)})")
    except Exception as e1:
        print(f"⚠ Pydot conversion failed: {e1}, trying write_dot...")
        buf = io.StringIO()
        write_dot(graph, buf)
        dot_string = buf.getvalue()
        print(f"✓ Graph converted to DOT via write_dot (length: {len(dot_string)})")
except Exception as e:
    print(f"✗ Graph to DOT conversion failed: {e}")
    traceback.print_exc()
    sys.exit(1)

print("\n--- Test 4: Build DoWhy model with DOT string ---")
try:
    model = CausalModel(
        data=data,
        treatment="Update_Command",
        outcome="Update_Success",
        graph=dot_string,
    )
    print(f"✓ DoWhy model created")
    print(f"  Treatment: {model._treatment}")
    print(f"  Outcome: {model._outcome}")
except Exception as e:
    print(f"✗ DoWhy model creation failed: {e}")
    traceback.print_exc()
    sys.exit(1)

print("\n--- Test 5: Identify effect ---")
try:
    estimand = model.identify_effect(proceed_when_unidentifiable=False)
    print(f"✓ Effect identified")
    print(f"  Estimand: {estimand}")
    if hasattr(estimand, "backdoor_variables"):
        print(f"  Backdoor set: {estimand.backdoor_variables}")
except Exception as e:
    print(f"✗ Effect identification failed: {e}")
    traceback.print_exc()
    sys.exit(1)

print("\n--- Test 6: Estimate ATE with linear regression ---")
try:
    estimate = model.estimate_effect(
        estimand, method_name="backdoor.linear_regression", confidence_intervals=True
    )
    print(f"✓ ATE estimated: {estimate.value:.4f}")
    if hasattr(estimate, "std_error"):
        print(f"  Std error: {estimate.std_error:.4f}")
except Exception as e:
    print(f"✗ ATE estimation failed: {e}")
    traceback.print_exc()
    # Don't exit - estimation might fail for various reasons

print("\n✓✓✓ All critical tests passed! ✓✓✓")
