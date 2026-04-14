from enum import StrEnum, Enum

from lce_qt_launcher.app_context import AppContext

import lce_qt_launcher.views.term_service as term_service
import lce_qt_launcher.features as features

class CmdArgAction(Enum):
    GEN_CONFIG = 0
    PRINT_VERSION = 1
    PRINT_LICENSE = 2
    PRINT_ABOUT_INFO = 3
    PRINT_HELP = 4
    CLI_VERSION = 5
    NO_ARGS = 6
    GUI_ARGUMENTS = 7

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
    GUI_ARGS_CMD_ARG = "--gui"
    GUI_ARGS_CMD_ARG_SHORT = "-g"
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
        elif argv[1] in (CmdArg.GUI_ARGS_CMD_ARG, CmdArg.GUI_ARGS_CMD_ARG_SHORT):
            return CmdArgAction.GUI_ARGUMENTS
    else : 
        return CmdArgAction.NO_ARGS
    
FALLBACK_ABOUT_MESSAGE = "This is a custom Minecraft LCE Launcher written in Python and Qt with Freedom and GNU/Linux support in mind."
FALLBACK_HELP_MESSAGE = "-h or --help to get this help \n -v or --version to get the app version \n -L or --license to get the license information \n -a or --about to get information about the app \n -cl or --cli to launch the cli version \n -g or --gen-config to generate or update the app config"

def launch_cmd_action(action : CmdArgAction, appContext : AppContext):
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
        features.launch_cli_interface(appContext.instanceManager)
    elif action == CmdArgAction.CLI_VERSION:
        term_service.print_warning("Not Implemented Yet!")
    else:
        term_service.print_information("Not Implemented Yet!")