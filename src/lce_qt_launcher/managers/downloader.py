from lce_qt_launcher.app_context import AppContext
import lce_qt_launcher.views.term_service as term_service

from zipfile import ZipFile

from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

from PySide6.QtCore import (
    QUrl,
    QObject,
)

from io import BytesIO

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

    def download_async(self, url_str: str, installation_path : str, object_name: str) -> QNetworkReply:
        """_summary_
            Download Content from the internet from s certain url and a object_name
        Args:
            url_str (str): _description_ the url of the content to download
            object_name (str): _description_ the name of the object name
        Returns:
            QNetworkReply: _description_ the QNetworkReply to use for updating the ui/tui and get information about the downlaod
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
            with ZipFile(BytesIO(data)) as archive:
                _ = self.extract_async(archive, installation_path)
            term_service.print_success(
                f"Installation of {object_name} was a success"
            )
        _ = reply.finished.connect(_when_finished)
        return reply

    def extract_async(self, data: ZipFile, installation_path: str) -> None:
        """
        _summary_ : extract the the data into the specified path

        Args:
            data : the zip file itself
            installation_path : path of the installation/extraction
        #FIXME Make Async
        """
        data.extractall(installation_path)
