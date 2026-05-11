#!/usr/bin/env sh

if $1 = "install"; then 

uv venv --system-site-packages
source .venv/bin/activate.fish
uv sync --system-certs

fi
