# LCE QT Launcher

[French Version](lisezmoi.md) (Not updated yet)

![LCE-QT-Launcher](assets/io.github.xgui4.lce_qt_launcher.png)
![Screnshot of the launcher](.github/screenshots/image.png)

> [!WARNING]
> This launcher is work in progress and its feature could be changes or remove at any time.
> PR are more than welcome to fix or add features. Just be compliant with the [GPLv3 license](license.md) and the [Code of Respect](code-of-conduct.md)

## About

This is a custom Minecraft LCE Launcher written in Python and Qt with Freedom and with GNU/Linux support in mind.

## Why LCE Qt Launcher ?

- Made in Python with Qt 6 : bloat free and integrate with GNU/Linux Plasma 6/Qt 6 Theme
- Customisation with Themes and laters modules/plugins
- Integration with Community Tools
- GNU/Linux first class support
- Licensed via copyleft licensing (GPLv3), so big tech free
- Free as Freedom Launcher
- Minecraft Themed by default

## Features

- Command Line interface (CLI)
- Multiple Instances support (Work in progress)
- localisations support (Work in progress)
  - Pre-Configured ones :
    - [MCLCE/MinecraftConsoles](https://github.com/mclce/minecraftconsoles) (previously smartcmd/MinecraftConsoles)
    - LegacyEvolved (will be removed soon as was replaced with NeoLegacy)
    - [NeoLegacy](https://github.com/pieeebot/neoLegacy/)
    - [360Revived](https://github.com/BluTac10/360Revived)
    - [LCE-Revelations](https://github.com/itsRevela/LCE-Revelations)
    - [HellishEnds](https://github.com/deadvoxelx/HellishEnds)
- Marketplaces :
  - [LCE Hub Emeralds Launcher Workshop](https://github.com/LCE-Hub/piston)
  - [LegacyMods (coming soon)](https://legacymods.org/)
- in-app news

## Long Term Goal / Roadmap

- Accessibility
- Modding Support
- Launcher Plugins
- Skin support
- GNU/Linux compatibility
- Windows support
- Experimental FreeBSD support
- Focus on being the main hub for Minecraft LCE on GNU/Linux

## How to run

### VSCode

> [!NOTE]
> In Windows you might need to replace `/` with `\`
> [!WARNING]
> This method is not recommed nore tested for NixOS, go to the NixOS Section, for the step for this particular OS.

1. Create a Python Virtual Env via a tool like UV (if not already done)
2. Set VSCode to that Python Virtual Env
3. Run "Pyside : Sync Virtual Env and Launch"
4. Run the app via Vscode debug mode or directly the [`src/lce_qt_launcher/main.py`](src/lce_qt_launcher/main.py) file.

### NixOS

1. load the nix shell with `nix-shell` command
2. compiled the ui and ressource file with [`scripts/build.sh`](scripts/build.sh)
3. load the app with [`python src/lce_qt_launcher/main.py`](src/lce_qt_launcher/main.py)

### Others

coming soon

## How to build

### Portable Nuitka Build

0. Create a Python Virtual Env via a tool like UV (if not already done)
1. Run `hatch run packages`

### Arch Linux

1. Go the [`packages/linux` directory](packages/linux)
2. Choose a channel dev, nigthly or stable (go to the directory)
3. Run `makepkg -si` or `makepkg -s` (for no install) in one of these directory

### Nix Package

#### Nix Flake (Not tested yet/Work in progress)

  Run `nix build`

#### Nixpkg

  Run `nix-build default.nix`

### Flatpak and Windows Installers

- Guide Coming Later

## Nigthly Build

> [!NOTE]
> This automatic nighly build is currently not-stable and is very experimental and in active developpement
> This branch is not stable and changes are made almost daily so this branch can sometimes break. Also, MacOS is not avaiable in the Nigthly Build due to Apple restriction and that I do now own a mac.

In this [GitHub Release](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/nightly) page you will found Nighly Build which are made automatically via GitHub Action when change are made in the `nighly` branch

## Software Requirement

- [Python 3.11 (For FreeBSD) to Python 3.12 (GNU/Linux, Windows and MacOS)](https://www.python.org)
  - with a virtual env with the required library install (specified in the readme and [`pyproject.toml`](pyproject.toml))
- [PySide6](https://pypi.org/project/PySide6/)
- [Monocraft Font](https://github.com/IdreesInc/Monocraft) installed
- For UNIX like system
  - A display server or compositor (Except on MacOS where it use its own proprietary one)
  - Bash (normally pre-installed on Linux but often demand installation in *BSD and MacOS)

## Python Library and Tools Used

- PySide 6
- requests
- platformdirs
- rich
- hatch
- uv

## Compatible Operating System

### Golden Support

    Platform Tested Regurlaly and with completed implemation/patch

- Windows 10 and later
- GNU/Linux

### Experimental Support

    Plattform tested with work in progress implemation

- NixOS

### Partly Supported Platform

    Platform not tested yet, but with implementation

- FreeBSD (While it may worked, it is not tested for it yet and might not worked at all)
- Flatpak (While it may worked, it is not tested for it yet and might not worked at all)

### Unsupported OS

    These platform are not tested and may work or not at all

- Other *BSD system, as Minecraft LCE is not supported on those and Wine is not available.
- Minecraft LCE on Android is currently quite laggy and buggy
- macOS: LCE Qt Launcher does not officially support MacOS and is not tested during PRs, but POISX compatibility should allow its use.

## Special Thank to

- [Prism Launcher](https://github.com/PrismLauncher/PrismLauncher) for certain UI elements and ui files
- [MCLCE/MinecraftConsoles](https://github.com/MCLCE/MinecraftConsoles) for the port of the game for PC
- [pieeebot/neoLegacy](https://github.com/pieeebot/neoLegacy) for backporting updates for the PC port
- [LCE Hub](https://github.com/LCE-Hub) for the Marketplace/Workshop

## Code of Respect

- [English](code-of-conduct.md)
- [French](CODE-DE-CONDUITE.md)

## License

[GPLV3](license.md)
