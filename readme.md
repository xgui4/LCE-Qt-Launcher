# LCE Qt Launcher

[French Version](lisezmoi.md)

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
  - Pre-Configured ones :
    - [MCLCE/MinecraftConsoles](https://github.com/mclce/minecraftconsoles) (previously smartcmd/MinecraftConsoles)
    - LegacyEvolved (will be removed soon as was replaced with NeoLegacy)
    - [NeoLegacy](https://github.com/pieeebot/neoLegacy/)
    - [LCE-Revelations](https://github.com/itsRevela/LCE-Revelations)
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
- Experimental FreeBSD and Nix/NixOS support
- Localisations support
- Focus on being the main hub for Minecraft LCE on GNU/Linux

## Compiling

See [`docs/en/COMPILING.md`](docs/en/COMPILING.md)

## Running/Debugging

See [`docs/en/RUNNING.md`](docs/en/RUNNING.md)

## How to get

### Tag Release

In the [GitHub Release page of this repo](https://github.com/xgui4/LCE-Qt-Launcher/releases/) page you will found tagged Release like [Beta 0.0.1.1](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/0.0.0.1beta). Right now it is just source code but next version , it will have installer and packages for Windows and Linux and instruction for FreeBSD Ports and Nix package.

### Flatpak (Coming Soon)

Coming Soon (Delayed due to technical issues)

### FreeBSD Port (Coming Soon)

Coming Soon (Delayed due to technical issues)

### Nigthly Build

> [!NOTE]
> This branch is not stable and changes are made almost daily so this branch can sometimes break. Also, MacOS is not avaiable in the Nigthly Build due to Apple restriction and that I do now own a mac.

In this [GitHub Release](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/nightly) page you will found Nighly Build which are made automatically via GitHub Action when change are made in the [`nightly` branch](https://github.com/xgui4/LCE-Qt-Launcher/tree/nightly)

### Via Git

You can also, downloading this repo with the command `git clone https://github.com/xgui4/lce-qt-launcher.git` and then compiling (see `docs/en/COMPILING.md` for more info how) anually or running in a .venv (see `docs/en/RUNNING.md` for more info how).

## Software Requirement

- [Python 3.11 (For FreeBSD) to Python 3.12 (GNU/Linux, Windows and MacOS)](https://www.python.org)
  - with a virtual env with the required library install (specified in the readme and [`pyproject.toml`](pyproject.toml))
- [PySide6](https://pypi.org/project/PySide6/)
- [Monocraft Font](https://github.com/IdreesInc/Monocraft) installed
- [Miracode Font](https://github.com/IdreesInc/Miracode)
- For UNIX like system
  - A display server or compositor (Except on MacOS where it use its own proprietary one)
  - Bash (normally pre-installed on Linux but often demand installation in *BSD and MacOS)

## Python Library and Tools Used

- PySide 6
- platformdirs
- rich
- hatch
- uv

## Compatible Operating System

### Golden Support

> [!NOTE]
> Platform Tested Regurlaly and with completed implemation/patch

- Windows 10 and later
- GNU/Linux

### Experimental Support

> [!NOTE]
> Plattform tested with work in progress implemation

- NixOS
- FreeBSD using UV (Note: The FreeBSD port is in active development and still experimental; using the UV virtual environment is currently the only officially supported method for FreeBSD.)

### Upcoming Platform

> [!NOTE]
> Platform not tested yet, but with implementation

- Flatpak
- FreeBSD Port

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
- [MinecraftLegacy Community](https://github.com/MinecraftConsole) to include my lancher in their list
- [Miracode Font](https://github.com/IdreesInc/Miracode)
- [HellishEnds](https://github.com/deadvoxelx/HellishEnds) - now dcma, so it is removed/unaivable for now
- [360Revived](https://github.com/BluTac10/360Revived) - now dcma, so it is removed/unaivable for now
- [Steam Tinker Launch](https://github.com/sonic2kk/steamtinkerlaunch) for Steam and SteamDeck integration on GNU/Linux via their software.

## Code of Respect

- [English](code-of-conduct.md)
- [French](CODE-DE-CONDUITE.md)

## License

[GPLV3](license.md)
