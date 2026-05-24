from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lce_qt_launcher.models.app_data import AppData

from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.models.pref import UserPref
from lce_qt_launcher.managers.instance_manager import InstanceManager, Instance
from lce_qt_launcher.models.theme import StrTheme
from lce_qt_launcher.utils.json_trans import JsonTrans, Languages

_default_instance: Instance = Instance()
_default_theme: StrTheme = StrTheme.MINECRAFT
_default_language: str = "en"


class AppContext:
    """_summary_ The App Main Context"""

    def __init__(
        self,
        appData: AppData,
        theme: StrTheme = _default_theme,
        instance: Instance = _default_instance,
        lang: str = _default_language,
    ) -> None:
        self.sys_man: SystemManager = SystemManager()
        self.userPref: UserPref = UserPref()
        self.instanceMan: InstanceManager = InstanceManager(instance, self)
        self.theme: StrTheme = theme
        self.translator: JsonTrans = JsonTrans(appData, lang)
        self.selectedLang: str = Languages.FALLBACK.value

        self.accesibleModeEnabled: bool = self.userPref.default_accesibility_mode
        self.devModeEnabled: bool = self.userPref.default_developper_mode
        self.experimentModeEnabled: bool = self.userPref.default_experiment_mode
        self.showHolidayEnabled: bool = self.userPref.default_show_holiday
        self.defaultInstancePath: str = self.userPref.default_instance_path
        self.defaultUsername: str = self.userPref.default_username

        self.BACKGROUND_PIXMAP_IMG: str = ":/assets/background.png"
        self.ICON: str = ":/assets/launcher_small.png"
        self.MINECRAFT_WEBSITE: str = "https://minecraft.net"
        self.MINECRAFT_LCE_WEBSITE: str = "https://minecraftlegacy.com/"

    def updateAppUILang(self) -> None:
        """_summary_  update the language

        Args:
            lang (str): _description_
        """
        self.translator.load_lang(self.selectedLang)
