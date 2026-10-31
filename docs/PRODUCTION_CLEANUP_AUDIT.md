# Production cleanup audit — 2026-10-31

The confirmed problems were documentation promotions and agent instructions that added unsolicited setup offers or promotional endings. No advertising pop-up, sponsor overlay, affiliate redirect, or artificial render/export paywall was found in the first-party runtime paths inspected. Accordingly, this change fixes the instruction and documentation sources and adds real local media regression coverage; it does not claim to remove a nonexistent runtime advertising module.

## Scope and method

- Baseline: `e99a2c62d2d2019cd34117f97691529dc8d25780` on the fork's `main`; implementation branch: `cleanup/remove-production-promotions`.
- Inventoried all 2,237 tracked files, including 2,101 UTF-8 text files and 283 URL hostnames. Searched hidden instruction directories as well as ordinary source files; generated dependencies, private environment files, and Git history were excluded from source searches.
- Searched case-insensitively for sponsor, donate/donation, affiliate, advertisement, promotion, upgrade, subscribe, visit, support us, funding, tracking parameters, CTAs, external URLs, browser navigation, banners, pop-ups, and render/export stops. Reviewed the matches in context rather than deleting by keyword.
- Traced the agent entrypoints (`AGENTS.md`, `COPILOT.md`, `.github/copilot-instructions.md`, `CODEX.md`, `CLAUDE.md`, `CURSOR.md`, editor rules) into `AGENT_GUIDE.md`, `PROJECT_CONTEXT.md`, pipeline YAML, and stage/meta/creative skills, including the hidden `.agents/` and `.claude/` skill trees.
- Inspected registry capability/setup reporting, provider dependency and error paths, checkpoint approval enforcement, composition dispatch, Remotion components, local Backlot navigation, export packaging, templates, configuration, documentation, and asset references.

## Confirmed sources and changes

Line numbers below refer to the baseline commit, so removed content remains traceable. For example, `README.md:765` means the file at that baseline, not its shifted line number after cleanup.

| Confirmed component | Original source lines | Why it appeared / execution path | Exact change |
|---|---|---|---|
| Project website promotion | `README.md:15` | README rendering displayed an external website badge above the operating instructions | Removed the badge/link paragraph |
| GitHub ranking promotion | `README.md:34`; `README_zh-CN.md:29` | README HTML linked ranking badges to GitHub Trending | Removed the ranking paragraphs; retained unrelated assets |
| Social-follow badge block | `README.md:42`, `README.md:45`; `README_zh-CN.md:32`, `README_zh-CN.md:35` | README rendering displayed YouTube/X/community badges under a follow heading | Removed those badge/heading blocks; retained functional help/community references elsewhere |
| Forced YouTube subscription link | `README.md:105`; `README_zh-CN.md:83` | README rendering presented a channel subscription CTA with `sub_confirmation=1` | Removed the complete subscription paragraphs |
| Social follow solicitation | `README.md:725`; `README_zh-CN.md:653` | Contact sections asked readers to follow the upstream author's social account | Removed the follow sentences; kept issue/discussion help links |
| External star-history widget | `README.md:743` | README loaded linked chart images from an unrelated external host | Removed the star-history section |
| Star solicitation | `README.md:763`; `README_zh-CN.md:679` | README footer asked users to star the project | Removed both solicitations |
| Donation solicitation | `README.md:765` | README footer linked to the upstream author's GitHub Sponsors page | Removed the donation sentence |
| GitHub Sponsor button configuration | `.github/FUNDING.yml:1` | GitHub consumes `github: calesthio` as repository funding metadata | Removed this single-purpose configuration file; no workflow module was removed |
| Sponsor insertion instructions | `docs/SPONSORS.md:3`, `docs/SPONSORS.md:16`, `docs/SPONSORS.md:21`, `docs/SPONSORS.md:37` | Human/agent guidance supplied logo tables, website targets, and CTA snippets for future README advertising | Replaced with this fork's no-solicitation policy, explicitly preserving legal/trademark notices |
| Unrequested runtime installation suggestion | `AGENT_GUIDE.md:135` | All agent entrypoints load the guide; its single-runtime exception appended an optional HyperFrames install prompt | Removed that install prompt; retained runtime availability disclosure, decision logging, and runtime approval rules |
| All-provider setup pitches | `AGENT_GUIDE.md:280`, `AGENT_GUIDE.md:320`, `AGENT_GUIDE.md:352`, `AGENT_GUIDE.md:363`, `AGENT_GUIDE.md:719` | Registry `provider_menu_summary()` exposes setup metadata; guide required agents to lead with upgrades and present setup for every unavailable capability | Present the relevant working path; consult setup metadata only for a requested/approved capability gap or explicit setup question. Keep full internal discovery and real blocker reporting |
| Onboarding upgrade prompts | `skills/meta/onboarding.md:34`, `skills/meta/onboarding.md:66`, `skills/meta/onboarding.md:90`, `skills/meta/onboarding.md:97`, `skills/meta/onboarding.md:191` | Vague first requests route from the guide to onboarding, whose greeting template inserted optional upgrades | Replaced upgrades with a conditional relevant limitation, removed unrelated runtime-install pitches, and switched initial discovery to the compact summary with correct field guidance |
| Explainer setup diversion | `skills/pipelines/explainer/proposal-director.md:112` | Explainer proposal preflight instructed setup offers before designing around unavailable tools | Limit setup guidance to the requested/approved path; continue when available tools satisfy the brief |
| Animation provider pitches / cloud-key requirement | `skills/pipelines/animation/proposal-director.md:138`, `skills/pipelines/animation/proposal-director.md:145`, `skills/pipelines/animation/proposal-director.md:185`, `skills/pipelines/animation/proposal-director.md:187`, `skills/pipelines/animation/proposal-director.md:201`, `skills/pipelines/animation/proposal-director.md:203` | Animation proposal template displayed unavailable provider installation text and unconditional API-key requirements, including for approaches with local alternatives | Keep full scan internally; show relevant capabilities and genuine gaps. Describe cloud or local providers, and make setup contingent on the requested approach being unavailable |
| Default script CTA | `skills/pipelines/explainer/script-director.md:73`, `skills/pipelines/explainer/script-director.md:203` | Script structure and review criterion expected a CTA even for neutral explainers | End with the core recap; require a CTA only when requested by the approved brief |
| Default description subscription solicitation | `skills/pipelines/explainer/publish-director.md:38`, `skills/pipelines/explainer/publish-director.md:147`, `skills/pipelines/explainer/publish-director.md:163` | Publish director explicitly required subscribe/like/follow, and the review/pitfall instructions reinforced a CTA in every description; `export_bundle` writes the resulting agent-supplied text verbatim | Make CTA conditional on the approved brief; prohibit appended unrelated solicitations. Retain required credits and relevant citations; require supplied/verified destinations for approved product/channel links |
| Forced long-form promotional segments | `skills/creative/long-form.md:18`, `skills/creative/long-form.md:52`, `skills/creative/long-form.md:104`, `skills/creative/long-form.md:192`, `skills/creative/long-form.md:194`, `skills/creative/long-form.md:213`, `skills/creative/long-form.md:224`, `skills/creative/long-form.md:230`, `skills/creative/long-form.md:236`, `skills/creative/long-form.md:237`, `skills/creative/long-form.md:238` | Creative reference templates prescribed branding, subscribe mid-rolls, channel cards, next-content teasers, and 20 seconds reserved for an end screen | Default to topic transitions, evidence, and the concluding takeaway; make branding, cards, CTAs, and end screens conditional on the approved brief |
| Default short-form social CTA | `skills/creative/short-form.md:172`, `skills/creative/short-form.md:181`, `skills/creative/short-form.md:190` | Short-form timing templates allocated the ending to follow/share/comment or CTA overlays | Default endings to the useful result/takeaway and replay loop; retain CTAs only when the approved brief requests them |
| Provider credit promotion | `docs/PROVIDERS.md:679` | Provider setup documentation encouraged checking a console for promotional new-user credits | Replaced the promotion with neutral credential, billing, and quota requirements |

The new **Clean Production Contract** in `AGENT_GUIDE.md` applies through the existing agent entrypoints. It covers generated messages, scripts, compositions, descriptions, and delivery: relevant progress/errors only, automatic continuation through eligible stages, no unsolicited promotional additions, no invented link destinations, and preservation of legal attribution and genuine provider restrictions.

## Paths checked and intentionally preserved

- `COPILOT.md`, `.github/copilot-instructions.md`, and `PROJECT_CONTEXT.md` contain routing/architecture guidance, not advertisements. Their pointers already reach the corrected guide; duplicating the policy there would create competing sources of truth.
- Pipeline manifests and `lib/checkpoint.py` retain all legitimate approvals, prerequisite validation, failed-stage reporting, and recorded full-run approval-policy handling. No approval flags were disabled to make a run proceed.
- `tools/tool_registry.py` retains complete provider/setup metadata. This is diagnostic data, not an automatically displayed advertisement; the instruction to promote that data was the source of the unsolicited messages. Provider selection, missing-key errors, local/free providers, credential handling, supported fallbacks, quotas, budgets, and billing checks remain intact.
- `tools/video/video_compose.py`, `tools/video/hyperframes_compose.py`, `tools/publishers/export_bundle.py`, and the Remotion component tree contain no confirmed injected sponsor/subscribe overlay or promotional render/export blocker. `EndTag` and `ProviderChip` are explicit composition components, not automatic ads; they remain available for requested content.
- Backlot opens a loopback project board and observes production state. Its `subscribe()` calls are server-sent event subscriptions, not channel subscription prompts. Its external font stylesheet is a font resource with fallback fonts, not a promotional destination or production gate.
- Provider API/docs/setup URLs, stock-source provenance, research citations, examples for explicitly requested marketing videos, project help/contribution links, JSON Schema URLs, required font/OFL notices, upstream skill attribution, the AGPL license, and copyright notices are preserved.
- Dated fish.audio/HeyGen promotional-tier expiry, commercial-use, and quota warnings are retained because they prevent misleading free-tier/billing claims. Npm `upgrade`, HTTP upgrade headers, browser navigation helpers, FFmpeg `-hide_banner`, visual animation pattern interrupts, and UI modal examples were reviewed as false positives.
- Inactive sponsor/ranking/social-preview artwork was not deleted. It is not injected into production, and removing whole assets/modules would not fix the confirmed instruction paths.

## Validation evidence

### Instruction behavior

Before edits, an isolated agent followed the original instructions in five simulated situations. It produced optional cloud setup offers for an already functional local job and a data-graphics job, upgrade offers in an exploratory greeting, a subscribe/like sentence in a neutral educational description, and a forced subscription/next-video end screen. These outputs traced directly to the sources above. The baseline did **not** establish a hard render block from optional provider setup, nor did it invent an unrelated description URL.

After edits, a fresh independent reviewer applied the updated instructions to seven scenarios. All seven met the expected behavior:

| Scenario | Observed behavior |
|---|---|
| Approved local job; 15 unrelated cloud providers lack keys | "Preflight passed ... No additional setup is needed. I'm continuing to the next eligible stage." |
| Exploratory greeting; only FFmpeg/Remotion confirmed | Named working charts/text/motion graphics and existing-media editing; no setup pitch or unverified narration claim |
| Approved free data-graphics job | Continued locally with Remotion/FFmpeg and no paid calls or cloud setup diversion |
| Neutral educational YouTube description | Explained sky color; no subscription ask or external link |
| Final 20 seconds of a neutral 12-minute lesson | Resolved the opening question, delivered the takeaway, and held the concluding diagram; no promotional end screen |
| Selected Sora path lacks its required credential | Reported the missing `OPENAI_API_KEY`/Sora access, billing/quotas, and blocked selected path; no call or unilateral provider swap |
| Brief explicitly requests a product CTA and supplies a legal credit URL | Preserved both the requested CTA and supplied credit; invented no product destination |

These simulations test instruction application; they are not a guarantee of every future model response. Independent review found a remaining unconditional branded intro in the long-form schedule; it was corrected and independently rechecked before delivery.

### Automated and practical checks

- Baseline full suite: **2,228 passed, 11 skipped, 3 xfailed, 1 subtest passed**, exit 0.
- Final full suite (`make test`): **2,230 passed, 11 skipped, 3 xfailed, 1 subtest passed**, exit 0 in 165.64 seconds. The two added tests pass; no new failures, skips, or expected failures.
- Added `tests/tools/test_clean_production_export.py`: **2 passed**. Uses real local video/audio fixtures, `AudioMixer`, `VideoCompose`, `ExportBundle`, schema validation, full frame decoding, exact metadata comparisons, and byte-for-byte MP4 export comparison. Covers no injected overlay/intro/end card, no appended promotional metadata/URLs, and retained supplied legal attribution URL. Allows one mux boundary frame rather than falsely requiring exact AAC/video packet alignment.
- `make lint`: exit 0.
- `cd remotion-composer && npx --no-install tsc --noEmit`: exit 0.
- Full-stage smoke: `.venv/bin/python tests/qa/test_08_end_to_end.py`: **38 passed, 0 failed**, exit 0. Research, proposal, script, scene planning, assets, editing, composition, and publishing checkpoints complete in order. Research/creative/provider assets are synthetic fixtures; mixing and video composition are real, local tool executions. Approval flags belong to this test simulation and were not used to alter production policy.
- Additional real Remotion render: `npx --no-install remotion render src/index.tsx Explainer /workspace/OpenMontage/projects/demos/renders/code-to-screen.mp4 --props public/demo-props/code-to-screen.json --codec h264 --browser-executable /usr/bin/chromium --concurrency 2`: exit 0.
- Both smoke videos and the local export were probed and fully decoded using `ffprobe` and `ffmpeg -v error -xerror ... -f null -`, with exit 0 and no decode errors. The Remotion filmstrip was visually inspected; the two-second regression fixture checks every decoded pixel for unexpected overlays across all frames.
- Smoke production logs and exported text metadata were searched for unsolicited promotional messages and external URLs; no matches. MP4 probe metadata contains no external URLs. This does not claim semantic OCR of every frame of arbitrary user footage.

| Verified artifact (generated, gitignored) | Result |
|---|---|
| `projects/production-cleanup-smoke/renders/final.mp4` | 60.021 seconds, 1920×1080 H.264 video + AAC audio; full decode passed |
| `projects/production-cleanup-smoke/exports/video/output.mp4` | Valid local export; SHA-256 matches the final render byte-for-byte |
| `projects/demos/renders/code-to-screen.mp4` | 25.045 seconds, 1920×1080 H.264 video + AAC audio; full decode passed |
| `projects/production-cleanup-smoke/verification.json` | Paths, probe results, file sizes, hashes, and decoder status |

### Limits and environment issues

- The initial `render_demo.py code-to-screen` invocation failed clearly, with a nonzero exit and `EAI_AGAIN remotion.media`, while Remotion tried to download Chrome Headless Shell. The supported `--browser-executable /usr/bin/chromium` option rendered successfully using the installed browser; no network restriction was bypassed and no render error was hidden. The convenience demo command itself remains subject to that browser-download environment requirement.
- No live paid provider generation or live web research was attempted: this environment has no configured provider secrets. The full existing suite exercises provider contracts, routing/error/fallback handling, budget/approval governance, and local tools without billing real APIs. HyperFrames/GPU/live API rendering is not independently claimed as validated by these smoke runs.
- Three pre-existing strict expected failures remain: `tests/tools/test_stock_source_adapters.py::test_search_propagates_transport_errors[archive_org]`, `[wikimedia]`, and `[pond5_pd]`. Those adapters still swallow transport errors; this is a known limitation outside the promotional paths changed here, not a clean bill of health for every provider error path. Other skipped checks include opt-in live API/HyperFrames tests and missing golden/comparison media fixtures.
- Pytest emits an existing `pytest-asyncio` warning about the unset fixture loop scope; the QA harness also emits an existing fallback stage-order warning. These are reported rather than silenced. Skipped and expected-failure tests remain visible in the full-suite result.

## Independent review and retained limitations

The independent reviewer found no unresolved Critical or Important issues after the branded-intro correction and independently reran the new regression tests: **2 passed**. Two pre-existing minor instruction tensions are documented for maintainers:

- `skills/meta/onboarding.md` includes a zero-key example mentioning Piper/stock footage. These still require their actual dependencies; FFmpeg/Remotion availability alone does not establish them. The updated discovery contract and the scenario above report only verified capabilities.
- Some stage-director gate reminders say an earlier "go ahead" does not cover later gates, while the shared guide permits an explicit, recorded full-run approval policy. A generic earlier approval and a recorded full-run policy are distinct; existing checkpoint/manifest enforcement remains authoritative. This cleanup does not relax legitimate gates.

The reviewer did not claim live provider authentication/generation quality, paid-account quota readiness, network publishing, or legal sufficiency of supplied licenses from local fixture tests. Those limits remain explicit above.
