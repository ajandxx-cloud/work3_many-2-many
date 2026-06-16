# Phase 10 Reproducibility Guide

**Status:** Blocked: prerequisites missing
**Structured source:** `10_RESULT_MANIFEST.md`

## Reproduction Status

Phase 10 is `Blocked: prerequisites missing` until the formal Phase 6 evidence report and the Phase 8 claim-gate artifacts exist. This guide is still created as a blocked/pending artifact so reviewers, coauthors, and future agents can see exactly what is reproducible now and what must wait.

Current blocker summary:

- Phase 6 formal synthetic evidence report is missing.
- Phase 8 claim-evidence matrix is missing.
- Phase 8 supported-claims list is missing.
- Phase 8 unsupported/exploratory-claims list is missing.

## Environment Setup

Run these commands from the repository root unless a later row says otherwise.

| purpose | command | notes |
|---|---|---|
| Editable install | `python -m pip install -e .` | Installs the local `drt` package declared in `pyproject.toml`. |
| Dependency snapshot | `python -m pip freeze` | Save the output with the final package; `pandas` and `matplotlib` may be present even though core metadata lists only `gurobipy` and `numpy`. |
| Code revision | `git rev-parse HEAD` | Capture after final Phase 10 commits and after any repository-maintenance commit. |
| Working-tree state | `git status --short` | Required because current version-control state is heavily drifted. |
| Active test suite | `$env:PYTHONPATH='src'; pytest tests -q` | PowerShell command for the active test suite; bare `pytest` may collect archived ad hoc tests. |

## Command Taxonomy

Command groups:

- `final evidence`: Phase 6 formal main evidence and Phase 8-supported final tables/figures.
- `critical robustness`: matched-coverage, fixed accepted-set, sensitivity, and equity checks that can qualify claims only after Phase 8.
- `supplementary diagnostic`: MILP, ALNS, gamma, weight, and other mechanism diagnostics.
- `legacy diagnostic`: current root result regeneration or historical outputs that are provenance only.
- `pilot readiness`: Phase 5 pilot artifacts and smoke checks; not final evidence.
- `manuscript figures`: figure-generation scripts and generated figure files.
- `manuscript build`: LaTeX build inputs and compiled PDF outputs.

## Prerequisite Blockers

The hard blockers are defined in `10_RESULT_MANIFEST.md` under `Prerequisite Gate`. They are repeated here for reviewer-facing clarity:

| prerequisite | status |
|---|---|
| `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md` | Blocked: prerequisites missing |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_CLAIM_EVIDENCE_MATRIX.md` | Blocked: prerequisites missing |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_SUPPORTED_CLAIMS.md` | Blocked: prerequisites missing |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` | Blocked: prerequisites missing |
