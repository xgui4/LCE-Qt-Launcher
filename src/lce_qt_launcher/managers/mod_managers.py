#!/usr/bin/env python
"""
    LCE Mods Manager
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
import sys
import os
import argparse

from enum import StrEnum
from zipfile import ZipFile

DLC_LOCATION = os.path.join("Windows64Media", "DLC")
WORLD_LOCATION = os.path.join("Windows64", "GameHDD")
MOD_LOCATION = os.path.join("Windows64", "Media")

class ContentType(StrEnum):
    DLC = DLC_LOCATION
    WORLD = WORLD_LOCATION
    MOD = MOD_LOCATION
    NONE = "0"
    CUSTOM_SKIN = "-1" # Temporaly placeholder DO NOT USE,

LEGAL_TEXT = """
    LCE Mods Managers    Copyright (C) 2026  Xgui4

    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
"""

def extract_zip(data : ZipFile, extraction_path : str) -> None:
    """
    _summary_ : extract the zipfile of the content to the desired path

    Args:
        data : the zip file itself
        extraction_path : the specified extraction path
    #TODO Make Async
    """
    data.extractall(extraction_path)

def install_content(instance_path : str,  contentType : ContentType, archive_file : str):
    """_summary_   #TODO docstring

    Args:
        instance_path (str): _description_ 
        contentType (ContentType): _description_ 
        archive_file (str): _description_ 
    """
    zipFile = ZipFile(archive_file)

    content_path : str = os.path.join(instance_path, contentType.value)

    extract_zip(zipFile, content_path)

def main():     
    parser = argparse.ArgumentParser(
        prog="LCE Mods Manager",
        description="Manage DLC, World and Mods for Minecraft LCE"
    )

    file : str = ""
    contentType : str = ""
    instance_path : str = ""
    contentTypeEnum : ContentType = ContentType.NONE

    if len(sys.argv) > 1:
        parser.add_help = True
        parser.epilog = LEGAL_TEXT

        parser.add_argument("--instance_path", type=str, help="Path of the instance to install the content on")
        parser.add_argument("--content_type", type=str, help="Content Type, possible valie : DLC, World and Mod")
        parser.add_argument("--file", type=str, help="The Archive file to install")

        parsed_cmd_args = parser.parse_known_intermixed_args()

        contentType : str = parsed_cmd_args[0].content_type

        contentTypeEnum : ContentType = ContentType.NONE

        if parsed_cmd_args[0].content_type == "None":
            print(r"""
            1. Install Maps/World
            2. Install DLC
            3. Install Mods
            4. Install Custom Skin (Coming Soon)
            5. Cancel 
            """)
        
            user_input = input("Choose a option")

            if user_input == "1":
                contentTypeEnum = ContentType.WORLD
            if user_input == "2":
                contentTypeEnum = ContentType.DLC
            if user_input == "3":
                contentTypeEnum = ContentType.MOD
            else:
                raise RuntimeError("Not impleted Yet") 
            
        if (contentType == "DLC"):
            contentTypeEnum = ContentType.DLC
        if (contentType == "World"):
            contentTypeEnum = ContentType.WORLD
        if (contentType == "Mod"):
            contentTypeEnum = ContentType.MOD
        else:
            pass
            
        instance_path = parsed_cmd_args[0].instance_path

        if instance_path == "None":
            instance_path = input("Enter the Instance path.")

        file : str = parsed_cmd_args[0].file

        if file == "None":
            file = input(f"Enter the archive of the {contentTypeEnum.name}")
    
    else:
        print(r"""
        1. Install Maps/World
        2. Install DLC
        3. Install Mods
        4. Install Custom Skin (Coming Soon)
        5. Cancel 
        """)
    
        user_input = input("Choose a option")

        if user_input == "1":
            contentTypeEnum = ContentType.WORLD
        if user_input == "2":
            contentTypeEnum = ContentType.DLC
        if user_input == "3":
            contentTypeEnum = ContentType.MOD
        else:
            raise RuntimeError("Not impleted Yet") 
        
        instance_path = input("Enter the Instance path.")

        file = input(f"Enter the archive of the {contentTypeEnum.name}")

    print(LEGAL_TEXT)

    print(f"""File : {file}
    Content Type : {contentTypeEnum.value}
    Instance_Path : {instance_path}""")

    install_content(instance_path, contentTypeEnum, file) 

if __name__ == "__main__":
    main()