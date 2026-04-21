from PySide6.QtWidgets import ( 
    QApplication, 
    QMainWindow, 
    QLabel, 
    QDialog
)
from PySide6.QtGui import ( 
    QPalette, 
    QPixmap, 
    QBrush
)
from PySide6.QtCore import ( 
    qVersion
)

from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.app_context import AppContext
from lce_qt_launcher.managers.instance_manager import InstanceManager
from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.ui_about import Ui_AboutDialog
from lce_qt_launcher.ui_instance import Ui_InstancesEditor
from lce_qt_launcher.ui_settingDialog import Ui_settingDialog
from lce_qt_launcher.ui_system_info import Ui_sys_info_dialog
from lce_qt_launcher.utils.json_trans import JsonTrans
from lce_qt_launcher.ui_form import Ui_launcher

import lce_qt_launcher.views.term_service as term_service
import lce_qt_launcher.features as features
import lce_qt_launcher.utils.holyday as holyday

import sys
import platform

class Launcher(QMainWindow):
    def __init__(self, 
                 appContext : AppContext, 
                 app : QApplication, 
                 parent=None) -> None:
        super().__init__(parent)

        translator: JsonTrans = appContext.translator
        instanceManager: InstanceManager = appContext.instanceMan
        buildInfo: BuildInfo = appContext.buildInfo

        self.image_label: str = instanceManager.instance.image
        self.news_feed: str = instanceManager.instance.news_feed
        self.instance_name: str = instanceManager.instance.name

        STARTING_GAME_MSG = translator.translate("start_game_msg")

        def gen_inst_from_form() -> None:
            instanceManager.instance = features.new_instance_from_form(self)

        def confirm_changes_button() -> None:
            gen_inst_from_form()

        def update_page() -> None:
            features.show_webbrowser(self, buildInfo.git_repo_url, buildInfo)

        def launch() -> None:
            features.launch_game(instanceManager, STARTING_GAME_MSG)

        def install() -> None:
            features.install_game(self, instanceManager.instance, instanceManager)

        def show_aboutQt() -> None:
            features.show_about_qt(self)

        def show_about() -> None:
            features.show_about_app(self)

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
            self.image_label = instanceManager.instance.image
            self.news_feed = instanceManager.instance.news_feed
            self.instance_name = instanceManager.instance.name
            self.ui.usernameInputBox.setText(instanceManager.instance.username)
            self.ui.pathInputBox.setText(instanceManager.instance.installation_path)
            self.ui.repoURLInputBox.setText(instanceManager.instance.repo_url)
            pixmap = QPixmap(self.image_label)
            self.ui.instance_img.setPixmap(pixmap)
            self.ui.repo_name_branch.setText(self.instance_name)
            self.ui.newsEngineView.setUrl(self.news_feed)

        def show_setting_dialog() -> None:
            features.show_setting(self, Ui_settingDialog())

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

        self.ui: Ui_launcher = Ui_launcher()

        self.ui.setupUi(self)
        
        self.about: Ui_AboutDialog = Ui_AboutDialog()
        self.aboutDialog: QDialog = QDialog()

        self.sysinfo_dialog: QDialog = QDialog() 
        self.dialog_ui: Ui_sys_info_dialog = Ui_sys_info_dialog()
        self.dialog_ui.setupUi(self.sysinfo_dialog)
        self.about.setupUi(self.aboutDialog)

        app_icon = QPixmap(":/assets/launcher.png");
        self.about.icon.setPixmap(app_icon)
        self.about.title.setText(appContext.buildInfo.app_name)
        self.about.versionLabel.setText(f"{appContext.buildInfo.version}")
        self.about.urlLabel.setText(appContext.buildInfo.git_repo_url)
        self.about.creditsText.setText("Xgui4")
        self.about.copyLabel.setText("Copyleft (C) GPLv3 Xgui4")
        self.about.commitLabel.setText(f"Commit : UNKOWMN")
        self.about.buildDateLabel.setText(f"Build date : UNKOWN")
        self.about.channelLabel.setText(f"Channel : {appContext.buildInfo.version_type}")
        self.about.platformLabel.setText(f"Platform : {platform.release()}")
        from lce_qt_launcher import license_str
        self.about.licenseText.setMarkdown(license_str)
        _ = self.about.aboutQt.clicked.connect(show_aboutQt)
        _ = self.about.closeButton.clicked.connect(self.aboutDialog.close)

        window_title: str = translator.translate(appContext.buildInfo.app_name)

        self.instance_window: QDialog = QDialog()
        self.instance_editor: Ui_InstancesEditor = Ui_InstancesEditor()
        self.instance_editor.setupUi(self.instance_window)
        self.instance_window.setWindowTitle(window_title)

        systemManager: SystemManager = buildInfo.system_manager

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
        _ = self.ui.settingButton.clicked.connect(show_setting_dialog)
        _ = self.ui.savetInstanceButton.clicked.connect(save_instance)
        _ = self.ui.confirmChangesButton.clicked.connect(confirm_changes_button)
        _ = self.ui.openInstanceEditor.clicked.connect(show_instance_editor)

        _ = self.ui.actionSetting.triggered.connect(show_setting_dialog)
        _ = self.ui.actionSetting_2.triggered.connect(show_setting_dialog)
        _ = self.ui.actionSetting_3.triggered.connect(show_setting_dialog)
        _ = self.ui.actionQuit.triggered.connect(app.quit)
        _ = self.ui.actionUpdate.triggered.connect(update_page)
        _ = self.ui.actionSystem_Information.triggered.connect(show_system_information)
        _ = self.ui.actionAbout.triggered.connect(show_about)
        _ = self.ui.actionAbout_QT.triggered.connect(show_aboutQt)
        _ = self.ui.actionAbout_Minecraft.triggered.connect(show_about_minecraft)
        _ = self.ui.actionMore_Minecraft_LCE_Projects.triggered.connect(show_more_lce_projects)
        _ = self.ui.actionSave.triggered.connect(save_instance)
        _ = self.ui.actionImport_Instance.triggered.connect(load_instance)

        self.versionlabel: QLabel = QLabel(f"Version {buildInfo.version}")
        self.ui.statusbar.addPermanentWidget(self.versionlabel)
        holyday_label: QLabel = QLabel(holyday.get_holyday())
        self.ui.statusbar.addWidget(holyday_label)