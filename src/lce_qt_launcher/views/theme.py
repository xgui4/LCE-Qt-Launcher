from ctypes import ArgumentError
from enum import StrEnum

class Theme(StrEnum):
    """_summary_ The QtApp Stylesheet theme"""
    MINECRAFT = ":/styles/minecraft.qss"
    DARK = ":/styles/dark.qss"
    LIGHT = ":/sytles/light.qss"
    SYSTEM = ""
    
def from_str_to_theme(string : str) -> Theme:
    match string:
        case ":/styles/minecraft.qss": return Theme.MINECRAFT
        case ":/styles/dark.qss": return Theme.DARK
        case ":/sytles/light.qss" : return Theme.LIGHT
        case "": return Theme.SYSTEM 
        case _ : raise ArgumentError(f"{string} is not a valid theme")