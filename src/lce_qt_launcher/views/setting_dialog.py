from PySide6.QtWidgets import QDialog, QWidget, QMessageBox
from PySide6.QtCore import Qt  

import lce_qt_launcher.models.theme as theme
from lce_qt_launcher.ui_settingDialog import Ui_settingDialog

class SettingDialog(QDialog):
    """_summary_ The Setting Dialog"""
    def __init__(self, parent : QWidget, ui_setting : Ui_settingDialog) -> None:
        super().__init__()
        self.setting_dialog: QDialog = QDialog(parent) 
        self.ui_setting: Ui_settingDialog =  ui_setting 
        self.ui_setting.setupUi(self.setting_dialog)  # pyright: ignore[reportUnknownMemberType]
        self.setting_dialog.show()

        def applyButtonCommand():
            isDevelopperModeEnabled = self.ui_setting.developperModeDheckBox.isChecked()
            isAccesbilityModeEnabled = self.ui_setting.accesibilitycheckBox.isChecked()
            isHolidayEnabled = self.ui_setting.holydayDheckBox.isChecked()
            themeSelectedIndex = self.ui_setting.themesComboBox.currentIndex()
            languageSelectedIndex = self.ui_setting.languagesComboBox.currentData()
            isExperimentsOn = self.ui_setting.enableExperimentscheckBox.isChecked()
            QMessageBox.information(self, "Setting", "Functionnal Setting Coming Later")

        self.ui_setting.settingsOptions.accepted.connect(applyButtonCommand)

        comingSoonMsgBox = lambda : QMessageBox().information(self, "Setting", "Not Implemented Yet!")

        self.ui_setting.settingsOptions.helpRequested.connect(comingSoonMsgBox)