from __future__ import annotations 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from instance_manager import Instance
    from build_info import BuildInfo

from zipfile import ZipFile, BadZipFile, LargeZipFile
from io import BytesIO

import requests
import os

SUCCESS_STATUS_CODE = 200

class Downloader:
    def __init__(self, build_info: BuildInfo):
        self._build_info = build_info

    def download_instance(self, instance : Instance):
        response = requests.get(instance.get_download_url())
        if response.status_code == SUCCESS_STATUS_CODE:
            print(f"Download of {instance.name} from {instance.get_download_url} was a success")
            try:
                archive : ZipFile = self.extract_instance(response, instance)
            except BadZipFile as err:
                print(f"Error : {err} while extracting {archive.filename}")
            except LargeZipFile as err:
                print(f"Error : {archive.filename} was too big.")
            else:
                if os.name == "posix":
                    exe_abs_path = os.path.join(instance.installation_path, instance.exe_name)
                    system = self._build_info.system_manager
                    system.set_file_permission(exe_abs_path)
        else:
            print(f"Error : {response.status_code} during the dowloading of the Minecraft LCE Client")
    
    def extract_instance(self, response, instance) -> ZipFile:
        with ZipFile(BytesIO(response.content)) as archive:
            return archive.extractall(instance.installation_path)