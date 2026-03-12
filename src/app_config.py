from PySide6.QtCore import qVersion

import subprocess

from system_manager import SystemManager

GITHUB_RELEASE_STR = "/releases/download/"

LAUNCHER_REPO = "https://github.com/xgui4/LCE_QT_Launcher"


#LAUNCHER_STRING : str = config.get__instance_url() + \
#                  GITHUB_RELEASE_STR + \
#                  config.get_instance_version() + "/" + \
#                  config.get_instance_archive()

def get_git_branch():
    try:
        return subprocess.run(
        ["git", "rev-parse", "--aabbrev-ref", "HEAD"],
        capture_output=True,
        text=True,
        check=True
        )
    except:
        print("Not a developpement version")
        return ""


class AppConfig:
    def __init__(self):
        self.version : str = get_git_branch(),
        self.name : str = "Minecraft LCE QT Launcher",
        self.version_type : str = "pre-alpha",
        self.qt_version : str = qVersion(),
        self.system_manager : SystemManager = SystemManager()
