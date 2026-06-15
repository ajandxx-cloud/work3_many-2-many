---
phase: 05-pilot-experiments
plan: 05-01
subsystem: experiments
tags: [phase05, pilot, validation, rep-03]
requires:
  - phase: 04-baseline-and-algorithm-implementation-check
    provides: runner schema, behavioral variant metadata, durable failure rows
provides:
  - isolated Phase 5 pilot runner for the four behavioral-main methods
  - persisted CSV validator for REP-03 status, provenance, metrics, and utility logs
  - generated pilot artifacts under results/pilot/phase05
affects: [phase05, phase06-formal-experiments, rep-03]
tech-stack:
  added: []
  patterns: [runner variant scoping, persisted artifact validation]
key-files:
  created:
    - experiments/phase05_pilot.py
    - experiments/pilot_validation.py
    - tests/test_phase05_pilot.py
    - results/pilot/phase05/synthetic_results.csv
    - results/pilot/phase05/metrics_table.csv
    - results/pilot/phase05/utility_components.csv
  modified: []
key-decisions:
  - "The Phase 5 main pilot selects variants by exact method_label plus evidence_family == behavioral_main."
  - "Pilot validation checks persisted files rather than in-memory rows."
patterns-established:
  - "Pilot outputs stay isolated under results/pilot/phase05."
  - "Utility logs are validated by run_id, seed, scenario, and variant identity for completed behavioral-main rows."
requirements-completed: [REP-03]
duration: 14 min
completed: 2026-06-15
---

# Phase 05 Plan 01: Pilot Harness and Artifact Validator Summary

**Isolated Phase 5 behavioral pilot runner with persisted REP-03 artifact validation**

## Performance

- **Duration:** 14 min
- **Started:** 2026-06-15T13:30:00Z
- **Completed:** 2026-06-15T13:44:00Z
- **Tasks:** 3
- **Files modified:** 6

## Accomplishments

- Added `experiments/phase05_pilot.py` to run exactly the four behavioral-main methods on the Phase 5 pilot scale and seeds.
- Added `experiments/pilot_validation.py` to validate persisted status, provenance, metric range, non-negative metric, and utility joinability requirements.
- Added focused Phase 5 tests covering method selection, isolated output directories, status blockers, metric range blockers, provenance checks, and utility joinability.
- Generated `results/pilot/phase05/synthetic_results.csv`, `metrics_table.csv`, and `utility_components.csv`.

## Task Commits

1. **Task 1-3: Pilot harness, validator, and focused tests** - `4721fa7` (`feat(05-01)`)

## Files Created/Modified

- `experiments/phase05_pilot.py` - Phase 5 wrapper around the existing runner with exact behavioral-main method selection.
- `experiments/pilot_validation.py` - Persisted CSV validator for Phase 5 readiness gates.
- `tests/test_phase05_pilot.py` - Focused tests for the pilot harness and validator.
- `results/pilot/phase05/synthetic_results.csv` - Generated 12-row main behavioral pilot output.
- `results/pilot/phase05/metrics_table.csv` - Generated aggregate metric table for the four pilot methods.
- `results/pilot/phase05/utility_components.csv` - Generated utility/component logs for all completed pilot runs.

## Decisions Made

- Selected the main pilot matrix by exact method label and `behavioral_main` evidence family to prevent diagnostic methods from leaking into main pilot evidence.
- Treated `detour_ratio` according to the Phase 2 metric contract as non-negative rather than bounded by `[0, 1]`; bounded ratio checks remain enforced for share/proportion fields.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- PowerShell does not support Bash-style heredoc syntax for `python - <<'PY'`; verification commands were rerun with PowerShell-native `python -c`.

## Verification

- `PYTHONPATH=src pytest tests/test_phase05_pilot.py -q` -> 8 passed.
- `PYTHONPATH=src pytest tests/test_runner.py tests/test_metrics.py tests/test_variants.py -q` -> 77 passed.
- `PYTHONPATH=src python -m experiments.phase05_pilot` -> generated 12 synthetic pilot rows, 4 metric rows, and utility logs under `results/pilot/phase05`.
- `validate_phase05_outputs(...)` -> passed with 0 failed rows, 0 timeout rows, and 240 utility rows.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Ready for `05-02`: coverage-control and fixed accepted-set diagnostic smokes can build on the generated pilot outputs and validator.

---
*Phase: 05-pilot-experiments*
*Completed: 2026-06-15*
