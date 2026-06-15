---
status: passed
phase: 00-repository-and-manuscript-audit
verified: 2026-06-15
requirements: [AUD-01, AUD-02, AUD-03]
---

# Phase 0 Verification: Repository and Manuscript Audit

## Result

**Passed with caveats.**

Phase 0 achieved its audit goal: current code modules, manuscript claims, result files, and experiment provenance are mapped well enough to guide Phase 1 and Phase 2. This verification does not certify current manuscript numbers as final evidence.

## Must-Have Checks

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Every current manuscript result is mapped to a script/data artifact or marked not reproducible | Passed | `00_CURRENT_EXPERIMENT_MAP.md` includes row-level provenance for main table, matched coverage, Beijing, sensitivity, equity, gamma, weight sensitivity, MILP, and figures |
| Every headline manuscript claim is classified by evidence strength | Passed | `00_MANUSCRIPT_CLAIM_AUDIT.md` includes headline and section-level claim classifications |
| Existing code modules, experiment scripts, result files, and manuscript sections are indexed | Passed | `00_REPOSITORY_AUDIT.md` records core code, experiment scripts, result artifacts, manuscript files, and phase-routed blockers |
| Review-note weaknesses are captured as risks and gates | Passed | `00_REPOSITORY_AUDIT.md`, `00_MANUSCRIPT_CLAIM_AUDIT.md`, and `STATE.md` route novelty, coverage, calibration, ALNS/MILP, synthetic policy, and reproducibility risks |
| No new experiments were run | Passed | Only file reads, text search, and result summarization were used; no experiment-generation commands were executed |

## Residual Risks

- Main table values are reproducible from `results/metrics_table.csv`, but that CSV aggregates all synthetic scales despite manuscript wording that implies a 200-request baseline scenario.
- FullModel and DoorToDoor served shares differ sharply, so the current efficiency headline remains coverage-confounded.
- Matched-coverage evidence is exploratory and split across post-hoc and endogenous diagnostic scripts.
- Gamma/welfare sweep is post-hoc accounting, not a Pareto frontier.
- Weight sensitivity provenance remains ambiguous relative to `results/weight_sensitivity.json`.
- Policy artifacts remain synthetic and partly illustrative.

## Next Gate

Proceed to Phase 1: Literature and Novelty Audit. Do not preserve strong novelty language until prior bidirectional meeting-point, DARPmp, ridepooling, and choice-based DRT work is audited.

After Phase 1, proceed to Phase 2 before running new formal experiments so metric denominators, baseline taxonomy, and coverage-control designs are fixed first.
