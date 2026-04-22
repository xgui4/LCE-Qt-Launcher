from enum import StrEnum

import platform
import os
import pathlib
import stat

import lce_qt_launcher.views.term_service as term_service

class OperatingSystemType(StrEnum):
    WINDOWS = "Microsoft Windows"
    MACOS = "MacOS"
    LINUX = "GNU/Linux"
    FREEBSD = "FreeBSD"
    ANDROID = "Android"
    UNKNOWN = "Unknown"

class SystemManager():
    """_summary_ Multiples Utilises to interact with the system
    """
    def __init__(self) -> None:
        self.type : OperatingSystemType = OperatingSystemType.UNKNOWN
        self.name : str = "Unknown"
        self.version : str = "Unknown"
        
        self.determine_os_info()

    def determine_os_info(self) -> None: 
        """_summary_ Assert the OS and its Info 
        """
        if (platform.system() == "Linux") : 
            self.type = OperatingSystemType.LINUX 
            self.name = self.type.name
            self.version = platform.version()
        elif (platform.system() == "Darwin") : 
            self.type = OperatingSystemType.MACOS 
            self.name = self.type.name
            self.version = str(platform.mac_ver())
        elif (platform.system() == "Windows") : 
            self.type = OperatingSystemType.WINDOWS
            self.name = self.type.name
            self.version = str(platform.win32_ver())
        elif (platform.system() == "FreeBSD"):
            self.type = OperatingSystemType.FREEBSD 
            self.name = self.type.name
            self.version = platform.version()
        elif (platform.system() == "Android") : 
            self.type = OperatingSystemType.ANDROID
            self.name = self.type.name
            self.version = platform.version()
        else:
            self.type = OperatingSystemType.UNKNOWN
            self.name = self.type.name
            self.version = platform.version()
    
    def adapt_qt_system_theme(self) -> None:
        if platform.system() == "Linux": 
            _LINUX_QT6_PATH = "/usr/lib/qt6/plugins"
            os.environ["QT_PLUGIN_PATH"] = _LINUX_QT6_PATH
        if platform.system() == "FreeBSD": 
            _FREEBSD_QT6_PATH = "/usr/local/lib/qt6/plugins"
            os.environ["QT_PLUGIN_PATH"] = _FREEBSD_QT6_PATH

    def set_file_permission(self, file_abs_path: str) -> str:
        """
        _summary_ Makes the file executable on POSIX systems. Do Nothing on NT (Windows)
        
        Args:
            file_abs_path : str = "The absolute file path to change the permissions"
        """
        if os.name == "posix":
            st = os.stat(file_abs_path)
            os.chmod(file_abs_path, st.st_mode | stat.S_IEXEC)
            return "Permissions updated."
        else:
            term_service.print_information("No POSIX system detected, skipping file permission management.")
            return "Non POSIX System."
    
    def found_default_save_path(self) -> str:
        """ 
        ! DEPRECIATED

        FIXME - REMOVE THIS FUNCTION AND REPLACE IT WITH OTHERS
        """
        return os.path.join(pathlib.Path.home(), "lce-qt-launcher")  
