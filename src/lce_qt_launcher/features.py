import os
import subprocess

from PySide6.QtNetwork import QNetworkReply
from PySide6.QtWidgets import (
    QFileDialog,
    QInputDialog,
    QLabel,
    QMessageBox,
    QProgressBar,
    QWidget,
)

from lce_qt_launcher.app_context import AppContext
from lce_qt_launcher.managers import import_managers
from lce_qt_launcher.managers.instance_manager import Instance, InstanceManager
from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.models.app_data import AppData
from lce_qt_launcher.models.pref import UserPref
from lce_qt_launcher.ui_settingDialog import Ui_settingDialog
from lce_qt_launcher.views.browser_dialog import BrowserDialog
from lce_qt_launcher.views.setting_dialog import SettingDialog
from lce_qt_launcher import (
    app_name_str,
    version_str,
    licence_name_str,
    qt_version_str,
    license_link_str,
    instance_extension_str,
)


import lce_qt_launcher.views.cli as cli
import lce_qt_launcher.views.term_service as term_service

def install_game_gui(
    parent: QWidget, instanceManager: InstanceManager, appContext : AppContext
) -> None:
    """_summary_
        Features : Install the game instance selected from instanceManager
    args:
    - parent : The QWidget parent
    - instanceManager : The instance manager to use
    - appContext (App Context): the appContext to use
    """
    # HACK : i keep the older method for now, but should be replace with a more generic one it would work even with the cli
    term_service.print_information("Starting Installation")
    progressLabel: QLabel = parent.ui.progressLabel # type: ignore
    progressBar: QProgressBar = parent.ui.progressBar # type: ignore
    download_reply: QNetworkReply | str = instanceManager.install_instance(appContext)
    if isinstance(download_reply, QNetworkReply):
        progressLabel.setVisible(True) # type: ignore
        progressBar.setVisible(True) # type: ignore
        parent.ui.downloadFromLabel.setVisible(True) # type: ignore
        parent.ui.downloadFromValue.setVisible(True) # type: ignore
        parent.ui.installToLabel.setVisible(True) # type: ignore
        parent.ui.installToValue.setVisible(True) # type: ignore
        progressLabel.setText(f"Downloading {instanceManager.instance.name} Progress") # type: ignore
        parent.ui.downloadFromValue.setText(instanceManager.instance.repo_url) # type: ignore 
        parent.ui.installToValue.setText(instanceManager.expanded_path(appContext)) # type: ignore

        def update_progress_bar(bytes_received: int, bytes_total: int) -> None:
            if bytes_total > 0:
                progressBar.setMaximum(bytes_total) # type: ignore
                progressBar.setValue(bytes_received) # type: ignore
            else: 
                progressBar.setRange(0, 0) # type: ignore

        download_reply.errorOccurred.connect(
            lambda : QMessageBox.critical(
                parent,
                "Install Manager",
                f"Instance {instanceManager.instance.name} has failed to install. \n Error : {download_reply.errorString()}",
                QMessageBox.StandardButton.Ok,
            )
        )
        download_reply.finished.connect(
            lambda : QMessageBox.information(
                parent,
                "Instance Manager",
                f"Installation of instance {instanceManager.instance.name} was a success",
                QMessageBox.StandardButton.Ok
            )
        )
        download_reply.downloadProgress.connect(update_progress_bar)

def install_game(
    instanceManager: InstanceManager,
    appContext : AppContext
) -> None:
    """_summary_
        Features : Install the game instance selected
    args:
    - instanceManager (InstanceManager): The instance manager to use
    - appContext (AppContext): the AppContext to use
    """
    term_service.print_information("Starting Installation")

    download_reply : QNetworkReply | str = instanceManager.install_instance(appContext)
    if isinstance(download_reply, QNetworkReply):
        download_reply.errorOccurred.connect(
            lambda : term_service.print_error(f"Instance {instanceManager.instance.name} has failed to install. Error : {download_reply.errorString()}")
        )
        download_reply.finished.connect(
            lambda : term_service.print_success(f"Installation of instance {instanceManager.instance.name} was a success")
        )
    else:
        print(download_reply)


def launch_game(instanceManager: InstanceManager, appContext : AppContext, starting_game_msg_str: str) -> None:
    """Features : Launch the game instance selected"""
    term_service.print_information(starting_game_msg_str)
    instanceManager.play(appContext)


def show_setting(
    parent: QWidget, setting_ui: Ui_settingDialog, appContext: AppContext
) -> None:
    """Features : Open the Setting Pages"""
    _ = SettingDialog(parent, setting_ui, appContext)


def load_instance_from_file(
    parent: QWidget,
    instanceManager: InstanceManager,
    appContext: AppContext,
    appData: AppData,
) -> None:
    """Features : Load the Selected Instance"""
    file_name: tuple[str, str] = QFileDialog.getOpenFileName(
        parent,
        "Load Instance File",
        os.path.expanduser("~"),
        f"{app_name_str} Instance (*{instance_extension_str})",
    )
    instanceManager.load_instance(file_name[0])
    try:
        import_managers.import_inst_file_to_app_data(file_name[0], appData)
    except FileExistsError:
        term_service.print_information(
            "Instance already in data folder. Skipping making symlink. "
        )


def show_about_qt(parent: QWidget) -> None:
    """Features : Load the Selected Instance"""
    print("Show About Qt popup.")
    QMessageBox.aboutQt(parent, "About Qt")


def open_url_at(sysMan: SystemManager, url: str) -> None:
    """_summary_ Open Url with system

    Args:
        sysMan (SystemManager): _description_ : SystemManager Class
        url (str): _description_ : The url to show
    """
    sysMan.open_url_with_system(url)


def generate_instance(instance_dict : dict[str, str]) -> Instance:
    """_summary_ :
        Create With Instance From Form
    Args:
        mainWindow (QMainWindow): _description_ : the main window form

    Returns:
        Instance: _description_ : the returned Instance created with the Form
    """
    newInstance = Instance()

    instance_name = instance_dict.get("instance_name")
    username_str = instance_dict.get("instance_str")
    version_str = instance_dict.get("version_str")
    path_str = instance_dict.get("path_str")
    repo_url_str = instance_dict.get("repo_url_str")

    if instance_name:
        newInstance.name = instance_name
    if username_str:
        newInstance.username = username_str
    if version_str:
        newInstance.version = version_str
    if path_str:
        newInstance.installation_path = path_str
    if repo_url_str:
        newInstance.repo_url = repo_url_str

    return newInstance

def new_instance_from_form(mainWindow) -> Instance: # type: ignore
    #FIXME: Make this feature less dependant on the GUI
    """_summary_ : Create With Instance From Form

    Args:
        mainWindow (QMainWindow): _description_ : the main window form

    Returns:
        Instance: _description_ : the returned Instance created with the Form
    """
    form  = mainWindow.ui # type: ignore
    username_str: str = form.usernameInputBox.text() # type: ignore
    version_str : str = form.versionInputBox.text() # type: ignore
    path_str: str = form.pathInputBox.text() # type: ignore
    repo_url_str: str = form.repoURLInputBox.text() # type: ignore
    instance_name: str = QInputDialog.getText(
        mainWindow, "Name your instance", "Set the name of the instance" # type: ignore
    )[0]
    newInstance = Instance()

    if instance_name:
        newInstance.name = instance_name
    if username_str:
        newInstance.username = username_str
    if version_str:
        newInstance.version = version_str
    if path_str:
        newInstance.installation_path = path_str
    if repo_url_str:
        newInstance.repo_url = repo_url_str

    return newInstance

def show_webbrowser(parent: QWidget, url: str) -> None:
    """_summary_ Create and show a Webbrowser view

    Args:
        parent (QWidget): _description_ the parent of the dialog
        url (str): _description_ the url desired
        buildInfo (BuildInfo): _description_ : The Build info of the app info
    """
    _ = BrowserDialog(parent, url)


def save_instance_to_file(
    parent: QWidget,
    instanceManager: InstanceManager,
    appContext: AppContext,
) -> None:
    """_summary_ Save the instance to a file

    Args:
        parent (QWidget): _description_ : the parent of the save dialog
        instanceManager (InstanceManager): _description_ Instance Manager to use to save the instance
        appContext (AppContext): _description_ the app context to use
        buildInfo (BuildInfo): _description_ The Build info of the app info
    """
    file_name: str = QFileDialog.getSaveFileName(
        parent,
        "Save Instance option to a file",
        os.path.expanduser("~"),
        f"{app_name_str} Instance File (*{instance_extension_str})",
    )[0]
    instanceManager.save_instance(file_name)


def launch_cli_interface(appContext: AppContext, appData: AppData) -> None:
    """_summary_ Launch the cli version of the app

    Args:
        instance_man (InstanceManager): _description_ : The instance manager to use
        buildInfo (BuildInfo): _description_ : The The Build info for the app info
    """
    cli.launch_cli(appContext, appData)


def generate_user_config(userPref: UserPref) -> None:
    """_summary_ Generate the default config

    Args:
        userPref (UserPref): _description_ : UserPreference Manager
    """
    userPref.generateDefaultConfig()


def display_license() -> None:
    """_summary_ Display the license of the app on the console

    Args:
        buildInfo (BuildInfo): _description_ : The Build info for the App Info
    """
    term_service.print_information(
        f"{app_name_str} is licensed via the {licence_name_str} License."
    )
    term_service.print_information(f"See {license_link_str} for more info")


def display_help(help_str: str) -> None:
    """_summary_ Display the help string of the app for the cli on the console

    Args:
        help_str (str): _description_ help string to show on the console
    """
    term_service.print_pretty(help_str)


def display_about(about_str: str) -> None:
    """_summary_  Display the about string of the app on the console

    Args:
        about_str (str): _description_ Display the help string of the app on the console
    """
    term_service.print_pretty(about_str)


def display_version() -> None:
    """_summary_ Display the string version on the console

    Args:
        buildInfo (BuildInfo): _description_ Display the help string of the app for the cli on the console
    """
    term_service.print_information(f"{app_name_str} Version {version_str}")
    term_service.print_information(f"Qt Version {qt_version_str}")


def launch_instance_with_steam(instanceManager: InstanceManager) -> None:
    subprocess.run(["steam", instanceManager.instance.steam_link])
