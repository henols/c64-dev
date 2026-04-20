# Session templates

Use these templates when the agent should structure its work more explicitly.

## New feature template

### Goal
What visible game behavior should exist after this change?

### Docs grounding
What Oscar64 docs, headers, or samples were checked?

### Plan
- file to edit
- data to add
- runtime risk
- smallest testable slice

### Verification
How will VICE or the debug MCP server prove success?

## Bug-fix template

### Symptom
What is happening now?

### Reproduction
Exact steps to reproduce.

### Evidence
What did docs confirm?
What did the debugger confirm?

### Patch
What changed?

### Verification
How was the fix re-tested?

## Optimization template

### Bottleneck
What is too slow, too large, or too unstable?

### Current evidence
What runtime observations support that claim?

### Change
What single optimization lever is being changed now?

### Result
What improved and what stayed the same?
