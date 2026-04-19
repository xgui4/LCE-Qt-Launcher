#!/usr/bin/env pwsh

$ErrorActionPreference = 'Stop'

Remove-Item -Path "dist" -Recurse 

Remove-Item -Path "src\legacy-qt-launcher\res_rc.py"
Remove-Item -Path "src\legacy-qt-launcher\ui_system_info.py"
Remove-Item -Path "src\legacy-qt-launcher\ui_form.py"
Remove-Item -Path "src\legacy-qt-launcher\ui_instance.py"
Remove-Item -Path "src\legacy-qt-launcher\ui_settingDialog.py" 
Remove-Item -Path "src\legacy-qt-launcher\ui_about.py" 

Get-ChildItem -Path . -Recurse -Include '__pycache__', '*.pyc' | Remove-Item -Recurse -Force