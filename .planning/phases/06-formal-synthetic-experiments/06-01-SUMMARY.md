---
phase: 06-formal-synthetic-experiments
plan: 06-01
subsystem: experiments
tags: [phase06, formal, harness, validation, exp-05]
requires:
  - phase: 05-pilot-experiments
    provides: isolated behavioral-main runner pattern and persisted artifact validation
provides:
  - Phase 6 formal main harness with predeclared seeds, scales, methods, and manifests
  - persisted formal main validator and label/implementation gate
  - failure/rerun ledger scaffold
  - generated formal smoke artifacts under results/formal/phase06/smoke
affects: [phase06-formal-experiments, exp-05, phase08-claim-gate, phase10-final-verification]
tech-stack:
  added: []
  patterns: [runner variant scoping, formal manifest predeclaration, persisted artifact validation]
key-files:
  created:
    - experiments/phase06_formal.py
    - experiments/formal_validation.py
    - tests/test_phase06_formal.py
    - .planning/phases/06-formal-synthetic-experiments/06_FAILURE_RERUN_LEDGER.csv
    - results/formal/phase06/smoke/formal_seed_manifest.json
    - results/formal/phase06/smoke/formal_config_manifest.json
    - results/formal/phase06/smoke/synthetic_results.csv
    - results/formal/phase06/smoke/metrics_table.csv
    - results/formal/phase06/smoke/utility_components.csv
    - results/formal/phase06/smoke/main_matrix_validation.json
  modified: []
key-decisions:
  - "Formal Phase 6 main outputs default to results/formal/phase06/main and never overwrite legacy result CSVs."
  - "The formal main method filter selects exactly four behavioral-main method labels."
  - "The validator treats BidirectionalMP_Choice_RH_ALNS label/implementation drift as a blocking evidence gate before full formal runs."
patterns-established:
  - "Required seeds 1-20 and optional extension seeds 21-30 are predeclared in manifest JSON before execution."
  - "Failure and timeout rows append to 06_FAILURE_RERUN_LEDGER.csv using the original run_id/config_id cell identity."
requirements-completed: []
duration: 1 session
completed: 2026-06-16
status: completed_with_blocking_gate
---

# Phase 06 Plan 01: Formal Harness, Manifests, and Validators Summary

**Formal execution harness created; full main matrix is blocked by an evidence-label gate**

## Accomplishments

- Added `experiments/phase06_formal.py` with required seeds `1..20`, optional extension seeds `21..30`, formal scales `[100, 200, 300, 500]`, exact behavioral-main method labels, manifest writing, runner scoping, smoke execution, and validation CLI paths.
- Added `experiments/formal_validation.py` to validate persisted formal artifacts: required files, raw schema, quartet metrics, scale/seed/method membership, matrix completeness, failed/timeout status closure, utility-log joinability, rerun ledger entries, and the `BidirectionalMP_Choice_RH_ALNS` label/implementation gate.
- Added `tests/test_phase06_formal.py` covering constants, manifests, exact filtering, isolated output writing, missing-cell blocking, failed/timeout blocking, missing utility rows, forbidden scale `20`, label-gate reporting, and ledger header shape.
- Ran a real smoke matrix for `scale=100`, `seed=1`, four behavioral-main methods, producing raw rows, metrics, utility logs, manifests, and validation output under `results/formal/phase06/smoke`.

## Task Commit

- This commit - `feat(06-01): add formal experiment harness gate`

## Gate Result

The smoke matrix itself is structurally complete:

- `synthetic_results`: 4 rows.
- `metrics_table`: 4 rows.
- `utility_components`: 400 rows.
- Failed rows: 0.
- Timeout rows: 0.

The validator correctly returns `passed: false` because `FullModel` is still labeled as `BidirectionalMP_Choice_RH_ALNS` while `FullModel._solve()` delegates to the common sequential actual-offer path rather than a rolling-horizon/ALNS implementation. This blocks the full 20-seed formal main matrix until the project either implements the labeled behavior or explicitly downgrades the paper-facing method label and downstream claim scope.

## Verification

- `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py -q` -> 11 passed.
- `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py tests/test_variants.py -q` -> 34 passed.
- `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py tests/test_runner.py tests/test_metrics.py -q` -> 65 passed.
- `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py -q` -> 88 passed.
- `$env:PYTHONPATH='src'; python -m experiments.phase06_formal --family main --scales 100 --seeds 1 --results-dir results/formal/phase06/smoke` -> generated 4 formal smoke rows and utility logs.
- `$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --scales 100 --seeds 1 --results-dir results/formal/phase06/smoke` -> expected failure on the label/implementation gate.

## Next Action

Do not start Plan 06-02's 320-row formal main matrix yet. First resolve the `BidirectionalMP_Choice_RH_ALNS` gate by either:

1. implementing actual rolling-horizon/ALNS behavior for the behavioral `FullModel` path while preserving actual-offer choice and utility logging, or
2. downgrading the method metadata, Phase 6 method manifest, Phase 8 claim scope, and manuscript language so the paper-facing label no longer claims rolling-horizon/ALNS.

Path 1 preserves the current Phase 2/Phase 9 contract. Path 2 is more conservative but requires replanning downstream claims.
