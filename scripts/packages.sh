#!/usr/bin/env bash

set -e

scripts/prepare.sh

hatch run python -m nuitka --standalone --assume-yes-for-download --output-dir=dist src/legacy_qt_launcher/main.py
tar -czf LCE-Qt-Launcher-Linux.tar.gz -C dist/legacy-qt-launcher/.dist .