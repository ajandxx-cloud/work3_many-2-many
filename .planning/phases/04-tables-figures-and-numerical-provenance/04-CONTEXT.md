# Phase 4: Tables, Figures, and Numerical Provenance - Context

**Gathered:** 2026-06-17T21:41:43.3623041+08:00
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 4 refreshes manuscript-ready tables and figures from validated formal
Phase 6 evidence, reconciles all reported values against the claim ledger, and
injects only verified final numerical content into the active manuscript.

This phase owns the numerical gate deferred by Phase 3. It may update
`03_CLAIM_LEDGER.md`, generate or refresh LaTeX tables and result figures from
formal Phase 6 CSV/JSON artifacts, clean manuscript references to legacy result
figures, and insert verified table/figure references in `manuscript/`.

This phase must not rerun full formal experiments by default, manually edit
result numbers, promote diagnostic evidence into headline findings, or broaden
claims into real Beijing validation, endogenous Gamma behavior, policy control,
or ALNS near-optimality. Code/script edits are allowed only when manuscript
critical for reproducible table/figure generation, formal CSV-to-LaTeX
conversion, or legacy figure reference cleanup.

</domain>

<decisions>
## Implementation Decisions

### Headline Number Placement

- **D-01:** Abstract, introduction, conclusion, and managerial/operational
  implications should remain non-numeric. They may state conditional findings,
  evidence roles, and trade-offs, but should not contain final percentages,
  confidence intervals, or headline improvement values.
- **D-02:** The experiments prose should be table-first. It should explain
  direction, conditions, denominator meaning, and coverage/passenger-response
  trade-offs; concrete values should live in the main table, main figure,
  table notes, figure notes, appendix, supplement, or provenance artifacts.
- **D-03:** Bootstrap intervals or uncertainty ranges may be reported in tables
  or table notes, but Phase 4 should not introduce significance language such
  as "statistically significant" unless a separate supported test workflow is
  implemented and verified.
- **D-04:** Managerial and operational implications should not repeat concrete
  numerical values. They should remain operator-facing interpretations and may
  refer readers to verified tables or appendix material where needed.

### Main Tables And Figure Set

- **D-05:** Formal statistics outputs are the official source for manuscript
  tables and result figures. Phase 4 should use `experiments/formal_statistics.py`
  and `results/formal/phase06/` outputs as the formal provenance path.
- **D-06:** The main manuscript should contain one core result table and one
  core result figure. Additional diagnostic, robustness, equity/type, Gamma,
  Beijing-inspired, and MILP details should not expand the main-text result
  package.
- **D-07:** Legacy result figure scripts such as `fig04_baseline_comparison.py`,
  `fig05_sensitivity.py`, `fig06_policy_map.py`, and `fig07_pareto.py` should
  exit the main manuscript result narrative unless they are rewritten from
  formal Phase 6 sources. Existing main-text references to legacy result figures
  should be removed or replaced by formal outputs.
- **D-08:** The formal manuscript table should be generated or transcribed from
  formal CSV sources into LaTeX, with caption or note provenance. Manual table
  values are allowed only when each value is checked against the formal CSV and
  claim ledger before insertion.

### Diagnostic Detail Boundary

- **D-09:** Diagnostic numerical details should live mainly in appendix or
  supplement. The main text should keep a qualitative diagnostic roadmap with
  explicit evidence-role labels.
- **D-10:** Matched-coverage and fixed-accepted-set diagnostics may be named in
  the main text, but their numerical values should not be reported there. They
  should remain diagnostic coverage-confounding and fixed-set decomposition
  evidence.
- **D-11:** Equity/type heterogeneity should be framed only as simulated
  passenger-type monitoring. The main text should not report Gini values,
  passenger-type acceptance rates, or real population equity conclusions.
- **D-12:** Gamma numerical detail should be appendix/supplement material.
  The main text should avoid Pareto-frontier framing and retain only the
  boundary that Gamma is post-hoc welfare or sensitivity accounting and does
  not affect routing, offer generation, or acceptance.
- **D-13:** MILP and algorithm diagnostics should remain method-scope or
  limitation wording in the main text. The main manuscript should not report
  MILP gap values or imply near-optimality.

### Provenance Gate Strictness

- **D-14:** Phase 4 must be ledger-first, manuscript-second. No final number
  should enter LaTeX until the claim ledger has complete provenance fields for
  the occurrence or table/figure claim: `source_path`, `script_path`,
  `generation_command`, `metric_formula`, `numerator`, `denominator`,
  `evidence_role`, `allowed_sentence`, and `prohibited_sentence`.
- **D-15:** When formal Phase 6 tables or validation reports conflict with old
  manuscript values or old ledger `reported_value` entries, formal Phase 6 wins.
  Old values remain historical blockers or prior reported values only.
- **D-16:** If a desired numerical claim lacks complete provenance, Phase 4
  should delete the numerical claim or convert it to non-numeric conditional
  wording. Weak-provenance values should not enter the main manuscript as
  exploratory numbers.
- **D-17:** Captions and notes should be concise but traceable. They should
  identify the evidence family, denominator, and diagnostic role where relevant;
  full paths, commands, formulas, and allowed/prohibited wording should live in
  the claim ledger or a provenance appendix/note.
- **D-18:** Code or script changes should be limited to manuscript-critical
  reproducibility: formal table/figure generation, formal CSV-to-LaTeX
  conversion, and cleanup of legacy figure references. Avoid broad refactors.

### Agent Discretion

- Downstream agents may choose exact LaTeX formatting, table column order,
  figure placement, and whether appendix/supplement content is represented as
  LaTeX appendix tables, supplementary CSV references, or provenance notes, as
  long as the decisions above are preserved.
- Downstream agents may decide whether a specific diagnostic artifact is
  omitted entirely or moved to appendix/supplement, but it must not become a
  main-text numerical headline.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Planning Source Of Truth

- `.planning/PROJECT.md` - Project goal, evidence boundary, TR-E target,
  constraints, and key decisions.
- `.planning/REQUIREMENTS.md` - Phase 4 requirements TFIG-01 through TFIG-06
  and verification dependencies.
- `.planning/ROADMAP.md` - Phase 4 goal, success criteria, and plan list.
- `.planning/STATE.md` - Current workflow state and accumulated decisions.
- `.planning/phases/01-evidence-foundation-and-milestone-setup/01-CONTEXT.md`
  - Evidence-foundation decisions and canonical evidence inventory.
- `.planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md`
  - Claim ledger, evidence-role, blocker, and safe wording decisions.
- `.planning/phases/03-tr-e-manuscript-repositioning/03-CONTEXT.md` -
  Manuscript repositioning decisions and Phase 4 numerical handoff.

### Milestone Controls

- `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` - Phase gates,
  evidence boundary, do-not-before-gate rules, and readiness rules.
- `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md` -
  Canonical manuscript/evidence audit and non-canonical source rules.
- `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md` -
  Allowed TR-E framing, prohibited framing, core contribution lock, and safe
  sentences.
- `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` - Occurrence-level
  claim ledger and mandatory provenance schema; Phase 4 execution queue.
- `.planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md` -
  Manuscript actions, evidence-role boundaries, and phase handoff rules.
- `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` -
  Old-number blockers, diagnostic role boundaries, and package consistency risks.

### Codebase Maps

- `.planning/codebase/STRUCTURE.md` - Canonical locations for manuscript,
  formal evidence, figure scripts, source code, and generated artifacts.
- `.planning/codebase/STACK.md` - Python/LaTeX/table/figure dependencies and
  pandas/matplotlib reproducibility risks.
- `.planning/codebase/ARCHITECTURE.md` - Formal statistics, results, plots, and
  manuscript publication data flow.
- `.planning/codebase/CONVENTIONS.md` - Repository style, artifact, and
  generated-file conventions.

### Active Manuscript Sources

- `manuscript/main.tex` - Master manuscript file, journal metadata, includes,
  figure/table references, and appendix entry point.
- `manuscript/sections/abstract.tex` - Should remain non-numeric under Phase 4
  decisions.
- `manuscript/sections/intro.tex` - Should remain non-numeric under Phase 4
  decisions.
- `manuscript/sections/experiments.tex` - Primary Phase 4 integration target
  for main table, main figure, denominator notes, and diagnostic roadmap.
- `manuscript/sections/policy.tex` - Managerial and operational implications;
  no concrete Phase 4 numbers.
- `manuscript/sections/conclusion.tex` - Should remain non-numeric and
  boundary-focused.
- `manuscript/references.bib` - Bibliography source if table/figure or
  appendix wording requires citation adjustments.

### Formal Phase 6 Evidence

- `results/formal/phase06/phase06_result_manifest.json` - Formal package
  inventory and smoke exclusion status.
- `results/formal/phase06/phase06_verification_report.json` - Formal Phase 6
  verification summary.
- `results/formal/phase06/main_behavioral/raw_results.csv` - Main behavioral
  raw results.
- `results/formal/phase06/main_behavioral/processed_results.csv` - Main
  behavioral processed results.
- `results/formal/phase06/main_behavioral/metrics_table.csv` - Main behavioral
  aggregate metrics.
- `results/formal/phase06/main_behavioral/validation_report.json` - Main
  behavioral validation report.
- `results/formal/phase06/tables/main_behavioral_table.csv` - Main manuscript
  table source.
- `results/formal/phase06/tables/paired_differences.csv` - Paired comparison
  source.
- `results/formal/phase06/tables/paired_bootstrap_ci.csv` - Bootstrap interval
  source for table notes only; not significance language.
- `results/formal/phase06/tables/matched_coverage_paired_differences.csv` -
  Matched-coverage diagnostic source; appendix/supplement numerical use.
- `results/formal/phase06/tables/fixed_accepted_set_paired_differences.csv` -
  Fixed-accepted-set diagnostic source; appendix/supplement numerical use.
- `results/formal/phase06/tables/robustness_setting_summary.csv` - Robustness
  source; not main-text numerical headline.
- `results/formal/phase06/tables/equity_type_summary.csv` - Simulated
  passenger-type heterogeneity source; monitoring/appendix only.
- `results/formal/phase06/tables/supplementary_summary.csv` - Supplementary
  diagnostics and sensitivity source.
- `results/formal/phase06/tables/critical_conflicts.csv` - Formal synthesis
  conflict ledger, if populated.
- `results/formal/phase06/tables/final_synthesis_validation.json` - Final
  synthesis validation status.
- `results/formal/phase06/plots/phase06_main_efficiency_coverage.png` - Formal
  main plot candidate.
- `results/formal/phase06/plots/plot_metadata.json` - Plot source metadata.
- `results/formal/phase06/coverage_controls/matched_coverage/validation_report.json`
  - Matched-coverage diagnostic validation.
- `results/formal/phase06/coverage_controls/fixed_accepted_set/validation_report.json`
  - Fixed-accepted-set diagnostic validation.
- `results/formal/phase06/robustness/validation_report.json` - Robustness
  package validation.
- `results/formal/phase06/robustness/equity_type_outcomes/validation_report.json`
  - Equity/type outcome validation.
- `results/formal/phase06/robustness/algorithm_diagnostics/validation_report.json`
  - Algorithm diagnostic validation.

### Generation And Figure Scripts

- `experiments/formal_statistics.py` - Official formal table, plot, manifest,
  verification, and synthesis generator for Phase 4.
- `experiments/formal_validation.py` - Formal denominator and validation helper.
- `experiments/phase06_formal.py` - Formal main package runner and validation
  entry point.
- `experiments/phase06_coverage_controls.py` - Matched-coverage and fixed-set
  diagnostic control package.
- `experiments/phase06_robustness.py` - Robustness, equity/type, Gamma, and
  algorithm diagnostic packages.
- `manuscript/figures/scripts/fig04_baseline_comparison.py` - Legacy result
  figure script; do not use as formal main figure unless rewritten from formal
  Phase 6 sources.
- `manuscript/figures/scripts/fig05_sensitivity.py` - Legacy sensitivity
  figure script; not a main formal source under Phase 4 decisions.
- `manuscript/figures/scripts/fig06_policy_map.py` - Legacy policy-map script;
  not a main formal source under Phase 4 decisions.
- `manuscript/figures/scripts/fig07_pareto.py` - Legacy Pareto/Gamma script;
  avoid main-text Pareto framing.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets

- `experiments/formal_statistics.py`: Primary reusable generator for formal
  tables, plots, manifests, verification reports, and synthesis validation. It
  already reads from `results/formal/phase06/` and writes the formal table and
  plot artifacts Phase 4 should prefer.
- `results/formal/phase06/tables/*.csv`: Existing formal table sources for main
  behavioral evidence, paired differences, bootstrap intervals, diagnostics,
  robustness, equity/type, and supplementary summaries.
- `results/formal/phase06/plots/phase06_main_efficiency_coverage.png`: Existing
  formal main result plot candidate for the one-main-figure strategy.
- `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md`: Existing
  occurrence-level execution queue. It already encodes source paths, formulas,
  denominators, evidence roles, allowed sentences, prohibited sentences, and
  Phase 4 statuses.
- `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md`:
  Existing blocker and safe-claim table for old values, diagnostic promotion,
  legacy result paths, Gamma/Pareto, Beijing, MILP, and package consistency.

### Established Patterns

- Active manuscript source is `manuscript/main.tex` plus
  `manuscript/sections/*.tex`; archive and root legacy result files are not
  formal manuscript evidence.
- Generated evidence and manuscript figures live under `results/` and
  `manuscript/figures/`; figure scripts should be plotting-focused and should
  not recompute simulations.
- Formal claims must trace to `results/formal/phase06/`; root legacy CSVs,
  smoke outputs, pilot outputs, archive outputs, and ad hoc outputs remain
  non-canonical by default.
- Phase 3 intentionally left abstract, introduction, experiments, implications,
  and conclusion non-numeric. Phase 4 may inject verified values only according
  to the conservative placement decisions above.
- Existing result figure scripts include legacy-path risks. Formal result
  figures should come from the formal statistics workflow unless a legacy script
  is deliberately rewritten and revalidated.

### Integration Points

- `manuscript/sections/experiments.tex`: Main Phase 4 manuscript target for the
  core formal table, formal figure, table-first narrative, denominator labels,
  and diagnostic roadmap.
- `manuscript/main.tex`: Must include any final table/figure labels and ensure
  legacy result figure references are not left in the main manuscript.
- `03_CLAIM_LEDGER.md`: Must be checked or updated before any final numeric
  LaTeX insertion.
- `experiments/formal_statistics.py`: Preferred location for any
  manuscript-critical table/plot generation changes or CSV-to-LaTeX generation
  helpers if needed.

</code_context>

<specifics>
## Specific Ideas

- Keep the front of the paper numerically restrained: the abstract,
  introduction, conclusion, and implications should carry the conditional
  finding, not the final percentages.
- Use one main manuscript table and one main manuscript figure.
- Use formal Phase 6 table/plot outputs as the official result presentation.
- Move diagnostic numerical values to appendix/supplement or leave them out of
  the main manuscript.
- Treat missing provenance as a reason to remove or de-numericize a claim, not
  as a reason to weaken the provenance standard.

</specifics>

<deferred>
## Deferred Ideas

None - discussion stayed within Phase 4 scope.

</deferred>

---

*Phase: 4-Tables, Figures, and Numerical Provenance*
*Context gathered: 2026-06-17T21:41:43.3623041+08:00*
