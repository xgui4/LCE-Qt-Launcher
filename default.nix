{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonApplication rec {
  pname = "lce-qt-launcher";
  version = "2026.4.26";
  format = "pyproject";

  src = ./.;

  nativeBuildInputs = [
    pkgs.python3Packages.hatchling
    pkgs.python3Packages.pyside6
    pkgs.python3Packages.shiboken6 
    pkgs.qt6.wrapQtAppsHook
    pkgs.qt6.qtbase
    pkgs.qt6.qtbase.dev
    pkgs.qt6.qttools
    pkgs.bash
    pkgs.coreutils
    pkgs.gnused
  ];

  propagatedBuildInputs = with pkgs.python3Packages; [
    pyside6
    requests
    platformdirs
    rich
  ];

  postPatch = ''
    patchShebangs scripts/
    chmod +x scripts/*.sh
    substituteInPlace scripts/build.sh \
      --replace-fail "/usr/lib/qt6/rcc" "rcc" \
      --replace-fail "/usr/lib/qt6/uic" "uic"
  '';

  # Manual installation of non-Python assets (Desktop files, icons, etc.)
  postInstall = ''
    # Desktop Entry & Mime
    install -Dm644 "packages/io.github.xgui4.lce_qt_launcher.desktop" "$out/share/applications/io.github.xgui4.lce_qt_launcher.desktop"
    install -Dm644 "packages/lce_inst-mime.xml" "$out/share/mime/packages/io.github.xgui4.lce_qt_launcher.xml"
    install -Dm644 "packages/io.github.xgui4.lce_qt_launcher.metainfo.xml" "$out/share/metainfo/io.github.xgui4.lce_qt_launcher.metainfo.xml"

    # Icons
    install -Dm644 "assets/io.github.xgui4.lce_qt_launcher.png" "$out/share/icons/hicolor/128x128/apps/io.github.xgui4.lce_qt_launcher.png"
    install -Dm644 "assets/lce_inst.png" "$out/share/icons/hicolor/128x128/mimetypes/application-x-lce_inst.png"

    # Data/Assets (Mirroring your /opt logic into Nix share)
    mkdir -p "$out/share/${pname}"
    cp -r data assets "$out/share/${pname}/"

    # Docs
    install -Dm644 "license.md" -t "$out/share/licenses/${pname}/"
    install -Dm644 "readme.md" "code-of-conduct.md" -t "$out/share/doc/${pname}/"
  '';

  dontWrapQtApps = true;
  preFixup = ''
    makeWrapperArgs+=("''${qtWrapperArgs[@]}")
  '';

  meta = with pkgs.lib; {
    description = "A custom Minecraft LCE Launcher written in Python and Qt with GNU/Linux support in mind.";
    license = licenses.gpl3;
    platforms = platforms.linux;
    mainProgram = "lce-qt-launcher";
  };
}
