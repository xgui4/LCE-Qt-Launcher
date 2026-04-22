from PySide6.QtCore import QObject, Signal

from enum import Enum

from lce_qt_launcher.build_info import BuildInfo
from lce_qt_launcher.managers.downloader import Downloader 

import os

class SourceType(Enum):
    LOCAL = 0
    QT_RESSOURCE = 1
    INTERNET = 2

class Image(QObject):
    """_summary_ An Image Entity

    Args:
        QObject (_type_): _description_ Inherit From QObject
    """

    changed: Signal = Signal()
    
    def __init__(self, 
                location : str, 
                filename : str, 
                img_type : str, 
                source : SourceType,
                buildInfo : BuildInfo,
                parent = None) -> None:
        super().__init__(parent)
        self.location: str = location
        self.filename: str = filename
        self.source: SourceType = source

        if source == SourceType.INTERNET:
            self.downloader: Downloader = Downloader(buildInfo)
            self.setup_image()

    def get_image_path(self) -> str:
        """_summary_ Get the image full path

        Returns:
            str: _description_ the full path in str
        """
        return os.path.join(self.location, self.filename)

    def setup_image(self) -> None:
        """_summary_ Setup an image like downloading the image if online 
        """
        if self.source == SourceType.INTERNET:
            self.downloader.save_file_from_internet(self.location, self.filename)
        else:
            pass