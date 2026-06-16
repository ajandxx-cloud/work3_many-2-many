# Phase 7 Case Study Results

**Phase:** 07 - Semi-Real or Beijing-Inspired Case Study
**Date:** 2026-06-16
**Status:** bounded closure
**Case classification:** Beijing-inspired synthetic case
**New Phase 7 case experiment run:** no

## Closure Decision

Phase 7 is closed as a bounded Beijing-inspired synthetic case. The repository
does not contain real or semi-real case-study data, so no real or semi-real
case experiment was run.

Running a new Phase 7 case experiment on the existing Beijing generator would
only create another synthetic run. It would not increase the case evidence
grade to real or semi-real external validity. Therefore this phase organizes
the existing synthetic case material, records its limitations, and prevents it
from being used as real Beijing evidence.

## Existing Case Material

The available case-like artifact is:

- `results/beijing_results.csv`

It contains 21 legacy synthetic rows:

- 3 seeds.
- 7 legacy variants.
- 200 requests.
- 15 vehicles.
- A generated 15 km x 15 km Beijing-inspired grid.
- Generated OD, generated request times, generated vehicle positions, and
  generated meeting points.

This legacy artifact predates the Phase 6 formal synthetic runner and does not
include a Phase 7 raw/processed/config/validation package. It is therefore
illustrative only.

## Legacy Summary

These values summarize `results/beijing_results.csv` and are not new Phase 7
formal evidence.

| Variant | n rows | served share mean | total vehicle-km mean | vkm per served trip mean | vkm per original request mean |
|---|---:|---:|---:|---:|---:|
| DoorToDoor | 3 | 0.775000 | 1353.868 | 8.787 | 6.769 |
| DoorToDoorCapped | 3 | 0.235000 | 480.269 | 10.218 | 2.401 |
| SingleSidedPickup | 3 | 0.780000 | 1227.577 | 7.903 | 6.138 |
| BidirectionalNoChoice | 3 | 0.813333 | 1221.099 | 7.544 | 6.105 |
| FullModel | 3 | 0.313333 | 261.692 | 4.179 | 1.308 |
| AblationNoRollingHorizon | 3 | 0.360000 | 506.768 | 7.037 | 2.534 |
| AblationNoChoice | 3 | 0.255000 | 184.847 | 3.624 | 0.924 |

## Comparison To Phase 6 Evidence

The legacy Beijing-inspired rows show a qualitative pattern that resembles the
formal synthetic evidence: the FullModel row has lower total vehicle-km and
lower vehicle-km denominators, while serving a smaller share than DoorToDoor.

This comparison is bounded:

- It is not a formal paired Phase 7 case experiment.
- It uses legacy variants and does not include the current four-method Phase 6
  behavioral method family in full; notably, the legacy case rows do not include
  `SingleSidedDropoff`.
- It lacks Phase 6-style raw/processed split, config manifest, seed manifest,
  failure ledger, and validation report.
- It cannot override Phase 6 formal synthetic evidence.
- It can only be used as a synthetic scenario-transfer illustration.

## Why No New Experiment Was Run

No new Phase 7 case experiment was run because the data audit found no real or
semi-real case data. A new run over the existing Beijing generator would remain
synthetic and would risk implying stronger external validity than the data
support. The correct fail-closed action is bounded documentation, not creating a
new pseudo-case.

## Case Result Status

| Artifact/check | Status |
|---|---|
| Data audit completed | complete |
| Case type explicit | Beijing-inspired synthetic case |
| Existing case-like results organized | complete |
| New real/semi-real experiment | not run |
| New synthetic bounded run | not run |
| Formal validator | not applicable because no new case experiment was run |
| Phase 6 evidence displaced | no |

## Interpretation

The Phase 7 case material may be described as an illustrative synthetic scenario
or scenario-based demonstration. It may not be described as evidence from real
Beijing operations.
