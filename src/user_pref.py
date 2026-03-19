from PySide6.QtCore import QSettings

from theme import Theme

class UserPref (QSettings):
    def __init__(self):
        super().__init__(QSettings.NativeFormat, QSettings.UserScope, "Xgui4", "LCE-QT-Laucher")

    def set_theme_pref(self, theme : str):
        super().setValue("customisation/theme", theme)
        super().sync()

    def get_theme_pref(self) -> str:
        return self.value("ustomisation/theme", Theme.MINECRAFT);
    
    def generate_default_config(self):
        super().setValue("customisation/theme", Theme.MINECRAFT)
        super().sync()
