from __future__ import annotations 
from typing import TYPE_CHECKING

from lce_qt_launcher.build_info import BuildInfo

import lce_qt_launcher.views.term_service as term_service 

if TYPE_CHECKING:
    from lce_qt_launcher.managers.instance_manager import Instance
    from lce_qt_launcher.build_info import BuildInfo

from zipfile import ZipFile, BadZipFile, LargeZipFile

from PySide6.QtNetwork import (
    QNetworkAccessManager,
    QNetworkRequest,
    QNetworkReply
) 

from io import BytesIO

import requests
import os

SUCCESS_STATUS_CODE = 200

class Downloader:
    def __init__(self, build_info: BuildInfo = None):
        self._build_info: BuildInfo = build_info
        networkManager = QNetworkAccessManager()

    def download_instance(self, instance : Instance):
        print("Go to installation")
        response = requests.get(instance.get_download_url())
        response.raise_for_status()
        if response.status_code == SUCCESS_STATUS_CODE:
            term_service.print_success(f"Download of {instance.name} from {instance.get_download_url} was a success")
            try:
                archive : ZipFile = self.extract_instance(response, instance)
            except BadZipFile as err:
                term_service.print_error(f"{err} while extracting {instance.name} games files")
            except LargeZipFile as err:
                term_service.print_error(f"The archive file for {instance.name} ({archive.filename}) was too big.")
            else:
                if os.name == "posix":
                    exe_abs_path = os.path.join(instance.installation_path, instance.exe_name)
                    system = self._build_info.system_manager
                    _ = system.set_file_permission(exe_abs_path)
        else:
            print(f"Error : {response.status_code} during the dowloading of the Minecraft LCE Client")
    
    def save_file_from_internet(
        self,
        url : str, 
        filename : str, 
        file_ext : str,
        save_location : str = ".", 
    ):
        print("downloading img")
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == SUCCESS_STATUS_CODE:
            term_service.print_success(f"Downloading of {url} file was success")
            with open(os.path.join(save_location ,f"{filename}.{file_ext}"), "wb") as f:
                f.write(response.content)
        else:
            print(f"Error while downloading the {url} file")

    def extract_instance(self, response, instance : Instance) -> ZipFile:
        with ZipFile(BytesIO(response.content)) as archive:
            return archive.extractall(instance.installation_path)