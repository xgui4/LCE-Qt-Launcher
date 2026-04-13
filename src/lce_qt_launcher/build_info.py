from PySide6.QtCore import qVersion
from importlib.metadata import PackageNotFoundError, metadata, version
from importlib.metadata._meta import PackageMetadata

from platformdirs import PlatformDirs

from lce_qt_launcher.managers.system_manager import SystemManager
import lce_qt_launcher.views.term_service as term_service

from lce_qt_launcher import (
    _FALLBACK_APP_NAME,
    _FALLBACK_VERSION_NUMBER,
    _FALLBACK_GIT_REPO_URL,
    _FALLBACK_LICENSE,
    _FALLBACK_LICENSE_LINK,
    _VERSION_TYPE,
    _INSTANCE_EXTENSION
)

class BuildInfo:
    def __init__(self):
        try:
            app_metadata: PackageMetadata = metadata("LCE-Qt-Launcher")

            version_metadata: str = version("LCE-Qt-Launcher")
            app_name_metadata: str = app_metadata["Name"]
            repo_url_metadata: str = app_metadata["Repository"]
            license_url_metadata: str = app_metadata["LicenseURL"]
            license_metadata: str = app_metadata["License"]

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
            
        except PackageNotFoundError:
            term_service.print_error(f"Package not found! More info : {PackageNotFoundError.with_traceback}")
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
        self.authors = "Xgui4"
        self.dirs = PlatformDirs(self.app_name, self.authors, ensure_exists=True);
        
        self.version_type : str = _VERSION_TYPE
        self.instance_extension : str = _INSTANCE_EXTENSION