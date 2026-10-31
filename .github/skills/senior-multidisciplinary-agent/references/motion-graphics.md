# Motion Graphics, Video and Audio — senior workflow

## OpenMontage's existing pipeline contract has precedence
Read root `AGENTS.md` → `AGENT_GUIDE.md`, then `PROJECT_CONTEXT.md`. All production goes through an approved `pipeline_defs/*.yaml` manifest, stage director skills under `skills/pipelines/`, tool registry preflight and appropriate Layer 3 skills. For a supplied reference video, use `skills/meta/video-reference-analyst.md`. Propose choices, budget and review gates before paid or consequential generation. Do not bypass cost or provider decisions with ad-hoc scripts. When both Remotion and HyperFrames are available, explain both and obtain the user's runtime approval. Honor composition_mode choice (atelier versus templated), provenance and user approval checkpoints. Preserve approved voices/artwork/creative commitments; this senior skill is **not** a substitute production pipeline.

## Creative direction
Translate the brief into audience, visual hierarchy, narrative arc, timing, typography, compositing strategy, color and motion language. Define scenes, source assets, transitions, audio beats, and safe areas. Keep text legible on phones and maintain intentional easing, motion continuity, rhythm, negative space and contrast. Avoid movement with no narrative purpose.

## Engineering pipeline
Check repository lockfiles and existing Remotion composition definitions. Prefer deterministic, frame-based animations driven by `useCurrentFrame()` and `interpolate()` rather than wall-clock timers. Avoid nondeterministic random values, remote unpinned assets and browser-dependent effects. For FFmpeg, probe streams with `ffprobe` before transcoding, specify frame rate, sample rate, pixel format, audio codec and output container, and verify mapping and timestamps.

## Rendering and quality assurance
Inspect representative still frames, transitions, captions and audio sync; ensure frame 0, boundaries, last frame and long-tail sections render. Inspect resolution, duration, frame rate, codec, audio peak/clipping, silence and black frames. Compare target platform specs. Use bounded render resolution/concurrency in Codespaces and note when GPU or paid services are unavailable. Do not claim a video is rendered unless the artifact exists and was inspected.

## Asset governance
Maintain exact references, license records, consent where required, source and generated asset provenance, and repeatable render parameters. Respect portrait or character identity constraints. Preserve source materials and never publish or upload media without authorization.

## Delivery checklist
Provide actual output path, duration, dimensions, fps, codecs, source dependencies, reproducibility command and verified playback or frame tests. Note any incomplete render or quality limitations explicitly.
