# Phase 8 Unsupported or Exploratory Claims

**Phase:** 08 - Evidence Synthesis and Claim Gate
**Date:** 2026-06-16
**Status:** complete

## Purpose

List claims that must be deleted, rewritten, moved to limitations, or kept only
as exploratory discussion. This file is the forbidden-language gate for Phase 9.

## Forbidden or Downgraded Claims

| original or likely overclaim | claim_id | why not allowed | contradiction or insufficiency | allowed replacement | manuscript action |
|---|---|---|---|---|---|
| "FullModel is unconditionally superior." | C-EFF-01 / C-COV-01 | The formal main matrix supports lower vkm intensity only with lower served share and explicit denominator context. | FullModel served share is lower than DoorToDoor; coverage and rejection differ. | "FullModel shows lower vehicle-km intensity under the tested formal synthetic paired design, with lower served share." | rewrite |
| "Bidirectional meeting points dominate door-to-door service under all metrics." | C-EFF-01 / C-COV-01 | Some metrics, especially served share and feasibility rejection, do not support dominance. | Main matrix served share is lower for FullModel; fixed accepted-set vkm/original is not an unconditional win. | "The design improves selected vehicle-km denominators under specified synthetic conditions." | rewrite |
| "FullModel wins on every denominator." | C-FAS-01 | Fixed accepted-set diagnostics do not support unconditional vkm/original dominance. | Fixed accepted-set aggregate vkm/original vs DoorToDoor is +0.052, not a win. | "Fixed accepted-set diagnostics support vkm per served request only." | rewrite |
| "Fixed accepted-set proves unconditional vkm/original advantage." | C-FAS-01 | Diagnostic-only and contradicted by vkm/original summary. | vkm/original fixed accepted-set does not favor FullModel unconditionally. | "Fixed accepted-set is a routing/service-design diagnostic for vkm per served request." | rewrite |
| "Equity benefits are strongly established." | C-EQ-01 | Passenger types are simulation-range constructs; outputs are diagnostics. | Equity package has type-level and individual burden rows but no empirical demographic calibration. | "Equity diagnostics report modeled type-level and individual-burden patterns." | move to exploratory discussion / limitations |
| "The Beijing case validates real-world Beijing operations." | C-CASE-01 | Phase 7 found no real or semi-real case data. | Generated OD, generated MP grid, simulated request times, no road network or observed preferences. | "Beijing-inspired synthetic scenario." | delete / rewrite |
| "The method provides direct citywide policy recommendations for Beijing." | C-POL-01 / C-CASE-01 | Synthetic scenario and no observed operations cannot support direct policy prescriptions. | Phase 7 prohibits real-city policy claims. | "The simulation suggests conditional managerial boundary conditions." | rewrite / move after limitations |
| "The method is deployment-ready." | C-DEP-01 | No real/semi-real validation, calibration, or deployment data. | Phase 7 data audit and Phase 6 synthetic boundary. | "Real-world deployment requires calibration and validation." | delete |
| "This is the first bidirectional meeting-point DRT paper." | C-NOV-01 | Phase 1 forbids broad firstness. | Prior work covers meeting points and pickup/dropoff walking in overlapping settings. | "Integrated choice-aware dynamic service-design simulation framework." | delete / rewrite |
| "No prior work considers dropoff walking." | C-NOV-01 | Directly forbidden by Phase 1 novelty audit. | Fielbaum et al. and Cortenbach metadata narrow this claim. | "Prior work covers overlapping walking-location settings." | delete |
| "Existing work assigns meeting points only on pickup side." | C-NOV-01 | Phase 1 marks this as contradicted or too broad. | Cortenbach metadata and Fielbaum et al. indicate pickup/dropoff walking relevance. | "Prior work covers partially overlapping meeting-point and walking-location designs." | rewrite |
| "Gamma sweep is a Pareto frontier." | C-GAMMA-01 | Gamma is post-hoc welfare accounting and does not affect routing or acceptance. | Served share and vkm/served are invariant across gamma. | "Post-hoc welfare sensitivity diagnostic." | delete / move appendix |
| "Legacy 29.1% vkm/trip improvement proves superiority." | C-LEG-01 | Legacy value is coverage-confounded and superseded by Phase 6 formal evidence. | Phase 0 found aggregation/caption mismatch and served-share confounding. | Use Phase 6 vkm denominators and CIs if supported by C-EFF-01/C-COV-01. | delete from abstract/intro/conclusion |
| Any claim relying only on pilot, smoke, or legacy unvalidated outputs. | C-LEG-01 / C-WEIGHT-01 | Formal claims require Phase 6/8 evidence. | Smoke and legacy outputs are excluded from formal manifest. | "Legacy outputs motivated the rebuild but are not final evidence." | delete or provenance-only |
| "Weight sensitivity proves robust efficiency gains across policy-relevant objective weights." | C-WEIGHT-01 | Legacy weight table has formula/provenance mismatch and is not Phase 6 formal evidence. | Phase 0 found JSON and manuscript vkm/trip values inconsistent. | "Legacy weight sensitivity is diagnostic provenance only unless rebuilt." | remove from main claims |
| "Chinese regulators should require disaggregated acceptance reporting based on this study." | C-POL-01 / C-EQ-01 | Strong regulatory prescription exceeds synthetic/equity evidence. | Equity is exploratory and not empirically calibrated. | "Future deployments should monitor type-level and individual burden measures." | rewrite as future-work/managerial caution |
| "1000 m is the minimum walking radius for deployment." | C-MP-01 | Radius threshold is scenario and parameter specific. | No pedestrian network or empirical walking tolerance calibration. | "Within the tested synthetic grid, radius/density diagnostics bound sensitivity." | rewrite / move to limitations |
| "15 vehicles per 100 requests is a planning rule." | C-FLEET-01 | Fleet-demand diagnostics are synthetic stress tests. | No observed fleet/demand calibration. | "Fleet-demand stress tests indicate setting-specific sensitivity." | rewrite |

## Strongest Forbidden Overclaim

The strongest forbidden overclaim is:

> FullModel is unconditionally superior and validates real-city deployment.

This combines the three largest risks: universal superiority, denominator
mixing, and real-world deployment/case-study overreach.

## Required Phase 9 Actions

- Delete legacy 29.1% and 35.0% effect-size claims from abstract, introduction,
  and conclusion unless replaced by Phase 6/8-approved conditional wording.
- Replace pickup-only and first/only novelty language with the integrated
  framework positioning.
- Replace real-Beijing or Chinese-city policy claims with synthetic,
  limitation-first boundary language.
- Move gamma, weight sensitivity, algorithm diagnostics, and most case material
  to appendix/supplement or limitations unless Phase 9 gives them clearly
  diagnostic main-text roles.
- Keep equity as exploratory diagnostics, not a strong improvement or policy
  proof.

