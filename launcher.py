#!/usr/bin/env python3

import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPalette, QPixmap, QBrush

from config import Config

import webbrowser
import requests
import zipfile
import io
import subprocess

config = Config()

LAUNCHER_REPO = "https://github.com/xgui4/LCE_QT_Launcher"

LAUNCHER_STRING = config.get__instance_url() + \
                  "/releases/download/" + \
                  config.get_instance_version() + "/" + \
                  config.get_instance_archive()

SUCCESS_STATUS_CODE = 200

BACKGROUND_PIXMAP_IMG = ":/assets/assets/background.png"

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
        config = Config()
        print(f"Lauching {config.get_instance_name()} {config.get_instance_version()}")
        
        print(f"Downloading {LAUNCHER_STRING}.")

        response = requests.get(LAUNCHER_STRING)

        if response.status_code == SUCCESS_STATUS_CODE:
            try:
                    with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
                        archive.extractall("./MinecraftLCEClient")
            except zipfile.BadZipFile as err:
                print(f"Error : {err}")
            except zipfile.zipfile.LargeZipFile as err:
                print(f"Error : {err}")
            else:
                client = f"./MinecraftLCEClient/{config.get_instance_exe_name}"
                print(f"Launching {client}")
                subprocess.run(client)
        else:
            print(f"Error : {response.status_code} during the dowbloading of the Minecraft LCE Client")

def update_page():
    webbrowser.open_new_tab(LAUNCHER_REPO)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
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
        widget = launcher()
        widget.show()
        sys.exit(app.exec())
