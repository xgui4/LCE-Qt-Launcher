# LCE QT Launcher

![LCE-QT-Launcher](assets/images/Launcher.png)

> [!WARNING]
> This launcher is work in progress and its feature could be changes or remove at any time.
> PR are more than welcome to fix or add features. Just be compliant with the [GPLv3 license](license.md) and [Code of Respect](code-of-conduct.md)

## About 

This is a custom Minecraft LCE Launcher written in Python and Qt with Freedom and GNU/Linux support in mind.

## Features 

- Command Line interface
- Qt 6 GUI (Native like Interface)
- Written in Python (No Electron or Rust)
- Customisable 
- Free Software (GPLv3)
- Multiple Instance (Work in progress)
- localisatiions (Work in progress)
<!--
- Coming laters: 
- Plugins
- Skin support
- Modding Support 
- in-app news
-->
- GNU/Linux compatibility
- Experimental FreeBSD support 
- Windows support
- Focus on being the main hub for Minecraft LCE on GNU/Linux 
- Minecraft Theme pre-configured

## How to run 

### VSCode

1. Create a Python Virtual Env via a tool like UV
2. Set VSCode to that Python Virtual Env
3. Run "Pyside : Sync Virtual Env and Launch"
4. Run the app via Vscode debug mode or directly the [`src/main.py`](src/main.py) file. 

### Others

Guide coming laters

## How to build

Coming in the next stable release when the program will be more stable
 
## Nigthly Build

> [!NOTE]
> This automatic nighly build is currently not-stable and very experimental and active developpement

In this [GitHub Relese](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/nightly) page you will found Nighly Build which are made automatically
via GitHub Action when change are made in the `nighly` branch
This branch is not stable and changes are made almost daily and this branch can sometime break
MacOS is not avaiable in the Nigthly Build for now since I lack a way to test it since I do not own a Mac

## Software Requirement 

- [Python 3.10 to Python 3.13](https://www.python.org)
    - with a virtual env with the required library install (specified in the readme and [`pyproject.toml`](pyproject.toml))
- [PySide6](https://pypi.org/project/PySide6/)
- [Monocraft Font](https://github.com/IdreesInc/Monocraft) installed 
- For UNIX like system
    - A display server or compositor (Except on MacOS where it use its own proprietary one)
    - Bash (normally pre-installed on Linux but often demand installation in *BSD and MacOS)

## Python Library Used 

 - pyside6,
 - requests,
 - rich,
 - term-image,
 - hatch,
 - uv, 
 - pip

## Compatible Operating System

- Windows 10 and later (not tested yet)
- GNU/Linux 

### Experimental Support 

- FreeBSD

### Unsupported OS

- Other *BSD like system
- Android since Minecraft LCE is currently quite laggy and buggy on Android
- MacOS since I cannot test it legally, but should work with POISX compatibility but it is not officially supported. 

## Thank to 

- [Prism Launcher](https://github.com/PrismLauncher/PrismLauncher) for certain UI elements and ui files 
- [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles)) for the port of the game

## Code of Respect 

- [English](code-of-conduct.md)
- [French](CODE-DE-CONDUITE.md)

## License

[GPLV3](license.md)
