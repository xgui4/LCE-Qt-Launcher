from PySide6.QtWidgets import(
    QMainWindow, 
    QLabel, 
    QProgressBar, 
    QVBoxLayout, 
    QDialog, 
    QMessageBox, 
    QFileDialog, 
    QInputDialog,
    QWidget 
)
from PySide6.QtGui import (
     QPixmap
) 

import lce_qt_launcher.term_service as term_service
import lce_qt_launcher.cli as cli 

from lce_qt_launcher.gui.browser_dialog import BrowserDialog
from lce_qt_launcher.gui.setting_dialog import SettingDialog
from lce_qt_launcher.preferences import UserPref
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

        _ = progressLabel.setVisible(True) 
        _ = progressBar.setVisible(True)  
        _ = progressBar.setEnabled(True)  
        _ = progressLabel.setText(f"Installation of {instance.name} Progress")  
        _ = progressBar.setValue(30) 
        print(instanceManager.install_instance())
        _ = progressBar.setValue(100) 
    else:
        _ = QMessageBox.critical(parent, "Minecraft LCE Qt Launcher", "Installation Cancelled", QMessageBox.StandardButton.Ok)

def launch_game(instanceManager : InstanceManager, starting_game_msg_str : str) -> None:
    term_service.print_information(starting_game_msg_str)
    print(instanceManager.play())

def show_setting(parent : QWidget, setting_ui : object)  -> None:
    _ = SettingDialog(parent, setting_ui)

def show_system_info(parent : QWidget) -> None:
    parent.sysinfo_dialog.show()  

def show_instance_editor(parent : QWidget) -> None:
    parent.instance_window.show()  

def load_instance(parent : QWidget, instanceManager : InstanceManager, buildInfo : BuildInfo) -> None:  
    file_name: str = QFileDialog.getSaveFileName(parent, "Set the instance save file path to load", f"{buildInfo.system_manager.found_default_save_path }(\"LCE Instance Save File\" (*{buildInfo.instance_extension}))")[0]
    instanceManager.load_instance(file_name[0])

def show_about_qt(parent : QWidget) -> None:
    print("Show About Qt popup.")
    QMessageBox.aboutQt(parent, "About Qt")

def show_about_app(parent) -> None:
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
    file_name: str = QFileDialog.getSaveFileName(parent, "Set the instance save file path to saved", f"{buildInfo.system_manager.found_default_save_path }(\"LCE Instance Save File\" (*{buildInfo.instance_extension}))")[0]
    instanceManager.save_instance(file_name)

def launch_cli_interface(instance_man : InstanceManager):
    cli.launch_cli(instance_man)

def generate_user_config(userPref : UserPref):
    userPref.generate_default_config()

def display_license(buildInfo : BuildInfo):
    term_service.print_information(f"{buildInfo.app_name} is licensed via the {buildInfo.license} License.")
    term_service.print_information(f"See {buildInfo.license_link} for more info")

def display_help(help_str : str):
    term_service.print_pretty(help_str)

def display_about(about_str : str):
    term_service.print_pretty(about_str)

def display_version(buildInfo : BuildInfo):
    term_service.print_information(f"{buildInfo.app_name} Version {buildInfo.version}")
    term_service.print_information(f"Qt Version {buildInfo.qt_version}")

def hide_options():
    pass