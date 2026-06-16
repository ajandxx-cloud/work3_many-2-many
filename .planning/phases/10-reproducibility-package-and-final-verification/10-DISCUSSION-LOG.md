# Phase 10: Reproducibility Package and Final Verification - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md; this log preserves the alternatives considered.

**Date:** 2026-06-16T11:30:41+08:00
**Phase:** 10-reproducibility-package-and-final-verification
**Areas discussed:** Upstream prerequisite gap policy, Reproduction command scope, Manifest granularity, Final claim verification format

---

## Upstream Prerequisite Gap Policy

| Option | Description | Selected |
|---|---|---|
| Blocking list | Fail closed: output a reproducibility package framework and blocker list, but do not claim final verification passed. | Yes |
| Partial package | Generate a partial reproducibility package and label available versus missing inputs. | |
| Continue as passed | Use current legacy or pilot artifacts as caveated final verification inputs. | |

**User's choice:** Blocking list.
**Notes:** Phase 10 must not mark final verification as passed when Phase 6 formal results/artifacts or Phase 8 claim-gate files are absent.

| Option | Description | Selected |
|---|---|---|
| Framework plus blockers | Create the three core Phase 10 artifacts with blocked/pending status. | Yes |
| Only blockers | Create only `10_FINAL_VERIFICATION.md` with missing prerequisites. | |
| No Phase 10 artifacts yet | Stop until Phase 6 and Phase 8 are complete. | |

**User's choice:** Framework plus blockers.
**Notes:** Blocked Phase 10 artifacts are useful because they tell later agents exactly what remains missing.

| Option | Description | Selected |
|---|---|---|
| Phase 6 plus Phase 8 | Formal result report/artifacts and the Phase 8 claim-gate trio are hard blockers. | Yes |
| Only Phase 8 | Treat only claim gate as a hard blocker. | |
| Stricter | Require Phase 6, Phase 7, Phase 8, and Phase 9 final outputs. | |

**User's choice:** Phase 6 plus Phase 8.
**Notes:** The hard blockers are Phase 6 formal results/artifacts plus `08_CLAIM_EVIDENCE_MATRIX.md`, `08_SUPPORTED_CLAIMS.md`, and `08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md`.

| Option | Description | Selected |
|---|---|---|
| Blocked: prerequisites missing | Required upstream evidence is absent; this is not a failed research result. | Yes |
| Failed verification | State that final verification failed. | |
| Pending verification | Use the softest wording. | |

**User's choice:** Blocked: prerequisites missing.
**Notes:** This is a prerequisite failure, not a negative finding.

---

## Reproduction Command Scope

| Option | Description | Selected |
|---|---|---|
| Final evidence entry points first | Reviewer-facing commands focus on final main tables/figures, Phase 6 formal artifacts, Phase 8 claim gate, and manuscript build. | Yes |
| Whole repository coverage | Cover pilot, legacy, formal, diagnostic, analysis, and manuscript build commands. | |
| Minimal submission package | Cover only final main tables, final main figures, and PDF compilation. | |

**User's choice:** Final evidence entry points first.
**Notes:** Pilot, legacy, and diagnostic commands are provenance or supplementary unless Phase 8 promotes them.

| Option | Description | Selected |
|---|---|---|
| Mark as non-final evidence | Include pilot and legacy artifacts in the manifest as readiness/provenance/legacy, not headline evidence. | Yes |
| Exclude entirely | Keep them out of the Phase 10 manifest. | |
| Put in supplement | Include them as supplementary package artifacts. | |

**User's choice:** Mark as non-final evidence.
**Notes:** The manifest should help prevent accidental reuse of pilot or legacy values in headline claims.

| Option | Description | Selected |
|---|---|---|
| Layer by evidence role | Separate critical robustness, supplementary diagnostic, and legacy diagnostic commands. | Yes |
| All as supplement | Treat all diagnostics as supplement without support-level distinctions. | |
| Only formal diagnostics | Exclude old gamma, weight, or legacy diagnostics. | |

**User's choice:** Layer by evidence role.
**Notes:** Only Phase 8-supported evidence may enter main-text claims.

| Option | Description | Selected |
|---|---|---|
| Include PDF and table/figure chain | Record LaTeX build, main table/figure generation, input paths, and output paths. | Yes |
| Only LaTeX compilation | Leave table and figure generation to the result manifest. | |
| Exclude manuscript build | Limit Phase 10 to experiment result reproducibility. | |

**User's choice:** Include PDF and table/figure chain.
**Notes:** Manuscript reproducibility includes the build chain and generated displays.

---

## Manifest Granularity

| Option | Description | Selected |
|---|---|---|
| Layered manifest plus row-level index | Group by evidence family, then list artifact path, role, status, command, inputs, outputs, and claim relationship. | Yes |
| Grouped summary only | Summarize each artifact class without per-file rows. | |
| Flat per-file table | Use one large ungrouped table for all artifacts. | |

**User's choice:** Layered manifest plus row-level index.
**Notes:** The manifest should be readable by humans and structured enough to become JSON/CSV later.

| Option | Description | Selected |
|---|---|---|
| Reviewer reproduction fields | Require path, role, evidence family, status, source command, inputs, outputs, code revision, claim link, and notes/blockers. | Yes |
| Lightweight fields | Use path, role, status, and notes only. | |
| Strong validation fields | Add mandatory checksum, timestamps, dependency snapshot, runtime, and owner phase. | |

**User's choice:** Reviewer reproduction fields.
**Notes:** This is the minimum row contract for `10_RESULT_MANIFEST.md`.

| Option | Description | Selected |
|---|---|---|
| Recommended but not hard blocking | Record code revision and dependency commands; checksums and dependency snapshots are improvements if absent. | Yes |
| Mandatory | Require checksum and dependency snapshot for every artifact. | |
| Not needed | Do not use checksum or dependency snapshots. | |

**User's choice:** Recommended but not hard blocking.
**Notes:** Missing checksums should not become the main blocker while Phase 6/8 are absent.

| Option | Description | Selected |
|---|---|---|
| Explicit pending | Use `claim_link = pending Phase 8` and mark the artifact unable to support final claims. | Yes |
| Leave blank | Fill claim links only after Phase 8. | |
| Phase 9 placeholders | Temporarily map artifacts to Phase 9 placeholder claims. | |

**User's choice:** Explicit pending.
**Notes:** This makes the absent claim gate visible in every affected artifact row.

---

## Final Claim Verification Format

| Option | Description | Selected |
|---|---|---|
| Gate matrix | List prerequisites, artifacts, tables/figures, claims, status, evidence path, and blocker. | Yes |
| Final checklist | Check REP-01/REP-02 and success criteria only. | |
| Narrative report | Explain pass/blocker status in paragraphs. | |

**User's choice:** Gate matrix.
**Notes:** The final verification should be auditable at row level.

| Option | Description | Selected |
|---|---|---|
| Pass / Pending / Blocked / Not final evidence | Distinguish passed, waiting on Phase 8, hard blocker, and non-final evidence. | Yes |
| Pass / Fail / Pending | Use simpler status labels. | |
| Green / Yellow / Red | Use visual status labels with separate definitions. | |

**User's choice:** Pass / Pending / Blocked / Not final evidence.
**Notes:** These values are the canonical verification statuses for Phase 10.

| Option | Description | Selected |
|---|---|---|
| Per final claim | Every final manuscript claim links to Phase 8 evidence, result artifacts, and tables/figures. | Yes |
| By claim family | Verify efficiency, coverage, equity, and managerial insight families. | |
| Headline claims only | Let Phase 8 handle detailed claims. | |

**User's choice:** Per final claim.
**Notes:** Missing evidence should appear as `Blocked` or `Pending` per claim.

| Option | Description | Selected |
|---|---|---|
| Standalone section plus machine-readable seed | Put a human-readable artifact index in `10_REPRODUCIBILITY.md` and a structured table seed in `10_RESULT_MANIFEST.md`. | Yes |
| Only in `10_RESULT_MANIFEST.md` | Avoid duplication. | |
| Separate `10_ARTIFACT_INDEX.md` | Create an additional artifact-index file. | |

**User's choice:** Standalone section plus machine-readable seed.
**Notes:** The roadmap requires a final artifact index, but not a separate file.

## the agent's Discretion

- Exact table layouts, artifact-family headings, optional checksum tooling, and
  command formatting can be chosen during planning.
- Machine-readable companion files may be added later, but the roadmap outputs
  remain the canonical artifacts.

## Deferred Ideas

None.
