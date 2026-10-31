# Production Cleanup Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan task-by-task, with a final independent review.

**Goal:** Remove unsolicited promotion from this fork and verify local video production and MP4 export.

**Architecture:** OpenMontage orchestrates through Markdown instructions; Python supplies tools and persistence. Fix confirmed instruction and documentation sources without removing provider integrations, legal notices, or legitimate approval gates.

**Tech Stack:** Python, pytest, YAML, Markdown, Remotion/React, FFmpeg.

**Spec:** The maintainer's five-phase repository audit, cleanup, workflow protection, validation, and pull-request request of 2026-10-31.

## Global Constraints

- Work on `cleanup/remove-production-promotions`; leave `main` unchanged.
- Trace suspected promotions before editing; preserve copyright, licenses, attribution, and provider documentation.
- Preserve authentication, quotas, paid API requirements, safety limits, and legitimate approvals.
- Continue automatically through eligible stages; do not treat unused providers as blockers.
- Keep user-requested marketing content and necessary reference/attribution URLs usable.
- Report unavailable runtime/provider validation honestly; never claim live API generation from fixture tests.

## Review Focus

- Fully local jobs with unrelated missing API keys must proceed without setup pitches.
- A selected unavailable provider must still produce a clear error or an authorized supported fallback.
- Required credits and user-approved links must survive export.
- Educational videos without a CTA request must finish without subscription asks or forced end screens.
- Gated stages must still require approval or a valid recorded approval policy.

### Task 1: Inventory and trace

- [x] Search all tracked source and hidden instruction/configuration directories for promotions, URLs, redirects, and interruptions.
- [x] Trace agent entrypoints, registry setup metadata, publishing instructions, UI navigation, and render/export paths.
- [x] Capture baseline instruction behavior and project test results before changes.

### Task 2: Targeted cleanup

**Files:** `README.md`, `README_zh-CN.md`, `.github/FUNDING.yml`, `docs/SPONSORS.md`, `AGENT_GUIDE.md`, `skills/meta/onboarding.md`, relevant proposal/publish directors, `skills/creative/long-form.md`, `skills/creative/short-form.md`.

- [x] Remove funding/social/ranking solicitations and replace sponsor insertion guidance with the fork's no-promotion policy.
- [x] Scope setup guidance to the requested/selected path or an explicit setup question; retain registry metadata and provider checks.
- [x] Make CTA/end-screen/link additions depend on the approved brief; preserve credits and source citations.
- [x] Re-run instruction scenarios and inspect each modified instruction for conflicts.

### Task 3: Pipeline validation and regression coverage

**Files:** `tests/tools/test_clean_production_export.py`; render smoke outputs under ignored `projects/` or `tests/qa/output/`.

- [x] Exercise real local composition, audio, and export; verify no unsolicited text/links, unchanged media bytes at export, retained requested attribution, and clear errors.
- [x] Run all tests, project lint, and frontend type checking; compare failures with the baseline.
- [x] Run the existing full-stage QA simulation and a Remotion render, probe output streams, and fully decode the MP4s.

### Task 4: Review and delivery

**Files:** `docs/PRODUCTION_CLEANUP_AUDIT.md`.

- [x] Record original source lines, execution paths, exact changes, retained false positives, test evidence, and limitations.
- [x] Request independent review; resolve material findings and revalidate changed paths.
- [x] Prepare the validated changes for the explicitly requested commit, branch push, and pull request against this fork's `main`; final delivery is recorded in the pull request and response.

## Execution Ledger

- Base: `e99a2c62d2d2019cd34117f97691529dc8d25780`; clean starting tree on branch `work`.
- Execution: continue directly as authorized by the maintainer; the dedicated branch provides the requested isolation.
- Dependencies: installed development requirements into ignored `.venv`; existing Remotion dependencies and system FFmpeg/Chromium are present.
- Pre-flight: documentation and instruction changes share the common guide's production contract; provider APIs, schemas, manifests, and checkpoint code remain unchanged unless validation proves a related defect.

- Task 1 complete: baseline instructions reproduced setup/CTA/end-screen additions; baseline suite 2,228 passed, 11 skipped, 3 xfailed.
- Task 2 complete: targeted source cleanup; seven independent updated-instruction scenarios passed, including real blockers and requested attribution/CTA boundaries.
- Task 3 complete: final `make test` 2,230 passed, 11 skipped, 3 xfailed; lint and TypeScript checks passed; full-stage QA 38/38 and Remotion render passed; three MP4 paths fully decoded and export hashes matched.
- Final review: no unresolved Critical/Important findings. Corrected the remaining branded-intro schedule. Deferred existing minor instruction tensions (zero-key onboarding assumptions and generic gate reminders) are documented in `docs/PRODUCTION_CLEANUP_AUDIT.md`.
- Validation limits: no live paid calls, independent HyperFrames/GPU render, or live web research. Initial browser download failure resolved for validation with installed Chromium. Existing stock-adapter expected failures and test warnings are recorded in the audit.
