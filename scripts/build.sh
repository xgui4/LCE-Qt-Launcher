#!/usr/bin/env bash

set -e

if [[ $(uname -s) != "FreeBSD" ]]; then 
    if command -v  pyside6-rcc  &> /dev/null; then
        pyside6-rcc res.qrc -o src/lce_qt_launcher/res_rc.py
        
        UICS=("form" "system_info" "instance" "settingDialog" "about")
        
        for ui in "${UICS[@]}"; do
            OUT="src/lce_qt_launcher/ui_${ui}.py"
            pyside6-uic -g python "src/${ui}.ui" -o "$OUT"
        done
    else
        /usr/lib/qt6/rcc -g python res.qrc -o src/lce_qt_launcher/res_rc.py
        
        UICS=("form" "system_info" "instance" "settingDialog" "about")
        
        for ui in "${UICS[@]}"; do
            OUT="src/lce_qt_launcher/ui_${ui}.py"
            /usr/lib/qt6/uic -g python "src/${ui}.ui" -o "$OUT"
            
            sed -i 's/^import res_rc/from . import res_rc/g' "$OUT"
        done
    fi
else
    /usr/local/pyside6/rcc -g python res.qrc -o src/lce_qt_launcher/res_rc.py
        
    UICS=("form" "system_info" "instance" "settingDialog")
        
    for ui in "${UICS[@]}"; do
        OUT="src/lce_qt_launcher/ui_${ui}.py"
        /usr/local/pyside6/uic -g python "src/${ui}.ui" -o "$OUT"
    done
fi