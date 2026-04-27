#!/usr/bin/env bash

set -e

echo "Removing the Nuitka compilation folder"
rm -rf "dist"
echo "Removing the Nuitka compilation folder finished"

echo "Removing the compilated Qt UI and Qt Ressource files"

QT_RESSOURCE="res_rc" 
QT_UI_ARRAY=("system_info" "form" "instance" "settingDialog" "about")

echo "Removing the compilated Qt Ressource file"
rm "src/lce_qt_launcher/$QT_RESSOURCE.py"
echo "done"

for QT_UI in "${QT_UI_ARRAY[@]}"
do
    echo "Removing the compilated ui_$QT_UI.py Qt UI file"
    rm "src/lce_qt_launcher/ui_$QT_UI.py"
    echo "done"
done

echo "Removing every pycaches filed"
find . -name '__pycache__' -print0 | xargs -0 rm -rf
echo "done"