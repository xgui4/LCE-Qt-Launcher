#!/usr/bin/env bash

set -e

QT_RESSOURCE="res.qrc"
UI_FILES=("form" "system_info" "instance" "settingDialog" "about" "contentInstaller")

RCC="pyside6-rcc"
UIC="pyside6-ui"

fix_import() {
    if [[ $(uname -o) == "GNU/Linux" ]]; then
        sed -i 's/^import res_rc/from . import res_rc/g' "$1"
    else 
        sed -i.bak 's/^import res_rc/from . import res_rc/g' "$1"
        rm "$1.bak"
    fi
}

find_qt_tool() {
    if command -v pyside6-rcc &> /dev/null; then
        RCC="pyside6-rcc"
        UIC="pyside6-uic"
    elif command -v /usr/local/bin/pyside6-rcc &> /dev/null; then
        RCC="/usr/local/bin/pyside6-rcc"
        UIC="/usr/local/bin/pyside6-uic"
    elif command -v /usr/lib/qt6/rcc &> /dev/null; then
        RCC="/usr/lib/qt6/rcc -g python"
        UIC="/usr/lib/qt6/uic -g python"
    elif command -v /usr/local/PySide6/bin/rcc &> /dev/null; then
        RCC="/usr/local/PySide6/bin/rcc -g python"
        UIC="/usr/local/PySide6/bin/uic -g python"
    fi
}

echo "finding the correct path for the Qt compilers"
find_qt_tool
echo "done"

echo "Starting Compilaton of Qt Ressource"
$RCC -g python $QT_RESSOURCE -o src/lce_qt_launcher/res_rc.py
echo "done"
            
for ui in "${UI_FILES[@]}"; do
    echo "Compiling ${ui}.ui"
    OUT="src/lce_qt_launcher/ui_${ui}.py"
    $UIC "src/${ui}.ui" -o "$OUT"
    echo "done"
    echo "fixing the import"
    fix_import "$OUT"
    echo "done"
done