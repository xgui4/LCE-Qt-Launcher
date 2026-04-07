from PySide6.QtCore import QSettings

from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.gui.theme import Theme

import lce_qt_launcher.utils as utils

_THEME_OPTION : str = "customisation/theme"
_INSTANCE_PATH_OPTION : str = "preferences/default_path"
_LANGUAGE_OPTION : str = "preferences/languages"

class UserPref (QSettings):
    def __init__(self, build_info : BuildInfo):
        super().__init__(QSettings.NativeFormat, QSettings.UserScope, "Xgui4", build_info.app_name)
        self.default_theme = Theme.MINECRAFT
        self.default_instance_path = utils.get_source_dir()
        self.defaul_language = "en"

    def set_theme_pref(self, theme : str):
        super().setValue(_THEME_OPTION, theme)
        super().sync()

    def get_theme_pref(self) -> str:
        return self.value(_THEME_OPTION, self.default_theme)

    def set_language_pref(self, language : str):
        super().setValue(_LANGUAGE_OPTION, language)
        super().sync()

    def get_language_pref(self) -> str:
        return self.value(_LANGUAGE_OPTION, self.default_theme)
    
    def set_instance_path_pref(self, instance_path : str):
        super().setValue(_INSTANCE_PATH_OPTION, instance_path)
        super().sync()

    def get_instance_path(self) -> str:
        return self.value(_INSTANCE_PATH_OPTION, self.default_instance_path)
    
    def generate_default_config(self):
        super().setValue(_THEME_OPTION, self.default_theme)
        super().setValue(_INSTANCE_PATH_OPTION, self.default_instance_path)
        super().sync()
