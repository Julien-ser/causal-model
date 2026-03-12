"""
Unit tests for the synthetic data generator.

These tests validate that the generated data has correct structure,
reasonable distributions, and respects causal relationships.
"""

import pytest
import numpy as np
import pandas as pd
from src.data_generator import (
    DataGenerator,
    generate_data,
    ALL_VARS,
    TREATMENT,
    OUTCOME,
)


class TestDataGenerator:
    """Test suite for synthetic data generation."""

    def test_generator_initialization(self):
        """Test that DataGenerator can be initialized with a seed."""
        gen = DataGenerator(seed=42)
        assert gen.seed == 42
        assert isinstance(gen.rng, np.random.RandomState)

    def test_generate_data_shape(self):
        """Test that generated data has correct shape and columns."""
        df = generate_data(n_samples=100)
        assert df.shape[0] == 100
        assert list(df.columns) == ALL_VARS

    def test_generate_default_samples(self):
        """Test that default generates 1000 samples."""
        df = generate_data()
        assert len(df) == 1000

    def test_all_variables_present(self):
        """Test that all required variables are present."""
        df = generate_data(n_samples=50)
        for var in ALL_VARS:
            assert var in df.columns, f"Missing variable: {var}"

    def test_binary_variables_are_binary(self):
        """Test that binary variables are indeed 0/1."""
        df = generate_data(n_samples=100)
        binary_vars = [TREATMENT, OUTCOME, "Rollback_Needed"]
        for var in binary_vars:
            unique_vals = df[var].unique()
            assert set(unique_vals).issubset({0, 1}), f"{var} should be binary"

    def test_continuous_variables_in_range(self):
        """Test that continuous variables are within expected ranges."""
        df = generate_data(n_samples=100)

        # These variables should be between 0 and 1 (continuous)
        continuous_vars = [
            "Network_Stability",
            "Device_Resources",
            "Device_Health",
        ]
        for var in continuous_vars:
            assert df[var].min() >= 0, f"{var} should be >= 0"
            assert df[var].max() <= 1, f"{var} should be <= 1"

        # These variables should be categorical strings
        categorical_vars = [
            "Update_Trigger",
            "Firmware_Version",
            "Device_Configuration",
        ]
        for var in categorical_vars:
            assert df[var].dtype == object, f"{var} should be object/categorical type"
            assert df[var].notnull().all(), f"{var} should have no nulls"

    def test_downtime_is_positive(self):
        """Test that Device_Downtime is positive."""
        df = generate_data(n_samples=100)
        assert (df["Device_Downtime"] >= 0).all()

    def test_update_success_zero_without_command(self):
        """Test that Update_Success is 0 when Update_Command is 0."""
        df = generate_data(n_samples=1000)
        no_command = df[df["Update_Command"] == 0]
        assert (no_command["Update_Success"] == 0).all(), (
            "Update_Success should be 0 when Update_Command is 0"
        )

    def test_update_command_correlation_with_trigger(self):
        """Test that Update_Command correlates with Update_Trigger."""
        df = generate_data(n_samples=1000)
        # Emergency triggers should have higher command rate
        emergency_rate = df[df["Update_Trigger"] == "emergency"][
            "Update_Command"
        ].mean()
        manual_rate = df[df["Update_Trigger"] == "manual"]["Update_Command"].mean()
        auto_rate = df[df["Update_Trigger"] == "auto"]["Update_Command"].mean()

        assert emergency_rate > manual_rate > auto_rate, (
            f"Trigger correlation: emergency={emergency_rate:.2f}, manual={manual_rate:.2f}, auto={auto_rate:.2f}"
        )

    def test_update_command_correlation_with_firmware(self):
        """Test that older firmware correlates with more update commands."""
        df = generate_data(n_samples=1000)
        # Define old vs new firmware versions
        old_versions = ["v1.0", "v1.5", "v2.0"]
        new_versions = ["v2.5", "v3.0"]

        old_firmware = df[df["Firmware_Version"].isin(old_versions)][
            "Update_Command"
        ].mean()
        new_firmware = df[df["Firmware_Version"].isin(new_versions)][
            "Update_Command"
        ].mean()

        assert old_firmware > new_firmware, (
            f"Older firmware should trigger more updates: old={old_firmware:.2f}, new={new_firmware:.2f}"
        )

    def test_update_success_correlation_with_network(self):
        """Test that better network stability correlates with update success."""
        df = generate_data(n_samples=1000)
        # Only consider cases where update was attempted
        attempted = df[df["Update_Command"] == 1]
        median_network = attempted["Network_Stability"].median()

        good_network_success = attempted[
            attempted["Network_Stability"] > median_network
        ]["Update_Success"].mean()
        poor_network_success = attempted[
            attempted["Network_Stability"] <= median_network
        ]["Update_Success"].mean()

        assert good_network_success > poor_network_success, (
            f"Network should affect success: good={good_network_success:.2f}, poor={poor_network_success:.2f}"
        )

    def test_rollback_correlation_with_success(self):
        """Test that rollback is more likely when update fails."""
        df = generate_data(n_samples=1000)
        success_rollback = df[df["Update_Success"] == 1]["Rollback_Needed"].mean()
        failure_rollback = df[df["Update_Success"] == 0]["Rollback_Needed"].mean()

        assert failure_rollback > success_rollback, (
            f"Rollback should be more likely after failure: fail={failure_rollback:.2f}, success={success_rollback:.2f}"
        )

    def test_downtime_correlation_with_success(self):
        """Test that downtime is longer when update fails."""
        df = generate_data(n_samples=1000)
        success_downtime = df[df["Update_Success"] == 1]["Device_Downtime"].mean()
        failure_downtime = df[df["Update_Success"] == 0]["Device_Downtime"].mean()

        assert failure_downtime > success_downtime * 2, (
            f"Failed updates should have significantly longer downtime: fail={failure_downtime:.1f}, success={success_downtime:.1f}"
        )

    def test_reproducibility_with_seed(self):
        """Test that same seed produces identical data."""
        df1 = generate_data(n_samples=100, seed=123)
        df2 = generate_data(n_samples=100, seed=123)
        pd.testing.assert_frame_equal(df1, df2)

    def test_different_seeds_produce_different_data(self):
        """Test that different seeds produce different data."""
        df1 = generate_data(n_samples=100, seed=123)
        df2 = generate_data(n_samples=100, seed=456)
        with pytest.raises(AssertionError):
            pd.testing.assert_frame_equal(df1, df2)

    def test_variability_in_generated_data(self):
        """Test that data has reasonable variability (not all same)."""
        df = generate_data(n_samples=100)
        # Update_Command should not be all 0 or all 1
        assert 0 < df["Update_Command"].mean() < 1
        # Update_Success should not be all 0 or all 1 (among attempted)
        attempted_success = df[df["Update_Command"] == 1]["Update_Success"].mean()
        assert 0 < attempted_success < 1

    def test_no_nulls_in_generated_data(self):
        """Test that generated data has no null values."""
        df = generate_data(n_samples=100)
        assert df.notnull().all().all()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
