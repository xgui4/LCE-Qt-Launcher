# Setup

## Tag Release ![Stable release deployment action status](https://github.com/xgui4/lce-qt-launcher/actions/workflows/stable.yml/badge.svg)

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
