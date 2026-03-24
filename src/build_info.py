from PySide6.QtCore import qVersion

from system_manager import SystemManager

import term_service

from pathlib import Path

import os
import subprocess
from datetime import date
import importlib.metadata

_APP_NAME = "Minecraft LCE QT Launcher"
_VERSION_NUMBER  = "0.0.1"
_VERSION_TYPE = "dev"
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
    
try:
    metadata = importlib.metadata.metadata("LCE-Qt-Launcher")

    version_metadata = importlib.metadata.version("LCE-Qt-Launcher")
    app_name_metadata = metadata["Name"]
    repo_url_metadata = metadata["Repository"]
    license_url_metadata = metadata["LicenseURL"]
    license_metadata = metadata["License"]

    if version_metadata is not "" or None:
        _VERSION_NUMBER = version_metadata
    if app_name_metadata is not "" or None:
        _APP_NAME = app_name_metadata
    if repo_url_metadata is not "" or None:
        _GIT_REPO_URL = repo_url_metadata
    if license_url_metadata is not "" or None:
        _LICENSE_LINK = license_url_metadata
    if license_metadata is not "" or None:
        _LICENSE = license_metadata
except importlib.metadata.PackageNotFoundError:
    pass
except RuntimeError:
    term_service.print_error(f"Metadata not found! More info : {RuntimeError.with_traceback}")

class BuildInfo:
    def __init__(self):
        self.version : str =  f"{_VERSION_TYPE} { _VERSION_NUMBER}-{get_version_info()}"
        self.app_name : str = _APP_NAME
        self.version_type : str = _VERSION_TYPE
        self.license : str = "GPLv3" # temporaliy masure until I  find the solution to why the one from metadata is "None"
        self.license_link: str = _LICENSE_LINK
        self.git_repo_url = _GIT_REPO_URL 
        self.qt_version : str = qVersion()
        self.system_manager : SystemManager = SystemManager()
        self.instance_extension = _INSTANCE_EXTENSION
