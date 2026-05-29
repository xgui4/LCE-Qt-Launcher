$ErrorActionPreference = 'Stop'

Write-Output "Starting Compilaton of Qt Ressource"
pyside6-rcc "res.qrc" -o "src\lce_qt_launcher\res_rc.py" || exit /b 1
Write-Output "done"

Write-Output "Compilation of Qt ui files"

$QT_UI_ARRAY="system_info","form","instance","settingDialog","about", "contentInstaller"

foreach ($QT_UI in $QT_UI_ARRAY)
{
    Write-Output "Compiling $QT_UI.ui Qt UI file"
    pyside6-uic "src/$T_UI..ui" -o "src\lce_qt_launcher\ui_$Qt_UI.py"
    Write-Output "done"
}

Write-Output "Compilation of all Qt ui files finished"