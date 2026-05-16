#!/usr/bin/env sh

if [ "$1" = "create-venv" ]; then 
    uv venv --system-site-packages
    . ".venv/bin/activate"
    uv sync --system-certs
fi

if [ "$1" = "sync" ]; then 
    uv sync --system-certs
fi
