# Phase 1 Literature Audit

**Phase:** 01 - Literature and Novelty Audit
**Plan:** 01-01
**Date:** 2026-06-15
**Status:** complete with residual citation-cleanup risks

## Purpose

This audit checks whether the manuscript can safely claim novelty around bidirectional pickup and dropoff meeting points, passenger choice, rolling-horizon dispatch, and many-to-many DRT. It does not approve final manuscript claims. It creates a positioning contract for Phase 2 experiment design, Phase 8 claim gating, and Phase 9 manuscript restructuring.

## Sources Checked

Local sources:

- `manuscript/sections/abstract.tex`
- `manuscript/sections/intro.tex`
- `manuscript/sections/literature.tex`
- `manuscript/references.bib`
- `.planning/phases/00-repository-and-manuscript-audit/00_MANUSCRIPT_CLAIM_AUDIT.md`
- `.planning/phases/00-repository-and-manuscript-audit/00_REPOSITORY_AUDIT.md`
- `.planning/phases/00-repository-and-manuscript-audit/00_CURRENT_EXPERIMENT_MAP.md`

External metadata checks:

- Cortenbach, L. E., Gkiotsalitis, K., van Berkum, E. C., and Walraven, E. (2024). "The Dial-a-Ride problem with meeting points: A problem formulation for shared demand-responsive transit." `Transportation Research Part C`, 169, 104869. DOI search note: `10.1016/j.trc.2024.104869`.
- Fielbaum, A., Bai, X., and Alonso-Mora, J. (2021). "On-demand ridesharing with optimized pick-up and drop-off walking locations." `Transportation Research Part C`, 126, 103061. DOI: `10.1016/j.trc.2021.103061`.
- Wu, W., Zhang, Z., Lu, K., and Ren, J. (2025). "Dynamic demand-responsive transit scheduling with time-dependent travel times: A joint supply and demand management approach." `Transportation Research Part E`, 202, 104232. DOI search note: `10.1016/j.tre.2025.104232`.
- Alonso-Mora, J., Samaranayake, S., Wallar, A., Frazzoli, E., and Rus, D. (2017). "On-demand high-capacity ride-sharing via dynamic trip-vehicle assignment." `PNAS`, 114(3), 462-467. DOI: `10.1073/pnas.1611675114`.

## Citation-by-Claim Matrix

| Cited work | Source path or DOI/search note | Problem setting | Meeting-point scope | Pickup walking | Dropoff walking | Passenger response or choice model | Online or rolling-horizon component | Algorithmic method | Direct overlap with this paper | Implication for novelty | Confidence level |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cortenbach et al. (2024) | External metadata: DOI `10.1016/j.trc.2024.104869`; local `manuscript/references.bib` has mismatched author/page metadata | Shared DRT / DARP with meeting points | DARPmp formulation with meeting points available as alternative pickup or drop-off points; local manuscript's single-sided summary is not safe as written | Yes | Yes or at least explicitly possible in the formulation metadata; exact instance policy needs full-text confirmation | No behavioral acceptance model verified | Static/batch in available metadata; no rolling horizon verified | Problem formulation and heuristic/optimization framing | Strong overlap on meeting-point DARP, time windows, capacity, ride time, load, route duration | blocks first claim | High for metadata; medium for detailed mechanism without full-text review |
| Fielbaum et al. (2021) | `manuscript/references.bib`; DOI `10.1016/j.trc.2021.103061` | On-demand ridesharing / ridepooling | Optimized pick-up and drop-off walking locations | Yes | Yes | No explicit binary-logit service acceptance verified in local manuscript context | On-demand/static ridepooling context; not this paper's rolling-horizon DRT layer | Dynamic assignment / optimization for ridepooling with walking links | Directly overlaps with bidirectional walking-location design, though not many-to-many DRT with this paper's choice layer | narrows claim | High |
| Wu et al. (2025) | External metadata: DOI `10.1016/j.tre.2025.104232`; local `manuscript/references.bib` appears to cite a different title, author set, volume, and page/article number | Dynamic DRT scheduling with time-dependent travel times | No meeting-point scope verified from metadata | Not verified | Not verified | Joint supply and demand management; not the same binary-logit single-offer model | Yes; rolling-horizon / dynamic scheduling | Multi-objective dynamic scheduling | Overlaps with rolling-horizon DRT and demand-management framing, not bidirectional meeting points | narrows claim | Medium-high for metadata; medium for detailed model comparison |
| Alonso-Mora et al. (2017) | `manuscript/references.bib`; DOI `10.1073/pnas.1611675114` | High-capacity ride-sharing via real-time trip-vehicle assignment | No meeting-point design in the canonical formulation | No | No | No passenger acceptance model in the sense used here | Real-time dynamic assignment | Scalable anytime assignment framework | Overlaps with many-to-many dynamic ridepooling architecture and assignment logic | background only | High |
| Stiglic et al. (2015) | `manuscript/references.bib` | Ride-sharing systems with meeting points | Meeting points / virtual stops for shared rides | Yes | Partly or indirectly, depending on route and meeting-point setup | No binary-logit service acceptance verified | Static or planning-context ridesharing | Matching/optimization analysis | Establishes that meeting points in ridesharing predate this paper | narrows claim | Medium |
| Stiglic et al. (2018) | `manuscript/references.bib` | Enhanced ride-sharing with meeting points | Meeting-point ride-sharing extension | Yes | Partly or indirectly, depending on setup | No binary-logit service acceptance verified | Static or planning-context ridesharing | Optimization/simulation | Reinforces prior meeting-point efficiency evidence | narrows claim | Medium |
| Cordeau and Laporte (2007) | `manuscript/references.bib` | Classical DARP models and algorithms | Door-to-door classical DARP | No | No | Deterministic demand/service | Static DARP | Exact/heuristic DARP foundations | Background for DARP constraints, not meeting-point novelty | background only | High |
| Molenbruch et al. (2017) | `manuscript/references.bib` | DARP typology and literature review | Broad DARP taxonomy | Not specific | Not specific | Broad taxonomy | Static/dynamic variants surveyed | Review | Supports method taxonomy and highlights need to classify variants precisely | background only | High |
| Ho et al. (2018) | `manuscript/references.bib` | DARP survey and recent developments | Broad DARP and DRT context | Not specific | Not specific | Broad taxonomy | Includes dynamic developments | Review | Background for DARP/DRT state of the art | background only | High |
| Pillac et al. (2013) | `manuscript/references.bib` | Dynamic vehicle routing review | Not meeting-point specific | No | No | Not passenger-choice specific | Yes, dynamic VRP taxonomy | Review | Supports dynamic/online framing, not meeting-point novelty | background only | High |
| Ropke and Pisinger (2006) | `manuscript/references.bib` | Pickup-and-delivery with time windows | No meeting-point service design | No | No | No passenger choice | Static metaheuristic context | ALNS | Algorithmic background for ALNS, not novelty of service design | background only | High |
| Bent and Van Hentenryck (2004) | `manuscript/references.bib` | Scenario-based planning for partially dynamic VRP | No meeting points | No | No | No passenger choice | Rolling/receding horizon motivation | Scenario-based dynamic optimization | Background for rolling horizon, not DRT meeting-point novelty | background only | High |
| Jin and Liu (2024 working paper) | `manuscript/references.bib`; internal working paper note | Many-to-one DRT with dynamic pricing | Not bidirectional many-to-many meeting points | Maybe pickup-side only by local manuscript description | No verified dropoff walking | Explicit passenger choice / dynamic pricing | Dynamic DRT context | Simulation/optimization working-paper context | Internal/related prior choice-model basis; cannot be used as external novelty proof | unresolved | Medium-low |
| Vansteenwegen et al. (2022) | `manuscript/references.bib` | Demand-responsive public bus systems survey | Broad DRT/flexible bus context | Not specific | Not specific | Broad survey | Broad survey | Review | Background for DRT service class and terminology | background only | High |

## Audit Findings

1. The current manuscript claim that existing work assigns meeting points only on the pickup side is not defensible as written. Fielbaum et al. (2021) explicitly covers optimized pickup and dropoff walking locations in ridepooling, and Cortenbach et al. (2024) appears from external metadata to formulate meeting points as alternative pickup or drop-off points in DARPmp.
2. A broad "first bidirectional meeting-point" claim is unsafe. Prior work already covers bidirectional walking-location ideas outside this exact many-to-many DRT and choice-aware rolling-horizon combination.
3. A narrower integrated-framework claim remains defensible as a planning hypothesis: combining bidirectional pickup/dropoff meeting-point sets, simulated binary-logit passenger acceptance with an outside option, online rolling-horizon dispatch, many-to-many DRT, and equity/coverage diagnostics in one simulation framework.
4. The local bibliography has citation-risk errors for at least Cortenbach et al. (2024) and Wu et al. (2025). Those errors should be corrected before Phase 9 manuscript editing, but they do not block Phase 1 positioning because the audit records the correction target.
5. Literature coverage supports using TR-E-level evidence standards: operational taxonomy, fair behavioral comparisons, metric denominator control, reproducibility, and conservative claim wording.

## Literature Blockers

| Blocker | Impact | Downstream owner |
|---|---|---|
| Full text of Cortenbach et al. (2024) was not locally available; metadata strongly contradicts the manuscript's single-sided wording, but exact formulation details still need full-text verification before final manuscript citation language. | Blocks any exact statement about whether DARPmp permits pickup-only, dropoff-only, or both-side meeting-point variants in all experiment instances. | Phase 9 manuscript restructure |
| Local `manuscript/references.bib` metadata for Cortenbach et al. (2024) appears wrong relative to external metadata. | Bibliography must be corrected before manuscript submission. | Phase 9 manuscript restructure |
| Local `manuscript/references.bib` metadata for Wu et al. (2025) appears to cite a different title/author set/article number than the external TR-E metadata checked during this audit. | Dynamic DRT comparison row must be cleaned before manuscript submission. | Phase 9 manuscript restructure |
| Review-note file path listed in Phase 1 context was not readable under the expected Unicode filename in this checkout. | Phase 0 extracted the review-note risks, so Phase 1 can proceed, but raw-note provenance remains fragile. | Phase 10 reproducibility package |

## Requirements Coverage

| Requirement | Status | Evidence |
|---|---|---|
| POS-01 | Satisfied with residual citation-cleanup risks | Matrix verifies that prior work already covers pickup/dropoff walking locations in ridepooling and likely DARPmp. The audit prevents overclaiming rather than preserving a false gap. |
| POS-02 | Satisfied by routing unsupported novelty claims to forbidden/unresolved language | See `01_NOVELTY_POSITIONING.md`. |
| POS-03 | Satisfied by requiring TR-E-level evidence planning even if final venue remains undecided | See `01_NOVELTY_POSITIONING.md` and `01_REVISED_RESEARCH_QUESTIONS.md`. |

## Phase 2 Handoff

Phase 2 should treat literature novelty as a constraint on experiment design:

- Separate service-design variants from passenger-response assumptions.
- Include deterministic diagnostics only as diagnostics, not behavioral evidence.
- Preserve matched coverage and fixed accepted-set comparisons as required controls.
- Track any claim that depends on "integrated framework" to the exact experiment family that can support it.
