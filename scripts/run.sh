#!/usr/bin/env bash

set -e

echo "Activate the python venv"
# shellcheck source=/dev/null
source .venv/bin/activate
echo "done"

src/lce_qt_launcher/main.py