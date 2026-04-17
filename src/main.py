#!/usr/bin/env python3

# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --windows-icon-from-ico=assets/app.ico
# nuitka-project: --windows-product-name=LCE-Qt-Launcher
# nuitka-project: --include-data-dir=assets=assets
# nuitka-project: --include-data-dir=data=data
# nuitka-project: --include-qt-plugins=sensible
# nuitka-project: --windows-console-mode=force
# nuitka-project: --product-version="0.26.4.16"
# nuitka-project: --file-version="0.26.4.16"
# nuitka-project: --file-description="Custom Free/Libre Minecraft LCE Launcher (Nightly)"
# nuitka-projet:  --include-distribution-metadata=lce-qt-launcher
# nuitka-project: --copyright="Copyleft Xgui4 2026 (GPLv3)"

from PySide6.QtWidgets import QMessageBox, QFileDialog

from lce_qt_launcher.views import term_service
from lce_qt_launcher.views.cmd_arg import CmdArgAction, parse_args, argsDetected, launch_cmd_action
from lce_qt_launcher.app_context import AppContext
from lce_qt_launcher.app import App

from ui_form import Ui_launcher
from ui_instance import Ui_InstancesEditor
from ui_system_info import Ui_sys_info_dialog
from ui_settingDialog import Ui_settingDialog
from ui_about import Ui_AboutDialog

import sys
import os

if __name__ == "__main__":
    appContext = AppContext()

    sys_man = appContext.buildInfo.system_manager
    try:
        sys_man.adapt_qt_system_theme()

        userPref = appContext.userPref

        user_language = userPref.get_language_pref()
        user_theme = userPref.get_theme_pref()
        show_holyday = userPref.get_show_holyday()
        developer_mode = userPref.get_developper_mode()
        accessible_mode = userPref.get_accesible_mode()

        appContext.updateLanguage(user_language)
        appContext.updateTheme(user_theme)
    except:
        term_service.print_error("They were a error while loading the system theme or user preference.")

    def about_to_quit_event():
        instance_manager_label = appContext.translator.translate("instance_manager_label")
        save_instance_msg_box_label = appContext.translator.translate("save_instance_msg_box_label")         
        save_filedialog_title = appContext.translator.translate("save_filedialog_title")
        question_options = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        anwser = QMessageBox.question(None, instance_manager_label, save_instance_msg_box_label, question_options)
        if anwser == QMessageBox.StandardButton.Yes:
            file_name: str = QFileDialog.getSaveFileName(
                None, save_filedialog_title,
                  f"{appContext.buildInfo.system_manager.found_default_save_path }(\"LCE Instance Save File\" (*{appContext.buildInfo.instance_extension}))")[0]
            appContext.instanceMan.save_instance(file_name)

    action : CmdArgAction = parse_args(sys.argv)
    if argsDetected(action):
        launch_cmd_action(action, appContext)
    else:
        os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"

        app = App(appContext.theme, Ui_launcher, Ui_sys_info_dialog, Ui_InstancesEditor, Ui_settingDialog, Ui_AboutDialog, appContext, sys.argv)
        _ = app.setStyle("Fusion")
        app.aboutToQuit.connect(about_to_quit_event)
        sys.exit(app.exec())