# FIXME make this module more python like with attributes instead of getter and setter

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
            app_name_str
        )
        self.defaultTheme: StrTheme = StrTheme.MINECRAFT
        self.defaultInstancePath: str = "{appInstancePath}/instances"
        self.defaultLanguage: str = "en"
        self.defaultShowHoliday: bool = True
        self.defaultAccesibilityMode: bool = False
        self.defaultDevelopperMode: bool = False
        self.defaultExperimentMode: bool = False
        self.defaultUsername: str = "Steve"

    def setThemePref(self, theme: str) -> None:
        super().setValue(_THEME_OPTION, theme)
        super().sync()

    def getThemePref(self) -> str:
        return str(self.value(_THEME_OPTION, self.defaultTheme, type=str))

    def setLanguagePref(self, language: str) -> None:
        super().setValue(_LANGUAGE_OPTION, language)
        super().sync()

    def getLanguagePref(self) -> str:
        return str(self.value(_LANGUAGE_OPTION, self.defaultTheme, type=str))

    def setInstancePathPref(self, instancePath: str) -> None:
        super().setValue(_INSTANCE_PATH_OPTION, instancePath)
        super().sync()

    def getInstancePathPref(self) -> str:
        return str(
            self.value(_INSTANCE_PATH_OPTION, self.defaultInstancePath, type=str)
        )

    def setShowHolidayPref(self, showHolidayBool: bool) -> None:
        super().setValue(_SHOW_HOLIDAY_OPTION, showHolidayBool)
        super().sync()

    def getShowHolidayPref(self) -> str:
        return str(
            self.value(_SHOW_HOLIDAY_OPTION, self.defaultShowHoliday, type=str)
        )

    def setAccesibleModePref(self, accesbilityModeBool: bool) -> None:
        super().setValue(_ACCESIBLE_MODE_OPTION, accesbilityModeBool)
        super().sync()

    def getAccesibleModePref(self) -> str:
        return str(
            self.value(_ACCESIBLE_MODE_OPTION, self.defaultAccesibilityMode, type=str)
        )

    def setDevelopperMode_pref(self, developperModeBool: bool) -> None:
        super().setValue(_DEVELOPPER_MODE_OPTION, developperModeBool)
        super().sync()

    def getDevelopperModePref(self) -> str:
        return str(
            self.value(_DEVELOPPER_MODE_OPTION, self.defaultDevelopperMode, type=str)
        )

    def setExperimentalModePref(self, experimentalModeBool: bool) -> None:
        super().setValue(_EXPERIMENTAL_MODE_OPTION, experimentalModeBool)
        super().sync()

    def getExperimentalModePref(self) -> str:
        return str(
            self.value(
                _EXPERIMENTAL_MODE_OPTION, self.defaultExperimentMode, type=str
            )
        )

    def setUsernamePref(self, newUsername: str) -> None:
        super().setValue(_USERNAME_OPTION, newUsername)
        super().sync()

    def getUsernamePref(self) -> str:
        return str(self.value(_USERNAME_OPTION, self.defaultUsername, type=str))

    def generateDefaultConfig(self) -> None:
        """_summary_ Generate the default config for the users"""
        self.setThemePref(self.defaultTheme)
        self.setLanguagePref(self.defaultLanguage)
        self.setInstancePathPref(self.defaultInstancePath)
        self.setShowHolidayPref(self.defaultShowHoliday)
        self.setAccesibleModePref(self.defaultAccesibilityMode)
        self.setAccesibleModePref(self.defaultDevelopperMode)
        self.setExperimentalModePref(self.defaultExperimentMode)
        self.setUsernamePref(self.defaultUsername)
        super().sync()
