#!/bin/bash
# Sube a GitHub todo lo nuevo cada 7 minutos (rama actual). Parar: crear <logdir>/PARAR_SUBIDA
cd "$(dirname "$0")/../.."
LOG=${1:-/tmp}
while [ ! -f $LOG/PARAR_SUBIDA ]; do
  git add -A videosclaude >/dev/null 2>&1
  if ! git diff --cached --quiet; then
    git commit -q -m "videosclaude: autoguardado ($(date +%H:%M))

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01UH48RdTZGtKBWsBMCmwfW2" >/dev/null 2>&1
    git push -q -u origin "$(git branch --show-current)" >/dev/null 2>&1 || (sleep 5; git push -q -u origin "$(git branch --show-current)" >/dev/null 2>&1)
  fi
  sleep 420
done
