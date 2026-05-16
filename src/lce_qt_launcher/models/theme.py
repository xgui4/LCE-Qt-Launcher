from ctypes import ArgumentError
from enum import StrEnum, Enum


class StrTheme(StrEnum):
    """_summary_ The QtApp Stylesheet theme"""

    MINECRAFT = ":/styles/minecraft.qss"
    DARK = ":/styles/dark.qss"
    LIGHT = ":/sytles/light.qss"
    SYSTEM = "SYSTEM"


class ThemeEntity(Enum):
    """TODO _summary_

    Args:
        Enum (_type_): _description_
    """

    DEFAULT = 0
    MINECRAFT = 1
    LIGHT = 2
    DARK = 3
    SYSTEM = 4


def from_entity_to_strTheme(entity: ThemeEntity) -> StrTheme:
    match entity:
        case ThemeEntity.DEFAULT | ThemeEntity.MINECRAFT:
            return StrTheme.MINECRAFT
        case ThemeEntity.LIGHT:
            return StrTheme.LIGHT
        case ThemeEntity.DARK:
            return StrTheme.DARK
        case ThemeEntity.SYSTEM:
            return StrTheme.SYSTEM


def get_theme_file_name(strTheme: StrTheme) -> str:
    """TODO _summary_

    Args:
        strTheme (StrTheme): _description_

    Returns:
        _type_: _description_
    """
    match strTheme:
        case StrTheme.MINECRAFT:
            return "minecraft.qss"
        case StrTheme.DARK:
            return "dark.qss"
        case StrTheme.LIGHT:
            return "light.qss"
        case StrTheme.SYSTEM:
            return "SYSTEM"


def from_str_to_strTheme(string: str) -> StrTheme:
    """TODO _summary_

    Args:
        string (str): _description_

    Raises:
        ArgumentError: _description_

    Returns:
        StrTheme: _description_
    """
    match string:
        case ":/styles/minecraft.qss":
            return StrTheme.MINECRAFT
        case ":/styles/dark.qss":
            return StrTheme.DARK
        case ":/sytles/light.qss":
            return StrTheme.LIGHT
        case "":
            return StrTheme.SYSTEM
        case _:
            raise ArgumentError(f"{string} is not a valid theme")
