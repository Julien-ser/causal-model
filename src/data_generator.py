"""
Synthetic data generator for firmware update causal model.

This module generates realistic simulation data for 1000 firmware update attempts,
with variables following the causal graph structure defined in causal_graph.py.
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple
from src.causal_graph import create_causal_graph


class DataGenerator:
    """
    Generates synthetic data for firmware update attempts.

    The data generation respects the causal DAG structure:
    - Exogenous variables are sampled independently
    - Treatment (Update_Command) depends on confounders and triggers
    - Outcome (Update_Success) depends on treatment and all relevant causes
    - Secondary outcomes depend on primary outcome and other factors
    """

    def __init__(self, seed: int = 42):
        """
        Initialize the data generator with a random seed.

        Args:
            seed: Random seed for reproducibility
        """
        self.seed = seed
        self.rng = np.random.RandomState(seed)

    def generate(self, n_samples: int = 1000) -> pd.DataFrame:
        """
        Generate synthetic firmware update data.

        Args:
            n_samples: Number of update attempts to simulate

        Returns:
            DataFrame with columns for all causal variables
        """
        data = {}

        # 1. Exogenous variables (root causes)
        data.update(self._generate_exogenous_vars(n_samples))

        # 2. Treatment: Update_Command (depends on Update_Trigger, Firmware_Version, Device_Configuration)
        data["Update_Command"] = self._generate_update_command(
            data["Update_Trigger"],
            data["Firmware_Version"],
            data["Device_Configuration"],
        )

        # 3. Primary outcome: Update_Success (depends on Update_Command and all other direct causes)
        data["Update_Success"] = self._generate_update_success(
            data["Update_Command"],
            data["Network_Stability"],
            data["Device_Resources"],
            data["Device_Health"],
            data["Firmware_Version"],
            data["Device_Configuration"],
        )

        # 4. Secondary outcomes
        data["Rollback_Needed"] = self._generate_rollback_needed(
            data["Update_Success"], data["Network_Stability"]
        )
        data["Device_Downtime"] = self._generate_device_downtime(
            data["Update_Success"], data["Network_Stability"], data["Device_Resources"]
        )

        return pd.DataFrame(data)

    def _generate_exogenous_vars(self, n: int) -> Dict[str, np.ndarray]:
        """Generate independent exogenous variables."""
        data = {}

        # Update_Trigger: categorical (0=manual, 1=automatic, 2=emergency)
        # Manual updates are most common, automatic less so, emergency rare
        trigger_probs = [0.6, 0.3, 0.1]
        data["Update_Trigger"] = self.rng.choice([0, 1, 2], size=n, p=trigger_probs)

        # Network_Stability: continuous 0-1, beta distribution (skewed toward good)
        data["Network_Stability"] = self.rng.beta(2, 1, size=n)

        # Device_Resources: continuous 0-1, beta distribution (varied)
        data["Device_Resources"] = self.rng.beta(3, 2, size=n)

        # Device_Health: continuous 0-1, beta distribution (usually good, sometimes poor)
        data["Device_Health"] = self.rng.beta(5, 2, size=n)

        # Firmware_Version: continuous, normalized 0-1 (older = lower number)
        # Assume devices with older firmware are less common (more have recent versions)
        data["Firmware_Version"] = self.rng.beta(2, 3, size=n)

        # Device_Configuration: continuous 0-1, uniform (varied)
        data["Device_Configuration"] = self.rng.uniform(0, 1, size=n)

        return data

    def _generate_update_command(
        self,
        trigger: np.ndarray,
        firmware_version: np.ndarray,
        device_config: np.ndarray,
    ) -> np.ndarray:
        """
        Generate Update_Command based on its parents in the DAG.

        Update_Command depends on:
        - Update_Trigger: emergencies always trigger, manual sometimes, auto rarely
        - Firmware_Version: older firmware more likely to need updates
        - Device_Configuration: certain configurations may inhibit updates
        """
        logits = np.zeros(len(trigger))

        # Effect of Update_Trigger
        # Emergency (2): high probability of update
        # Manual (0): moderate probability
        # Automatic (1): lower probability
        logits += np.where(trigger == 2, 2.5, np.where(trigger == 0, 1.0, -0.5))

        # Effect of Firmware_Version (older firmware = more likely to update)
        logits += (1 - firmware_version) * 2.0

        # Effect of Device_Configuration (some configs may block updates)
        logits -= device_config * 0.5

        # Add noise
        logits += self.rng.normal(0, 0.3, size=len(trigger))

        # Convert to probability and sample
        prob = 1 / (1 + np.exp(-logits))
        return self.rng.binomial(1, prob)

    def _generate_update_success(
        self,
        update_cmd: np.ndarray,
        network_stability: np.ndarray,
        device_resources: np.ndarray,
        device_health: np.ndarray,
        firmware_version: np.ndarray,
        device_config: np.ndarray,
    ) -> np.ndarray:
        """
        Generate Update_Success based on its parents in the DAG.

        This is the main outcome variable. It depends on:
        - Update_Command (treatment): if no command, success is meaningless (set to 0)
        - Network_Stability: better network increases success
        - Device_Resources: more resources increase success
        - Device_Health: better health increases success
        - Firmware_Version: older firmware harder to update
        - Device_Configuration: certain configs may hinder updates
        """
        logits = np.zeros(len(update_cmd))

        # Base rate for when update command is given
        base_logit = 0.5

        # Treatment effect: Update_Command influences success (main causal effect)
        # But success is defined as 0 if no command was given
        logits += update_cmd * base_logit

        # Effect of Network_Stability
        logits += network_stability * 3.0

        # Effect of Device_Resources
        logits += device_resources * 2.0

        # Effect of Device_Health
        logits += device_health * 2.5

        # Effect of Firmware_Version (older = harder to update)
        logits -= (1 - firmware_version) * 1.5

        # Effect of Device_Configuration
        logits -= device_config * 1.0

        # Interactions: e.g., good network + good resources amplifies success
        logits += (network_stability * device_resources) * 1.0
        logits += (network_stability * device_health) * 0.5

        # Add noise
        logits += self.rng.normal(0, 0.4, size=len(update_cmd))

        # Convert to probability
        prob = 1 / (1 + np.exp(-logits))

        # If no update command was given, success is 0 by definition
        success = self.rng.binomial(1, prob)
        success[update_cmd == 0] = 0

        return success

    def _generate_rollback_needed(
        self, update_success: np.ndarray, network_stability: np.ndarray
    ) -> np.ndarray:
        """
        Generate Rollback_Needed.

        Typically rollback is needed when update fails, but sometimes
        successful updates might still require rollback (edge cases).
        Failed updates almost always need rollback.
        """
        prob = np.where(
            update_success == 1,
            0.05,  # Small chance of rollback even after success
            0.90,  # High chance of rollback after failure
        )

        # Network stability: if poor network, rollback more likely after failure
        prob = np.where(update_success == 0, prob + (1 - network_stability) * 0.1, prob)

        prob = np.clip(prob, 0, 1)
        return self.rng.binomial(1, prob)

    def _generate_device_downtime(
        self,
        update_success: np.ndarray,
        network_stability: np.ndarray,
        device_resources: np.ndarray,
    ) -> np.ndarray:
        """
        Generate Device_Downtime in seconds.

        - Successful updates: minimal downtime (fast reboot)
        - Failed updates: longer downtime (recovery, rollback)
        - Network issues can increase downtime (retries, timeouts)
        - Resource constraints can slow down processes
        """
        # Base downtime
        base_downtime = np.where(
            update_success == 1,
            self.rng.uniform(5, 30, size=len(update_success)),  # Fast successful update
            self.rng.uniform(
                60, 300, size=len(update_success)
            ),  # Longer failure recovery
        )

        # Network stability effect: worse network increases downtime
        network_factor = 1 + (1 - network_stability) * 2.0
        base_downtime *= network_factor

        # Resource constraints: fewer resources = slower operations
        resource_factor = 1 + (1 - device_resources) * 1.5
        base_downtime *= resource_factor

        # Add some noise
        downtime = base_downtime * self.rng.uniform(0.8, 1.2, size=len(update_success))

        return np.round(downtime, 1)


def generate_data(n_samples: int = 1000, seed: int = 42) -> pd.DataFrame:
    """
    Convenience function to generate synthetic firmware update data.

    Args:
        n_samples: Number of update attempts to simulate
        seed: Random seed for reproducibility

    Returns:
        DataFrame with simulated firmware update data
    """
    generator = DataGenerator(seed=seed)
    return generator.generate(n_samples)


# Exogenous variables (cause all other variables indirectly or directly)
EXOGENOUS_VARS = [
    "Update_Trigger",
    "Network_Stability",
    "Device_Resources",
    "Device_Health",
    "Firmware_Version",
    "Device_Configuration",
]

# Key variables
TREATMENT = "Update_Command"
OUTCOME = "Update_Success"
SECONDARY_OUTCOMES = ["Rollback_Needed", "Device_Downtime"]

ALL_VARS = EXOGENOUS_VARS + [TREATMENT] + [OUTCOME] + SECONDARY_OUTCOMES
