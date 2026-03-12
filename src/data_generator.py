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

        # Update_Trigger: categorical with string labels
        # Manual updates are most common, automatic less so, emergency rare
        trigger_options = ["manual", "auto", "emergency"]
        trigger_probs = [0.6, 0.3, 0.1]
        data["Update_Trigger"] = self.rng.choice(
            trigger_options, size=n, p=trigger_probs
        )

        # Network_Stability: continuous 0-1, beta distribution (skewed toward good)
        data["Network_Stability"] = self.rng.beta(2, 1, size=n)

        # Device_Resources: continuous 0-1, beta distribution (varied)
        data["Device_Resources"] = self.rng.beta(3, 2, size=n)

        # Device_Health: continuous 0-1, beta distribution (usually good, sometimes poor)
        data["Device_Health"] = self.rng.beta(5, 2, size=n)

        # Firmware_Version: categorical with realistic version strings
        # Assume devices with older firmware are less common (more have recent versions)
        fw_options = ["v1.0", "v1.5", "v2.0", "v2.5", "v3.0"]
        fw_probs = [0.05, 0.15, 0.3, 0.3, 0.2]
        data["Firmware_Version"] = self.rng.choice(fw_options, size=n, p=fw_probs)

        # Device_Configuration: categorical (risk level)
        config_options = ["low", "medium", "high"]
        config_probs = [0.4, 0.4, 0.2]
        data["Device_Configuration"] = self.rng.choice(
            config_options, size=n, p=config_probs
        )

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
        n = len(trigger)
        logits = np.zeros(n)

        # Effect of Update_Trigger (string values)
        trigger_effect = np.zeros(n)
        for i, t in enumerate(trigger):
            if t == "emergency":
                trigger_effect[i] = 2.5
            elif t == "manual":
                trigger_effect[i] = 1.0
            else:  # auto
                trigger_effect[i] = -0.5
        logits += trigger_effect

        # Effect of Firmware_Version (older firmware = more likely to update)
        fw_effect = np.zeros(n)
        for i, fw in enumerate(firmware_version):
            if fw in ["v1.0", "v1.5"]:
                fw_effect[i] = 0.4
            elif fw == "v2.0":
                fw_effect[i] = 0.2
            else:  # v2.5, v3.0
                fw_effect[i] = 0.0
        logits += fw_effect

        # Effect of Device_Configuration (high security configs may block updates)
        config_effect = np.zeros(n)
        for i, cfg in enumerate(device_config):
            if cfg == "high":
                config_effect[i] = -0.5
            elif cfg == "medium":
                config_effect[i] = -0.2
            else:  # low
                config_effect[i] = 0.0
        logits += config_effect

        # Add noise
        logits += self.rng.normal(0, 0.3, size=n)

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
        n = len(update_cmd)
        logits = np.zeros(n)

        # Base rate for when update command is given
        base_logit = 0.5

        # Treatment effect: Update_Command influences success (main causal effect)
        # But success is defined as 0 if no command was given
        logits += update_cmd * base_logit

        # Effect of Network_Stability (continuous 0-1)
        logits += network_stability * 3.0

        # Effect of Device_Resources (continuous 0-1)
        logits += device_resources * 2.0

        # Effect of Device_Health (continuous 0-1)
        logits += device_health * 2.5

        # Effect of Firmware_Version (categorical: older versions have lower success)
        for i, fw in enumerate(firmware_version):
            if fw in ["v1.0", "v1.5"]:
                logits[i] -= 1.0  # Older firmware = harder to update
            elif fw == "v2.0":
                logits[i] -= 0.5
            else:  # v2.5, v3.0
                logits[i] -= 0.0

        # Effect of Device_Configuration (categorical)
        for i, cfg in enumerate(device_config):
            if cfg == "high":
                logits[i] -= 1.0  # High security configs hinder updates
            elif cfg == "medium":
                logits[i] -= 0.5
            else:  # low
                logits[i] -= 0.0

        # Interactions: e.g., good network + good resources amplifies success
        logits += (network_stability * device_resources) * 1.0
        logits += (network_stability * device_health) * 0.5

        # Add noise
        logits += self.rng.normal(0, 0.4, size=n)

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
