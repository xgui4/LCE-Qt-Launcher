from PySide6.QtCore import QSettings

from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.views.theme import Theme

import lce_qt_launcher.utils as utils

_THEME_OPTION : str = "customisation/theme"
_INSTANCE_PATH_OPTION : str = "preferences/default_path"
_LANGUAGE_OPTION : str = "preferences/languages"
_SHOW_HOLYDAY_OPTION : str = "views/show_hoyday_enabled"
_DEVELOPPER_MODE_OPTION  : str = "developper/dev_mode_enabled"
_ACCESIBLE_MODE_OPTION  : str = "accesibility/accesibility_mode_enabled"

class UserPref (QSettings):
    def __init__(self, build_info : BuildInfo):
        super().__init__(QSettings.NativeFormat, QSettings.UserScope, "Xgui4", build_info.app_name)
        self.default_theme : Theme = Theme.MINECRAFT
        self.default_instance_path : str = "~/.local/share/lce_qt_launcher/default"
        self.default_language : str  = "en"
        self.default_show_holyday : bool = True
        self.default_accesibility_mode : bool = False
        self.default_developper_mode : bool = False

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
    
    def set_show_holyday(self, show_holyday_bool : bool):
        super().setValue(_SHOW_HOLYDAY_OPTION, show_holyday_bool)
        super().sync()
    def get_show_holyday(self) -> str:
        return self.value(_SHOW_HOLYDAY_OPTION, self.default_show_holyday)

    def set_accesible_mode(self, accesbility_mode_bool : bool):
        super().setValue(_ACCESIBLE_MODE_OPTION, accesbility_mode_bool)
        super().sync()
    def get_accesible_mode(self) -> str:
        return self.value(_ACCESIBLE_MODE_OPTION, self.default_accesibility_mode)
    
    def set_developper_mode(self, developper_mode_bool : bool):
        super().setValue(_DEVELOPPER_MODE_OPTION, developper_mode_bool)
        super().sync()
    def get_developper_mode(self) -> str:
        return self.value(_DEVELOPPER_MODE_OPTION, self.default_developper_mode)
    
    def generate_default_config(self):
        self.set_theme_pref(self.default_theme)
        self.set_language_pref(self.default_language)
        self.set_instance_path_pref(self.default_instance_path)
        self.set_show_holyday(self.default_show_holyday)
        self.set_accesible_mode(self.default_accesibility_mode)
        self.set_accesible_mode(self.default_developper_mode)
        super().sync()
