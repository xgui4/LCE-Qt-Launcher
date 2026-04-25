from enum import StrEnum, Enum

from lce_qt_launcher.app_context import AppContext

import lce_qt_launcher.features as features

class CmdArgAction(Enum): 
    """_summary_ The CMD flags Actions"""
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
    """_summary_ The list of command lines args str"""
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

def parse_args(argv : list[str]) -> CmdArgAction:
    """_summary_ Parse the cmd_args to get it actions

    Args:
        argv (list[str]): _description_ the cmd_args/flags to paraes

    Returns:
        CmdArgAction: _description_ The Action of the flags/cmd_args to launch/activated
    """
    match argv: 
        case CmdArg.GEN_CONFIG_CMD_ARG | CmdArg.GEN_CONFIG_CMD_ARG_SHORT:
            return CmdArgAction.GEN_CONFIG
        case CmdArg.VERSION_CMD_ARG | CmdArg.VERSION_CMD_ARG_SHORT:
            return CmdArgAction.PRINT_VERSION
        case CmdArg.LICENSE_CMD_ARG | CmdArg.LICENSE_CMD_ARG_SHORT:
            return CmdArgAction.PRINT_LICENSE
        case CmdArg.ABOUT_CMD_ARG | CmdArg.ABOUT_CMD_ARG_SHORT:
            return CmdArgAction.PRINT_ABOUT_INFO
        case CmdArg.HELP_CMD_ARG, CmdArg.HELP_CMD_ARG_SHORT:
            return CmdArgAction.PRINT_HELP
        case CmdArg.CLI_VERSION_CMD_ARG, CmdArg.CLI_VERSION_CMD_ARG_SHORT:
            return CmdArgAction.CLI_VERSION
        case _:
            return CmdArgAction.NO_ARGS
    
FALLBACK_ABOUT_MESSAGE = "This is a custom Minecraft LCE Launcher written in Python and Qt with Freedom and GNU/Linux support in mind."
FALLBACK_HELP_MESSAGE = "-h or --help to get this help \n -v or --version to get the app version \n -L or --license to get the license information \n -a or --about to get information about the app \n -cl or --cli to launch the cli version \n -g or --gen-config to generate or update the app config"

def launch_cmd_action(action : CmdArgAction, appContext : AppContext) -> None:
    """_summary_ Do the action with an provided AppContext

    Args:
        action (CmdArgAction): _description_ : the action to run
        appContext (AppContext): _description_ : the provided AppContext
    """
    if action == CmdArgAction.GEN_CONFIG:
        features.generate_user_config(appContext.userPref)
    elif action == CmdArgAction.PRINT_LICENSE:
        features.display_license(appContext.buildInfo)
    elif action == CmdArgAction.PRINT_HELP:
        features.display_help(appContext.translator.translate("help-message", FALLBACK_HELP_MESSAGE))
    elif action == CmdArgAction.PRINT_ABOUT_INFO:
        features.display_about(appContext.translator.translate("about_message", FALLBACK_ABOUT_MESSAGE))
    elif action == CmdArgAction.PRINT_VERSION: 
        features.display_version(appContext.buildInfo)
    elif action == CmdArgAction.CLI_VERSION:
        features.launch_cli_interface(appContext.instanceMan)
    else:
        pass