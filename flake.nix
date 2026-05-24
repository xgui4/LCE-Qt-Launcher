{
  description = "A custom Minecraft LCE Launcher written with PySide6 (Qt6 for Python) with Freedom and with GNU/Linux support in mind.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        # Wraps your existing package definition
        packages.default = import ./default.nix { inherit pkgs; };

        # Wraps your existing dev shell environment
        devShells.default = import ./shell.nix { inherit pkgs; };
      }
    );
}