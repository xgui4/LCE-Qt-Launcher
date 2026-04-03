#!/usr/bin/env bash

hatch run python -m nuitka --standalone --assume-yes-for-download --output-dir=dist src/main.py
tar -czf LCE-Qt-Launcher-Linux.tar.gz -C dist/main.dist .