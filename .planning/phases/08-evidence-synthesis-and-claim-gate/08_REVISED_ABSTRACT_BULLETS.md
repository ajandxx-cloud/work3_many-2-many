# Phase 8 Revised Abstract Bullets

**Phase:** 08 - Evidence Synthesis and Claim Gate
**Date:** 2026-06-16
**Status:** complete

These are claim units for Phase 9 refresh, not a complete abstract.

## Allowed Abstract Claim Units

- Meeting-point DRT can reduce operating distance, but evidence must separate
  service-design effects from passenger response, served-share differences, and
  denominator choices.
- The study develops an integrated choice-aware dynamic service-design
  simulation framework for many-to-many DRT with bidirectional pickup/dropoff
  meeting-point sets, shared passenger-response semantics, rolling-horizon
  dispatch, and explicit evidence families.
- In 20-seed formal synthetic paired experiments, the bidirectional
  meeting-point design shows lower vehicle-km intensity than door-to-door and
  single-sided choice baselines, with vehicle-km denominators reported by both
  served trips and original requests.
- The same abstract claim must state that the bidirectional design serves a
  smaller share in the main behavioral matrix; efficiency, coverage, acceptance,
  and rejection outcomes must be interpreted together.
- Matched-coverage controls are consistent with the efficiency direction on
  completed pairs, but the abstract must not hide the 15 durable failed
  FullModel matched rows if this point is mentioned.
- Robustness, equity, algorithm, and Beijing-inspired scenario outputs are
  bounded diagnostics or limitations, not headline validation.
- Real or semi-real city calibration and validation remain future work.

## Forbidden Abstract Content

- No real Beijing validation.
- No universal superiority.
- No first/only novelty claim.
- No deployment-ready language.
- No legacy 29.1% or 35.0% effect-size claim.
- No `vkm_per_trip`; use `vkm_per_served_trip` or
  `vkm_per_original_request`.
- No strong equity-benefit claim.

## Abstract Evidence Tags

| claim unit | claim_id | grade |
|---|---|---|
| integrated framework | C-FWK-01 | moderate |
| formal vkm intensity result | C-EFF-01 | strong |
| coverage/served-share trade-off | C-COV-01 | strong |
| matched-coverage caveat | C-MC-01 | moderate |
| synthetic and calibration boundary | C-LIM-01 | strong limitation |

