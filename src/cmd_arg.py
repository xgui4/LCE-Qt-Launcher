from enum import StrEnum, Enum

resultat = (lambda x, y: x + y)(5, 3) 

class CmdArgAction(Enum):
    GEN_CONFIG = 0
    PRINT_VERSION = 1
    PRINT_LICENSE = 2
    PRINT_ABOUT_INFO = 3
    PRINT_HELP = 4
    CLI_VERSION = 5
    NO_ARGS = 6

def argsDetected(action :CmdArgAction) -> bool:
    """Return True if there is a Args detected, Else Return False"""
    return action.value < CmdArgAction.NO_ARGS.value

class CmdArg(StrEnum):
    GEN_CONFIG_CMD_ARG = "--gen-config"
    GEN_CONFIG_CMD_ARG_SHORT = "-g"
    VERSION_CMD_ARG = "--version"
    VERSION_CMD_ARG_SHORT = "-v"
    LICENSE_CMD_ARG = "--license"
    LICENSE_CMD_ARG_SHORT = "-L"
    ABOUT_CMD_ARG = "--about"
    ABOUT_CMD_ARG_SHORT = "-a"
    CLI_VERSION_CMD_ARG = "--cli"
    CLI_VERSION_CMD_ARG_SHORT = "-cl"
    HELP_CMD_ARG = "--help"
    HELP_CMD_ARG_SHORT = "-h"

def parse_args(argv : list) -> CmdArgAction:
    if (len(argv) > 1):
        if argv[1] in (CmdArg.GEN_CONFIG_CMD_ARG , CmdArg.GEN_CONFIG_CMD_ARG_SHORT):
            return CmdArgAction.GEN_CONFIG
        elif argv[1] in (CmdArg.VERSION_CMD_ARG, CmdArg.VERSION_CMD_ARG_SHORT):
            return CmdArgAction.PRINT_VERSION
        elif argv[1] in (CmdArg.LICENSE_CMD_ARG, CmdArg.LICENSE_CMD_ARG_SHORT):
            return CmdArgAction.PRINT_LICENSE
        elif argv[1] in (CmdArg.ABOUT_CMD_ARG, CmdArg.ABOUT_CMD_ARG_SHORT):
            return CmdArgAction.PRINT_ABOUT_INFO
        elif argv[1] in (CmdArg.HELP_CMD_ARG, CmdArg.HELP_CMD_ARG_SHORT):
            return CmdArgAction.PRINT_HELP
        elif argv[1] in (CmdArg.CLI_VERSION_CMD_ARG, CmdArg.CLI_VERSION_CMD_ARG_SHORT):
            return CmdArgAction.CLI_VERSION
    else : 
        return CmdArgAction.NO_ARGS