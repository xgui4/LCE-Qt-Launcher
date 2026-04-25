#!/usr/bin/env python3

# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --windows-icon-from-ico=assets/app.ico
# nuitka-project: --windows-product-name=LCE-Qt-Launcher
# nuitka-project: --include-data-dir=assets=assets
# nuitka-project: --include-data-dir=data=data
# nuitka-project: --include-qt-plugins=sensible
# nuitka-project: --windows-console-mode=force
# nuitka-project: --product-version="1.0.0.11"
# nuitka-project: --file-version="1.0.0.11"
# nuitka-project: --file-description="Custom Free/Libre Minecraft LCE Launcher (Nightly)"
# nuitka-projet:  --include-distribution-metadata=lce-qt-launcher
# nuitka-project: --copyright="Copyleft Xgui4 2026 (GPLv3)"

"""
    LCE Qt Launcher Manager
    Copyright (C) 2026 Xgui4

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from PySide6.QtWidgets import (
    QMessageBox, 
    QFileDialog
) 

from lce_qt_launcher.models.app_data import AppData
from lce_qt_launcher.views import term_service
from lce_qt_launcher.views.cmd_arg import CmdArgAction, parse_args, argsDetected, launch_cmd_action
from lce_qt_launcher.app_context import AppContext
from lce_qt_launcher.app import App
from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.views.theme import Theme
import lce_qt_launcher.views.theme as theme

import sys
import os

def main() -> None:
    """_summary_ Main Function
    """

    appData : AppData = AppData()
    appContext: AppContext = AppContext(appData)

    sys_man: SystemManager = appContext.sys_man
    try:
        sys_man.adapt_qt_system_theme()

        userPref = appContext.userPref

        user_language: str = userPref.get_language_pref()
        user_theme: str = userPref.get_theme_pref()
        show_holiday: str = userPref.get_show_holiday()
        developer_mode: str = userPref.get_developper_mode()
        accessible_mode: str = userPref.get_accesible_mode()
         
        try: 
            selected_theme: Theme = theme.from_str_to_theme(user_theme)
            appContext.updateTheme(selected_theme)
            appContext.updateShowHolidayStatus(show_holiday)
            appContext.updateSetDevMoodeStatus(developer_mode)
            appContext.updateSetAccesbilityMoodeStatus(accessible_mode)
        except RuntimeError as err:
            term_service.print_error(str(err))

        appContext.updateLanguage(user_language)
    except:
        term_service.print_error("They were a error while loading the system theme or user preference.")

    def about_to_quit_event() -> None:
        instance_manager_label: str = appContext.translator.translate("instance_manager_label")
        save_instance_msg_box_label: str = appContext.translator.translate("save_instance_msg_box_label")         
        save_filedialog_title: str = appContext.translator.translate("save_filedialog_title")
        question_options = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        anwser = QMessageBox.question(None, instance_manager_label, save_instance_msg_box_label, question_options)
        if anwser == QMessageBox.StandardButton.Yes:
            file_name: str = QFileDialog.getSaveFileName(
                None, save_filedialog_title,
                  f"{appContext.sys_man.found_default_save_path()}(\"LCE Instance Save File\" (*{appContext.buildInfo.instance_extension}))")[0]
            appContext.instanceMan.save_instance(file_name)

    action : CmdArgAction = parse_args(sys.argv)
    if argsDetected(action):
        launch_cmd_action(action, appContext)
    else:
        os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"

        app = App(appContext.theme, appContext, sys.argv)
        _ = app.setStyle("Fusion")
        _ = app.aboutToQuit.connect(about_to_quit_event)
        sys.exit(app.exec())

if __name__ == "__main__":
    main()
