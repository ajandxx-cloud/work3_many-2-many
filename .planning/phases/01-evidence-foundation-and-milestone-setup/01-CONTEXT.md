# Phase 1: Evidence Foundation and Milestone Setup - Context

**Gathered:** 2026-06-16T22:33:13+08:00
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 1 establishes the milestone workspace and evidence foundation before any claim edits. It creates the milestone scaffold under `.planning/milestones/tr_e_claim_ready/`, writes a gate-driven milestone plan, audits canonical manuscript and evidence sources, and prepares a manuscript action plan for later phases. It does not revise manuscript claims, change numerical values, rerun formal experiments by default, or fix ordinary technical debt unless a claim-critical or verification-blocking issue is discovered.

</domain>

<decisions>
## Implementation Decisions

### Audit Strictness
- **D-01:** `01_REPO_AND_EVIDENCE_AUDIT.md` should use a canonical-first structure with a risk appendix. The main body should lock canonical manuscript and evidence paths; the appendix should capture non-canonical sources and misuse risks.
- **D-02:** `results/formal/phase06/` must be classified by evidence role: primary behavioral evidence, matched-coverage diagnostics, fixed-accepted-set diagnostics, robustness/sensitivity evidence, equity/type heterogeneity evidence, algorithm/MILP diagnostics, and excluded smoke artifacts.
- **D-03:** Root legacy CSVs, smoke outputs, archive outputs, and ad hoc outputs are prohibited for formal manuscript claims by default. They may be used only after explicit later audit and only when labeled historical or diagnostic.
- **D-04:** Known old values and wording risks, including `18.3%`, `29.1%`, `35.0%`, `0.1216`, Part A framing, real-world Beijing wording, universal dominance language, endogenous Gamma language, and exact-benchmark MILP language, should be listed as high-priority tracking items. Phase 1 must not correct manuscript claims or inject replacement numbers.
- **D-05:** The audit should include an allowed/prohibited use table by evidence role.
- **D-06:** Evidence references must use complete relative paths so Phase 2 claim ledger and Phase 4 provenance work can reuse them directly.
- **D-07:** Phase 1 should record existing Phase 6 validation report status and source paths, but should not rerun formal validation by default.
- **D-08:** The audit should include an out-of-scope/deferred section for future items such as real Beijing public-data ingestion, endogenous Gamma behavior, and a full dynamic exact benchmark.

### Milestone Plan Contract
- **D-09:** `00_MILESTONE_PLAN.md` should be a hard-gate plan with phase entry and exit gates, not a loose overview.
- **D-10:** Key gates must include failure routing. Failures should block `TR-E submission-ready` claims unless documented as non-impacting, and may route work back to the relevant phase.
- **D-11:** The milestone plan must include "Do not before gate" rules, including no major manuscript claim edits before the Phase 2 claim ledger, no final numerical injection before Phase 4 provenance checks, and no submission-ready label before Phase 5 readiness gates.
- **D-12:** Verification gates should include command-level placeholders plus success criteria, not exact final commands. Expected gate categories include formal statistics validation, targeted pytest checks, LaTeX compilation, claim ledger coverage, table/figure provenance, and prohibited wording scans.

### Manuscript Action Plan Granularity
- **D-13:** `04_MANUSCRIPT_ACTION_PLAN.md` should use a dual-axis structure: manuscript section/file area plus evidence role.
- **D-14:** The action plan should list concrete manuscript paths and region-level tasks, such as `manuscript/main.tex` metadata, `manuscript/sections/abstract.tex`, `manuscript/sections/intro.tex`, `manuscript/sections/literature.tex`, `manuscript/sections/experiments.tex`, `manuscript/sections/policy.tex`, and `manuscript/sections/conclusion.tex`. It should not draft final replacement prose in Phase 1.
- **D-15:** The action plan must mark final percentages, uplift values, confidence intervals, significance wording, and table/figure numbers as "defer until Phase 4" wherever final provenance is required.
- **D-16:** The action plan should list wording families for later scans and replacement: Transportation Research Part A, policy-first framing, real-world Beijing validation, universal dominance, exact dynamic benchmark or ALNS near-optimality claims, and endogenous Gamma/Pareto language.

### Risk And Blocker Posture
- **D-17:** Known risks should be classified by manuscript impact: claim-critical blocker, verification risk, reproducibility hardening, manuscript/package consistency risk, claim-impact conditional risk, or future model/evidence.
- **D-18:** Direct code fixes are in scope only for claim-critical or verification-blocking issues. Ordinary technical debt should be recorded but not expanded into this milestone.
- **D-19:** Bare root `pytest` failure is a verification risk and reproducibility-hardening item, not a Phase 1 blocker. The audit should record the known green targeted command: `$env:PYTHONPATH='src'; pytest tests`.
- **D-20:** Undeclared `pandas` and `matplotlib` dependencies are verification/reproducibility risks. Phase 1 should document affected workflows and defer metadata edits unless the issue blocks verification.
- **D-21:** Gamma, Beijing, and MILP semantics are claim-critical wording risks. They do not automatically trigger code fixes, but they must constrain manuscript wording, claim ledger entries, allowed sentences, and prohibited sentences.
- **D-22:** Route-stop bookkeeping and completed-trip metric precision are claim-impact conditional risks. If Phase 2 or Phase 4 uses walking, in-vehicle time, detour, fairness, or similarly fine-grained metrics as formal claims, those claims must be verified, downgraded, or explicitly limited.
- **D-23:** README old known issues and Part A framing are manuscript/package consistency risks for Phase 3, not Phase 1 blockers.
- **D-24:** Phase 1 should reserve the Phase 2 interface for `05_BLOCKERS_AND_SAFE_CLAIMS.md`, but should not create a premature safe-claims table. Phase 2 should build that file from the audit, positioning lock, claim ledger, and wording scans.

### Agent Discretion
- No user decisions were delegated to agent discretion. Downstream agents should follow the decisions above.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Planning Source Of Truth
- `.planning/PROJECT.md` - Project framing, evidence boundaries, constraints, and key decisions.
- `.planning/REQUIREMENTS.md` - Requirement-to-phase mapping and out-of-scope boundaries.
- `.planning/ROADMAP.md` - Phase 1 goal, plans, success criteria, and dependency order.
- `.planning/STATE.md` - Current workflow state and accumulated decisions.

### Codebase Maps And Risks
- `.planning/codebase/CONVENTIONS.md` - Repository naming, style, import, logging, and test conventions.
- `.planning/codebase/STRUCTURE.md` - Canonical locations for source, experiments, results, manuscript, archive, and planning artifacts.
- `.planning/codebase/CONCERNS.md` - Known risks that must feed the Phase 1 audit and blocker posture.

### Manuscript Sources
- `manuscript/main.tex` - Master manuscript source and journal metadata.
- `manuscript/sections/abstract.tex` - Abstract rewrite target; final numbers deferred until Phase 4.
- `manuscript/sections/intro.tex` - Introduction and contribution framing target; final numbers deferred until Phase 4.
- `manuscript/sections/literature.tex` - TR-E logistics/operations literature positioning target.
- `manuscript/sections/model.tex` - Offer, choice, Gamma, and modeling semantics target.
- `manuscript/sections/algorithm.tex` - Rolling-horizon and algorithm scope target.
- `manuscript/sections/experiments.tex` - Evidence-role separation and denominator narrative target.
- `manuscript/sections/policy.tex` - Managerial/operational implications target.
- `manuscript/sections/conclusion.tex` - Conditional contribution, limitation, and future work target.
- `manuscript/references.bib` - Bibliography source.

### Formal Phase 6 Evidence
- `results/formal/phase06/phase06_result_manifest.json` - Formal result manifest and evidence package inventory.
- `results/formal/phase06/phase06_verification_report.json` - Formal Phase 6 verification summary.
- `results/formal/phase06/main_behavioral/raw_results.csv` - Main behavioral raw results.
- `results/formal/phase06/main_behavioral/processed_results.csv` - Main behavioral processed results.
- `results/formal/phase06/main_behavioral/metrics_table.csv` - Main behavioral aggregate metrics.
- `results/formal/phase06/main_behavioral/validation_report.json` - Main behavioral validator report.
- `results/formal/phase06/tables/main_behavioral_table.csv` - Manuscript-facing main behavioral table source.
- `results/formal/phase06/tables/paired_differences.csv` - Paired comparison table source.
- `results/formal/phase06/tables/paired_bootstrap_ci.csv` - Bootstrap interval table source.
- `results/formal/phase06/tables/equity_type_summary.csv` - Equity/type heterogeneity table source.
- `results/formal/phase06/tables/matched_coverage_paired_differences.csv` - Matched-coverage diagnostic table source.
- `results/formal/phase06/tables/fixed_accepted_set_paired_differences.csv` - Fixed-accepted-set diagnostic table source.
- `results/formal/phase06/tables/final_synthesis_validation.json` - Final synthesis validation source.
- `results/formal/phase06/coverage_controls/matched_coverage/validation_report.json` - Matched-coverage diagnostic validation.
- `results/formal/phase06/coverage_controls/fixed_accepted_set/validation_report.json` - Fixed-accepted-set diagnostic validation.
- `results/formal/phase06/robustness/validation_report.json` - Robustness package validation summary.
- `results/formal/phase06/robustness/equity_type_outcomes/validation_report.json` - Equity/type outcome validation.
- `results/formal/phase06/robustness/algorithm_diagnostics/validation_report.json` - Algorithm diagnostic validation.
- `results/formal/phase06/smoke/validation_report.json` - Smoke package report; explicitly non-canonical for formal manuscript claims unless later audited and labeled.

### Generation And Validation Scripts
- `experiments/phase06_formal.py` - Formal main package runner and manifest logic.
- `experiments/formal_validation.py` - Formal validation helpers.
- `experiments/formal_statistics.py` - Formal statistics, tables, plots, manifests, and synthesis outputs.
- `experiments/phase06_coverage_controls.py` - Matched-coverage and fixed-accepted-set diagnostic controls.
- `experiments/phase06_robustness.py` - Robustness, equity, and algorithm diagnostics.
- `manuscript/figures/scripts/fig04_baseline_comparison.py` - Figure generation script tied to baseline comparison.
- `manuscript/figures/scripts/fig05_sensitivity.py` - Figure generation script tied to sensitivity evidence.
- `manuscript/figures/scripts/fig06_policy_map.py` - Figure generation script tied to implication/decision-map material.
- `manuscript/figures/scripts/fig07_pareto.py` - Figure generation script tied to post-hoc Pareto/Gamma material.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `experiments/formal_statistics.py`: Existing source for formal tables, plots, manifests, validation markdown, and synthesis artifacts. Phase 1 should audit what it produces and how later phases should consume it.
- `experiments/formal_validation.py`, `experiments/phase06_formal.py`, `experiments/phase06_coverage_controls.py`, and `experiments/phase06_robustness.py`: Existing validators and package runners that define evidence roles and validation reports.
- `manuscript/figures/scripts/`: Existing figure-generation scripts. Phase 1 should record them as provenance targets; Phase 4 should verify formal Phase 6 inputs before relying on their outputs.
- `.planning/codebase/CONCERNS.md`: Existing risk inventory that should seed the Phase 1 audit and blocker taxonomy.

### Established Patterns
- Planning artifacts live under `.planning/`; milestone artifacts for this work should live under `.planning/milestones/tr_e_claim_ready/`.
- Generated evidence stays under `results/`, with formal Phase 6 evidence under `results/formal/phase06/`.
- Active manuscript source is `manuscript/main.tex` plus `manuscript/sections/*.tex`; archive and old paper paths are historical unless explicitly audited.
- Experiment and validation outputs use CSV/JSON manifests and validation reports. Phase 1 should preserve path-level provenance instead of manually transcribing numbers.

### Integration Points
- Phase 1 outputs should feed Phase 2 positioning lock, claim ledger, and blockers/safe-claims file.
- Phase 1 manuscript action plan should feed Phase 3 rewrite tasks while preserving the Phase 4 numerical-provenance gate.
- Phase 1 audit should feed Phase 4 table/figure provenance checks and Phase 5 readiness verification.

</code_context>

<specifics>
## Specific Ideas

- Use canonical-first audit structure with a risk appendix.
- Use evidence-role categories, not directory-only categories, for `results/formal/phase06/`.
- Include allowed/prohibited evidence-use rules directly in Phase 1 audit.
- Preserve full relative paths for all evidence and manuscript references.
- Track known old values and old wording risks without changing manuscript text in Phase 1.

</specifics>

<deferred>
## Deferred Ideas

- Real Beijing public-data ingestion and empirical validation belong to future evidence work, not this milestone.
- Endogenous Gamma behavior belongs to future model work unless a later scoped milestone implements and validates it.
- A full dynamic exact benchmark belongs to future model/evidence work. Current MILP language stays simplified ex-post diagnostic.
- Broad import cleanup, root pytest hardening, dependency metadata cleanup, route-stop refactoring, and dependency locking are not Phase 1 work unless they become claim-critical or verification-blocking.

</deferred>

---

*Phase: 1-Evidence Foundation and Milestone Setup*
*Context gathered: 2026-06-16T22:33:13+08:00*
