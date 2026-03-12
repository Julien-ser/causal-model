# Causal Model for Firmware Update Agent

A causal inference model and visualization dashboard for an agentic loop that manages firmware updates.

## Mission

Create a sample causal model/visualization of an agentic loop for updating firmware. The project uses DoWhy for causal inference and Streamlit for interactive visualization.

## Causal Model

### DAG Structure

The causal graph includes these variables:
- **Update_Trigger**: Initiates update (manual, auto, emergency)
- **Network_Stability**: Network quality (0-1 score)
- **Device_Resources**: CPU, memory, storage availability
- **Device_Health**: Battery, temperature, hardware status
- **Device_Configuration**: Settings, encryption, policies
- **Firmware_Version**: Current version (older harder to update)
- **Update_Command**: Treatment - whether update command issued
- **Update_Success**: Outcome - whether update succeeded
- **Rollback_Needed**: Whether rollback was required
- **Device_Downtime**: Downtime duration during update

### Key Relationships

- Main effect: `Update_Command` → `Update_Success`
- Moderators: `Network_Stability`, `Device_Resources`, `Device_Health` → `Update_Success`
- Confounders: `Firmware_Version`, `Device_Configuration` affect both treatment and outcome
- Consequences: `Update_Success` → `Rollback_Needed, Device_Downtime`

See `src/causal_graph.py` for complete definition.

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit dashboard (once implemented)
streamlit run app.py
```

## Project Structure

- `src/` - Source code (data generator, causal engine, agent, simulator, visualization)
- `tests/` - Unit and integration tests
- `data/` - Synthetic and generated data
- `notebooks/` - Jupyter notebooks for exploration
- `app.py` - Streamlit dashboard (to be created)

## Current Progress

✅ **Phase 1 Complete** - Planning & Setup
- ✅ Task 1: Defined causal variables and designed DAG with hypothesized relationships
- ✅ Task 2: Set up Python project structure (src/, tests/, data/, notebooks/)
- ✅ Task 3: Created requirements.txt with core libraries (doWhy, causalml, networkx, plotly, streamlit, pandas, numpy)
- ✅ Task 4: Designed mock data schema (see data/SCHEMA.md)

🔄 **Phase 2 In Progress** - Causal Model Development
- ⏳ Implement causal graph using networkx
- ⏳ Create synthetic data generator
- ⏳ Build causal inference engine
- ⏳ Write unit tests
