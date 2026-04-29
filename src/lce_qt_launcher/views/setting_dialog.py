from PySide6.QtWidgets  import QDialog, QWidget

from lce_qt_launcher.ui_settingDialog import Ui_settingDialog

class SettingDialog(QDialog):
    """_summary_ The Setting Dialog"""
    def __init__(self, parent : QWidget, ui_setting : Ui_settingDialog) -> None:
        super().__init__()
        self.setting_dialog: QDialog = QDialog(parent) 
        self.ui_setting: Ui_settingDialog =  ui_setting 
        self.ui_setting.setupUi(self.setting_dialog)  # pyright: ignore[reportUnknownMemberType]
        self.setting_dialog.show()