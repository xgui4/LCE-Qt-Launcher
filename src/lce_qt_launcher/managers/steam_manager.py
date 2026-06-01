#!/usr/bin/env python
"""
LCE Instances Steam Manager
Copyright (C) 2026 Xgui4

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from PySide6.QtWidgets import QMessageBox

import argparse
import subprocess
import platform
import sys

LEGAL_TEXT = """
    LCE Instances Steam Manager Copyright (C) 2026  Xgui4
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
    """

STEAM_USERS_LOCATION = "~/.steam/steam/config/loginusers.vdf"
STEAM_SHORTCUTS_LOCATION = "~/steam/steam/userdata/{steam-id}/config/"


def add_instance_to_steam(abs_instance_exe_path: str, instance_name: str, icon: str):
    """_summary_
        add the instance to the steam
    Args:
        instance_exe_path (str): _description_ the instance executable file path
        instance_name (str): _description_ the instance name string
        icon (str): _description_ the icon path string
    """
    try:
        try:
            QMessageBox.warning(
                None,
                "Warning",
                "For this operation, it is recommended to close steam. ",
            )
        except RuntimeError:
            input("Warning : For this operation, it is recommended to close steam.")
        QMessageBox.warning(
            None, "Warning", "For this operation, it is recommended to close steam. "
        )
        if platform.uname().system == "Linux":
            subprocess.run(
                [
                    "steamtinkerlaunch",
                    "ansg",
                    f'-an="Minecraft LCE ({instance_name}"',
                    f'-ep="{abs_instance_exe_path}"',
                    f"-ip={icon}",
                ]
            )
            try:
                QMessageBox.warning(
                    None,
                    "Warning",
                    "This function is in work in progress and the id is not saved in the launcher. \n"
                    + "Until this is added, a manual intervention is needed to found the id and put in the save file. ",
                )
            except RuntimeError:
                print(
                    "Warning : This function is in work in progress and the id is not saved in the launcher. \n"
                    + "Until this is added, a manual intervention is needed to found the id and put in the save file. "
                )
        else:
            QMessageBox.critical(None, "Critical Error", "Not Implemented Yet!")
    except RuntimeError as err:
        print(f"Error while adding program to steam : {err}")


def main():
    parser = argparse.ArgumentParser(
        prog="LCE Instances Steam Manager", description="Add LCE instance to Steam"
    )

    instance_exe_path: str = ""
    instance_name: str = ""
    icon: str = ""

    print(LEGAL_TEXT)

    if len(sys.argv) > 1:
        parser.add_help = True
        parser.epilog = LEGAL_TEXT

        parser.add_argument(
            "--exe_path", type=str, help="Path of the instance exe to add to Steam"
        )
        parser.add_argument(
            "--name", type=str, help="Instance Name of the instance to add to Steam"
        )
        parser.add_argument(
            "--icon", type=str, help="The icon of the instance to add to Steam"
        )

        parsed_cmd_args = parser.parse_known_intermixed_args()

        if parsed_cmd_args[0].intance_exe_path == "None":
            instance_exe_path = input(
                "Enter the instance of path of the exe to add on steam"
            )
        if parsed_cmd_args[0].intance_name == "None":
            instance_name = input("Enter the name of instance to add on steam")
        if parsed_cmd_args[0].icon == "None":
            icon = input("Enter the path of the icon of the instance to add on steam")

        add_instance_to_steam(instance_exe_path, instance_name, icon)
    else:
        instance_exe_path = input(
            "Enter the instance of path of the exe to add on steam"
        )
        instance_name = input("Enter the name of instance to add on steam")
        icon = input("Enter the path of the icon of the instance to add on steam")
        add_instance_to_steam(instance_exe_path, instance_name, icon)


if __name__ == "__main__":
    main()
