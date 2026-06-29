# Comment Obtenir

## Version taggé ![État de l'action de déploiement de la version Stable](https://github.com/xgui4/lce-qt-launcher/actions/workflows/stable.yml/badge.svg)

Sur la page [GitHub Releases de ce dépôt](https://github.com/xgui4/LCE-Qt-Launcher/releases/), vous trouverez les versions étiquetées, par exemple [Beta 0.0.1.1](https://github.com/xgui4/LCE-Qt-Launcher/releases/tag/0.0.0.1beta).

### Flatpak (Bientôt disponible) ![État de l'action de déploiement de Flatpak](https://github.com/xgui4/lce-qt-launcher/actions/workflows/flatpak.yml/badge.svg)

A Venir bientôt (décalé du a des problèmes techniques)

### FreeBSD Port (Expérimental)

Voir [mon overlay de ports FreeBSD](https://github.com/xgui4/freebsd-ports) pour installer le port games/lce-qt-laucher (py311-lce-qt-launcher).

### Version Nightly/Quotidienne (Nighly Build) ![État de l'action de déploiement de la version Nightly](https://github.com/xgui4/lce-qt-launcher/actions/workflows/nightly.yml/badge.svg)

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
