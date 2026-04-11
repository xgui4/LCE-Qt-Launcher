from PySide6.QtCore import QObject , Property, Signal

from enum import Enum

from lce_qt_launcher.managers.downloader import Downloader 

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
        self.img_type = img_type
        self.source = source

        if source == SourceType.INTERNET:
            self.downloader = Downloader()

    def get_path(self):
        pass

    def setup_image(self):
        if self.source == SourceType.INTERNET:
            Downloader().save_file_from_internet(self.location, self.filename, self.img_type)
        else:
            pass