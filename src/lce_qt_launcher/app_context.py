from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lce_qt_launcher.models.app_data import AppData

from lce_qt_launcher.managers.system_manager import SystemManager
from lce_qt_launcher.models.pref import UserPref
from lce_qt_launcher.managers.instance_manager import InstanceManager, Instance
from lce_qt_launcher.models.theme import StrTheme
from lce_qt_launcher.utils.json_trans import JsonTrans, Languages

import os

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

        self.accesibleModeEnabled: bool = self.userPref.defaultAccesibilityMode
        self.devModeEnabled: bool = self.userPref.defaultDevelopperMode
        self.experimentModeEnabled: bool = self.userPref.defaultExperimentMode
        self.showHolidayEnabled: bool = self.userPref.defaultShowHoliday
        self.instancePath: str = self.expand_path(self.userPref.defaultInstancePath, appData)
        self.username: str = self.userPref.defaultUsername

        self.BACKGROUND_PIXMAP_IMG: str = ":/assets/background.png"
        self.ICON: str = ":/assets/launcher_small.png"
        self.MINECRAFT_WEBSITE: str = "https://minecraft.net"
        self.MINECRAFT_LCE_WEBSITE: str = "https://minecraftlegacy.com/"

    def expand_path(self, path : str, appData : AppData) -> str:
        return path.replace("{appInstancePath}", os.path.join(appData.appDataDirs[0]))

    def updateAppUILang(self) -> None:
        """_summary_  update the language

        Args:
            lang (str): _description_
        """
        self.translator.load_lang(self.selectedLang)
