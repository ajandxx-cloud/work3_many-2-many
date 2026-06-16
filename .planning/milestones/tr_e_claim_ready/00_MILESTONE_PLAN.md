# TR-E Claim-Ready Milestone Plan

## Milestone Objective

Turn the current Work 3 DRT experiment repository into a Transportation
Research Part E manuscript package whose claims, tables, figures, and journal
positioning are traceable to formal Phase 6 evidence or explicitly labeled as
diagnostic, exploratory, or limited.

This milestone is claim-led. It does not tune parameters, fabricate numbers,
manually edit evidence, or promote non-canonical outputs into formal claims.

## Canonical Evidence Boundary

Formal manuscript claims must trace to `results/formal/phase06/`.

Canonical formal evidence families:

| Evidence role | Canonical paths | Allowed use | Prohibited use |
|---------------|-----------------|-------------|----------------|
| Primary behavioral evidence | `results/formal/phase06/main_behavioral/raw_results.csv`, `results/formal/phase06/main_behavioral/processed_results.csv`, `results/formal/phase06/main_behavioral/metrics_table.csv`, `results/formal/phase06/tables/main_behavioral_table.csv`, `results/formal/phase06/tables/paired_differences.csv`, `results/formal/phase06/tables/paired_bootstrap_ci.csv` | Main conditional operational-efficiency and coverage-tradeoff claims after Phase 4 provenance checks. | Universal dominance, real-world validation, or final numerical claims before Phase 4. |
| Matched-coverage diagnostic | `results/formal/phase06/coverage_controls/matched_coverage/`, `results/formal/phase06/tables/matched_coverage_paired_differences.csv` | Diagnostic interpretation of coverage confounding. | Primary headline estimate or equal-coverage dominance claim. |
| Fixed-accepted-set diagnostic | `results/formal/phase06/coverage_controls/fixed_accepted_set/`, `results/formal/phase06/tables/fixed_accepted_set_paired_differences.csv` | Diagnostic routing/meeting-point decomposition for fixed accepted sets. | Complete dynamic benchmark claim. |
| Robustness and sensitivity | `results/formal/phase06/robustness/utility_sensitivity/`, `results/formal/phase06/robustness/mp_density_walking_radius/`, `results/formal/phase06/robustness/fleet_demand_stress/` | Conditional robustness, sensitivity, and service-design qualification. | Stronger causal or real-world generalization than the synthetic evidence supports. |
| Equity/type heterogeneity | `results/formal/phase06/robustness/equity_type_outcomes/`, `results/formal/phase06/tables/equity_type_summary.csv` | Limited heterogeneity and passenger-segment monitoring discussion. | Formal equity dominance or real population-distribution claims. |
| Algorithm/MILP diagnostics | `results/formal/phase06/robustness/algorithm_diagnostics/` | Ex-post simplified routing diagnostics and limitations. | ALNS near-optimality proof or complete exact dynamic routing benchmark. |
| Excluded smoke artifacts | `results/formal/phase06/smoke/` | Smoke/package sanity checks only if explicitly labeled non-canonical. | Formal manuscript claims. |

Root legacy CSVs, pilot outputs, archive outputs, and ad hoc logs are
non-canonical by default. They may be cited only as historical or diagnostic
material after an explicit later audit.

## Phase Order And Entry Gates

| Phase | Entry gate | Output gate |
|-------|------------|-------------|
| Phase 1: Evidence Foundation and Milestone Setup | `.planning/phases/01-evidence-foundation-and-milestone-setup/01-CONTEXT.md` exists. | `00_MILESTONE_PLAN.md`, `01_REPO_AND_EVIDENCE_AUDIT.md`, and `04_MANUSCRIPT_ACTION_PLAN.md` exist. |
| Phase 2: TR-E Positioning Lock and Claim Ledger | Phase 1 audit and action plan exist. | `02_TR_E_POSITIONING_LOCK.md`, `03_CLAIM_LEDGER.md`, and `05_BLOCKERS_AND_SAFE_CLAIMS.md` exist; claim ledger contains required provenance columns. |
| Phase 3: TR-E Manuscript Repositioning | Phase 2 positioning, ledger, and blockers/safe-claims table exist. | Manuscript structure and non-numeric TR-E framing are revised without final evidence-dependent numerical injection. |
| Phase 4: Tables, Figures, and Numerical Provenance | Phase 3 manuscript edits are complete and the claim ledger exists. | Tables, figures, and final numerical claims are reconciled against formal Phase 6 paths. |
| Phase 5: Verification and Readiness Closeout | Phase 4 provenance and final numerical injection are complete. | Verification report records validation, tests, manuscript compilation, claim-ledger coverage, table/figure provenance, prohibited wording scan, and readiness classification. |

## Do Not Before Gate Rules

- Do not make major manuscript claim edits before Phase 2 creates the claim
  ledger and blockers/safe-claims table.
- Do not inject final percentages, improvement values, confidence intervals,
  significance language, or table/figure numbers before Phase 4 provenance
  checks.
- Do not use root legacy CSVs, smoke outputs, archive outputs, or ad hoc outputs
  as formal manuscript evidence unless a later phase explicitly audits and
  labels them.
- Do not describe Gamma as endogenous behavior unless future model work
  implements and validates that behavior.
- Do not describe the Beijing scenario as real-world validation unless future
  evidence work implements reproducible public-data ingestion.
- Do not describe the MILP as a full exact dynamic benchmark or ALNS
  near-optimality proof.
- Do not use the `TR-E submission-ready` label before Phase 5 readiness gates
  pass.

## Verification Gates

Phase 1 gates:

- `Test-Path .planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md`
- `Test-Path .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md`
- `Test-Path .planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md`
- `git diff --name-only -- manuscript results src experiments analysis README.md pyproject.toml`
  must print no paths during Phase 1 execution.

Formal-evidence gates for later phases:

- `$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06`
- `$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main_behavioral`
- `$env:PYTHONPATH='src'; python -m experiments.phase06_coverage_controls --validate --package all`
- `$env:PYTHONPATH='src'; python -m experiments.phase06_robustness --validate --package all`

Targeted test gate:

- `$env:PYTHONPATH='src'; pytest tests`

Manuscript compilation gate from `manuscript/`:

- `pdflatex main`
- `bibtex main`
- `pdflatex main`
- `pdflatex main`

Readiness gates:

- formal validation passes or failures are documented as non-impacting
- targeted pytest checks pass or failures are documented as non-impacting
- manuscript compilation passes or failures are documented with submission impact
- numerical claim ledger covers 100% of numerical claims
- all manuscript tables and figures trace to `results/formal/phase06/`
- prohibited wording scans are clean

## Failure Routing

| Failure | Route |
|---------|-------|
| Missing canonical evidence path | Return to Phase 1 audit or Phase 4 provenance, depending on discovery point. |
| Unmapped or unsafe manuscript claim | Return to Phase 2 claim ledger and blockers/safe-claims table. |
| Manuscript prose needs TR-E repositioning without new numbers | Route to Phase 3. |
| Table, figure, denominator, or final number cannot be traced | Route to Phase 4. |
| Validation, targeted tests, manuscript compilation, or prohibited wording scan fails | Route to Phase 5 closeout and classify readiness below submission-ready. |
| Claim-critical formula or code bug is discovered | Pause manuscript claims, fix only the claim-critical issue, rerun targeted validation, and document impact. |

## Risk Classification

| Risk class | Meaning | Phase handling |
|------------|---------|----------------|
| Claim-critical blocker | Can invalidate a manuscript claim if unresolved. | Blocks related claim until downgraded, fixed, or documented. |
| Verification risk | Can block reproducibility or readiness verification. | Track and route to Phase 5 unless it blocks earlier work. |
| Reproducibility hardening | Improves future reproducibility but is not manuscript-critical now. | Defer unless needed for verification. |
| Manuscript/package consistency risk | Creates journal-fit or package-facing inconsistency. | Route to Phase 3 or Phase 5. |
| Claim-impact conditional risk | Matters only if a later claim uses that metric or pathway. | Add guardrail in Phase 2 and verify in Phase 4 if used. |
| Future model/evidence | Requires new model or evidence beyond this milestone. | Defer to v2. |

Known examples:

- bare root `pytest` failure is a verification risk; known green targeted
  command is `$env:PYTHONPATH='src'; pytest tests`
- undeclared `pandas` and `matplotlib` are reproducibility-hardening and
  verification risks
- route-stop bookkeeping is a claim-impact conditional risk for fine-grained
  walk, IVT, detour, fairness, or completed-trip metric claims
- real Beijing ingestion, endogenous Gamma behavior, and a full dynamic exact
  benchmark are future model/evidence items

## Artifact Map

| Artifact | Owner phase | Status |
|----------|-------------|--------|
| `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` | Phase 1 | current file |
| `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md` | Phase 1 | planned |
| `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md` | Phase 2 | reserved |
| `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` | Phase 2 | reserved |
| `.planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md` | Phase 1 | planned |
| `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` | Phase 2 | reserved |
| `.planning/milestones/tr_e_claim_ready/99_MILESTONE_VERIFICATION.md` | Phase 5 | reserved |

## Readiness Label Rules

The final report may say `TR-E submission-ready` only if all Phase 5 hard
readiness gates pass. Otherwise the readiness label must be one of:

- `TR-E near-ready with minor blockers`
- `not ready due to specific blockers`

Failures may be documented as non-impacting only when the report gives exact
commands, outputs, source paths, and manuscript-impact reasoning.

