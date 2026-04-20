# C64 Game Builder

This repository hosts an agent-ready skill for Commodore 64 game development.

## Main skill folder

The canonical skill lives in:

- `c64-game-builder/`

That folder contains:
- `SKILL.md` for the portable agent instructions
- `references/` for setup and workflow notes
- `examples/` for MCP configuration examples
- `scripts/` for validation and packaging

## Install the skill

Choose the install method that matches your coding agent.

### Install from a packaged zip

Use the latest packaged `skill.zip` from the repo releases or from a GitHub Actions artifact.

Typical flow:
1. Open the latest release or a successful workflow run
2. Download `skill.zip`
3. Import or add that zip in the coding agent that supports packaged skills

### Install from the GitHub folder

If your coding agent supports installing a skill from a GitHub directory, point it at:

- `c64-game-builder/`

This is the canonical source folder for the skill.

### MCP requirement

To get full value from the skill, configure these MCP servers in your agent environment:
- `oscar64-docs-mcp`
- `c64-debug-mcp`

The skill itself contains workflow guidance. MCP server registration should stay outside the skill in agent-specific configuration.

## What the skill supports

- Oscar64 documentation lookup through MCP
- VICE-backed runtime debugging through MCP
- gameplay feature work
- sprite and character rendering
- joystick and keyboard input
- memory-map decisions
- breakpoint-driven debugging
- visual verification in the emulator

## Packaging

The GitHub Actions workflow at `.github/workflows/build-c64-game-builder.yml` packages the skill from the `c64-game-builder/` subfolder and uploads `skill.zip` as an artifact.

## Suggested MCP stack

Use the skill together with:
- `oscar64-docs-mcp`
- `c64-debug-mcp`

The goal is to support portable use across coding agents by keeping skill instructions separate from agent-specific MCP configuration.
