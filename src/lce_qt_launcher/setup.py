#!/usr/bin/env python3
"""
LCE Qt Launcher Setup
Copyright (C) 2026 Xgui4

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see https://www.gnu.org/licenses/.
"""

from PySide6.QtWidgets import (
    QApplication,
)
from PySide6.QtGui import QFontDatabase

from lce_qt_launcher.views.setup_view import SetupView


def main():
    app = QApplication()
    app.setStyle("Fusion")

    font_id = QFontDatabase.addApplicationFont(":/fonts/monocraft.ttc")

    if font_id == -1:
        print("Error: Font could not be loaded.")
    else:
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        app.setFont(family)

    SetupView()


if __name__ == "__main__":
    main()
