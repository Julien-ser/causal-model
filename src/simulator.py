"""
Simulator for evaluating agent performance in firmware update decisions.

Generates random device states and simulates outcomes using the true data generating process.
"""

import numpy as np
from src.data_generator import DataGenerator
from src.agent import Agent


class Simulator:
    def __init__(self, agent: Agent, n_episodes: int = 100, seed: int = 456):
        """
        Initialize simulator.

        Args:
            agent: Agent instance to evaluate.
            n_episodes: Number of decision episodes to simulate.
            seed: Random seed for reproducibility.
        """
        self.agent = agent
        self.n_episodes = n_episodes
        self.seed = seed
        self.rng = np.random.RandomState(seed)
        self.dg = DataGenerator(seed=seed)

    def run(self) -> dict:
        """
        Run the simulation loop.

        Returns:
            A dictionary containing success rates and episode details.
        """
        results = {
            "agent_success": 0,
            "agent_updates": 0,
            "always_update_success": 0,
            "details": [],
        }
        for _ in range(self.n_episodes):
            # Generate exogenous state for a single device
            exog = self.dg._generate_exogenous_vars(1)
            state = {k: v[0] for k, v in exog.items()}
            # Agent perceives and acts
            self.agent.perceive(state)
            action = self.agent.act()
            # Prepare arrays for DGP outcome generation
            arrays = {k: np.array([state[k]]) for k in state}
            cmd_array = np.array([1 if action == "update" else 0])
            # Generate outcome using true DGP
            success = self.dg._generate_update_success(
                update_cmd=cmd_array,
                network_stability=arrays["Network_Stability"],
                device_resources=arrays["Device_Resources"],
                device_health=arrays["Device_Health"],
                firmware_version=arrays["Firmware_Version"],
                device_config=arrays["Device_Configuration"],
            )[0]
            # Update agent metrics
            if action == "update" and success == 1:
                results["agent_success"] += 1
            if action == "update":
                results["agent_updates"] += 1
            # Always update baseline (for comparison)
            always_success = self.dg._generate_update_success(
                update_cmd=np.array([1]),
                network_stability=arrays["Network_Stability"],
                device_resources=arrays["Device_Resources"],
                device_health=arrays["Device_Health"],
                firmware_version=arrays["Firmware_Version"],
                device_config=arrays["Device_Configuration"],
            )[0]
            results["always_update_success"] += always_success
            # Record details
            results["details"].append(
                {"state": state, "action": action, "success": success}
            )
        total = self.n_episodes
        results["agent_success_rate"] = results["agent_success"] / total
        results["always_update_success_rate"] = results["always_update_success"] / total
        results["never_update_success_rate"] = (
            0.0  # never update always yields 0 success
        )
        return results
