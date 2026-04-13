$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

hatch run python -m nuitka --standalone --assume-yes-for-download --output-dir=dist src/main.py
Compress-Archive -Path dist/main.dist/* -DestinationPath LCE-Qt-Launcher-Windows.zip