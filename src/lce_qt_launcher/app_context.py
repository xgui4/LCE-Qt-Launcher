from __future__ import annotations 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lce_qt_launcher.models.app_data import AppData

from lce_qt_launcher import Languages
from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.models.preferences import UserPref
from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.managers.instance_manager import InstanceManager, Instance
from lce_qt_launcher.views.theme import Theme
from lce_qt_launcher.utils.json_trans import JsonTrans

_default_instance : Instance = Instance()
_default_theme : Theme = Theme.MINECRAFT
_default_language : str = "en"

class AppContext():
    """_summary_ The App Main Context
    """
    def __init__(self, 
                appData: AppData,
                theme : Theme = _default_theme, 
                instance : Instance = _default_instance, 
                lang : str = _default_language) -> None:
        self.buildInfo: BuildInfo = BuildInfo()
        self.sys_man: SystemManager = SystemManager()
        self.userPref: UserPref = UserPref(self.buildInfo)
        self.instanceMan: InstanceManager = InstanceManager(instance, self.buildInfo, self)
        self.theme: Theme = theme
        self.translator: JsonTrans = JsonTrans(appData, lang)
        self.accesibleModeEnabled : bool = self.userPref.default_accesibility_mode
        self.devModeEnabled : bool = self.userPref.default_developper_mode
        self.showHolidayEnabled : bool = self.userPref.default_show_holiday
        self.currentLang : str = Languages.FALLBACK.value
        
        self.BACKGROUND_PIXMAP_IMG : str = ":/assets/background.png"
        self.ICON : str = ":/assets/launcher_small.png"
        self.MINECRAFT_WEBSITE : str = "https://minecraft.net"
        self.MINECRAFT_LCE_WEBSITE : str = "https://minecraftlegacy.com/"

    def updateTheme(self, theme : Theme) -> None:
        """_summary_ Update the theme

        Args:
            theme (Theme): _description_ the theme (enum) to update
        """
        self.theme = theme
        self.userPref.set_theme_pref(theme.value)

    def updateInstance(self, instance : Instance) -> None:
        """_summary_ #TODO : TBW

        Args:
            instance (Instance): _description_
        """
        self.instanceMan.instance = instance

    def updateLanguage(self, lang : str) -> None:
        """_summary_  update the language 

        Args:
            lang (str): _description_
        """
        self.currentLang = lang
        self.translator.load_lang(lang)
        
    def updateShowHolidayStatus(self, request : str)  -> None:
        """_summary_ Update the show holiday status via boolean string "request"

        Args:
            request (str): _description_ the boolean string request to update the show holiday option. 
        """
        if request == "true":
            self.showHolidayEnabled = True
        else:
            self.showHolidayEnabled = False
            
    def updateSetDevMoodeStatus(self, request : str)  -> None:
        """_summary_ Update the dev mode status via boolean string "request"

        Args:
            request (str): _description_ the boolean string request to update the developper mode option. 
        """
        if request == "true":
            self.devModeEnabled = True
        else:
            self.devModeEnabled = False
            
    def updateSetAccesbilityMoodeStatus(self, request : str)  -> None:
        """_summary_ Update the dev mode status via boolean string "request"

        Args:
            request (str): _description_ the boolean string request to update the developper mode option. 
        """
        if request == "true":
            self.accesibleModeEnabled = True
        else:
            self.accesibleModeEnabled = False