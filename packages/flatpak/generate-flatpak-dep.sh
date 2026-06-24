#!/usr/bin/env sh

uv export --prune pyside6 --no-editable --no-dev --output-file requirements.txt
sed -i '/./d' requirements.txt
flatpak_pip_generator --runtime org.kde.Sdk//6.10  --requirements-file requirements.txt