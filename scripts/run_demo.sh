#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 -m venv .venv 2>/dev/null || true
# shellcheck disable=SC1091
source .venv/bin/activate
pip install -r requirements.txt -q
[[ -f .env ]] || cp .env.example .env
echo "Demo: http://127.0.0.1:8765/docs"
exec python -m uvicorn demo.app:app --host 127.0.0.1 --port 8765
