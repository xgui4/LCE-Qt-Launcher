from __future__ import annotations 
from typing import TYPE_CHECKING

from lce_qt_launcher.build_info import BuildInfo

import lce_qt_launcher.views.term_service as term_service 
import lce_qt_launcher.utils as utils

if TYPE_CHECKING:
    from lce_qt_launcher.managers.instance_manager import Instance
    from lce_qt_launcher.build_info import BuildInfo

from zipfile import ZipFile, BadZipFile, LargeZipFile

from PySide6.QtNetwork import (
    QNetworkAccessManager,
    QNetworkRequest,
    QNetworkReply
) 

from PySide6.QtCore import (
    QUrl,
    QObject,
    QFile,
    QIODevice
)

from io import BytesIO

import requests
import os

START_DOWNLOAD_REQUEST_MSG_STR = "Starting Download Request"

SUCCESS_STATUS_CODE = 200

class Downloader(QObject):
    def __init__(self, build_info: BuildInfo = None):
        super().__init__()
        self._buildInfo: BuildInfo = build_info
        self.manager = QNetworkAccessManager()

    def download_inst_async(self, instance: Instance) -> QNetworkReply:
        print(START_DOWNLOAD_REQUEST_MSG_STR)
        url = QUrl(instance.get_download_url())
        request = QNetworkRequest(url)
        reply = self.manager.get(request)

        def _when_finished():
            reply.deleteLater()
            if reply.error() != QNetworkReply.NetworkError.NoError:
                term_service.print_error(f"Network error : {reply.errorString()}")
                return
            data = reply.readAll().data()
            try:
                with ZipFile(BytesIO(data)) as archive:
                    self.extract_inst_async(archive, instance)
                term_service.print_success(f"Installation of {instance.name} was a success")
                if os.name == "posix":
                    exe_path = os.path.join(instance.installation_path, instance.exe_name)
                    self._buildInfo.system_manager.set_file_permission(exe_path)
            except BadZipFile as e: 
                error_msg : str = f"Extraction Error : {e}"
                term_service.print_error(error_msg)
                raise RuntimeError(error_msg)
            except Exception as e:
                error_msg = f"Extraction Error : {e}"
                term_service.print_error(error_msg)
                raise RuntimeError(error_msg)
            else:
                if os.name == "posix":
                    exe_abs_path = os.path.join(instance.installation_path, instance.exe_name)
                    system = self._buildInfo.system_manager
                    _ = system.set_file_permission(exe_abs_path)

        reply.finished.connect(_when_finished)
        return reply

    def download_inst(self, instance : Instance):
        print("Go to installation")
        response = requests.get(instance.get_download_url())
        response.raise_for_status()
        if response.status_code == SUCCESS_STATUS_CODE:
            term_service.print_success(f"Download of {instance.name} from {instance.get_download_url} was a success")
            try:
                archive : ZipFile = self.extract_inst(response, instance)
            except BadZipFile as err:
                term_service.print_error(f"{err} while extracting {instance.name} games files")
            except LargeZipFile as err:
                term_service.print_error(f"The archive file for {instance.name} ({archive.filename}) was too big.")
            else:
                if os.name == "posix":
                    exe_abs_path = os.path.join(instance.installation_path, instance.exe_name)
                    system = self._buildInfo.system_manager
                    _ = system.set_file_permission(exe_abs_path)
        else:
            print(f"Error : {response.status_code} during the dowloading of the Minecraft LCE Client")
    
    def save_file_from_internet(
        self,
        url : str, 
        filename : str, 
        save_location : str = ".", 
    ):
        print("downloading img")
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == SUCCESS_STATUS_CODE:
            term_service.print_success(f"Downloading of {url} file was success")
            with open(os.path.join(save_location , filename), "wb") as f:
                f.write(response.content)
        else:
            print(f"Error while downloading the {url} file")

    def extract_inst(self, response, instance : Instance) -> ZipFile:
        with ZipFile(BytesIO(response.content)) as archive:
            return archive.extractall(instance.installation_path)
        
    def extract_inst_async(self, data, instance : Instance) -> ZipFile:
        """#TODO Make Async"""
        #download_folder : str = utils.get_user_download_folder()
        #os.makedirs(os.path.join(download_folder, "lce_downloaded_archive"), exist_ok=True)
        #with open(os.path.join(download_folder, "lce_downloaded_archive", instance.archive_file), "wb") as f:
        #    f.write(data)
        return data.extractall(instance.installation_path)
