# C64 Game Builder

Portable Agent Skill for Commodore 64 game development with Oscar64 and VICE-backed debugging.

This repository is designed to work well across multiple coding agents by separating:

- the reusable agent instructions in `SKILL.md`
- agent-specific metadata in `agents/openai.yaml`
- agent-specific MCP setup examples in `references/` and `examples/`

## Install this skill

Choose the install path that matches your agent.

### Install from `skill.zip`

Use this when your agent supports importing packaged skills.

1. Download the latest `skill.zip` from a GitHub release or a successful GitHub Actions run
2. Import that zip into your coding agent
3. Configure the required MCP servers in the agent environment

### Install from the source folder

Use this when your agent supports installing from a GitHub directory or local folder.

Canonical skill folder:

- `c64-game-builder/`

That folder contains the full portable skill source.

### Required MCP servers

For full functionality, configure:
- `oscar64-docs-mcp`
- `c64-debug-mcp`

Keep MCP server registration outside the skill itself.

## What this skill does

The skill teaches an MCP-enabled coding agent how to build and debug Commodore 64 games by using two MCP servers together:

- `oscar64-docs-mcp` for grounded Oscar64 compiler docs, headers, tutorials, and samples
- `c64-debug-mcp` for live runtime debugging against VICE

The skill is optimized for:

- gameplay slices
- sprite and character rendering
- joystick and keyboard input
- memory map decisions
- IRQ and timing work
- debugger-driven bug fixing
- visual verification in the emulator

## Repository layout

```text
.
├── SKILL.md
├── README.md
├── LICENSE.txt
├── agents/
│   └── openai.yaml
├── references/
│   ├── debug-playbook.md
│   ├── mcp-setup.md
│   ├── mcp-setup-claude.md
│   ├── mcp-setup-codex.md
│   └── session-templates.md
├── scripts/
│   ├── __init__.py
│   ├── package_skill.py
│   ├── quick_validate.py
│   └── validate_env.sh
└── examples/
    └── claude-project.mcp.json
```

## Compatibility model

This repo is intentionally split into:

- a portable core skill that can be read by a broad range of agents
- optional OpenAI-specific metadata in `agents/openai.yaml`
- per-agent MCP setup notes under `references/`

### OpenAI / ChatGPT / Codex

Use the skill folder directly or package it into `skill.zip`.

### Claude Code

Use the checked-in MCP example as the starting point for a project-scoped `.mcp.json`.

## Packaging and distribution

### Local packaging

Run:

```bash
python scripts/quick_validate.py .
python scripts/package_skill.py . dist
```

This writes:

```text
dist/skill.zip
```

### GitHub Actions build

The repository root workflow at `../.github/workflows/build-c64-game-builder.yml`:
- validates the skill on push and pull request
- builds `dist/skill.zip`
- uploads `skill.zip` as a workflow artifact
- creates a GitHub release and attaches `skill.zip` when a `v*` tag is pushed

## MCP setup

Read:
- `references/mcp-setup.md`
- `references/mcp-setup-claude.md`
- `references/mcp-setup-codex.md`

The checked-in example config is:
- `examples/claude-project.mcp.json`

## Practical usage advice

For best results in coding agents:
- keep the MCP server configuration outside the skill itself
- keep the skill directory at a stable path in GitHub
- prefer a docs-first, debugger-second workflow
- verify visible behavior in VICE before claiming a game feature works

## License

MIT
