from lce_qt_launcher import Languages
from lce_qt_launcher.models.preferences import UserPref
from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.managers.instance_manager import InstanceManager, Instance
from lce_qt_launcher.views.theme import Theme
from lce_qt_launcher.utils.json_trans import JsonTrans

_default_instance : Instance = Instance()
_default_theme : Theme = Theme.MINECRAFT
_default_language : str = "en"

class AppContext():
    def __init__(self, theme = _default_theme, instance = _default_instance , lang : str = _default_language):
        self.buildInfo = BuildInfo()
        self.sys_man = self.buildInfo.system_manager
        self.userPref = UserPref(self.buildInfo)
        self.instanceMan = InstanceManager(instance, self.buildInfo)
        self.theme = theme
        self.translator = JsonTrans(lang)
        self.accesibleModeEnabled : bool = self.userPref.default_accesibility_mode
        self.devModeEnabled : bool = self.userPref.default_developper_mode
        self.showHolydayEnabled : bool = self.userPref.default_show_holyday
        self.currentLang : str = Languages.FALLBACK.value
        
        self.BACKGROUND_PIXMAP_IMG = ":/assets/background.png"
        self.ICON = ":/assets/launcher_small.png"
        self.MINECRAFT_WEBSITE = "https://minecraft.net"
        self.MINECRAFT_LCE_WEBSITE = "https://minecraftlegacy.com/"

    def updateTheme(self, theme : Theme):
        self.theme = theme
        self.userPref.set_theme_pref(theme.value)

    def updateInstance(self, instnce : Instance):
        self.instanceMan.load_instance(instnce)

    def updateLanguage(self, lang : str):
        self.currentLang = lang
        self.translator.load_lang(lang)