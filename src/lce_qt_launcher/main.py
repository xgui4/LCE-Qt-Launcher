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
#   nuitka-project: --product-version="0.0.20.6"
#   nuitka-project: --file-version="0.0.20.6"
#   nuitka-project: --file-description="LCE Qt Launcher Alpha"
#   nuitka-project: --copyright="Copyleft Xgui4 2026 (GPLv3)"

# nuitka-project: --include-data-dir=assets=assets
# nuitka-project: --include-data-dir=data=data
# nuitka-projet:  --include-distribution-metadata=lce-qt-launcher


from lce_qt_launcher import instance_extension_str
from lce_qt_launcher.models.pref import UserPref
from lce_qt_launcher.models.app_data import AppData
from lce_qt_launcher.views import term_service
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

    try:
        if "--disable-system-qt-plugins" not in sys.argv:
            sys_man.adapt_qt_system_theme()
        userPref: UserPref = appContext.userPref
        user_language: str = userPref.get_language_pref() #FIXME :  This should return a language
        user_theme: str = userPref.get_theme_pref()
        show_holiday: str = userPref.get_show_holiday_pref()
        developer_mode: str = userPref.get_developper_mode_pref()
        accessible_mode: str = userPref.get_accesible_mode_pref()
        experiment_mode: str = userPref.get_experimental_mode_pref()
        username: str = userPref.get_username_pref()
        default_instance_path: str = userPref.get_instance_path_pref()
        try:
            selected_theme: StrTheme = theme.from_str_to_strTheme(user_theme)
            appContext.theme = selected_theme
            appContext.showHolidayEnabled = bool(show_holiday)
            appContext.devModeEnabled = bool(developer_mode)
            appContext.experimentModeEnabled = bool(experiment_mode)
            appContext.accesibleModeEnabled = bool(accessible_mode)
            appContext.defaultUsername = str(username)
            appContext.defaultInstancePath = str(default_instance_path)
        except RuntimeError as err:
            term_service.print_error(str(err))
        finally:
            appContext.updateAppUILang()
    except:
        #FIXME do not use a bare except : https://docs.astral.sh/ruff/rules/bare-except/
        term_service.print_error(
            "They were a error while loading the system theme or user preference."
        )

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
