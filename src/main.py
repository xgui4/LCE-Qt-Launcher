#!/usr/bin/env python3

# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --windows-icon-from-ico=assets/app.ico
# nuitka-project: --product-name=LCE-Qt-Launcher
# nuitka-project: --include-data-dir=assets=assets
# nuitka-project: --include-qt-plugins=sensible
# nuitka-project: --windows-console-mode=force
# nuitka-project: --product-version="0.26.3.2"
# nuitka-project: --file-version="0.26.3.2"
# nuitka-project: --file-description="Custom Free/Libre Minecraft LCE Launcher (Nightly)"
# nuitka-project: --copyright="Copyleft Xgui4 2026 (GPLv3)"

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QDialog, QMessageBox, QFileDialog, QWidget
from PySide6.QtGui import QPalette, QPixmap, QBrush
from PySide6.QtCore import qVersion, QFile, QIODevice

from lce_qt_launcher.user_pref import UserPref
from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.managers.instance_manager import InstanceManager, Instance
from lce_qt_launcher.cmd_arg import CmdArgAction, parse_args, argsDetected
from lce_qt_launcher.gui.theme import Theme
from lce_qt_launcher.json_trans import JsonTrans

import lce_qt_launcher.term_service as term_service
import lce_qt_launcher.features as features
import lce_qt_launcher.utils as utils

import platform
import sys
import os

userPref = UserPref()
buildInfo = BuildInfo()

translator = JsonTrans()

defaultInstance = Instance()
instanceManager = InstanceManager(defaultInstance, buildInfo)

BACKGROUND_PIXMAP_IMG = ":/assets/background.png"
ICON = ":/assets/launcher_small.png"
MINECRAFT_WEBSITE = "https://minecraft.net"
MINECRAFT_LCE_WEBSITE = "https://minecraftlegacy.com/"

theme : Theme = Theme.MINECRAFT

if platform.system() == "Linux": 
    _LINUX_QT6_PATH = "/usr/lib/qt6/plugins"
    os.environ["QT_PLUGIN_PATH"] = _LINUX_QT6_PATH

if platform.system() == "FreeBSD": 
   _FREEBSD_QT6_PATH = "/usr/local/lib/qt6/plugins"
   os.environ["QT_PLUGIN_PATH"] = _FREEBSD_QT6_PATH

os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"

PLAY_BUTTON_LABEL = "play"

HELP_STR = "help-message"

ABOUT_STR = "about-message"

INSTANCE_MANAGER_LABEL = translator.translate("instance_manager_label")
SAVE_INSTANCE_MSG_BOX_LABEL = translator.translate("save_instance_msg_box_label")
STARTING_GAME_MSG = translator.translate("start_game_msg")

SAVE_FILEDIALOG_TITLE = "save_filedialog_title"

QUESTIONS_OPTIONS = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No

from ui_form import Ui_launcher
from ui_system_info import Ui_sys_info_dialog

def gen_inst_from_form(parent : QWidget):
    instanceManager.instance = features.new_instance_from_form(parent)

def about_to_quit_event():
    anwser = QMessageBox.question(None, INSTANCE_MANAGER_LABEL, SAVE_INSTANCE_MSG_BOX_LABEL, QUESTIONS_OPTIONS)
    if anwser == QMessageBox.StandardButton.Yes:
        file_name: str = QFileDialog.getSaveFileName(None, SAVE_FILEDIALOG_TITLE, f"{buildInfo.system_manager.found_default_save_path }(\"LCE Instance Save File\" (*{buildInfo.instance_extension}))")[0]
        instanceManager.save_instance(file_name)

class launcher(QMainWindow):
    def confirm_changes_button(self):
        gen_inst_from_form(self)

    def update_page(self):
        features.show_webbrowser(self, buildInfo.git_repo_url, buildInfo)

    def launch(self):
        features.launch_game(instanceManager, STARTING_GAME_MSG)

    def install(self):
        features.install_game(self, defaultInstance, instanceManager)

    def show_aboutQt(self) -> None:
        features.show_about_qt(self)

    def show_about(self) -> None:
        features.show_about_app(self, buildInfo, ICON)

    def show_system_information(self) -> None:
        features.show_system_info(self)

    def show_about_minecraft(self) -> None:
        features.show_webbrowser(self, MINECRAFT_WEBSITE, buildInfo)

    def show_more_lce_projects(self) -> None:
        features.show_webbrowser(self, MINECRAFT_LCE_WEBSITE, buildInfo)

    def save_instance(self) -> None:
        features.save_instance(self, instanceManager, buildInfo)

    def load_instance(self) -> None:
        features.load_instance(self, instanceManager, buildInfo)

    def show_setting_dialog(self) -> None:
        features.show_setting(self)

    def __init__(self, parent=None) -> None:
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

        _ = self.ui.playButton.clicked.connect(self.launch)
        _ = self.ui.installButton.clicked.connect(self.install)
        _ = self.ui.confirmChangesButton.clicked.connect(self.confirm_changes_button)
        _ = self.ui.settingButton.clicked.connect(self.show_setting_dialog)

        _ = self.ui.actionQuit.triggered.connect(app.quit)
        _ = self.ui.actionUpdate.triggered.connect(self.update_page)
        _ = self.ui.actionSystem_Information.triggered.connect(self.show_system_information)
        _ = self.ui.actionAbout.triggered.connect(self.show_about)
        _ = self.ui.actionAbout_QT.triggered.connect(self.show_aboutQt)
        _ = self.ui.actionAbout_Minecraft.triggered.connect(self.show_about_minecraft)
        _ = self.ui.actionMore_Minecraft_LCE_Projects.triggered.connect(self.show_more_lce_projects)
        _ = self.ui.actionSave.triggered.connect(self.save_instance)
        _ = self.ui.actionImport_Instance.triggered.connect(self.load_instance)

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
            features.display_help(translator.translate(HELP_STR))
        if action == CmdArgAction.PRINT_ABOUT_INFO:
            features.display_about(translator.translate("about_message"))
        if action == CmdArgAction.PRINT_VERSION: 
            features.display_version(buildInfo)
        if action == CmdArgAction.CLI_VERSION:
            features.launch_cli_interface(instanceManager)
        else:
            term_service.print_information("Not Implemented Yet!")
    else:
        app = QApplication(sys.argv)

        _ = app.setStyle("Fusion")

        widget = launcher()
        widget.show()

        if os.name == "nt":
            os.environ["QT_QPA_PLATFORM"] = "windows:darkmode=2"
        try:
            theme_file : str = theme.value
            file = QFile(theme_file)
            if file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
                content = file.readAll()
                stylesheet = str(content, encoding='utf-8')  # pyright: ignore[reportArgumentType]
                app.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(FileNotFoundError.with_traceback)
            term_service.print_warning("Theme ({theme}) not found in ressource, searching in the local storage.")
            try: 
                with open(os.path.join(utils.get_assets_dir(), "styles", "minecraft.qss"), "r") as file:
                    app.setStyleSheet(file.read())
            except FileNotFoundError:
                _ = QMessageBox.warning(None,"Error", f"{theme} file not found. Reverting to default theme")

        sys.exit(app.exec())