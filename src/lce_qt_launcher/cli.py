from lce_qt_launcher.managers.instance_manager import InstanceManager, Instance
from  lce_qt_launcher.build_info import BuildInfo

import lce_qt_launcher.term_service as term_service

MENU_STR = """
1. [bold green] Play [/bold green]
2. [bold green] Install [/bold green]
3. [bold red] Others : Coming Soon ! [/bold red]
"""

def launch_cli(instance_man : InstanceManager):    
    print("LCE Qt Launcher")

    term_service.print_pretty(MENU_STR)

    user_output: str = input()

    if user_output == "1":
        print(instance_man.play())
    if user_output == "2":
        print(instance_man.install_instance())
    else:
        term_service.print_information("Not implemented Yet!")
