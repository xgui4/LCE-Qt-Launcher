from enum import StrEnum

import platform
import os
import pathlib
import stat

class OperatingSystemType(StrEnum):
    WINDOWS = "Microsoft Windows",
    MACOS = "MacOS",
    LINUX = "GNU/Linux",
    FREEBSD = "FreeBSD",
    ANDROID = "Android",
    UNKNOWN = "Unknow"

class SystemManager():
    def __init__(self):
        self.type : OperatingSystemType = None
        self.name : str = None
        self.version : str = None
        
        self.determine_os_info()

    def determine_os_info(self):
        if (platform.system() == "Linux") : 
            self.type = OperatingSystemType.LINUX 
            self.name = self.type.name
            self.version = platform.version()
        if (platform.system() == "Darwin") : 
            self.type = OperatingSystemType.MACOS 
            self.name = self.type.name
            self.version = platform.mac_ver()
        if (platform.system() == "Windows") : 
            self.type = OperatingSystemType.WINDOWS
            self.name = self.type.name
            self.version = platform.win32_ver()
        if (platform.system() == "FreeBSD"):
            self.type = OperatingSystemType.FREEBSD 
            self.name = self.type.name
            self.version = platform.version()
        if (platform.system() == "Android") : 
            self.type = OperatingSystemType.ANDROID
            self.name = self.type.name
            self.version = platform.version()
        else:
            self.type = OperatingSystemType.UNKNOWN
            self.name = self.type.name
            self.version = platform.version()
    
    def adapt_qt_system_theme(self):
        if platform.system() == "Linux": 
            _LINUX_QT6_PATH = "/usr/lib/qt6/plugins"
            os.environ["QT_PLUGIN_PATH"] = _LINUX_QT6_PATH

        if platform.system() == "FreeBSD": 
            _FREEBSD_QT6_PATH = "/usr/local/lib/qt6/plugins"
            os.environ["QT_PLUGIN_PATH"] = _FREEBSD_QT6_PATH

        if os.name == "nt":
            os.environ["QT_QPA_PLATFORM"] = "windows:darkmode=2"

    def set_file_permission(self, file_abs_path : str) -> str:
        if self.type in [OperatingSystemType.LINUX, OperatingSystemType.FREEBSD, OperatingSystemType.MACOS]:
                curr_perm = os.stat(file_abs_path)
                new_perm = curr_perm.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
                os.chmod(file_abs_path, new_perm)
        else:
            pass
    
    def found_default_save_path(self) -> str:
        return os.path.join(pathlib.Path.home(), "lce-qt-launcher")  
