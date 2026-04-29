$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

Write-Output "Beginning the Nuitka compilation"
hatch run python -m nuitka --standalone --assume-yes-for-download --output-dir=dist src\lce_qt_launcher\main.py
Write-Output "done"

Write-Output "Compressing the Nuitka compressions"
Compress-Archive -Path dist/main.dist\* -DestinationPath LCE-Qt-Launcher-Windows.zip
Write-Output "done"