---
name: c64-game-builder
description: help an mcp-enabled coding agent create, extend, port, debug, and polish commodore 64 games when it has access to the oscar64-docs mcp server for compiler docs and samples and the c64-debug mcp server for live debugging in vice. use for gameplay feature work, rendering and sprite logic, input handling, sid or timing issues, memory-map decisions, breakpoint-driven debugging, screen verification, and iterative prg testing.
---

# C64 Game Builder

Use the two MCP servers as a tight loop:
1. Ask Oscar64 Docs for the right API, headers, constraints, and examples.
2. Make the smallest code change that can prove the idea.
3. Run the repository's existing build flow.
4. Use C64 Debug against VICE to verify behavior in memory, registers, and on screen.
5. Report what changed, what was verified, and what still needs work.

Never invent Oscar64 functions, headers, memory addresses, or hardware behavior when the docs server or live debugger can confirm them.

## Shared rules

- Read repository context first.
- Prefer Oscar64 C unless assembly is clearly warranted.
- Implement vertical slices: one visible behavior at a time.
- Separate verified facts from hypotheses.
- Do not claim a bug is fixed unless it was verified by a reproducible path, debugger evidence, or both.

## Oscar64 Docs MCP

Use the docs server first for discovery and grounding.

Default pattern:
1. Search for the gameplay or system topic.
2. Read the most relevant manual, API, and tutorial entries.
3. Find one or two sample programs close to the task.
4. Extract the exact function names, headers, constants, required setup, and constraints.
5. Then write or patch code.

## C64 Debug MCP

Use the debug server whenever compile success does not guarantee correct runtime behavior.

Recommended tool sequence:
1. `program_load`
2. `execute` or `wait_for_state`
3. `breakpoint_set`
4. `get_registers` or `memory_read`
5. `get_display_text`, `get_display_state`, or `capture_display`
6. `memory_write` or `set_registers` only for controlled experiments
7. `list_breakpoints` and `breakpoint_clear`

## Output format

For meaningful work, end with this structure:

### Result
State the concrete change, fix, or finding.

### Evidence
State what was confirmed from Oscar64 Docs and what was confirmed in the debugger.

### Files
List created or modified files.

### Next move
Propose the next smallest useful step.
