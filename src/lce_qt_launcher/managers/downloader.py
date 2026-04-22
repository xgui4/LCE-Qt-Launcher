from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lce_qt_launcher.managers.instance_manager import Instance
    from lce_qt_launcher.build_info import BuildInfo
    from requests.models import Response

import lce_qt_launcher.views.term_service as term_service 

from lce_qt_launcher.managers.system_manager import SystemManager

from zipfile import (
    ZipFile, BadZipFile
)

from PySide6.QtNetwork import (
    QNetworkAccessManager,
    QNetworkRequest,
    QNetworkReply
) 

from PySide6.QtCore import (
    QUrl,
    QObject,
)

from io import BytesIO

import requests
import os

START_DOWNLOAD_REQUEST_MSG_STR = "Starting Download Request"

SUCCESS_STATUS_CODE = 200

class Downloader(QObject):
    """_summary_ Downloader Manager to download stuff from the internet

    Args:
        QObject (_type_): _description_ Inherit from the QObject
    """
    def __init__(self, appContext : AppContext) -> None:
        super().__init__()
        self._buildInfo: BuildInfo = build_info
        self.manager: QNetworkAccessManager = QNetworkAccessManager()

    def download_inst_async(self, instance: Instance) -> QNetworkReply:
        """ _summary_ Download and install the selected Instance 

        Args:
            instance : The selected instance to install or Update
        #TODO  : make it better and less dependant of instance"""
        print(START_DOWNLOAD_REQUEST_MSG_STR)
        url: QUrl = QUrl(instance.get_download_url())
        request: QNetworkRequest = QNetworkRequest(url)
        reply: QNetworkReply = self.manager.get(request)

        def _when_finished() -> None:
            reply.deleteLater()
            if reply.error() != QNetworkReply.NetworkError.NoError:
                term_service.print_error(f"Network error : {reply.errorString()}")
                return
            data = reply.readAll().data()
            try:
                with ZipFile(BytesIO(data)) as archive:
                    _ = self.extract_inst_async(archive, instance)
                term_service.print_success(f"Installation of {instance.name} was a success")
                if os.name == "posix":
                    exe_path = os.path.join(instance.installation_path, instance.exe_name)
                    _ = self._buildInfo.system_manager.set_file_permission(exe_path)
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
                    exe_abs_path: str = os.path.join(instance.installation_path, instance.exe_name)
                    system: SystemManager = self._buildInfo.system_manager
                    _ = system.set_file_permission(exe_abs_path)

        _ = reply.finished.connect(_when_finished)
        return reply
    
    def save_file_from_internet(
        self,
        url : str, 
        filename : str, 
        save_location : str = ".", 
    ) -> None:
        """
        _summary_ : download a file from the internet and than save it in a specified location 

        Args:
            url : the url to download the file
            filename : the filename to save the file inot (with extension)
            save_location (optional) : the specified location , default into "." 
        #TODO - Make Async
        """
        print("downloading img")
        response: Response = requests.get(url)
        response.raise_for_status()
        if response.status_code == SUCCESS_STATUS_CODE:
            term_service.print_success(f"Downloading of {url} file was success")
            with open(file=os.path.join(save_location , filename), mode="wb") as f:
                _ = f.write(response.content)
        else:
            print(f"Error while downloading the {url} file")
        
    def extract_inst_async(self, data : ZipFile, instance : Instance) -> None:
        """
        _summary_ : extract the zipfile of the downloaded instance

        Args:
            data : the zip file itself
            instance : the specified instance 
        #TODO Make Async
        """
        data.extractall(instance.installation_path)
