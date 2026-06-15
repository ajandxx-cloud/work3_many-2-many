---
phase: 05-pilot-experiments
status: gaps_found
verified: 2026-06-15
requirements: [REP-03]
plans_verified: [05-01, 05-02, 05-03]
---

# Phase 5 Verification

## Verification Complete

Status: `gaps_found`

Phase 5 executed all planned pilot work, but the phase goal is not fully achieved because Phase 6 readiness is blocked by unresolved pilot diagnostic issues.

## Must-Have Results

| Criterion | Status | Evidence |
|---|---|---|
| Four main behavioral methods run on 3 synthetic pilot seeds at scale 20 | passed | `results/pilot/phase05/synthetic_results.csv` has 12 main behavioral rows |
| Main behavioral pilot has zero failed rows and zero timeout rows | passed | `validate_phase05_outputs(...)` reports `failed_rows: 0`, `timeout_rows: 0` |
| Persisted REP-03 status/provenance fields are present | passed | `validate_phase05_outputs(...)` passed schema/provenance checks |
| Utility/component logs are durable and joinable | passed | `validate_phase05_outputs(...)` reports 240 utility rows and passed joinability |
| Metric sanity checks pass for persisted main pilot rows | passed | Share fields in range; non-negative numeric fields; no NaN/infinity |
| Matched-coverage diagnostic passes tolerance | failed | `BUG-05-001` and `BUG-05-002` in `05_BUG_LEDGER.csv` |
| Fixed accepted-set smoke produces a retained set and routing diagnostic | failed | `BUG-05-003` in `05_BUG_LEDGER.csv` |
| Gate report avoids formal claims and method-superiority framing | passed | `05_PILOT_RESULTS.md` states no formal claims and contains diagnostic-only limitations |
| Phase 6 readiness is controlled by bug ledger blockers | passed | `.planning/STATE.md` marks Phase 6 blocked while ledger rows remain open |

## Automated Checks

```powershell
$env:PYTHONPATH='src'; pytest tests/test_phase05_pilot.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py -q
```

Result: 90 passed.

```powershell
gsd-sdk query verify.schema-drift 05
```

Result: no schema drift detected.

## Gaps

### BUG-05-001

- Source: `results/pilot/phase05/matched_coverage_pilot.csv`
- Trigger: `scale=20 tolerance=0.03`, seed 42
- Symptom: matched-coverage served-share gap `0.0833` exceeds tolerance `0.03`
- Blocks Phase 6: yes

### BUG-05-002

- Source: `results/pilot/phase05/matched_coverage_pilot.csv`
- Trigger: `scale=20 tolerance=0.03`, seed 44
- Symptom: matched-coverage served-share gap `0.0333` exceeds tolerance `0.03`
- Blocks Phase 6: yes

### BUG-05-003

- Source: `results/pilot/phase05/fixed_accepted_set_smoke.json`
- Trigger: `scale=20 seed=42`
- Symptom: common served request intersection is empty, so fixed-set routing diagnostic was skipped
- Blocks Phase 6: yes

## Required Follow-Up

Run a gap-closure planning cycle before Phase 6:

```text
$gsd-plan-phase 5 --gaps
```

Expected gap-closure scope:

- Fix or redesign matched-coverage cap/target logic and rerun `python -m experiments.phase05_coverage_smoke`.
- Resolve or redesign the fixed accepted-set smoke so it produces an approved diagnostic outcome.
- Update `05_BUG_LEDGER.csv` with fixed or approved non-blocking dispositions and rerun verification.

