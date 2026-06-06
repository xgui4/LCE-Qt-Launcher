#!/usr/bin/env python3
"""
LCE Qt Launcher
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
along with this program. If not, see https://www.gnu.org/licenses/.
"""
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --include-qt-plugins=sensible

# nuitka-project-if: {OS} == "Windows":
#   nuitka-project: --windows-icon-from-ico=assets/app.ico
#   nuitka-project: --windows-product-name=LCE-Qt-Launcher
#   nuitka-project: --product-version="0.0.21.1"
#   nuitka-project: --file-version="0.0.21.1"
#   nuitka-project: --file-description="LCE Qt Launcher Alpha"
#   nuitka-project: --copyright="Copyleft Xgui4 2026 (GPLv3)"

# nuitka-projet:  --include-distribution-metadata=lce-qt-launcher

from lce_qt_launcher import instance_extension_str
from lce_qt_launcher.models.pref import UserPref
from lce_qt_launcher.models.app_data import AppData
from lce_qt_launcher.views.cmd_arg import (
    CmdArgAction,
    parse_args,
    argsDetected,
    launch_cmd_action,
)
from lce_qt_launcher.app_context import AppContext
from lce_qt_launcher.app import App
from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.models.theme import StrTheme
import lce_qt_launcher.models.theme as theme


from PySide6.QtWidgets import QMessageBox, QFileDialog
from PySide6.QtGui import QFontDatabase


import sys
import os


def main() -> None:
    appData: AppData = AppData()
    appContext: AppContext = AppContext(appData)
    sys_man: SystemManager = appContext.sys_man

    if "--disable-system-qt-plugins" not in sys.argv:
        sys_man.adapt_qt_system_theme()

    userPref: UserPref = appContext.userPref
    languagePref : str = userPref.getLanguagePref()
    userTheme: str = userPref.getThemePref()
    showHoliday: str = userPref.getShowHolidayPref()
    developerMode: str = userPref.getDevelopperModePref()
    accessibleMode: str = userPref.getAccesibleModePref()
    experimentMode: str = userPref.getExperimentalModePref()
    username: str = userPref.getUsernamePref()
    defaultInstancePath: str = userPref.getInstancePathPref()

    selected_theme: StrTheme = theme.from_str_to_strTheme(userTheme)
    appContext.theme = selected_theme
    appContext.selectedLang = languagePref 
    appContext.showHolidayEnabled = bool(showHoliday)
    appContext.devModeEnabled = bool(developerMode)
    appContext.experimentModeEnabled = bool(experimentMode)
    appContext.accesibleModeEnabled = bool(accessibleMode)
    appContext.username = username
    appContext.instancePath =  appContext.expand_path(defaultInstancePath, appData)
    appContext.updateAppUILang()

    def about_to_quit_event() -> None:
        instance_manager_label: str = appContext.translator.translate(
            "instance_manager_label"
        )
        save_instance_msg_box_label: str = appContext.translator.translate(
            "save_instance_msg_box_label"
        )
        save_filedialog_title: str = appContext.translator.translate(
            "save_filedialog_title"
        )
        question_options = (
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        anwser = QMessageBox.question(
            None, instance_manager_label, save_instance_msg_box_label, question_options
        )
        if anwser == QMessageBox.StandardButton.Yes:
            file_name: str = QFileDialog.getSaveFileName(
                None,
                save_filedialog_title,
                f'{appData.appDataDirs}("LCE Instance Save File" (*{instance_extension_str}))',
            )[0]
            appContext.instanceMan.save_instance(file_name)

    action: CmdArgAction = parse_args(sys.argv)
    if argsDetected(action):
        launch_cmd_action(action, appContext, appData)
    else:
        os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"

        app = App(appContext.theme, appContext, sys.argv)
        app.setStyle("Fusion")
        app.aboutToQuit.connect(about_to_quit_event)

        font_id = QFontDatabase.addApplicationFont(":/fonts/monocraft.ttc")

        if font_id == -1:
            print("Error: Font could not be loaded.")
        else:
            family = QFontDatabase.applicationFontFamilies(font_id)[0]
            app.setFont(family)

        sys.exit(app.exec())


if __name__ == "__main__":
    main()
