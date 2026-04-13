from __future__ import annotations 
from typing import TYPE_CHECKING

import os

if TYPE_CHECKING:
    from lce_qt_launcher.app_context import AppContext

from pathlib import Path

def get_source_dir() -> str:
    if "__compiled__" in globals():
        return Path(os.path.dirname(os.path.abspath(__file__)))
    else:
        dir: Path = Path(os.path.dirname(os.path.abspath(__file__)))
        return str(dir.parent.parent)

def get_project_root_dir() -> str:
    if "__compiled__" in globals():
        return Path(os.path.dirname(os.path.abspath(__file__)))
    else:
        dir: Path = Path(os.path.dirname(os.path.abspath(__file__)))
        return str(dir.parent.parent.parent)

def get_locales_dir() -> str:
    return os.path.join(get_project_root_dir(),"assets", "languages")

def get_assets_dir() -> str:
    return os.path.join(get_project_root_dir(), "assets")

def get_user_app_data_dir(appContext : AppContext) -> str:
    dirs = appContext.buildInfo.dirs
    dirs.user_data_dir()

def get_user_app_config_dir(appContext : AppContext) -> str:
    dirs = appContext.buildInfo.dirs
    dirs.user_config_dir()

def get_site_app_data_dir(appContext : AppContext) -> str:
    dirs = appContext.buildInfo.dirs
    dirs.site_data_dir()

def get_site_app_config_dir(appContext : AppContext) -> str:
    dirs = appContext.buildInfo.dirs
    dirs.site_config_dir()

def get_user_app_cache_dir(appContext : AppContext) -> str:
    dirs = appContext.buildInfo.dirs
    dirs.user_cache_dir()

def get_user_app_log_dir(appContext : AppContext) -> str:
    dirs = appContext.buildInfo.dirs
    dirs.user_log_dir()

def get_user_doc_folder(appContext : AppContext) -> str:
    dirs = appContext.buildInfo.dirs
    dirs.user_documents_dir()

def get_user_download_folder(appContext : AppContext) -> str:
    dirs = appContext.buildInfo.dirs
    dirs.user_download_dir()