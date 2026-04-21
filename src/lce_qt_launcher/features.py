# pyright: reportAttributeAccessIssue=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false
from PySide6.QtNetwork import QNetworkReply

from PySide6.QtWidgets import(
    QMainWindow, 
    QLabel, 
    QProgressBar, 
    QMessageBox, 
    QFileDialog, 
    QInputDialog,
    QWidget,
)

from lce_qt_launcher.ui_settingDialog import Ui_settingDialog
import lce_qt_launcher.views.term_service as term_service
import lce_qt_launcher.views.cli as cli 

from lce_qt_launcher.views.browser_dialog import BrowserDialog
from lce_qt_launcher.views.setting_dialog import SettingDialog
from lce_qt_launcher.models.preferences import UserPref
from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.managers.instance_manager import InstanceManager, Instance

def install_game(parent : QWidget, instance : Instance, instanceManager : InstanceManager) -> None:
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

            def update_progress_bar(bytes_received, bytes_total):
                if bytes_total > 0:
                    _ = progressBar.setMaximum(bytes_total)
                    _ = progressBar.setValue(bytes_received)
                else:
                    _ = progressBar.setRange(0, 0)  
            _ = reply.downloadProgress.connect(update_progress_bar)

        except RuntimeError as e:
            _ = progressLabel.setVisible(True) 
            _ = progressBar.setVisible(True)  
            _ = progressBar.setEnabled(True)  
            _ = progressLabel.setText(f"Downloading {instance.name} Cancelled due to a error.")
            _ = QMessageBox.critical(parent, "Minecraft LCE Qt Launcher", f"There were a error during the installation \n traceback : {e.with_traceback()}", QMessageBox.StandardButton.Ok)
    else:
        _ = QMessageBox.information(parent, "Minecraft LCE Qt Launcher", "Installation Cancelled", QMessageBox.StandardButton.Ok)

def launch_game(instanceManager : InstanceManager, starting_game_msg_str : str) -> None:
    term_service.print_information(starting_game_msg_str)
    print(instanceManager.play())

def show_setting(parent : QWidget, setting_ui : Ui_settingDialog)  -> None:
    _ = SettingDialog(parent, setting_ui)

def show_system_info(parent : QWidget) -> None:
    parent.sysinfo_dialog.show()  

def show_instance_editor(parent : QWidget) -> None:
    parent.instance_window.show()  

def load_instance(parent : QWidget, instanceManager : InstanceManager, buildInfo : BuildInfo) -> None:  
    file_name = QFileDialog.getOpenFileName(
        parent, "Load Instance File", 
        buildInfo.system_manager.found_default_save_path(), 
        f"{buildInfo.app_name} Instance (*{buildInfo.instance_extension})")
    instanceManager.load_instance(file_name[0])


def show_about_qt(parent : QWidget) -> None:
    print("Show About Qt popup.")
    QMessageBox.aboutQt(parent, "About Qt")

def show_about_app(parent : QWidget) -> None:
    parent.aboutDialog.show()

def new_instance_from_form(mainWindow : QMainWindow) -> Instance:
    form = mainWindow.ui  

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
    _ = BrowserDialog(parent, url, buildInfo)

def save_instance(parent :  QWidget, instanceManager : InstanceManager, buildInfo : BuildInfo):
    file_name: str = QFileDialog.getSaveFileName(
        parent, 
        "Save Instance option to a file", 
        buildInfo.system_manager.found_default_save_path(), 
        f"{buildInfo.app_name} Instance File (*{buildInfo.instance_extension})")[0]
    instanceManager.save_instance(file_name)

def launch_cli_interface(instance_man : InstanceManager, buildInfo : BuildInfo, argv : list):
    cli.launch_cli(instance_man, buildInfo, argv)

def generate_user_config(userPref : UserPref) -> None:
    userPref.generate_default_config()

def display_license(buildInfo : BuildInfo) -> None:
    term_service.print_information(f"{buildInfo.app_name} is licensed via the {buildInfo.license} License.")
    term_service.print_information(f"See {buildInfo.license_link} for more info")

def display_help(help_str : str) -> None:
    term_service.print_pretty(help_str)

def display_about(about_str : str) -> None:
    term_service.print_pretty(about_str)

def display_version(buildInfo : BuildInfo) -> None:
    term_service.print_information(f"{buildInfo.app_name} Version {buildInfo.version}")
    term_service.print_information(f"Qt Version {buildInfo.qt_version}")
