---
phase: 01-problem-formulation-model-structure
plan: "03"
subsystem: choice-model
tags: [MNL, passenger-choice, outside-option, heterogeneity, latex]
dependency_graph:
  requires: []
  provides: [MNL-utility, outside-option, passenger-heterogeneity, choice-probability, acceptance-probability]
  affects: [model/model.tex, Phase-2-simulation, Phase-3-calibration]
tech_stack:
  added: []
  patterns: [MNL-logit, random-utility-model, Bernoulli-acceptance]
key_files:
  created:
    - model/choice-model.tex
  modified: []
decisions:
  - "beta_0^k set to 0 (outside option normalized as reference alternative)"
  - "Three passenger types named: price-sensitive, time-sensitive, walk-sensitive"
  - "Baseline beta values flagged as provisional pending Work 1/2 calibration"
metrics:
  duration: ~10min
  completed: "2026-04-11"
---

# Phase 1 Plan 03: MNL Passenger Choice Model Summary

MNL choice model fragment with outside option, three passenger types, and acceptance probability — ready for `\input{choice-model}` in model.tex.

## Equation Label Inventory

| Label | Type | Description |
|-------|------|-------------|
| `eq:utility` | equation | MNL deterministic utility $U_{rb}^k$ with four $\beta^k$ terms |
| `eq:utility-outside` | equation | Outside option utility $U_{r0}^k = \beta_0^k$ |
| `eq:type-price` | equation | Ordering constraint: price-sensitive type has largest $|\beta_4|$ |
| `eq:type-time` | equation | Ordering constraint: time-sensitive type has largest $|\beta_2|+|\beta_3|$ |
| `eq:type-walk` | equation | Ordering constraint: walk-sensitive type has largest $|\beta_1|$ |
| `eq:beta-price` | equation | Baseline $\beta$ values for price-sensitive type (provisional) |
| `eq:beta-time` | equation | Baseline $\beta$ values for time-sensitive type (provisional) |
| `eq:beta-walk` | equation | Baseline $\beta$ values for walk-sensitive type (provisional) |
| `eq:choice-prob` | equation | MNL choice probability $P_{rb}^k$ with outside option in denominator |
| `eq:outside-prob` | equation | Outside option probability $P_{r0}^k$ |
| `eq:acceptance-prob` | equation | Acceptance probability $P_r^{\text{acc},k} = 1 - P_{r0}^k$ |
| `tab:passenger-types` | table | Qualitative $\beta$ profiles for three passenger types |

Total: 11 equation labels + 1 table label = 12 labels.

## Baseline Beta Parameter Values (Provisional)

All values below are provisional and must be confirmed against Work 1/2 calibration before Phase 3 simulation.

| Type | $\beta_1$ (Walk, /m) | $\beta_2$ (Wait, /min) | $\beta_3$ (IVT, /min) | $\beta_4$ (Price, /CNY) |
|------|----------------------|------------------------|------------------------|--------------------------|
| price-sensitive | -0.005 | -0.04 | -0.02 | -0.15 |
| time-sensitive  | -0.005 | -0.10 | -0.08 | -0.03 |
| walk-sensitive  | -0.020 | -0.04 | -0.02 | -0.05 |

Source: provisional values consistent with DRT literature ranges; to be calibrated.

## Outside Option ASC

$\beta_0^k$ is set to **0** for all passenger types, normalizing the outside option as the reference alternative. This is the standard MNL normalization. A non-zero $\beta_0^k$ could represent modal preference (e.g., car ownership) but is deferred to Phase 3 sensitivity analysis.

## Open Questions for Phase 3 Simulation Setup

1. Calibration source: Should $\beta$ values come from Work 1/2 SP survey data, or from literature (e.g., Cortenbach et al. 2024, Wu et al. 2025)? Confirm before Phase 3.
2. Outside option ASC: Should $\beta_0^k$ vary by type (e.g., walk-sensitive passengers may have lower outside option utility if they lack car access)? Currently set to 0 for all types.
3. Demand mix: What fraction of requests should be assigned to each passenger type in simulation? Suggest 40% price / 40% time / 20% walk as baseline, with sensitivity runs.
4. Scale parameter: The Gumbel scale is fixed at 1 (standard MNL). If heteroscedasticity is needed, a nested logit or mixed logit extension may be required — flag for Phase 3.
5. Bundle set size $|\mathcal{B}_r|$: The choice probability formula assumes the system offers a set of bundles. Phase 2 must specify whether $|\mathcal{B}_r| = 1$ (single best offer) or $|\mathcal{B}_r| > 1$ (menu). Currently the model supports both.

## Deviations from Plan

None — plan executed exactly as written.

## Self-Check: PASSED

- `model/choice-model.tex` exists and is non-empty
- 11 `eq:*` labels present (>= 8 required)
- 12 total labels present (>= 9 required)
- All four $\beta^k$ parameters appear with type superscript
- `\exp(U_{r0}^k)` appears in both definition and denominator of choice probability
- Three passenger types match $\mathcal{K} = \{\text{price}, \text{time}, \text{walk}\}$
- No `\documentclass` or `\begin{document}` in file
- Comment `%% choice-model.tex` on line 1
