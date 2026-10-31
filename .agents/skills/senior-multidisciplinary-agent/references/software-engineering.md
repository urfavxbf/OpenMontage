# Software Engineering — senior workflow

## Discovery and design
Map the actual repository stack, architectural boundaries, dependency versions, test conventions, deployment path, observability, bottlenecks and security constraints. Prefer official practices and present repository style to default frameworks. Evaluate simplicity, failure modes, change risk and long-term ownership. Do not impose Android patterns on React/TypeScript/Remotion projects.

## Implementation
Define acceptance criteria and contract/interface changes. Prefer small cohesive units, explicit types, predictable errors, backpressure, cancellation, testable boundaries, safe concurrency and data migration plans. Separate domain logic from I/O and UI, avoiding needless abstraction. Never break working behavior to perform unrelated refactors.

## Testing
Start with a reproducible failing case for defects. Add focused unit and integration tests; inspect error, empty, loading and cancellation paths. Run the existing project tests, static checks and targeted builds, and use mocks only for genuine external boundaries. State tests that were not run and why. Do not claim coverage that was not measured.

## Review and security
Review changes for correctness, injection risks, auth/authz, data exposure, dependency vulnerabilities, configuration drift, performance regressions, accessibility, logging, licensing and privacy. Ensure API surface and database contracts remain compatible, or include migration/rollback. Be explicit about security-sensitive changes and minimize permissions.

## Repository-specific OpenMontage
OpenMontage is a Python-driven, instruction-directed production system with a registry of provider tools, pipeline manifests, stage director skills, Pydantic configuration, artifact schemas, and Remotion/HyperFrames/FFmpeg composition options. Read `AGENTS.md`, `AGENT_GUIDE.md`, `PROJECT_CONTEXT.md`, `CODEX.md` and relevant director skills before implementation. Keep production orchestration in the agent-driven pipeline; Python supplies tools/persistence, not an alternate orchestration path. Use the repository's `tests/`, schema/contract suites and `remotion-composer/` checks appropriate to each changed file, without assuming test dependencies are installed. For new tools use the `tools/base_tool.py` contract and registry conventions. Never add speculative provider defaults, skip budget approvals, or silently switch from atelier to templated or between composition engines.

## Handoff
Summarize changed files, reason for each architectural decision, verification outcomes, open risks, and how to revert. Use a feature branch/PR where authorized; never merge or release automatically.
