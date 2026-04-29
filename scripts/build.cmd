@echo off

echo "Starting Compilaton of Qt Ressource"
pyside6-rcc "res.qrc" -o "src\lce_qt_launcher\res_rc.py" || exit /b 1
echo "done"

setlocal enabledelayedexpansion

echo "Compilation of Qt ui files"

set ui[0]="form"
set ui[1]="system_info"
set ui[2]="instance"
set ui[3]="settingDialog"
set ui[4]="about"

for /L %%i in (0,1,4) do (
    set "filename=!ui[%%i]!"

    echo "Compiling !filename!.ui Qt UI file"
    pyside6-uic "src/!filename!.ui" -o "src\lce_qt_launcher\ui_!filename!.py" || (
        echo Error compiling !filename!.ui
        exit /b 1
    )
    echo "done"
)

echo "Compilation of all Qt ui files finished"