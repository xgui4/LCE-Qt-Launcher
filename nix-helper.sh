#!/usr/bin/env bash

set -e 

user_input=$1

if [[ $user_input == "install" ]]; then
    nix-build default.nix
    nix-env -i ./result
fi
if [[ $user_input == "compile" ]]; then
    ./scripts/build.sh
fi
if [[ $user_input == "clear" ]]; then
    ./scripts/clear.sh
fi
