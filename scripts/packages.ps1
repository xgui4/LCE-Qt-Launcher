$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

hatch run python -m nuitka --standalone --assume-yes-for-download --output-dir=dist src\lce_qt_launcher\main.py
Compress-Archive -Path dist/lce-qt-launcher.dist\* -DestinationPath LCE-Qt-Launcher-Windows.zip