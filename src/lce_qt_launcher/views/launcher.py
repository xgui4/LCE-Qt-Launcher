from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QLabel,
    QDialog,
    QListWidgetItem,
    QInputDialog,
    QMessageBox,
)

from PySide6.QtGui import QPalette, QPixmap, QBrush

from PySide6.QtCore import qVersion, Qt, QFile, QIODevice

from PySide6.QtWebEngineCore import (
    QWebEnginePage,
    QWebEngineProfile,
    QWebEngineDownloadRequest,
)

import sys
import platform
import json
import webbrowser
import os
import subprocess

from pathlib import Path

from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.app_context import AppContext
from lce_qt_launcher.managers.instance_manager import Instance, InstanceManager
from lce_qt_launcher.models.app_data import AppData
from lce_qt_launcher.views.content_installer_dialog import ContentInstallerView
from lce_qt_launcher.ui_about import Ui_AboutDialog
from lce_qt_launcher.ui_instance import Ui_InstancesEditor
from lce_qt_launcher.ui_settingDialog import Ui_settingDialog
from lce_qt_launcher.ui_system_info import Ui_sys_info_dialog
from lce_qt_launcher.utils.json_trans import JsonTrans
from lce_qt_launcher.ui_form import Ui_launcher
from lce_qt_launcher.managers.steam_manager import add_instance_to_steam
from lce_qt_launcher import (
    app_name_str,
    version_str,
    license_text_str,
    version_type_str,
    git_repo_url_str,
    instance_extension_str
)

import lce_qt_launcher.views.term_service as term_service
import lce_qt_launcher.features as features
import lce_qt_launcher.utils.holiday as holiday


class LauncherView(QMainWindow):
    """_summary_ The Main Window / launcher of the QApplcation

    Args:
        QMainWindow (_type_): _description_ Inherited/is a QMainWindow
    """

    def __init__(
        self,
        appContext: AppContext,
        appData: AppData,
        app: QApplication,
    ) -> None:
        super().__init__(None)

        translator: JsonTrans = appContext.translator
        instanceManager: InstanceManager = appContext.instanceMan

        self.image_label: str = instanceManager.instance.image
        self.news_feed: str = instanceManager.instance.news_feed
        self.instance_name: str = instanceManager.instance.name
        self.instances: list[Instance] = list[Instance]()

        STARTING_GAME_MSG: str = translator.translate("start_game_msg")

        def generateInstanceFromForm() -> None:
            """
            _sumarry_ Generate An Instance From the Form
            """
            instanceManager.instance = features.new_instance_from_form(self)

        def confirmChangesButtonCommand() -> None:
            """_summary_ Generate An Instance From the Form for confirming the changes"""
            generateInstanceFromForm()

        def playButtonCommand() -> None:
            """_summary_ playButtonCommand the Game"""
            features.launch_game(instanceManager, STARTING_GAME_MSG)

        def installButtonCommand() -> None:
            """_summary_ Install the Game"""
            features.install_game(self, instanceManager.instance, instanceManager)

        def showSettingDialogCommand() -> None:
            """_summary_ Show the setting Dialog"""
            features.show_setting(self, Ui_settingDialog(), appContext)

        def saveInstanceButtonCommand() -> None:
            """_summary_ Save the instance on a file on disk"""
            features.save_instance_to_file(self, instanceManager, appContext)

        def changeInstanceIconButtonCommand() -> None:
            """_summary_ Open the instance icon/image interface"""
            file_name: str = QFileDialog.getOpenFileName(
                self,
                "Select the image file for the instance",
                appContext.sys_man.found_default_save_path(),
                f"{app_name_str} Instance File (*{instance_extension_str})",
            )[0]
            instanceManager.instance.image = file_name
            self.ui.instance_img.setPixmap(QPixmap(file_name))

        def showInstanceEditorButtonCommand() -> None:
            """_summary_ Open the instance editor button command"""
            features.show_instance_editor(self)

        def showAboutMinecraftActionCommand() -> None:
            """_summary_ Open an QWebEngine at the Minecraft Website"""
            features.show_webbrowser(self, appContext.MINECRAFT_WEBSITE)

        def showMoreLCEProjectsActionCommand() -> None:
            """_summary_ Open An QWebEngine at the Minecraft LCE collection website (not by me)"""
            features.show_webbrowser(self, appContext.MINECRAFT_LCE_WEBSITE)

        def updateActionCommand() -> None:
            """_summary_ "Show the Update Page in a QWebEngine Popup"""
            features.show_webbrowser(self, git_repo_url_str)

        def loadInstanceActionCommand() -> None:
            """_summary_ Open the Load Save File Dialog"""
            features.load_instance_from_file(self, instanceManager, appContext, appData)
            self.loadInstanceInForm(instanceManager)

        def showSystemInformationActionCommand() -> None:
            """_summary_ Show the system info dialog"""
            features.show_system_info(self)

        def showAboutQtActionCommand() -> None:
            """_summary_ Show the About Qt Dialog"""
            features.show_about_qt(self)

        def showAboutActionCommand() -> None:
            """_summary_ Show About App dialog"""
            features.show_about_app(self)

        def installContentActionCommand() -> None:
            """_summary_ Open the Content Installer Window"""
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
        for inst in appData.instsList:
            self.instances.append(inst)
            item = QListWidgetItem()
            item.setText(inst.name)
            item.setIcon(QPixmap(inst.image))
            item.setData(Qt.ItemDataRole.FileInfoRole, inst)
            self.ui.listWidget.addItem(item)

        arguments: list[str] = (
            QApplication.instance().arguments() if not None else "Error"  # pyright: ignore[reportOptionalMemberAccess]
        )
        if len(arguments) > 1:
            file_arg: str = arguments[1]
            try:
                path = Path(file_arg)
                if path.is_file():
                    with path.open("r", encoding="utf-8") as instance:
                        inst_dict: dict[str, str] = json.load(instance)
                        instanceManager.instance.load_inst_from_dict(inst_dict)
                        instanceManager.instance.display()
                else:
                    term_service.print_information(
                        "No file argument given or file not found. Loading default instance."
                    )
            except json.JSONDecodeError as err:
                term_service.print_error(
                    f"Invalid or corrupted Save File (JSON syntax) : {err.msg} at line {err.lineno}"
                )
            except (ValueError, TypeError) as err:
                term_service.print_error(f"Data structure error in Save File : {err}")
            except PermissionError:
                term_service.print_error(
                    "System Error : Permission denied when reading the file."
                )
            except RecursionError:
                term_service.print_error(
                    "System Error : The JSON structure is too deep to be processed."
                )
            except Exception as err:
                term_service.print_error(f"An unexpected error occurred : {err}")
        else:
            term_service.print_information(
                "No argument given, start with default instance."
            )

        self.sysinfo_dialog: QDialog = QDialog()
        self.dialog_ui: Ui_sys_info_dialog = Ui_sys_info_dialog()
        self.dialog_ui.setupUi(self.sysinfo_dialog)

        self.about: Ui_AboutDialog = Ui_AboutDialog()
        self.aboutDialog: QDialog = QDialog()

        self.about.setupUi(self.aboutDialog)

        self.about.title.setText(app_name_str)
        self.about.versionLabel.setText(f"{version_str}")
        self.about.urlLabel.setText(git_repo_url_str)
        self.about.creditsText.setText("Xgui4")
        self.about.copyLabel.setText("Copyleft (C) GPLv3 Xgui4")
        self.about.channelLabel.setText(f"**Channel** : {version_type_str}")
        self.about.platformLabel.setText(f"**Platform** : {platform.release()}")

        self.about.licenseText.setMarkdown(license_text_str)
        self.about.aboutQt.clicked.connect(showAboutQtActionCommand)
        self.about.closeButton.clicked.connect(self.aboutDialog.close)

        self.instance_window: QDialog = QDialog()
        self.instance_editor: Ui_InstancesEditor = Ui_InstancesEditor()
        self.instance_editor.setupUi(self.instance_window)
        self.instance_window.setWindowTitle(app_name_str)

        systemManager: SystemManager = appContext.sys_man

        self.dialog_ui.appVersionLabel.setText(
            f"**App Version** : {app_name_str} {version_type_str} {version_str}"
        )
        self.dialog_ui.qVersionLabel.setText(f"**Qt Version** : {qVersion()}")
        self.dialog_ui.pyVersionLabel.setText(f"**Python Version** : {sys.version}")
        self.dialog_ui.osInfoLabel.setText(
            f"**System Name** : {systemManager.name} \n**System Version** : {systemManager.version}"
        )
        self.dialog_ui.pluginsInfoLabel.setText("")
        self.dialog_ui.runnersLabel.setText("")

        self.ui.progressLabel.setVisible(False)
        self.ui.progressBar.setVisible(False)
        self.ui.progressBar.setEnabled(False)

        self.ui.playButton.clicked.connect(playButtonCommand)
        self.ui.installButton.clicked.connect(installButtonCommand)
        self.ui.settingButton.clicked.connect(showSettingDialogCommand)
        self.ui.savetInstanceButton.clicked.connect(saveInstanceButtonCommand)
        self.ui.confirmChangesButton.clicked.connect(confirmChangesButtonCommand)
        self.ui.openInstanceEditor.clicked.connect(showInstanceEditorButtonCommand)
        self.ui.changeInstanceIconButton.clicked.connect(changeInstanceIconButtonCommand)

        self.ui.actionSetting.triggered.connect(showSettingDialogCommand)
        self.ui.actionSetting_2.triggered.connect(showSettingDialogCommand)
        self.ui.actionSetting_3.triggered.connect(showSettingDialogCommand)
        self.ui.actionQuit.triggered.connect(app.quit)
        self.ui.actionUpdate.triggered.connect(updateActionCommand)
        self.ui.actionSystem_Information.triggered.connect(showSystemInformationActionCommand)
        self.ui.actionAbout.triggered.connect(showAboutActionCommand)
        self.ui.actionAbout_QT.triggered.connect(showAboutQtActionCommand)
        self.ui.actionAbout_Minecraft.triggered.connect(showAboutMinecraftActionCommand)
        self.ui.actionMore_Minecraft_LCE_Projects.triggered.connect(showMoreLCEProjectsActionCommand)
        self.ui.actionSave.triggered.connect(saveInstanceButtonCommand)
        self.ui.actionImport_Instance.triggered.connect(loadInstanceActionCommand)
        self.ui.actionInstall_Content.triggered.connect(installContentActionCommand)

        def loadSteam():
            return subprocess.run(["steam", instanceManager.instance.steam_link])

        self.ui.playOnSteamButton.clicked.connect(loadSteam)

        def openAppInstancesData():
            return systemManager.open_url_with_system(
                os.path.join(appData.appDataDirs[0], "instances")
            )

        self.ui.actionInstances.triggered.connect(openAppInstancesData)

        def open_workshop():
            return features.show_webbrowser(self, "https://lce-hub.github.io/piston/")

        self.ui.actionLCE_Hub_Workshop.triggered.connect(open_workshop)

        def open_legacymods():
            return features.show_webbrowser(self, "https://legacymods.org/")

        self.ui.actionLegacyMods_Coming_Soon.triggered.connect(open_legacymods)

        def openAppRoot():
            return systemManager.open_url_with_system(appData.projectRootDir)

        self.ui.actionApp_Root.triggered.connect(openAppRoot)

        def openAppConfig():
            return systemManager.open_url_with_system(appData.appConfigDir)

        self.ui.actionApp_Root.triggered.connect(openAppConfig)

        def open_github_issues():
            return webbrowser.open(git_repo_url_str + "/issues")

        self.ui.actionReport_a_Bugs_or_Sugess_a_feature.triggered.connect(
            open_github_issues
        )

        def loadDefaultInstance():
            return self.loadInstanceCommand(dict(), instanceManager)

        self.ui.actionLoadDefaultInstance.triggered.connect(loadDefaultInstance)

        self.ui.actionLoadmclceInstance.setEnabled(False)
        self.ui.actionLoadmclceInstance.setText(
            "MCLCE Source Code Backup (Remote Git Not supported yet)"
        )

        mclceJson = QFile(":/instances/mclce.lce_inst")
        if not mclceJson.open(QIODevice.OpenModeFlag.ReadOnly):
            term_service.print_error("Cannot found or open MCLCE Instance")
            self.ui.actionLoadmclceInstance.setEnabled(False)
            return None
        else:
            raw_text_neo: str = bytes(mclceJson.readAll().data()).decode("utf-8")
            data_neo = json.loads(raw_text_neo)

            def loadNeoLegacyInstance():
                return self.loadInstanceCommand(data_neo, instanceManager)

            self.ui.actionLoadmclceInstance.triggered.connect(loadNeoLegacyInstance)

        revelationJson = QFile(":/instances/revelations.lce_inst")
        if not revelationJson.open(QIODevice.OpenModeFlag.ReadOnly):
            term_service.print_error("Cannot found or open revelations Instance")
            self.ui.actionLoadRevelationsInstance.setEnabled(False)
            return None
        else:
            raw_text_rev = bytes(revelationJson.readAll().data()).decode("utf-8")
            data_rev = json.loads(raw_text_rev)

            def loadRevelationInstance():
                return self.loadInstanceCommand(data_rev, instanceManager)

            self.ui.actionLoadRevelationsInstance.triggered.connect(
                loadRevelationInstance
            )

        aetherJson = QFile(":/instances/aether.lce_inst")
        if not aetherJson.open(QIODevice.OpenModeFlag.ReadOnly):
            term_service.print_error("Cannot found or open Aether Instance")
            self.ui.actionLoadAetherInstance.setEnabled(False)
            return None
        else:
            raw_text_aether = bytes(aetherJson.readAll().data()).decode("utf-8")
            data_aether = json.loads(raw_text_aether)

            def loadAetherInstance():
                return self.loadInstanceCommand(data_aether, instanceManager)

            self.ui.actionLoadAetherInstance.triggered.connect(loadAetherInstance)

        def addSteamLinkIntegrationButtonCommand():
            steamIntegrationDialog = QInputDialog(self)
            value = steamIntegrationDialog.getText(
                self, "Add Steam Integration", "steamid"
            )
            if value[1]:
                self.ui.steamLinkValue.setText(value[0])
                question = QMessageBox()
                answer = question.question(
                    self, "Add Instance to Steam Non-Steam Game Shortcuts ?", "Add "
                )
                if answer == QMessageBox.StandardButton.Yes:
                    full_extention_path: str = os.path.join(
                        instanceManager.instance.installation_path,
                        instanceManager.instance.exe_name,
                    )
                    add_instance_to_steam(
                        full_extention_path,
                        instanceManager.instance.name,
                        instanceManager.instance.image,
                    )
                instanceManager.instance.steam_link = value[0]

        self.ui.addSteamLinkIntegration.clicked.connect(
            addSteamLinkIntegrationButtonCommand
        )

        self.ui.InstancesList.setEnabled(False)

        self.setup_web_engine()

        self.versionlabel: QLabel = QLabel(f"Version {version_type_str} {version_str}")
        self.ui.statusbar.addPermanentWidget(self.versionlabel)

        if appContext.showHolidayEnabled:
            holyday_label: QLabel = QLabel(holiday.get_holiday())
            self.ui.statusbar.addWidget(holyday_label)

        self.loadInstanceInForm(instanceManager)

    def setup_web_engine(self):
        page: QWebEnginePage = self.ui.marketplacesWebsiteEngine.page()
        self.browser_profile: QWebEngineProfile = page.profile()
        self.browser_profile.downloadRequested.connect(self.handleDownloadCommand)

    def handleDownloadCommand(self, download: QWebEngineDownloadRequest):
        """Processes the PySide6 download stream request."""
        print("Download Started!")

        path_str, _ = QFileDialog.getSaveFileName(
            None, "Save File", download.downloadFileName()
        )

        if path_str:
            save_path: Path = Path(path_str)
            download.setDownloadDirectory(str(save_path.parent))
            download.setDownloadFileName(save_path.name)
            download.accept()
        else:
            download.cancel()

    def loadInstanceCommand(
        self,
        data: dict[str, str],
        instanceManager: InstanceManager,
    ) -> None:
        """TODO :_summary_

        Args:
            data (dict[str, str]): _description_
            instanceManager (InstanceManager): _description_
        """
        instance: Instance = Instance()
        instance.load_inst_from_dict(data)
        instanceManager.instance = instance
        self.loadInstanceInForm(instanceManager)

    def loadInstanceInForm(self, instanceManager: InstanceManager) -> None:
        """TODO : _summary_

        Args:
            instanceManager (InstanceManager): _description_
        """
        self.ui.instanceNameInputBox.setText(instanceManager.instance.name)
        self.image_label = instanceManager.instance.image
        self.news_feed = instanceManager.instance.news_feed
        self.instance_name = instanceManager.instance.name
        self.ui.usernameInputBox.setText(instanceManager.instance.username)
        self.ui.versionsComboBox.setEditText(instanceManager.instance.version)
        self.ui.pathInputBox.setText(instanceManager.instance.installation_path)
        self.ui.repoURLInputBox.setText(instanceManager.instance.repo_url)
        pixmap: QPixmap = QPixmap(self.image_label)
        self.ui.instance_img.setPixmap(pixmap)
        self.ui.repo_name_branch.setText(self.instance_name)
        self.ui.newsEngineView.setUrl(self.news_feed)
        instanceManager.instance.display()
        # TODO : FIX THE INSTANCE SOURCE BEFORE RENABLED THIS FEATURES
        if not instanceManager.is_installable():
            self.ui.installButton.setEnabled(False)
        else:
            self.ui.installButton.setEnabled(True)
