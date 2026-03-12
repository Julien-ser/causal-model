# Causal Model for Firmware Update Agent

A causal inference model and visualization dashboard for an agentic loop that manages firmware updates.

## Mission

Create a sample causal model/visualization of an agentic loop for updating firmware. The project uses DoWhy for causal inference and Streamlit for interactive visualization.

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

✅ **Task 1 Complete**: Project setup
- Created directory structure (`src/`, `tests/`, `data/`, `notebooks/`)
- Created `requirements.txt` with core libraries
- Installed dependencies: dowhy, causalml, networkx, plotly, streamlit, pandas, numpy

🔜 **Next**: Phase 1 - Define causal variables and design mock data schema
