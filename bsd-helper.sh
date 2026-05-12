#!/usr/bin/env sh

if [ "$1" = "create-venv" ]; then 
    uv venv --system-site-packages
    source .venv/bin/activate.sh
    uv sync --system-certs
fi

if [ "$1" = "sync" ]; then 
    uv sync --system-certs
fi
