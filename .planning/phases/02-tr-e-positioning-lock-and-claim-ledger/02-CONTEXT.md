# Phase 2: TR-E Positioning Lock and Claim Ledger - Context

**Gathered:** 2026-06-17T16:19:34.8091735+08:00
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 2 defines the safe TR-E framing and claim-control artifacts that must exist before manuscript prose is edited. It creates `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md`, `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md`, and `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md`.

This phase does not rewrite manuscript prose, inject final numerical values, refresh tables or figures, rerun formal experiments, or fix broad code/reproducibility issues. It locks how downstream phases classify evidence, map manuscript claims to provenance, and avoid unsafe TR Part A, dominance, real-world validation, Gamma, Beijing, MILP, and diagnostic-overreach wording.

</domain>

<decisions>
## Implementation Decisions

### Claim Ledger Granularity And Coverage
- **D-01:** `03_CLAIM_LEDGER.md` must use one row per manuscript claim occurrence. Each claim occurrence gets its own row even when multiple rows share the same underlying idea or evidence source.
- **D-02:** Ledger rows must include `claim_family_id` so related occurrences can be grouped without losing per-location traceability.
- **D-03:** The ledger must cover both current manuscript claims and planned safe replacement claims. It is not only an audit list; it is the executable handoff for Phase 3 manuscript revision and Phase 4 numerical provenance.
- **D-04:** Planned replacement claims in Phase 2 must use non-numeric safe wording. Final percentages, improvement values, confidence intervals, significance language, table numbers, and figure numbers must use Phase 4 placeholders such as `[PHASE4_VERIFIED_VALUE]` until provenance is verified.
- **D-05:** In addition to the mandatory provenance schema, ledger rows should include execution fields: `claim_id`, `claim_family_id`, `manuscript_location`, `current_sentence`, `claim_type`, `comparison`, `metric`, `reported_value`, `phase4_status`, and `action`.
- **D-06:** The mandatory provenance columns remain required for every applicable ledger row: `source_path`, `script_path`, `generation_command`, `metric_formula`, `numerator`, `denominator`, `evidence_role`, `allowed_sentence`, and `prohibited_sentence`.
- **D-07:** Recommended `action` values for the planner to consider are `retain_with_verification`, `replace_non_numeric`, `delete`, `downgrade_to_diagnostic`, `move_to_limitation`, and `phase4_verify_number`. The exact enum may be refined by the planner, but it must preserve these semantics.

### TR-E Positioning Lock Core Narrative
- **D-08:** `02_TR_E_POSITIONING_LOCK.md` should anchor the paper as operational service-design evidence for TR-E. The primary contribution is not a policy validation, a deployable decision tool, or a stronger optimization-method claim.
- **D-09:** The strongest allowed title/abstract/introduction mechanism wording is `passenger-response-aware simulation framework`.
- **D-10:** Prohibit `co-optimization of meeting points, routing, and passenger response` and similar wording that implies endogenous passenger-response-aware routing. The current mechanism is route-then-sample acceptance, not optimization over acceptance probability.
- **D-11:** Journal-fit rationale should be anchored in DRT/DARP operations, meeting-point service consolidation, dynamic routing, fleet operations, and logistics/operations management.
- **D-12:** Passenger choice should be framed as a service-design evaluation mechanism. It must not be presented as empirically calibrated behavioral validation or as a behaviorally endogenous routing-control mechanism.
- **D-13:** Policy and public-service material may appear only as bounded implications or limitations. It must not be the main journal-fit rationale.
- **D-14:** The core allowed sentence should be conservative but contribution-bearing: the study may say that passenger-response-aware bidirectional meeting-point consolidation can reduce routing intensity per served trip under tested synthetic service-design conditions, while creating measurable coverage and passenger-type trade-offs.

### Evidence Role And Blocker Classification
- **D-15:** `05_BLOCKERS_AND_SAFE_CLAIMS.md` must use four claim statuses: `safe`, `safe_with_qualifier`, `downgrade_required`, and `blocker`.
- **D-16:** Known old or risky values, including `18.3%`, `29.1%`, `35.0%`, and `0.1216`, are `blocker until Phase 4 verified`. Phase 3 may not retain them or replace them with final values.
- **D-17:** Diagnostic evidence may appear in the main text only when each relevant claim has an explicit diagnostic qualifier. Diagnostic evidence must not become the headline estimate.
- **D-18:** Matched-coverage evidence must be labeled as a diagnostic coverage-confounding control, not a primary equal-service headline claim.
- **D-19:** Fixed-accepted-set evidence must be labeled as a diagnostic decomposition over fixed accepted sets, not a full dynamic benchmark.
- **D-20:** MILP and algorithm diagnostics must be labeled as simplified ex-post diagnostics and limitations, not ALNS near-optimality proof.
- **D-21:** Gamma/Pareto material must be labeled as post-hoc welfare or sensitivity accounting, not behavioral policy control.
- **D-22:** Fine-grained passenger-burden claims involving walking, IVT, detour, fairness, type burden, or completed-trip precision should be `safe_with_qualifier` or `blocker` unless Phase 4 verifies them. Main metrics such as routing intensity, served share, and vkm per original request can be formal ledger claims with provenance and Phase 4 numerical verification.

### Prohibited Wording And Replacement Rules
- **D-23:** Policy-first framing is prohibited as the main narrative. The manuscript section currently named `Policy Implications` should be reframed in Phase 3 as managerial or operational implications.
- **D-24:** Bounded public-service or service-design implications are allowed when they are clearly limited by the evidence.
- **D-25:** Generic dominance, superiority, and broad `outperforms` wording is prohibited. Metric-specific and evidence-bounded comparisons are allowed, such as lower vkm per served trip under tested settings, while noting lower served share or other trade-offs.
- **D-26:** Behavioral Pareto and endogenous Gamma wording is prohibited. Gamma may be described only as post-hoc welfare or sensitivity accounting, not as a routing, offer-generation, acceptance, or policy-control mechanism.
- **D-27:** `Pareto frontier` should be avoided when it implies behaviorally endogenous optimization or policy control. If retained at all, it must be reframed as a post-hoc welfare or sensitivity display.
- **D-28:** Beijing wording must use a qualifier such as `Beijing-inspired synthetic grid` or `semi-realistic synthetic grid`. Real-world Beijing validation, empirical Beijing case-study, or public-data validation wording is prohibited.
- **D-29:** MILP wording must use a qualifier such as `simplified ex-post diagnostic over fixed accepted sets`. Exact dynamic benchmark, complete benchmark, and ALNS near-optimality proof wording is prohibited.

### Artifact Responsibilities
- **D-30:** `02_TR_E_POSITIONING_LOCK.md` should state allowed framing, prohibited framing, core contribution, journal-fit rationale, and safe core sentences.
- **D-31:** `03_CLAIM_LEDGER.md` should be the occurrence-level claim table with mandatory provenance fields and execution fields. It should map current claims to planned safe replacements without final numerical injection.
- **D-32:** `05_BLOCKERS_AND_SAFE_CLAIMS.md` should classify safe claims, safe-with-qualifier claims, downgrade-required claims, blockers, old numbers, prohibited wording, and diagnostic evidence boundaries.
- **D-33:** Phase 2 may scan manuscript and package-facing text to build the ledger and blocker table, but it must not edit `manuscript/`, `README.md`, `CLAUDE.md`, result files, or code.

### Agent Discretion
- No user decisions were delegated to agent discretion. Downstream agents should follow the decisions above.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Planning Source Of Truth
- `.planning/PROJECT.md` - Project goal, evidence boundary, TR-E target, constraints, and key decisions.
- `.planning/REQUIREMENTS.md` - Phase 2 requirements: PLAN-04 and CLAI-01 through CLAI-04.
- `.planning/ROADMAP.md` - Phase 2 goal, success criteria, and plan list.
- `.planning/STATE.md` - Current workflow state and accumulated decisions.
- `.planning/phases/01-evidence-foundation-and-milestone-setup/01-CONTEXT.md` - Prior phase decisions and canonical reference inventory.

### Milestone Inputs
- `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` - Evidence boundary, do-not-before-gate rules, verification gates, and readiness rules.
- `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md` - Canonical manuscript/evidence audit, validation snapshot, risk appendix, and non-canonical source rules.
- `.planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md` - Manuscript file actions, evidence-role boundaries, wording scan families, and Phase 2 handoff.

### Codebase Maps And Risks
- `.planning/codebase/STRUCTURE.md` - Repository locations for manuscript, results, source, experiments, archive, and planning artifacts.
- `.planning/codebase/CONCERNS.md` - Known risks around pytest, dependency metadata, route-stop bookkeeping, Gamma semantics, Beijing wording, and MILP diagnostic scope.

### Manuscript And Package Sources To Scan
- `README.md` - Package-facing journal target and old Part A framing.
- `CLAUDE.md` - Existing project-facing Part A and policy framing.
- `manuscript/main.tex` - Master manuscript source, journal metadata, notation, and section includes.
- `manuscript/sections/abstract.tex` - Abstract claims and headline numerical-risk region.
- `manuscript/sections/intro.tex` - Introduction, contribution list, old values, and contribution framing.
- `manuscript/sections/literature.tex` - DRT/DARP, passenger choice, dynamic DRT, and operations positioning.
- `manuscript/sections/model.tex` - Offer, binary-logit response, Gamma, and model-scope language.
- `manuscript/sections/algorithm.tex` - Rolling-horizon, ALNS, and MILP scope language.
- `manuscript/sections/experiments.tex` - Main results, diagnostics, robustness, Gamma/Pareto, denominators, and old numerical claims.
- `manuscript/sections/policy.tex` - Policy-first language, managerial/operational implications target, old numerical claims, and equity/type wording.
- `manuscript/sections/conclusion.tex` - Conditional contribution, limitation, and headline claim wording.
- `manuscript/references.bib` - Bibliography target and journal-fit references.
- `manuscript/cover_letter.tex` - Package-consistency scan target if the submission package includes it.
- `manuscript/response_to_reviewers.tex` - Package-consistency scan target if the submission package includes it.

### Formal Phase 6 Evidence
- `results/formal/phase06/phase06_result_manifest.json` - Formal result manifest and smoke-exclusion status.
- `results/formal/phase06/phase06_verification_report.json` - Top-level formal verification status.
- `results/formal/phase06/main_behavioral/raw_results.csv` - Main behavioral raw results.
- `results/formal/phase06/main_behavioral/processed_results.csv` - Main behavioral processed results.
- `results/formal/phase06/main_behavioral/metrics_table.csv` - Main behavioral aggregate metrics.
- `results/formal/phase06/main_behavioral/validation_report.json` - Main behavioral validator report.
- `results/formal/phase06/tables/main_behavioral_table.csv` - Manuscript-facing main behavioral table source.
- `results/formal/phase06/tables/paired_differences.csv` - Paired-difference source for Phase 4 verification.
- `results/formal/phase06/tables/paired_bootstrap_ci.csv` - Bootstrap interval source for Phase 4 verification.
- `results/formal/phase06/tables/equity_type_summary.csv` - Equity/type heterogeneity source; limited monitoring evidence unless verified for stronger claims.
- `results/formal/phase06/tables/matched_coverage_paired_differences.csv` - Matched-coverage diagnostic source.
- `results/formal/phase06/tables/fixed_accepted_set_paired_differences.csv` - Fixed-accepted-set diagnostic source.
- `results/formal/phase06/tables/robustness_setting_summary.csv` - Robustness/sensitivity source.
- `results/formal/phase06/tables/supplementary_summary.csv` - Supplementary summary source.
- `results/formal/phase06/tables/critical_conflicts.csv` - Conflict ledger source, if populated by formal-statistics workflows.
- `results/formal/phase06/tables/final_synthesis_validation.json` - Final synthesis validation status.
- `results/formal/phase06/coverage_controls/matched_coverage/validation_report.json` - Matched-coverage diagnostic validation.
- `results/formal/phase06/coverage_controls/fixed_accepted_set/validation_report.json` - Fixed-accepted-set diagnostic validation.
- `results/formal/phase06/robustness/validation_report.json` - Robustness package validation summary.
- `results/formal/phase06/robustness/equity_type_outcomes/validation_report.json` - Equity/type outcome validation.
- `results/formal/phase06/robustness/algorithm_diagnostics/validation_report.json` - Algorithm diagnostic validation.

### Generation And Validation Scripts
- `experiments/phase06_formal.py` - Formal main behavioral runner, manifest, and validation entry point.
- `experiments/formal_validation.py` - Main formal output validation helpers and denominator checks.
- `experiments/formal_statistics.py` - Formal tables, plots, manifests, verification reports, and synthesis validation.
- `experiments/phase06_coverage_controls.py` - Matched-coverage and fixed-accepted-set diagnostic controls.
- `experiments/phase06_robustness.py` - Utility, density/radius, fleet stress, equity/type, and algorithm diagnostics.
- `manuscript/figures/scripts/fig04_baseline_comparison.py` - Baseline comparison figure script; old annotation comments must be ledger-scanned.
- `manuscript/figures/scripts/fig05_sensitivity.py` - Sensitivity figure script.
- `manuscript/figures/scripts/fig06_policy_map.py` - Policy-map figure script; Phase 3 should reframe policy language.
- `manuscript/figures/scripts/fig07_pareto.py` - Pareto/Gamma figure script; Phase 4 must label output as post-hoc welfare/sensitivity if retained.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `experiments/formal_statistics.py`: Existing source for formal tables, plots, manifests, validation markdown, and synthesis artifacts. Phase 2 should cite it as the generation script for table/figure-derived claims where applicable, while final numerical verification remains Phase 4 work.
- `experiments/formal_validation.py`, `experiments/phase06_formal.py`, `experiments/phase06_coverage_controls.py`, and `experiments/phase06_robustness.py`: Existing validators and package runners that define evidence roles and validation reports.
- `results/formal/phase06/tables/*.csv`: Existing formal table sources that the ledger can reference by source path. Phase 2 should not manually edit or reinterpret their numbers beyond assigning evidence roles and Phase 4 verification status.
- `rg` scans over `manuscript/`, `README.md`, `CLAUDE.md`, and figure scripts can identify old values, Part A wording, policy-first language, dominance wording, Gamma/Pareto language, Beijing wording, and MILP wording.

### Established Patterns
- Planning artifacts for this milestone live under `.planning/milestones/tr_e_claim_ready/`.
- GSD phase context and discussion artifacts live under `.planning/phases/02-tr-e-positioning-lock-and-claim-ledger/`.
- Formal manuscript claims must trace to `results/formal/phase06/`; root legacy results, smoke, archive, and ad hoc outputs are non-canonical by default.
- Active manuscript source is `manuscript/main.tex` plus `manuscript/sections/*.tex`; archive and old paper paths are historical unless explicitly audited.
- Phase 2 should preserve path-level provenance and avoid transcribing unverified replacement numbers.

### Integration Points
- `02_TR_E_POSITIONING_LOCK.md` feeds Phase 3 framing and wording choices.
- `03_CLAIM_LEDGER.md` feeds Phase 3 claim replacement/deletion and Phase 4 numerical provenance.
- `05_BLOCKERS_AND_SAFE_CLAIMS.md` feeds Phase 3 prohibited wording, Phase 4 verification priorities, and Phase 5 readiness classification.
- Phase 4 must reconcile final numerical claims against the ledger before final manuscript injection.
- Phase 5 must use the blocker/prohibited-wording rules before any `TR-E submission-ready` label.

</code_context>

<specifics>
## Specific Ideas

- Use occurrence-level claim IDs, with family IDs linking repeated ideas.
- Use non-numeric allowed sentences before Phase 4, with explicit Phase 4 placeholders for final values.
- Treat the ledger as both an audit artifact and an execution queue for Phase 3/4.
- Use the phrase `passenger-response-aware simulation framework` as the strongest safe method label.
- Use `operational service-design evidence` as the primary TR-E positioning anchor.
- Require explicit diagnostic qualifiers on each diagnostic-evidence claim, not only in table notes or paragraph introductions.
- Rename or reframe `Policy Implications` toward managerial and operational implications in Phase 3.

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within Phase 2 scope.

</deferred>

---

*Phase: 2-TR-E Positioning Lock and Claim Ledger*
*Context gathered: 2026-06-17T16:19:34.8091735+08:00*
