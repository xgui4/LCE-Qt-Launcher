from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lce_qt_launcher.managers.instance_manager import Instance

from lce_qt_launcher.app_context import AppContext
import lce_qt_launcher.views.term_service as term_service

from lce_qt_launcher.managers.system_manager import SystemManager

from zipfile import ZipFile, BadZipFile

from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

from PySide6.QtCore import (
    QUrl,
    QObject,
)

from io import BytesIO

import os

START_DOWNLOAD_REQUEST_MSG_STR = "Starting Download Request"

SUCCESS_STATUS_CODE = 200


class Downloader(QObject):
    """_summary_ Downloader Manager to download stuff from the internet

    Args:
        QObject (_type_): _description_ Inherit from the QObject
    """

    def __init__(self, appContext: AppContext) -> None:
        super().__init__()
        self.manager: QNetworkAccessManager = QNetworkAccessManager()
        self.appContext: AppContext = appContext

    def download_async(self, url_str: str, object_name: str) -> QNetworkReply:
        """#TODO docstring _summary_

        Args:
            url_str (str): _description_
            object_name (str): _description_

        Raises:
            RuntimeError: _description_
            RuntimeError: _description_

        Returns:
            QNetworkReply: _description_
        """
        print(START_DOWNLOAD_REQUEST_MSG_STR)
        url: QUrl = QUrl(url_str)
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
                    _ = self.extract_async(archive, object_name)
                term_service.print_success(
                    f"Installation of {object_name} was a success"
                )
            except BadZipFile as e:
                error_msg: str = f"Extraction Error : {e}"
                term_service.print_error(error_msg)
                raise RuntimeError(error_msg)
            except Exception as e:
                error_msg = f"Extraction Error : {e}"
                term_service.print_error(error_msg)
                raise RuntimeError(error_msg)

        _ = reply.finished.connect(_when_finished)
        return reply

    def download_inst_async(self, instance: Instance) -> QNetworkReply:
        """_summary_ Download and install the selected Instance

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
                term_service.print_success(
                    f"Installation of {instance.name} was a success"
                )
                if os.name == "posix":
                    exe_path = os.path.join(
                        instance.installation_path, instance.exe_name
                    )
                    _ = self.appContext.sys_man.set_file_permission(exe_path)
            except BadZipFile as e:
                error_msg: str = f"Extraction Error : {e}"
                term_service.print_error(error_msg)
                raise RuntimeError(error_msg)
            except Exception as e:
                error_msg = f"Extraction Error : {e}"
                term_service.print_error(error_msg)
                raise RuntimeError(error_msg)
            else:
                if os.name == "posix":
                    exe_abs_path: str = os.path.join(
                        instance.installation_path, instance.exe_name
                    )
                    system: SystemManager = self.appContext.sys_man
                    _ = system.set_file_permission(exe_abs_path)

        _ = reply.finished.connect(_when_finished)
        return reply

    def extract_inst_async(self, data: ZipFile, instance: Instance) -> None:
        """
        _summary_ : extract the zipfile of the downloaded instance

        Args:
            data : the zip file itself
            instance : the specified instance
        #TODO Make Async
        """
        data.extractall(instance.installation_path)

    def extract_async(self, data: ZipFile, installation_path: str) -> None:
        """
        _summary_ : extract the the data into the specified path

        Args:
            data : the zip file itself
            installation_path : path of the installation/extraction
        #TODO Make Async
        """
        data.extractall(installation_path)
