# Phase 09 Table, Figure, Limitations, and Managerial Insights Plan

**Artifact:** `09_TABLE_FIGURE_PLAN.md`  
**Purpose:** Assign manuscript displays to evidence roles and convert the
current policy section into bounded, limitations-first managerial insight.

## Current Display Inventory

Current experiment and policy display labels visible in `experiments.tex` and
`policy.tex` are assigned below. Each target role uses one of: `keep main`,
`revise main`, `move appendix/supplement`, or `remove/replace`.

| Label | Current display | Evidence family | Target role | Required revision |
|---|---|---|---|---|
| `tab:variants` | Legacy six-variant definition table | Design/context | revise main | Replace legacy variant names with the approved four-method behavioral taxonomy plus clearly separated diagnostics. |
| `tab:main-results` | Legacy main results table | Formal behavioral evidence | remove/replace | Replace with Phase 6/8-supported formal main-evidence table; no legacy values. |
| `tab:milp-gap` | MILP vs ALNS optimality gap | Algorithm diagnostic | move appendix/supplement | Keep only scoped diagnostic summary in main text if Phase 8 permits. |
| `fig:baseline-comparison` | Baseline comparison bar chart | Legacy formal/diagnostic mix | remove/replace | Replace from reproducible Phase 6 data and approved method/metric contract. |
| `tab:matched-coverage` | Exploratory matched-coverage diagnostic | Robustness control | revise main | Convert to compact robustness summary with full design/table in appendix or supplement. |
| `tab:result-provenance` | Provenance of legacy efficiency numbers | Provenance | revise main | Replace with Phase 6/8 provenance and claim-support status. |
| `tab:beijing-results` | Beijing-inspired synthetic grid results | Synthetic boundary/case stress test | move appendix/supplement | Summarize in main text only as `Beijing-inspired synthetic scenario` if Phase 8 supports. |
| `fig:sensitivity` | Walking tolerance and fleet-size sensitivity | Robustness/managerial boundary | revise main | Rebuild with supported axes, captions, and boundary language. |
| `tab:pareto` | Gamma welfare sensitivity table | Diagnostic welfare accounting | move appendix/supplement | Do not call this a Pareto frontier unless gamma affects decisions. |
| `fig:pareto` | Gamma welfare figure | Diagnostic welfare accounting | move appendix/supplement | Retitle as gamma sensitivity or remove if Phase 8 does not support. |
| `tab:weight-sensitivity` | Weight sensitivity table | Diagnostic/robustness | move appendix/supplement | Main text may contain only a bounded summary if Phase 8 promotes it. |
| `fig:policy-map` | Policy deployment map | Managerial insight/decision aid | remove/replace | Replace prescriptive tier map with bounded insight template or appendix-only scenario visualization. |
| `tab:vot-mapping` | Value-of-time mapping table | Calibration limitation | move appendix/supplement | Keep as parameter interpretation and calibration caveat, not policy evidence. |

Figure scripts under `manuscript/figures/scripts/` are reproducible script
assets, but several current scripts encode legacy titles, labels, or numeric
annotations. They must be regenerated after Phase 6 formal outputs and Phase 8
claim support are available.

## Target Main-Text Displays

The revised manuscript should keep the main text lean and evidence ordered.

| Proposed display | Target role | Evidence gate |
|---|---|---|
| Design and method taxonomy table | keep main | Must use approved method labels and diagnostic separation. |
| Formal main-evidence table | revise main | Requires complete Phase 6 formal matrix and Phase 8 supported claim status. |
| Paired-difference summary table or compact panel | revise main | Requires paired differences, confidence intervals, and `n_pairs`. |
| Robustness summary table | revise main | Covers matched coverage and fixed accepted-set controls at summary level only. |
| Equity trade-off summary | revise main | Reports bounded type-level trade-offs without universal policy claims. |
| Managerial insight table | revise main | Uses condition, insight placeholder, boundary, limitation, and Phase 8 support status. |

Main-text figures should be limited to displays that directly support the
evidence chain. Candidate main figures are a system/design schematic, a formal
paired-evidence figure if Phase 6/8 support exists, and a sensitivity or
managerial-boundary figure only if it is clearly bounded.

## Appendix and Supplement Displays

Appendix or supplement material should carry the detail needed for
reproducibility without crowding the main argument:

| Display family | Target role | Required detail |
|---|---|---|
| Full matched-coverage tables | move appendix/supplement | Target served-share cap, tolerance, achieved shares, failure rows, and paired metrics. |
| Full fixed accepted-set diagnostics | move appendix/supplement | Construction rule, retained set, retained share, failures, and routing metrics. |
| Algorithm diagnostics | move appendix/supplement | ALNS, greedy, no-rolling-horizon, no-choice, and MILP assumptions/statuses. |
| Gamma welfare accounting | move appendix/supplement | Full sweep and statement that gamma is post-hoc unless implementation changes. |
| Weight sensitivity | move appendix/supplement | Full grid, provenance, metrics, and Phase 8 support status. |
| Beijing-inspired synthetic scenario tables | move appendix/supplement | Scenario definition, synthetic boundary, and formal claim status. |
| Value-of-time mapping and calibration caveats | move appendix/supplement | Parameter source, interpretation, and calibration limitation. |

## Main Table Contract

The primary table must contain only the formal main-evidence matrix and must be
generated after Phase 6 formal outputs and Phase 8 claim support are available.
It must not contain diagnostic methods, pilot values, or legacy manuscript
numbers.

Required columns:

| Column | Requirement |
|---|---|
| `method` | One of the four approved behavioral method labels. |
| `scenario_key` or `scale` | Paired scenario or request-scale key. |
| `n_pairs` | Number of valid paired comparisons after failed/timeout rows are accounted for. |
| `total_vehicle_km` | Total vehicle distance for the method/scenario. |
| `vkm_per_served_trip` | Distance normalized by served requests. |
| `vkm_per_original_request` | Distance normalized by original requests. |
| `served_share` | Served requests divided by original requests. |
| paired difference | Within-pair method difference against the declared reference method. |
| confidence interval | 95% confidence interval for the paired difference, with method documented. |
| Phase 8 support status | Supported, bounded, downgraded, or unsupported claim status. |

Any table note must state the pairing unit, confidence-interval method,
handling of missing/failed/timeout rows, and the relationship between coverage
and efficiency.

## Main Figure Contract

Main-text figures must be generated from reproducible scripts/data rather than
AI-created artwork. Schematic figures are allowed only when their source script
or editable source is committed and their caption identifies the figure as a
conceptual schematic rather than empirical evidence.

Rules for main figures:

- Use Phase 6/8-supported data files for empirical displays.
- Keep script paths, data paths, and output filenames documented.
- Remove hard-coded legacy numerical annotations before final manuscript use.
- Do not present diagnostics as formal evidence by color, title, ordering, or
  caption phrasing.
- Regenerate figures after any Phase 8 claim downgrade.

## Caption and Vocabulary Checklist

Before a table or figure enters the revised manuscript, its caption and notes
must pass this checklist:

- Forbid `vkm_per_trip`; use `vkm_per_served_trip` or
  `vkm_per_original_request`.
- Forbid unsupported `Pareto frontier` language for the post-hoc gamma sweep.
  Use gamma sensitivity or welfare-accounting diagnostic unless gamma affects
  decisions in the model and Phase 8 supports the claim.
- Forbid real-Beijing wording unless Phase 7 supplies real or semi-real case
  evidence and Phase 8 supports the case claim.
- Use `Beijing-inspired synthetic scenario` for current Beijing-related
  displays.
- State whether each display is formal evidence, robustness evidence,
  diagnostic evidence, synthetic-boundary evidence, or appendix/supplement
  detail.
- Include denominator definitions whenever vehicle-km, served share, acceptance,
  rejection, wait, walk, or IVT values appear.
- State Phase 8 support status for any caption that implies a substantive
  finding.
