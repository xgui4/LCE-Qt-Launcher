# LCE Qt Launcher

[Version anglaise](readme.md)

![LCE-QT-Launcher](assets/io.github.xgui4.lce_qt_launcher.png)
![Capture d'écran du lanceur (version Alpha 0.0.20.0)](.github/screenshots/image.png)

- Autres Repo:
  - [Repo de backup](https://code.nolog.cz/xgui4/LCE-Qt-Launcher)
  - [Repo de données](https://code.nolog.cz/xgui4/lce-qt-Launcher-data)

> [!WARNING]
> Ce lanceur est en cours de développement et ses fonctionnalités peuvent être modifiées ou supprimées à tout moment.
> Les demandes d'aide (PR) pour corriger ou ajouter des fonctionnalités sont les bienvenues. Veuillez simplement respecter la [GPLv3](license.md) et le [Code de conduite](code-of-conduct.md).

##

> [!NOTE]
> Les mises à jour et installations automatiques des fichiers du jeu sont instables et peu fiables. Il est recommandé d'avoir déjà installé le jeu.
> En effet, le mécanisme d'installation et de mise à jour nécessite un dépôt externe qui peut être fermé sans préavis. Je fais de mon mieux, et les versions de développement (nightly) sont généralement à jour,
> mais la version stable est parfois retardée et nécessite une intervention manuelle.

## À propos

Un lanceur Minecraft LCE personnalisé multiplateforme gratuit, écrit avec PySide6 (Qt6 pour Python).

[Découvrez le site officiel de LCE Qt Launcher !](https://xgui4.github.io/LCE-Qt-Launcher/) ![État du déploiement sur la page GitHub](https://github.com/xgui4/lce-qt-launcher/actions/workflows/site.yml/badge.svg)

## Pourquoi LCE Qt Launcher ?

- Développé en Python avec Qt 6 : Prise en charge native des thèmes Linux et hautement personnalisable
- Intégration avec les outils communautaires
- Compatibilité GNU/Linux optimale
- Sans logiciel tiers
- Libre sous licence Freedom Launcher (GPLv3)

## Fonctionnalités

- Interface en ligne de commande (CLI)
- Prise en charge de plusieurs instances
- Places de marché :
- [LCE Hub Emeralds Launcher Workshop](https://github.com/LCE-Hub/piston)
- Actualités intégrées pour les instances
- Disponible en plusieurs formats :
- Version Nuitka : Linux et Windows
- AppImage (GNU/Linux uniquement)
- Package d'installation Inno Setup (pour la version Nuitka) (Windows)
- Portage FreeBSD
- Package Arch
- Flatpak (prochainement disponible)
- Environnement virtuel uv (portable)

## Objectif à long terme / Feuille de route

## Axes de développement à long terme

- Compatibilité GNU/Linux
- Prise en charge de Windows
- Prise en charge d'AppImage
- Centraliser toutes les fonctionnalités Minecraft LCE sur GNU/Linux
- Simplicité (éviter autant que possible les éléments superflus comme JavaScript)

## Fonctionnalités en cours de développement

- Prise en charge des thèmes
- Prise en charge expérimentale de FreeBSD et Nix/NixOS
- Prise en charge de Flatpak
- Prise en charge des localisations

## Fonctionnalités futures/en projet

- Séparation des données dans des dépôts distincts (lce-qt-launcher-data)
- Gestion personnalisée des versions/instances
Amélioration de l'interface et du mécanisme de gestion des instances
- Prise en charge de davantage d'outils communautaires
- Prise en charge des DLC NeoLegacy
- Amélioration de l'interface  et du mécanisme d'actualités
- Accessibilité

## Comment exécuter

Voir [`docs/fr/UTILISATION`](docs/fr/UTILISATION.md)

## Comment compiler/débugger

Voir [`docs/fr/COMPILATION`](docs/fr/COMPILATION.md)

## Bibliothèques et outils Python utilisés

- PySide 6
- platformdirs
- rich
- hatch
- uv

## Comment obtenir

Voir [`docs/fr/SETUP.md`](docs/fr/SETUP.md)

### Remerciements particuliers à

Voir [`THANKS.md`](THANKS.md)

## Code de respect

- [En Anglais](code-of-conduct.md)
- [En Français](CODE-DE-CONDUITE.md)

## Licence

[GPLv3](license.md)
