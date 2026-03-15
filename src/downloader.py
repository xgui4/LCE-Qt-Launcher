from __future__ import annotations 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from instance_manager import Instance

from zipfile import ZipFile, BadZipFile, LargeZipFile
from io import BytesIO

import requests
import os
import stat
import platform

SUCCESS_STATUS_CODE = 200

class Downloader:
    def download_client(self, instance : Instance):
        response = requests.get(instance.get_download_url())
        if response.status_code == SUCCESS_STATUS_CODE:
            try:
                with ZipFile(BytesIO(response.content)) as archive:
                    archive.extractall(instance.installation_path)
            except BadZipFile as err:
                print(f"Error : {err} while extracting {archive.filename}")
            except LargeZipFile as err:
                print(f"Error : {archive.filename} was too big.")
            else:
                if os.name == "posix":
                    exe_abs_path = os.path.join(instance.installation_path, instance.exe_name)
                    curr_perm = os.stat(exe_abs_path)
                    new_perm = curr_perm.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
                    os.chmod(exe_abs_path, new_perm)
        else:
            print(f"Error : {response.status_code} during the dowbloading of the Minecraft LCE Client")