# Phase 04 Implementation Audit

## Baseline Family Status

Phase 04 now exposes the four required behavioral service-design variants under
the shared actual-offer choice harness:

| Decision | Status | Evidence |
|---|---|---|
| D-01 | Complete | `DoorToDoor`, `SingleSidedPickup`, `SingleSidedDropoff`, and `FullModel` run on the shared small-scenario harness. |
| D-02 | Complete | `SingleSidedDropoff` uses door-to-door pickup and dropoff-side meeting points. |
| D-03 | Complete | Legacy classes remain available, while concept labels are exposed through `method_metadata`. |
| D-04 | Complete | Method metadata includes `method_label`, `service_design`, `choice_model`, `reoptimization`, `routing_solver`, `evidence_family`, `diagnostic_role`, and `legacy_class` where relevant. |
| D-05 | Complete | `VARIANT_MAPPING.md` maps code variants to concept labels and evidence roles. |
| D-06 | Complete | Variant metadata separates behavioral, supplementary, deterministic, and algorithm diagnostic evidence families. |
| D-07 | Complete | Tests monkeypatch `_mnl_filter_requests` and behavioral variants still run. |
| D-08 | Complete | Tests validate utility logs, rejected request exclusion, and one row per original request. |
| D-09 | Complete | Door-to-door served records have zero pickup and dropoff walk. |
| D-10 | Complete | Passenger type maps are identical across the four behavioral service designs for a shared seed/request pair. |
| D-11 | Complete | Acceptance draws are request-seeded in `evaluate_single_offer`, independent of variant execution order. |

## Deterministic Diagnostics

`BidirectionalNoChoice`, `AblationNoChoice`, and no-rolling-horizon variants are
kept available as diagnostics. Their `evidence_family` and `diagnostic_role`
metadata prevent accidental mixing with behavioral main comparisons.

## Runner Schema and Failure Rows

`04_BASELINE_VALIDATION.md` records the Phase 04 runner schema contract,
failure-row behavior, timeout handling, and metric denominator checks. Raw
runner rows now carry the D-22/D-23 method, provenance, status, and count fields;
failed and timeout runs are persisted as rows instead of being silently omitted.

## Required Tests

```bash
PYTHONPATH=src pytest tests/test_variants.py -q
PYTHONPATH=src pytest tests/test_runner.py tests/test_metrics.py -q
```

Latest local results:

- `tests/test_variants.py`: 21 passed.
- `tests/test_runner.py tests/test_metrics.py`: 54 passed.

## Caveats

- This audit validates small-scenario behavior only. Phase 5 owns pilot smoke
  runs and Phase 6 owns formal paired experiments.
- `FullModel` remains the implementation class name for provenance; paper-facing
  outputs must use `BidirectionalMP_Choice_RH_ALNS`.
