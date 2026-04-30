# LCE Qt Launcher

[Version anglaise](readme.md)

![LCE-QT-Launcher](assets/io.github.xgui4.lce_qt_launcher.png)
![Capture d'écran du lanceur](.github/screenshots/image.png)

> [!WARNING]
> Ce lanceur est en cours de développement et ses fonctionnalités peuvent être modifiées ou supprimées à tout moment.
> Les contributions (PR) sont les bienvenues pour corriger ou ajouter des fonctionnalités. Veuillez respecter la [licence GPLv3](license.md) et le [Code de conduite](code-of-conduct.md).

## À propos

Il s'agit d'un lanceur LCE personnalisé pour Minecraft, écrit en Python et Qt avec Freedom et conçu pour GNU/Linux.

## Pourquoi le lanceur LCE Qt ?

- Développé en Python avec Qt 6 : léger et compatible avec le thème Plasma 6/Qt 6 de GNU/Linux
- Personnalisation avec les thèmes et les modules/plugins (prochainement)
- Intégration avec les outils communautaires
- Compatibilité GNU/Linux optimale
- Licence copyleft (GPLv3), donc sans big tech
- Gratuit comme Freedom Launcher
- Thème Minecraft par défaut

## Fonctionnalités

- Interface en ligne de commande (CLI)
- Prise en charge de plusieurs instances (en cours de développement)
- Prise en charge des localisations (en cours de développement)
- Instances préconfigurées :
  - [MCLCE/MinecraftConsoles](https://github.com/mclce/minecraftconsoles) (anciennement smartcmd/MinecraftConsoles)
  - LegacyEvolved (sera bientôt supprimé car remplacé par NeoLegacy)
  - [NeoLegacy](https://github.com/pieeebot/neoLegacy/)
- Places de marché / Workshop :
  - [Atelier du lanceur Emeralds de LCE Hub](https://github.com/LCE-Hub/piston)
  - [LegacyMods (bientôt disponible)](https://legacymods.org/)
- Actualités intégrées

## Objectif à long terme / Feuille de route

- Accessibilité
- Prise en charge des mods
- Plugins pour le lanceur
- Prise en charge des thèmes
- Compatibilité GNU/Linux
- Prise en charge de Windows
- Prise en charge expérimentale de FreeBSD
- Devenir la plateforme principale pour Minecraft LCE sur GNU/Linux

## Comment exécuter

### VSCode

> [!NOTE]
> Sous Windows, remplacez `/` par `\`.

> [!WARNING]
> Cette méthode n'est ni recommandée ni testée pour NixOS. Consultez la section NixOS pour la procédure spécifique à ce système d'exploitation.

1. Créez un environnement virtuel Python à l'aide d'un outil comme UV (si ce n'est pas déjà fait).
2. Configurez VS Code pour utiliser cet environnement virtuel Python.
3. Exécutez « PySide : Sync Virtual Env and Launch ». 
4. Exécutez l'application via le mode débogage de VS Code ou directement le fichier [`src/lce_qt_launcher/main.py`](src/lce_qt_launcher/main.py).

### NixOS

1. Lancez le shell Nix avec la commande `nix-shell`.
2. Compilez l'interface utilisateur et le fichier de ressources avec `scripts/build.sh`.
3. Executé l'application avec `python src/lce_qt_launcher/main.py`.

### Autres

À venir

## Comment compiler

### Compilation portable avec Nuitka

0. Créez un environnement virtuel Python avec un outil comme UV (si ce n'est pas déjà fait).
1. Exécutez `hatch run packages`.

### Arch Linux

1. Accédez au répertoire `packages/linux`.
2. Choisissez un canal : dev, nightly ou stable (accédez au répertoire correspondant).
3. Exécutez `makepkg -si` ou `makepkg -s` (pour une installation sans paquets) dans l'un de ces répertoires.

### Paquet Nix

#### Nix Flake (Non testé/En cours de développement)
Exécutez `nix build`

#### Nixpkg
Exécutez `nix-build default.nix`

### Installateurs Flatpak et Windows

- Guide à venir

## Versions Quotidiennes (Nightly Release)

> [!NOTE]
> Les versions quotidiennes automatiques sont actuellement instable, très expérimentale et en développement actif.
> Cette branche n'est pas stable et des modifications y sont apportées presque quotidiennement ; elle peut donc parfois dysfonctionner. De plus, macOS n'est pas disponible dans la compilation nocturne en raison des restrictions d'Apple et du fait que je ne possède pas de Mac.

Sur cette page [GitHub Release](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/nightly), vous trouverez les versions nightly, générées automatiquement via GitHub Actions lors de modifications apportées à la branche `nighly`.

## Configuration logicielle requise

- [Python 3.11 (pour FreeBSD) à Python 3.12 (GNU/Linux, Windows et macOS)](https://www.python.org)
- Un environnement virtuel avec les bibliothèques requises installées (spécifiées dans le fichier README et le fichier [`pyproject.toml`](pyproject.toml))
- [PySide6](https://pypi.org/project/PySide6/)
- [Police Monocraft](https://github.com/IdreesInc/Monocraft) installée
- Pour les systèmes de type UNIX
  - Un serveur d'affichage ou un compositeur (sauf sur macOS où un serveur propriétaire est utilisé).
  - Bash (normalement préinstallé sous Linux, mais souvent requis sous *BSD et macOS)

## Bibliothèques et outils Python utilisés

- PySide 6
- requests
- platformdirs
- rich
- hatch
- uv

## Systèmes d'exploitation compatibles

### Compatibilité officielle

- Windows 10 et versions ultérieures
- GNU/Linux

### Compatibilité expérimentale

- NixOS

### Plateformes prises en charge prochainement 

- FreeBSD (Bien que cela puisse fonctionner, cela n'a pas encore été testé et le fonctionnement n'est pas garanti)
- Flatpak (Bien que cela puisse fonctionner, cela n'a pas encore été testé et le fonctionnement n'est pas garanti)

### Systèmes d'exploitation non pris en charge

- Autres systèmes *BSD, car Minecraft LCE n'est pas pris en charge sur ces systèmes et Wine n'est pas disponible.
- Minecraft LCE sur Android est actuellement assez lent et bogué.
- macOS : LCE Qt Launcher ne prend pas officiellement en charge macOS et n'est pas testé lors des contributions, mais la compatibilité POISX devrait permettre son utilisation.

### Remerciements particuliers à :

- [Prism Launcher](https://github.com/PrismLauncher/PrismLauncher) pour certains éléments et fichiers d'interface utilisateur
- [MCLCE/MinecraftConsoles](https://github.com/MCLCE/MinecraftConsoles)
aftConsoles) pour le portage du jeu sur PC
- [pieeebot/neoLegacy](https://github.com/pieeebot/neoLegacy) pour la rétrocompatibilité des mises à jour pour le portage PC
- [LCE Hub](https://github.com/LCE-Hub) pour la Marketplace/Workshop

## Code de conduite

- [Anglais](code-of-conduct.md)
- [Français](CODE-DE-CONDUITE.md)

## Licence

[GPLv3](license.md)
