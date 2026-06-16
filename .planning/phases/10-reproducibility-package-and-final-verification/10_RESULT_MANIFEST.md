# Phase 10 Result Manifest

**Status:** Blocked: prerequisites missing
**Purpose:** Inventory result, diagnostic, display, and manuscript-build artifacts by evidence role before final claim verification.

## Prerequisite Gate

Phase 10 must fail closed until the formal evidence report and claim-gate artifacts below exist. Missing prerequisites use the exact status `Blocked: prerequisites missing`.

| prerequisite_path | status | implication |
|---|---|---|
| `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md` | Blocked: prerequisites missing | Formal synthetic evidence report is absent, so main results cannot be certified as final evidence. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_CLAIM_EVIDENCE_MATRIX.md` | Blocked: prerequisites missing | Claim-to-evidence mapping is absent, so artifact claim links remain `pending Phase 8`. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_SUPPORTED_CLAIMS.md` | Blocked: prerequisites missing | Supported final claims are not approved. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` | Blocked: prerequisites missing | Unsupported or exploratory claims are not classified for final manuscript use. |

## Manifest Schema

Rows in the layered manifest use one artifact per row and the following stable columns so the table can later be exported to JSON or CSV.

| path | role | evidence_family | status | source_command | inputs | outputs | code_revision | claim_link | notes/blockers |
|---|---|---|---|---|---|---|---|---|---|
| Example path | Example role | Example evidence family | Example status | Example command | Example inputs | Example outputs | Example revision | Example claim link | Example notes/blockers |

## Evidence Families

| evidence_family | allowed role | final-claim rule |
|---|---|---|
| `formal_main_evidence` | final evidence candidate | Requires complete Phase 6 report and Phase 8 claim support before use in headline claims. |
| `critical_robustness` | robustness evidence candidate | May qualify final claims only after Phase 8 support; otherwise `pending Phase 8`. |
| `supplementary_diagnostic` | diagnostic | Mechanism or appendix support only unless Phase 8 explicitly promotes a bounded claim. |
| `legacy_diagnostic` | legacy or provenance | Not final evidence; use only to explain historical outputs or audit provenance. |
| `pilot_readiness` | readiness or provenance | Not final evidence; pilot outputs cannot support headline claims. |
| `manuscript_display` | display asset | Reproducible display artifact; empirical status depends on underlying evidence and Phase 8 support. |
| `manuscript_build` | build artifact | Reproducibility and packaging support, not empirical evidence by itself. |
