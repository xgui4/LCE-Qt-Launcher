from importlib.metadata import PackageNotFoundError, metadata, version
from importlib.metadata._meta import PackageMetadata

from PySide6.QtCore import qVersion

from lce_qt_launcher import (
    AUTHORS,
    FALLBACK_APP_NAME,
    FALLBACK_GIT_REPO_URL,
    FALLBACK_LICENSE,
    FALLBACK_LICENSE_LINK,
    FALLBACK_VERSION_NUMBER,
    INSTANCE_EXTENSION,
    VERSION_TYPE,
)
import lce_qt_launcher.views.term_service as term_service

class BuildInfo:
    """Application Information and Metadata Information"""
    def __init__(self) -> None:
        self.version : str = FALLBACK_VERSION_NUMBER
        self.app_name: str = FALLBACK_APP_NAME
        self.git_repo_url: str = FALLBACK_GIT_REPO_URL 
        self.license_link: str = FALLBACK_LICENSE_LINK 
        self.license : str = FALLBACK_LICENSE 
        try:
            app_metadata: PackageMetadata = metadata("LCE-Qt-Launcher")

            version_metadata: str = version("LCE-Qt-Launcher")
            app_name_metadata: str = app_metadata["Name"]
            repo_url_metadata: str = app_metadata["Repository"]
            license_url_metadata: str = app_metadata["LicenseURL"]
            license_metadata: str = app_metadata["License"]

            if version_metadata:
                self.version = version_metadata
            if app_name_metadata:
                self.app_name = app_name_metadata
            if repo_url_metadata:
                self.git_repo_url = repo_url_metadata
            if license_url_metadata:
                self.license_link = license_url_metadata
            if license_metadata:
                self.license = license_metadata
            
        except PackageNotFoundError:
            term_service.print_error(f"Package not found! More info : {PackageNotFoundError.msg}")
        except RuntimeError:
            term_service.print_error(f"Metadata not found! More info : {RuntimeError.args}")

        self.qt_version : str = qVersion()
        self.authors : str = AUTHORS
        self.version_type : str = VERSION_TYPE
        self.instance_extension : str = INSTANCE_EXTENSION