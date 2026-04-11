from PySide6.QtWidgets  import QDialog, QVBoxLayout, QLabel

class SettingDialog(QDialog):
    def __init__(self, parent, setting_ui):
        self.setting_dialog = QDialog(parent) 
        self.setting_ui = setting_ui()
        self.setting_ui.setupUi(self.setting_dialog)
        self.setting_dialog.show()