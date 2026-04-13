# LCE QT Launcher

[Version Anglaise](readme.md)

![LCE-QT-Launcher](assets/images/Launcher.png)
![Capture d'écran du lanceur](.github/screenshots/image.png)

> [!WARNING]
> Ce lanceur est en cours de développement et ses fonctionnalités peuvent être modifiées ou supprimées à tout moment.
> Les contributions (PR) sont les bienvenues pour corriger ou ajouter des fonctionnalités. Veuillez respecter la [licence GPLv3](license.md) et le [Code de conduite](CODE-DE-CONDUITE.md).

## À propos

Il s'agit d'un lanceur LCE personnalisé pour Minecraft, écrit en Python et Qt avec Freedom et conçu pour être compatible avec GNU/Linux.

## Fonctionnalités

- Interface en ligne de commande (CLI)
- Interface graphique Qt 6 (interface de type natif)
- Écrit en Python (sans Electron ni Rust)
- Personnalisable
- Logiciel libre (GPLv3)
- Instances multiples (en cours de développement)
- Localisations (en cours de développement)
<!-- Prochainement :
- Plugins du Lanceur
- Prise en charge des skin
- Prise en charge des mods -->
- Plusieurs instances par défaut : MCLE et Legacy Evolved
- Actualités intégrées
- Thème Minecraft préconfiguré

## Objectif à long terme

- Accessibilité
- Compatibilité GNU/Linux
- Prise en charge de Windows
- Prise en charge expérimentale de FreeBSD
- Devenir la plateforme principale pour Minecraft LCE sur GNU/Linux

## Comment exécuter

### VSCode

1. Créez un environnement virtuel Python avec un outil comme UV.
2. Configurez VSCode pour utiliser cet environnement virtuel Python.
3. Exécutez « PySide : Sync Virtual Env and Launch ». 
4. Exécutez l'application via le mode débogage de VS Code ou via directement le fichier [`src/main.py`](src/main.py).

### Autres

Guide à venir

## Comment compiler

Disponible dans la prochaine version stable, lorsque le programme sera plus stable.

## Versions Quotidiennes (Nightly Release)

> [!NOTE]
> Les versions quotidiennes automatiques sont actuellement instable, très expérimentale et en développement actif.
> Cette branche n'est pas stable et des modifications y sont apportées presque quotidiennement ; elle peut donc parfois dysfonctionner. De plus, macOS n'est pas disponible dans la compilation nocturne en raison des restrictions d'Apple et du fait que je ne possède pas de Mac. En raison d'un problème temporaire, la compilation automatique Linux a été désactivée car elle remplaçait la compilation Windows. Cette fonctionnalité sera réactivée une fois le problème résolu.

Sur cette page [GitHub Release](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/nightly), vous trouverez les versions de développement quotidiennes automatiques (Nighly Build), générées automatiquement via GitHub Actions lors de modifications apportées à la branche `nighly`.

## Configuration logicielle requise

- [Python 3.11 (Pour FreeBSD) ou Python 3.12 ((GNU/Linux, Windows ou MacOS)](https://www.python.org)
- Un environnement virtuel avec les bibliothèques requises installées (spécifiées dans le fichier README et [`pyproject.toml`](pyproject.toml))
- [PySide6](https://pypi.org/project/PySide6/)
- [Police Monocraft](https://github.com/IdreesInc/Monocraft) installée
- Pour un système de type UNIX
    - Un serveur d'affichage ou un compositeur (sauf sur macOS où un serveur propriétaire est utilisé)
    - Bash (Généralement préinstallé sous Linux, mais souvent requis sous *BSD et macOS)

## Bibliothèques et outils Python utilisés

- PySide 6
- requests
- rich
- hatch
- uv

## Systèmes d'exploitation compatibles

### Compatibilité optimale

- Windows 10 et versions ultérieures
- GNU/Linux

### Compatibilité expérimentale

- FreeBSD

### Systèmes d'exploitation non pris en charge

- Autres systèmes *BSD
- Android : Minecraft LCE présente actuellement des ralentissements et des bugs importants sur Android.
- macOS : les tests ne sont pas autorisés, mais la compatibilité POISX devrait permettre de l'utiliser. Cependant, ce système n'est pas officiellement pris en charge.

## Remerciements

- [Prism Launcher](https://github.com/PrismLauncher/PrismLauncher) pour certains éléments et fichiers d'interface utilisateur
- [MCLCE/MinecraftConsoles](https://github.com/MCLCE/MinecraftConsoles) pour le portage du jeu

## Code de conduite

- [Anglais](code-of-conduct.md)
- [Français](CODE-DE-CONDUITE.md)

## Licence

[GPLv3](license.md)