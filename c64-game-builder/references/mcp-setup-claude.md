# Claude Code setup

This project supports Claude Code by keeping MCP wiring outside the skill and checking in an example project config.

## Recommended approach

1. Keep the reusable workflow in `SKILL.md`.
2. Configure MCP servers in a project-scoped `.mcp.json`.
3. Start VICE with remote monitor enabled before using the debug server.

## Example config

See:

- `examples/claude-project.mcp.json`

Typical shape:

```json
{
  "mcpServers": {
    "oscar64-docs": {
      "command": "npx",
      "args": ["-y", "oscar64-docs-mcp@latest"]
    },
    "c64-debug": {
      "command": "npx",
      "args": ["-y", "c64-debug-mcp"]
    }
  }
}
```

## Runtime expectations

Claude should use the docs server first to confirm APIs and examples, then use the debug server to validate runtime behavior in VICE.

The skill should not assume automatic build commands. It should inspect the repository first and then use the repository’s existing build flow.
