# Comment compiler

## Compilation portable de Nuitka

0. Créez un environnement virtuel Python avec un outil comme UV (si ce n'est pas déjà fait).
1. Exécutez `hatch run packages`.

### Arch Linux

1. Accédez au répertoire `packages/linux`.
2. Choisissez un canal : dev, nightly ou stable (accédez au répertoire correspondant).
3. Exécutez `makepkg -si` ou `makepkg -s` (pour une installation sans modification) dans l'un de ces répertoires.

### Paquet Nix

#### Nix Flake (Expérimental)

1. Exécutez `nix build`.

#### Nixpkg

1. nix-build default.nix
2. nix-env -i ./result

#### Programme d'installation Windows

Prérequis :
[Inno Setup 6.6+](https://jrsoftware.org/isdl.php)

1. Accédez au répertoire des paquets Windows : `cd packages/windows`
2. Exécutez le script avec Inno Setup pour le canal souhaité : [`nightly.iss`](packages/windows/setup-nightly.iss) ou [`stable.iss`](packages/windows/stable.iss)

#### Via système de portage FreeBSD (Expérimental)

> [!NOTE]
> La version pour le system de portage pour FreeBSD n'est actuellement disponible que pour la dernière version étiquetée et est expérimental. Il peut arriver qu'il y ait un retard de version. Pour obtenir une version de développement ou une version personnalisée, la méthode UV est actuellement la seule méthode officiellement prise en charge.

Utilité mon FreeBSD Port [Overlay](https://github.com/xgui4/freebsd-ports/tree/master/lce-qt-launcher)

#### Flatpak (Bientôt)

Le support pour flatpak est a venir et ne marche pas correctement pour le moment

<!-- 
> [!NOTE]
> Pour Flatpak, la compilation manuelle est recommandée uniquement à des fins de développement ou pour les forks ne disposant pas de dépôt Flatpak.
> Actuellement, il s'agit de la seule méthode disponible, le dépôt Flatpak officiel n'étant pas encore activé. Une fois activé, cette partie de l'annonce sera supprimée et il sera alors recommandé d'utiliser le dépôt Flatpak, qui sera affiché ici.

1. Accédez au répertoire contenant le manifeste Flatpak : `cd packages/flatpak`
2. Compilez Flatpak : `flatpak-builder --user --install build-dir io.github.xgui4.lce_qt_launcher.yml --install-deps-from=flathub`
-->

### AppImage (GNU/Linux uniquement)

1. Accédez à l'environnement virtuel et activez-le.
2. Installez le paquet pyproject-appimage.
3. Exécutez pyproject-appimage.
