from src.instance_manager import InstanceManager, Instance
from  src.build_info import BuildInfo

import src.term_service as term_service
import src.utils as utils

import os

MENU_STR = """
1. [bold green] Play [/bold green]
2. [bold green] Install [/bold green]
3. [bold red] Others : Coming Soon ! [/bold red]
"""

def launch_cli():    
    try:
        ascii_art: str = os.path.join(utils.get_assets_dir(), "images", "ascii-art-text.png")
        term_service.show_image(ascii_art)
    except FileNotFoundError:
        term_service.print_error("Image cannot be found.")
        print("LCE Qt Launcher")
    except PermissionError:
        term_service.print_error("File Permission error on the file")
        print("LCE Qt Launcher")
    except:
        term_service.print_error("An unkown error occurred")
        print("LCE Qt Launcher")
    term_service.print_pretty(MENU_STR)

    user_output: str = input()

    buildInfo = BuildInfo()
    defaultInstance = Instance()
    instanceManager = InstanceManager(defaultInstance,buildInfo)

    if user_output == "1":
        print(instanceManager.play())
    if user_output == "2":
        print(instanceManager.install_instance())
    else:
        term_service.print_information("Not implemented Yet!")
