#!/usr/bin/env bash

set -e

scripts/prepare.sh

echo "Beginning the Nuitka compilation"
hatch run python -m nuitka --standalone --assume-yes-for-download --output-dir=dist src/lce_qt_launcher/main.py
echo "done"

echo "Compressing the Nuitka compressions"
tar -czf LCE-Qt-Launcher-Linux.tar.gz -C dist/main.dist .
echo "done"