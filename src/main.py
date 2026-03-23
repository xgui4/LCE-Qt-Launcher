#!/usr/bin/env python3

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QDialog, QMessageBox, QFileDialog
from PySide6.QtGui import QPalette, QPixmap, QBrush
from PySide6.QtCore import qVersion
from user_pref import UserPref
from build_info import BuildInfo
from instance_manager import InstanceManager, Instance
from cmd_arg import CmdArgAction, parse_args, argsDetected

import term_service
import features

from theme import Theme
from json_trans import JsonTrans
from browser_dialog import BrowserDialog
from setting_dialog import SettingDialog
from cli import launch_cli

import sys
import os
import platform

userPref = UserPref()
buildInfo = BuildInfo()

translator = JsonTrans()

defaultInstance = Instance()
instanceManager = InstanceManager(defaultInstance, buildInfo)

BACKGROUND_PIXMAP_IMG = ":/assets/background.png"
ICON = ":/assets/launcher_small.png"
MINECRAFT_WEBSITE = "https://minecraft.net"
MINECRAFT_LCE_WEBSITE = "https://minecraftlegacy.com/"

theme = Theme.MINECRAFT.value

if platform.system() == "Linux": 
    _LINUX_QT6_PATH = "/usr/lib/qt6/plugins"
    os.environ["QT_PLUGIN_PATH"] = _LINUX_QT6_PATH

if platform.system() == "FreeBSD": 
    _FREEBSD_QT6_PATH = "/usr/local/lib/qt6/plugins"
    os.environ["QT_PLUGIN_PATH"] = _FREEBSD_QT6_PATH

HELP_STR = """
-h or --help to get this help 
-v or --version to get the app version
-L or --license to get the license information
-a or --about to get information about the app
-cl or --cli to launch the cli version
-g or --gen-config to generate or update the app config
"""

INSTANCE_MANAGER_LABEL = translator.translate("instance_manager_label")
SAVE_INSTANCE_MSG_BOX_LABEL = translator.translate("save_instance_msg_box_label")
STARTING_GAME_MSG = translator.translate("start_game_msg")

QUESTIONS_OPTIONS = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No

from ui_form import Ui_launcher
from ui_system_info import Ui_sys_info_dialog

def gen_inst_from_form(parent):
    instanceManager.instance = features.new_instance_from_form(parent)

def about_to_quit_event():
    anwser = QMessageBox.question(None, INSTANCE_MANAGER_LABEL, SAVE_INSTANCE_MSG_BOX_LABEL, QUESTIONS_OPTIONS)
    if anwser == QMessageBox.StandardButton.Yes:
        file_name = QFileDialog.getSaveFileName(None, "Set the instance save file path", f"{buildInfo.system_manager.found_default_save_path }(\"LCE Instance Save File\" (*{buildInfo.instance_extension}))")
        instanceManager.save_instance(file_name[0])

class launcher(QMainWindow):
    def confirm_changes_button(self):
        gen_inst_from_form(self)

    def update_page(self):
        BrowserDialog(self, buildInfo.git_repo_url)
    def launch(self):
        term_service.print_information(STARTING_GAME_MSG)
        instanceManager.play() 

    def install(self):
        button_reply = QMessageBox.question(self, 'Confirm Installation', 
                                            "Do you really want to re-install the game? " \
                                            "This version does not support update a installation yet," \
                                            " so a backup is recommended.",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if button_reply == QMessageBox.StandardButton.Yes:
            term_service.print_information("Starting Installation")
            self.ui.progressLabel.setVisible(True) 
            self.ui.progressBar.setVisible(True)
            self.ui.progressBar.setEnabled(True)
            self.ui.progressLabel.setText(f"Installation of {defaultInstance.name} Progress")
            self.ui.progressBar.setValue(30)
            instanceManager.install_instance() 
            self.ui.progressBar.setValue(100)
        else:
            QMessageBox.critical(self, "Minecraft LCE Qt Launcher" "Installation Cancelled")

    def show_aboutQt(self):
        print("Show About Qt popup.")
        QMessageBox.aboutQt(self, "About Qt")

    def show_about(self):
        self.aboutPopupWindow = QDialog() 

        self.aboutPopupWindow.setWindowTitle(f"About {buildInfo.app_name} {buildInfo.version}")

        imageLabel = QLabel()
        logoPixmap = QPixmap(ICON)
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

    def show_system_information(self):
        self.sysinfo_dialog.show()

    def show_about_minecraft(self):
        BrowserDialog(self, MINECRAFT_WEBSITE)
    
    def show_more_lce_projects(self):
        BrowserDialog(self, MINECRAFT_LCE_WEBSITE)

    def save_instance(self):
        file_name = QFileDialog.getSaveFileName(self, "Set the instance save file path to saved", f"{buildInfo.system_manager.found_default_save_path }(\"LCE Instance Save File\" (*{buildInfo.instance_extension}))")
        instanceManager.save_instance(file_name)

    def load_instance(self):
        file_name = QFileDialog.getSaveFileName(self, "Set the instance save file path to load", f"{buildInfo.system_manager.found_default_save_path }(\"LCE Instance Save File\" (*{buildInfo.instance_extension}))")
        instanceManager.load_instance(file_name)

    def show_setting_dialog(self):
        SettingDialog(self)

    def __init__(self, parent=None):
        super().__init__(parent)

        background_pixmap = QPixmap(BACKGROUND_PIXMAP_IMG)
        if not background_pixmap.isNull():
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(background_pixmap))
            self.setPalette(palette)
            self.setAutoFillBackground(True)
        else:
            term_service.print_error("Cannot set the background")

        self.ui = Ui_launcher()

        self.ui.setupUi(self)
        
        self.sysinfo_dialog = QDialog() 
        self.dialog_ui = Ui_sys_info_dialog()
        self.dialog_ui.setupUi(self.sysinfo_dialog)

        systemManager = buildInfo.system_manager

        self.dialog_ui.appVersion.setText(f"{buildInfo.app_name} Version {buildInfo.version_type} {buildInfo.version}")
        self.dialog_ui.qVersionLabel.setText(f"Qt Version {qVersion()}")
        self.dialog_ui.pyVersionLabel.setText(f"Python Version : {sys.version}")
        self.dialog_ui.osInfoLabel.setText(f"OS : {systemManager.name} \n Version : {systemManager.version}")
        self.dialog_ui.pluginsInfoLabel.setText("")
        self.dialog_ui.runnersLabel.setText("")

        self.ui.progressLabel.setVisible(False)
        self.ui.progressBar.setVisible(False)
        self.ui.progressBar.setEnabled(False)

        self.ui.playButton.clicked.connect(self.launch)
        self.ui.installButton.clicked.connect(self.install)
        self.ui.confirmChangesButton.clicked.connect(self.confirm_changes_button)
        self.ui.settingButton.clicked.connect(self.show_setting_dialog)

        self.ui.actionQuit.triggered.connect(app.quit)
        self.ui.actionUpdate.triggered.connect(self.update_page)
        self.ui.actionSystem_Information.triggered.connect(self.show_system_information)
        self.ui.actionAbout.triggered.connect(self.show_about)
        self.ui.actionAbout_QT.triggered.connect(self.show_aboutQt)
        self.ui.actionAbout_Minecraft.triggered.connect(self.show_about_minecraft)
        self.ui.actionMore_Minecraft_LCE_Projects.triggered.connect(self.show_more_lce_projects)
        self.ui.actionSave.triggered.connect(self.save_instance)
        self.ui.actionImport_Instance.triggered.connect(self.load_instance)

        self.versionlabel = QLabel(f"Version {buildInfo.version}")
        self.ui.statusbar.addPermanentWidget(self.versionlabel)

if __name__ == "__main__":
    action : CmdArgAction = parse_args(sys.argv)
    if argsDetected(action):
        if action == CmdArgAction.GEN_CONFIG:
            userPref.generate_default_config()
        if action == CmdArgAction.PRINT_LICENSE:
            term_service.print_information(f"{buildInfo.app_name} is licensed via the {buildInfo.license} License.")
            term_service.print_information(f"See {buildInfo.license_link} for more info")
        if action == CmdArgAction.PRINT_HELP:
            print(HELP_STR)
        if action == CmdArgAction.PRINT_ABOUT_INFO:
            term_service.print_information("This is a custom Minecraft LCE Launcher written in Python and Qt with Freedom and GNU/Linux support in mind.")
        if action == CmdArgAction.PRINT_VERSION: 
            term_service.print_information(f"{buildInfo.app_name} Version {buildInfo.version}")
            term_service.print_information(f"Qt Version {buildInfo.qt_version}")
        if action == CmdArgAction.CLI_VERSION:
            launch_cli()
        else:
            term_service.print_information("Not Implemented Yet!")
    else:
        app = QApplication(sys.argv)
        try:
            with open(":/styles/minecraft.qss", "r") as file:
                app.setStyleSheet(file.read())
        except FileNotFoundError:
            QMessageBox.warning(None,"Error", f"{theme} file not found. Reverting to default theme")

        widget = launcher()
        widget.show()

        app.aboutToQuit.connect(gen_inst_from_form)

        sys.exit(app.exec())
