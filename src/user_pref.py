from PySide6.QtCore import QSettings

from theme import Theme

class UserPref (QSettings):

    _THEME_OPTION = "customisation/theme"
    _DEFAULT_THEME = Theme.MINECRAFT

    def __init__(self):
        super().__init__(QSettings.NativeFormat, QSettings.UserScope, "Xgui4", "LCE-QT-Laucher")

    def set_theme_pref(self, theme : str):
        super().setValue(self._THEME_OPTION, theme)
        super().sync()

    def get_theme_pref(self) -> str:
        return self.value(self._THEME_OPTION, self._DEFAULT_THEME);
    
    def generate_default_config(self):
        super().setValue(self._THEME_OPTION, self._DEFAULT_THEME)
        super().sync()
