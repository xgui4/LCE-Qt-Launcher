from sys import argv

from lce_qt_launcher.managers.instance_manager import InstanceManager
from lce_qt_launcher.build_info import BuildInfo
import lce_qt_launcher.views.term_service as term_service

def launch_cli(instance_man : InstanceManager, build_info : BuildInfo) -> None:  
    """
    _summary_ : launch the cli interface 

    Args: 
        instance_man : the instancer Manager object 
        buildInfo (FIXME : unused) : an BuildInfo class
    """
    
    MENU_STR = """
1. [bold green] Play [/bold green]
2. [bold green] Install [/bold green]
3. [bold red] Others : Coming Soon ! [/bold red]
"""
    term_service.print_warning("CLI mode is currently untested and might be working correctly and will be reworked soon.")
    term_service.print_pretty("""
LCE Qt Launcher Copyright (C) 2026  Xgui4
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
""")
    term_service.print_pretty(MENU_STR)

    user_output: str = input()    

    if len(argv) < 1:
        user_output = input()
    if user_output == "1" or argv[2] == "play":
        print(instance_man.play())
    if user_output == "2" or argv[2] == "install":
        print(instance_man.install_instance())
    else:
        term_service.print_information("Not implemented Yet!")
