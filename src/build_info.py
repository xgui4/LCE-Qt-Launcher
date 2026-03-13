from PySide6.QtCore import qVersion

from system_manager import SystemManager

import subprocess

_APP_NAME = "Minecraft LCE QT Launcher"
_VERSION_TYPE = "pre-alpha"
_LICENSE = "GPLv3"
_LICENSE_LINK = "https://www.gnu.org/licenses/gpl-3.0.en.html"
_GIT_REPO_URL = "https://github.com/xgui4/LCE_QT_Launcher"

def get_git_info():
    try:
        # Récupère le nom de la branche
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], 
            text=True
        ).strip()
        
        # Récupère le hash court
        commit_hash = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], 
            text=True
        ).strip()
        
        return f"{branch}-{commit_hash}"
    except Exception:
        print("Not a development version")
        return ""


class BuildInfo:
    def __init__(self):
        self.version : str = "0.0.1" + "-" + get_git_info() 
        self.app_name : str = _APP_NAME
        self.version_type : str = _VERSION_TYPE
        self.license : str = _LICENSE
        self.license_link: str = _LICENSE_LINK
        self.git_repo_url = _GIT_REPO_URL 
        self.qt_version : str = qVersion()
        self.system_manager : SystemManager = SystemManager()
