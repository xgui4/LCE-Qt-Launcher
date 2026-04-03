from lce_qt_launcher.preferences import UserPref
from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.managers.instance_manager import InstanceManager, Instance
from lce_qt_launcher.gui.theme import Theme
from lce_qt_launcher.json_trans import JsonTrans

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

        self.BACKGROUND_PIXMAP_IMG = ":/assets/background.png"
        self.ICON = ":/assets/launcher_small.png"
        self.MINECRAFT_WEBSITE = "https://minecraft.net"
        self.MINECRAFT_LCE_WEBSITE = "https://minecraftlegacy.com/"

    def updateTheme(self, theme : Theme):
        self.theme = theme

    def updateInstance(self, instnce : Instance):
        self.instanceMan.load_instance(instnce)

    def updateLanguage(self, lang : str):
        self.translator.load_lang(lang)