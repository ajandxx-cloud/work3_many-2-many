---
phase: 01
slug: evidence-foundation-and-milestone-setup
status: complete
created: 2026-06-16
research_mode: inline-codex
---

# Phase 1 Research: Evidence Foundation and Milestone Setup

## Research Question

What does the executor need to know to plan Phase 1 well, without drifting into
claim editing, numerical replacement, experiment reruns, or broad technical debt?

## Scope Finding

Phase 1 is a documentation and planning-foundation phase. It should create
milestone-control artifacts under `.planning/milestones/tr_e_claim_ready/` and
prepare downstream phases to rewrite the manuscript safely. It should not edit
`manuscript/`, `results/`, `src/`, `experiments/`, `analysis/`, `README.md`,
or `pyproject.toml` unless a claim-critical or verification-blocking issue is
discovered and explicitly routed.

The Phase 1 deliverables are:

- `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md`
- `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md`
- `.planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md`

Phase 2 owns the positioning lock, claim ledger, and blockers/safe-claims table.
Phase 3 owns structural manuscript repositioning without final numerical
injection. Phase 4 owns table/figure provenance and final numerical injection.
Phase 5 owns readiness verification and the final readiness label.

## Canonical Evidence Boundary

The canonical formal evidence root is `results/formal/phase06/`.

Primary behavioral evidence:

- `results/formal/phase06/main_behavioral/raw_results.csv`
- `results/formal/phase06/main_behavioral/processed_results.csv`
- `results/formal/phase06/main_behavioral/metrics_table.csv`
- `results/formal/phase06/main_behavioral/validation_report.json`
- `results/formal/phase06/tables/main_behavioral_table.csv`
- `results/formal/phase06/tables/paired_differences.csv`
- `results/formal/phase06/tables/paired_bootstrap_ci.csv`

Diagnostic and supporting evidence:

- `results/formal/phase06/coverage_controls/matched_coverage/`
- `results/formal/phase06/coverage_controls/fixed_accepted_set/`
- `results/formal/phase06/robustness/utility_sensitivity/`
- `results/formal/phase06/robustness/mp_density_walking_radius/`
- `results/formal/phase06/robustness/fleet_demand_stress/`
- `results/formal/phase06/robustness/equity_type_outcomes/`
- `results/formal/phase06/robustness/algorithm_diagnostics/`
- `results/formal/phase06/tables/equity_type_summary.csv`
- `results/formal/phase06/tables/matched_coverage_paired_differences.csv`
- `results/formal/phase06/tables/fixed_accepted_set_paired_differences.csv`
- `results/formal/phase06/tables/final_synthesis_validation.json`

Excluded or non-canonical by default:

- `results/formal/phase06/smoke/`
- root legacy CSV/JSON/Markdown outputs under `results/`
- `results/pilot/phase05/`
- `archive/`
- ad hoc logs and smoke outputs

The top-level result manifest reports `formal_smoke_excluded: true`, and the
Phase 6 verification report shows the main matrix, coverage controls,
robustness packages, denominator checks, failure ledger, and raw-to-processed
provenance passed. The audit should record these statuses and paths, not rerun
formal experiments.

## Manuscript and Wording Risk Surface

The canonical manuscript source is:

- `manuscript/main.tex`
- `manuscript/sections/abstract.tex`
- `manuscript/sections/intro.tex`
- `manuscript/sections/literature.tex`
- `manuscript/sections/model.tex`
- `manuscript/sections/algorithm.tex`
- `manuscript/sections/experiments.tex`
- `manuscript/sections/policy.tex`
- `manuscript/sections/conclusion.tex`
- `manuscript/references.bib`

Current scans show Part A framing and old or sensitive values in the manuscript
and package docs, including:

- `Transportation Research Part A`
- policy-first and public-policy wording
- old numeric claims such as `18.3%`, `29.1%`, `35.0%`, and `0.1216`
- Beijing wording that could imply real-world validation
- MILP/ALNS language that could imply exact dynamic benchmarking or
  near-optimality
- Gamma/Pareto language that could imply endogenous behavior

Phase 1 should track these as risk families only. It must not replace numbers,
rewrite claims, or draft final replacement prose.

## Repository Risk Inputs

`.planning/codebase/CONCERNS.md` identifies risks that should be preserved in
the audit:

- bare root `pytest` collects archived ad hoc tests and fails; known green
  command is `$env:PYTHONPATH='src'; pytest tests`
- `pandas` and `matplotlib` are used but not declared in `pyproject.toml`
- route-stop bookkeeping can affect completed-trip walk/IVT/fairness metrics
- Gamma is currently post-hoc, not an endogenous routing or choice control
- Beijing is synthetic or Beijing-inspired, not a real public-data case study
- MILP is a static simplified diagnostic, not a full exact dynamic benchmark

Phase 1 should classify these by manuscript impact, not expand them into code
fixes. Route-stop precision becomes claim-critical only if later phases use
fine-grained walk, IVT, detour, or fairness metrics as formal headline claims.

## Planning Pattern

The most robust Phase 1 plan structure is sequential:

1. Create the milestone folder and hard-gate milestone plan.
2. Write the canonical-first repository and evidence audit.
3. Write the manuscript action plan and handoff sections.

The audit should come before the action plan because the action plan needs the
evidence-role and risk taxonomy. The milestone plan can be created first
because it defines the phase gates and prevents later phases from skipping the
claim ledger and provenance checks.

## Validation Architecture

Phase 1 validation should be artifact- and boundary-based:

- File-existence checks for the milestone folder and required Markdown files.
- Source assertions for required headings and evidence-role sections.
- Path assertions that formal claims point to `results/formal/phase06/`.
- Boundary assertions that Phase 1 did not modify manuscript/source/result
  files.
- Prohibited-readiness assertions that no Phase 1 document calls the package
  `TR-E submission-ready`.
- Handoff assertions that Phase 2 receives the expected inputs:
  `01_REPO_AND_EVIDENCE_AUDIT.md`, `04_MANUSCRIPT_ACTION_PLAN.md`, and the
  Phase 1 plan summaries.

Useful verification commands for Phase 1 execution include:

- `Test-Path .planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md`
- `Test-Path .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md`
- `Test-Path .planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md`
- `rg -n "results/formal/phase06|formal_smoke_excluded|Evidence Role|Allowed use|Prohibited use" .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md`
- `rg -n "Phase 4|defer until Phase 4|manuscript/sections|prohibited wording" .planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md`
- `git diff --name-only -- manuscript results src experiments analysis README.md pyproject.toml`

Formal statistics validation and manuscript compilation should be referenced as
later milestone gates. Phase 1 may record existing validation report status but
should not rerun full formal experiments by default.

## Research Complete

Phase 1 can be planned as three executable documentation plans. Each plan should
include concrete read-first files, exact output paths, source assertions, and a
security/threat-model note that no secrets or local solver/license details are
to be copied into planning artifacts.

