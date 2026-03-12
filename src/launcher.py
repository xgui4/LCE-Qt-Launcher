#!/usr/bin/env python3

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPalette, QPixmap, QBrush

from config import Config
from app_config import AppConfig

import webbrowser

config = Config()

appConfig = AppConfig()



SUCCESS_STATUS_CODE = 200

BACKGROUND_PIXMAP_IMG = ":/assets/background.png"

GEN_CONFIG_CMD_ARG = "--gen-config"
GEN_CONFIG_CMD_ARG_SHORT = "-g"
VERSION_CMD_ARG = "--version"
VERSION_CMD_ARG_SHORT = "-v"
LICENSE_CMD_ARG = "--license"
LICENSE_CMD_ARG_SHORT = "-L"
ABOUT_CMD_ARG = "--about"
ABOUT_CMD_ARG_SHORT = "-a"
HELP_CMD_ARG = "--help"
HELP_CMD_ARG_SHORT = "-h"

VERSION = "0.0.0.1-pre-alpha"
DESCRIPTION = """
This is a custom MCLCE Launcher written in python and Qt with Freedom 
and GNU/Linux support in mind.
"""
LICENSE = "GPLv3"
HELP_STR = """
-h or --help to get this help 
-v or --version to get the app version
-L or --license to get the license information
-a or --about to get information about the app
-g or --gen-config to generate or update the app config

"""

def launch():
        print("not implemented yet!")

def update_page():
    webbrowser.open_new_tab(config.LAUNCHER_REPO)

from ui_form import Ui_launcher

class launcher(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        background_pixmap = QPixmap(BACKGROUND_PIXMAP_IMG)
        if not background_pixmap.isNull():
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(background_pixmap))
            self.setPalette(palette)
            self.setAutoFillBackground(True)

        self.ui = Ui_launcher()
        self.ui.setupUi(self)
        self.ui.actionQuit.triggered.connect(app.quit)
        self.ui.playButton.clicked.connect(launch)
        self.ui.actionUpdate.triggered.connect(update_page)
        self.ui.actionAbout.triggered.connect(self.createPopupMenu)
        self.versionlabel = QLabel(f"Version {VERSION}")
        self.ui.statusbar.addPermanentWidget(self.versionlabel)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in (GEN_CONFIG_CMD_ARG , GEN_CONFIG_CMD_ARG_SHORT):
            config.generate_default_config()
            print("Config Updated !")
        elif sys.argv[1] in (VERSION_CMD_ARG, VERSION_CMD_ARG_SHORT):
            print(VERSION)
        elif sys.argv[1] in (LICENSE_CMD_ARG, LICENSE_CMD_ARG_SHORT):
            print(LICENSE)
        elif sys.argv[1] in (ABOUT_CMD_ARG, ABOUT_CMD_ARG_SHORT):
            print(DESCRIPTION)
        elif sys.argv[1] in (HELP_CMD_ARG, HELP_CMD_ARG_SHORT):
            print(HELP_STR)
    else:
        app = QApplication(sys.argv)

        try:
            with open("assets/styles/minecraft.qss", "r") as file:
                app.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error : qrc:/styles/minecraft.qss file not found. Reverting to default theme")

        widget = launcher()
        widget.show()
        sys.exit(app.exec())
