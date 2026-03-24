#!/usr/bin/env bash

# THIS SCRIPT WAS NOT TESTED YET ! USE AT YOUR OWN RISK 

set -e

if [[ ! -d ".venv/" ]]; then
    uv sync
fi 

path=$(dirname "$(realpath "$0")")

if [[ "$VIRTUAL_ENV" != "" ]]; then
    source "$path/.venv/bin/activate"
fi

pyside6-rcc "$path/res.qrc" -o "$path/src/res_rc.py" &&
pyside6-uic "$path/src/form.ui" -o "$path/src/ui_form.py" &&
pyside6-uic "$path/src/system_info.ui" -o "$path/src/ui_system_info.py" &&

if [ "$#" == 0 ]|| [ "$1" == "develop" ]; then 
    python -m pip install --editable .
else
    python -m pip install .
fi