#!/usr/bin/env bash

set -e

scripts/prepare.sh

hatch run python -m nuitka --standalone --assume-yes-for-download --output-dir=dist src/lce_qt_launcher/main.py
tar -czf LCE-Qt-Launcher-Linux.tar.gz -C dist/lce-qt-launcher/.dist .