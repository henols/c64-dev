# MCP setup

This skill is designed to work with two MCP servers:

- `oscar64-docs-mcp`
- `c64-debug-mcp`

## Oscar64 Docs MCP

Purpose:
- search Oscar64 documentation
- inspect compiler/library usage
- find relevant tutorial pages and sample code
- ground code generation in documented APIs instead of memory

Public setup pattern:

```bash
npx -y oscar64-docs-mcp@latest
```

Environment notes:
- requires a recent Node.js runtime
- may use `OSCAR_MCP_CACHE_DIR` to control cache location

Use it for:
- headers
- compiler/library functions
- sprite APIs
- VIC-II usage patterns
- IRQ setup
- joystick handling
- examples and sample programs

## C64 Debug MCP

Purpose:
- drive VICE via remote monitor
- load and run programs
- set breakpoints
- inspect registers and memory
- inspect screen state and capture the display
- inject controlled input for testing

Public setup pattern:

```bash
npx -y c64-debug-mcp
```

VICE should be started with remote monitor enabled, for example:

```bash
x64sc -remotemonitor -remotemonitoraddress 127.0.0.1:6502
```

Use it for:
- `program_load`
- `execute`
- `breakpoint_set`
- `memory_read`
- `get_registers`
- `capture_display`
- `get_display_text`
- `joystick_input`

## Portability guidance

Do not hardcode MCP registration into the skill itself.

Instead:
- keep the skill focused on workflow and behavior
- keep MCP server wiring in agent-specific configuration files
- store example configs in `examples/` and `references/`

This makes the skill easier to use across OpenAI tools, Claude Code, and other MCP-capable agents.
