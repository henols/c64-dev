# Debug playbook

Use this file when the coding agent needs a more concrete runtime-debug checklist.

## General strategy

1. Reproduce the problem with minimal steps.
2. Confirm the intended API or hardware behavior in Oscar64 docs.
3. Load the built program into VICE through the debug MCP server.
4. Set the narrowest breakpoint that can prove or disprove the current hypothesis.
5. Inspect registers, memory, and visible output.
6. Change code only after evidence points to a likely cause.

## Sprite problems

Check:
- sprite enable path
- X and Y coordinates
- sprite data location
- sprite pointer setup
- sprite color and priority
- whether update logic actually runs each frame

Useful debug actions:
- inspect sprite-related memory
- capture the display
- step around the initialization path

## Input problems

Check:
- expected joystick port
- keyboard scan logic
- whether input is polled in the main loop or IRQ
- whether game state ignores valid input

Useful debug actions:
- run to the input handler
- inspect state variables before and after input processing
- use controlled input if the MCP server supports it

## Screen corruption

Check:
- screen RAM location
- color RAM writes
- charset location and bank assumptions
- accidental overwrites by game logic or data loading

Useful debug actions:
- inspect the relevant memory region
- compare expected and actual character bytes
- capture the screen before and after the suspected corruption point

## Crash or freeze

Check:
- program counter
- stack pointer
- last known good state
- IRQ setup and re-entry risk
- recent pointer arithmetic or memory copy logic

Useful debug actions:
- breakpoint near the last visible good frame
- inspect stack and surrounding memory
- step through hot control-flow paths

## Reporting format

End with:
- exact symptom
- evidence collected
- likely cause
- patch applied
- verification performed
- remaining uncertainty, if any
