# Causal DAG Structure

```
Update_Trigger ──────┬────> Update_Command ─────> Update_Success ─────> Rollback_Needed
                     │                         ├────> Device_Downtime
                     │                         ↑
                     │                         │
Firmware_Version ───┴────> Update_Command     │
Device_Configuration ──────────────┬─────────┤
                                    │         │
Network_Stability ──────────────────┼─────────┤
Device_Resources ───────────────────┼─────────┤
Device_Health ──────────────────────┼─────────┘
                                    │
                                    ↓
                                Update_Success
```

## Legend

- **Treatment**: `Update_Command` - whether to issue update
- **Outcome**: `Update_Success` - whether update succeeded
- **Confounders**: Variables that affect both treatment and outcome (Firmware_Version, Device_Configuration)
- **Moderators**: Variables that affect the treatment-outcome relationship (Network_Stability, Device_Resources, Device_Health)
- **Trigger**: Root cause that influences the decision to update
- **Consequences**: Downstream effects (Rollback_Needed, Device_Downtime)

## Key Relationships

1. **Main causal effect**: `Update_Command → Update_Success`
   - This is the primary relationship we want to estimate
   - The causal effect may be modified by moderators

2. **Backdoor paths** (confounding):
   - `Update_Command ← Firmware_Version → Update_Success`
   - `Update_Command ← Device_Configuration → Update_Success`
   - These must be blocked to estimate the causal effect

3. **Frontdoor paths** (mediation):
   - `Update_Command → Update_Success → Rollback_Needed`
   - `Update_Command → Update_Success → Device_Downtime`

## Identification Strategy

To identify the causal effect of `Update_Command` on `Update_Success`:

1. **Adjust for confounders**: Include `Firmware_Version` and `Device_Configuration` as covariates
2. **Condition on moderators**: Optionally stratify by `Network_Stability`, `Device_Resources`, `Device_Health`
3. **Use backdoor criterion**: The set {Firmware_Version, Device_Configuration} blocks all backdoor paths from Update_Command to Update_Success
