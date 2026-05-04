import os

from PySide6.QtWidgets import ( 
    QApplication,
    QFileDialog, 
    QMainWindow, 
    QLabel, 
    QDialog,
    QListWidgetItem
)
from PySide6.QtGui import ( 
    QPalette, 
    QPixmap,
    QBrush
)
from PySide6.QtCore import ( 
    qVersion,
    Qt
)

import sys
import platform
import json
import webbrowser

from pathlib import Path

from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.app_context import AppContext
from lce_qt_launcher.managers.instance_manager import Instance, InstanceManager
from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.models.app_data import AppData
from lce_qt_launcher.views.content_installer_dialog import ContentInstallerView
from lce_qt_launcher.ui_about import Ui_AboutDialog
from lce_qt_launcher.ui_instance import Ui_InstancesEditor
from lce_qt_launcher.ui_settingDialog import Ui_settingDialog
from lce_qt_launcher.ui_system_info import Ui_sys_info_dialog
from lce_qt_launcher.utils.json_trans import JsonTrans
from lce_qt_launcher.ui_form import Ui_launcher

import lce_qt_launcher.views.term_service as term_service
import lce_qt_launcher.features as features
import lce_qt_launcher.utils.holiday as holiday

class Launcher(QMainWindow):
    """_summary_ The Main Window / playButtonCommander of the QApplcation

    Args:
        QMainWindow (_type_): _description_ The inheite type of playButtonCommander
    """
    def __init__(self, 
                 appContext : AppContext, 
                 appData : AppData, 
                 app : QApplication,
                ) -> None:
        super().__init__(None)

        translator: JsonTrans = appContext.translator
        instanceManager: InstanceManager = appContext.instanceMan
        buildInfo: BuildInfo = appContext.buildInfo

        self.image_label: str = instanceManager.instance.image
        self.news_feed: str = instanceManager.instance.news_feed
        self.instance_name: str = instanceManager.instance.name

        self.instances : list[Instance] = list()

        STARTING_GAME_MSG = translator.translate("start_game_msg")

        def generateInstanceFromForm() -> None:
            """
            _sumarry_ Generate An Instance From the Form
            """
            instanceManager.instance = features.new_instance_from_form(self)

        def confirmChangesButtonCommand() -> None:
            """_summary_ Generate An Instance From the Form for confirming the changes
            """
            generateInstanceFromForm()

        def playButtonCommand() -> None:
            """_summary_ playButtonCommand the Game
            """
            features.launch_game(instanceManager, STARTING_GAME_MSG)

        def installButtonCommand() -> None:
            """_summary_ Install the Game
            """
            features.install_game(self, instanceManager.instance, instanceManager)

        def showSettingDialogCommand() -> None:
            """_summary_ Show the setting Dialog
            """
            features.show_setting(self, Ui_settingDialog())

        def saveInstanceButtonCommand() -> None:
            """_summary_ Save the instance on a file on disk
            """
            features.save_instance_to_file(self, instanceManager, appContext, buildInfo)

        def changeInstanceIconButtonCommand() -> None:
            file_name: str = QFileDialog.getOpenFileName(
                self, 
                "Select the image file for the instance", 
                appContext.sys_man.found_default_save_path(), 
                f"{buildInfo.app_name} Instance File (*{buildInfo.instance_extension})")[0]
            instanceManager.instance.image = file_name
            self.ui.instance_img.setPixmap(QPixmap(file_name))

        def showInstanceEditorButtonCommand() -> None:
            features.show_instance_editor(self)

        def showAboutMinecraftActionCommand() -> None:
            """_summary_ Open an QWebEngine at the Minecraft Website 
            """
            features.show_webbrowser(self, appContext.MINECRAFT_WEBSITE, buildInfo)

        def showMoreLCEProjectsActionCommand() -> None:
            """_summary_ Open An QWebEngine at the Minecraft LCE collection website (not by me)
            """
            features.show_webbrowser(self, appContext.MINECRAFT_LCE_WEBSITE, buildInfo)      

        def updateActionCommand() -> None:
            """_summary_ "Show the Update Page in a QWebEngine Popup
            """
            features.show_webbrowser(self, buildInfo.git_repo_url, buildInfo)
        
        def loadInstanceActionCommand() -> None:
            """_summary_ Open the Load Save File Dialog 
            """
            features.load_instance(self, instanceManager, appContext, buildInfo, appData)
            self.ui.instanceNameLabel.setText(instanceManager.instance.name)
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

        def showSystemInformationActionCommand() -> None:
            """_summary_ Show the system info dialog
            """
            features.show_system_info(self)

        def showAboutQtActionCommand() -> None:
            """_summary_ Show the About Qt Dialog
            """
            features.show_about_qt(self)

        def showAboutActionCommand() -> None:
            """_summary_ Show About App dialog 
            """ 
            features.show_about_app(self)

        def installContentActionCommand() -> None:
            ContentInstallerView()

        background_pixmap = QPixmap(appContext.BACKGROUND_PIXMAP_IMG)
        if not background_pixmap.isNull():
            palette: QPalette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(background_pixmap))
            self.setPalette(palette)
            self.setAutoFillBackground(True)
        else:
            term_service.print_error("Cannot set the background")
            
        self.ui: Ui_launcher = Ui_launcher()

        self.ui.setupUi(self)
        
        arguments: list[str] =  QApplication.instance().arguments() if not None else "Error"  # pyright: ignore[reportOptionalMemberAccess]

        for inst in appData.instsList:
            self.instances.append(inst)
            item =  QListWidgetItem()
            item.setText(inst.name)
            item.setIcon(QPixmap(inst.image))
            item.setData(Qt.ItemDataRole.FileInfoRole, inst)
            self.ui.listWidget.addItem(item)
        
        if len(arguments) > 1:
            file_arg: str = arguments[1]
            
            try:
                path = Path(file_arg)
                if path.is_file():
                    with path.open("r", encoding="utf-8") as instance:
                        inst_dict: dict[str, str] = json.load(instance)   # pyright: ignore[reportAny]
                        instanceManager.instance.load_inst_from_dict(inst_dict)
                        instanceManager.instance.display()
                        self.ui.instanceNameLabel.setText(instanceManager.instance.name)
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
                else:
                    term_service.print_information("No file argument given or file not found. Loading default instance.")
            except json.JSONDecodeError as err:
                term_service.print_error(f"Invalid or corrupted Save File (JSON syntax) : {err.msg} at line {err.lineno}") 
            except (ValueError, TypeError) as err:
                term_service.print_error(f"Data structure error in Save File : {err}") 
            except PermissionError:
                term_service.print_error("System Error : Permission denied when reading the file.") 
            except RecursionError:
                term_service.print_error("System Error : The JSON structure is too deep to be processed.")
            except Exception as err:
                term_service.print_error(f"An unexpected error occurred : {err}")
        else:
            term_service.print_information("No argument given, start with default instance.")
        
        self.about: Ui_AboutDialog = Ui_AboutDialog()
        self.aboutDialog: QDialog = QDialog()

        self.sysinfo_dialog: QDialog = QDialog() 
        self.dialog_ui = Ui_sys_info_dialog()
        self.dialog_ui.setupUi(self.sysinfo_dialog)
        self.about.setupUi(self.aboutDialog)
        self.aboutDialog.setWindowTitle(appContext.buildInfo.app_name)

        self.about.title.setText(appContext.buildInfo.app_name)
        self.about.versionLabel.setText(f"{appContext.buildInfo.version}")
        self.about.urlLabel.setText(appContext.buildInfo.git_repo_url)
        self.about.creditsText.setText("Xgui4")
        self.about.copyLabel.setText("Copyleft (C) GPLv3 Xgui4")
        self.about.channelLabel.setText(f"Channel : {appContext.buildInfo.version_type}")
        self.about.platformLabel.setText(f"Platform : {platform.release()}")
        from lce_qt_launcher import license_str
        self.about.licenseText.setMarkdown(license_str)
        _ = self.about.aboutQt.clicked.connect(showAboutQtActionCommand)
        _ = self.about.closeButton.clicked.connect(self.aboutDialog.close)

        self.instance_window: QDialog = QDialog()
        self.instance_editor: Ui_InstancesEditor = Ui_InstancesEditor()
        self.instance_editor.setupUi(self.instance_window)
        self.instance_window.setWindowTitle(appContext.buildInfo.app_name)

        systemManager: SystemManager = appContext.sys_man

        self.dialog_ui.appVersion.setText(f"{buildInfo.app_name} Version {buildInfo.version_type} {buildInfo.version}")
        self.dialog_ui.qVersionLabel.setText(f"Qt Version {qVersion()}")
        self.dialog_ui.pyVersionLabel.setText(f"Python Version : {sys.version}")
        self.dialog_ui.osInfoLabel.setText(f"OS : {systemManager.name} \n Version : {systemManager.version}")
        self.dialog_ui.pluginsInfoLabel.setText("")
        self.dialog_ui.runnersLabel.setText("")

        self.ui.progressLabel.setVisible(False)
        self.ui.progressBar.setVisible(False)
        self.ui.progressBar.setEnabled(False)

        _ = self.ui.playButton.clicked.connect(playButtonCommand)
        _ = self.ui.installButton.clicked.connect(installButtonCommand)
        _ = self.ui.settingButton.clicked.connect(showSettingDialogCommand)
        _ = self.ui.savetInstanceButton.clicked.connect(saveInstanceButtonCommand)
        _ = self.ui.confirmChangesButton.clicked.connect(confirmChangesButtonCommand)
        _ = self.ui.openInstanceEditor.clicked.connect(showInstanceEditorButtonCommand)
        _ = self.ui.changeInstanceIconButton.clicked.connect(changeInstanceIconButtonCommand)

        _ = self.ui.actionSetting.triggered.connect(showSettingDialogCommand)
        _ = self.ui.actionSetting_2.triggered.connect(showSettingDialogCommand)
        _ = self.ui.actionSetting_3.triggered.connect(showSettingDialogCommand)
        _ = self.ui.actionQuit.triggered.connect(app.quit)
        _ = self.ui.actionUpdate.triggered.connect(updateActionCommand)
        _ = self.ui.actionSystem_Information.triggered.connect(showSystemInformationActionCommand)
        _ = self.ui.actionAbout.triggered.connect(showAboutActionCommand)
        _ = self.ui.actionAbout_QT.triggered.connect(showAboutQtActionCommand)
        _ = self.ui.actionAbout_Minecraft.triggered.connect(showAboutMinecraftActionCommand)
        _ = self.ui.actionMore_Minecraft_LCE_Projects.triggered.connect(showMoreLCEProjectsActionCommand)
        _ = self.ui.actionSave.triggered.connect(saveInstanceButtonCommand)
        _ = self.ui.actionImport_Instance.triggered.connect(loadInstanceActionCommand)
        _ = self.ui.actionInstall_Content.triggered.connect(installContentActionCommand)

        openAppInstancesData = lambda : systemManager.open_url_with_system(os.path.join(appData.appDataDirs[0], "instances"))
        _ = self.ui.actionInstances.triggered.connect(openAppInstancesData)

        open_workshop = lambda : features.show_webbrowser(self, "https://lce-hub.github.io/piston/", buildInfo); 
        _ = self.ui.actionLCE_Hub_Workshop.triggered.connect(open_workshop)

        open_legacymods = lambda : features.show_webbrowser(self, "https://legacymods.org/", buildInfo); 
        _ = self.ui.actionLegacyMods_Coming_Soon.triggered.connect(open_legacymods)

        openAppRoot = lambda : systemManager.open_url_with_system(appData.projectRootDir);
        _= self.ui.actionApp_Root.triggered.connect(openAppRoot)

        openAppConfig = lambda : systemManager.open_url_with_system(appData.appConfigDir);
        _= self.ui.actionApp_Root.triggered.connect(openAppConfig)

        open_github_issues = lambda : webbrowser.open(appContext.buildInfo.git_repo_url + "/issues")
        _ = self.ui.actionReport_a_Bugs_or_Sugess_a_feature.triggered.connect(open_github_issues)

        self.versionlabel: QLabel = QLabel(f"Version {buildInfo.version}")
        self.ui.statusbar.addPermanentWidget(self.versionlabel)
        holyday_label: QLabel = QLabel(holiday.get_holiday())
        self.ui.statusbar.addWidget(holyday_label)