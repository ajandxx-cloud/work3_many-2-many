# Phase 03 Verification: Passenger Choice Model Rebuild

**Date:** 2026-06-15

## Result

Phase 03 passes verification.

## Requirements Verified

- **CHO-01:** Passenger utility model includes a service attractiveness constant through `ChoiceParameters.service_asc`, `experiments/config.py`, and variant constructor hooks.
- **CHO-02:** Outside option utility is explicit through `ChoiceParameters.outside_option_constant` and tested in the core choice evaluator.
- **CHO-03:** Passenger type parameters and shares are documented as inherited/simulation-range inputs in `03_PARAMETER_CALIBRATION.md` and wired through deterministic request-seeded assignment.
- **CHO-04:** Acceptance outcomes now emit utility-component logs and status-aware rows, with `utility_components.csv` as the joinable artifact.

## Verification Commands

```powershell
$env:PYTHONPATH='src'; pytest tests\test_choice.py tests\test_metrics.py tests\test_variants.py tests\test_runner.py -q
```

Result: passed, 77 tests.

```powershell
rg "_mnl_filter_requests|utility_components.csv|chosen output artifact" experiments\variants.py tests\test_variants.py .planning\phases\03-passenger-choice-model-rebuild\03_CHOICE_MODEL_CONTRACT.md
```

Result: `_mnl_filter_requests()` remains only as a quarantined legacy helper, a contract reference, and a regression-test monkeypatch target. No Phase 3 behavioral path calls it.

## Evidence

- Actual-offer behavioral sequence implemented in `experiments/variants.py`.
- Status schema and derived rates implemented in `experiments/metrics.py`.
- `utility_components.csv` output implemented in `experiments/runner.py`.
- Core actual-offer evaluator implemented in `src/drt/choice.py` and `src/drt/types.py`.
- Regression coverage added in `tests/test_choice.py`, `tests/test_metrics.py`, `tests/test_variants.py`, and `tests/test_runner.py`.

## Residual Risks

- Choice coefficients remain simulation-range values, not real-data calibration; this is documented and must be treated as sensitivity evidence rather than empirical behavioral estimation.
- Phase 4 still needs the baseline/algorithm implementation audit before pilot experiments.
- Formal evidence and manuscript claims remain blocked until Phase 5+ pilot/formal runs and Phase 8 claim gates.

## Decision

Phase 03 is complete and ready to hand off to Phase 04: Baseline and Algorithm Implementation Check.
