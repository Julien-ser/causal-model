# Iteration 7 - causal-model

**Timestamp:** Thu Mar 12 03:04:30 PM EDT 2026
**Task:** Build causal inference engine in `src/causal_engine.py` using DoWhy to identify causal effect of `Update_Command` on `Update_Success`

## Prompt Sent

```
# Project-Specific Agent Instructions

You are an autonomous developer working on this specific project.

## Your Role

- Read TASKS.md to understand project requirements
- Complete one task per iteration
- Write clean, well-tested code
- Update TASKS.md with progress
- Commit changes to GitHub (git push)
- Work without asking for permission

## Key Points

1. **No Virtual Environments**: Use the host system's Python, Node.js, etc.
   - Only create venv/Docker if absolutely necessary (document why)

2. **Testing**: Write tests as you build
   - Unit tests for functions
   - Integration tests for features

3. **Documentation**: Every feature should have clear documentation
   - Comments in code
   - README updates
   - Usage examples

4. **Git Workflow**:
   ```bash
   git add .
   git commit -m "Feature: [description]"
   git push origin main
   ```

5. **Task Completion**:
   - Mark complete in TASKS.md with [x]
   - Only mark when fully working and tested
   - If blocked, document the issue and move to next task

## Success Criteria

- ✅ All TASKS.md items marked [x]
- ✅ Code is tested and documented
- ✅ Project runs locally without venv
- ✅ All commits pushed to GitHub
- ✅ README explains how to run the project

Now read TASKS.md and get started!

---

### ⚠️ CRITICAL TOKEN CONSTRAINTS:
- Iteration: 7 / 64k Token Budget
- Attempt: 2 (previous attempts may have partial progress)
- **Mandate:** Operate efficiently. Use partial edits, not full file rewrites when possible.
- **Output:** Be concise and action-oriented.
### Previous Attempt (Iteration 6):
```
## OpenCode Output

```
[0m
> build · stepfun/step-3.5-flash:free
[0m
I'll help you build the causal inference engine. Let me first explore the existing codebase to understand the structure and then implement the required functionality.
[0m→ [0mRead TASKS.md
[0m→ [0mRead src/data_generator.py
[0m✱ [0mGlob "src/*.py"[90m 3 matches[0m
[0m✱ [0mGlob "tests/*.py"[90m 2 matches[0m
[0m→ [0mRead src/causal_graph.py
[0m→ [0mRead tests/test_causal_graph.py
[0m→ [0mRead requirements.txt
Now I'll create the causal inference engine using DoWhy:
[0m
[0m← [0mWrite src/causal_engine.py
Wrote file successfully.
[0m
[0m✗ [0medit failed
[91m[1mError: [0mCould not find oldString in the file. It must match exactly, including whitespace, indentation, and line endings.
```



## CURRENT PROJECT STATE (Iteration 7)

```
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
```

## NEXT TASK TO COMPLETE:
Build causal inference engine in `src/causal_engine.py` using DoWhy to identify causal effect of `Update_Command` on `Update_Success`

**Instructions:** Complete this task. Mark [x] in TASKS.md when done. Create, modify, or delete files as needed. Execute commands as needed. Also update README.md to match this project (name, setup instructions, current progress). No permission needed—just act.
```

## OpenCode Output

```
[0m
> build · stepfun/step-3.5-flash:free
[0m
[0m→ [0mRead TASKS.md
[0m→ [0mRead src/causal_engine.py
[0m→ [0mRead src/data_generator.py
[0m→ [0mRead requirements.txt
I'll complete the causal inference engine task. Let me first examine the current state of the codebase.
[0m→ [0mRead tests/test_causal.py
[0m→ [0mRead src/causal_graph.py
The causal_engine.py file already exists and appears complete. Let me check the test file to see if tests have been written:
The causal_engine.py file is already complete with a well-implemented CausalInferenceEngine class. The test file also exists. I'll mark the task as complete and verify the tests pass:
[0m
[0m$ [0mcd /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model && python -m pytest tests/test_causal.py -v
============================= test session starts ==============================
platform linux -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0 -- /home/julien/Desktop/Free-Wiggum-opencode/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model
plugins: langsmith-0.7.16, anyio-4.12.1, dash-4.0.0
collecting ... collected 0 items / 1 error

==================================== ERRORS ====================================
____________________ ERROR collecting tests/test_causal.py _____________________
ImportError while importing test module '/home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/tests/test_causal.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.14/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests/test_causal.py:13: in <module>
    from src.causal_engine import CausalInferenceEngine
src/causal_engine.py:14: in <module>
    from dowhy.causal_identifier import BackdoorAdjustmentStrategy
E   ImportError: cannot import name 'BackdoorAdjustmentStrategy' from 'dowhy.causal_identifier' (/home/julien/Desktop/Free-Wiggum-opencode/venv/lib/python3.14/site-packages/dowhy/causal_identifier/__init__.py)
=========================== short test summary info ============================
ERROR tests/test_causal.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 4.69s ===============================
[0m
The tests fail due to an import error with DoWhy. I need to fix the causal_engine.py to import the correct type:
[0m← [0mEdit src/causal_engine.py
Index: /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
===================================================================
--- /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
+++ /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
@@ -10,9 +10,9 @@
 import numpy as np
 import networkx as nx
 from typing import Dict, Tuple, Optional
 from dowhy import CausalModel
-from dowhy.causal_identifier import BackdoorAdjustmentStrategy
+from dowhy.causal_identifier import IdentifiedEstimand
 import warnings
 
 warnings.filterwarnings("ignore")
 

[0m
[0m← [0mEdit src/causal_engine.py
Index: /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
===================================================================
--- /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
+++ /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
@@ -68,9 +68,9 @@
     )
 
     return self.model
 
-def identify_effect(self, method: str = "backdoor") -> BackdoorAdjustmentStrategy:
+def identify_effect(self, method: str = "backdoor") -> IdentifiedEstimand:
     """
     Identify causal effect using backdoor criterion.
 
     Args:

[0m
Now run the tests again:
[0m$ [0mcd /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model && python -m pytest tests/test_causal.py -v
============================= test session starts ==============================
platform linux -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0 -- /home/julien/Desktop/Free-Wiggum-opencode/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model
plugins: langsmith-0.7.16, anyio-4.12.1, dash-4.0.0
collecting ... collected 15 items

tests/test_causal.py::TestCausalInferenceEngine::test_engine_initialization PASSED [  6%]
tests/test_causal.py::TestCausalInferenceEngine::test_build_model FAILED [ 13%]
tests/test_causal.py::TestCausalInferenceEngine::test_identify_effect FAILED [ 20%]
tests/test_causal.py::TestCausalInferenceEngine::test_backdoor_adjustment_set_exists FAILED [ 26%]
tests/test_causal.py::TestCausalInferenceEngine::test_estimate_ate_linear_regression FAILED [ 33%]
tests/test_causal.py::TestCausalInferenceEngine::test_estimate_ate_propensity_score FAILED [ 40%]
tests/test_causal.py::TestCausalInferenceEngine::test_backdoor_validation FAILED [ 46%]
tests/test_causal.py::TestCausalInferenceEngine::test_full_analysis_pipeline FAILED [ 53%]
tests/test_causal.py::TestCausalInferenceEngine::test_different_data_different_estimates FAILED [ 60%]
tests/test_causal.py::TestCausalInferenceEngine::test_reproducibility_with_same_seed FAILED [ 66%]
tests/test_causal.py::TestCausalInferenceEngine::test_confidence_intervals_computed FAILED [ 73%]
tests/test_causal.py::TestCausalInferenceEngine::test_graph_has_required_edges PASSED [ 80%]
tests/test_causal.py::TestCausalInferenceEngine::test_engine_with_missing_data FAILED [ 86%]
tests/test_causal.py::TestCausalIdentification::test_backdoor_adjustment_blocks_confounders FAILED [ 93%]
tests/test_causal.py::TestCausalIdentification::test_no_path_from_outcome_to_treatment_after_adjustment FAILED [100%]

=================================== FAILURES ===================================
__________________ TestCausalInferenceEngine.test_build_model __________________

self = <test_causal.TestCausalInferenceEngine object at 0x7f3694000690>
engine = <src.causal_engine.CausalInferenceEngine object at 0x7f36c4540cd0>

    def test_build_model(self, engine):
        """Test model building with DoWhy."""
>       model = engine.build_model()
                ^^^^^^^^^^^^^^^^^^^^

tests/test_causal.py:43: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
src/causal_engine.py:66: in build_model
    self.model = CausalModel(
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:114: in __init__
    self.init_graph(graph=graph, identify_vars=identify_vars)
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:159: in init_graph
    self._graph = CausalGraph(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dowhy.causal_graph.CausalGraph object at 0x7f36942096a0>
treatment_name = ['Update_Command'], outcome_name = ['Update_Success']
graph = 'Update_Trigger->Update_Command; Network_Stability->Update_Success; Network_Stability->Device_Downtime; Device_Resourc...on->Update_Success; Update_Command->Update_Success; Update_Success->Rollback_Needed; Update_Success->Device_Downtime; '
common_cause_names = [], instrument_names = [], effect_modifier_names = []
mediator_names = []
observed_node_names = ['Update_Trigger', 'Network_Stability', 'Device_Resources', 'Device_Health', 'Firmware_Version', 'Device_Configuration', ...]
missing_nodes_as_confounders = False

    def __init__(
        self,
        treatment_name,
        outcome_name,
        graph=None,
        common_cause_names=None,
        instrument_names=None,
        effect_modifier_names=None,
        mediator_names=None,
        observed_node_names=None,
        missing_nodes_as_confounders=False,
    ):
        self.treatment_name = parse_state(treatment_name)
        self.outcome_name = parse_state(outcome_name)
        instrument_names = parse_state(instrument_names)
        common_cause_names = parse_state(common_cause_names)
        effect_modifier_names = parse_state(effect_modifier_names)
        mediator_names = parse_state(mediator_names)
        self.logger = logging.getLogger(__name__)
    
        # re.sub only takes string parameter so the first if is to avoid error
        # if the input is a text file, convert the contained data into string
        if isinstance(graph, str) and re.match(r".*\.txt", str(graph)):
            text_file = open(graph, "r")
            graph = text_file.read()
            text_file.close()
    
        if isinstance(graph, str) and re.match(r"^dag", graph):  # Convert daggity output to dot format
            graph = daggity_to_dot(graph)
    
        if isinstance(graph, str):
            graph = graph.replace("\n", " ")
    
        if graph is None:
            self._graph = nx.DiGraph()
            self._graph = self.build_graph(common_cause_names, instrument_names, effect_modifier_names, mediator_names)
        elif isinstance(graph, nx.DiGraph):
            self._graph = nx.DiGraph(graph)
        elif isinstance(graph, ProbabilisticCausalModel):
            self._graph = nx.DiGraph(graph.graph)
        elif isinstance(graph, str) and re.match(r".*\.dot", graph):
            # load dot file
            try:
                import pygraphviz as pgv
    
                self._graph = nx.DiGraph(nx.drawing.nx_agraph.read_dot(graph))
            except Exception as e:
                self.logger.error("Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot...")
                try:
                    import pydot
    
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.read_dot(graph))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(r".*\.gml", graph):
            self._graph = nx.DiGraph(nx.read_gml(graph))
        elif isinstance(graph, str) and re.match(r".*graph\s*\{.*\}\s*", graph):
            try:
                import pygraphviz as pgv
    
                self._graph = pgv.AGraph(graph, strict=True, directed=True)
                self._graph = nx.drawing.nx_agraph.from_agraph(self._graph)
            except Exception as e:
                self.logger.error("Error: Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot ...")
                try:
                    import pydot
    
                    P_list = pydot.graph_from_dot_data(graph)
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.from_pydot(P_list[0]))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(".*graph\s*\[.*\]\s*", graph):
            self._graph = nx.DiGraph(nx.parse_gml(graph))
        else:
            error_msg = "Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format."
            self.logger.error(error_msg)
            self.logger.error("Error: Incorrect graph format")
>           raise ValueError(error_msg)
E           ValueError: Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.

../../venv/lib/python3.14/site-packages/dowhy/causal_graph.py:107: ValueError
------------------------------ Captured log call -------------------------------
ERROR    dowhy.causal_graph:causal_graph.py:105 Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.
ERROR    dowhy.causal_graph:causal_graph.py:106 Error: Incorrect graph format
________________ TestCausalInferenceEngine.test_identify_effect ________________

self = <test_causal.TestCausalInferenceEngine object at 0x7f36942155b0>
engine = <src.causal_engine.CausalInferenceEngine object at 0x7f3694001810>

    def test_identify_effect(self, engine):
        """Test effect identification produces an estimand."""
>       engine.build_model()

tests/test_causal.py:52: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
src/causal_engine.py:66: in build_model
    self.model = CausalModel(
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:114: in __init__
    self.init_graph(graph=graph, identify_vars=identify_vars)
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:159: in init_graph
    self._graph = CausalGraph(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dowhy.causal_graph.CausalGraph object at 0x7f36940025d0>
treatment_name = ['Update_Command'], outcome_name = ['Update_Success']
graph = 'Update_Trigger->Update_Command; Network_Stability->Update_Success; Network_Stability->Device_Downtime; Device_Resourc...on->Update_Success; Update_Command->Update_Success; Update_Success->Rollback_Needed; Update_Success->Device_Downtime; '
common_cause_names = [], instrument_names = [], effect_modifier_names = []
mediator_names = []
observed_node_names = ['Update_Trigger', 'Network_Stability', 'Device_Resources', 'Device_Health', 'Firmware_Version', 'Device_Configuration', ...]
missing_nodes_as_confounders = False

    def __init__(
        self,
        treatment_name,
        outcome_name,
        graph=None,
        common_cause_names=None,
        instrument_names=None,
        effect_modifier_names=None,
        mediator_names=None,
        observed_node_names=None,
        missing_nodes_as_confounders=False,
    ):
        self.treatment_name = parse_state(treatment_name)
        self.outcome_name = parse_state(outcome_name)
        instrument_names = parse_state(instrument_names)
        common_cause_names = parse_state(common_cause_names)
        effect_modifier_names = parse_state(effect_modifier_names)
        mediator_names = parse_state(mediator_names)
        self.logger = logging.getLogger(__name__)
    
        # re.sub only takes string parameter so the first if is to avoid error
        # if the input is a text file, convert the contained data into string
        if isinstance(graph, str) and re.match(r".*\.txt", str(graph)):
            text_file = open(graph, "r")
            graph = text_file.read()
            text_file.close()
    
        if isinstance(graph, str) and re.match(r"^dag", graph):  # Convert daggity output to dot format
            graph = daggity_to_dot(graph)
    
        if isinstance(graph, str):
            graph = graph.replace("\n", " ")
    
        if graph is None:
            self._graph = nx.DiGraph()
            self._graph = self.build_graph(common_cause_names, instrument_names, effect_modifier_names, mediator_names)
        elif isinstance(graph, nx.DiGraph):
            self._graph = nx.DiGraph(graph)
        elif isinstance(graph, ProbabilisticCausalModel):
            self._graph = nx.DiGraph(graph.graph)
        elif isinstance(graph, str) and re.match(r".*\.dot", graph):
            # load dot file
            try:
                import pygraphviz as pgv
    
                self._graph = nx.DiGraph(nx.drawing.nx_agraph.read_dot(graph))
            except Exception as e:
                self.logger.error("Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot...")
                try:
                    import pydot
    
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.read_dot(graph))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(r".*\.gml", graph):
            self._graph = nx.DiGraph(nx.read_gml(graph))
        elif isinstance(graph, str) and re.match(r".*graph\s*\{.*\}\s*", graph):
            try:
                import pygraphviz as pgv
    
                self._graph = pgv.AGraph(graph, strict=True, directed=True)
                self._graph = nx.drawing.nx_agraph.from_agraph(self._graph)
            except Exception as e:
                self.logger.error("Error: Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot ...")
                try:
                    import pydot
    
                    P_list = pydot.graph_from_dot_data(graph)
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.from_pydot(P_list[0]))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(".*graph\s*\[.*\]\s*", graph):
            self._graph = nx.DiGraph(nx.parse_gml(graph))
        else:
            error_msg = "Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format."
            self.logger.error(error_msg)
            self.logger.error("Error: Incorrect graph format")
>           raise ValueError(error_msg)
E           ValueError: Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.

../../venv/lib/python3.14/site-packages/dowhy/causal_graph.py:107: ValueError
------------------------------ Captured log call -------------------------------
ERROR    dowhy.causal_graph:causal_graph.py:105 Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.
ERROR    dowhy.causal_graph:causal_graph.py:106 Error: Incorrect graph format
________ TestCausalInferenceEngine.test_backdoor_adjustment_set_exists _________

self = <test_causal.TestCausalInferenceEngine object at 0x7f3694215810>
engine = <src.causal_engine.CausalInferenceEngine object at 0x7f36942168b0>

    def test_backdoor_adjustment_set_exists(self, engine):
        """Test that a backdoor adjustment set is identified."""
>       engine.build_model()

tests/test_causal.py:59: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
src/causal_engine.py:66: in build_model
    self.model = CausalModel(
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:114: in __init__
    self.init_graph(graph=graph, identify_vars=identify_vars)
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:159: in init_graph
    self._graph = CausalGraph(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dowhy.causal_graph.CausalGraph object at 0x7f3694002c10>
treatment_name = ['Update_Command'], outcome_name = ['Update_Success']
graph = 'Update_Trigger->Update_Command; Network_Stability->Update_Success; Network_Stability->Device_Downtime; Device_Resourc...on->Update_Success; Update_Command->Update_Success; Update_Success->Rollback_Needed; Update_Success->Device_Downtime; '
common_cause_names = [], instrument_names = [], effect_modifier_names = []
mediator_names = []
observed_node_names = ['Update_Trigger', 'Network_Stability', 'Device_Resources', 'Device_Health', 'Firmware_Version', 'Device_Configuration', ...]
missing_nodes_as_confounders = False

    def __init__(
        self,
        treatment_name,
        outcome_name,
        graph=None,
        common_cause_names=None,
        instrument_names=None,
        effect_modifier_names=None,
        mediator_names=None,
        observed_node_names=None,
        missing_nodes_as_confounders=False,
    ):
        self.treatment_name = parse_state(treatment_name)
        self.outcome_name = parse_state(outcome_name)
        instrument_names = parse_state(instrument_names)
        common_cause_names = parse_state(common_cause_names)
        effect_modifier_names = parse_state(effect_modifier_names)
        mediator_names = parse_state(mediator_names)
        self.logger = logging.getLogger(__name__)
    
        # re.sub only takes string parameter so the first if is to avoid error
        # if the input is a text file, convert the contained data into string
        if isinstance(graph, str) and re.match(r".*\.txt", str(graph)):
            text_file = open(graph, "r")
            graph = text_file.read()
            text_file.close()
    
        if isinstance(graph, str) and re.match(r"^dag", graph):  # Convert daggity output to dot format
            graph = daggity_to_dot(graph)
    
        if isinstance(graph, str):
            graph = graph.replace("\n", " ")
    
        if graph is None:
            self._graph = nx.DiGraph()
            self._graph = self.build_graph(common_cause_names, instrument_names, effect_modifier_names, mediator_names)
        elif isinstance(graph, nx.DiGraph):
            self._graph = nx.DiGraph(graph)
        elif isinstance(graph, ProbabilisticCausalModel):
            self._graph = nx.DiGraph(graph.graph)
        elif isinstance(graph, str) and re.match(r".*\.dot", graph):
            # load dot file
            try:
                import pygraphviz as pgv
    
                self._graph = nx.DiGraph(nx.drawing.nx_agraph.read_dot(graph))
            except Exception as e:
                self.logger.error("Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot...")
                try:
                    import pydot
    
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.read_dot(graph))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(r".*\.gml", graph):
            self._graph = nx.DiGraph(nx.read_gml(graph))
        elif isinstance(graph, str) and re.match(r".*graph\s*\{.*\}\s*", graph):
            try:
                import pygraphviz as pgv
    
                self._graph = pgv.AGraph(graph, strict=True, directed=True)
                self._graph = nx.drawing.nx_agraph.from_agraph(self._graph)
            except Exception as e:
                self.logger.error("Error: Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot ...")
                try:
                    import pydot
    
                    P_list = pydot.graph_from_dot_data(graph)
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.from_pydot(P_list[0]))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(".*graph\s*\[.*\]\s*", graph):
            self._graph = nx.DiGraph(nx.parse_gml(graph))
        else:
            error_msg = "Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format."
            self.logger.error(error_msg)
            self.logger.error("Error: Incorrect graph format")
>           raise ValueError(error_msg)
E           ValueError: Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.

../../venv/lib/python3.14/site-packages/dowhy/causal_graph.py:107: ValueError
------------------------------ Captured log call -------------------------------
ERROR    dowhy.causal_graph:causal_graph.py:105 Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.
ERROR    dowhy.causal_graph:causal_graph.py:106 Error: Incorrect graph format
________ TestCausalInferenceEngine.test_estimate_ate_linear_regression _________

self = <test_causal.TestCausalInferenceEngine object at 0x7f36941b9d90>
engine = <src.causal_engine.CausalInferenceEngine object at 0x7f3694217230>

    def test_estimate_ate_linear_regression(self, engine):
        """Test ATE estimation with linear regression."""
>       result = engine.run_full_analysis(method="linear_regression")
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: CausalInferenceEngine.run_full_analysis() got an unexpected keyword argument 'method'

tests/test_causal.py:69: TypeError
_________ TestCausalInferenceEngine.test_estimate_ate_propensity_score _________

self = <test_causal.TestCausalInferenceEngine object at 0x7f36941b6cf0>
engine = <src.causal_engine.CausalInferenceEngine object at 0x7f3693fb4dd0>

    def test_estimate_ate_propensity_score(self, engine):
        """Test ATE estimation with propensity score matching."""
>       result = engine.run_full_analysis(method="propensity_score_matching")
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: CausalInferenceEngine.run_full_analysis() got an unexpected keyword argument 'method'

tests/test_causal.py:80: TypeError
______________ TestCausalInferenceEngine.test_backdoor_validation ______________

self = <test_causal.TestCausalInferenceEngine object at 0x7f36941b6f10>
engine = <src.causal_engine.CausalInferenceEngine object at 0x7f3693f40e20>

    def test_backdoor_validation(self, engine):
        """Test backdoor criterion validation."""
>       engine.build_model()

tests/test_causal.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
src/causal_engine.py:66: in build_model
    self.model = CausalModel(
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:114: in __init__
    self.init_graph(graph=graph, identify_vars=identify_vars)
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:159: in init_graph
    self._graph = CausalGraph(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dowhy.causal_graph.CausalGraph object at 0x7f3693f90510>
treatment_name = ['Update_Command'], outcome_name = ['Update_Success']
graph = 'Update_Trigger->Update_Command; Network_Stability->Update_Success; Network_Stability->Device_Downtime; Device_Resourc...on->Update_Success; Update_Command->Update_Success; Update_Success->Rollback_Needed; Update_Success->Device_Downtime; '
common_cause_names = [], instrument_names = [], effect_modifier_names = []
mediator_names = []
observed_node_names = ['Update_Trigger', 'Network_Stability', 'Device_Resources', 'Device_Health', 'Firmware_Version', 'Device_Configuration', ...]
missing_nodes_as_confounders = False

    def __init__(
        self,
        treatment_name,
        outcome_name,
        graph=None,
        common_cause_names=None,
        instrument_names=None,
        effect_modifier_names=None,
        mediator_names=None,
        observed_node_names=None,
        missing_nodes_as_confounders=False,
    ):
        self.treatment_name = parse_state(treatment_name)
        self.outcome_name = parse_state(outcome_name)
        instrument_names = parse_state(instrument_names)
        common_cause_names = parse_state(common_cause_names)
        effect_modifier_names = parse_state(effect_modifier_names)
        mediator_names = parse_state(mediator_names)
        self.logger = logging.getLogger(__name__)
    
        # re.sub only takes string parameter so the first if is to avoid error
        # if the input is a text file, convert the contained data into string
        if isinstance(graph, str) and re.match(r".*\.txt", str(graph)):
            text_file = open(graph, "r")
            graph = text_file.read()
            text_file.close()
    
        if isinstance(graph, str) and re.match(r"^dag", graph):  # Convert daggity output to dot format
            graph = daggity_to_dot(graph)
    
        if isinstance(graph, str):
            graph = graph.replace("\n", " ")
    
        if graph is None:
            self._graph = nx.DiGraph()
            self._graph = self.build_graph(common_cause_names, instrument_names, effect_modifier_names, mediator_names)
        elif isinstance(graph, nx.DiGraph):
            self._graph = nx.DiGraph(graph)
        elif isinstance(graph, ProbabilisticCausalModel):
            self._graph = nx.DiGraph(graph.graph)
        elif isinstance(graph, str) and re.match(r".*\.dot", graph):
            # load dot file
            try:
                import pygraphviz as pgv
    
                self._graph = nx.DiGraph(nx.drawing.nx_agraph.read_dot(graph))
            except Exception as e:
                self.logger.error("Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot...")
                try:
                    import pydot
    
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.read_dot(graph))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(r".*\.gml", graph):
            self._graph = nx.DiGraph(nx.read_gml(graph))
        elif isinstance(graph, str) and re.match(r".*graph\s*\{.*\}\s*", graph):
            try:
                import pygraphviz as pgv
    
                self._graph = pgv.AGraph(graph, strict=True, directed=True)
                self._graph = nx.drawing.nx_agraph.from_agraph(self._graph)
            except Exception as e:
                self.logger.error("Error: Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot ...")
                try:
                    import pydot
    
                    P_list = pydot.graph_from_dot_data(graph)
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.from_pydot(P_list[0]))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(".*graph\s*\[.*\]\s*", graph):
            self._graph = nx.DiGraph(nx.parse_gml(graph))
        else:
            error_msg = "Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format."
            self.logger.error(error_msg)
            self.logger.error("Error: Incorrect graph format")
>           raise ValueError(error_msg)
E           ValueError: Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.

../../venv/lib/python3.14/site-packages/dowhy/causal_graph.py:107: ValueError
------------------------------ Captured log call -------------------------------
ERROR    dowhy.causal_graph:causal_graph.py:105 Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.
ERROR    dowhy.causal_graph:causal_graph.py:106 Error: Incorrect graph format
____________ TestCausalInferenceEngine.test_full_analysis_pipeline _____________

self = <test_causal.TestCausalInferenceEngine object at 0x7f36941f6250>
engine = <src.causal_engine.CausalInferenceEngine object at 0x7f3693f418c0>

    def test_full_analysis_pipeline(self, engine):
        """Test the complete analysis pipeline."""
>       result = engine.run_full_analysis(estimation_methods=["linear_regression"])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_causal.py:98: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
src/causal_engine.py:231: in run_full_analysis
    self.build_model(treatment, outcome)
src/causal_engine.py:66: in build_model
    self.model = CausalModel(
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:114: in __init__
    self.init_graph(graph=graph, identify_vars=identify_vars)
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:159: in init_graph
    self._graph = CausalGraph(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dowhy.causal_graph.CausalGraph object at 0x7f3693f909d0>
treatment_name = ['Update_Command'], outcome_name = ['Update_Success']
graph = 'Update_Trigger->Update_Command; Network_Stability->Update_Success; Network_Stability->Device_Downtime; Device_Resourc...on->Update_Success; Update_Command->Update_Success; Update_Success->Rollback_Needed; Update_Success->Device_Downtime; '
common_cause_names = [], instrument_names = [], effect_modifier_names = []
mediator_names = []
observed_node_names = ['Update_Trigger', 'Network_Stability', 'Device_Resources', 'Device_Health', 'Firmware_Version', 'Device_Configuration', ...]
missing_nodes_as_confounders = False

    def __init__(
        self,
        treatment_name,
        outcome_name,
        graph=None,
        common_cause_names=None,
        instrument_names=None,
        effect_modifier_names=None,
        mediator_names=None,
        observed_node_names=None,
        missing_nodes_as_confounders=False,
    ):
        self.treatment_name = parse_state(treatment_name)
        self.outcome_name = parse_state(outcome_name)
        instrument_names = parse_state(instrument_names)
        common_cause_names = parse_state(common_cause_names)
        effect_modifier_names = parse_state(effect_modifier_names)
        mediator_names = parse_state(mediator_names)
        self.logger = logging.getLogger(__name__)
    
        # re.sub only takes string parameter so the first if is to avoid error
        # if the input is a text file, convert the contained data into string
        if isinstance(graph, str) and re.match(r".*\.txt", str(graph)):
            text_file = open(graph, "r")
            graph = text_file.read()
            text_file.close()
    
        if isinstance(graph, str) and re.match(r"^dag", graph):  # Convert daggity output to dot format
            graph = daggity_to_dot(graph)
    
        if isinstance(graph, str):
            graph = graph.replace("\n", " ")
    
        if graph is None:
            self._graph = nx.DiGraph()
            self._graph = self.build_graph(common_cause_names, instrument_names, effect_modifier_names, mediator_names)
        elif isinstance(graph, nx.DiGraph):
            self._graph = nx.DiGraph(graph)
        elif isinstance(graph, ProbabilisticCausalModel):
            self._graph = nx.DiGraph(graph.graph)
        elif isinstance(graph, str) and re.match(r".*\.dot", graph):
            # load dot file
            try:
                import pygraphviz as pgv
    
                self._graph = nx.DiGraph(nx.drawing.nx_agraph.read_dot(graph))
            except Exception as e:
                self.logger.error("Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot...")
                try:
                    import pydot
    
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.read_dot(graph))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(r".*\.gml", graph):
            self._graph = nx.DiGraph(nx.read_gml(graph))
        elif isinstance(graph, str) and re.match(r".*graph\s*\{.*\}\s*", graph):
            try:
                import pygraphviz as pgv
    
                self._graph = pgv.AGraph(graph, strict=True, directed=True)
                self._graph = nx.drawing.nx_agraph.from_agraph(self._graph)
            except Exception as e:
                self.logger.error("Error: Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot ...")
                try:
                    import pydot
    
                    P_list = pydot.graph_from_dot_data(graph)
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.from_pydot(P_list[0]))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(".*graph\s*\[.*\]\s*", graph):
            self._graph = nx.DiGraph(nx.parse_gml(graph))
        else:
            error_msg = "Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format."
            self.logger.error(error_msg)
            self.logger.error("Error: Incorrect graph format")
>           raise ValueError(error_msg)
E           ValueError: Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.

../../venv/lib/python3.14/site-packages/dowhy/causal_graph.py:107: ValueError
------------------------------ Captured log call -------------------------------
ERROR    dowhy.causal_graph:causal_graph.py:105 Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.
ERROR    dowhy.causal_graph:causal_graph.py:106 Error: Incorrect graph format
______ TestCausalInferenceEngine.test_different_data_different_estimates _______

self = <test_causal.TestCausalInferenceEngine object at 0x7f36941f6550>
causal_graph = <networkx.classes.digraph.DiGraph object at 0x7f3693f19f50>

    def test_different_data_different_estimates(self, causal_graph):
        """Test that different data produces different estimates."""
        data1 = generate_data(n_samples=500, seed=42)
        data2 = generate_data(n_samples=500, seed=123)
    
        engine1 = CausalInferenceEngine(causal_graph, data1)
        engine2 = CausalInferenceEngine(causal_graph, data2)
    
>       result1 = engine1.run_full_analysis()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_causal.py:116: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
src/causal_engine.py:231: in run_full_analysis
    self.build_model(treatment, outcome)
src/causal_engine.py:66: in build_model
    self.model = CausalModel(
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:114: in __init__
    self.init_graph(graph=graph, identify_vars=identify_vars)
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:159: in init_graph
    self._graph = CausalGraph(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dowhy.causal_graph.CausalGraph object at 0x7f3693fb6b10>
treatment_name = ['Update_Command'], outcome_name = ['Update_Success']
graph = 'Update_Trigger->Update_Command; Network_Stability->Update_Success; Network_Stability->Device_Downtime; Device_Resourc...on->Update_Success; Update_Command->Update_Success; Update_Success->Rollback_Needed; Update_Success->Device_Downtime; '
common_cause_names = [], instrument_names = [], effect_modifier_names = []
mediator_names = []
observed_node_names = ['Update_Trigger', 'Network_Stability', 'Device_Resources', 'Device_Health', 'Firmware_Version', 'Device_Configuration', ...]
missing_nodes_as_confounders = False

    def __init__(
        self,
        treatment_name,
        outcome_name,
        graph=None,
        common_cause_names=None,
        instrument_names=None,
        effect_modifier_names=None,
        mediator_names=None,
        observed_node_names=None,
        missing_nodes_as_confounders=False,
    ):
        self.treatment_name = parse_state(treatment_name)
        self.outcome_name = parse_state(outcome_name)
        instrument_names = parse_state(instrument_names)
        common_cause_names = parse_state(common_cause_names)
        effect_modifier_names = parse_state(effect_modifier_names)
        mediator_names = parse_state(mediator_names)
        self.logger = logging.getLogger(__name__)
    
        # re.sub only takes string parameter so the first if is to avoid error
        # if the input is a text file, convert the contained data into string
        if isinstance(graph, str) and re.match(r".*\.txt", str(graph)):
            text_file = open(graph, "r")
            graph = text_file.read()
            text_file.close()
    
        if isinstance(graph, str) and re.match(r"^dag", graph):  # Convert daggity output to dot format
            graph = daggity_to_dot(graph)
    
        if isinstance(graph, str):
            graph = graph.replace("\n", " ")
    
        if graph is None:
            self._graph = nx.DiGraph()
            self._graph = self.build_graph(common_cause_names, instrument_names, effect_modifier_names, mediator_names)
        elif isinstance(graph, nx.DiGraph):
            self._graph = nx.DiGraph(graph)
        elif isinstance(graph, ProbabilisticCausalModel):
            self._graph = nx.DiGraph(graph.graph)
        elif isinstance(graph, str) and re.match(r".*\.dot", graph):
            # load dot file
            try:
                import pygraphviz as pgv
    
                self._graph = nx.DiGraph(nx.drawing.nx_agraph.read_dot(graph))
            except Exception as e:
                self.logger.error("Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot...")
                try:
                    import pydot
    
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.read_dot(graph))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(r".*\.gml", graph):
            self._graph = nx.DiGraph(nx.read_gml(graph))
        elif isinstance(graph, str) and re.match(r".*graph\s*\{.*\}\s*", graph):
            try:
                import pygraphviz as pgv
    
                self._graph = pgv.AGraph(graph, strict=True, directed=True)
                self._graph = nx.drawing.nx_agraph.from_agraph(self._graph)
            except Exception as e:
                self.logger.error("Error: Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot ...")
                try:
                    import pydot
    
                    P_list = pydot.graph_from_dot_data(graph)
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.from_pydot(P_list[0]))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(".*graph\s*\[.*\]\s*", graph):
            self._graph = nx.DiGraph(nx.parse_gml(graph))
        else:
            error_msg = "Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format."
            self.logger.error(error_msg)
            self.logger.error("Error: Incorrect graph format")
>           raise ValueError(error_msg)
E           ValueError: Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.

../../venv/lib/python3.14/site-packages/dowhy/causal_graph.py:107: ValueError
------------------------------ Captured log call -------------------------------
ERROR    dowhy.causal_graph:causal_graph.py:105 Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.
ERROR    dowhy.causal_graph:causal_graph.py:106 Error: Incorrect graph format
________ TestCausalInferenceEngine.test_reproducibility_with_same_seed _________

self = <test_causal.TestCausalInferenceEngine object at 0x7f36941e27b0>
causal_graph = <networkx.classes.digraph.DiGraph object at 0x7f3693f1b050>

    def test_reproducibility_with_same_seed(self, causal_graph):
        """Test that same seed produces same results."""
        data = generate_data(n_samples=500, seed=42)
        engine1 = CausalInferenceEngine(causal_graph, data)
        engine2 = CausalInferenceEngine(causal_graph, data)
    
>       result1 = engine1.run_full_analysis()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_causal.py:135: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
src/causal_engine.py:231: in run_full_analysis
    self.build_model(treatment, outcome)
src/causal_engine.py:66: in build_model
    self.model = CausalModel(
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:114: in __init__
    self.init_graph(graph=graph, identify_vars=identify_vars)
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:159: in init_graph
    self._graph = CausalGraph(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dowhy.causal_graph.CausalGraph object at 0x7f3693f42f10>
treatment_name = ['Update_Command'], outcome_name = ['Update_Success']
graph = 'Update_Trigger->Update_Command; Network_Stability->Update_Success; Network_Stability->Device_Downtime; Device_Resourc...on->Update_Success; Update_Command->Update_Success; Update_Success->Rollback_Needed; Update_Success->Device_Downtime; '
common_cause_names = [], instrument_names = [], effect_modifier_names = []
mediator_names = []
observed_node_names = ['Update_Trigger', 'Network_Stability', 'Device_Resources', 'Device_Health', 'Firmware_Version', 'Device_Configuration', ...]
missing_nodes_as_confounders = False

    def __init__(
        self,
        treatment_name,
        outcome_name,
        graph=None,
        common_cause_names=None,
        instrument_names=None,
        effect_modifier_names=None,
        mediator_names=None,
        observed_node_names=None,
        missing_nodes_as_confounders=False,
    ):
        self.treatment_name = parse_state(treatment_name)
        self.outcome_name = parse_state(outcome_name)
        instrument_names = parse_state(instrument_names)
        common_cause_names = parse_state(common_cause_names)
        effect_modifier_names = parse_state(effect_modifier_names)
        mediator_names = parse_state(mediator_names)
        self.logger = logging.getLogger(__name__)
    
        # re.sub only takes string parameter so the first if is to avoid error
        # if the input is a text file, convert the contained data into string
        if isinstance(graph, str) and re.match(r".*\.txt", str(graph)):
            text_file = open(graph, "r")
            graph = text_file.read()
            text_file.close()
    
        if isinstance(graph, str) and re.match(r"^dag", graph):  # Convert daggity output to dot format
            graph = daggity_to_dot(graph)
    
        if isinstance(graph, str):
            graph = graph.replace("\n", " ")
    
        if graph is None:
            self._graph = nx.DiGraph()
            self._graph = self.build_graph(common_cause_names, instrument_names, effect_modifier_names, mediator_names)
        elif isinstance(graph, nx.DiGraph):
            self._graph = nx.DiGraph(graph)
        elif isinstance(graph, ProbabilisticCausalModel):
            self._graph = nx.DiGraph(graph.graph)
        elif isinstance(graph, str) and re.match(r".*\.dot", graph):
            # load dot file
            try:
                import pygraphviz as pgv
    
                self._graph = nx.DiGraph(nx.drawing.nx_agraph.read_dot(graph))
            except Exception as e:
                self.logger.error("Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot...")
                try:
                    import pydot
    
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.read_dot(graph))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(r".*\.gml", graph):
            self._graph = nx.DiGraph(nx.read_gml(graph))
        elif isinstance(graph, str) and re.match(r".*graph\s*\{.*\}\s*", graph):
            try:
                import pygraphviz as pgv
    
                self._graph = pgv.AGraph(graph, strict=True, directed=True)
                self._graph = nx.drawing.nx_agraph.from_agraph(self._graph)
            except Exception as e:
                self.logger.error("Error: Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot ...")
                try:
                    import pydot
    
                    P_list = pydot.graph_from_dot_data(graph)
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.from_pydot(P_list[0]))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(".*graph\s*\[.*\]\s*", graph):
            self._graph = nx.DiGraph(nx.parse_gml(graph))
        else:
            error_msg = "Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format."
            self.logger.error(error_msg)
            self.logger.error("Error: Incorrect graph format")
>           raise ValueError(error_msg)
E           ValueError: Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.

../../venv/lib/python3.14/site-packages/dowhy/causal_graph.py:107: ValueError
------------------------------ Captured log call -------------------------------
ERROR    dowhy.causal_graph:causal_graph.py:105 Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format.
ERROR    dowhy.causal_graph:causal_graph.py:106 Error: Incorrect graph format
_________ TestCausalInferenceEngine.test_confidence_intervals_computed _________

self = <test_causal.TestCausalInferenceEngine object at 0x7f36941e2990>
engine = <src.causal_engine.CausalInferenceEngine object at 0x7f3694018750>

    def test_confidence_intervals_computed(self, engine):
        """Test that confidence intervals are included when requested."""
>       result = engine.run_full_analysis(method="linear_regression")
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: CausalInferenceEngine.run_full_analysis() got an unexpected keyword argument 'method'

tests/test_causal.py:149: TypeError
___________ TestCausalInferenceEngine.test_engine_with_missing_data ____________

self = <test_causal.TestCausalInferenceEngine object at 0x7f3694019a90>
causal_graph = <networkx.classes.digraph.DiGraph object at 0x7f369401b310>

    def test_engine_with_missing_data(self, causal_graph):
        """Test engine handles missing data appropriately."""
        data = generate_data(n_samples=100)
        # Intentionally drop some columns to test error handling
        incomplete_data = data.drop(columns=["Network_Stability", "Device_Resources"])
    
        engine = CausalInferenceEngine(causal_graph, incomplete_data)
>       result = engine.run_full_analysis()
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_causal.py:178: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
src/causal_engine.py:231: in run_full_analysis
    self.build_model(treatment, outcome)
src/causal_engine.py:66: in build_model
    self.model = CausalModel(
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:114: in __init__
    self.init_graph(graph=graph, identify_vars=identify_vars)
../../venv/lib/python3.14/site-packages/dowhy/causal_model.py:159: in init_graph
    self._graph = CausalGraph(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dowhy.causal_graph.CausalGraph object at 0x7f3693f438a0>
treatment_name = ['Update_Command'], outcome_name = ['Update_Success']
graph = 'Update_Trigger->Update_Command; Network_Stability->Update_Success; Network_Stability->Device_Downtime; Device_Resourc...on->Update_Success; Update_Command->Update_Success; Update_Success->Rollback_Needed; Update_Success->Device_Downtime; '
common_cause_names = [], instrument_names = [], effect_modifier_names = []
mediator_names = []
observed_node_names = ['Update_Trigger', 'Device_Health', 'Firmware_Version', 'Device_Configuration', 'Update_Command', 'Update_Success', ...]
missing_nodes_as_confounders = False

    def __init__(
        self,
        treatment_name,
        outcome_name,
        graph=None,
        common_cause_names=None,
        instrument_names=None,
        effect_modifier_names=None,
        mediator_names=None,
        observed_node_names=None,
        missing_nodes_as_confounders=False,
    ):
        self.treatment_name = parse_state(treatment_name)
        self.outcome_name = parse_state(outcome_name)
        instrument_names = parse_state(instrument_names)
        common_cause_names = parse_state(common_cause_names)
        effect_modifier_names = parse_state(effect_modifier_names)
        mediator_names = parse_state(mediator_names)
        self.logger = logging.getLogger(__name__)
    
        # re.sub only takes string parameter so the first if is to avoid error
        # if the input is a text file, convert the contained data into string
        if isinstance(graph, str) and re.match(r".*\.txt", str(graph)):
            text_file = open(graph, "r")
            graph = text_file.read()
            text_file.close()
    
        if isinstance(graph, str) and re.match(r"^dag", graph):  # Convert daggity output to dot format
            graph = daggity_to_dot(graph)
    
        if isinstance(graph, str):
            graph = graph.replace("\n", " ")
    
        if graph is None:
            self._graph = nx.DiGraph()
            self._graph = self.build_graph(common_cause_names, instrument_names, effect_modifier_names, mediator_names)
        elif isinstance(graph, nx.DiGraph):
            self._graph = nx.DiGraph(graph)
        elif isinstance(graph, ProbabilisticCausalModel):
            self._graph = nx.DiGraph(graph.graph)
        elif isinstance(graph, str) and re.match(r".*\.dot", graph):
            # load dot file
            try:
                import pygraphviz as pgv
    
                self._graph = nx.DiGraph(nx.drawing.nx_agraph.read_dot(graph))
            except Exception as e:
                self.logger.error("Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot...")
                try:
                    import pydot
    
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.read_dot(graph))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(r".*\.gml", graph):
            self._graph = nx.DiGraph(nx.read_gml(graph))
        elif isinstance(graph, str) and re.match(r".*graph\s*\{.*\}\s*", graph):
            try:
                import pygraphviz as pgv
    
                self._graph = pgv.AGraph(graph, strict=True, directed=True)
                self._graph = nx.drawing.nx_agraph.from_agraph(self._graph)
            except Exception as e:
                self.logger.error("Error: Pygraphviz cannot be loaded. " + str(e) + "\nTrying pydot ...")
                try:
                    import pydot
    
                    P_list = pydot.graph_from_dot_data(graph)
                    self._graph = nx.DiGraph(nx.drawing.nx_pydot.from_pydot(P_list[0]))
                except Exception as e:
                    self.logger.error("Error: Pydot cannot be loaded. " + str(e))
                    raise e
        elif isinstance(graph, str) and re.match(".*graph\s*\[.*\]\s*", graph):
            self._graph = nx.DiGraph(nx.parse_gml(graph))
        else:
            error_msg = "Incorrect format: Please provide graph as a networkx DiGraph, GCM model, or as a string or text file in dot, gml format."
            self.logger.error(error_msg)
            self.logger.error("Error: Incorrect graph format")
>           raise ValueError(error_msg)

...13677 bytes truncated...

The tool call succeeded but the output was truncated. Full output saved to: /home/julien/.local/share/opencode/tool-output/tool_ce3705ff3001vhJB4cirJy1SJz
Use the Task tool to have explore agent process this file with Grep and Read (with offset/limit). Do NOT read the full file yourself - delegate to save context.
[0m
The main issue: DoWhy's CausalModel doesn't accept the simple string format we're using. We need to either pass the NetworkX DiGraph directly or use proper DOT format. The simplest fix is to pass the graph directly:
[0m← [0mEdit src/causal_engine.py
Index: /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
===================================================================
--- /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
+++ /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
@@ -56,16 +56,11 @@
 
 Returns:
     Configured CausalModel instance
 """
-# Convert NetworkX graph to DOT string for DoWhy
-graph_str = ""
-for edge in self.graph.edges():
-    graph_str += f"{edge[0]}->{edge[1]}; "
-
-# Create DoWhy model
+# Create DoWhy model using NetworkX graph directly
 self.model = CausalModel(
-    data=self.data, treatment=treatment, outcome=outcome, graph=graph_str
+    data=self.data, treatment=treatment, outcome=outcome, graph=self.graph
 )
 
 return self.model
 

[0m
Now run tests again:
[0m$ [0mcd /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model && python -m pytest tests/test_causal.py::TestCausalInferenceEngine::test_build_model -v
============================= test session starts ==============================
platform linux -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0 -- /home/julien/Desktop/Free-Wiggum-opencode/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model
plugins: langsmith-0.7.16, anyio-4.12.1, dash-4.0.0
collecting ... collected 1 item

tests/test_causal.py::TestCausalInferenceEngine::test_build_model FAILED [100%]

=================================== FAILURES ===================================
__________________ TestCausalInferenceEngine.test_build_model __________________

self = <test_causal.TestCausalInferenceEngine object at 0x7fed866b4910>
engine = <src.causal_engine.CausalInferenceEngine object at 0x7fed8667d160>

    def test_build_model(self, engine):
        """Test model building with DoWhy."""
        model = engine.build_model()
        assert model is not None
        assert engine.model is not None
        # Check that treatment and outcome are set correctly
>       assert engine.model._treatment == "Update_Command"
E       AssertionError: assert ['Update_Command'] == 'Update_Command'
E        +  where ['Update_Command'] = <dowhy.causal_model.CausalModel object at 0x7fed8667d400>._treatment
E        +    where <dowhy.causal_model.CausalModel object at 0x7fed8667d400> = <src.causal_engine.CausalInferenceEngine object at 0x7fed8667d160>.model

tests/test_causal.py:47: AssertionError
=========================== short test summary info ============================
FAILED tests/test_causal.py::TestCausalInferenceEngine::test_build_model - As...
============================== 1 failed in 3.53s ===============================
[0m
The model now builds successfully. The test failures are due to:
1. DoWhy stores treatment/outcome as lists, not strings
2. Tests use `method=` parameter but engine uses `estimation_methods=`

I'll fix both the tests and also add a convenience parameter to the engine for single-method calls. Let me first update the causal_engine.py to accept a `method` parameter for convenience:
[0m← [0mEdit src/causal_engine.py
Index: /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
===================================================================
--- /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
+++ /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/src/causal_engine.py
@@ -206,20 +206,24 @@
     self,
     treatment: str = "Update_Command",
     outcome: str = "Update_Success",
     estimation_methods: list = None,
+    method: str = None,
 ) -> Dict:
     """
     Run complete causal analysis pipeline.
 
     Args:
         treatment: Treatment variable name
         outcome: Outcome variable name
         estimation_methods: List of estimation methods to try
+        method: Single estimation method (convenience parameter)
 
     Returns:
         Dictionary with all results
     """
+    if method is not None:
+        estimation_methods = [method]
     if estimation_methods is None:
         estimation_methods = ["linear_regression", "propensity_score_matching"]
 
     # Build model

[0m
Now fix the tests to check list instead of string for treatment/outcome:
[0m← [0mEdit tests/test_causal.py
Index: /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/tests/test_causal.py
===================================================================
--- /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/tests/test_causal.py
+++ /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model/tests/test_causal.py
@@ -43,10 +43,10 @@
     model = engine.build_model()
     assert model is not None
     assert engine.model is not None
     # Check that treatment and outcome are set correctly
-    assert engine.model._treatment == "Update_Command"
-    assert engine.model._outcome == "Update_Success"
+    assert engine.model._treatment == ["Update_Command"]
+    assert engine.model._outcome == ["Update_Success"]
 
 def test_identify_effect(self, engine):
     """Test effect identification produces an estimand."""
     engine.build_model()

[0m
Run the full test suite again:
[0m$ [0mcd /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model && python -m pytest tests/test_causal.py -v
============================= test session starts ==============================
platform linux -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0 -- /home/julien/Desktop/Free-Wiggum-opencode/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model
plugins: langsmith-0.7.16, anyio-4.12.1, dash-4.0.0
collecting ... collected 15 items

tests/test_causal.py::TestCausalInferenceEngine::test_engine_initialization PASSED [  6%]
tests/test_causal.py::TestCausalInferenceEngine::test_build_model PASSED [ 13%]
tests/test_causal.py::TestCausalInferenceEngine::test_identify_effect PASSED [ 20%]
tests/test_causal.py::TestCausalInferenceEngine::test_backdoor_adjustment_set_exists FAILED [ 26%]
tests/test_causal.py::TestCausalInferenceEngine::test_estimate_ate_linear_regression 

<bash_metadata>
bash tool terminated command after exceeding timeout 120000 ms
</bash_metadata>
[0m
Tests are timing out. Let me run a single quick test to verify basic functionality:
[0m$ [0mcd /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model && python -m pytest tests/test_causal.py::TestCausalInferenceEngine::test_engine_initialization tests/test_causal.py::TestCausalInferenceEngine::test_build_model -v --timeout=30
ERROR: usage: python -m pytest [options] [file_or_dir] [file_or_dir] [...]
python -m pytest: error: unrecognized arguments: --timeout=30
  inifile: None
  rootdir: /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model
[0m
[0m$ [0mcd /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model && python -m pytest tests/test_causal.py::TestCausalInferenceEngine::test_build_model -v
============================= test session starts ==============================
platform linux -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0 -- /home/julien/Desktop/Free-Wiggum-opencode/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/julien/Desktop/Free-Wiggum-opencode/projects/causal-model
plugins: langsmith-0.7.16, anyio-4.12.1, dash-4.0.0
collecting ... collected 1 item

tests/test_causal.py::TestCausalInferenceEngine::test_build_model PASSED [100%]

============================== 1 passed in 2.95s ===============================
[0m
```

## TASKS.md After Iteration

```markdown
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
```

**Completed at:** Thu Mar 12 03:08:39 PM EDT 2026
