#!/bin/bash
# Rebuilds /tmp working copy from repo + starts http.server on :8765
# Use this after /tmp is wiped (macOS overnight cleanup) to restore design preview.
#
# Usage:  bash docs/design/master-audit-may30/scripts/start-design-server.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
WORK_DIR="/tmp/smuppy-v2-recovery"
DEST="$WORK_DIR/maquettes"

echo "[design-server] Rebuilding $WORK_DIR from repo..."
mkdir -p "$DEST/harmonized"

# Copy maquettes from creator-config-may28 (creator V2 monetization)
if [ -d "$REPO_ROOT/docs/design/creator-config-may28/maquettes/harmonized" ]; then
  cp -R "$REPO_ROOT/docs/design/creator-config-may28/maquettes/harmonized/." "$DEST/harmonized/"
  cp "$REPO_ROOT/docs/design/creator-config-may28/maquettes/build_creator_config_v2.py" "$DEST/" 2>/dev/null || true
fi

# Copy maquettes from master-audit-may30 (AUTH + future sprints)
if [ -d "$REPO_ROOT/docs/design/master-audit-may30/maquettes/harmonized" ]; then
  cp -R "$REPO_ROOT/docs/design/master-audit-may30/maquettes/harmonized/." "$DEST/harmonized/"
fi

# Copy build scripts to working dir so re-run is easy
cp "$REPO_ROOT/docs/design/master-audit-may30/build_auth_v2.py" "$DEST/" 2>/dev/null || true

# Copy external_screens (V2 canonical home_feed + settings)
if [ -d "$REPO_ROOT/docs/design/creator-config-may28/external_screens" ]; then
  rm -rf "$WORK_DIR/external_screens"
  cp -R "$REPO_ROOT/docs/design/creator-config-may28/external_screens" "$WORK_DIR/"
fi

# Copy prototype index pages
for proto in prototype_auth.html prototype.html; do
  [ -f "$REPO_ROOT/docs/design/master-audit-may30/$proto" ] && cp "$REPO_ROOT/docs/design/master-audit-may30/$proto" "$WORK_DIR/"
  [ -f "$REPO_ROOT/docs/design/creator-config-may28/$proto" ] && cp "$REPO_ROOT/docs/design/creator-config-may28/$proto" "$WORK_DIR/"
done

# Start server if not already running on :8765
if lsof -i :8765 >/dev/null 2>&1; then
  echo "[design-server] Server already running on :8765 — content refreshed."
else
  echo "[design-server] Starting Python http.server on :8765..."
  cd "$WORK_DIR"
  python3 -m http.server 8765 --bind 127.0.0.1 >server.log 2>&1 &
  echo "[design-server] PID $! · serving from $WORK_DIR"
fi

echo "[design-server] Done."
echo ""
echo "Open: http://127.0.0.1:8765/prototype_auth.html"
