# Firmware Update Data Schema

## Overview
This document defines the schema for synthetic firmware update data used in the causal model.

## Core Tables

### 1. update_attempts
Main table tracking each firmware update attempt.

| Column | Type | Description |
|--------|------|-------------|
| attempt_id | int (PK) | Unique identifier for each attempt |
| device_id | str | Device identifier |
| timestamp | datetime | When the update was attempted |
| update_trigger | categorical | Type: 'manual', 'automatic', 'emergency' |
| firmware_version | str | Current version before update (e.g., '1.2.3') |
| update_command | binary (0/1) | Whether update command was issued |
| network_stability | float | Network quality score (0.0-1.0) |
| device_resources | float | Resource availability score (0.0-1.0) |
| device_health | float | Health score (0.0-1.0) |
| device_configuration | categorical | Config type: 'standard', 'secure', 'legacy' |
| update_success | binary (0/1) | Whether update completed successfully |
| rollback_needed | binary (0/1) | Whether rollback was performed |
| device_downtime | float | Downtime in seconds |
| update_duration | float | Total update time in seconds |
| failure_mode | categorical (nullable) | If failed: 'network', 'resource', 'validation', 'power', 'unknown' |

### 2. devices
Static device information.

| Column | Type | Description |
|--------|------|-------------|
| device_id | str (PK) | Unique device identifier |
| device_type | categorical | 'sensor', 'gateway', 'controller', 'display' |
| deployment_date | datetime | When device was deployed |
| location | str | Geographic/operational location |
| hardware_specs | json | CPU, memory, storage specs |
| power_source | categorical | 'battery', ' wired', 'solar' |
| connectivity | categorical | 'wifi', 'cellular', 'ethernet', 'bluetooth' |

### 3. firmware_versions
Version history and metadata.

| Column | Type | Description |
|--------|------|-------------|
| version | str (PK) | Version string (e.g., '1.2.3') |
| release_date | datetime | When version was released |
| size_mb | float | Firmware package size in MB |
| is_security_update | binary | Whether this is a security patch |
| previous_version | str | Reference to previous version |
| update_complexity | categorical | 'low', 'medium', 'high' |

### 4. update_failures
Detailed failure analysis (only populated for failed attempts).

| Column | Type | Description |
|--------|------|-------------|
| failure_id | int (PK) | Unique failure identifier |
| attempt_id | int (FK) | References update_attempts.attempt_id |
| error_code | str | System error code |
| error_message | text | Human-readable error |
| failure_timestamp | datetime | When failure occurred |
| recovery_action | categorical | 'rollback', 'retry', 'manual_intervention' |
| logs_available | binary | Whether full logs were captured |

## Synthetic Data Generation Parameters

The data generator will produce 1000 samples with:

### Variable Distributions
- **update_trigger**: manual (40%), automatic (45%), emergency (15%)
- **network_stability**: Beta(α=2, β=1.5) truncated to [0.2, 1.0]
- **device_resources**: Normal(μ=0.7, σ=0.2) truncated to [0.1, 1.0]
- **device_health**: Normal(μ=0.8, σ=0.15) truncated to [0.2, 1.0]
- **update_command**: Bernoulli(p=0.75) - depends on trigger
- **update_success**: Depends on treatment and confounders (target ACE ~0.3)
- **failure_mode** distribution: network (35%), resource (25%), validation (20%), power (15%), unknown (5%)

### Confounding Structure
- Older firmwares are less likely to receive updates (Update_Command ↓)
- Older firmwares are harder to update (Update_Success ↓)
- Poor device_health reduces both update_command issuance and success
- Emergency triggers bypass normal checks (higher command rate, variable success)

### Temporal Effects
- Device wear over time decreases device_health
- Network stability varies diurnally
- Update success improves over time as bugs are fixed

## Data Files

Generated data will be saved as:
- `data/synthetic_updates.csv` - Main update attempts table
- `data/devices.csv` - Device catalog
- `data/firmware_versions.csv` - Version metadata
- `data/update_failures.csv` - Failure details

## Usage

```python
from src.data_generator import CausalDataGenerator

generator = CausalDataGenerator(n_samples=1000, seed=42)
data = generator.generate_data()
generator.save_data('data/')
```
