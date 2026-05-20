# LCE Qt Launcher

[Version anglaise](readme.md)

![LCE-QT-Launcher](assets/io.github.xgui4.lce_qt_launcher.png)
![Capture d'écran du lanceur](.github/screenshots/image.png)

> [!WARNING]
> Ce lanceur est en cours de développement et ses fonctionnalités peuvent être modifiées ou supprimées à tout moment.
> Les contributions (PR) sont les bienvenues pour corriger ou ajouter des fonctionnalités. Veuillez respecter la [licence GPLv3](license.md) et le [Code de conduite](CODE-DE-CONDUITE.md).

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
- Prise en charge des localisations
- Prise en charge expérimentale de FreeBSD et Nix/NixOS
- Devenir la plateforme principale pour Minecraft LCE sur GNU/Linux

## Comment exécuter

voir [`docs/fr/UTILISATION`](docs/fr/UTILISATION.md)

## Comment compiler/débugger

voir [`docs/fr/COMPILATION`](docs/fr/COMPILATION.md)

## Comment obtenir

### Version taggé

Sur la page [GitHub Releases de ce dépôt](https://github.com/xgui4/LCE-Qt-Launcher/releases/), vous trouverez les versions étiquetées, par exemple [Beta 0.0.1.1](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/0.0.0.1beta). Actuellement, il ne s'agit que du code source, mais la prochaine version inclura un programme d'installation, des paquets pour Windows et Linux, ainsi que des instructions pour FreeBSD Ports et un paquet Nix.

### Flatpak (Bientôt disponible)

A Venir bientôt (décalé du a des problèmes techniques)

### FreeBSD Port (Bientôt disponible)

A Venir bientôt (décalé du a des problèmes techniques)

### Version Nightly/Quotidienne (Nighly Build)

> [!NOTE]
> Cette branche n'est pas stable et des modifications y sont apportées presque quotidiennement. Elle peut donc parfois dysfonctionner. De plus, macOS n'est pas disponible dans la version de nuit en raison des restrictions d'Apple et du fait que je ne possède pas de Mac.

Sur cette page [GitHub Release](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/nightly), vous trouverez les versions Nightly, générées automatiquement via GitHub Actions lors de modifications apportées à la branche [`nightly`](https://github.com/xgui4/LCE-Qt-Launcher/tree/nightly).

### Via Git

Vous pouvez également télécharger ce dépôt avec la commande `git clone https://github.com/xgui4/lce-qt-launcher.git` puis le compiler (voir [`docs/fr/COMPILATION.md`](docs/fr/COMPILATION.md) pour plus d'informations) manuellement ou l'exécuter dans un environnement virtuel (.venv) (voir [`docs/fr/UTILISATION.md`](docs/fr/UTILISATION.md) pour plus d'informations).

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
- platformdirs
- rich
- hatch
- uv

## Systèmes d'exploitation compatibles

### Compatibilité officielle

> [!NOTE]
> Plateformes testées régulièrement et avec implémentation/correctif finalisé

- Windows 10 et versions ultérieures
- GNU/Linux

### Compatibilité expérimentale

> [!NOTE]
> Plateforme testée avec implémentation en cours de developement

- NixOS
- FreeBSD en utilisant UV (Remarque : le portage FreeBSD est en développement actif et encore expérimental ; l'utilisation de l'environnement virtuel UV est actuellement la seule méthode officiellement prise en charge pour FreeBSD.)

### Plateformes prises en charge partiellement

> [!NOTE]
> Plateformes non testées, mais avec implémentation

- Flatpak
- FreeBSD port

### Systèmes d'exploitation non pris en charge

> [!NOTE]
> Ces plateformes n'ont pas été testées et leur fonctionnement n'est pas garantis :

- Autres systèmes *BSD, car Minecraft LCE n'est pas pris en charge sur ces systèmes et Wine n'est pas disponible.
- Minecraft LCE sur Android est actuellement assez lent et bogué.
- macOS : LCE Qt Launcher ne prend pas officiellement en charge macOS et n'est pas testé lors des contributions, mais la compatibilité POISX devrait permettre son utilisation.

### Remerciements particuliers à

- [Prism Launcher](https://github.com/PrismLauncher/PrismLauncher) pour certains éléments et fichiers d'interface utilisateur
- [MCLCE/MinecraftConsoles](https://github.com/MCLCE/MinecraftConsoles)
aftConsoles) pour le portage du jeu sur PC
- [pieeebot/neoLegacy](https://github.com/pieeebot/neoLegacy) pour la rétrocompatibilité des mises à jour pour le portage PC
- [LCE Hub](https://github.com/LCE-Hub) pour la Marketplace/Workshop
- [HellishEnds](https://github.com/deadvoxelx/HellishEnds) - maintenant DCMA, il est donc supprimé/indisponible pour le moment
- [360Revived](https://github.com/BluTac10/360Revived) - maintenant DCMA, donc supprimé/inutilisable pour le moment

## Code de conduite

- [Anglais](code-of-conduct.md)
- [Français](CODE-DE-CONDUITE.md)

## Licence

[GPLv3](license.md)
