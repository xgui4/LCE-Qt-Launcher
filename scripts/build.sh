#!/usr/bin/env bash

set -e

if [[ $(uname -s) != "FreeBSD" ]]; then 
    /usr/lib/qt6/uic -g python src/form.ui -o src/lce_qt_launcher/ui_form.py &&
    /usr/lib/qt6/rcc -g python res.qrc -o src/lce_qt_launcher/res_rc.py && 
    /usr/lib/qt6/uic -g python src/system_info.ui -o src/lce_qt_launcher/ui_system_info.py && 
    /usr/lib/qt6/uic -g python src/instance.ui -o src/lce_qt_launcher/ui_instance.py && 
    /usr/lib/qt6/uic -g python src/settingDialog.ui -o src/lce_qt_launcher/ui_settingDialog.py
else
    /usr/local/pyside6/rcc -g python "res.qrc" -o "src/lce_qt_launcher/res_rc.py" &&
    /usr/local/pyside6/uic -g python "src/form.ui" -o "src/lce_qt_launcher/ui_form.py" &&
    /usr/local/pyside6/uic -g python "src/system_info.ui" -o "src/lce_qt_launcher/ui_system_info.py" 
    /usr/local/pyside6/uic -g python "src/settingDialog.ui" -o "src/lce_qt_launcher/ui_settingDialog.py" 
    /usr/local/pyside6/uic -g python "src/about.ui" -o "src/lce_qt_launcher/ui_about.py" 
fi


