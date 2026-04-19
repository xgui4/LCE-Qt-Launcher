$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

hatch run python -m nuitka --standalone --assume-yes-for-download --output-dir=dist src\legacy-qt-launcher\main.py
Compress-Archive -Path distlegacy-qt-launcher.dist\* -DestinationPath LCE-Qt-Launcher-Windows.zip