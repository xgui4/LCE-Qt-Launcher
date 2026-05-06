{
  description = "LCE Qt Launcher Flake  - A custom Minecraft LCE Launcher written in Python and Qt with GNU/Linux support in mind.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};

        python = pkgs.python314;

        nativeBuildInputs = with pkgs; [
         python
         python3Packages.pyside6
         python3Packages.shiboken6
         python3Packages.requests
         python3Packages.platformdirs
         python3Packages.rich
         python3Packages.vdf
         qt6.wrapQtAppsHook
         python3Packages.shiboken6
         qt6.wrapQtAppsHook
         qt6.qtbase
         qt6.qtbase.dev
         qt6.qttools
         bash
         coreutils
         gnused
         libGL
        ];

        buildInputs = with pkgs; [];
      in {
        devShells.default = pkgs.mkShell {inherit nativeBuildInputs buildInputs;};

        packages.default = python.pkgs.buildPythonApplication {
          pname = "lce_qt_launcher";
          version = "0.2026.5.6";
          format = "hatchling";
          license = pkgs.lib.licenses.gpl3plus;

          src = ./.;

          # True if tests
          doCheck = false;

          inherit nativeBuildInputs buildInputs;
        };
      }
    );
}