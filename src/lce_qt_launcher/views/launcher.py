from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QLabel,
    QListWidgetItem,
    QInputDialog,
    QMessageBox,
)
from PySide6.QtGui import QPalette, QPixmap, QBrush
from PySide6.QtCore import Qt #, QFile, QIODevice
from PySide6.QtWebEngineCore import (
    QWebEnginePage,
    QWebEngineProfile,
    QWebEngineDownloadRequest,
)

import json
import webbrowser
import os

from pathlib import Path

from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.app_context import AppContext
from lce_qt_launcher.managers.instance_manager import Instance, InstanceManager
from lce_qt_launcher.models.app_data import AppData
from lce_qt_launcher.views.content_installer_dialog import ContentInstallerView
from lce_qt_launcher.views.instance_editor_view import InstanceEditorView
from lce_qt_launcher.views.about_view import AboutView
from lce_qt_launcher.ui_settingDialog import Ui_settingDialog
from lce_qt_launcher.utils.json_trans import JsonTrans
from lce_qt_launcher.ui_form import Ui_launcher
from lce_qt_launcher.managers.steam_manager import add_instance_to_steam
from lce_qt_launcher import (
    app_name_str,
    version_str,
    version_type_str,
    git_repo_url_str,
    instance_extension_str,
)
from lce_qt_launcher.views.system_info_view import SystemInfoView

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
        self.username: str = appContext.username

        skinUsername : str = appContext.username # pyright: ignore[reportUnusedVariable] # disabled temporably

        STARTING_GAME_MSG: str = translator.translate("start_game_msg")

        def generateInstanceFromForm() -> None:
            instanceManager.instance = features.new_instance_from_form(self)  # type: ignore

        def confirmChangesButtonCommand() -> None:
            generateInstanceFromForm()

        def playButtonCommand() -> None:
            features.launch_game(instanceManager, appContext, STARTING_GAME_MSG)

        def installButtonCommand() -> None:
            features.install_game_gui(self, instanceManager, appContext)

        def showSettingDialogCommand() -> None:
            features.show_setting(self, Ui_settingDialog(), appContext)

        def saveInstanceButtonCommand() -> None:
            features.save_instance_to_file(self, instanceManager, appContext)

        def changeInstanceIconButtonCommand() -> None:
            file_name: str = QFileDialog.getOpenFileName(
                self,
                "Select the image file for the instance",
                os.path.expanduser("~"),
                f"{app_name_str} Instance File (*{instance_extension_str})",
            )[0]
            instanceManager.instance.image = file_name
            self.ui.instance_img.setPixmap(QPixmap(file_name))

        def showInstanceEditorButtonCommand() -> None:
            editor = InstanceEditorView(self)
            editor.loadInstance(instanceManager.instance)

        def showAboutMinecraftActionCommand() -> None:
            features.show_webbrowser(self, appContext.MINECRAFT_WEBSITE)

        def showMoreLCEProjectsActionCommand() -> None:
            features.show_webbrowser(self, appContext.MINECRAFT_LCE_WEBSITE)

        def updateActionCommand() -> None:
            features.show_webbrowser(self, git_repo_url_str)

        def loadInstanceActionCommand() -> None:
            features.load_instance_from_file(self, instanceManager, appContext, appData)
            self.loadInstanceInForm(instanceManager, appContext)

        def showSystemInformationActionCommand() -> None:
            SystemInfoView(self, systemManager)

        def showAboutQtActionCommand() -> None:
            features.show_about_qt(self)

        def showAboutActionCommand() -> None:
            AboutView(self)

        def installContentActionCommand() -> None:
            ContentInstallerView()

        def loadSteamCommand() -> None:
            features.launch_instance_with_steam(instanceManager)

        def openAppInstancesDataCommand() -> None:
            systemManager.open_url_with_system(
                os.path.join(appData.appDataDirs[0], "instances")
            )

        def openWorkshopCommand() -> None:
            features.show_webbrowser(self, "https://lce-hub.github.io/piston/")

        def openAppRootCommand() -> None:
            systemManager.open_url_with_system(appData.projectRootDir)

        def openAppConfigCommand() -> None:
            # FIXME appData do not give the correct path
            systemManager.open_url_with_system(appData.appConfigDir)

        def openGitHubIssuesCommand() -> None:
            webbrowser.open(git_repo_url_str + "/issues")

        # def loadDefaultInstanceCommand() -> None:
        #     self.loadInstanceData(dict(), instanceManager, appContext)

        def loadInstanceFromItemDataCommand() -> None:
            item = self.ui.listWidget.currentItem()
            if item:
                instance: Instance = item.data(Qt.UserRole)  # type: ignore
            else:
                raise RuntimeError("Could not load instance")
            instanceManager.instance = instance
            self.loadInstanceInForm(instanceManager, appContext)

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

        def changeTheSkinCommand():
            skinUsername = self.ui.usernameSkinInputBox.text()
            URL_STR = "https://kurojs.github.io/McView3D/embed.html?skin=Steve&width=400&height=400&animation=idle"
            new_url_str : str = URL_STR.replace("Steve", skinUsername)
            self.ui.skinManagerWebUI.setUrl(new_url_str)

        background_pixmap = QPixmap(appContext.BACKGROUND_PIXMAP_IMG)
        if not background_pixmap.isNull():
            palette: QPalette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(background_pixmap))
            self.setPalette(palette)
            self.setAutoFillBackground(True)
        else:
            term_service.print_error("Cannot set the background")

        self.ui: Ui_launcher = Ui_launcher()
        self.ui.setupUi(self)  # type: ignore
        for inst in appData.instsList:
            self.instances.append(inst)
            item = QListWidgetItem()
            item.setText(inst.name)
            item.setIcon(QPixmap(inst.image))
            item.setData(Qt.UserRole, inst)  # type: ignore
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

        systemManager: SystemManager = appContext.sys_man

        self.ui.progressLabel.setVisible(False)
        self.ui.progressBar.setVisible(False)
        self.ui.downloadFromLabel.setVisible(False)
        self.ui.downloadFromValue.setVisible(False)
        self.ui.installToLabel.setVisible(False)
        self.ui.installToValue.setVisible(False)

        self.ui.playButton.clicked.connect(playButtonCommand)
        self.ui.installButton.clicked.connect(installButtonCommand)
        self.ui.settingButton.clicked.connect(showSettingDialogCommand)
        self.ui.savetInstanceButton.clicked.connect(saveInstanceButtonCommand)
        self.ui.confirmChangesButton.clicked.connect(confirmChangesButtonCommand)
        self.ui.openInstanceEditor.clicked.connect(showInstanceEditorButtonCommand)
        self.ui.changeInstanceIconButton.clicked.connect(
            changeInstanceIconButtonCommand
        )
        self.ui.playOnSteamButton.clicked.connect(loadSteamCommand)
        self.ui.addSteamLinkIntegration.clicked.connect(
            addSteamLinkIntegrationButtonCommand
        )
        self.ui.loadSelectedInstanceButton.clicked.connect(
            loadInstanceFromItemDataCommand
        )
        self.ui.addInstanceButton.clicked.connect(loadInstanceActionCommand)

        self.ui.actionSetting.triggered.connect(showSettingDialogCommand)
        self.ui.actionSetting_2.triggered.connect(showSettingDialogCommand)
        self.ui.actionSetting_3.triggered.connect(showSettingDialogCommand)
        self.ui.actionQuit.triggered.connect(app.quit)
        self.ui.actionUpdate.triggered.connect(updateActionCommand)
        self.ui.actionSystem_Information.triggered.connect(
            showSystemInformationActionCommand
        )
        self.ui.actionAbout.triggered.connect(showAboutActionCommand)
        self.ui.actionAbout_QT.triggered.connect(showAboutQtActionCommand)
        self.ui.actionAbout_Minecraft.triggered.connect(showAboutMinecraftActionCommand)
        self.ui.actionMore_Minecraft_LCE_Projects.triggered.connect(
            showMoreLCEProjectsActionCommand
        )
        self.ui.actionSave.triggered.connect(saveInstanceButtonCommand)
        self.ui.actionImport_Instance.triggered.connect(loadInstanceActionCommand)
        self.ui.actionInstall_Content.triggered.connect(installContentActionCommand)
        self.ui.actionInstances.triggered.connect(openAppInstancesDataCommand)
        self.ui.actionLCE_Hub_Workshop.triggered.connect(openWorkshopCommand)
        self.ui.actionApp_Root.triggered.connect(openAppRootCommand)

        self.ui.actionConfigPath.triggered.connect(openAppConfigCommand)
        # Action for opening configuration is temporaly disabled until it is fixed
        self.ui.actionConfigPath.setEnabled(False)
        self.ui.actionConfigPath.setText("Configuration (Broken)")

        self.ui.actionReport_a_Bugs_or_Sugess_a_feature.triggered.connect(
            openGitHubIssuesCommand
        )

        self.ui.changeSkinButton.clicked.connect(changeTheSkinCommand)

        self.ui.downloadSkinButton.setEnabled(False)
        self.ui.downloadFromLabel.setText("Download Skin (Coming Soon)")

        self.setup_web_engine()

        self.versionLabel: QLabel = QLabel(f"Version {version_type_str} {version_str}")
        self.ui.statusbar.addPermanentWidget(self.versionLabel)

        self.usernameLabel: QLabel = QLabel(self.username)
        self.ui.statusbar.addWidget(self.usernameLabel)

        if appContext.showHolidayEnabled:
            holyday_label: QLabel = QLabel(holiday.get_holiday())
            self.ui.statusbar.addWidget(holyday_label)

        self.loadInstanceInForm(instanceManager, appContext)

    def setup_web_engine(self):
        page: QWebEnginePage = self.ui.marketplacesWebsiteEngine.page()
        self.browser_profile: QWebEngineProfile = page.profile()
        self.browser_profile.downloadRequested.connect(self.handleDownloadCommand)

    def handleDownloadCommand(self, download: QWebEngineDownloadRequest):
        """Processes the PySide6 download stream request."""

        term_service.print_information("Download Started!")

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

    def loadInstanceData(
        self,
        data: dict[str, str],
        instanceManager: InstanceManager,
        appContext: AppContext,
    ) -> None:
        """_summary_ Loas insance from data json in instance manager

        Args:
            data (dict[str, str]): _description_ the json data to load
            instanceManager (InstanceManager): _description_ the instance manager to use
            appContext (AppContext): _description_ the App Context to use
        """
        instance: Instance = Instance()
        instance.load_inst_from_dict(data)
        instanceManager.instance = instance
        self.loadInstanceInForm(instanceManager, appContext)

    def loadInstanceInForm(
        self, instanceManager: InstanceManager, appContext: AppContext
    ) -> None:
        """_summary_ Load Instance in form

        Args:
            instanceManager (InstanceManager): _description_ the instance manager to load
        """
        self.ui.instanceNameInputBox.setText(instanceManager.instance.name)
        self.image_label = instanceManager.instance.image
        self.news_feed = instanceManager.instance.news_feed
        self.instance_name = instanceManager.instance.name
        self.ui.usernameInputBox.setText(
            appContext.username
            if instanceManager.instance.username == "Steve" or ""
            else instanceManager.instance.username
        )
        self.ui.versionsComboBox.setEditText(instanceManager.instance.version)
        self.ui.pathInputBox.setText(instanceManager.expanded_path(appContext))
        self.ui.repoURLInputBox.setText(instanceManager.instance.repo_url)
        pixmap: QPixmap = QPixmap(self.image_label)
        self.ui.instance_img.setPixmap(pixmap)
        self.ui.repo_name_branch.setText(self.instance_name)
        self.ui.newsEngineView.setUrl(self.news_feed)
        instanceManager.instance.display()

        if not instanceManager.is_installable():
            self.ui.installButton.setEnabled(False)
        else:
            self.ui.installButton.setEnabled(True)
