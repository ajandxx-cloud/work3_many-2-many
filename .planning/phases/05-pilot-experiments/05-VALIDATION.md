---
phase: 05
slug: pilot-experiments
status: draft
nyquist_compliant: true
wave_0_complete: true
created: 2026-06-15
---

# Phase 05 - Validation Strategy

## Test Infrastructure

| Property | Value |
|----------|-------|
| Framework | pytest |
| Config file | none |
| Quick run command | `PYTHONPATH=src pytest tests/test_runner.py tests/test_metrics.py tests/test_variants.py -q` |
| Phase-focused command | `PYTHONPATH=src pytest tests/test_phase05_pilot.py -q` |
| Smoke command | `PYTHONPATH=src python -m experiments.phase05_pilot` |
| Estimated runtime | 30-180 seconds depending on FullModel runtime |

## Sampling Rate

- After every task commit: run the focused test file if it exists, otherwise the quick run command.
- After each wave: run the full quick run command plus `tests/test_phase05_pilot.py`.
- Before verify-work: run the pilot smoke command and verify all gate artifacts exist.
- Max feedback latency: one task.

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 05-01-01 | 05-01 | 1 | REP-03 | unit/integration | `PYTHONPATH=src pytest tests/test_phase05_pilot.py -q` | yes | pending |
| 05-01-02 | 05-01 | 1 | REP-03 | integration | `PYTHONPATH=src pytest tests/test_phase05_pilot.py tests/test_runner.py -q` | yes | pending |
| 05-02-01 | 05-02 | 2 | REP-03 | unit/integration | `PYTHONPATH=src pytest tests/test_phase05_pilot.py -q` | yes | pending |
| 05-02-02 | 05-02 | 2 | REP-03 | smoke | `PYTHONPATH=src python -m experiments.phase05_coverage_smoke` | yes | pending |
| 05-03-01 | 05-03 | 3 | REP-03 | smoke | `PYTHONPATH=src python -m experiments.phase05_pilot` | yes | pending |
| 05-03-02 | 05-03 | 3 | REP-03 | artifact check | `PYTHONPATH=src pytest tests/test_phase05_pilot.py -q` | yes | pending |

## Wave 0 Requirements

Existing infrastructure covers the phase:

- `tests/test_runner.py`
- `tests/test_metrics.py`
- `tests/test_variants.py`
- `experiments/runner.py`
- `experiments/metrics.py`
- `experiments/variants.py`

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Bug ledger triage | REP-03 | The executor must judge whether each discovered issue blocks Phase 6 | Inspect `05_BUG_LEDGER.csv` and confirm every open blocker has a fix or rerun record |
| No manuscript claims | Phase boundary | This is a writing/content gate | Confirm `05_PILOT_RESULTS.md` contains no method-superiority language or formal evidence claims |

## Validation Sign-Off

- [x] All planned tasks have automated verification or artifact checks.
- [x] Sampling continuity has no three-task gap without automated verification.
- [x] Wave 0 infrastructure exists.
- [x] No watch-mode flags are used.
- [x] `nyquist_compliant: true` is set in frontmatter.

Approval: pending execution

