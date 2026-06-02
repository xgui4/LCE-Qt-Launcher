# Comment exécuter

## VSCode

> [!NOTE]
> Sous Windows, vous devrez peut-être remplacer `/` par `\`.
> [!WARNING]
> Cette méthode n'est ni recommandée ni testée pour NixOS. Consultez la section NixOS pour connaître la procédure spécifique à ce système d'exploitation.

1. Créez un environnement virtuel Python à l'aide d'un outil comme UV (si ce n'est pas déjà fait).
2. Configurez VSCode pour utiliser cet environnement virtuel Python.
3. Exécutez « Pyside : Synchroniser l'environnement virtuel et lancer ».
4. Lancez l'application via le mode débogage de VSCode ou directement le fichier [`src/lce_qt_launcher/main.py`](src/lce_qt_launcher/main.py).

## FreeBSD

1. Crée un environnemnt python virtuelle avec accès system avec la commande `uv venv --system-site-packages`
2. Synchroniser l'environnement virtuelle avec `uv sync`
3. Activer l'environnement virtuelle (remplace {.sh} par .sh pour bash, .fish  pour fish ou rien pour le shell POSIX) `source .venv/bin/activate{.sh}`
4. Executer le programme avec la commande `python src/lce_qt_launcher/main.py`

## NixOS

1. Lancez le shell Nix avec la commande `nix-shell`.
2. Compilez l'interface utilisateur et le fichier de ressources avec `scripts/build.sh`.
3. Chargez l'application avec `python src/lce_qt_launcher/main.py`.

## Utilisation de la ligne de commande

1. Créez l'environnement virtuel (venv) avec uv (`uv sync`).
2. Chargez le venv avec `source .venv/bin/activate.sh` (remplacez `.sh` par votre shell : sous Windows, `.venv\Scripts\activate.ps1` pour PowerShell ou `.venv\Scripts\activate.bat` pour l'invite de commandes).
3. Exécutez `scripts/build.sh` (pour Linux) ou `scripts\build.cmd` (pour Windows).
4. Exécutez le script Python principal. `src/lce_qt_launche.py` (Sous Windows, vous devrez peut-être invoquer directement `python3` et remplacer `/` par `\`)

## AppImage (GNU/Linux uniquement)

1. `chmod +x <nom_du_fichier_appimage>`
2. `./<nom_du_fichier_appimage>`
