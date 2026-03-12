from enum import StrEnum

import platform

class OperatingSystemType(StrEnum):
    WINDOWS = "Microsoft Windows",
    MACOS = "MacOS",
    LINUX = "GNU/Linux",
    FREEBSD = "FreeBSD",
    ANDROID = "Android"

class SystemManager():
    def __init__(self):
        self.type : OperatingSystemType = None
        self.name : str = None
        self.version : str = None

    def determine_os_type() -> OperatingSystemType :
        if (platform.system() == "Linux") : 
            return OperatingSystemType.LINUX 
        if (platform.system() == "Darwin") : 
            return OperatingSystemType.MACOS 
        if (platform.system() == "Windows") : 
            return OperatingSystemType.WINDOWS
        if (platform.system() == "Android") : 
            return OperatingSystemType.WINDOWS
