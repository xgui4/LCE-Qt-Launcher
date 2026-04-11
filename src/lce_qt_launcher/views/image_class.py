from PySide6.QtCore import QObject

from enum import Enum

class SourceType(Enum):
    LOCAL = 0
    QT_RESSOURCE = 1
    INTERNER = 2


class Image(QObject):
    def __init__(self, url : str, parent = ..., *, objectName = ...):
        super().__init__(parent, objectName=objectName)