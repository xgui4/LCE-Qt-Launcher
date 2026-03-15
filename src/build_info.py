from PySide6.QtCore import qVersion

from system_manager import SystemManager

from pathlib import Path

import os

import subprocess

_APP_NAME = "Minecraft LCE QT Launcher"
_VERSION_TYPE = "pre-alpha"
_LICENSE = "GPLv3"
_LICENSE_LINK = "https://www.gnu.org/licenses/gpl-3.0.en.html"
_GIT_REPO_URL = "https://github.com/xgui4/LCE_QT_Launcher"

def get_source_dir() -> str:
    return os.path.abspath(os.path.dirname(__file__))

def get_project_root_dir() -> str:
    dir: Path = Path(get_source_dir())
    return str(dir.parent)

def get_locales_dir() -> str:
    return os.path.join(get_project_root_dir(),"assets", "languages")

def get_assets_dir() -> str:
    return os.path.join(get_project_root_dir(), "assets")


PROJET_ROOT_DIR = get_project_root_dir()
LOCALES_FOLDER = get_locales_dir()
ASSETS_FOLDER = get_assets_dir()

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
