# Work 3 TR-E Claim-Ready Manuscript Package

## What This Is

This project is the current Work 3 research repository for a many-to-many demand-responsive transit (DRT) manuscript and its reproducible experiment package. The immediate project goal is to turn the existing experimental repository into a Transportation Research Part E: Logistics and Transportation Review-ready manuscript package, repositioned around logistics and operations rather than a Transportation Research Part A policy framing.

The paper studies passenger-response-aware bidirectional meeting-point consolidation for many-to-many DRT. The central contribution is conditional and evidence-bounded: bidirectional pickup and dropoff meeting points, binary-logit passenger response, and rolling-horizon routing can reduce routing intensity per served trip under specific service-design conditions, while creating measurable coverage and passenger-type trade-offs.

## Core Value

Produce a defensible TR Part E manuscript package in which every claim, table, figure, and positioning statement is traceable to the formal Phase 6 evidence or is clearly labeled as diagnostic, exploratory, or a limitation.

## Requirements

### Validated

- The repository contains a reusable Python DRT simulation package under `src/drt/` with meeting-point candidate generation, feasibility checks, insertion evaluation, binary-logit passenger response, rolling-horizon ALNS, and an ex-post MILP diagnostic.
- The repository contains phase-specific experiment harnesses under `experiments/`, including formal Phase 6 main behavioral runs, coverage controls, robustness packages, equity outcomes, and algorithm diagnostics.
- The current formal evidence package is under `results/formal/phase06/`, and its manifest reports the formal smoke package as excluded from formal evidence.
- Phase 6 validation passed for the main behavioral matrix, coverage controls, robustness packages, denominator checks, failure ledger, and raw-to-processed provenance.
- The formal main behavioral package contains 320 completed rows across 20 paired seeds, four scales, and four main behavioral methods.
- Coverage-control packages, robustness packages, equity type outcomes, and algorithm diagnostics have validator reports and durable rows where applicable.
- `manuscript/` is the canonical current paper source; archive paths and root legacy results are non-canonical unless explicitly used for historical comparison.
- Existing codebase concerns document known risks around default pytest collection, undeclared pandas/matplotlib dependencies, route-stop bookkeeping, Gamma semantics, Beijing scenario wording, and MILP diagnostic scope.
- Phase 1 completed the evidence-foundation scaffold: `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md`, `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md`, and `.planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md` exist, with verification passed in `.planning/phases/01-evidence-foundation-and-milestone-setup/01-VERIFICATION.md`.

### Active

- [ ] Reposition README, manuscript metadata, abstract, introduction, literature review, experiment narrative, implications, and conclusion from a Part A policy-first framing to a TR Part E logistics-and-operations framing.
- [ ] Create the milestone planning and audit folder `.planning/milestones/tr_e_claim_ready/` with a milestone plan, repository/evidence audit, TR-E positioning lock, claim ledger, manuscript action plan, blockers/safe claims table, and verification report.
- [ ] Build a claim ledger that maps every numerical and qualitative manuscript claim to source path, generation script, generation command, metric formula, numerator, denominator, evidence role, allowed sentence, and prohibited sentence.
- [ ] Replace or relabel any old 3-seed, smoke, archived, or ad hoc manuscript claims that conflict with the formal Phase 6 evidence package.
- [ ] Keep the main claim conditional: FullModel can lower vehicle-km per served trip relative to DoorToDoor under the tested synthetic service-design conditions, but it has lower served share and passenger-response trade-offs.
- [ ] Clearly separate primary behavioral evidence, matched-coverage diagnostics, fixed-accepted-set diagnostics, robustness/sensitivity evidence, equity/type heterogeneity evidence, and algorithm diagnostics.
- [ ] Ensure Gamma is described only as post-hoc welfare accounting unless future work implements endogenous Gamma behavior.
- [ ] Ensure Beijing wording is "Beijing-inspired synthetic grid" or equivalent unless a real public data ingestion pipeline and reproducible dataset are implemented.
- [ ] Ensure the MILP is described as a simplified ex-post routing diagnostic for fixed accepted sets, not as a full exact dynamic routing benchmark or proof of ALNS near-optimality.
- [ ] Keep Phase 3 manuscript edits structural and non-numeric where final values depend on refreshed evidence; inject final percentages, uplift values, confidence intervals, and table/figure references only after Phase 4 provenance checks.
- [ ] Regenerate or refresh manuscript-ready tables and figures only from validated processed formal Phase 6 outputs.
- [ ] Mark the paper TR-E submission-ready only if hard readiness gates pass: manuscript compiles, validation and tests pass or documented failures have no submission impact, claim ledger covers 100% numerical claims, all tables/figures trace to `results/formal/phase06/`, and no prohibited wording remains.

### Out of Scope

- Broad algorithm redesign - this milestone is for manuscript readiness unless a claim-critical bug blocks validity.
- Hidden parameter tuning or experiment modification to obtain stronger conclusions - all numerical changes must preserve provenance and be documented.
- Fabricating or manually editing result numbers - every number must come from raw, processed, table, figure, or validation artifacts.
- Treating diagnostic evidence as a primary headline claim - diagnostics can support interpretation only when labeled as such.
- Claiming universal dominance over DoorToDoor or all baselines - the evidence supports conditional efficiency-consolidation claims with coverage and acceptance trade-offs.
- Claiming real Beijing validation - the current scenario is synthetic or Beijing-inspired unless real-data ingestion is added in a separate scoped milestone.
- Claiming an endogenous Pareto frontier or Gamma-controlled routing behavior - current Gamma behavior is post-hoc welfare scoring.
- Treating archive, old paper, paper_work3, root smoke outputs, or ad hoc tests as formal evidence without explicit provenance review.

## Context

The repository is a brownfield academic simulation and manuscript project. It contains Python source code, experiment runners, formal result artifacts, manuscript LaTeX files, generated figures, tests, and archival materials.

The original project framing in `README.md`, `CLAUDE.md`, and `manuscript/main.tex` targets Transportation Research Part A: Policy and Practice. The new target is Transportation Research Part E: Logistics and Transportation Review. The revised framing should emphasize logistics, service consolidation, operator decisions, fleet deployment, dynamic routing, passenger-response-aware offer design, and reproducible evidence.

The canonical manuscript source is `manuscript/main.tex` plus `manuscript/sections/*.tex` and `manuscript/references.bib`. The current paper already includes many useful guardrails, including post-hoc Gamma language, Beijing-inspired synthetic wording in some locations, and matched-coverage diagnostic labeling. However, Part A policy language, old headline values, table consistency, and claim/evidence traceability still need systematic audit.

The canonical formal evidence package is `results/formal/phase06/`. The top-level verification report says the formal main behavioral matrix has 20 paired seeds, the expected seed-scale-method rows exist, coverage controls and robustness packages have complete or durable rows, denominator checks passed, and known failed rows are recorded in the failure ledger.

Key current evidence signals from formal Phase 6 include:

- FullModel has lower served share than DoorToDoor in aggregate formal paired comparisons.
- FullModel has lower vehicle-km per served trip and per original request than DoorToDoor in the formal main behavioral comparison.
- Behavioral acceptance differences are mixed and should not be overclaimed.
- Matched-coverage and fixed-accepted-set outputs are diagnostic controls and must not become the primary headline claim.
- Equity/type outcomes are useful but limited evidence and should be presented as heterogeneity/monitoring implications.
- Algorithm diagnostics and MILP results are diagnostic, not proof of full exact optimality.

## Constraints

- **Evidence integrity**: No fabrication, no manual numeric editing, no hidden parameter tuning, and no untracked evidence substitutions.
- **Evidence provenance**: Every changed manuscript claim must trace to a formal result file, table, figure script, raw/processed artifact, or validation report.
- **Evidence boundary**: Formal claims must use `results/formal/phase06/`; smoke tests, archive outputs, root legacy CSVs, and ad hoc outputs are non-canonical by default.
- **Target journal**: The working target is Transportation Research Part E: Logistics and Transportation Review.
- **Claim posture**: Claims must be conditional, operational, and logistics-oriented; avoid universal dominance, real-world validation, or policy-overreach language.
- **Gamma semantics**: Gamma is post-hoc welfare accounting only unless a future milestone implements endogenous behavior.
- **Scenario semantics**: Beijing evidence is Beijing-inspired or semi-realistic synthetic grid unless real public-data ingestion exists.
- **MILP semantics**: MILP is a simplified ex-post routing diagnostic for fixed accepted sets, not a complete dynamic benchmark.
- **Numerical injection order**: Phase 3 may revise structure, positioning, and non-numeric wording, but final concrete percentages, improvement values, confidence intervals, significance language, and table/figure numbers must wait until Phase 4 verifies provenance.
- **Claim ledger schema**: Claim ledger rows must include `source_path`, `script_path`, `generation_command`, `metric_formula`, `numerator`, `denominator`, `evidence_role`, `allowed_sentence`, and `prohibited_sentence`.
- **Readiness standard**: The final report may say "TR-E submission-ready" only when manuscript compilation passes, formal validation passes or non-impacting failures are documented, targeted tests pass or non-impacting failures are documented, numerical-claim ledger coverage is 100%, all tables and figures trace to `results/formal/phase06/`, and prohibited wording scans clean.
- **Code scope**: Fix only manuscript-critical reproducibility issues in this milestone unless a claim-critical bug is discovered.
- **Generated files**: Keep generated results, figures, caches, and archive artifacts separate from source and planning artifacts.
- **Verification**: Minimum verification should include formal statistics validation when available, targeted pytest checks, and manuscript compilation.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Target TR Part E rather than TR Part A | User explicitly requested TR-E claim-ready manuscript repositioning; current Part A policy framing is mismatched. | Pending |
| Treat `manuscript/` as canonical paper source | User specified manuscript source; archive and old paper paths are historical. | Pending |
| Treat `results/formal/phase06/` as canonical evidence | User specified Phase 6 as current formal evidence, and verification reports indicate it passed. | Pending |
| Use conditional logistics/operations claim wording | Formal evidence supports efficiency-consolidation under tested conditions, not universal superiority. | Pending |
| Classify matched coverage, fixed accepted set, MILP, Gamma, and algorithm checks as diagnostics unless stronger evidence exists | Prevents diagnostic evidence from being promoted into primary claims. | Pending |
| Do not rerun full formal experiments by default | Current formal evidence package passed; reruns are reserved for failed verification or claim-critical formula bugs. | Pending |
| Defer final numerical injection until Phase 4 | Prevents Phase 3 prose from baking in numbers before table/figure provenance is refreshed. | Pending |
| Require hard claim-ledger columns and readiness gates | Keeps claim control operational rather than merely narrative. | Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `$gsd-transition`):
1. Requirements invalidated? Move to Out of Scope with reason.
2. Requirements validated? Move to Validated with phase reference.
3. New requirements emerged? Add to Active.
4. Decisions to log? Add to Key Decisions.
5. "What This Is" still accurate? Update if drifted.

**After each milestone** (via `$gsd-complete-milestone`):
1. Full review of all sections.
2. Core Value check - still the right priority?
3. Audit Out of Scope - reasons still valid?
4. Update Context with current state.

---
*Last updated: 2026-06-16 after Phase 1 completion*
