#!/usr/bin/env bash
set -euo pipefail

echo "Checking local environment for C64 Game Builder"

if command -v node >/dev/null 2>&1; then
  echo "[ok] node: $(node --version)"
else
  echo "[warn] node is not installed"
fi

if command -v npm >/dev/null 2>&1; then
  echo "[ok] npm: $(npm --version)"
else
  echo "[warn] npm is not installed"
fi

if command -v npx >/dev/null 2>&1; then
  echo "[ok] npx is available"
else
  echo "[warn] npx is not installed"
fi

if command -v python3 >/dev/null 2>&1; then
  echo "[ok] python3: $(python3 --version)"
else
  echo "[warn] python3 is not installed"
fi

if command -v x64sc >/dev/null 2>&1; then
  echo "[ok] VICE x64sc is available"
else
  echo "[warn] VICE x64sc not found in PATH"
fi

echo

echo "Expected MCP servers:"
echo "  - oscar64-docs-mcp"
echo "  - c64-debug-mcp"
echo

echo "Example docs server launch:"
echo "  npx -y oscar64-docs-mcp@latest"
echo

echo "Example debug server launch:"
echo "  npx -y c64-debug-mcp"
echo

echo "Example VICE launch:"
echo "  x64sc -remotemonitor -remotemonitoraddress 127.0.0.1:6502"
