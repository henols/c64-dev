# C64 Development Setup Skill

A Claude Code skill that automates the setup of a complete Commodore 64 development environment.

## Features

- Validates MCP server availability (oscar64 and c64debug)
- Checks for oscar64 compiler installation
- Creates proper project structure with source directories
- Generates Makefile for building C64 programs
- Creates comprehensive CLAUDE.md with C64 development guide
- Provides example starter program
- Non-destructive: asks before overwriting files

## Usage

In Claude Code, invoke the skill with:

```
/c64-dev
```

Or ask Claude to set up a C64 project:
> "Set up a new C64 development project"

## What Gets Created

When you run this skill in a directory, it creates:

```
.
├── src/
│   └── main.c                 # Example starter program
├── Makefile                   # Build configuration
└── CLAUDE.md                  # Development guide
```

## Required MCP Servers

**IMPORTANT:** This skill requires both MCP servers to be configured before it can create your project:

1. **oscar64docs MCP Server** (REQUIRED) - Provides compiler documentation
2. **c64debug MCP Server** (REQUIRED) - Provides debugging capabilities and VICE integration

If either MCP server is missing, the skill will:
- Ask if you want project-local (`.claude/mcp.json`) or global (`~/.config/claude/config.json`) configuration
- Automatically create the configuration file with the correct MCP server settings
- Ask you to restart Claude Code
- Wait for you to restart and re-run the skill

## Optional Components

3. **oscar64 Compiler** - Compiles C code to C64 .prg files (recommended but not required for project creation)

## After Setup

Once setup is complete:

1. Build your program:
   ```bash
   make
   ```

2. Load into VICE using c64debug tools:
   ```
   mcp__c64debug__program_load(filePath="game.prg")
   ```

3. Start coding your C64 program!

If VICE is not running or not configured properly, c64debug will provide specific guidance.

## Development Workflow

1. Write C code in `src/` directory
2. Build with `make`
3. Load and run using c64debug tools
4. Debug using breakpoints and memory inspection
5. Test with keyboard/joystick input
6. Capture display to verify output

## Troubleshooting

See the SKILL.md file Phase 4 section for detailed troubleshooting guidance on:
- MCP server connection issues
- Compiler errors
- c64debug and VICE connection issues
- Permission problems

## Version

1.0.0 - Initial release

## Author

henrik
