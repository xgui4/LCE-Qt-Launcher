#!/usr/bin/env python3

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QDialog, QMessageBox
from PySide6.QtGui import QPalette, QPixmap, QBrush

from user_pref import UserPref
from build_info import BuildInfo
# from downloader import Downloader
from instance_manager import InstanceManager, Instance
from cmd_arg import CmdArgAction, parse_args, argsDetected

import webbrowser
import sys

userPref = UserPref()
buildInfo = BuildInfo()
# downloader = Downloader()

defaultInstance = Instance()
instanceManager = InstanceManager(defaultInstance)

SUCCESS_STATUS_CODE = 200

BACKGROUND_PIXMAP_IMG = ":/assets/background.png"

def update_page():
    webbrowser.open_new_tab(userPref.LAUNCHER_REPO)

from ui_form import Ui_launcher

class launcher(QMainWindow):
    def launch(self):
        instanceManager.play() 
    def show_aboutQt(self):
        QMessageBox.aboutQt(self, "About Qt")
    def show_about(self):
        self.aboutPopupWindow = QDialog() 
        self.aboutPopupWindow.setWindowTitle(f"About {buildInfo.app_name} {buildInfo.version}")

        imageLabel = QLabel()

        logoPixmap = QPixmap(":/assets/launcher_small.png")

        imageLabel.setPixmap(logoPixmap)

        mainLayout = QVBoxLayout(self.aboutPopupWindow)

        titleLabel = QLabel(buildInfo.app_name)

        versionLabel = QLabel(f"Version {buildInfo.version}")

        licenseLabel = QLabel(f"License {buildInfo.license}")

        mainLayout.addWidget(imageLabel)
        mainLayout.addWidget(titleLabel)
        mainLayout.addWidget(versionLabel)
        mainLayout.addWidget(licenseLabel)
        
        self.aboutPopupWindow.show()

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
        self.ui.playButton.clicked.connect(self.launch)
        self.ui.actionUpdate.triggered.connect(update_page)

        self.ui.actionAbout.triggered.connect(self.show_about)

        self.ui.actionAbout.triggered.connect(QMessageBox.aboutQt)

        self.versionlabel = QLabel(f"Version {buildInfo.version}")
        self.ui.statusbar.addPermanentWidget(self.versionlabel)

if __name__ == "__main__":
    action : CmdArgAction = parse_args(sys.argv)
    if argsDetected(action):
        if action == CmdArgAction.GEN_CONFIG:
            userPref.generate_default_config()
        if action == CmdArgAction.PRINT_LICENSE:
            print(f"{buildInfo.app_name} is licensed via the {buildInfo.license} License.")
            print(f"See {buildInfo.license_link} for more info")
        if action == CmdArgAction.PRINT_HELP:
            print("Not Implemented Yet!")
        if action == CmdArgAction.PRINT_ABOUT_INFO:
            print("Not Inplemented Yet!")
        if action == CmdArgAction.PRINT_VERSION: 
            print(f"{buildInfo.app_name} Version {buildInfo.version}")
            print(f"Qt Version {buildInfo.qt_version}")
        else:
            print("Not Implemented Yet!")
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
