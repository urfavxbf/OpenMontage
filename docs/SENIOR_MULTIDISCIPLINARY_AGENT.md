# Senior Multidisciplinary Agent — OpenMontage fork

This fork adds an optional senior multidisciplinary custom agent and Agent Skill with a shared code/quality/research/video playbook.

## Files and discovery

- **VS Code/Copilot custom agent**: `.github/agents/senior-multidisciplinary.agent.md`
- **Copilot Agent Skill**: `.github/skills/senior-multidisciplinary-agent/SKILL.md`
- **Codex workspace Agent Skill**: `.agents/skills/senior-multidisciplinary-agent/SKILL.md`

The skill trees are intentionally identical; update both copies together. The existing `.agents/skills/SENIOR-SKILL.md` is preserved as a legacy standalone copy; **use the folder's `SKILL.md`** for correct reference discovery.

## First action and precedence

1. Read `AGENTS.md` → `AGENT_GUIDE.md` and `PROJECT_CONTEXT.md`.
2. For video work, follow the chosen `pipeline_defs/` YAML, run tool/registry preflight, read director skills under `skills/pipelines/` and relevant vendor Layer 3 skills under `.agents/skills/`.
3. Use the senior skill as an **additional** engineering, research, security and motion-quality reference. It does not replace OpenMontage provider/runtimes choices, approvals, checkpoints, append-only decision log or budget rules.
4. When Remotion and HyperFrames are both available, offer both choices; don't infer selection from the assistant's preferences. No secret/paid tool/media publishing rights come from installing a skill.

## Verification

```bash
python3 .agents/skills/senior-multidisciplinary-agent/scripts/validate_skill.py
python3 .github/skills/senior-multidisciplinary-agent/scripts/validate_skill.py
diff -qr .agents/skills/senior-multidisciplinary-agent .github/skills/senior-multidisciplinary-agent
python3 .agents/skills/senior-multidisciplinary-agent/scripts/doctor.py
```

Validation is offline and standard-library only. The doctor is read-only and reports available programs; it does not install dependencies.

## Usage

In a compatible VS Code/Copilot Chat environment, open the agent selector and choose **Senior Multidisciplinary Engineer**. For Codex or other skill-aware runtimes, ask to **use the `senior-multidisciplinary-agent` skill**. Actual discovery depends on runtime support and available workspace context.

**Sample:** "Use the Senior Multidisciplinary Engineer agent. First read AGENT_GUIDE.md and PROJECT_CONTEXT.md, then audit the selected OpenMontage video production pipeline, stage contracts, provider costs, media validation and test coverage; do not change files yet."
