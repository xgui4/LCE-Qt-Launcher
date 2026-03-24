#!/usr/bin/env python3

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QDialog, QMessageBox, QFileDialog
from PySide6.QtGui import QPalette, QPixmap, QBrush
from PySide6.QtCore import qVersion
from user_pref import UserPref
from build_info import BuildInfo, get_assets_dir
from instance_manager import InstanceManager, Instance
from cmd_arg import CmdArgAction, parse_args, argsDetected

import term_service
import features

from theme import Theme
from json_trans import JsonTrans

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

# if platform.system() == "Linux": 
  #  _LINUX_QT6_PATH = "/usr/lib/qt6/plugins"
  #  os.environ["QT_PLUGIN_PATH"] = _LINUX_QT6_PATH

# if platform.system() == "FreeBSD": 
   # _FREEBSD_QT6_PATH = "/usr/local/lib/qt6/plugins"
   # os.environ["QT_PLUGIN_PATH"] = _FREEBSD_QT6_PATH

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

SAVE_FILEDIALOG_TITLE = "save_filedialog_title"

QUESTIONS_OPTIONS = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No

from ui_form import Ui_launcher
from ui_system_info import Ui_sys_info_dialog

def gen_inst_from_form(parent):
    instanceManager.instance = features.new_instance_from_form(parent)

def about_to_quit_event():
    anwser = QMessageBox.question(None, INSTANCE_MANAGER_LABEL, SAVE_INSTANCE_MSG_BOX_LABEL, QUESTIONS_OPTIONS)
    if anwser == QMessageBox.StandardButton.Yes:
        file_name = QFileDialog.getSaveFileName(None, SAVE_FILEDIALOG_TITLE, f"{buildInfo.system_manager.found_default_save_path }(\"LCE Instance Save File\" (*{buildInfo.instance_extension}))")
        instanceManager.save_instance(file_name[0])

class launcher(QMainWindow):
    def confirm_changes_button(self):
        gen_inst_from_form(self)

    def update_page(self):
        features.show_webbrowser(self, buildInfo.git_repo_url)

    def launch(self):
        features.launch_game(instanceManager, STARTING_GAME_MSG)

    def install(self):
        features.install_game(self, defaultInstance, instanceManager)

    def show_aboutQt(self):
        features.show_about_qt(self)

    def show_about(self):
        features.show_about_app(self, buildInfo, ICON)

    def show_system_information(self):
        features.show_system_info(self)

    def show_about_minecraft(self):
        features.show_webbrowser(self, MINECRAFT_WEBSITE)

    def show_more_lce_projects(self):
        features.show_webbrowser(self, MINECRAFT_LCE_WEBSITE)

    def save_instance(self):
        features.save_instance(self, instanceManager, buildInfo)

    def load_instance(self):
        features.load_instance(self, instanceManager, buildInfo)

    def show_setting_dialog(self):
        features.show_setting(self)

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
            features.generate_user_config(userPref)
        if action == CmdArgAction.PRINT_LICENSE:
            features.display_license(buildInfo)
        if action == CmdArgAction.PRINT_HELP:
            features.display_help(HELP_STR)
        if action == CmdArgAction.PRINT_ABOUT_INFO:
            features.display_about("This is a custom Minecraft LCE Launcher written in Python and Qt with Freedom and GNU/Linux support in mind.")
        if action == CmdArgAction.PRINT_VERSION: 
            features.display_version(buildInfo)
        if action == CmdArgAction.CLI_VERSION:
            features.launch_cli_interfaces()
        else:
            term_service.print_information("Not Implemented Yet!")
    else:
        app = QApplication(sys.argv)
        
        try:
            with open(":/styles/minecraft.qss", "r") as file:
                app.setStyleSheet(file.read())
        except FileNotFoundError:
            try: 
                with open(os.path.join(get_assets_dir(), "styles", "minecraft.qss"), "r") as file:
                    app.setStyleSheet(file.read())
            except FileNotFoundError:
                QMessageBox.warning(None,"Error", f"{theme} file not found. Reverting to default theme")

        widget = launcher()
        widget.show()

        sys.exit(app.exec())
