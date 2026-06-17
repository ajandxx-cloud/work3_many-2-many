# Phase 4: Tables, Figures, and Numerical Provenance - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md; this log preserves the alternatives considered.

**Date:** 2026-06-17T21:41:43.3623041+08:00
**Phase:** 4-Tables, Figures, and Numerical Provenance
**Areas discussed:** Headline Number Placement, Main Tables And Figure Set, Diagnostic Detail Boundary, Provenance Gate Strictness

---

## Headline Number Placement

| Option | Description | Selected |
|--------|-------------|----------|
| Conservative | Keep abstract, introduction, and conclusion mostly non-numeric; put values in tables/figures/notes. | Yes |
| Balanced | Include one core verified value in abstract or conclusion with trade-off wording. | No |
| Explicit | Include core values and CIs across abstract, introduction, experiments, and conclusion. | No |

**User's choice:** Conservative placement.
**Notes:** Abstract, introduction, conclusion, and implications remain non-numeric.

| Option | Description | Selected |
|--------|-------------|----------|
| Table-first prose | Experiments prose explains direction, conditions, and trade-offs; values stay in tables/figures/notes. | Yes |
| A few prose values | Experiments prose may include one or two core values. | No |
| Full numerical narrative | Experiments prose reports values for every main comparison. | No |

**User's choice:** Table-first prose.
**Notes:** Experiments section should not become a dense numerical narrative.

| Option | Description | Selected |
|--------|-------------|----------|
| Intervals only | Report intervals in tables/notes and avoid significance language. | Yes |
| Directional interval interpretation | Text may state interval direction without significance language. | No |
| Significance language allowed | Use significance wording if bootstrap outputs support it. | No |

**User's choice:** Intervals only.
**Notes:** Avoid "statistically significant" unless a separate supported test exists.

| Option | Description | Selected |
|--------|-------------|----------|
| No concrete numbers | Implications stay interpretive and refer to verified tables/appendix if needed. | Yes |
| A few threshold values | Include selected tested-setting thresholds. | No |
| Full diagnostic values | Include robustness, type, Gamma, and other diagnostic numbers if provenance exists. | No |

**User's choice:** No concrete numbers.
**Notes:** Managerial and operational implications remain operator-facing but non-numeric.

---

## Main Tables And Figure Set

| Option | Description | Selected |
|--------|-------------|----------|
| Formal statistics outputs | Use `experiments/formal_statistics.py` and `results/formal/phase06/` as official table/figure sources. | Yes |
| Refit legacy scripts | Update old manuscript figure scripts to read formal results. | No |
| Dual-track | Use formal outputs and repair old figure scripts where possible. | No |

**User's choice:** Formal statistics outputs.
**Notes:** Legacy result scripts are not official formal evidence sources.

| Option | Description | Selected |
|--------|-------------|----------|
| One table plus one figure | Main manuscript includes one core result table and one core result figure. | Yes |
| One table plus multiple figures | Add robustness or diagnostic overview figures to main text. | No |
| Full package | Include main, diagnostic, robustness, equity/type, Gamma, and MILP table/figure set. | No |

**User's choice:** One main table plus one main figure.
**Notes:** Diagnostic material should not expand the main-text result package.

| Option | Description | Selected |
|--------|-------------|----------|
| Retire legacy result figures | Remove or replace main-text references to old result figures. | Yes |
| Downgrade legacy figures | Keep scripts but relabel as diagnostic/supplemental candidates. | No |
| Rewrite immediately | Rewrite all old result scripts to formal Phase 6 inputs now. | No |

**User's choice:** Retire legacy result figures from the main manuscript.
**Notes:** Scripts may remain for package consistency review unless they are referenced by the main manuscript.

| Option | Description | Selected |
|--------|-------------|----------|
| Generate LaTeX table from formal CSV | Build/transcribe LaTeX table from formal CSV with concise provenance in caption/note. | Yes |
| Supplement CSV only | Keep full table as supplementary CSV, not LaTeX. | No |
| Manual table with ledger check | Hand-write table values after ledger verification. | No |

**User's choice:** Generate or transcribe LaTeX table from formal CSV.
**Notes:** Manual editing is allowed only after formal CSV and ledger checks.

---

## Diagnostic Detail Boundary

| Option | Description | Selected |
|--------|-------------|----------|
| Appendix/supplement diagnostics | Main text keeps qualitative roadmap; diagnostic numbers live outside main narrative. | Yes |
| A few diagnostic values | Main text may include one or two diagnostic values. | No |
| Full diagnostic package | Main text reports diagnostic values broadly. | No |

**User's choice:** Diagnostic numbers mainly appendix/supplement.
**Notes:** Main text should retain evidence-role labels and diagnostic purpose only.

| Option | Description | Selected |
|--------|-------------|----------|
| Name but no values | Main text names matched coverage and fixed accepted set but reports no values. | Yes |
| Matched coverage value | Report one matched-coverage value in main text. | No |
| Both values | Report matched-coverage and fixed-set values in main text. | No |

**User's choice:** Name but do not report values.
**Notes:** Both diagnostics remain roadmap items in main text.

| Option | Description | Selected |
|--------|-------------|----------|
| Passenger-type monitoring only | No main-text Gini or type acceptance rates. | Yes |
| Type ordering | Main text may report which simulated type is more/less likely to accept. | No |
| Full values | Main text may report verified Gini/type rates. | No |

**User's choice:** Passenger-type monitoring only.
**Notes:** Avoid real population equity implications.

| Option | Description | Selected |
|--------|-------------|----------|
| Appendix and avoid Pareto | Gamma detail moves outside main text; avoid Pareto-frontier framing. | Yes |
| Direction only | Main text may report post-hoc Gamma direction. | No |
| Main figure/table | Main text may retain Gamma figure/table if labeled post-hoc. | No |

**User's choice:** Appendix/supplement and avoid Pareto terminology.
**Notes:** Main text keeps only post-hoc accounting boundary language.

| Option | Description | Selected |
|--------|-------------|----------|
| Method limitation only | Main text states fixed-set diagnostic scope and reports no gap values. | Yes |
| Direction-only sentence | Main text may state diagnostic direction without values. | No |
| Appendix table reference | Main text may refer to appendix table while reporting no values. | No |

**User's choice:** Method limitation only.
**Notes:** Do not use MILP gap values in main manuscript.

---

## Provenance Gate Strictness

| Option | Description | Selected |
|--------|-------------|----------|
| Ledger before manuscript | Complete provenance fields before inserting any final LaTeX number. | Yes |
| Tables first | Generate tables first, then backfill ledger. | No |
| Prose claims only | Gate prose claims but rely on CSV provenance for tables. | No |

**User's choice:** Ledger before manuscript.
**Notes:** Claim ledger is the hard gate.

| Option | Description | Selected |
|--------|-------------|----------|
| Formal table wins | Formal Phase 6 tables and validation reports override old values. | Yes |
| Manual conflict review | Pause and ask for each conflict. | No |
| Keep old value | Preserve old value until conflict is explained. | No |

**User's choice:** Formal table wins.
**Notes:** Old values are historical blockers, not source of truth.

| Option | Description | Selected |
|--------|-------------|----------|
| Delete or non-numeric | Remove value or convert to non-numeric wording if provenance is incomplete. | Yes |
| Appendix exploratory | Allow weak-provenance values in appendix with exploratory label. | No |
| Pause and investigate | Stop Phase 4 for missing provenance. | No |

**User's choice:** Delete or non-numeric.
**Notes:** Weak provenance should not enter the formal manuscript.

| Option | Description | Selected |
|--------|-------------|----------|
| Concise traceable notes | Captions/notes include evidence family, denominator, and diagnostic role. | Yes |
| Detailed path and command | Every note includes exact path and generation command. | No |
| Content only | Provenance appears only in ledger. | No |

**User's choice:** Concise traceable notes.
**Notes:** Full paths and commands stay in ledger or provenance appendix/note.

| Option | Description | Selected |
|--------|-------------|----------|
| Manuscript-critical only | Script/code edits limited to table/figure generation and legacy reference cleanup. | Yes |
| Moderate refactor | Refactor formal statistics helpers if useful. | No |
| Avoid scripts | Keep code unchanged and manually convert CSV to LaTeX. | No |

**User's choice:** Only manuscript-critical reproducibility changes.
**Notes:** Avoid broad refactors.

---

## Agent's Discretion

- Downstream agents may choose exact LaTeX formatting, table column order,
  figure placement, and appendix/supplement mechanics while preserving the
  decisions above.

## Deferred Ideas

None.
