# LCE QT Launcher

![LCE-QT-Launcher](assets/Launcher.png)

> [!WARNING]
> This launcher is work in progress and its feature could be changes or remove at any time.
> PR are more than welcome to fix or add features. Just be compliant with the [GPLv3 license](license.mc) and [Code of Respect](code-of-conduct.md)

## About 

This is a custom Minecraft LCE Launcher written in Python and Qt with Freedom and GNU/Linux support in mind.

## Features 

- Command Line interface
- Qt 6 GUI (Native like Interface)
- Written in Python (No Electron or Rust)
- Customisable 
- Free Software (GPLv3)
- Multiple Instance (Work in progress)
<!-- Coming laters: 
- Plugins
- Skin support
- Modding Support 
-->
- GNU/Linux compatibility first (with secondary Windows and FreeBSD support)
- Focus on being the main hub for Minecraft LCE on GNU/Linux 
- Minecraft Theme pre-configured
 
## Software Requirement 

- [Python 3.12.x](https://www.python.org/downloads/latest/python3.12/)
    - with a virtual env with the required library install (specified in the readme and [`pyproject.toml`](pyproject.toml))
- [PySide6](https://pypi.org/project/PySide6/)
- [Monocraft Font](https://github.com/IdreesInc/Monocraft) installed 
- A display server or compositor (for Unix like system, MacOS and Windows use their own proprietary one)

## Python Library Used 
 - pyside6,
 - requests,
 - rich,
 - term-image,
 - pillow,
 - pip

## Compatible Operating System

- Windows 10 and later (not tested yet)
- GNU/Linux 
- MacOS (not officially supported, since I cannot test it, but should work with POISX compatibility)
- Android (not tested yet)

## Code of Respect 

- [English](code-of-conduct.md)
- [French](CODE-DE-CONDUITE.md)

## License
[GPLV3](license.md)
