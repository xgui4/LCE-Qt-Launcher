# Maintainer: Xgui4
pkgname=lce-qt-launcher-dev
pkgver=r153.26b153b
pkgrel=1
pkgdesc="A custom Minecraft LCE Launcher written with PySide6 (Python) with GNU/Linux support in mind."
arch=('any')
url="https://github.com/xgui4/LCE-Qt-Launcher"
license=('GPL-3.0-or-later')
depends=(
    'python' 
    'pyside6' 
    'python-requests' 
    'python-platformdirs'
    'python-rich'
) 
makedepends=(
    'git'     
    'bash' 
    'curl'             
    'python-build' 
    'python-installer' 
    'python-hatchling' 
    'python-wheel'
    'qt6-tools'
)
optdepends=(
    'wine: Allow to launch non-Linux-native Minecraft LCE ports' 
    'steam: Allow for Steam integration'
    'ttc-monocraft: Minecraft Font for the UI (Availaible in the AUR)'
)
provides=("${pkgname%-dev}" "${pkgname%}")
conflicts=("${pkgname%-nightly}" "${pkgname%}")
source=()
backup=("etc/lce-qt-launcher")

pkgver() {
    cd "$startdir"
  ( set -o pipefail
    git describe --long --abbrev=7 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
  )
}

build() {
    cd "$startdir"
    rm -rf dist/ build/
    /usr/bin/python -m build --wheel --no-isolation
}

package() {
    cd "$startdir"
    /usr/bin/python -m installer --destdir="$pkgdir" dist/*.whl
    install -d "$pkgdir/opt/lce_qt_launcher"
    cp -r data assets "$pkgdir"
    install -Dm644 data/lce_qt_launcher.ini "$pkgdir/etc/lce_qt_launcher.ini"
    install -Dm644 "pkg/io.github.xgui4.lce_qt_launcher.desktop" "$pkgdir/usr/share/applications/io.github.xgui4.lce_qt_launcher.desktop"
    install -Dm644 license.md -t "$pkgdir/usr/share/licenses/$pkgname/"
    install -Dm644 readme.md code-of-conduct.md -t "$pkgdir/usr/share/doc/$pkgname/"
    install -Dm644 "pkg/io.github.xgui4.lce_qt_launcher.metainfo.xml" "$pkgdir/usr/share/metainfo/io.github.xgui4.lce_qt_launcher.gtk.metainfo.xml"
}
