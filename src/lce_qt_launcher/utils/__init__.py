from __future__ import annotations 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lce_qt_launcher.app_context import AppContext

from platformdirs import PlatformDirs
from pathlib import Path

import os
import platformdirs

def get_source_dir() -> str:
    if "__compiled__" in globals():
        return os.path.dirname(os.path.abspath(__file__))
    else:
        dir: Path = Path(os.path.dirname(os.path.abspath(__file__)))
        return str(dir.parent.parent)

def get_project_root_dir() -> str:
    if "__compiled__" in globals():
        return os.path.dirname(os.path.abspath(__file__))
    else:
        dir: Path = Path(os.path.dirname(os.path.abspath(__file__)))
        return str(dir.parent.parent.parent)

def get_locales_dir() -> str:
    return os.path.join(get_project_root_dir(),"assets", "languages")

def get_assets_dir() -> str:
    return os.path.join(get_project_root_dir(), "assets")

def get_user_app_data_dir(appContext : AppContext) -> str:
    dirs: PlatformDirs = appContext.buildInfo.dirs
    return dirs.user_data_dir

def get_user_app_config_dir(appContext : AppContext) -> str:
    dirs: PlatformDirs = appContext.buildInfo.dirs
    return dirs.user_config_dir

def get_site_app_data_dir(appContext : AppContext) -> str:
    dirs: PlatformDirs = appContext.buildInfo.dirs
    return dirs.site_data_dir

def get_site_app_config_dir(appContext : AppContext) -> str:
    dirs: PlatformDirs = appContext.buildInfo.dirs
    return dirs.site_config_dir

def get_user_app_cache_dir(appContext : AppContext) -> str:
    dirs: PlatformDirs = appContext.buildInfo.dirs
    return dirs.user_cache_dir

def get_user_app_log_dir(appContext : AppContext) -> str:
    dirs: PlatformDirs = appContext.buildInfo.dirs
    return dirs.user_log_dir

def get_user_doc_folder() -> str:
    return platformdirs.user_documents_dir()

def get_user_download_folder() -> str:
    return platformdirs.user_downloads_dir()