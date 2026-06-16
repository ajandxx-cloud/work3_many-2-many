# Manuscript Action Plan

## Purpose

This action plan sequences later manuscript edits, evidence checks,
table/figure refresh, and verification work. It does not draft final
replacement prose and does not lock final percentages, uplift values,
confidence intervals, significance wording, or table/figure numbers.

Final numerical injection: defer until Phase 4.

## Axis 1: Manuscript File And Region

| File/region | Later action | Evidence gate |
|-------------|--------------|---------------|
| `manuscript/main.tex` | Phase 3 updates journal metadata and package-facing target from Transportation Research Part A to Transportation Research Part E: Logistics and Transportation Review. | No numerical evidence gate; Phase 5 compile gate applies. |
| `manuscript/sections/abstract.tex` | Phase 3 rewrites as conditional logistics/operations contribution with no final evidence-dependent numbers. | Final percentages, CIs, significance language, and table/figure references defer until Phase 4. |
| `manuscript/sections/intro.tex` | Phase 3 revises motivation and contributions around logistics, consolidation, passenger-response-aware offer design, and rolling-horizon operations. | Final contribution numbers defer until Phase 4 and must map to `03_CLAIM_LEDGER.md`. |
| `manuscript/sections/literature.tex` | Phase 3 strengthens DARP, meeting-point DRT, on-demand mobility logistics, passenger choice, and dynamic DRT operations positioning. | Bibliographic changes only; no result-number gate. |
| `manuscript/sections/model.tex` | Phase 3 clarifies binary-logit response, meeting-point semantics, Gamma post-hoc accounting, and Beijing-inspired synthetic scenario language where model-facing. | Gamma must not be described as endogenous unless future evidence exists. |
| `manuscript/sections/algorithm.tex` | Phase 3 clarifies rolling horizon, ALNS heuristic role, and MILP simplified ex-post diagnostic scope. | MILP language must not imply complete exact dynamic benchmark or ALNS near-optimality. |
| `manuscript/sections/experiments.tex` | Phase 3 separates primary evidence from diagnostics, robustness, equity/type heterogeneity, and algorithm diagnostics. Phase 4 reconciles tables and numerical text. | All final reported values defer until Phase 4 and must trace to `results/formal/phase06/`. |
| `manuscript/sections/policy.tex` | Phase 3 reframes policy-first text as managerial and operational implications for service design, fleet deployment, consolidation, coverage-efficiency trade-offs, and passenger-segment monitoring. | Any retained numerical examples defer until Phase 4; public-service implications must be labeled as supported limitations. |
| `manuscript/sections/conclusion.tex` | Phase 3 states conditional contribution, limitations, evidence boundaries, and future work without overclaiming. | Final headline values defer until Phase 4. |
| `manuscript/references.bib` | Phase 3/4 update only if needed for TR-E logistics/operations fit or cited evidence support. | Bibliography consistency checked during Phase 5 compilation. |

## Axis 2: Evidence Role

| Evidence role | How later phases use it | Boundary |
|---------------|-------------------------|----------|
| primary behavioral evidence | Phase 2 ledger maps main conditional claims; Phase 4 injects verified final values from `results/formal/phase06/main_behavioral/` and `results/formal/phase06/tables/`. | Must preserve coverage and passenger-response trade-offs. |
| matched-coverage diagnostic | Phase 2/3 label as diagnostic coverage-confounding check; Phase 4 verifies values if mentioned. | Not the primary headline estimate. |
| fixed-accepted-set diagnostic | Phase 2/3 label as fixed accepted set decomposition. | Not a complete dynamic benchmark. |
| robustness/sensitivity evidence | Phase 2/3 use for conditional service-design boundaries and limitations. | No unbounded generalization. |
| equity/type heterogeneity evidence | Phase 2/3 use for passenger-segment monitoring and limited heterogeneity implications. | No real population equity conclusion. |
| algorithm/MILP diagnostic | Phase 2/3 use for method-scope and limitation language. | No ALNS near-optimality proof or exact dynamic benchmark claim. |
| limitations | Phase 3/5 keep future work explicit: real Beijing data, endogenous Gamma, full exact benchmark, dependency provenance, and route-stop precision. | Do not convert limitations into claims. |

## Section-Level Wording Families For Scans

Later phases should scan for and replace or qualify these wording families:

- `Transportation Research Part A`
- `policy-first`
- `Policy Implications` when the section should become managerial or operational
- `real-world Beijing`
- `Beijing validation`
- `universal dominance`
- `dominates`
- `exact dynamic benchmark`
- `near-optimal`
- `endogenous Gamma`
- `Pareto frontier` when it implies behavior rather than post-hoc accounting
- `TR-E submission-ready` outside the Phase 5 final readiness report

## Numerical Injection Gate

For all manuscript files, defer until Phase 4:

- final percentages
- uplift or improvement values
- confidence intervals
- statistical significance wording
- table numbers
- figure numbers
- final values derived from paired differences, bootstrap intervals, equity
  summaries, matched-coverage diagnostics, fixed-accepted-set diagnostics,
  Gamma/Pareto sensitivity, or MILP diagnostics

Phase 4 must verify source path, script path, generation command, metric
formula, numerator, denominator, evidence role, allowed sentence, and prohibited
sentence through `03_CLAIM_LEDGER.md` before final injection.

## Phase Handoff

Phase 2 should create:

- `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md`
- `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md`
- `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md`

Phase 2 must build the safe-claims and blockers table from this action plan,
`01_REPO_AND_EVIDENCE_AUDIT.md`, current manuscript scans, formal evidence
paths, and the claim ledger. Phase 1 does not create a premature safe-claims
table.

Phase 3 should perform non-numeric TR-E manuscript repositioning:

- metadata and package-facing target updates
- abstract and introduction repositioning
- literature, model, and algorithm scope clarification
- experiments evidence-role separation
- managerial and operational implications
- conditional conclusion and limitations

Phase 4 should perform tables, figures, numerical provenance, and final
numerical injection:

- refresh or verify manuscript-ready tables from formal Phase 6 processed
  outputs only
- refresh or verify figures from formal Phase 6 processed outputs only
- reconcile old values such as `18.3%`, `29.1%`, `35.0%`, and `0.1216`
- verify denominators for vkm per served trip, vkm per original request,
  served share, behavioral acceptance rate, choice rejection rate, and
  feasibility rejection rate
- inject final values only after provenance is verified

Phase 5 should verify readiness:

- formal validation status
- targeted pytest checks
- LaTeX compilation
- claim-ledger coverage
- table/figure provenance
- prohibited wording scans
- readiness classification

`TR-E submission-ready` is allowed only as a Phase 5 readiness label after
manuscript compilation, validation/test impact checks, 100% numerical
claim-ledger coverage, formal Phase 6 table/figure provenance, and prohibited
wording scans all pass.

## Out Of Scope For Phase 1

- drafting final manuscript replacement prose
- correcting old manuscript values
- deciding safe claims before Phase 2
- rerunning formal experiments
- changing source code, result files, dependency metadata, README, or manuscript
  files
- implementing real Beijing public-data ingestion
- implementing endogenous Gamma behavior
- implementing a full exact dynamic benchmark

