from term_image.image import from_file
from rich import print

from user_pref import UserPref
from build_info import BuildInfo
from instance_manager import InstanceManager, Instance
from cmd_arg import CmdArgAction, parse_args, argsDetected

import webbrowser
import sys
import os
import platform

image = from_file("/home/xgui4/Downloads/ascii-art-text.png")

image.draw()

MENU_STR = """
1. [bold green] Play [/bold green]
2. [bold green] Install [/bold green]
3. [bold red] Others : Coming Soon ! [/bold red]
"""

print(MENU_STR)

user_output = input()

userPref = UserPref()
buildInfo = BuildInfo()

defaultInstance = Instance()
instanceManager = InstanceManager(defaultInstance)

if user_output == "1":
    instanceManager.play() 
if user_output == "2":
    instanceManager.install()
else:
    print("not implemented yet") 
