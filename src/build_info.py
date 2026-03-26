from src.system_manager import SystemManager

import src.term_service as term_service

import importlib.metadata

from PySide6.QtCore import qVersion
from importlib.metadata._meta import PackageMetadata

_FALLBACK_APP_NAME = "Minecraft LCE QT Launcher"
_FALLBACK_VERSION_NUMBER  = "0.0.1"
_FALLBACK_LICENSE = "GPLv3"
_FALLBACK_LICENSE_LINK = "https://www.gnu.org/licenses/gpl-3.0"
_FALLBACK_GIT_REPO_URL = "https://github.com/xgui4/LCE-QT-Launcher"

_VERSION_TYPE = "pre-alpha"
_INSTANCE_EXTENSION = ".lce_inst"

class BuildInfo:
    def __init__(self):
        try:
            metadata: PackageMetadata = importlib.metadata.metadata("LCE-Qt-Launcher")

            version_metadata: str = importlib.metadata.version("LCE-Qt-Launcher")
            app_name_metadata: str = metadata["Name"]
            repo_url_metadata: str = metadata["Repository"]
            license_url_metadata: str = metadata["LicenseURL"]
            license_metadata: str = metadata["License"]

            if version_metadata:
                self.version : str  = version_metadata
            else:
                self.version : str = _FALLBACK_VERSION_NUMBER
            if app_name_metadata:
                self.app_name: str = app_name_metadata
            else:
                self.app_name = _FALLBACK_APP_NAME
            if repo_url_metadata:
                self.git_repo_url: str = repo_url_metadata
            else:
                self.git_repo_url : str = _FALLBACK_GIT_REPO_URL 
            if license_url_metadata:
                self.license_link: str = license_url_metadata
            else:
                self.license_link : str = _FALLBACK_LICENSE_LINK 
            if license_metadata:
                self.license: str = license_metadata
            else:
                self.license : str = _FALLBACK_LICENSE 
            
        except importlib.metadata.PackageNotFoundError:
            term_service.print_error(f"Package not found! More info : {importlib.metadata.PackageNotFoundError.with_traceback}")
            self.version : str = _FALLBACK_VERSION_NUMBER
            self.app_name = _FALLBACK_APP_NAME
            self.git_repo_url : str = _FALLBACK_GIT_REPO_URL 
            self.license_link : str = _FALLBACK_LICENSE_LINK 
            self.license  : str = _FALLBACK_LICENSE 
        except RuntimeError:
            term_service.print_error(f"Metadata not found! More info : {RuntimeError.with_traceback}")
            self.version : str = _FALLBACK_VERSION_NUMBER
            self.app_name = _FALLBACK_APP_NAME
            self.git_repo_url : str = _FALLBACK_GIT_REPO_URL 
            self.license_link : str = _FALLBACK_LICENSE_LINK 
            self.license  : str = _FALLBACK_LICENSE 

        self.qt_version : str = qVersion()
        self.system_manager : SystemManager = SystemManager()
        
        self.version_type : str = _VERSION_TYPE
        self.instance_extension : str = _INSTANCE_EXTENSION