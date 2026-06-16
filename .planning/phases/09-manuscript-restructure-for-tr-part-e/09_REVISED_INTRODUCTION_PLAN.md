# Phase 9 Revised Introduction and Literature Positioning Plan

**Purpose:** Plan the new introduction and literature-positioning logic for a
Transportation Research Part E evidence-chain manuscript. This file is a
planning artifact, not final manuscript prose.

## Current Introduction Risks

The current introduction opens with a plausible DRT motivation, but it still
sets up the manuscript as a broad gap-filling method paper and previews old
effect-size results before the claim gate exists. It also uses risky novelty
language around prior meeting-point work and ends with a paper organization
that preserves the old model/algorithm/experiments/policy flow.

Risks to remove or quarantine:

- Overstating the novelty gap by implying prior work only handles pickup-side
  meeting points.
- Previewing unsupported numerical gains before Phase 8 supported claims exist.
- Treating algorithm diagnostics as a headline contribution rather than support
  evidence.
- Framing policy implications before limitations and boundary conditions.
- Mixing behavioral evidence, coverage controls, and diagnostics in the setup.

## Revised Introduction Flow

- **Evidence problem first.** Open with the reviewer-facing fair-evidence
   problem: passenger response, coverage, baseline inconsistency, and
   diagnostic/result mixing can make meeting-point DRT look stronger or weaker
   than the evidence supports.
- **Operational setting.** Explain why demand-responsive transit with walking
   access/egress creates a service-design problem for operators rather than a
   simple routing-only problem.
- **Framework response.** Introduce the choice-aware dynamic service-design
   framework as an integrated simulation and evidence-chain tool, not as a
   broad first/only novelty claim.
- **Claim discipline.** State that comparisons require shared passenger
   response, explicit denominators, paired seeds, coverage controls, and a
   claim-evidence gate.
- **Research questions and contributions.** Present the three approved
   research questions and order contributions around evidence discipline,
   model/framework, experimental findings, and managerial implications.
- **Paper organization.** Close with the TR-E evidence-chain structure.

## Paragraph-Level Outline

- **Opening evidence-confounding paragraph.** Meeting-point DRT can reduce
   vehicle detours, but passenger response, coverage, baseline inconsistency,
   and diagnostic/result mixing can confound conclusions. The paragraph should
   make the fair-comparison problem the reason for the paper.
- **DRT service-design paragraph.** Describe the operating challenge:
   bidirectional pickup/dropoff meeting points can support route consolidation,
   but only if passengers accept the offered walk, wait, fare, and in-vehicle
   travel trade-off.
- **Literature gap paragraph.** Position prior DARP, meeting-point, walking
   ridepooling, passenger-choice, and rolling-horizon work as partially
   overlapping literatures. Avoid saying no prior work considers dropoff
   walking.
- **Framework paragraph.** Introduce the integrated choice-aware dynamic
   service-design simulation framework, including shared passenger response,
   route-then-sample operation, rolling-horizon dispatch, and diagnostic
   solvers as support tools.
- **Evidence-chain paragraph.** Explain the paper's evidence discipline:
   Phase 2 metric denominators, behavioral main comparisons, matched-coverage
   controls, fixed accepted-set diagnostics, paired seeds, and Phase 8 claim
   gating.
- **Research questions and contribution paragraph.** Use the exact three
   research questions and contribution order defined below.
- **Organization paragraph.** State that the manuscript proceeds through
   `Literature and Positioning`, `Framework and Solution Approach`,
   `Experimental Design and Evidence Families`, `Formal Main Evidence`,
   `Robustness, Equity, and Diagnostic Evidence`,
   `Limitations and Boundary Conditions`,
   `Managerial Insights and Boundary Conditions`, and `Conclusion`.

## Research Questions

1. Under fair comparison, whether and when bidirectional meeting-point design improves operating efficiency relative to door-to-door and single-sided variants under shared passenger-response assumptions?
2. How do passenger response and coverage change the interpretation of efficiency results from bidirectional meeting-point service design?
3. What equity and managerial boundary conditions follow from the evidence?

Algorithm diagnostics are not a standalone research question. They are
methodological support for routing credibility, runtime interpretation, and
diagnostic scope.

## Contribution Order

The introduction should present contributions in this exact order:

1. **evidence discipline** - fair comparison families, metric-denominator
   control, paired evidence, and claim gating.
2. **model/framework** - integrated choice-aware dynamic service-design
   simulation with bidirectional pickup/dropoff meeting points.
3. **experimental findings** - Phase 8-supported results only, with coverage
   and rejection context.
4. **managerial implications** - conditional insights after limitations and
   boundary conditions.

## Literature Positioning Rewrite Rules

| Current risk | Allowed replacement | Required source | Phase 8 dependency |
|---|---|---|---|
| broad first/only language | "We study an integrated choice-aware dynamic service-design simulation framework..." | `01_NOVELTY_POSITIONING.md`; exact citation check before final text | Phase 8 must approve any precise novelty claim. |
| pickup-side-only claim about prior work | "Prior work covers meeting points and walking locations in partially overlapping settings; this paper evaluates the integrated bidirectional service-design evidence chain." | `01_LITERATURE_AUDIT.md`; full-text check for Cortenbach et al. (2024); Fielbaum et al. (2021) | Unresolved scope remains a blocker for exact contrast wording. |
| passenger-choice gap claims | "The framework combines passenger response with service-design comparison under shared assumptions." | Phase 3 choice model contract; Phase 2 fair-comparison contract | Phase 8 must approve any claim that passenger response changes final interpretation. |
| rolling-horizon claims | "Rolling-horizon ALNS is the operational mechanism and algorithm diagnostic support." | `manuscript/sections/algorithm.tex`; Phase 4/6 algorithm diagnostic artifacts when available | Phase 8 must approve any result claim about rolling-horizon benefit. |
| DARPmp/ridepooling overlap | "DARPmp and ridepooling studies motivate meeting-point/walking-location design; this paper tests a claim-gated DRT service-design evidence chain." | `01_LITERATURE_AUDIT.md`; Cortenbach et al. (2024); Fielbaum et al. (2021); DARP/DRT surveys | Phase 8 gates final wording if overlap affects claimed contribution strength. |

Any exact novelty statement must cite Phase 1 audit evidence and the relevant
local or external source. unresolved literature items are blockers, not safe
claims. If an exact mechanism, citation, or bibliography record remains
uncertain, the introduction should use a broader positioning statement or mark
the wording as pending rather than asserting priority.
