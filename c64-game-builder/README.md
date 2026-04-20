# C64 Game Builder

Portable Agent Skill for Commodore 64 game development with Oscar64 and VICE-backed debugging.

This repository is designed to work well across multiple coding agents by separating:

- the reusable agent instructions in `SKILL.md`
- agent-specific metadata in `agents/openai.yaml`
- agent-specific MCP setup examples in `references/` and `examples/`

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
│   └── validate_env.sh
├── examples/
│   └── claude-project.mcp.json
└── .github/
    └── workflows/
        └── build-skill.yml
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

A GitHub Actions workflow is included at `.github/workflows/build-skill.yml`.

It will:
- validate the skill on push and pull request
- build `dist/skill.zip`
- upload `skill.zip` as a workflow artifact
- attach `skill.zip` to published GitHub releases

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
