# How to build

## Portable Nuitka Build

0. Create a Python Virtual Env via a tool like UV (if not already done)
1. Run `hatch run packages`

### Arch Linux

1. Go the [`packages/linux` directory](packages/linux)
2. Choose a channel dev, nigthly or stable (go to the directory)
3. Run `makepkg -si` or `makepkg -s` (for no install) in one of these directory

### Nix Package

Documentation Coming Soon

#### Windows Installer

Requirements :
  [Inno Setup 6.6+](https://jrsoftware.org/isdl.php)

  1. Go to the windows packages locations : `cd pacakges/windows`
  2. run the script with Inno Setup for your desired channel [`nightly.iss`](packages/windows/setup-nigthly.iss) or [`stable.iss`](packages/windows/setup.iss))

#### FreeBSD Port (Experimental)

> [!NOTE]
> The FreeBSD port is only avaiable for the latest tagged release right now and is experimental. And sometime may lagged in version. To get the nightly build or custom version, the UV method is currently the only officially supported method.

Using my Github FreeBSD [Overlay](https://github.com/xgui4/freebsd-ports/tree/master/lce-qt-launcher)

#### Flatpak (Coming soon)

Flatpak support is in the work, but is not working right now.
<!--
> [!NOTE]
> For Flatpak, manual building is only recommended for development purposes or for forks that don't have a Flatpak repository.
> Currently, this is the only method since the official Flatpak repository is not yet activated. Once activated, this part of the notice will be removed, and it will then be recommended to use the Flatpak repository, which will be displayed here.

1. Go to the flatpak manifest location : `cd packages/flatpak`
2. Build the flatpak : `flatpak-builder --user --install build-dir io.github.xgui4.lce_qt_launcher.yml --install-deps-from=flathub`
-->