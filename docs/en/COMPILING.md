# How to build

## Portable Nuitka Build

0. Create a Python Virtual Env via a tool like UV (if not already done)
1. Run `hatch run packages`

### Arch Linux

1. Go the [`packages/linux` directory](packages/linux)
2. Choose a channel dev, nigthly or stable (go to the directory)
3. Run `makepkg -si` or `makepkg -s` (for no install) in one of these directory

### Nix Package

<!--
#### Nix Flake (Coming Soon)

  Run `nix build`
-->
#### Nixpkg

```bash

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

```

#### Windows Installer

Requirements :
  [Inno Setup 6.6+](https://jrsoftware.org/isdl.php)

  1. Go to the windows packages locations : `cd pacakges/windows`
  2. run the script with Inno Setup for your desired channel [`setup-nightly.iss`](packages/windows/setup-nigthly.iss) or [`setup.iss`](packages/windows/setup.iss))

#### FreeBSD

1. go to the freebsd port folder : `cd freebsd-ports`
2. run the install scripts : `install`

#### Flatpak

> [!NOTE]
> For Flatpak, manual building is only recommended for development purposes or for forks that don't have a Flatpak repository.
> Currently, this is the only method since the official Flatpak repository is not yet activated. Once activated, this part of the notice will be removed, and it will then be recommended to use the Flatpak repository, which will be displayed here.

1. Go to the flatpak manifest location : `cd packages/flatpak`
2. Build the flatpak : `flatpak-builder --user --install build-dir io.github.xgui4.lce_qt_launcher.yml --install-deps-from=flathub`
