# LCE Qt Launcher

[French Version](lisezmoi.md)

![LCE-Qt-Launcher Icon](assets/io.github.xgui4.lce_qt_launcher.png)
![Screnshot of the launcher in version 0.0.20a0 of the launcher)](.github/screenshots/image.png)

- Other Repo:
  - [Backup repo](https://code.nolog.cz/xgui4/LCE-Qt-Launcher)
  - [Data repo](https://code.nolog.cz/xgui4/lce-qt-Launcher-data)

> [!WARNING]
> This launcher is work in progress and its feature could be changes or remove at any time.
> PR are more than welcome to fix or add features. Just be compliant with the [GPLv3 license](license.md) and the [Code of Respect](code-of-conduct.md)

##

> [!NOTE]
> The auto-update and installation of the game files is unstable and unviable, it is recommnend to have the game file already installation
> as the installation and update mechanism require external repo that can be shutdown without previous notice. I do my best and the nightly build are often
> up to date but the stable version sometime lack behind and require manual intervention.

## About

This is a custom Minecraft LCE Launcher written with PySide6 (Qt6 for Python) with Freedom and with GNU/Linux support in mind.

[Check the official LCE Qt Launcher Website !](https://xgui4.github.io/LCE-Qt-Launcher/)![GitHub Page Deploy Action Status](https://github.com/xgui4/lce-qt-launcher/actions/workflows/site.yml/badge.svg)

## Why LCE Qt Launcher ?

- Made in Python with Qt 6 : bloat free and integrate with GNU/Linux Plasma 6/Qt 6 Theme
- Integration with Community Tools
- GNU/Linux first class support
- Licensed via copyleft licensing (GPLv3), so big tech free
- Free as Freedom Launcher

## Features

- Command Line interface (CLI)
- Multiple Instances support
  - Pre-Configured ones :
    - [NeoLegacy (Default)](https://github.com/pieeebot/neoLegacy/)
    - [MCLCE/MinecraftConsoles (source code backup only)](https://git.minecraftlegacy.com/backups/MinecraftConsoles) (previously smartcmd/MinecraftConsoles)
    - [LCE-Revelation](https://git.revela.dev/itsRevela/LCE-Revelations)
    - [Aether Mod](https://github.com/Frcoxd/aether-papu)
- Marketplaces :
  - [LCE Hub Emeralds Launcher Workshop](https://github.com/LCE-Hub/piston)
  - [LegacyMods (coming soon)](https://legacymods.org/)
- in-app news for the instances

## Long Term Goal / Roadmap

- Accessibility
- Skin support
- GNU/Linux compatibility
- Windows support
- Experimental FreeBSD and Nix/NixOS support
- Flatpak support
- AppImage Support
- Localisations support
- Focus on being one place for everything Minecraft LCE on GNU/Linux

## Compiling

See [`docs/en/COMPILING.md`](docs/en/COMPILING.md)

## Running/Debugging

See [`docs/en/RUNNING.md`](docs/en/RUNNING.md)

## How to get

### Tag Release ![Stable release deployment action status](https://github.com/xgui4/lce-qt-launcher/actions/workflows/stable.yml/badge.svg)

In the [GitHub Release page of this repo](https://github.com/xgui4/LCE-Qt-Launcher/releases/) page you will found tagged Release like [Beta 0.0.1.1](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/0.0.0.1beta).

### Flatpak (Coming Soon) ![Flatpak deployment action status](https://github.com/xgui4/lce-qt-launcher/actions/workflows/flatpak.yml/badge.svg)

Coming Soon (Delayed due to technical issues)

### FreeBSD Port (Experimental)

See [my FreeBSD Port Overlay](https://github.com/xgui4/freebsd-ports) to installing games/lce-qt-laucher (py{python version}-lce-qt-launcher) port.

### Nigthly Build ![Nightly Build Action Status](https://github.com/xgui4/lce-qt-launcher/actions/workflows/nightly.yml/badge.svg)

> [!NOTE]
> This branch is not stable and changes are made almost daily so this branch can sometimes break. Also, MacOS is not avaiable in the Nigthly Build due to Apple restriction and that I do now own a mac.

In this [GitHub Release](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/nightly) page you will found Nighly Build which are made automatically via GitHub Action when change are made in the [`dev` branch](https://github.com/xgui4/LCE-Qt-Launcher/tree/dev)

### AppImage and Others Linux Packages

Aavailable in [nightly build](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/nightly) and tagged version (Coming soon!) (Note : currently the AppImage and Arch Package atomatic build is broken)

### Via Git

You can also, downloading this repo with the command `git clone https://github.com/xgui4/lce-qt-launcher.git` and then compiling (see `docs/en/COMPILING.md` for more info how) anually or running in a .venv (see `docs/en/RUNNING.md` for more info how).

## Software Requirement

- [uv](https://pypi.org/project/uv) or [hatch](https://pypi.org/project/hatch/)
- [Python 3.10 to Python 3.12 (for Nuitka build, system package and portable build python version can be higher)](https://www.python.org)
- A display server or compositor

- For UNIX like system
  - A display server or compositor
  - Bash (normally pre-installed on Linux but often demand installation in *BSD and MacOS)
- For Windows
  - Powershell

## Software recommendations

- [Monocraft Font](https://github.com/IdreesInc/Monocraft) installed
- [Miracode Font](https://github.com/IdreesInc/Miracode)
- Steam, [Steam Tinker Launch](https://github.com/sonic2kk/steamtinkerlaunch) and Valve Proton for better GNU/Linux support, Proton is not required for Windows

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
- FreeBSD Port & in venv (portable)
- AppImage

### Upcoming Platform

> [!NOTE]
> Platform not tested yet, but with implementation

- Flatpak

### Unsupported OS

> [!NOTE]
> These platform are not tested and may work or not at all

- Other *BSD system, as Minecraft LCE is not supported on those and Wine is not available.
- Minecraft LCE on Android is currently quite laggy and buggy
- macOS: LCE Qt Launcher does not officially support MacOS and is not tested during PRs and testing and does not have package for it and there is no documentation for it. But expericenced user could make it work.

## Special Thank to

- [Prism Launcher](https://github.com/PrismLauncher/PrismLauncher) for certain UI elements and ui files
- [MCLCE/MinecraftConsoles community](https://git.minecraftlegacy.com/backups/MinecraftConsoles) for the port of the game for PC
- [neoLegacy community](https://github.com/neoStudiosLCE/neoLegacy") for backporting updates for the PC port
- [LCE-Revelation community](https://git.revela.dev/itsRevela/LCE-Revelations)
- [LCE Hub Communiy](https://github.com/LCE-Hub) for the Marketplace/Workshop
- [MinecraftLegacy Community](https://github.com/MinecraftConsole) to include my launcher in their list
- [Miracode Font](https://github.com/IdreesInc/Miracode)
- [Monocraft Font](https://github.com/IdreesInc/Monocraft)
- [Steam Tinker Launch](https://github.com/sonic2kk/steamtinkerlaunch) for Steam and SteamDeck integration on GNU/Linux via their software.
- and also everyone in the LCE community to continue the legacy of Legacy Console Edition and where some of the images assets came from.
- and to Notch (Markus Persson), 4J Studio and Mojang to make this game in the first place

## Code of Respect

- [In English](code-of-conduct.md)
- [In French](CODE-DE-CONDUITE.md)

## License

[GPLV3](license.md)
