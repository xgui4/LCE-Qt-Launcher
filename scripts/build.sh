#!/usr/bin/env bash

set -e

QT_RESSOURCE="res.qrc"
UI_FILES=("form" "system_info" "instance" "settingDialog" "about")

if [[ $(uname -s) != "FreeBSD" ]]; then 
    if command -v  pyside6-rcc  &> /dev/null; then
        echo "Starting Compilaton of Qt Ressource"
        pyside6-rcc $QT_RESSOURCE -o src/lce_qt_launcher/res_rc.py
        echo "Compilation of $QT_RESSOURCE to src/lce_qt_launcher/res_rc.py is finished"
                
        for ui in "${UI_FILES[@]}"; do
            echo "Compiling ${ui}.ui"
            OUT="src/lce_qt_launcher/ui_${ui}.py"
            pyside6-uic -g python "src/${ui}.ui" -o "$OUT"
            echo "Compilation of ${ui}.ui to $OUT finished"
        done
    else
        echo "Starting Compilaton of Qt Ressource"
        /usr/lib/qt6/rcc -g python $QT_RESSOURCE -o src/lce_qt_launcher/res_rc.py
        echo "Compilation of $QT_RESSOURCE to src/lce_qt_launcher/res_rc.py is finished"
                
        for ui in "${UI_FILES[@]}"; do
            echo "Compiling ${ui}.ui"
            OUT="src/lce_qt_launcher/ui_${ui}.py"
            /usr/lib/qt6/uic -g python "src/${ui}.ui" -o "$OUT"
            echo "Compilation of ${ui}.ui to $OUT finished"
            
            sed -i "s/^import $QT_RESSOURCE/from . import res_rc/g" "$OUT"
        done
    fi
else
    echo "Starting Compilaton of Qt Ressource"
    /usr/local/pyside6/rcc -g python $QT_RESSOURCE -o src/lce_qt_launcher/res_rc.py
    echo "Compilation of $QT_RESSOURCE to src/lce_qt_launcher/res_rc.py is finished"
                
    for ui in "${UI_FILES[@]}"; do
        echo "Compiling ${ui}.ui"
        OUT="src/lce_qt_launcher/ui_${ui}.py"
        /usr/local/pyside6/uic -g python "src/${ui}.ui" -o "$OUT"
        echo "Compilation of ${ui}.ui to $OUT finished"
    done
fi