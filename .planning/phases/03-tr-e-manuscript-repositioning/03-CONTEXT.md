# Phase 3: TR-E Manuscript Repositioning - Context

**Gathered:** 2026-06-17T20:48:36.4109432+08:00
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 3 rewrites the active manuscript as a Transportation Research Part E
logistics-and-operations contribution. It applies the Phase 2 positioning
lock, claim ledger, and blockers table to manuscript prose, but it does not
finalize evidence-dependent numerical claims.

This phase may revise manuscript metadata, title, abstract, introduction,
literature positioning, model and algorithm scope wording, experiments
narrative, managerial/operational implications, conclusion, and non-numeric
claim wording. It may remove or downgrade unsafe old values and diagnostic
tables from the main text.

This phase must not inject final percentages, confidence intervals,
significance language, final table/figure numbers, or final diagnostic values
before Phase 4 verifies provenance. It must not rerun formal experiments,
manually edit result numbers, or broaden the manuscript into real Beijing
validation, endogenous Gamma behavior, or a full exact dynamic MILP benchmark.

</domain>

<decisions>
## Implementation Decisions

### Title, Abstract, And Introduction Frame

- **D-01:** The manuscript's primary identity should be
  TR-E logistics/operations evidence for bidirectional meeting-point DRT
  service design. It should not be framed primarily as policy validation,
  a deployable decision tool, or optimization-method supremacy.
- **D-02:** The core title/abstract noun phrase should be
  `bidirectional meeting-point DRT service design`. Passenger response should
  appear as the mechanism in subtitle, abstract, and contribution wording, but
  should not dominate the title in a way that makes the paper read as a method
  paper.
- **D-03:** Old numerical values in the abstract and introduction should be
  replaced with non-numeric conditional statements. Phase 3 should not use
  final percentages or Phase 4 placeholders in the abstract/introduction by
  default.
- **D-04:** The introduction contribution structure should become three
  contribution paragraphs, not the current bullet-style list. The three
  paragraphs should cover: the service-design problem, the
  passenger-response-aware simulation mechanism, and evidence-bounded
  operational trade-offs.

### Experiments Evidence-Layering Structure

- **D-05:** The experiments main text should keep only the core experiments
  and move diagnostics substantially to appendix or supplement.
- **D-06:** The main text should retain only one diagnostic roadmap paragraph.
  That paragraph should identify diagnostic evidence roles but should not
  include diagnostic numerical values.
- **D-07:** The main experimental narrative should focus on routing intensity,
  served share, and rejection decomposition: vehicle-km per served trip,
  vehicle-km per original request, served share, choice rejection, and
  feasibility rejection.
- **D-08:** Phase 3 should delete or comment out old diagnostic tables in the
  experiments main text, retaining only the core main-table position. Diagnostic
  tables may move to appendix/supplement or be decided in Phase 4.

### Managerial And Operational Implications

- **D-09:** The current `Policy Implications` section should be renamed and
  rewritten as `Managerial and Operational Implications`.
- **D-10:** The section should retain four to five operator-facing
  service-design themes, but should not present them as policy recommendations.
- **D-11:** The implication themes should be organized by service-design
  decisions: walking tolerance, fleet deployment, consolidation trade-off,
  passenger-segment monitoring, and validation limits.
- **D-12:** Chinese urban/suburban context may be weakly retained only as
  `tested synthetic Chinese-suburban-inspired conditions` or equivalent
  synthetic/tested-condition wording. It must not be presented as real-world
  Chinese deployment validation.
- **D-13:** Prescriptive R1-R5 recommendation sentences should be converted
  into bounded design considerations. Retain operator-facing usefulness, but
  downgrade `should` language where it implies policy prescription or a
  decision tool.

### Boundary Wording For Diagnostics And Sensitive Evidence

- **D-14:** Gamma/Pareto content should be downgraded to appendix/supplement
  post-hoc sensitivity accounting. The main text should only state that Gamma
  does not affect routing, offer generation, or acceptance.
- **D-15:** The Beijing-inspired scenario should be treated as a robustness or
  sensitivity setting, in appendix/supplement or with only weak main-text
  reference. It must be labeled `Beijing-inspired synthetic grid` or
  `semi-realistic synthetic grid` and must not be treated as real-world
  validation.
- **D-16:** MILP/ALNS optimality-gap material should be downgraded to an
  algorithm diagnostic appendix. The main text should state that the MILP is a
  simplified ex-post diagnostic over fixed accepted sets and should not include
  gap tables or gap values.
- **D-17:** Equity/passenger-type heterogeneity should be treated as a
  passenger-segment monitoring implication. The experiment includes simulated
  passenger types and validated `equity_type_outcomes` diagnostics, but the
  manuscript should not claim real population equity validation or report final
  Gini/type-acceptance values in the main text before Phase 4.

### Agent Discretion

- Downstream agents may choose exact prose, section order, and LaTeX mechanics
  as long as the decisions above and the Phase 2 evidence-role boundaries are
  preserved.
- Downstream agents may decide whether moved diagnostic material becomes a
  formal appendix section, supplement placeholder, or Phase 4 handoff note, but
  diagnostic numerical values must not remain in the Phase 3 main-text
  headline narrative.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Planning Source Of Truth

- `.planning/PROJECT.md` - Project goal, evidence boundary, target journal,
  constraints, and key decisions.
- `.planning/REQUIREMENTS.md` - Phase 3 requirements and phase-to-requirement
  mapping.
- `.planning/ROADMAP.md` - Phase 3 goal, success criteria, and plan list.
- `.planning/STATE.md` - Current workflow state and accumulated decisions.
- `.planning/phases/01-evidence-foundation-and-milestone-setup/01-CONTEXT.md`
  - Prior evidence-foundation decisions and canonical reference inventory.
- `.planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md`
  - Prior positioning, claim-ledger, blocker, and wording-boundary decisions.

### Milestone Controls

- `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md` -
  Allowed TR-E framing, prohibited framing, core contribution lock, evidence
  role boundaries, and safe sentences.
- `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` - Occurrence-level
  manuscript claim ledger with allowed/prohibited sentences, evidence roles,
  provenance fields, and Phase 4 numerical-gate status.
- `.planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md` -
  Manuscript file actions, evidence-role boundaries, scan families, and phase
  handoff rules.
- `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` -
  Blocker families, safe claim families, prohibited wording, owner phases, and
  verification checks.

### Codebase Maps

- `.planning/codebase/CONVENTIONS.md` - Repository naming, style, LaTeX/source
  conventions, and artifact conventions.
- `.planning/codebase/STRUCTURE.md` - Canonical locations for manuscript,
  formal evidence, source code, experiments, results, and planning artifacts.

### Active Manuscript Sources

- `manuscript/main.tex` - Journal metadata, title, notation, section includes,
  and appendix entry point.
- `manuscript/sections/abstract.tex` - Abstract rewrite target; old numerical
  headline and policy/equity wording must be removed or made non-numeric.
- `manuscript/sections/intro.tex` - Introduction and contribution-frame rewrite
  target; old bullet contributions should become three contribution paragraphs.
- `manuscript/sections/literature.tex` - TR-E logistics/operations literature
  positioning target.
- `manuscript/sections/model.tex` - Binary-logit response, passenger-type,
  meeting-point semantics, and Gamma post-hoc wording target.
- `manuscript/sections/algorithm.tex` - Rolling-horizon heuristic and MILP
  diagnostic-scope wording target.
- `manuscript/sections/experiments.tex` - Core evidence narrative, diagnostics
  demotion, denominator/rejection narrative, and old table cleanup target.
- `manuscript/sections/policy.tex` - Rename/rewrite target for managerial and
  operational implications.
- `manuscript/sections/conclusion.tex` - Conditional contribution, evidence
  boundary, limitations, and future-work rewrite target.
- `manuscript/references.bib` - Bibliography source if TR-E logistics and
  operations citations need adjustment.

### Formal Evidence And Diagnostics

- `results/formal/phase06/phase06_result_manifest.json` - Formal result
  manifest and evidence package inventory.
- `results/formal/phase06/phase06_verification_report.json` - Formal Phase 6
  verification summary.
- `results/formal/phase06/main_behavioral/validation_report.json` - Main
  behavioral validation report.
- `results/formal/phase06/tables/main_behavioral_table.csv` - Core main-table
  source for Phase 4, not a Phase 3 final-number source.
- `results/formal/phase06/tables/paired_differences.csv` - Paired comparison
  source for Phase 4 numerical provenance.
- `results/formal/phase06/tables/paired_bootstrap_ci.csv` - Bootstrap interval
  source for Phase 4 numerical provenance.
- `results/formal/phase06/tables/equity_type_summary.csv` - Passenger-type
  heterogeneity diagnostic source; use only for monitoring implications unless
  Phase 4 verifies stronger wording.
- `results/formal/phase06/coverage_controls/matched_coverage/validation_report.json`
  - Matched-coverage diagnostic validation; diagnostic only.
- `results/formal/phase06/coverage_controls/fixed_accepted_set/validation_report.json`
  - Fixed-accepted-set diagnostic validation; diagnostic only.
- `results/formal/phase06/robustness/validation_report.json` - Robustness
  package validation summary.
- `results/formal/phase06/robustness/equity_type_outcomes/validation_report.json`
  - Equity/passenger-type diagnostic validation; confirms structural validity
  of type-level and individual-burden rows.
- `results/formal/phase06/robustness/equity_type_outcomes/config_manifest.json`
  - Confirms passenger-type parameters are simulation-range constructs.
- `results/formal/phase06/robustness/equity_type_outcomes/equity_summary.json`
  - Confirms equity claims are exploratory and individual burden summaries are
  diagnostic.
- `results/formal/phase06/robustness/algorithm_diagnostics/validation_report.json`
  - Algorithm diagnostic validation; not ALNS near-optimality proof.

### Generation And Validation Scripts

- `experiments/formal_statistics.py` - Formal table, plot, manifest, report,
  and synthesis generator.
- `experiments/phase06_formal.py` - Formal main behavioral runner, manifest,
  and validation entry point.
- `experiments/formal_validation.py` - Formal validation helpers and
  denominator checks.
- `experiments/phase06_coverage_controls.py` - Matched-coverage and
  fixed-accepted-set diagnostic controls.
- `experiments/phase06_robustness.py` - Robustness, equity/passenger-type, and
  algorithm diagnostic packages.
- `src/drt/types.py` - Passenger type definitions and simulation parameter
  constructs.
- `src/drt/choice.py` - Passenger-type assignment and binary-logit acceptance
  evaluation.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets

- `03_CLAIM_LEDGER.md`: Provides claim IDs, manuscript locations,
  allowed/prohibited sentences, evidence roles, and Phase 4 numerical-gate
  status. Phase 3 should use it as an execution queue for prose replacement and
  deletion.
- `05_BLOCKERS_AND_SAFE_CLAIMS.md`: Provides concrete blocker hits for old
  values, TR-A wording, policy-first wording, dominance/outperform language,
  Gamma/Pareto, Beijing, MILP, diagnostics, and equity/type claims.
- `manuscript/main.tex`: Already contains an appendix entry point, so diagnostic
  demotion to appendix/supplement is structurally feasible.
- `results/formal/phase06/robustness/equity_type_outcomes/*`: Confirms the
  experiment includes simulated passenger-type diagnostics, but the config
  limits them to simulation-range constructs rather than empirical equity
  validation.

### Established Patterns

- Active manuscript source is `manuscript/main.tex` plus
  `manuscript/sections/*.tex`; archive and old paper paths are not active
  manuscript source.
- Formal claims must trace to `results/formal/phase06/`; root legacy results,
  smoke outputs, archives, pilot outputs, and ad hoc outputs are non-canonical
  by default.
- Phase 3 may change non-numeric wording and structure, but Phase 4 owns final
  numerical injection, table/figure refresh, denominator reconciliation, and
  value provenance.
- Diagnostic evidence must carry explicit diagnostic qualifiers and must not be
  promoted into the primary behavioral headline.

### Integration Points

- `manuscript/sections/abstract.tex` and `manuscript/sections/intro.tex` should
  consume the service-design-evidence identity and non-numeric contribution
  wording.
- `manuscript/sections/experiments.tex` should consume the core-evidence-only
  main-text structure, diagnostic roadmap paragraph, and table demotion
  decisions.
- `manuscript/sections/policy.tex` should become managerial/operational
  implications organized by service-design decisions.
- `manuscript/sections/conclusion.tex` should restate conditional contribution,
  evidence boundaries, diagnostics, limitations, and future work without old
  headline values.

</code_context>

<specifics>
## Specific Ideas

- Use `bidirectional meeting-point DRT service design` as the manuscript's
  primary title/abstract concept.
- Use `passenger-response-aware simulation` as a mechanism phrase, not as the
  paper's dominant identity.
- Replace final values in abstract and introduction with conditional,
  non-numeric wording rather than Phase 4 placeholders by default.
- Use three contribution paragraphs in the introduction: service design,
  passenger-response-aware simulation, and evidence-bounded trade-offs.
- Keep the main experiments narrative to routing intensity, served share, and
  rejection decomposition.
- Keep only one main-text diagnostic roadmap paragraph and move diagnostic
  details to appendix/supplement or Phase 4 handoff.
- Convert policy recommendations into bounded design considerations under
  managerial and operational implications.
- Treat passenger-type results as monitoring implications only, not real
  population equity conclusions.

</specifics>

<deferred>
## Deferred Ideas

None - discussion stayed within Phase 3 scope.

</deferred>

---

*Phase: 3-TR-E Manuscript Repositioning*
*Context gathered: 2026-06-17T20:48:36.4109432+08:00*
