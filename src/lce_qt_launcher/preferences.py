from PySide6.QtCore import QSettings

from lce_qt_launcher.gui.theme import Theme

_THEME_OPTION : str = "customisation/theme"

class UserPref (QSettings):
    def __init__(self):
        self.default_theme = Theme.MINECRAFT
        super().__init__(QSettings.NativeFormat, QSettings.UserScope, "Xgui4", "LCE-QT-Laucher")

    def set_theme_pref(self, theme : str):
        super().setValue(_THEME_OPTION, theme)
        super().sync()

    def get_theme_pref(self) -> str:
        return self.value(_THEME_OPTION, self.default_theme);
    
    def generate_default_config(self):
        super().setValue(_THEME_OPTION, self.default_theme)
        super().sync()
