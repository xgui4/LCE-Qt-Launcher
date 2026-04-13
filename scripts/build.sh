#!/usr/bin/env bash

set -e

if [[ $(uname -s) != "FreeBSD" ]]; then 
    pyside6-rcc "res.qrc" -o "src/res_rc.py" &&
    pyside6-uic "src/form.ui" -o "src/ui_form.py" &&
    pyside6-uic "src/instance.ui" -o "src/ui_instance.py" &&
    pyside6-uic "src/system_info.ui" -o "src/ui_system_info.py" 
    pyside6-uic "src/settingDialog.ui" -o "src/ui_settingDialog.py" 
    pyside6-uic "src/about.ui" -o "src/ui_about.py" 
else
    /usr/local/pyside6/rcc -g python "res.qrc" -o "src/res_rc.py" &&
    /usr/local/pyside6/uic -g python "src/form.ui" -o "src/ui_form.py" &&
    /usr/local/pyside6/uic -g python "src/system_info.ui" -o "src/ui_system_info.py" 
    /usr/local/pyside6/uic -g python "src/settingDialog.ui" -o "src/ui_settingDialog.py" 
    /usr/local/pyside6/uic -g python "src/about.ui" -o "src/ui_about.py" 
fi