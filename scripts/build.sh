#!/usr/bin/env bash
set -e

# Fonction pour trouver l'outil (soit le nom pip, soit l'outil Qt6 natif)
find_tool() {
    if command -v "pyside6-$1" &> /dev/null; then
        echo "pyside6-$1"
    elif command -v "$1" &> /dev/null; then
        echo "$1 -g python"
    elif [[ -f "/usr/local/pyside6/$1" ]]; then
        echo "/usr/local/pyside6/$1 -g python"
    else
        echo "ERREUR: Outil $1 introuvable" >&2
        exit 1
    fi
}

RCC=$(find_tool rcc)
UIC=$(find_tool uic)

echo "Construction avec : $RCC et $UIC"

$RCC "res.qrc" -o "src/res_rc.py"
$UIC "src/form.ui" -o "src/ui_form.py"
$UIC "src/instance.ui" -o "src/ui_instance.py"
$UIC "src/system_info.ui" -o "src/ui_system_info.py" 
$UIC "src/settingDialog.ui" -o "src/ui_settingDialog.py" 
$UIC "src/about.ui" -o "src/ui_about.py"