from PySide6.QtWidgets import ( 
    QApplication, 
    QMainWindow, 
    QLabel, 
    QDialog, 
    QWidget
)
from PySide6.QtGui import ( 
    QPalette, 
    QPixmap, 
    QBrush
)
from PySide6.QtCore import ( 
    qVersion, 
)

from lce_qt_launcher.app_context import AppContext

import lce_qt_launcher.term_service as term_service
import lce_qt_launcher.features as features

import sys

class Launcher(QMainWindow):
    def __init__(self, appContext : AppContext, launcher_ui : object, sys_dialog_ui: object, instance_ui_editor: object, app : QApplication, parent=None) -> None:
        super().__init__(parent)

        translator = appContext.translator

        instanceManager = appContext.instanceMan

        buildInfo = appContext.buildInfo

        STARTING_GAME_MSG = translator.translate("start_game_msg")

        def gen_inst_from_form():
            instanceManager.instance = features.new_instance_from_form(self)

        def confirm_changes_button():
            gen_inst_from_form(self)

        def update_page():
            features.show_webbrowser(self, buildInfo.git_repo_url, buildInfo)

        def launch():
            features.launch_game(instanceManager, STARTING_GAME_MSG)

        def install():
            features.install_game(self, instanceManager.instance, instanceManager)

        def show_aboutQt() -> None:
            features.show_about_qt(self)

        def show_about() -> None:
            features.show_about_app(self, buildInfo, appContext.ICON)

        def show_system_information() -> None:
            features.show_system_info(self)

        def show_about_minecraft() -> None:
            features.show_webbrowser(self, appContext.MINECRAFT_WEBSITE, buildInfo)

        def show_more_lce_projects() -> None:
            features.show_webbrowser(self, appContext.MINECRAFT_LCE_WEBSITE, buildInfo)

        def save_instance() -> None:
            features.save_instance(self, instanceManager, buildInfo)

        def load_instance() -> None:
            features.load_instance(self, instanceManager, buildInfo)

        def show_setting_dialog() -> None:
            features.show_setting(self)

        def show_instance_editor() -> None:
            features.show_instance_editor(self)

        background_pixmap = QPixmap(appContext.BACKGROUND_PIXMAP_IMG)
        if not background_pixmap.isNull():
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(background_pixmap))
            self.setPalette(palette)
            self.setAutoFillBackground(True)
        else:
            term_service.print_error("Cannot set the background")

        self.ui = launcher_ui()

        self.ui.setupUi(self)
        
        self.sysinfo_dialog = QDialog() 
        self.dialog_ui = sys_dialog_ui()
        self.dialog_ui.setupUi(self.sysinfo_dialog)

        self.instance_window = QMainWindow()
        self.instance_editor = instance_ui_editor()
        self.instance_editor.setupUi(self.instance_window)

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

        _ = self.ui.playButton.clicked.connect(launch)
        _ = self.ui.installButton.clicked.connect(install)
        _ = self.ui.confirmChangesButton.clicked.connect(confirm_changes_button)
        _ = self.ui.settingButton.clicked.connect(show_setting_dialog)
        _ = self.ui.openInstanceEditor.clicked.connect(show_instance_editor)

        _ = self.ui.actionQuit.triggered.connect(app.quit)
        _ = self.ui.actionUpdate.triggered.connect(update_page)
        _ = self.ui.actionSystem_Information.triggered.connect(show_system_information)
        _ = self.ui.actionAbout.triggered.connect(show_about)
        _ = self.ui.actionAbout_QT.triggered.connect(show_aboutQt)
        _ = self.ui.actionAbout_Minecraft.triggered.connect(show_about_minecraft)
        _ = self.ui.actionMore_Minecraft_LCE_Projects.triggered.connect(show_more_lce_projects)
        _ = self.ui.actionSave.triggered.connect(save_instance)
        _ = self.ui.actionImport_Instance.triggered.connect(load_instance)

        self.versionlabel = QLabel(f"Version {buildInfo.version}")
        self.ui.statusbar.addPermanentWidget(self.versionlabel)