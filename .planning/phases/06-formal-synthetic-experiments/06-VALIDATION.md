---
phase: 06
slug: formal-synthetic-experiments
status: draft
nyquist_compliant: true
wave_0_complete: false
created: 2026-06-15
---

# Phase 06 - Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | pytest |
| **Config file** | none |
| **Quick run command** | `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py tests/test_metrics.py tests/test_variants.py -q` |
| **Full suite command** | `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py tests/test_milp.py -q` |
| **Estimated runtime** | quick: under 60 seconds after tests exist; full: solver-dependent, MILP skips when unavailable |

## Sampling Rate

- **After every task commit:** Run the quick command or the task-specific command.
- **After every plan wave:** Run the full suite command plus the relevant persisted-artifact validator.
- **Before `$gsd-verify-work`:** Formal main and supplementary validators must pass against persisted outputs.
- **Max feedback latency:** under 60 seconds for unit/schema checks; formal run validation can be longer because it samples generated artifacts.

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 06-01-01 | 06-01 | 1 | EXP-05 | T-06-01 | Formal seed/config manifest prevents untracked replacement seeds | unit | `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py -q` | W0 | pending |
| 06-01-02 | 06-01 | 1 | EXP-05 | T-06-02 | Main runner filters exact behavioral-main methods only | unit/integration | `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py tests/test_variants.py -q` | W0 | pending |
| 06-01-03 | 06-01 | 1 | EXP-05 | T-06-03 | Validator blocks missing rows, failed rows, timeout rows, and missing utility logs | unit | `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py -q` | W0 | pending |
| 06-02-01 | 06-02 | 2 | EXP-05 | T-06-04 | Main smoke run writes to isolated formal directory | integration | `$env:PYTHONPATH='src'; python -m experiments.phase06_formal --family main --scales 100 --seeds 1 --results-dir results/formal/phase06/smoke` | W1 | pending |
| 06-02-02 | 06-02 | 2 | EXP-05 | T-06-05 | Formal main matrix preserves failed/timeout rows and reruns same cells | artifact | `$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main` | W1 | pending |
| 06-03-01 | 06-03 | 2 | EXP-05 | T-06-06 | Matched coverage records target basis and blocks invalid targets | unit/integration | `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py -q` | W1 | pending |
| 06-03-02 | 06-03 | 2 | EXP-05 | T-06-07 | Fixed accepted-set package records construction rule and retained count | unit/integration | `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py -q` | W1 | pending |
| 06-03-03 | 06-03 | 2 | EXP-05 | T-06-08 | Utility sensitivity keeps baseline and sensitivity rows separate | artifact | `$env:PYTHONPATH='src'; python -m experiments.phase06_supplementary --package utility_sensitivity --validate` | W1 | pending |
| 06-04-01 | 06-04 | 2 | EXP-05 | T-06-09 | Robustness diagnostics cannot become behavioral-main evidence | artifact | `$env:PYTHONPATH='src'; python -m experiments.phase06_supplementary --validate` | W1 | pending |
| 06-04-02 | 06-04 | 2 | EXP-05 | T-06-10 | MILP no-solver/timeout/incomparable states remain durable rows | unit | `$env:PYTHONPATH='src'; pytest tests/test_milp.py tests/test_phase06_formal.py -q` | W1 | pending |
| 06-05-01 | 06-05 | 3 | EXP-05 | T-06-11 | Paired bootstrap CIs use complete paired keys only | unit/artifact | `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py tests/test_metrics.py -q` | W2 | pending |
| 06-05-02 | 06-05 | 3 | EXP-05 | T-06-12 | Evidence report links all raw, processed, config, failure, rerun, CI, and gate artifacts | source/artifact | `$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06` | W2 | pending |

## Wave 0 Requirements

- [ ] `tests/test_phase06_formal.py` - stubs and assertions for Phase 6 manifests, filters, validators, supplementary gates, and statistics.
- [ ] `experiments/phase06_formal.py` - formal main matrix CLI and manifest writer.
- [ ] `experiments/formal_validation.py` - persisted artifact validator.
- [ ] `experiments/phase06_supplementary.py` - supplementary package CLI and gate rows.
- [ ] `experiments/formal_statistics.py` - paired-difference and CI generation.

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Runtime feasibility for optional seeds 21-30 | EXP-05 | Runtime depends on local hardware and observed formal run duration | Inspect `results/formal/phase06/main/formal_run_manifest.json`; attempt optional seeds only after all required 20 seeds pass |
| Critical supplementary conflict interpretation | EXP-05 | Claim impact requires research judgment before Phase 8 | Read `supplementary_gate_results.csv` and document any critical conflict in `06_FORMAL_SYNTHETIC_RESULTS.md` |
| Final table/caption language | EXP-05 | Claims are approved in Phase 8, not by automated tests | Confirm Phase 6 report uses evidence-only language and does not approve final manuscript claims |

## Validation Sign-Off

- [x] All tasks have automated verify commands or Wave 0 dependencies.
- [x] Sampling continuity: no 3 consecutive tasks without automated verify.
- [x] Wave 0 covers all missing references.
- [x] No watch-mode flags.
- [x] Feedback latency is bounded for tests; formal run validation is artifact-based.
- [x] `nyquist_compliant: true` set in frontmatter.

**Approval:** pending execution
