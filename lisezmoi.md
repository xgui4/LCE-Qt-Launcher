# LCE Qt Launcher

[Version anglaise](readme.md)

![LCE-QT-Launcher](assets/io.github.xgui4.lce_qt_launcher.png)
![Capture d'écran du lanceur (version Alpha 0.0.20.0)](.github/screenshots/image.png)

- Autres Repo:
  - [Repo de backup](https://code.nolog.cz/xgui4/LCE-Qt-Launcher)
  - [Repo de données](https://code.nolog.cz/xgui4/lce-qt-Launcher-data)

> [!WARNING]
> Ce lanceur est en cours de développement et ses fonctionnalités peuvent être modifiées ou supprimées à tout moment.
> Les contributions (PR) sont les bienvenues pour corriger ou ajouter des fonctionnalités. Veuillez respecter la [licence GPLv3](license.md) et le [Code de conduite](CODE-DE-CONDUITE.md).

##

> [!NOTE]
> La mise à jour et l'installation automatiques des fichiers du jeu sont instables et non viables. Il est recommandé d'avoir déjà installé le jeu. En effet, le mécanisme d'installation et de mise à jour nécessite un dépôt externe qui peut être fermé sans préavis. Je fais de mon mieux et les versions de développement sont généralement à jour, mais la version stable est parfois en retard et nécessite une intervention manuelle.

## À propos

Il s'agit d'un lanceur LCE personnalisé pour Minecraft, écrit avec PySide6 (Qt6 pour Python) et conçu pour GNU/Linux.

## Pourquoi LCE Qt Launcher ?

- Développé en Python avec Qt 6 : léger et compatible avec le thème Plasma 6/Qt 6 de GNU/Linux
- Personnalisation avec les thèmes
- Intégration avec les outils communautaires
- Compatibilité GNU/Linux optimale
- Licence copyleft (GPLv3), donc sans big tech
- Launcher Libre

## Fonctionnalités

- Interface en ligne de commande (CLI)
- Prise en charge de plusieurs instances
- Instances préconfigurées :
  - [MCLCE/MinecraftConsoles](https://github.com/mclce/minecraftconsoles) (anciennement smartcmd/MinecraftConsoles)
  - [LCE-Revelation](https://git.revela.dev/itsRevela/LCE-Revelations)
  - [Aether Mod](https://github.com/Frcoxd/aether-papu)
- Places de marché / Workshop :
  - [Atelier du lanceur Emeralds de LCE Hub](https://github.com/LCE-Hub/piston)
  - [LegacyMods (bientôt disponible)](https://legacymods.org/)
- Actualités intégrées pour les instances

## Objectif à long terme / Feuille de route

- Accessibilité
- Prise en charge des thèmes
- Compatibilité GNU/Linux
- Support pour le format AppImage
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

Sur la page [GitHub Releases de ce dépôt](https://github.com/xgui4/LCE-Qt-Launcher/releases/), vous trouverez les versions étiquetées, par exemple [Beta 0.0.1.1](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/0.0.0.1beta).

### Flatpak (Bientôt disponible)

A Venir bientôt (décalé du a des problèmes techniques)

### FreeBSD Port (Expérimental)

Voir [mon overlay de ports FreeBSD](https://github.com/xgui4/freebsd-ports) pour installer le port games/lce-qt-laucher (py311-lce-qt-launcher).

### Version Nightly/Quotidienne (Nighly Build) ![Nightly Build Action Status](https://github.com/xgui4/lce-qt-launcher/actions/workflows/nightly.yml/badge.svg)

> [!NOTE]
> Cette branche n'est pas stable et des modifications y sont apportées presque quotidiennement. Elle peut donc parfois dysfonctionner. De plus, macOS n'est pas disponible dans la version nighly en raison des restrictions d'Apple et du fait que je ne possède pas de Mac.

Sur cette page [GitHub Release](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/nightly), vous trouverez les versions Nightly, générées automatiquement via GitHub Actions lors de modifications apportées à la branche [`dev`](https://github.com/xgui4/LCE-Qt-Launcher/tree/dev).

### AppImage et autres paquets Linux

Disponible dans la version de développement [nightly](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/nightly) et dans la version taguée (Bientôt disponible !). (Remarque : la génération automatique des paquets AppImage et Arch est actuellement défectueuse.)

### Via Git

Vous pouvez également télécharger ce dépôt avec la commande `git clone https://github.com/xgui4/lce-qt-launcher.git` puis le compiler (voir [`docs/fr/COMPILATION.md`](docs/fr/COMPILATION.md) pour plus d'informations) manuellement ou l'exécuter dans un environnement virtuel (.venv) (voir [`docs/fr/UTILISATION.md`](docs/fr/UTILISATION.md) pour plus d'informations).

## Configuration logicielle requise

- [Python 3.11 (pour FreeBSD) à Python 3.12 (GNU/Linux, Windows et macOS)](https://www.python.org)
- Un environnement virtuel avec les bibliothèques requises installées (spécifiées dans le fichier README et le fichier [`pyproject.toml`](pyproject.toml))
- [PySide6](https://pypi.org/project/PySide6/)
- [Police Monocraft](https://github.com/IdreesInc/Monocraft) installée
- [Police Miracode](https://github.com/IdreesInc/Miracode)
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
- FreeBSD Port & en venv (installation portable)
- AppImage

### Plateformes prises en charge  prochainement

> [!NOTE]
> Plateformes non testées, mais avec implémentation

- Flatpak

### Systèmes d'exploitation non pris en charge

> [!NOTE]
> Ces plateformes n'ont pas été testées et leur fonctionnement n'est pas garantis :

- Autres systèmes *BSD, car Minecraft LCE n'est pas pris en charge sur ces systèmes et Wine n'est pas disponible.
- Minecraft LCE sur Android est actuellement assez lent et bogué.
- macOS : LCE Qt Launcher ne prend pas officiellement en charge macOS et n'est pas testé lors des contributions, mais la compatibilité POISX devrait permettre son utilisation.

### Remerciements particuliers à

- [Prism Launcher](https://github.com/PrismLauncher/PrismLauncher) pour certains éléments et fichiers d'interface utilisateur
- [Communauté MCLCE/MinecraftConsoles](https://git.minecraftlegacy.com/backups/MinecraftConsoles) pour le portage du jeu sur PC
- [Communauté néoLegacy](https://github.com/neoStudiosLCE/neoLegacy) pour le rétroportage des mises à jour pour la version PC
- [Communauté LCE-Revelation](https://git.revela.dev/itsRevela/LCE-Revelations)
- [Communauté LCE Hub](https://github.com/LCE-Hub) pour le Marketplace/Workshop
- [Communauté MinecraftLegacy](https://github.com/MinecraftConsole) pour l'ajout de mon lanceur à leur liste
- [Miracode Police de caractères](https://github.com/IdreesInc/Miracode)
- [Monocraft Police de caractères](https://github.com/IdreesInc/Monocraft)
- [Steam Tinker Launch](https://github.com/sonic2kk/steamtinkerlaunch) pour l'intégration de Steam et SteamDeck sur GNU/Linux via leur logiciel.
- et merci a toute a communauté LCE pour continuer sa "legacy" et donc certains images viennents
- et merci à Notch (Markus Persson), 4J Studio pour avoir fait ce jeux.

## Code de respect

- [En Anglais](code-of-conduct.md)
- [En Français](CODE-DE-CONDUITE.md)

## Licence

[GPLv3](license.md)
