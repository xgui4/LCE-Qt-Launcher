from PySide6.QtCore import QObject , Property, Signal

from enum import Enum

from lce_qt_launcher.managers.downloader import Downloader 

import os

class SourceType(Enum):
    LOCAL = 0
    QT_RESSOURCE = 1
    INTERNET = 2

class Image(QObject):

    changed = Signal()
    
    def __init__(self, location : str, filename : str, img_type : str, source : SourceType, parent = None):
        super().__init__(parent)
        self.location = location
        self.filename = filename
        self.source = source

        if source == SourceType.INTERNET:
            self.downloader = Downloader()
            self.setup_image()

    def get_image_path(self):
        return os.path.join(self.location, self.filename)

    def setup_image(self):
        if self.source == SourceType.INTERNET:
            Downloader().save_file_from_internet(self.location, self.filename)
        else:
            pass