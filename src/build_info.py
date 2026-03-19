from PySide6.QtCore import qVersion

from system_manager import SystemManager

from pathlib import Path

import os
import subprocess
from datetime import date

_APP_NAME = "Minecraft LCE QT Launcher"
_VERSION_TYPE = "nighly"
_VERSION_NUMBER  = "0.0.1"
_LICENSE = "GPLv3"
_LICENSE_LINK = "https://www.gnu.org/licenses/gpl-3.0"
_GIT_REPO_URL = "https://github.com/xgui4/LCE-QT-Launcher"
_INSTANCE_EXTENSION = ".lce_inst"

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

def get_version_info():
    try:
        date_info = date.today()

        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], 
            text=True
        ).strip()
        
        commit_hash = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], 
            text=True
        ).strip()
        
        return f"{branch}-{date_info}_{commit_hash}"
    except Exception:
        return ""

class BuildInfo:
    def __init__(self):
        self.version : str =  f"{_VERSION_TYPE} { _VERSION_NUMBER}-{get_version_info()}"
        self.app_name : str = _APP_NAME
        self.version_type : str = _VERSION_TYPE
        self.license : str = _LICENSE
        self.license_link: str = _LICENSE_LINK
        self.git_repo_url = _GIT_REPO_URL 
        self.qt_version : str = qVersion()
        self.system_manager : SystemManager = SystemManager()
        self.instance_extension = _INSTANCE_EXTENSION
