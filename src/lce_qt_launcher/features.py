# pyright: reportAttributeAccessIssue=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false
from PySide6.QtNetwork import QNetworkReply
from PySide6.QtWidgets import (
    QFileDialog,
    QInputDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QWidget,
)

from lce_qt_launcher.app_context import AppContext
from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.managers.instance_manager import Instance, InstanceManager
from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.models.preferences import UserPref
from lce_qt_launcher.ui_settingDialog import Ui_settingDialog
from lce_qt_launcher.views.browser_dialog import BrowserDialog
from lce_qt_launcher.views.setting_dialog import SettingDialog
import lce_qt_launcher.views.cli as cli
import lce_qt_launcher.views.term_service as term_service

def install_game(parent : QWidget, instance : Instance, instanceManager : InstanceManager) -> None:
    """Features : Install the game instance selected
    #TODO : Separe the GUI with the logic of the model
    # ARGS:
    - parent : The QWidget parent
    - instance : The selected Instance
    - instanceManager : The instance manager to use"""
    button_reply = QMessageBox.question(parent, 'Confirm Installation', 
                                    "Do you really want to re-install the game? " +
                                    "This version does not support update a installation yet," +
                                    " so a backup is recommended.",
                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    if button_reply == QMessageBox.StandardButton.Yes:
        term_service.print_information("Starting Installation")

        progressLabel : QLabel =  parent.ui.progressLabel  
        progressBar : QProgressBar = parent.ui.progressBar  
        try:
            reply: QNetworkReply = instanceManager.install_instance()
            _ = progressLabel.setVisible(True)
            _ = progressBar.setVisible(True)  
            _ = progressBar.setEnabled(True)  
            _ = progressLabel.setText(f"Downloading {instance.name} Progress")

            #TODO - VERIFY THIS
            def update_progress_bar(bytes_received, bytes_total) -> None:  # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
                if bytes_total > 0:
                    _ = progressBar.setMaximum(bytes_total)  # pyright: ignore[reportUnknownArgumentType]
                    _ = progressBar.setValue(bytes_received)  # pyright: ignore[reportUnknownArgumentType]
                else:
                    _ = progressBar.setRange(0, 0)  
            _ = reply.downloadProgress.connect(update_progress_bar)  # pyright: ignore[reportUnknownArgumentType]

        except RuntimeError as e:
            _ = progressLabel.setVisible(True) 
            _ = progressBar.setVisible(True)  
            _ = progressBar.setEnabled(True)  
            _ = progressLabel.setText(f"Downloading {instance.name} Cancelled due to a error.")
            _ = QMessageBox.critical(parent, "Minecraft LCE Qt Launcher", f"There were a error during the installation \n traceback : {e.args}", QMessageBox.StandardButton.Ok)
    else:
        _ = QMessageBox.information(parent, "Minecraft LCE Qt Launcher", "Installation Cancelled", QMessageBox.StandardButton.Ok)

def launch_game(instanceManager : InstanceManager, starting_game_msg_str : str) -> None:
    """Features : Launch the game instance selected"""
    term_service.print_information(starting_game_msg_str)
    print(instanceManager.play())

def show_setting(parent : QWidget, setting_ui : Ui_settingDialog)  -> None:
    """Features : Open the Setting Pages"""
    _ = SettingDialog(parent, setting_ui)

def show_system_info(parent : QWidget) -> None:
    """Features : Open the System Info Pages"""
    parent.sysinfo_dialog.show()  

def show_instance_editor(parent : QWidget) -> None:
    """Features : Open the Instance Editor"""
    parent.instance_window.show()  

def load_instance(parent : QWidget, instanceManager : InstanceManager, appContext: AppContext, buildInfo : BuildInfo) -> None:  
    """Features : Load the Selected Instance"""
    file_name: tuple[str, str] = QFileDialog.getOpenFileName(
        parent, "Load Instance File", 
        appContext.sys_man.found_default_save_path(), 
        f"{buildInfo.app_name} Instance (*{buildInfo.instance_extension})")
    instanceManager.load_instance(file_name[0])

def show_about_qt(parent : QWidget) -> None:
    """Features : Load the Selected Instance"""
    print("Show About Qt popup.")
    QMessageBox.aboutQt(parent, "About Qt")

def show_about_app(parent : QWidget) -> None:
    """_summary_ Features : Show About This App Dialog

    Args:
        parent (QWidget): _description_
    """
    parent.aboutDialog.show()

def open_url_at(sysMan : SystemManager, url : str):
    """_summary_ Open Url with system

    Args:
        sysMan (SystemManager): _description_ : SystemManager Class
        url (str): _description_ : The url to show
    """
    sysMan.open_url_with_system(url)

def new_instance_from_form(mainWindow : QMainWindow) -> Instance:
    """_summary_ : Create With Instance From Form
    #TODO : Make this feature less dependant on the GUI

    Args:
        mainWindow (QMainWindow): _description_ : the main window form (#TODO : should be changed)

    Returns:
        Instance: _description_ : the returned Instance created with the Form
    """
    form:QMainWindow = mainWindow.ui  
    username_str :str = form.usernameInputBox.text()  
    path_str : str = form.pathInputBox.text() 
    server_ip_str: str = form.serverIPInputBox.text() 
    server_name_str : str = form.serverNameInputBox.text()   
    repo_url_str: str = form.repoURLInputBox.text()
    instance_name: str = QInputDialog.getText(mainWindow, "Name your instance", "Set the name of the instance")[0]
    newInstance = Instance()

    if instance_name:
        newInstance.name = instance_name
    if username_str:
        newInstance.username = username_str
    if path_str:
        newInstance.installation_path = path_str
    if server_ip_str and server_name_str:
        newInstance.servers = [f"ip : {server_ip_str}, name : {server_name_str}"]
    if repo_url_str:
        newInstance.repo_url = repo_url_str

    return newInstance; 

def show_webbrowser(parent : QWidget, url : str, buildInfo : BuildInfo):
    """_summary_ Create and show a Webbrowser view

    Args:
        parent (QWidget): _description_ the parent of the dialog
        url (str): _description_ the url desired
        buildInfo (BuildInfo): _description_ : The Build info of the app info
    """
    _ = BrowserDialog(parent, url, buildInfo)

def save_instance_to_file(parent :  QWidget, instanceManager : InstanceManager, appContext: AppContext, buildInfo : BuildInfo) -> None:
    """_summary_ Save the instance to a file

    Args:
        parent (QWidget): _description_ : the parent of the save dialog
        instanceManager (InstanceManager): _description_ Instance Manager to use to save the instance
        appContext (AppContext): _description_ #TODO : To be determined 
        buildInfo (BuildInfo): _description_ The Build info of the app info
    """
    file_name: str = QFileDialog.getSaveFileName(
        parent, 
        "Save Instance option to a file", 
        appContext.sys_man.found_default_save_path(), 
        f"{buildInfo.app_name} Instance File (*{buildInfo.instance_extension})")[0]
    instanceManager.save_instance(file_name)

def launch_cli_interface(instance_man : InstanceManager) -> None:
    """_summary_ Launch the cli version of the app

    Args:
        instance_man (InstanceManager): _description_ : The instance manager to use
        buildInfo (BuildInfo): _description_ : The The Build info for the app info
    """
    cli.launch_cli(instance_man)

def generate_user_config(userPref : UserPref) -> None:
    """_summary_ Generate the default config

    Args:
        userPref (UserPref): _description_ : UserPreference Manager
    """
    userPref.generate_default_config()

def display_license(buildInfo : BuildInfo) -> None:
    """_summary_ Display the license of the app on the console

    Args:
        buildInfo (BuildInfo): _description_ : The Build info for the App Info 
    """
    term_service.print_information(f"{buildInfo.app_name} is licensed via the {buildInfo.license} License.")
    term_service.print_information(f"See {buildInfo.license_link} for more info")

def display_help(help_str : str) -> None:
    """_summary_ Display the help string of the app for the cli on the console

    Args:
        help_str (str): _description_ help string to show on the console 
    """
    term_service.print_pretty(help_str)

def display_about(about_str : str) -> None:
    """_summary_  Display the about string of the app on the console

    Args:
        about_str (str): _description_ Display the help string of the app on the console
    """
    term_service.print_pretty(about_str)

def display_version(buildInfo : BuildInfo) -> None:
    """_summary_ Display the string version on the console 

    Args:
        buildInfo (BuildInfo): _description_ Display the help string of the app for the cli on the console
    """
    term_service.print_information(f"{buildInfo.app_name} Version {buildInfo.version}")
    term_service.print_information(f"Qt Version {buildInfo.qt_version}")
