from lce_qt_launcher.managers.instance_manager import InstanceManager
from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.views.cmd_arg import CmdArgAction
from lce_qt_launcher.app_context import AppContext

import lce_qt_launcher.features as features
import lce_qt_launcher.views.term_service as term_service

FALLBACK_ABOUT_MESSAGE = "This is a custom Minecraft LCE Launcher written in Python and Qt with Freedom and GNU/Linux support in mind."
FALLBACK_HELP_MESSAGE = "-h or --help to get this help \n -v or --version to get the app version \n -L or --license to get the license information \n -a or --about to get information about the app \n -cl or --cli to launch the cli version \n -g or --gen-config to generate or update the app config"

def parse_cmd_arg(action : CmdArgAction, appContext : AppContext):
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
    else:
        term_service.print_information("Not Implemented Yet!")

def launch_cli(instance_man : InstanceManager, build_info : BuildInfo, argv : set = {}):    
    MENU_STR = """
1. [bold green] Play [/bold green]
2. [bold green] Install [/bold green]
3. [bold red] Others : Coming Soon ! [/bold red]
"""
    term_service.print_pretty(build_info.app_name)
    term_service.print_pretty(MENU_STR)
    if len(argv) < 1:
        user_output: str = input()
    if user_output == "1" or argv[1] == "play":
        print(instance_man.play())
    if user_output == "2" or argv[1] == "install":
        print(instance_man.install_instance())
    else:
        term_service.print_information("Not implemented Yet!")
