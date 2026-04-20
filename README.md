# C64 Development Setup Skill

This repository contains C64 development resources and an agent-ready skill for Commodore 64 work.

## Main skill folder

The portable packaged skill now lives in:

- `c64-game-builder/`

That folder contains:
- `SKILL.md` for the portable agent instructions
- `references/` for setup and workflow notes
- `examples/` for MCP configuration examples
- `scripts/` for validation and packaging
- `.github/workflows/build-skill.yml` for CI packaging

## Legacy setup notes

A previous repo-level setup flow focused on creating a complete Commodore 64 development environment.
The newer `c64-game-builder/` folder is the preferred location for the reusable skill package and GitHub-based distribution.

## What the packaged skill supports

- Oscar64 documentation lookup through MCP
- VICE-backed runtime debugging through MCP
- gameplay feature work
- sprite and character rendering
- joystick and keyboard input
- memory-map decisions
- breakpoint-driven debugging
- visual verification in the emulator

## Packaging

The GitHub Actions workflow packages the skill from the `c64-game-builder/` subfolder and uploads `skill.zip` as an artifact.

## Suggested MCP stack

Use the skill together with:
- `oscar64-docs-mcp`
- `c64-debug-mcp`

The goal is to support portable use across coding agents by keeping skill instructions separate from agent-specific MCP configuration.
