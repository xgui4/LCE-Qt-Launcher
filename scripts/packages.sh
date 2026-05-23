#!/usr/bin/env bash

set -e

scripts/prepare.sh

echo "NOTE : this new version of the packages helper script 
for UNIX like system is experiental and a work in progrss
The script in nightly or in other branch/channel might be
more up to date."

echo "1. Ntuika portable build"
echo "2. Arch Packages (Require Arch)"
echo "3. Flatpak. (Hightly experiental)"  
echo "Choose a option (between 1 and 3):"

read -r user_input

if [[ $user_input == "1" ]]; then 
    echo "Beginning the Nuitka compilation"
    hatch run python -m nuitka --standalone --assume-yes-for-download --output-dir=dist src/lce_qt_launcher/main.py
    echo "done"

    echo "Compressing the Nuitka compressions"
    tar -czf LCE-Qt-Launcher-Linux.tar.gz -C dist/main.dist .
    echo "done"
elif [[ $user_input == "2" ]]; then
    cd packages/linux 

    echo "stable (0) or nigthly (git)"
    echo "Choose a channel (0 or 1):"
    read -r user_input
    if [[ $user_input == "0" ]]; then 
        cd stable
        makepkg -s
    elif [[ $user_input == "1" ]]; then
        cd "dev"
        makepkg -s
    fi
elif [[ $user_input == "3" ]]; then
    cd packages/flatpak
    flatpak-builder --user --force-clean --install build-dir io.github.xgui4.lce_qt_launcher.yml --install-deps-from=flathub
fi