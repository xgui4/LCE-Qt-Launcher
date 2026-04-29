#TODO : Need to finish some python docstring

from PySide6.QtCore import QSettings

from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.views.theme import Theme

_THEME_OPTION : str = "customisation/theme"
_INSTANCE_PATH_OPTION : str = "preferences/default_path"
_LANGUAGE_OPTION : str = "preferences/languages"
_SHOW_HOLIDAY_OPTION : str = "views/show_hoyday_enabled"
_DEVELOPPER_MODE_OPTION  : str = "developper/dev_mode_enabled"
_ACCESIBLE_MODE_OPTION  : str = "accesibility/accesibility_mode_enabled"

class UserPref (QSettings): 
    """_summary_ The UserPref managed by QtSettings

    Args:
        QSettings (_type_): _description_  : Inherit QtSettings
    """
    def __init__(self, build_info : BuildInfo) -> None:
        super().__init__(QSettings.Format.IniFormat, QSettings.Scope.UserScope, "Xgui4", build_info.app_name) 
        self.default_theme : Theme = Theme.MINECRAFT
        self.default_instance_path : str = "~/.local/share/lce_qt_launcher/default"
        self.default_language : str  = "en"
        self.default_show_holiday : bool = True
        self.default_accesibility_mode : bool = False
        self.default_developper_mode : bool = False

    def set_theme_pref(self, theme : str) -> None:
        """_summary_ Theme Setter

        Args:
            theme (str): _description_ the theme to set
        """
        super().setValue(_THEME_OPTION, theme)
        super().sync()
    def get_theme_pref(self) -> str:
        """_summary_ Theme Getter"""
        return str(self.value(_THEME_OPTION, self.default_theme, type=str))

    def set_language_pref(self, language : str) -> None:
        """_summary_ Language Setter

        Args:
            language (str): _description_ the language to set
        """
        super().setValue(_LANGUAGE_OPTION, language)
        super().sync()
    def get_language_pref(self) -> str:
        """_summary_ Language Getter"""
        return str(self.value(_LANGUAGE_OPTION, self.default_theme, type=str))
    
    def set_instance_path_pref(self, instance_path : str) -> None:
        """_summary_ Default Instance Path Setter

        Args:
            instance_path (str): _description_ the Default Instance Path to set
        """
        super().setValue(_INSTANCE_PATH_OPTION, instance_path)
        super().sync()
    def get_instance_path(self) -> str:
        """_summary_ Default Instance Path Getter
        """
        return str(self.value(_INSTANCE_PATH_OPTION, self.default_instance_path, type=str))
    
    def set_show_holiday(self, show_holiday_bool : bool) -> None:
        """_summary_  Show Holiday Toggle Setter
        """
        super().setValue(_SHOW_HOLIDAY_OPTION, show_holiday_bool)
        super().sync()
    def get_show_holiday(self) -> str:
        """_summary_ Show Holiday Toggle Getter

        Returns:
            str: _description_ show holyday preference
        """
        return str(self.value(_SHOW_HOLIDAY_OPTION, self.default_show_holiday, type=str))

    def set_accesible_mode(self, accesbility_mode_bool : bool) -> None:
        """_summary_ Accessiblty Mode Sette 

        Args:
            accesbility_mode_bool (bool): _description_ #TODO DOCSTRINGS
        """
        super().setValue(_ACCESIBLE_MODE_OPTION, accesbility_mode_bool)
        super().sync()
    def get_accesible_mode(self) -> str:
        """_summary_ Accesiblity Toggle Getter

        Returns:
            str: _description_ 
        """
        return str(self.value(_ACCESIBLE_MODE_OPTION, self.default_accesibility_mode, type=str))
    
    def set_developper_mode(self, developper_mode_bool : bool) -> None:
        """_summary_ Dev Mode Setter

        Args:
            developper_mode_bool (bool): _description_ #TODO DOCSTRINGS
        """
        super().setValue(_DEVELOPPER_MODE_OPTION, developper_mode_bool)
        super().sync()
    def get_developper_mode(self) -> str:
        """_summary_ Dev Mode Getter

        Returns:
            str: _description_ #TODO DOCSTRINGS
        """
        return str(self.value(_DEVELOPPER_MODE_OPTION, self.default_developper_mode, type=str))
    
    def generate_default_config(self) -> None:
        """_summary_ Generate the default config for the users
        """
        self.set_theme_pref(self.default_theme)
        self.set_language_pref(self.default_language)
        self.set_instance_path_pref(self.default_instance_path)
        self.set_show_holiday(self.default_show_holiday)
        self.set_accesible_mode(self.default_accesibility_mode)
        self.set_accesible_mode(self.default_developper_mode)
        super().sync()
