#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python -m venv .venv || true
source .venv/bin/activate
pip install -r requirements.txt
python job_template.py
