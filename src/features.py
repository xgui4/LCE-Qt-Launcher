from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QDialog, QMessageBox, QFileDialog, QInputDialog
from PySide6.QtGui import QPalette, QPixmap, QBrush
from PySide6.QtCore import qVersion
from user_pref import UserPref
from build_info import BuildInfo
from instance_manager import InstanceManager, Instance
from cmd_arg import CmdArgAction, parse_args, argsDetected

import term_service

from browser_dialog import BrowserDialog
from setting_dialog import SettingDialog
from cli import launch_cli

import sys
import os
import platform

def confirm_changes(parent):
    pass

def launch_game(parent):
    pass

def launch_game(parent):
    pass

def launch_setting(parent):
    pass

def load_instance(parent):
    pass

def new_instance_from_form(mainWindow : QMainWindow):
    form = mainWindow.ui

    username_str = form.usernameInputBox.text()
    path_str = form.pathInputBox.text()
    server_ip_str = form.serverIPInputBox.text()
    server_name_str = form.serverNameInputBox.text()
    repo_url_str = form.repoURLInputBox.text()

    instance_name = QInputDialog.getText(mainWindow, "Name your instance", "Set the name of the instance")

    newInstance = Instance()

    if instance_name:
        newInstance.name = instance_name
    if username_str:
        newInstance.username = username_str
    if path_str:
        newInstance.installation_path = path_str
    if server_ip_str and server_name_str:
        newInstance.servers = {f"ip : {server_ip_str}, name : {server_name_str}" }
    if repo_url_str:
        newInstance.repo_url = repo_url_str

    return newInstance; 

def setup_update(parent):
    pass

def hide_options(parent):
    pass

def show_webpage(parent):
    pass