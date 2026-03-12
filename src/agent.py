"""
Agent for firmware update decisions using causal inference.

The agent observes the device state (confounding variables) and decides whether
to issue an update command based on the predicted probability of success.
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from typing import Dict
from src.causal_engine import CausalInferenceEngine


class Agent:
    def __init__(self, engine: CausalInferenceEngine, decision_threshold: float = 0.7):
        """
        Initialize the agent.

        Args:
            engine: CausalInferenceEngine containing the data and causal model.
            decision_threshold: Minimum predicted success probability to trigger an update.
        """
        self.engine = engine
        self.decision_threshold = decision_threshold
        self.backdoor_set = engine.get_backdoor_adjustment_set()
        self.model = self._train_predictive_model()

    def _train_predictive_model(self):
        """Train an OLS regression model to predict Update_Success."""
        data = self.engine.data
        # Construct formula with backdoor variables and treatment
        terms = []
        for var in self.backdoor_set:
            if var in ["Update_Trigger", "Firmware_Version", "Device_Configuration"]:
                terms.append(f"C({var})")
            else:
                terms.append(var)
        terms.append("Update_Command")  # treatment
        formula = "Update_Success ~ " + " + ".join(terms)
        model = smf.ols(formula, data=data).fit(disp=0)
        return model

    def perceive(self, device_state: Dict) -> None:
        """
        Observe the current device state.

        Args:
            device_state: Dictionary containing values for all backdoor variables.
        """
        self.current_state = device_state

    def reason(self) -> float:
        """
        Predict the success probability if an update command were issued.

        Returns:
            A probability value between 0 and 1 (clipped).
        """
        state = self.current_state.copy()
        state["Update_Command"] = 1  # simulate intervention
        df = pd.DataFrame([state])
        pred = self.model.predict(df)[0]
        # Ensure within [0, 1]
        return float(np.clip(pred, 0.0, 1.0))

    def act(self) -> str:
        """
        Decide on an action based on the predicted probability.

        Returns:
            "update" if probability meets or exceeds threshold, else "no_update".
        """
        prob = self.reason()
        return "update" if prob >= self.decision_threshold else "no_update"
