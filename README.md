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

## Synthetic Data Generation

The project includes a comprehensive synthetic data generator (`src/data_generator.py`) that simulates realistic firmware update scenarios.

### Features

- Generates 1000+ firmware update attempts with realistic confounding variables
- Respects causal DAG structure: treatment affects outcome, confounders influence both
- Categorical variables: `Update_Trigger` (manual/auto/emergency), `Firmware_Version` (v1.0-v3.0), `Device_Configuration` (low/medium/high)
- Continuous variables: `Network_Stability`, `Device_Resources`, `Device_Health` (0-1 scores)
- Binary outcomes: `Update_Command` (treatment), `Update_Success` (outcome), `Rollback_Needed`
- Continuous outcome: `Device_Downtime` (seconds)

### Usage

```python
from src.data_generator import generate_data, DataGenerator

# Quick generation
data = generate_data(n_samples=1000, random_seed=42)

# Custom configuration
config = DataGeneratorConfig(
    n_samples=2000,
    network_stability_mean=0.7,
    treatment_effect_size=0.25
)
generator = DataGenerator(config)
data = generator.generate()

# Generate interventional data (set all devices to receive update command)
interventional_data = generator.generate_interventional_data(treatment_value=1)
```

### Testing

The data generator includes 17 comprehensive unit tests covering:
- Data structure and variable types
- Causal relationships (e.g., older firmware → more updates)
- Effect sizes (e.g., better network → higher success rate)
- Reproducibility with random seeds

Run tests: `pytest tests/test_data_generator.py -v`

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
- ✅ Implement causal graph using networkx with required nodes
- ✅ Create synthetic data generator (`src/data_generator.py`)
  - Generates 1000 realistic firmware update attempts
  - Respects causal DAG structure with confounders
  - Includes both observational and interventional data generation
  - Comprehensive unit tests (17 tests passing)
- ⏳ Build causal inference engine
- ⏳ Write unit tests for backdoor criteria and effect estimation
