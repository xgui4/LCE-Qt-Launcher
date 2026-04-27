# LCE-Qt-Launcher Nix Packages

{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonApplication rec {
  pname = "lce-qt-launcher";
  version = "2026.4.26";
  format = "pyproject";

  src = ./.;

  # Outils nécessaires à la compilation
  nativeBuildInputs = [
    pkgs.python3Packages.hatchling
    pkgs.qt6.wrapQtAppsHook  # Indispensable ici pour le wrap automatique
  ];

  # Dépendances Python (Note: pas de virgules dans les listes Nix)
  propagatedBuildInputs = with pkgs.python3Packages; [
    pyside6
    requests
    platformdirs
    rich
  ];

  # On s'assure que le wrapper Qt est appliqué aux exécutables Python
  dontWrapQtApps = true; # On désactive le wrap automatique global...

  preFixup = ''
    makeWrapperArgs+=("''${qtWrapperArgs[@]}")
  ''; # ...pour l'injecter proprement dans le wrapper Python (meilleure pratique)

  meta = with pkgs.lib; {
    description = "A custom Minecraft LCE Launcher written in Python and Qt with GNU/Linux support in mind.";
    license = licenses.gpl3;
    platforms = platforms.linux;
    mainProgram = "lce-qt-launcher";
  };
}
