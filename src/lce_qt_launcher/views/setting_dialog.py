from PySide6.QtWidgets import QDialog, QWidget, QMessageBox
from PySide6.QtCore import Qt

from lce_qt_launcher.app_context import AppContext
import lce_qt_launcher.models.theme as theme
from lce_qt_launcher.ui_settingDialog import Ui_settingDialog


class SettingDialog(QDialog):
    """_summary_ The Setting Dialog"""

    def __init__(
        self, parent: QWidget, ui_setting: Ui_settingDialog, appContext: AppContext
    ) -> None:
        super().__init__()
        self.setting_dialog: QDialog = QDialog(parent)
        self.ui_setting: Ui_settingDialog = ui_setting
        self.ui_setting.setupUi(self.setting_dialog)  # pyright: ignore[reportUnknownMemberType]
        self.setting_dialog.show()
        self.appContext = appContext
        self.userPref = appContext.userPref

        self.ui_setting.settingsOptions.accepted.connect(self.applyButtonCommand)

        comingSoonMsgBox = lambda: QMessageBox().information(
            self, "Setting", "Not Implemented Yet!"
        )

        self.ui_setting.settingsOptions.helpRequested.connect(comingSoonMsgBox)

        self.ui_setting.accesibilitycheckBox.setChecked(
            bool(self.userPref.get_accesible_mode())
        )
        self.ui_setting.developperModeDheckBox.setChecked(
            bool(self.userPref.get_developper_mode())
        )
        self.ui_setting.holydayDheckBox.setChecked(
            bool(self.userPref.get_show_holiday())
        )
        self.ui_setting.enableExperimentscheckBox.setChecked(
            bool(self.userPref.get_experimental_mode())
        )

        self.ui_setting.languagesComboBox.setEditText(self.userPref.get_language_pref())
        self.ui_setting.themesComboBox.setEditText(self.userPref.get_theme_pref())

    def applyButtonCommand(self):
        isDevelopperModeEnabled = self.ui_setting.developperModeDheckBox.isChecked()
        isAccesbilityModeEnabled = self.ui_setting.accesibilitycheckBox.isChecked()
        isHolidayEnabled = self.ui_setting.holydayDheckBox.isChecked()
        themeSelectedIndex = self.ui_setting.themesComboBox.currentIndex()
        languageSelectedIndex = self.ui_setting.languagesComboBox.currentData()
        isExperimentsOn = self.ui_setting.enableExperimentscheckBox.isChecked()
        QMessageBox.information(self, "Setting", "Functionnal Setting Coming Later")

        self.userPref.set_accesible_mode(isAccesbilityModeEnabled)
        self.userPref.set_developper_mode(isDevelopperModeEnabled)
        self.userPref.set_show_holiday(isHolidayEnabled)
        self.userPref.set_theme_pref(
            str(theme.from_entity_to_strTheme(theme.ThemeEntity(themeSelectedIndex)))
        )
        self.userPref.set_language_pref(languageSelectedIndex)
        self.userPref.set_experimental_mode(isExperimentsOn)
