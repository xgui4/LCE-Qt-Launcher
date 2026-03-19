#!/usr/bin/env python3

from term_image.image import from_file
from rich import print

from instance_manager import InstanceManager, Instance

import build_info

import os

MENU_STR = """
1. [bold green] Play [/bold green]
2. [bold green] Install [/bold green]
3. [bold red] Others : Coming Soon ! [/bold red]
"""

def launch_cli():    

    ascii_art = os.path.join(build_info.get_assets_dir(), "ascii-art-text.png")
    
    image = from_file(ascii_art)

    image.draw()

    print(MENU_STR)

    user_output = input()

    defaultInstance = Instance()
    instanceManager = InstanceManager(defaultInstance)

    if user_output == "1":
        instanceManager.play() 
    if user_output == "2":
        instanceManager.install_instance()
    else:
        print("not implemented yet") 
