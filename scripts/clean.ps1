#!/usr/bin/env pwsh

$ErrorActionPreference = 'Stop'

Write-Output "Removing the Nuitka compilation folder"
Remove-Item -Path "dist" -Recurse 
Write-Output "Removing the Nuitka compilation folder finished"

Write-Output "Removing the compilated Qt UI and Qt Ressource files"

$QT_RESSOURCE="res_rc" 
$QT_UI_ARRAY="system_info","form","instance","settingDialog","about"

Write-Output "Removing the compilated Qt Ressource file"
Remove-Item -Path "src\lce_qt_launcher\$QT_RESSOURCE.py"
Write-Output "Removing the compilated Qt Ressource file finished"

foreach ($QT_UI in $QT_UI_ARRAY)
{
    Write-Output "Removing the compilated ui_$QT_UI.py Qt UI file"
    Remove-Item -Path "src\lce_qt_launcher\ui_$QT_UI.py"
    Write-Output "Removing the compilated ui_$QT_UI.py Qt UI file finished"
}

Write-Output "Removing every pycaches filed"
Get-ChildItem -Path . -Recurse -Include '__pycache__', '*.pyc' | Remove-Item -Recurse -Force
Write-Output "Removing every pycaches done"
