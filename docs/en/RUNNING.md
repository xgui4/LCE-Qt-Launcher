# How to run

## VSCode

> [!NOTE]
> In Windows you might need to replace `/` with `\`
> [!WARNING]
> This method is not recommed nore tested for NixOS, go to the NixOS Section, for the step for this particular OS.

1. Create a Python Virtual Env via a tool like UV (if not already done)
2. Set VSCode to that Python Virtual Env
3. Run "Pyside : Sync Virtual Env and Launch"
4. Run the app via Vscode debug mode or directly the [`src/lce_qt_launcher/main.py`](src/lce_qt_launcher/main.py) file.

## NixOS

1. load the nix shell with `nix-shell` command
2. compiled the ui and ressource file with [`scripts/build.sh`](scripts/build.sh)
3. load the app with [`python src/lce_qt_launcher/main.py`](src/lce_qt_launcher/main.py)

## FreeBSD

```shell

#!/usr/bin/env sh

if [ "$1" = "create-venv" ]; then 
    uv venv --system-site-packages
fi

if [ "$1" = "sync" ]; then 
    uv sync --system-certs
fi


```

## Using the command line

1. Create the venv with uv (`uv sync`)
2. Load the venv with `source .venv/bin/activate.sh` (replace .sh with your shell, on Windows it is `.venv\Scripts\activate.ps1` for powershell or `.venv\Scripts\activate.bat` for cmd)
3. Run `scripts/build.sh` (for Linux) `scripts\build.cmd` for (Windows)
4. Run the main python script `src/lce_qt_launche.py` (On Windows you might need to invoque `python3` directly and replace `/` with `\`)
