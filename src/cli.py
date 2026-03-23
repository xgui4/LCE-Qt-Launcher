from instance_manager import InstanceManager, Instance

import term_service
import build_info

import os

MENU_STR = """
1. [bold green] Play [/bold green]
2. [bold green] Install [/bold green]
3. [bold red] Others : Coming Soon ! [/bold red]
"""

def launch_cli():    
    try:
        ascii_art = os.path.join(build_info.get_assets_dir(), "ascii-art-text.png")
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

    user_output = input()

    defaultInstance = Instance()
    instanceManager = InstanceManager(defaultInstance)

    if user_output == "1":
        instanceManager.play() 
    if user_output == "2":
        instanceManager.install_instance()
    else:
        term_service.print_information("Not implemented Yet!")
