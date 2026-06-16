# Phase 09 Research: Manuscript Restructure for TR Part E

**Phase:** 09 - Manuscript Restructure for TR Part E
**Date:** 2026-06-16
**Status:** Research complete

## Research Question

What does Phase 9 need to know to plan a defensible Transportation Research Part E
manuscript restructure without importing unsupported evidence or reviving known
metric, comparison, and external-validity risks?

## Executive Findings

Phase 9 should be planned as a manuscript architecture and evidence-translation
phase, not as a final claim-writing phase. The current manuscript still carries
TR Part A targeting, unconditional efficiency language, mixed comparison families,
coverage-confounded headline results, and policy-style recommendations. The
restructure should instead build a TR-E logistics/operations manuscript around
an evidence chain: fair service-design comparison, shared passenger response,
coverage controls, formal paired evidence, claim grading, limitations, and
bounded managerial insights.

The most important planning constraint is that Phase 8 artifacts are absent in
this workspace. Phase 9 can define structure, templates, and placeholders now,
but final abstract, introduction, table captions, conclusion bullets, and
managerial claims must be blocked on:

- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_CLAIM_EVIDENCE_MATRIX.md`
- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_SUPPORTED_CLAIMS.md`
- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md`

## External Journal Constraints

Official ScienceDirect/Elsevier pages checked on 2026-06-16:

- TR-E aims and scope: https://www.sciencedirect.com/journal/transportation-research-part-e-logistics-and-transportation-review/about/aims-and-scope
- TR-E guide for authors: https://www.sciencedirect.com/journal/transportation-research-part-e-logistics-and-transportation-review/publish/guide-for-authors

Planning implications:

- TR-E is differentiated from the other Transportation Research journals by its
  logistics focus. The manuscript should make the operational logistics problem
  central: service design, dispatch, demand response, routing efficiency,
  coverage, and reproducibility.
- TR-E accepts diverse methods including operations research, simulation,
  experiments, empirical analysis, machine learning, and network analysis. A
  simulation-plus-operations manuscript is in scope if the methods, evidence
  boundaries, and data transparency are clear.
- The journal uses double anonymized review. Final manuscript packaging should
  separate title-page material and keep the anonymized manuscript free of author
  names, affiliations, and acknowledgements.
- Abstract must be concise, factual, standalone, and no longer than 250 words.
  It should state purpose, principal results, and major conclusions without
  references or unexplained abbreviations.
- Highlights are required: 3 to 5 bullet points, each no more than 85 characters.
  Phase 9 should plan them even if the roadmap outputs do not explicitly list a
  highlights artifact.
- Tables must be editable text, cited in order, numbered consecutively, captioned,
  and used sparingly. This supports a compact main-table strategy with detail in
  appendix/supplement.
- Figures must be cited in order, captioned, and supplied as separate files with
  logical names. Captions should explain symbols and abbreviations, with minimal
  text inside images.
- Elsevier does not permit generative AI or AI-assisted tools to create or alter
  submitted images except when that is part of the research design and described
  reproducibly. Figure work should rely on reproducible scripts and generated
  plots from project data, not AI-created artwork.
- Supplementary material must be accurate, relevant, cited from the manuscript,
  submitted with the manuscript, and clearly captioned. Phase 9 should explicitly
  allocate detailed robustness, equity, failure, and diagnostic tables to
  appendix/supplement roles.
- Research data transparency is encouraged. The manuscript structure should
  reserve space for data/code availability and, later, cite repositories or state
  why data cannot be shared.
- If generative AI tools contribute to manuscript preparation, Elsevier requires
  a declaration section before references at submission. Phase 9 should flag this
  as a final-submission task if AI-assisted text drafting is used.

## Local Manuscript Diagnosis

Current manuscript source under `manuscript/` is modular enough for targeted
restructuring:

- `manuscript/main.tex` owns journal target, title, front matter, section order,
  bibliography, and appendix.
- `manuscript/sections/abstract.tex` contains the current abstract and keywords.
- `manuscript/sections/intro.tex` contains the current evidence gap, contribution
  list, and paper organization.
- `manuscript/sections/literature.tex` contains DARP, meeting-point,
  passenger-choice, rolling-horizon, and positioning material.
- `manuscript/sections/model.tex` contains problem formulation, passenger choice,
  and three-layer architecture.
- `manuscript/sections/algorithm.tex` contains MILP diagnostic and rolling-horizon
  ALNS methodology.
- `manuscript/sections/experiments.tex` mixes main results, diagnostics,
  sensitivity, equity, welfare/gamma, and weight sensitivity.
- `manuscript/sections/policy.tex` contains five policy recommendations and
  VOT interpretation.
- `manuscript/sections/conclusion.tex` restates headline claims and policy
  implications.

Main risks in the current text:

- `main.tex` still targets Transportation Research Part A and the title still
  reads like a method paper rather than a claim-gated TR-E evidence-chain paper.
- The abstract makes numerical claims from the older evidence chain, including
  the 29.1% improvement, equity values, and five policy implications. These must
  not be final until Phase 8 claim grading exists.
- The introduction still says the paper "fills" a broad gap and includes a
  contribution that empirically demonstrates a 29.1% gain. This should become a
  conditional research question and evidence-chain contribution.
- Literature positioning still uses "to our knowledge, first" style language.
  Phase 1 forbids broad first/only claims unless a precise scoped version is
  verified.
- Model and algorithm sections are separate. Phase 9 context prefers combining
  them into `Framework and Solution Approach`, with MILP, greedy, no-rolling-
  horizon, and no-choice paths labeled as diagnostics.
- Experiments mix behavioral evidence and diagnostics in one section. Phase 9
  should split experimental design from evidence families, then separate main
  evidence, robustness controls, equity, and algorithm diagnostics.
- `policy.tex` presents scenario-specific results as policy implications for
  Chinese city operators. These should be reframed as simulation-based
  managerial insights with explicit condition, supported insight, applicability
  boundary, and limitation.
- There is no standalone limitations section before managerial insights.

## Upstream Evidence Contracts to Preserve

From Phase 2:

- Behavioral main comparisons must use shared passenger-response assumptions.
  Door-to-door all-accept rows cannot be compared against choice-filtered
  bidirectional rows as if they were fair behavioral evidence.
- Main behavioral tables must report the efficiency-and-coverage quartet:
  `total_vkm`, `vkm_per_served_trip`, `vkm_per_original_request`, and
  `served_share`.
- `vkm_per_trip` is forbidden for new formal evidence. Use explicit denominator
  names.
- Matched-coverage and fixed accepted-set controls support interpretation but
  are not standalone superiority evidence.
- Deterministic diagnostics and algorithm diagnostics must not become headline
  behavioral evidence.
- Gamma/welfare sweeps must not be called a Pareto frontier unless gamma affects
  routing, offers, or acceptance.
- Paired differences and confidence intervals should be the main formal
  comparison language where formal results are available.

From Phase 6:

- Main evidence should use four behavioral service designs:
  `DoorToDoor + Choice`, `SingleSidedPickup + Choice`,
  `SingleSidedDropoff + Choice`, and
  `BidirectionalMP + Choice + RollingHorizon/ALNS`.
- Diagnostic methods such as no-rolling-horizon, greedy insertion, ALNS budget
  diagnostics, and MILP/static diagnostics are not main evidence methods.
- Main matrix completion, quartet metrics, paired confidence intervals, and
  absence or explanation of critical supplementary conflicts are prerequisites
  for Phase 8 claim approval.
- Supplementary packages should be reported as main-text robustness summaries
  with complete details in appendix/supplement material.

## Recommended Manuscript Architecture

The manuscript should move from "method wins" to "evidence-chain reconstruction."
A suitable section order is:

1. Introduction: evidence gap, research questions, contributions, and claim
   discipline.
2. Literature and positioning: DARPmp, bidirectional walking, choice-aware DRT,
   rolling horizon, and the precise gap.
3. Framework and Solution Approach: choice-aware service-design framework,
   passenger response, rolling-horizon ALNS, and diagnostic solvers.
4. Experimental Design and Evidence Families: methods, scenarios, response
   assumptions, metrics, paired design, and family roles.
5. Formal Main Evidence: only claim-gated behavioral comparisons.
6. Robustness, Equity, and Diagnostic Evidence: matched coverage, fixed
   accepted set, utility sensitivity, equity, and algorithm diagnostics.
7. Limitations and Boundary Conditions.
8. Managerial Insights and Boundary Conditions.
9. Conclusion.

This architecture preserves TR-E logistics fit by foregrounding service design,
operational evidence, simulation controls, and bounded managerial insight.

## Table and Figure Planning

Main text should be sparse and evidence-role explicit:

- Main Table 1: formal behavioral evidence matrix over the four core methods,
  reporting the quartet plus paired differences and confidence intervals.
- Main Table 2: paired-difference summary by scale/comparison, if Phase 8
  supports a concise claim.
- Main Table 3 or compact panel: robustness challenge summary for matched
  coverage and fixed accepted-set controls.
- Main Figure 1: evidence-chain or framework schematic, replacing any figure
  that implies unsupported mechanism/result certainty.
- Main Figure 2: service-design comparison plot over claim-gated metrics.
- Main Figure 3: equity/boundary-condition summary if Phase 8 supports it.
- Appendix/supplement tables: complete rows, failures/timeouts, utility
  sensitivity, meeting-point density, fleet/demand, type-level distributions,
  ALNS diagnostics, MILP/no-Gurobi status, and full run provenance.

Avoid:

- Mixing `FullModel`, `DoorToDoor`, and diagnostic labels as paper-facing method
  names.
- Tables that report only vehicle-km or only `vkm_per_served_trip`.
- Figures using old generated outputs without checking their result provenance.
- Policy maps that look prescriptive when the scenario is synthetic.

## Planning Recommendations

Phase 9 should create five executable plans:

1. Manuscript architecture and source-of-truth restructure artifact.
2. Abstract and highlights plan, blocked on Phase 8 supported claims.
3. Introduction and literature positioning plan, replacing overclaiming with
   research questions and evidence-chain contribution.
4. Experiment and evidence-family section plan, translating Phase 2/6 contracts
   into TR-E main text and appendix/supplement allocation.
5. Table/figure and managerial-insight plan, converting policy claims into
   bounded simulation insights and explicit limitations.

The plans should primarily write Phase 9 Markdown outputs. Direct LaTeX edits
can be included as optional or follow-up tasks only after Phase 8 artifacts are
present and read.

## Blockers and Open Checks

- Phase 8 claim-gate artifacts are absent. Final wording must stay placeholder-
  based until they exist.
- Phase 7 case-study artifacts are absent. Beijing language must remain
  "Beijing-inspired synthetic scenario" unless later evidence says otherwise.
- Phase 6 formal result report is not present in this workspace. Do not cite
  final formal numbers from Phase 6 unless the report exists and passes.
- Current manuscript and bibliography contain old target-journal and possible
  bibliography cleanup needs; final paper packaging should include those checks.

## RESEARCH COMPLETE

