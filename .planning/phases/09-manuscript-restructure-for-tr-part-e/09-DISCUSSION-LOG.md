# Phase 9: Manuscript Restructure for TR Part E - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md; this log preserves the alternatives considered.

**Date:** 2026-06-16T10:12:31.7906036+08:00
**Phase:** 9-Manuscript Restructure for TR Part E
**Areas discussed:** Manuscript storyline, Section restructuring, Table and figure boundaries, Policy and managerial implications tone, Abstract and introduction contribution framing

---

## Manuscript Storyline

| Question | Options Presented | User's Choice | Notes |
|---|---|---|---|
| What should the main manuscript storyline prioritize? | Evidence-chain reconstruction; Method framework; Managerial insight | Evidence-chain reconstruction | The paper should not be framed as unconditional method superiority. |
| How should the introduction open? | Reviewer problem / evidence gap first; Operational problem first; Method opportunity first | Reviewer problem / evidence gap first | Open with fair-comparison and evidence-confounding risks. |
| What tone should the title and abstract use? | Cautious and conditional; Method contribution; Result finding | Cautious and conditional | Avoid unqualified superiority language. |
| How should the contribution list be ordered? | Evidence discipline -> model framework -> experimental findings -> managerial implications; Model framework -> algorithm -> experiments -> managerial implications; Research findings -> method -> robustness -> implications | Evidence discipline -> model framework -> experimental findings -> managerial implications | Evidence discipline leads the paper. |

## Section Restructuring

| Question | Options Presented | User's Choice | Notes |
|---|---|---|---|
| What overall section architecture should Phase 9 use? | Keep existing skeleton and reorder emphasis; TR-E evidence-chain structure; Method-paper structure | TR-E evidence-chain structure | Larger rewrite is acceptable to match TR-E evidence logic. |
| How should model and algorithm material be positioned? | Combine as Framework and Solution Approach; Separate Model and Algorithm chapters; Model in main text, algorithm in appendix | Combine as Framework and Solution Approach | Diagnostics remain visibly separate from main evidence. |
| How should the experiment section be organized? | Experimental design first, then evidence packages; Organize by result themes; Organize by experiment type | Experimental design first, then evidence packages | Evidence-family boundaries should precede results. |
| Where should limitations be placed? | Standalone section before managerial insights; In the conclusion; After each result subsection | Standalone section before managerial insights | Boundary conditions should precede applied implications. |

## Table and Figure Boundaries

| Question | Options Presented | User's Choice | Notes |
|---|---|---|---|
| What should the main text's primary table contain? | Formal main-evidence matrix plus quartet metrics; Main evidence plus key robustness in one table; Only BidirectionalMP versus DoorToDoor | Formal main-evidence matrix plus quartet metrics | Main table must report the efficiency-and-coverage quartet. |
| Where should matched coverage and fixed accepted-set controls appear? | Main-text robustness subsection plus complete appendix tables; Appendix only; Large table directly after main results | Main-text robustness subsection plus complete appendix tables | Must state whether robustness controls challenge the main interpretation. |
| How should algorithm diagnostics be presented? | Main text only states diagnostic scope; One algorithm performance figure in the main text; Appendix only with no main-text discussion | Main text only states diagnostic scope | Detailed diagnostic plots go to appendix/supplement. |
| How should equity and passenger-type results be presented? | Main-text trade-off summary plus appendix distribution details; Present at the same level as main results; Appendix only | Main-text trade-off summary plus appendix distribution details | Equity is a condition/boundary result, not hidden and not made the main result. |

## Policy and Managerial Implications Tone

| Question | Options Presented | User's Choice | Notes |
|---|---|---|---|
| What should the policy/managerial section title be? | Managerial Insights and Boundary Conditions; Policy Implications; Implications for Dynamic DRT Design | Managerial Insights and Boundary Conditions | This lowers policy-overreach risk. |
| How should the existing R1-R5 recommendations be handled? | Rewrite as conditional insight bullets; Keep the R1-R5 framework and add caveats; Move all to appendix/discussion | Rewrite as conditional insight bullets | Unsupported items should be removed, downgraded, or reframed. |
| How should Beijing/city-density language be handled? | Only describe Beijing-inspired synthetic scenarios; Keep Beijing case language with caveats; Remove city-density extrapolation entirely | Only describe Beijing-inspired synthetic scenarios | Do not imply real Beijing evidence. |
| What question should managerial insights primarily answer? | When it is worth adopting bidirectional meeting-point design; How operators should tune parameters; What the results imply for city policy | When it is worth adopting bidirectional meeting-point design | Focus on conditions, trade-offs, and boundaries. |

## Abstract and Introduction Contribution Framing

| Question | Options Presented | User's Choice | Notes |
|---|---|---|---|
| How should the abstract's first sentence position the research object? | Open with the fair-evidence problem; Open with the service-design problem; Open with the dynamic DRT operations problem | Open with the fair-evidence problem | Lead with confounding from passenger response, coverage, and baselines. |
| How should the core contribution sentence be framed? | Provide an evidence-chain framework; Propose the bidirectional meeting-point method; Demonstrate conditional efficiency gains | Provide an evidence-chain framework | Pair framework with fair comparison, coverage controls, and claim gate. |
| How should the introduction's research questions be designed? | Use a three-question structure; Use a four-question structure with algorithm diagnostics as RQ4; Use contributions only, no explicit research questions | Use a three-question structure | Algorithm diagnostics should not become a standalone headline RQ. |
| How should the abstract close? | Conditional conclusion plus boundary conditions; Managerial implications; Future research | Conditional conclusion plus boundary conditions | Close with design guidance bounded by synthetic evidence and trade-offs. |

## the agent's Discretion

- Exact section titles, figure numbering, appendix/supplement split, captions,
  and wording templates can be chosen by the planner as long as they preserve
  the locked decisions in `09-CONTEXT.md`.
- Direct LaTeX edits are optional and should be planned carefully; they must not
  introduce unsupported claims before Phase 8 claim-gate artifacts exist.

## Deferred Ideas

None. Discussion stayed within Phase 9 scope.
