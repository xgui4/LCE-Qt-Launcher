{ pkgs ? import <nixpkgs> {} }:

let
  myPython = pkgs.python3.withPackages (ps: with ps; [
    pyside6
    requests
    shiboken6
    platformdirs
    rich
  ]);

  # Create standalone wrapper scripts
  pyside-uic = pkgs.writeShellScriptBin "pyside6-uic" ''
    exec ${pkgs.qt6.qtbase}/libexec/uic -g python "$@"
  '';
  
  pyside-rcc = pkgs.writeShellScriptBin "pyside6-rcc" ''
    exec ${pkgs.qt6.qtbase}/libexec/rcc -g python "$@"
  '';

in
pkgs.mkShell {
  buildInputs = with pkgs; [
    pyside-uic
    pyside-rcc
    monocraft
    qt6.qtbase
    qt6.qtwayland
    libGL
  ];

   postPatch = ''
    patchShebangs scripts/
    chmod +x scripts/*.sh
    substituteInPlace scripts/build.sh \
      --replace-fail "/usr/lib/qt6/rcc" "${pkgs.qt6.qtbase}/libexec/rcc" \
      --replace-fail "/usr/lib/qt6/uic" "${pkgs.qt6.qtbase}/libexec/uic"

    # Remove the build-time dependencies Nix doesn't need 
    # (this prevents Hatchling from complaining they are missing)
    sed -i '/"hatch<=/d' pyproject.toml
    sed -i '/"Nuitka<=/d' pyproject.toml
    sed -i '/"patchelf<=/d' pyproject.toml
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

  dontCheckRuntimeDeps = true;
  dontWrapQtApps = true;
  preFixup = ''
    makeWrapperArgs+=("''${qtWrapperArgs[@]}")
  '';

  shellHook = ''
    # Ensure our wrapped Python and tools are first in PATH
    export PATH="${myPython}/bin:${pyside-uic}/bin:${pyside-rcc}/bin:$PATH"
    
    # Reset PYTHONPATH to only include your source
    export PYTHONPATH="$(pwd)/src"

    # Tell UV which Python to use
    export UV_PYTHON="${myPython}/bin/python3"
    
    # NixOS Graphics & Qt Fixes
    export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath [ pkgs.libGL pkgs.stdenv.cc.cc ]}:$LD_LIBRARY_PATH"
    export QT_PLUGIN_PATH="${pkgs.qt6.qtbase}/${pkgs.qt6.qtbase.qtPluginPrefix}"
    export QT_QPA_PLATFORM_PLUGIN_PATH="${pkgs.qt6.qtbase}/lib/qt-6/plugins/platforms"

    echo "Environment Reset: Python is $(which python3)"
    echo "pyside6-uic is now $(which pyside6-uic) and outputs Python code."
  '';
}
