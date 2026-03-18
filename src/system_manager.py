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
        
        self.determine_os_type()

    def determine_os_type(self):
        if (platform.system() == "Linux") : 
            self.type = OperatingSystemType.LINUX 
        if (platform.system() == "Darwin") : 
            self.type = OperatingSystemType.MACOS 
        if (platform.system() == "Windows") : 
            self.type = OperatingSystemType.WINDOWS
        if (platform.system() == "FreeBSD"):
            self.type = OperatingSystemType.FREEBSD 
        if (platform.system() == "Android") : 
            self.type = OperatingSystemType.ANDROID
        else:
            self.type = OperatingSystemType.UNKNOWN
    
    def set_file_permission(self, file_abs_path : str) -> str:
        if self.type in [OperatingSystemType.LINUX, OperatingSystemType.FREEBSD, OperatingSystemType.MACOS]:
                curr_perm = os.stat(file_abs_path)
                new_perm = curr_perm.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
                os.chmod(file_abs_path, new_perm)
        else:
            pass
    
    def found_default_save_path(self) -> str:
        return os.path.join(pathlib.Path.home(), "saves")  
