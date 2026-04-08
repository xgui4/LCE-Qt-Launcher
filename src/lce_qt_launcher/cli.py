from lce_qt_launcher.managers.instance_manager import InstanceManager
from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.cmd_arg import CmdArgAction

import lce_qt_launcher.features as features
import lce_qt_launcher.term_service as term_service

MENU_STR = """
1. [bold green] Play [/bold green]
2. [bold green] Install [/bold green]
3. [bold red] Others : Coming Soon ! [/bold red]
"""

def parse_cmd_arg(action, appContext):
        if action == CmdArgAction.GEN_CONFIG:
            features.generate_user_config(appContext.userPref)
        if action == CmdArgAction.PRINT_LICENSE:
            features.display_license(appContext.buildInfo)
        if action == CmdArgAction.PRINT_HELP:
            features.display_help(appContext.translator.translate("help-message"))
        if action == CmdArgAction.PRINT_ABOUT_INFO:
            features.display_about(appContext.translator.translate("about_message"))
        if action == CmdArgAction.PRINT_VERSION: 
            features.display_version(appContext.buildInfo)
        if action == CmdArgAction.CLI_VERSION:
            features.launch_cli_interface(appContext.instanceManager)
        else:
            term_service.print_information("Not Implemented Yet!")

def launch_cli(instance_man : InstanceManager, build_info : BuildInfo, argv : set = {}):    
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
