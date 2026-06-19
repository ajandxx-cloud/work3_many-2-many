# Requirements: Work 3 TR-E Claim-Ready Manuscript Package

**Defined:** 2026-06-16
**Core Value:** Produce a defensible TR Part E manuscript package in which every claim, table, figure, and positioning statement is traceable to the formal Phase 6 evidence or is clearly labeled as diagnostic, exploratory, or a limitation.

## v1 Requirements

Requirements for the current initialization roadmap. Each requirement must map to exactly one roadmap phase.

### Planning And Audit

- [x] **PLAN-01**: Project has a milestone folder at `.planning/milestones/tr_e_claim_ready/` containing the required milestone artifacts.
- [x] **PLAN-02**: Project has `00_MILESTONE_PLAN.md` defining execution order, evidence boundaries, manuscript touchpoints, and verification gates.
- [x] **PLAN-03**: Project has `01_REPO_AND_EVIDENCE_AUDIT.md` documenting canonical source files, canonical evidence packages, non-canonical archives/smoke outputs, and current repository risks.
- [x] **PLAN-04**: Project has `05_BLOCKERS_AND_SAFE_CLAIMS.md` identifying claim-critical blockers, safe claims, downgraded claims, and prohibited wording.

### TR-E Positioning

- [x] **POSE-01**: README, manuscript metadata, and project-facing documentation touched by this milestone consistently target Transportation Research Part E: Logistics and Transportation Review.
- [x] **POSE-02**: Manuscript title, abstract, introduction, and contribution framing present the work as a logistics/operations contribution rather than a TR Part A policy-first contribution.
- [x] **POSE-03**: Literature review connects the paper to DARP, meeting-point DRT, dynamic DRT routing, on-demand mobility logistics, service consolidation, passenger choice, and rolling-horizon operations.
- [x] **POSE-04**: The policy section is reframed as managerial and operational implications for service design, fleet deployment, consolidation, coverage-efficiency trade-offs, and passenger-segment monitoring.

### Claims And Evidence

- [x] **CLAI-01**: Project has `02_TR_E_POSITIONING_LOCK.md` stating the allowed paper framing, prohibited framing, core contribution, and journal-fit rationale.
- [x] **CLAI-02**: Project has `03_CLAIM_LEDGER.md` mapping each manuscript claim with mandatory columns: `source_path`, `script_path`, `generation_command`, `metric_formula`, `numerator`, `denominator`, `evidence_role`, `allowed_sentence`, and `prohibited_sentence`, plus manuscript location, comparison, metric, and reported number where applicable.
- [x] **CLAI-03**: Every numerical claim in abstract, introduction, experiments, managerial/operational implications, and conclusion appears in the claim ledger.
- [x] **CLAI-04**: Claims distinguish primary behavioral evidence, matched-coverage diagnostic evidence, fixed-accepted-set diagnostic evidence, robustness/sensitivity evidence, equity/type heterogeneity evidence, algorithm diagnostics, and limitations.
- [x] **CLAI-05**: Manuscript does not state or imply that FullModel universally dominates DoorToDoor or all baselines.
- [x] **CLAI-06**: Manuscript describes Gamma only as post-hoc welfare accounting unless endogenous Gamma behavior is implemented and tested in a separate future milestone.
- [x] **CLAI-07**: Manuscript describes the Beijing scenario as Beijing-inspired or semi-realistic synthetic grid unless real public data ingestion is implemented.
- [x] **CLAI-08**: Manuscript describes the MILP only as a simplified ex-post routing diagnostic for fixed accepted sets, not a full exact dynamic routing benchmark or ALNS near-optimality proof.

### Manuscript Revision

- [x] **MANU-01**: `manuscript/main.tex` journal field is updated from Transportation Research Part A to Transportation Research Part E: Logistics and Transportation Review.
- [x] **MANU-02**: Abstract is rewritten to emphasize logistics, service consolidation, dynamic routing, operational efficiency, passenger-response-aware offer design, evidence provenance, and conditional findings, but final concrete percentages, uplift values, confidence intervals, and table/figure references are not injected until Phase 4 verifies provenance.
- [x] **MANU-03**: Introduction contribution list is rewritten as concise, defensible, evidence-consistent TR-E contributions, with final numerical claims deferred until Phase 4 provenance checks.
- [x] **MANU-04**: Model and algorithm sections are revised only as needed to keep offer generation, passenger response, rolling horizon routing, Gamma semantics, and MILP scope clear and claim-consistent.
- [x] **MANU-05**: Experiments section separates main formal evidence, diagnostics, robustness/sensitivity, equity/type heterogeneity, and algorithm diagnostics.
- [x] **MANU-06**: Managerial and operational implications replace policy-first framing while retaining clearly labeled public-service implications where supported.
- [x] **MANU-07**: Conclusion states conditional contributions, formal evidence boundaries, limitations, and future work without overclaiming, with final concrete numerical claims deferred until Phase 4 provenance checks.
- [x] **MANU-08**: Elsevier-style prose is polished, and bullet-style contribution lists are converted to acceptable academic prose or concise list form when needed.

### Tables Figures And Provenance

- [x] **TFIG-01**: Manuscript-ready tables are generated or refreshed from formal Phase 6 processed outputs only.
- [x] **TFIG-02**: Manuscript-ready figures are generated or refreshed from validated formal Phase 6 processed outputs only.
- [x] **TFIG-03**: Any old manuscript table using 3-seed results is replaced with formal Phase 6 evidence or clearly removed from the main paper.
- [x] **TFIG-04**: Existing old values such as 18.3%, 29.1%, 35.0%, and 0.1216 are checked against current formal evidence and either updated, retained with provenance, or removed; only after this check may verified final numbers be injected into abstract, introduction, experiments, managerial/operational implications, and conclusion.
- [x] **TFIG-05**: Denominators are consistent and labeled for vkm per served trip, vkm per original request, served share, behavioral acceptance rate, choice rejection rate, and feasibility rejection rate.
- [x] **TFIG-06**: Weight sensitivity calculations use the shared metric helper and are not inflated by acceptance-rate-only denominators.

### Verification And Readiness

- [x] **VERI-01**: Project has `04_MANUSCRIPT_ACTION_PLAN.md` sequencing manuscript edits, evidence checks, table/figure refresh, and verification tasks.
- [x] **VERI-02**: Formal statistics validation command is run when available, or its unavailability is documented with manuscript impact.
- [x] **VERI-03**: Targeted pytest checks run for metrics, variants, runner, scenarios, coverage controls, robustness, and formal statistics, or any failures are documented with exact reason and manuscript impact.
- [ ] **VERI-04**: Manuscript compilation is run from `manuscript/` using a pdflatex/bibtex/pdflatex/pdflatex sequence, or any failure is documented with exact reason and manuscript impact.
- [ ] **VERI-05**: Project has `99_MILESTONE_VERIFICATION.md` recording verification commands, outputs, pass/fail status, remaining blockers, and readiness classification.
- [ ] **VERI-06**: Final readiness status is one of: TR-E submission-ready, TR-E near-ready with minor blockers, or not ready due to specific blockers; `TR-E submission-ready` is allowed only when manuscript compilation passes, formal statistics validation passes or documented failures have no submission impact, targeted pytest checks pass or documented failures have no manuscript impact, claim ledger covers 100% of numerical claims, all manuscript tables/figures trace to `results/formal/phase06/`, and prohibited wording is absent.

## v2 Requirements

Deferred to future milestones. Tracked but not in the current roadmap.

### Empirical Data

- **DATA-01**: Implement reproducible public-data ingestion for a real Beijing case study.
- **DATA-02**: Validate passenger choice parameters against stated-preference or revealed-preference data.
- **DATA-03**: Add environment/dependency provenance for formal runs, including Python, package versions, OS, CPU, and solver status.

### Model Extensions

- **MODL-01**: Implement endogenous Gamma behavior in offer generation, routing, or acceptance decisions if Pareto-frontier claims are desired.
- **MODL-02**: Replace the simplified ex-post MILP diagnostic with a fuller exact dynamic routing benchmark if exactness claims are desired.
- **MODL-03**: Add richer passenger choice sets beyond a single-offer binary logit mechanism.
- **MODL-04**: Improve rolling-horizon service ledger bookkeeping for exact completed-trip walking and in-vehicle time reconstruction.

### Reproducibility Hardening

- **REPR-01**: Make bare `pytest` from the repository root green by configuring `testpaths`, `pythonpath`, and archive exclusions.
- **REPR-02**: Add dependency metadata or extras for pandas and matplotlib.
- **REPR-03**: Add a lockfile or constraints file for paper reproduction.

## Out of Scope

Explicitly excluded from the current initialization roadmap.

| Feature | Reason |
|---------|--------|
| Broad algorithm redesign | Current goal is manuscript readiness and claim integrity, not a new optimization method. |
| Full formal experiment rerun by default | Phase 6 formal evidence has passed validation; rerun only if verification fails or a claim-critical formula bug is found. |
| Manual editing of numerical results | Violates evidence integrity and user constraints. |
| Hidden parameter tuning for stronger narrative | Violates evidence integrity and would make claims indefensible. |
| Real Beijing validation claim | No reproducible real public-data ingestion pipeline is currently established. |
| Endogenous Pareto frontier claim | Gamma is currently post-hoc welfare accounting only. |
| Full exact dynamic routing benchmark claim | Current MILP is a simplified ex-post diagnostic. |
| Archive/smoke/ad hoc outputs as formal evidence | Non-canonical unless explicitly audited and labeled historical or diagnostic. |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| PLAN-01 | Phase 1 | Complete |
| PLAN-02 | Phase 1 | Complete |
| PLAN-03 | Phase 1 | Complete |
| PLAN-04 | Phase 2 | Complete |
| POSE-01 | Phase 3 | Complete |
| POSE-02 | Phase 3 | Complete |
| POSE-03 | Phase 3 | Complete |
| POSE-04 | Phase 3 | Complete |
| CLAI-01 | Phase 2 | Complete |
| CLAI-02 | Phase 2 | Complete |
| CLAI-03 | Phase 2 | Complete |
| CLAI-04 | Phase 2 | Complete |
| CLAI-05 | Phase 3 | Complete |
| CLAI-06 | Phase 3 | Complete |
| CLAI-07 | Phase 3 | Complete |
| CLAI-08 | Phase 3 | Complete |
| MANU-01 | Phase 3 | Complete |
| MANU-02 | Phase 3 | Complete |
| MANU-03 | Phase 3 | Complete |
| MANU-04 | Phase 3 | Complete |
| MANU-05 | Phase 3 | Complete |
| MANU-06 | Phase 3 | Complete |
| MANU-07 | Phase 3 | Complete |
| MANU-08 | Phase 3 | Complete |
| TFIG-01 | Phase 4 | Complete |
| TFIG-02 | Phase 4 | Complete |
| TFIG-03 | Phase 4 | Complete |
| TFIG-04 | Phase 4 | Complete |
| TFIG-05 | Phase 4 | Complete |
| TFIG-06 | Phase 4 | Complete |
| VERI-01 | Phase 1 | Complete |
| VERI-02 | Phase 5 | Complete |
| VERI-03 | Phase 5 | Complete |
| VERI-04 | Phase 5 | Pending |
| VERI-05 | Phase 5 | Pending |
| VERI-06 | Phase 5 | Pending |

**Coverage:**
- v1 requirements: 36 total
- Mapped to phases: 36
- Unmapped: 0

---
*Requirements defined: 2026-06-16*
*Last updated: 2026-06-16 after roadmap creation*
