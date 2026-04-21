from __future__ import annotations 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lce_qt_launcher.app_context import AppContext

from platformdirs import PlatformDirs

from lce_qt_launcher.managers.instance_manager import Instance

from PySide6.QtCore import QObject, Signal

from pathlib import Path

import json
import os

def _is_compiled() -> bool:
    return "__compiled__" in globals()

def _is_installed() -> bool:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return "site-packages" in current_dir or "dist-packages" in current_dir

class AppData(QObject):
    changed: Signal = Signal()
    def __init__(self, appContext : AppContext) -> None:
        super().__init__(parent = None, objectName="App Data")
        self.instsList : list[Instance] = []
        self.appContext : AppContext = appContext 
        self.sourceDir : str = self._get_source_dir()
        self.projectRootDir : str = self._get_project_root_dir()
        self.localesDir : str = self._get_locales_dir()
        self.assetsDirs : str = self._get_assets_dir()
        self.appDataDirs: tuple[str, str]  = ( self._get_user_app_data_dir(), self._get_site_app_data_dir() )
        self.appConfigDirs : tuple[str, str]  = ( self._get_user_app_config_dir(), self._get_site_app_config_dir() )
        self.appCacheDir : str =  self._get_app_cache_dir()
        self.appLogDir : str = self._get_app_log_dir()
        self.load_insts_list_into_mem()

    def load_insts_list_into_mem(self) -> None:
        """#TODO : make it so it also work on both user and system (site) dir if needed. """
        defaults_insts_dir : Path = Path(os.path.join(self.appDataDirs[0], "instances"))

        if not defaults_insts_dir.exists():
            return

        instancesLists : list[Instance] = []

        for file_path in defaults_insts_dir.iterdir():
            if file_path.is_file():
                try:
                    with open(file=file_path, mode="r", encoding="utf-8") as file:                        context_dict:dict[str, str] = json.load(file)  
                    new_inst = Instance()
                    new_inst.load_inst_from_dict(context_dict)
                    instancesLists.append(new_inst)
                except (json.JSONDecodeError, OSError, ValueError):
                    continue
        self.instsList = instancesLists

    def _get_source_dir(self) -> str:
        if _is_compiled() or _is_installed():
            return os.path.dirname(os.path.abspath(__file__))
        else:
            dir: Path = Path(os.path.dirname(os.path.abspath(__file__)))
            return str(dir.parent)

    def _get_project_root_dir(self) -> str:
        if _is_compiled() or _is_installed():
            return os.path.dirname(os.path.abspath(__file__))
        else:
            dir: Path = Path(os.path.dirname(os.path.abspath(__file__)))
            return str(dir.parent.parent.parent)

    def _get_locales_dir(self) -> str:
        return os.path.join(self._get_project_root_dir(),"assets", "languages")

    def _get_assets_dir(self) -> str:
        return os.path.join(self._get_project_root_dir(), "assets")

    def _get_user_app_data_dir(self) -> str:
        dirs: PlatformDirs = self.appContext.buildInfo.dirs
        return dirs.user_data_dir

    def _get_user_app_config_dir(self) -> str:
        dirs: PlatformDirs = self.appContext.buildInfo.dirs
        return dirs.user_config_dir

    def _get_site_app_data_dir(self) -> str:
        dirs: PlatformDirs = self.appContext.buildInfo.dirs
        return dirs.site_data_dir

    def _get_site_app_config_dir(self) -> str:
        dirs: PlatformDirs = self.appContext.buildInfo.dirs
        return dirs.site_config_dir

    def _get_app_cache_dir(self) -> str:
        dirs: PlatformDirs = self.appContext.buildInfo.dirs
        return dirs.user_cache_dir

    def _get_app_log_dir(self) -> str:
        dirs: PlatformDirs = self.appContext.buildInfo.dirs
        return dirs.user_log_dir