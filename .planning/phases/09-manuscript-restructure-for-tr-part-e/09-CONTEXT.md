# Phase 9: Manuscript Restructure for TR Part E - Context

**Gathered:** 2026-06-16T10:12:31.7906036+08:00
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 9 turns the completed evidence chain into a Transportation Research Part E
manuscript structure. The phase should translate claim-gated evidence into a
cautious, conditional paper architecture: abstract, introduction, experiment
section plan, table/figure plan, and TR-E manuscript structure.

In scope:
- Rebuild the manuscript story around evidence-chain reconstruction rather than
  unconditional method superiority.
- Design a TR-E-style section structure that makes fair comparison, passenger
  response, coverage controls, formal evidence, limitations, and managerial
  boundary conditions visible.
- Plan paper-facing tables and figures so main behavioral evidence, robustness
  controls, equity trade-offs, and algorithm diagnostics are not mixed.
- Rewrite the abstract and introduction plan around cautious, conditional
  claims that pass the Phase 8 claim-evidence gate.
- Convert the current policy section into simulation-based managerial insights
  with explicit boundary conditions.

Out of scope:
- Running new experiments or changing the experiment design.
- Approving final claims before Phase 8 claim-evidence artifacts exist.
- Using pilot, diagnostic, or supplementary evidence as headline evidence.
- Presenting Beijing-inspired synthetic scenarios as real Beijing evidence.
- Writing universal city-policy prescriptions from synthetic simulations.

Critical upstream dependency:
- Phase 9 must consume Phase 8 claim-gate outputs before final claim wording is
  locked. If Phase 8 artifacts do not exist when Phase 9 planning starts, the
  planner must treat them as blocking prerequisites or write explicit
  placeholders requiring those artifacts before manuscript text is finalized.

</domain>

<decisions>
## Implementation Decisions

### Manuscript Storyline
- **D-01:** The manuscript's main storyline must be evidence-chain
  reconstruction. It should explain how the project rebuilds a defensible chain
  from fair baselines, shared passenger response, coverage controls, formal
  paired evidence, and claim gating.
- **D-02:** The introduction should open with the reviewer-facing evidence gap:
  meeting-point DRT evidence is easily confounded by passenger response,
  coverage, baseline inconsistency, and diagnostic/result mixing.
- **D-03:** The title and abstract should use a cautious, conditional tone.
  Avoid unconditional superiority language and emphasize conditions such as
  consistent passenger response, fair comparison, and bounded simulation
  evidence.
- **D-04:** The contribution list should be ordered as evidence discipline,
  model/framework, experimental findings, and managerial implications. The
  paper should not lead with "our method wins."

### Section Restructuring
- **D-05:** Use a TR-E evidence-chain structure rather than preserving the
  current section skeleton unchanged.
- **D-06:** Combine model and algorithm material into a single
  `Framework and Solution Approach` section. This section should present the
  choice-aware service-design framework, passenger response, and rolling-horizon
  ALNS as the operational mechanism, while labeling greedy, no-rolling-horizon,
  and MILP paths as diagnostics.
- **D-07:** Organize the experiment section as experimental design first, then
  evidence packages. The reader should see the boundaries between main
  evidence, matched coverage, fixed accepted-set controls, utility sensitivity,
  equity, and algorithm diagnostics before reading results.
- **D-08:** Place limitations as a standalone section before managerial
  insights. Boundary conditions must be established before any applied
  implication is presented.
- **D-09:** A suitable high-level manuscript outline is:
  1. Introduction: evidence gap, research questions, and contributions.
  2. Literature and positioning.
  3. Framework and Solution Approach.
  4. Experimental Design and Evidence Families.
  5. Formal Main Evidence.
  6. Robustness, Equity, and Diagnostic Evidence.
  7. Limitations and Boundary Conditions.
  8. Managerial Insights and Boundary Conditions.
  9. Conclusion.

### Tables and Figures
- **D-10:** The main text's primary table must contain only the formal main
  evidence matrix: the four core behavioral service-design methods over paired
  seeds and scales, reporting `total_vehicle_km`, `vkm_per_served_trip`,
  `vkm_per_original_request`, `served_share`, and paired differences with
  confidence intervals where available.
- **D-11:** Matched-coverage and fixed accepted-set controls should appear as a
  main-text robustness subsection with a compact summary of whether they
  challenge the main efficiency interpretation. Complete rows, failures,
  timeouts, and design details belong in appendix/supplement tables.
- **D-12:** Algorithm diagnostics should be scoped in the main text, but their
  detailed plots and tables should go to appendix/supplement material. ALNS,
  greedy, no-rolling-horizon, and MILP diagnostics must not be used as
  behavioral headline evidence.
- **D-13:** Equity and passenger-type results should appear as a main-text
  trade-off summary, with type-level tables, individual-level burden
  distributions, and sensitivity details in appendix/supplement material.
- **D-14:** Paper-facing tables must not revive ambiguous `vkm_per_trip`
  language. Use the Phase 2/6 metric names and denominators explicitly.

### Managerial Insights and Boundary Conditions
- **D-15:** Rename the old policy section to
  `Managerial Insights and Boundary Conditions`.
- **D-16:** Rewrite the current R1-R5 recommendations as conditional insight
  bullets. Each bullet must state the experiment condition, supported insight,
  applicability boundary, and limitation. Unsupported Phase 8 claims should be
  removed, downgraded, or moved to limitations/future work.
- **D-17:** Beijing/city-density language must be limited to
  `Beijing-inspired synthetic scenario`. Do not imply real Beijing evidence or
  semi-real external validity unless Phase 7 provides it.
- **D-18:** Managerial insights should primarily answer when bidirectional
  meeting-point design is worth considering, using coverage, acceptance,
  efficiency, and equity trade-offs. They should not read as parameter
  prescriptions or city policy recommendations.

### Abstract and Introduction Framing
- **D-19:** The abstract should open with the fair-evidence problem:
  meeting-point DRT may reduce operating distance, but evidence can be
  confounded by passenger response, coverage, and inconsistent baselines.
- **D-20:** The core contribution sentence should frame the paper as providing
  an evidence-chain framework: a choice-aware dynamic service-design simulation
  framework paired with fair comparison, coverage controls, and a claim-evidence
  gate.
- **D-21:** The introduction should use three research questions:
  1. Under fair comparison, whether and when bidirectional meeting-point design
     improves operating efficiency.
  2. How passenger response and coverage change the interpretation of those
     efficiency results.
  3. What equity and managerial boundary conditions follow from the evidence.
- **D-22:** Algorithm diagnostics should not be a standalone research question.
  They are methodological support and diagnostic evidence, not a headline
  manuscript contribution.
- **D-23:** The abstract should close with conditional design guidance and
  boundary conditions, emphasizing synthetic evidence, trade-offs, and limits
  rather than universal policy prescription.

### the agent's Discretion
The planner may choose exact section titles, figure numbering, appendix versus
supplement labels, table captions, and wording templates, provided those choices
preserve the decisions above and remain subordinate to Phase 8 claim-gate
outputs. The planner may also decide whether Phase 9 outputs stay as planning
Markdown artifacts or include direct LaTeX edits, but direct manuscript edits
must not introduce claims unsupported by Phase 8.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project and Phase Definition
- `.planning/ROADMAP.md` - Phase 9 goal, MS-01/MS-02 requirements, success
  criteria, and required outputs.
- `.planning/REQUIREMENTS.md` - Manuscript, claims, metrics, case-study,
  reproducibility, and evidence-gate requirements.
- `.planning/PROJECT.md` - Core value, TR-E rigor, strict phase gates,
  evidence-graded claims, and synthetic-data honesty.
- `.planning/STATE.md` - Current project state and known blockers/concerns.

### Upstream Claim and Evidence Gates
- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_CLAIM_EVIDENCE_MATRIX.md` - Required upstream claim-evidence matrix. Must be read when available before final manuscript wording.
- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_SUPPORTED_CLAIMS.md` - Supported final claims allowed into abstract, introduction, conclusion, and managerial insights.
- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` - Claims to remove, downgrade, or move to limitations.
- `.planning/phases/06-formal-synthetic-experiments/06-CONTEXT.md` - Formal evidence design decisions, main evidence matrix, supplementary package boundaries, and reporting rules.
- `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md` - Expected formal evidence report. Must be read when available before tables/figures are finalized.
- `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07_CASE_STUDY_RESULTS.md` - Expected case-study evidence. Must be read when available before any external-validity or Beijing/city-density language is finalized.

### Prior Phase Contracts
- `.planning/phases/02-experimental-contract-and-metric-standardization/02-CONTEXT.md` - Experiment-family separation, metric denominator rules, and coverage-control handoff.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md` - Behavioral evidence versus supplementary diagnostic boundaries.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_BASELINE_TAXONOMY.md` - Required service-design baseline taxonomy and conceptual labels.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_METRICS_DEFINITIONS.md` - Metric formulas, denominator rules, and forbidden ambiguous metric language.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_COVERAGE_CONFOUNDING_PLAN.md` - Matched-coverage and fixed accepted-set semantics.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_STATISTICAL_PLAN.md` - Paired-seed and confidence-interval discipline.
- `.planning/phases/03-passenger-choice-model-rebuild/03-CONTEXT.md` - Shared actual-offer choice decisions and utility logging requirements.
- `.planning/phases/03-passenger-choice-model-rebuild/03_CHOICE_MODEL_CONTRACT.md` - Choice timing, status semantics, and utility component contract.
- `.planning/phases/03-passenger-choice-model-rebuild/03_PARAMETER_CALIBRATION.md` - Choice parameter, sensitivity, and source-label discipline.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04-CONTEXT.md` - Behavioral baseline, diagnostic role, output schema, and failure-row decisions.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/VARIANT_MAPPING.md` - Historical code labels versus paper-safe concept labels.
- `.planning/phases/05-pilot-experiments/05-CONTEXT.md` - Pilot/formal separation and readiness-only status.
- `.planning/phases/05-pilot-experiments/05_PILOT_RESULTS.md` - Pilot pass state, carry-forward warnings, and readiness caveats.

### Manuscript Source
- `manuscript/main.tex` - Current LaTeX entry point and section include order.
- `manuscript/sections/abstract.tex` - Current abstract text to replace or plan around.
- `manuscript/sections/intro.tex` - Current introduction structure.
- `manuscript/sections/literature.tex` - Current literature review and positioning text.
- `manuscript/sections/model.tex` - Current problem formulation, passenger choice, and three-layer model sections.
- `manuscript/sections/algorithm.tex` - Current solution methodology, MILP diagnostic, and ALNS sections.
- `manuscript/sections/experiments.tex` - Current experiment, sensitivity, equity, welfare, and diagnostic sections.
- `manuscript/sections/policy.tex` - Current policy implications section to rewrite as managerial insights and boundary conditions.
- `manuscript/sections/conclusion.tex` - Current conclusion text.
- `manuscript/references.bib` - Bibliography metadata, including known cleanup needs for prior literature.

### Codebase and Artifact Maps
- `.planning/codebase/CONVENTIONS.md` - Naming, artifact, and style conventions.
- `.planning/codebase/STRUCTURE.md` - Repository/manuscript directory layout and figure/script locations.
- `.planning/codebase/CONCERNS.md` - Known risks: overclaiming, metric ambiguity, gamma/Pareto semantics, Beijing synthetic-data boundary, and generated artifact concerns.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `manuscript/main.tex`: Existing section include order can be rewritten or
  planned without discovering a new manuscript build system.
- `manuscript/sections/*.tex`: Current text is already separated by abstract,
  introduction, literature, model, algorithm, experiments, policy, and
  conclusion, making targeted restructuring feasible.
- `manuscript/figures/` and `manuscript/figures/scripts/`: Existing figure
  assets and scripts can be reclassified into main-text versus
  appendix/supplement roles after Phase 8 determines supported claims.
- `.planning/phases/02-*`, `.planning/phases/04-*`, `.planning/phases/05-*`,
  and `.planning/phases/06-*`: Existing contracts and reports provide the
  evidence-family language that Phase 9 should use in manuscript plans.

### Established Patterns
- Active paper text belongs under `manuscript/sections/`; figure scripts belong
  under `manuscript/figures/scripts/`; generated figures belong under
  `manuscript/figures/`.
- Planning evidence reports live under `.planning/phases/{phase-dir}/` and use
  zero-padded phase prefixes.
- Result evidence and diagnostic evidence must remain separated by evidence
  family, diagnostic role, and denominator vocabulary.
- The project already treats pilot outputs as readiness evidence only and
  formal paired-seed evidence as the source for main claims.

### Integration Points
- Phase 9 should create the roadmap outputs:
  `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_TR_E_MANUSCRIPT_STRUCTURE.md`,
  `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_REVISED_ABSTRACT.md`,
  `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_REVISED_INTRODUCTION_PLAN.md`,
  `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_EXPERIMENT_SECTION_PLAN.md`,
  and `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_TABLE_FIGURE_PLAN.md`.
- If direct LaTeX edits are later scoped, they should touch
  `manuscript/sections/abstract.tex`, `manuscript/sections/intro.tex`,
  `manuscript/sections/experiments.tex`, `manuscript/sections/policy.tex`, and
  possibly `manuscript/main.tex` include order.
- Table/figure planning should reference formal outputs, robustness controls,
  and appendix/supplement allocation instead of copying unsupported historical
  result artifacts.

</code_context>

<specifics>
## Specific Ideas

- Preferred story label: evidence-chain reconstruction.
- Preferred policy section title: `Managerial Insights and Boundary Conditions`.
- Preferred contribution order: evidence discipline, model/framework,
  experimental findings, managerial implications.
- Preferred research questions:
  1. Under fair comparison, whether and when bidirectional meeting-point design
     improves operating efficiency.
  2. How passenger response and coverage affect interpretation of efficiency.
  3. What equity and managerial boundary conditions follow from the evidence.
- Preferred abstract shape:
  1. Open with fair-evidence confounding problem.
  2. State evidence-chain framework contribution.
  3. Summarize claim-gated formal evidence only.
  4. Close with conditional design guidance and boundary conditions.
- Preferred table/figure split: main formal evidence in the main text;
  robustness/equity summaries in the main text with complete detail in
  appendix/supplement; algorithm diagnostics mostly in appendix/supplement.

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within Phase 9 scope.

</deferred>

---

*Phase: 9-Manuscript Restructure for TR Part E*
*Context gathered: 2026-06-16T10:12:31.7906036+08:00*
