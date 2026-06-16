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
