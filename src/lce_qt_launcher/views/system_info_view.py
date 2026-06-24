import sys

from PySide6.QtWidgets import QDialog, QWidget
from PySide6.QtCore import qVersion

from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.ui_system_info import Ui_sys_info_dialog

from lce_qt_launcher import app_name_str, version_str, version_type_str


class SystemInfoView(QDialog):
    def __init__(self, parent: QWidget, systemManager: SystemManager):
        super().__init__(parent)

        self.sysinfo_dialog: QDialog = QDialog()
        self.dialog_ui: Ui_sys_info_dialog = Ui_sys_info_dialog()
        self.dialog_ui.setupUi(self.sysinfo_dialog)

        self.dialog_ui.appVersionLabel.setText(
            f"**App Version** : {app_name_str} {version_type_str} {version_str}"
        )
        self.dialog_ui.qVersionLabel.setText(f"**Qt Version** : {qVersion()}")
        self.dialog_ui.pyVersionLabel.setText(f"**Python Version** : {sys.version}")
        self.dialog_ui.osInfoLabel.setText(
            f"**System Name** : {systemManager.name} \n**System Version** : {systemManager.version}"
        )

        self.dialog_ui.pluginsInfoLabel.setText("")
        self.dialog_ui.runnersLabel.setText("")

        self.sysinfo_dialog.show()
