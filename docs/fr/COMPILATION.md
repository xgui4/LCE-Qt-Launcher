# Comment compiler

## Compilation portable de Nuitka

0. Créez un environnement virtuel Python avec un outil comme UV (si ce n'est pas déjà fait).
1. Exécutez `hatch run packages`.

### Arch Linux

1. Accédez au répertoire `packages/linux`.
2. Choisissez un canal : dev, nightly ou stable (accédez au répertoire correspondant).
3. Exécutez `makepkg -si` ou `makepkg -s` (pour une installation sans modification) dans l'un de ces répertoires.

### Paquet Nix

<!--
#### Nix Flake (Bientôt disponible)

Exécutez `nix build`.

-->
#### Nixpkg

```bash

if [[ $user_input == "install" ]]; then

nix-build default.nix

nix-env -i ./result
fi
if [[ $user_input == "compile" ]]; puis

./scripts/build.sh
fi puis

./scripts/clear.sh
fi

```

#### Programme d'installation Windows

Prérequis :
[Inno Setup 6.6+](https://jrsoftware.org/isdl.php)

1. Accédez au répertoire des paquets Windows : `cd packages/windows`
2. Exécutez le script avec Inno Setup pour le canal souhaité : [`setup-nightly.iss`](packages/windows/setup-nightly.iss) ou [`setup.iss`](packages/windows/setup.iss)

#### FreeBSD

Utilité mon FreeBSD Port [Overlay](https://github.com/xgui4/freebsd-ports/tree/master/lce-qt-launcher)

#### Flatpak

> [!NOTE]
> Pour Flatpak, la compilation manuelle est recommandée uniquement à des fins de développement ou pour les forks ne disposant pas de dépôt Flatpak.
> Actuellement, il s'agit de la seule méthode disponible, le dépôt Flatpak officiel n'étant pas encore activé. Une fois activé, cette partie de l'annonce sera supprimée et il sera alors recommandé d'utiliser le dépôt Flatpak, qui sera affiché ici.

1. Accédez au répertoire contenant le manifeste Flatpak : `cd packages/flatpak`
2. Compilez Flatpak : `flatpak-builder --user --install build-dir io.github.xgui4.lce_qt_launcher.yml --install-deps-from=flathub`
