@echo off
cd /d "%~dp0"

call ..\prepare.cmd || exit /b 1
powershell.exe -ExecutionPolicy Bypass -File "..\packages.ps1"