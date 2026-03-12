# causal-model
**Mission:** Create a sample causal model/visualization of an agentic loop for updating firmware

## Phase 1: Planning & Setup
- [x] Define causal variables (firmware state, update trigger, network reliability, device health) and hypothesize relationships in a DAG
- [x] Set up Python project structure with `src/`, `tests/`, `data/`, and `notebooks/` directories; create `requirements.txt`
- [x] Install core libraries: `doWhy`, `causalml`, `networkx`, `plotly`, `streamlit`, `pandas`, `numpy`
- [x] Design mock data schema for firmware versions, update attempts, failure modes, and outcomes

## Phase 2: Causal Model Development
- [x] Implement causal graph using `networkx` with nodes: `Update_Command`, `Network_Stability`, `Device_Resources`, `Update_Success`, `Rollback_Needed`
- [x] Create synthetic data generator in `src/data_generator.py` that simulates 1000 firmware update attempts with confounding variables
- [ ] Build causal inference engine in `src/causal_engine.py` using DoWhy to identify causal effect of `Update_Command` on `Update_Success`
- [ ] Write unit tests in `tests/test_causal.py` validating backdoor criteria and effect estimation

## Phase 3: Agentic Loop Implementation
- [ ] Design agent architecture with perception (observe device state), reasoning (apply causal model), and action (decide update/rollback) modules
- [ ] Implement `Agent` class in `src/agent.py` that observes current firmware state and uses causal effects to recommend action
- [ ] Create policy function that maps predicted success probability to update decision threshold
- [ ] Build simulation loop in `src/simulator.py` that runs 100 agent decisions and tracks outcomes vs. baseline

## Phase 4: Visualization & Dashboard
- [ ] Build causal graph visualization with `plotly` showing DAG with effect sizes and confidence intervals in `src/visualization.py`
- [ ] Create interactive Streamlit dashboard in `app.py` with tabs: Causal Graph, Agent Performance, Scenario Simulator
- [ ] Implement real-time metrics panel showing agent win rate, false positives, and rollback frequency
- [ ] Write `README.md` with setup instructions, causal assumptions, and example scenarios; add `docker-compose.yml` for one-command deployment
