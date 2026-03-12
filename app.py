import streamlit as st
from src.causal_graph import create_causal_graph
from src.data_generator import generate_data
from src.causal_engine import CausalInferenceEngine
from src.visualization import plot_causal_graph
from src.agent import Agent
from src.simulator import Simulator
import pandas as pd

st.set_page_config(page_title="Causal Firmware Update Dashboard", layout="wide")


@st.cache_resource
def load_engine_and_agent():
    data = generate_data(n_samples=1000, seed=42)
    graph = create_causal_graph()
    engine = CausalInferenceEngine(graph, data)
    engine.build_model()
    engine.identify_effect()
    agent = Agent(engine, decision_threshold=0.7)
    return engine, agent


engine, agent = load_engine_and_agent()

st.title("Firmware Update Causal Model Dashboard")
tab1, tab2, tab3 = st.tabs(["Causal Graph", "Agent Performance", "Scenario Simulator"])

with tab1:
    st.header("Causal DAG")
    # Get ATE for edge annotation if available
    result = engine.run_full_analysis()
    ate = result["estimates"].get("linear_regression", {}).get("ate")
    effect_dict = None
    if ate is not None:
        effect_dict = {("Update_Command", "Update_Success"): ate}
    fig = plot_causal_graph(engine.graph, effect_sizes=effect_dict)
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Estimated Average Treatment Effect")
    if ate is not None:
        st.write(f"ATE of Update_Command on Update_Success: **{ate:.4f}**")
    else:
        st.write("ATE not available.")

with tab2:
    st.header("Agent Performance")
    st.write(
        "Simulate the agent's decisions over 100 device episodes and compare against baselines."
    )
    if st.button("Run Simulation", key="run_sim"):
        simulator = Simulator(agent, n_episodes=100, seed=123)
        results = simulator.run()
        col1, col2, col3 = st.columns(3)
        col1.metric("Agent Success Rate", f"{results['agent_success_rate']:.2%}")
        col2.metric(
            "Always Update Success Rate", f"{results['always_update_success_rate']:.2%}"
        )
        col3.metric("Agent Update Rate", f"{results['agent_updates'] / 100:.2%}")
        # Additional metrics
        agent_failure_rate = (
            (results["agent_updates"] - results["agent_success"])
            / results["agent_updates"]
            if results["agent_updates"] > 0
            else 0.0
        )
        agent_rollback_rate = results.get("agent_rollback_rate", 0.0)
        col1, col2 = st.columns(2)
        col1.metric("Agent Failure Rate", f"{agent_failure_rate:.2%}")
        col2.metric("Agent Rollback Rate", f"{agent_rollback_rate:.2%}")
        # Show detailed results
        details_df = pd.DataFrame(results["details"])
        st.subheader("Simulation Details")
        st.dataframe(details_df)
    else:
        st.info("Click the button to run simulation.")

with tab3:
    st.header("Scenario Simulator")
    st.write("Enter specific device state to see what the agent would decide.")
    col_left, col_right = st.columns(2)
    with col_left:
        network_stability = st.slider(
            "Network Stability (0-1)", 0.0, 1.0, 0.9, step=0.01, key="ns"
        )
        device_resources = st.slider(
            "Device Resources (0-1)", 0.0, 1.0, 0.8, step=0.01, key="dr"
        )
        device_health = st.slider(
            "Device Health (0-1)", 0.0, 1.0, 0.9, step=0.01, key="dh"
        )
    with col_right:
        firmware_version = st.selectbox(
            "Firmware Version",
            options=["v1.0", "v1.5", "v2.0", "v2.5", "v3.0"],
            key="fw",
        )
        device_config = st.selectbox(
            "Device Configuration", options=["low", "medium", "high"], key="dc"
        )
        update_trigger = st.selectbox(
            "Update Trigger", options=["manual", "auto", "emergency"], key="trigger"
        )
    if st.button("Get Agent Decision"):
        state = {
            "Network_Stability": network_stability,
            "Device_Resources": device_resources,
            "Device_Health": device_health,
            "Firmware_Version": firmware_version,
            "Device_Configuration": device_config,
            "Update_Trigger": update_trigger,
        }
        agent.perceive(state)
        prob = agent.reason()
        decision = agent.act()
        st.write(f"**Predicted success probability if update issued:** {prob:.2%}")
        if decision == "update":
            st.success("✅ Agent recommends: **YES, perform update**")
        else:
            st.error("❌ Agent recommends: **NO, do not update**")
