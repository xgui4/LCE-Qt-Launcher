from PySide6.QtWidgets  import QDialog, QWidget

from lce_qt_launcher.ui_settingDialog import Ui_settingDialog

class SettingDialog(QDialog):
    def __init__(self, parent : QWidget, ui_setting : Ui_settingDialog) -> None:
        self.setting_dialog: QDialog = QDialog(parent) 
        self.ui_setting: Ui_settingDialog =  ui_setting 
        self.setting_ui.setupUi(self.setting_dialog)
        self.setting_dialog.show()