#FIXME make this module more python like with attributes instead of getter and setter

from PySide6.QtCore import QSettings

from lce_qt_launcher.models.theme import StrTheme
from lce_qt_launcher import app_name_str

_THEME_OPTION: str = "customisation/theme"
_INSTANCE_PATH_OPTION: str = "preferences/default_path"
_LANGUAGE_OPTION: str = "preferences/language"
_SHOW_HOLIDAY_OPTION: str = "views/show_hoyday_enabled"
_DEVELOPPER_MODE_OPTION: str = "developper/dev_mode_enabled"
_ACCESIBLE_MODE_OPTION: str = "accesibility/accesibility_mode_enabled"
_EXPERIMENTAL_MODE_OPTION: str = "preferences/experimental_mode_enabled"
_USERNAME_OPTION: str = "user_profile/username"


class UserPref(QSettings):
    """_summary_ The UserPref managed by QtSettings

    Args:
        QSettings (_type_): _description_  : Inherit QtSettings
    """

    def __init__(self) -> None:
        super().__init__(
            QSettings.Format.IniFormat,
            QSettings.Scope.UserScope,
            "Xgui4",
            app_name_str,
        )
        self.default_theme: StrTheme = StrTheme.MINECRAFT
        self.default_instance_path: str = "{appData}/instances"
        self.default_language: str = "en"
        self.default_show_holiday: bool = True
        self.default_accesibility_mode: bool = False
        self.default_developper_mode: bool = False
        self.default_experiment_mode: bool = False
        self.default_username: str = "Steve"

    def set_theme_pref(self, theme: str) -> None:
        super().setValue(_THEME_OPTION, theme)
        super().sync()

    def get_theme_pref(self) -> str:
        return str(self.value(_THEME_OPTION, self.default_theme, type=str))

    def set_language_pref(self, language: str) -> None:
        super().setValue(_LANGUAGE_OPTION, language)
        super().sync()

    def get_language_pref(self) -> str:
        return str(self.value(_LANGUAGE_OPTION, self.default_theme, type=str))

    def set_instance_path_pref(self, instance_path: str) -> None:
        super().setValue(_INSTANCE_PATH_OPTION, instance_path)
        super().sync()

    def get_instance_path_pref(self) -> str:
        return str(
            self.value(_INSTANCE_PATH_OPTION, self.default_instance_path, type=str)
        )

    def set_show_holiday_pref(self, show_holiday_bool: bool) -> None:
        super().setValue(_SHOW_HOLIDAY_OPTION, show_holiday_bool)
        super().sync()

    def get_show_holiday_pref(self) -> str:
        return str(
            self.value(_SHOW_HOLIDAY_OPTION, self.default_show_holiday, type=str)
        )

    def set_accesible_mode_pref(self, accesbility_mode_bool: bool) -> None:
        super().setValue(_ACCESIBLE_MODE_OPTION, accesbility_mode_bool)
        super().sync()

    def get_accesible_mode_pref(self) -> str:
        return str(
            self.value(_ACCESIBLE_MODE_OPTION, self.default_accesibility_mode, type=str)
        )

    def set_developper_mode_pref(self, developper_mode_bool: bool) -> None:
        super().setValue(_DEVELOPPER_MODE_OPTION, developper_mode_bool)
        super().sync()

    def get_developper_mode_pref(self) -> str:
        return str(
            self.value(_DEVELOPPER_MODE_OPTION, self.default_developper_mode, type=str)
        )

    def set_experimental_mode_pref(self, experimental_mode_bool: bool) -> None:
        super().setValue(_EXPERIMENTAL_MODE_OPTION, experimental_mode_bool)
        super().sync()

    def get_experimental_mode_pref(self) -> str:
        return str(
            self.value(
                _EXPERIMENTAL_MODE_OPTION, self.default_experiment_mode, type=str
            )
        )

    def set_username_pref(self, new_username: str) -> None:
        super().setValue(_USERNAME_OPTION, new_username)
        super().sync()

    def get_username_pref(self) -> str:
        return str(self.value(_USERNAME_OPTION, self.default_username, type=str))

    def generate_default_config(self) -> None:
        """_summary_ Generate the default config for the users"""
        self.set_theme_pref(self.default_theme)
        self.set_language_pref(self.default_language)
        self.set_instance_path_pref(self.default_instance_path)
        self.set_show_holiday_pref(self.default_show_holiday)
        self.set_accesible_mode_pref(self.default_accesibility_mode)
        self.set_accesible_mode_pref(self.default_developper_mode)
        self.set_experimental_mode_pref(self.default_experiment_mode)
        self.set_username_pref(self.default_username)
        super().sync()
