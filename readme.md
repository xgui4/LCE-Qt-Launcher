# LCE Qt Launcher

[French Version](lisezmoi.md)

![LCE-Qt-Launcher Icon](assets/io.github.xgui4.lce_qt_launcher.png)
![Screenshot of the launcher in version 0.0.20a0 of the launcher)](.github/screenshots/image.png)

- Other Repo:
  - [Backup repo](https://code.nolog.cz/xgui4/LCE-Qt-Launcher)
  - [Data repo](https://code.nolog.cz/xgui4/lce-qt-Launcher-data)

> [!WARNING]
> This launcher is under development and its features may be modified or removed at any time.
> Requests for help (PR) are welcome to fix or add features. Please simply adhere to the [GPLv3](license.md) and the [Code of Conduct](code-of-conduct.md).

##

> [!NOTE]
> Automatic updates and installations of game files are unstable and unreliable. It is recommended that you already have the game installed.
> This is because the installation and update mechanism requires an external repository that can be shut down without notice. I do my best, and the development versions (nightly) are generally up-to-date,
> but the stable version is sometimes delayed and requires manual intervention.

## About

A free cross-platform custom Minecraft LCE launcher, written with PySide6 (Qt6 for Python).

[Check out the official LCE Qt Launcher website!](https://xgui4.github.io/LCE-Qt-Launcher/) ![Deployment status on the GitHub page](https://github.com/xgui4/lce-qt-launcher/actions/workflows/site.yml/badge.svg)

## Why LCE Qt Launcher ?

- Made in Python with Qt 6 : Native Linux theme support and highly customisable
- Integration with Community Tools
- GNU/Linux first class support
- Big Tech free
- Free as Freedom Launcher (GPLv3)

## Features

- Command Line interface (CLI)
- Multiple Instances support
- Marketplaces :
  - [LCE Hub Emeralds Launcher Workshop](https://github.com/LCE-Hub/piston)
- in-app news for the instances
- Availaible in mutliple formats :
  - Nuitka Build : Linux and Windows
  - AppImage (GNU/Linux only)
  - Inno Setup installer package (for the Nuitka build) (Windows)
  - FreeBSD port
  - Arch Packgage
  - Flatpak (coming soon)
  - uv virtual venv (portable)

## Long Term Goal / Roadmap

## Long time Developpement focus

- GNU/Linux compatibility
- Windows support
- AppImage Support
- Focus on being one place for everything Minecraft LCE on GNU/Linux
- KISS (like try to avoid bloat like JS when possible)

## Work in progress features

- Skin support
- Experimental FreeBSD and Nix/NixOS support
- Flatpak support
- Localisations support

## Future features/planning features

- Separe the data into each own repository (lce-qt-launcher-data)
- My own versions/instance store
- Better stores UI/Mecanism
- Support for more community tools
- NeoLegacy DLC support
- Better News UI/Mecanism
- Accessibility

## Compiling

See [`docs/en/COMPILING.md`](docs/en/COMPILING.md)

## Running/Debugging

See [`docs/en/RUNNING.md`](docs/en/RUNNING.md)

## Python Library and Tools Used

- PySide 6
- platformdirs
- rich
- hatch
- uv

## How to get

See [`docs/SETUP.md`](docs/en/SETUP.md)

## Special Thank to

See [`THANKS.md`](THANKS.md)

## Code of Respect

- [In English](code-of-conduct.md)
- [In French](CODE-DE-CONDUITE.md)

## License

[GPLV3](license.md)
