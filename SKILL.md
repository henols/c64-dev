---
name: c64-dev
description: Sets up a C64 development environment with oscar64 and c64debug. Use when the user wants to create or initialize a C64 project.
metadata:
  author: henrik
  version: "1.0.0"
---

# C64 Development Setup Skill

This skill sets up a complete Commodore 64 development environment with oscar64 compiler and c64debug MCP server integration.

## EXECUTION ORDER - READ THIS FIRST

**YOU MUST FOLLOW THIS ORDER EXACTLY:**

1. ✅ **Phase 1, Step 1.1:** Check oscar64docs MCP server - **BLOCKING**
2. ✅ **Phase 1, Step 1.2:** Check c64debug MCP server - **BLOCKING**
3. ❓ **Phase 1, Decision Point:**
   - If BOTH MCP servers found → Continue to Step 1.4
   - If EITHER MCP server missing → Display error, use AskUserQuestion, **EXIT SKILL IMMEDIATELY**
4. ✅ **Phase 1, Step 1.4:** Check oscar64 compiler binary (only if Step 3 passed) - **NON-BLOCKING**
5. ✅ **Phase 2:** Create project files (ONLY if Phase 1 succeeded)
6. ✅ **Phase 3:** Validation and summary report

**CRITICAL ORDER:**
- MCP servers MUST be checked FIRST (Steps 1.1 and 1.2)
- oscar64 compiler binary is checked AFTER MCP servers (Step 1.4)
- NEVER skip MCP server checks
- NEVER create files before both MCP servers are confirmed

## What This Skill Does

1. **Validates required MCP servers FIRST** (oscar64docs and c64debug) - **BLOCKING**
   - Checks oscar64docs MCP server
   - Checks c64debug MCP server
   - If either missing, auto-configures them in .claude/mcp.json
   - User must restart Claude Code and re-run the skill
2. **Then checks for oscar64 compiler binary** (only after MCP servers confirmed) - **NON-BLOCKING**
   - Guidance provided if missing
3. Creates a proper C64 project structure (only if MCP servers present)
4. Generates configuration files (Makefile, CLAUDE.md)
5. Creates an example starter program
6. Provides complete setup guidance

## Phase 1: Validate Required MCP Servers (MANDATORY - EXECUTION STOPS HERE IF FAILED)

**THIS IS NOT OPTIONAL. YOU MUST EXECUTE THESE CHECKS FIRST. DO NOT SKIP. DO NOT PROCEED WITHOUT COMPLETING THESE CHECKS.**

### Step 1.1: Check oscar64docs MCP Server

Execute this FIRST:
```
ReadMcpResourceTool(server="oscar64docs", uri="docs://oscar64/manual")
```

**Expected result:** Returns the oscar64 manual content
**If this fails:** oscar64docs MCP server is NOT configured → Go to Step 1.3 (Auto-Configure and Exit)

### Step 1.2: Check c64debug MCP Server

Execute this SECOND (only if Step 1.1 succeeded):
```
mcp__c64debug__get_session_state()
```

**Expected result:** Returns session state (may show "not connected" but the tool exists)
**If this fails or tool doesn't exist:** c64debug MCP server is NOT configured → Go to Step 1.3 (Block and Exit)

### Step 1.3: If EITHER Check Failed - AUTO-CONFIGURE MCP SERVERS

**If either MCP server is missing, the skill will configure them.**

**Step 1.3.1: Ask user where to configure MCP servers**

Use AskUserQuestion:
```
AskUserQuestion({
  questions: [{
    question: "MCP servers are not configured. Where would you like to configure them?",
    header: "MCP Location",
    options: [
      {
        label: "This project only",
        description: "Create .claude/mcp.json in the current directory (project-specific)"
      },
      {
        label: "All projects (global)",
        description: "Add to ~/.config/claude/config.json (applies to all your projects)"
      }
    ],
    multiSelect: false
  }]
})
```

**Step 1.3.2: Create configuration based on user choice**

**If user chose "This project only":**
1. **Create `.claude/` directory** in current working directory if it doesn't exist
2. **Create `.claude/mcp.json`** in current working directory with this exact configuration:

```json
{
  "mcpServers": {
    "oscar64docs": {
      "command": "npx",
      "args": ["-y", "oscar64-docs-mcp"]
    },
    "c64debug": {
      "command": "npx",
      "args": ["-y", "c64-debug-mcp"]
    }
  }
}
```

**If user chose "All projects (global)":**
1. **Check if `~/.config/claude/config.json` exists**
2. **If it exists:** Read it, merge the MCP server configuration, and write it back
3. **If it doesn't exist:** Create `~/.config/claude/` directory and create `config.json` with the configuration
4. **Create `~/.config/claude/config.json`** with this configuration (or merge into existing):

```json
{
  "mcpServers": {
    "oscar64docs": {
      "command": "npx",
      "args": ["-y", "oscar64-docs-mcp"]
    },
    "c64debug": {
      "command": "npx",
      "args": ["-y", "c64-debug-mcp"]
    }
  }
}
```

**Step 1.3.3: Display success message based on choice**

**If project-local configuration:**

---

**✅ MCP SERVERS CONFIGURED (PROJECT)**

I've created `.claude/mcp.json` in the current directory with the configuration for both required MCP servers:
- **oscar64docs** (oscar64-docs-mcp via npx) - Provides compiler documentation
- **c64debug** (c64-debug-mcp via npx) - Provides debugging and VICE integration

These servers will only be available for this project.

**IMPORTANT: You must restart Claude Code for the MCP servers to load.**

---

**If global configuration:**

---

**✅ MCP SERVERS CONFIGURED (GLOBAL)**

I've updated `~/.config/claude/config.json` with the configuration for both required MCP servers:
- **oscar64docs** (oscar64-docs-mcp via npx) - Provides compiler documentation
- **c64debug** (c64-debug-mcp via npx) - Provides debugging and VICE integration

These servers will be available for all your Claude Code projects.

**IMPORTANT: You must restart Claude Code for the MCP servers to load.**

---

**Step 1.3.4: Use AskUserQuestion to confirm restart:**

```
AskUserQuestion({
  questions: [{
    question: "MCP servers have been configured. Please restart Claude Code and re-run /c64-dev to continue. Ready to proceed?",
    header: "Restart Required",
    options: [
      {
        label: "I'll restart now",
        description: "I will restart Claude Code and run /c64-dev again"
      },
      {
        label: "Show config location",
        description: "Display where the MCP configuration was saved"
      }
    ],
    multiSelect: false
  }]
})
```

**Step 1.3.5: TERMINATE THE SKILL IMMEDIATELY**
   - Display appropriate message based on configuration location:
     - Project: "MCP configuration saved to `.claude/mcp.json`"
     - Global: "MCP configuration saved to `~/.config/claude/config.json`"
   - Display: "Please restart Claude Code and run `/c64-dev` again to continue"
   - **DO NOT PROCEED TO PHASE 2**
   - **DO NOT CREATE PROJECT FILES**
   - **DO NOT CHECK OSCAR64 COMPILER**
   - Exit skill execution now

---

**DECISION POINT - EVALUATE MCP SERVER CHECKS:**

**IF EITHER SERVER CHECK FAILED:**
- ❌ Display the missing server instructions above
- ❌ Use AskUserQuestion to block
- ❌ **TERMINATE - End the skill execution here**
- ❌ **DO NOT CHECK OSCAR64 COMPILER**
- ❌ **DO NOT PROCEED TO PHASE 2**

**ONLY IF BOTH SERVERS SUCCEEDED:**

If both `ReadMcpResourceTool(server="oscar64docs", ...)` succeeded AND `mcp__c64debug__get_session_state()` succeeded:

- ✅ Display: "✅ Both required MCP servers are configured and available"
- ✅ Continue to Step 1.4 below
- ✅ Then proceed to Phase 2 (project creation)

---

### Step 1.4: Check Oscar64 Compiler (Optional - Non-Blocking)

**ONLY EXECUTE THIS STEP IF BOTH MCP SERVERS WERE CONFIRMED IN STEPS 1.1 AND 1.2**

Check if oscar64 compiler binary is available (non-blocking):

Run: `oscar64 -h`

Note: oscar64 doesn't support `--version`, use `-h` instead

**If found:** Note for report - compiler is ready
**If not found:** Note for report - provide installation instructions in Phase 3 summary

**This check is non-blocking - continue to Phase 2 regardless of result.**

**Note on VICE Emulator:**
The c64debug MCP server handles VICE detection and configuration. No separate check is needed.

## Phase 2: Project Structure Setup

### Create Directory Structure

Create the following directory if it doesn't exist:
- `src/` - C source files

### Create Makefile

Generate a Makefile with oscar64 build rules:

```makefile
# Commodore 64 Project Makefile
# Compiler: oscar64

CC = oscar64
CFLAGS = -O2
TARGET = game.prg
SOURCES = $(wildcard src/*.c)

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) $(SOURCES) -o $(TARGET)

clean:
	rm -f $(TARGET)
	rm -f *.prg

run: $(TARGET)
	@echo "Load $(TARGET) into VICE with c64debug tools"
```

**IMPORTANT:** Only create if Makefile doesn't exist. If it exists, ask the user if they want to overwrite it.

### Create CLAUDE.md

Generate project documentation with C64 development guide:

```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Commodore 64 project written in C and compiled with oscar64. The project uses the VICE emulator for debugging and testing.

## Required MCP Servers

**CRITICAL**: This project REQUIRES two MCP servers to function. Without them, development is not possible:

1. **oscar64** - Provides access to the Oscar64 compiler manual
   - Access the manual: `ReadMcpResourceTool(server="oscar64docs", uri="docs://oscar64/manual")`
   - Essential for understanding compiler features, C64-specific APIs, and optimization techniques

2. **c64debug** - Provides all debugging and testing capabilities
   - Without this server, there is no way to load programs, debug code, or test the game
   - All program execution, memory inspection, and input simulation requires c64debug tools

**You must use these MCP servers** - they are not optional. Reference the oscar64 manual when writing C code, and use c64debug tools for all testing and debugging.

## Build System

The project uses a Makefile-based build system with the oscar64 compiler. Key commands:

- `make` - Build the project (compiles C files with oscar64 to .prg)
- `make clean` - Clean build artifacts

Oscar64 is a C compiler specifically designed for the Commodore 64 that produces optimized 6502 machine code.

## C64 Debugging

This project is configured with the c64debug MCP server for interactive debugging. The VICE emulator must be running with remote monitor enabled.

### Loading and Running Programs

Use the c64debug tools to interact with the running C64:
- `mcp__c64debug__program_load` - Load a .prg file into the emulator
- `mcp__c64debug__execute` - Control execution (pause, resume, step, reset)
- `mcp__c64debug__get_session_state` - Check if emulator is connected
- `mcp__c64debug__get_monitor_state` - Check if C64 is running or stopped

### Memory and Registers

- `mcp__c64debug__memory_read` / `memory_write` - Read/write C64 memory ($0000-$FFFF)
- `mcp__c64debug__get_registers` / `set_registers` - View/modify CPU registers (A, X, Y, PC, SP, FL)
- Always pause execution with `execute(action="pause")` before reading registers or writing memory

### Breakpoints and Debugging

- `mcp__c64debug__breakpoint_set` - Set execution, read, or write breakpoints
- `mcp__c64debug__list_breakpoints` - List all breakpoints
- `mcp__c64debug__breakpoint_clear` - Remove a breakpoint by ID
- `mcp__c64debug__wait_for_state` - Wait for emulator to reach a specific state

### Display and Input

- `mcp__c64debug__capture_display` - Capture screen to PNG file
- `mcp__c64debug__get_display_text` - Get current text screen contents
- `mcp__c64debug__get_display_state` - Get screen RAM, color RAM, and graphics mode
- `mcp__c64debug__write_text` - Type text into the C64 (requires running state)
- `mcp__c64debug__keyboard_input` - Send key presses (RETURN, CLR, HOME, F1-F8, etc.)
- `mcp__c64debug__joystick_input` - Send joystick input to port 1 or 2

## C64 Architecture Notes

### Memory Map
- `$0000-$00FF` - Zero page (fast access)
- `$0100-$01FF` - Stack
- `$0400-$07FF` - Default screen RAM (1000 bytes)
- `$D000-$DFFF` - I/O (VIC-II at $D000-$D3FF, SID at $D400-$D7FF, CIA at $DC00-$DDFF)
- `$D800-$DBFF` - Color RAM
- `$E000-$FFFF` - KERNAL ROM

### VIC-II Registers (Video)
- `$D000-$D001` - Sprite 0 X/Y position
- `$D010` - Sprite X MSB
- `$D015` - Sprite enable
- `$D020` - Border color
- `$D021` - Background color

### Timing
- PAL: 312 raster lines, 63 cycles per line
- Raster interrupts commonly used for game logic and graphics updates

## Development Workflow

1. Write C code (oscar64 compiles to optimized 6502 machine code)
2. Build with `make`
3. Load into VICE with `mcp__c64debug__program_load`
4. Use breakpoints and stepping to debug
5. Capture display to verify visual output
6. Test with keyboard/joystick input

## Common Debugging Patterns

When debugging crashes or unexpected behavior:
1. Check `get_monitor_state` to see stop reason and PC
2. Read registers with `get_registers` to inspect A, X, Y, SP
3. Read memory around PC to see current instructions
4. Set breakpoints at key game loop points
5. Step through code with `execute(action="step")`

When implementing new features:
1. Set breakpoints at entry points
2. Use `memory_read` to verify data structures
3. Capture display to verify visual changes
4. Use `wait_for_state` to ensure stable execution state
```

**IMPORTANT:** Only create if CLAUDE.md doesn't exist. If it exists, inform the user and skip creation.

### Create Example src/main.c

Generate a simple starter program:

```c
// C64 Starter Program
// Compiled with oscar64

#include <c64/vic.h>
#include <c64/sid.h>
#include <stdio.h>

// VIC-II color constants
#define COLOR_BLACK     0
#define COLOR_WHITE     1
#define COLOR_RED       2
#define COLOR_CYAN      3
#define COLOR_PURPLE    4
#define COLOR_GREEN     5
#define COLOR_BLUE      6
#define COLOR_YELLOW    7
#define COLOR_ORANGE    8
#define COLOR_BROWN     9
#define COLOR_LIGHT_RED 10
#define COLOR_DARK_GRAY 11
#define COLOR_GRAY      12
#define COLOR_LIGHT_GREEN 13
#define COLOR_LIGHT_BLUE 14
#define COLOR_LIGHT_GRAY 15

void main(void) {
    // Set border and background colors
    vic.color_border = COLOR_BLACK;
    vic.color_back = COLOR_BLUE;

    // Clear screen and set text color
    printf("\x93");  // Clear screen (PETSCII code)

    // Print welcome message
    printf("\n\n");
    printf("  commodore 64 starter program\n");
    printf("  compiled with oscar64\n\n");
    printf("  press any key to continue...\n");

    // Wait for keypress
    getchar();

    // Main loop
    while(1) {
        // Your C64 program logic here

        // Example: Cycle border color
        vic.color_border++;
        vic.color_border &= 0x0F;

        // Small delay
        for(int i = 0; i < 1000; i++) {
            // Busy wait
        }
    }
}
```

**IMPORTANT:** Only create if src/main.c doesn't exist. If it exists, inform the user and skip creation.

## Phase 3: Validation and Summary

**Note:** This phase only runs if both MCP servers were found in Phase 1.

### Test Build (If oscar64 is available)

If oscar64 compiler was detected in Phase 1, run `make` to verify the project compiles successfully. If oscar64 is not available, skip the build and note it in the report.

### Summary Report

Display a comprehensive report including:

1. **MCP Servers Status**
   - oscar64: ✓ Available (confirmed - Phase 1 would have blocked if missing)
   - c64debug: ✓ Available (confirmed - Phase 1 would have blocked if missing)

2. **System Tools Status**
   - oscar64 compiler: ✓ Installed / ✗ Not found

3. **Project Files Created**
   - List all files created
   - Note any files that were skipped (if user chose not to overwrite)

4. **Build Status**
   - ✓ Project builds successfully (if oscar64 is installed)
   - ⚠️ Build skipped (if oscar64 is not installed)

5. **Next Steps**
   - **If oscar64 compiler is missing:**
     - Download link: https://github.com/drmortalwombat/oscar64/releases
     - PATH setup instructions
     - After installing, run `make` to build
   - **Development workflow:**
     - Build the project with `make`
     - Load and run the program using c64debug tools
     - See CLAUDE.md for complete development workflow
     - Use c64debug MCP server for interactive debugging

## Phase 4: Troubleshooting

### Common Issues

**MCP Server Connection Failures:**
- Verify MCP servers are properly configured in Claude Code/Desktop settings
- Restart Claude Code/Desktop after modifying MCP server configuration
- Check MCP server logs for errors
- Ensure the server command and arguments are correct in the configuration file

**Oscar64 Compiler Errors:**
- Verify PATH includes oscar64 binary location
- Check oscar64 version compatibility
- Consult oscar64 manual via MCP: `ReadMcpResourceTool(server="oscar64docs", uri="docs://oscar64/manual")`

**c64debug Connection Issues:**
- Check if c64debug MCP server is properly configured
- Use `mcp__c64debug__get_session_state` to check connection status
- If VICE is not running or not configured, c64debug will provide specific guidance
- Refer to c64debug MCP documentation for VICE setup requirements

**Permission Issues:**
- Verify `.claude/settings.json` has all required permissions
- Check file permissions on project directory
- Ensure Makefile is executable

**Build Errors:**
- Check C syntax (oscar64 is C99-like but not fully compatible)
- Verify all source files are in `src/` directory
- Check for missing includes or libraries
- Consult oscar64 manual for platform-specific APIs

## Implementation Instructions

**CRITICAL EXECUTION ORDER - FOLLOW EXACTLY:**

### Phase 1: MCP Server Validation (BLOCKING - NO EXCEPTIONS)

**Execute these steps in EXACT order:**

**Step 1.1: Check oscar64 MCP Server (FIRST CHECK - BLOCKING)**
```
ReadMcpResourceTool(server="oscar64docs", uri="docs://oscar64/manual")
```
- If succeeds → Continue to Step 1.2
- If fails → Go to Step 1.3 (Block and Exit)

**Step 1.2: Check c64debug MCP Server (SECOND CHECK - BLOCKING)**
```
mcp__c64debug__get_session_state()
```
- If succeeds → Continue to Decision Point
- If fails → Go to Step 1.3 (Block and Exit)

**Decision Point: Evaluate MCP Server Results**

```
IF (Step 1.1 succeeded) AND (Step 1.2 succeeded):
    ✅ Display: "Both MCP servers confirmed available"
    ✅ Go to Step 1.4 (check oscar64 compiler binary)
    ✅ Then go to Phase 2 (create files)

ELSE (either Step 1.1 OR Step 1.2 failed):
    ⚙️  Auto-configure MCP servers:
        1. Ask user: "This project only" or "All projects (global)"?
        2. If "This project only":
           - Create .claude/ directory in current directory
           - Write .claude/mcp.json with correct npx configuration
        3. If "All projects (global)":
           - Create ~/.config/claude/ directory if needed
           - Write or merge into ~/.config/claude/config.json
        4. Display success message (show location used)
        5. Use AskUserQuestion to prompt restart
    ❌ DO NOT CHECK OSCAR64 COMPILER BINARY
    ❌ DO NOT CREATE ANY PROJECT FILES
    ❌ EXIT SKILL IMMEDIATELY
    ❌ Tell user to restart Claude Code and re-run /c64-dev
```

**Step 1.4: Check oscar64 Compiler Binary (ONLY IF BOTH MCP SERVERS CONFIRMED)**
   - Run: `oscar64 -h` (note: oscar64 doesn't support --version)
   - If found: note for report
   - If not found: note for report, provide installation instructions later
   - This is NON-BLOCKING - continue to Phase 2 regardless

2. **Create project structure (Phase 2) - only if MCP servers are available**
   - Create `src/` directory
   - Create `Makefile`
   - Create `CLAUDE.md`
   - Create `src/main.c`
   - **Check for existing files before creating them**
   - Use `AskUserQuestion` to ask about overwriting existing files if they exist

3. **Validate and report (Phase 3)**
   - If oscar64 compiler is available: attempt to run `make` to test build
   - If oscar64 is not available: skip build, provide installation instructions
   - Display comprehensive summary report with:
     - What was detected (MCP servers, oscar64)
     - What was created (project files)
     - Next steps (install oscar64 if missing, start developing)

## Non-Destructive Operation

This skill is designed to be non-destructive:
- Never overwrite existing files without user consent
- Check for file existence before creation
- Provide clear warnings about what will be created
- Allow user to cancel at any point

## Success Criteria

### Full Success (MCP servers available):
- ✅ Both oscar64 and c64debug MCP servers are detected and available
- ✅ Project structure has been created (`src/` directory)
- ✅ Configuration files are in place (Makefile, CLAUDE.md)
- ✅ Example program has been created (src/main.c)
- ✅ User has clear next steps for development

### Partial Success (MCP servers missing):
- ⚠️ One or both MCP servers are not configured
- ✅ User receives detailed instructions for configuring MCP servers
- ✅ User understands they need to configure MCP servers and re-run the skill
- ❌ Project files are NOT created (user must fix MCP configuration first)
