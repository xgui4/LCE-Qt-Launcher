#!/usr/bin/env bash

set -e

if [[ $("uname -s") != "FreeBSD" ]]; then 
    pyside6-rcc "res.qrc" -o "src/res_rc.py" &&
    pyside6-uic "src/form.ui" -o "src/ui_form.py" &&
    pyside6-uic "src/system_info.ui" -o "src/ui_system_info.py" 
else
    /usr/local/pyside6/rcc -g python "res.qrc" -o "src/res_rc.py" &&
    /usr/local/pyside6/uic -g python "src/form.ui" -o "src/ui_form.py" &&
    /usr/local/pyside6/uic -g python "src/system_info.ui" -o "src/ui_system_info.py" 
fi