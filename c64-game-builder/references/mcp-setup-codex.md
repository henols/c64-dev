# Codex setup

This skill is structured so it can be kept in GitHub and used from a stable folder path.

## Recommended approach

1. Keep the core instructions in `SKILL.md`.
2. Keep MCP server registration outside the skill.
3. Keep the skill directory at a stable path such as `c64-game-builder/`.
4. Use the GitHub Actions workflow to rebuild `skill.zip` on changes.

## Why this structure works well

- portable skill instructions live in one place
- agent-specific metadata is optional
- MCP config can vary per environment without forcing changes to the skill

## Expected agent behavior

A coding agent should:
- inspect the repository and build flow first
- use Oscar64 docs before generating unfamiliar code
- use VICE-backed debugging when runtime correctness matters
- report what was confirmed in docs and what was confirmed in the emulator
