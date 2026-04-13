#!/usr/bin/env pwsh

$ErrorActionPreference = 'Stop'

Remove-Item -Path -Recurse dist

Remove-Item -Path "src\res_rc.py"
Remove-Item -Path "src\ui_system_info.py"
Remove-Item -Path "src\ui_form.py"
Remove-Item -Path "src\ui_instance.py"
Remove-Item -Path "src\ui_settingDialog.py" 
Remove-Item -Path "src\ui_about.py" 

Get-ChildItem -Path . -Recurse -Include '__pycache__', '*.pyc' | Remove-Item -Recurse -Force