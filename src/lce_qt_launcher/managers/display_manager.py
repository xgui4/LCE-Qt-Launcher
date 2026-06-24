from enum import Enum

import lce_qt_launcher.views.term_service as term_service

from PySide6.QtWidgets import QMessageBox, QWidget


class DisplayType(Enum):
    """_summary_ The display/loggin type : Console/Terminal, MessageBox (Qt), Mixed (both)"""

    CONSOLE = 0
    QMESSAGE_BOX = 1
    MIXED = 2


class DisplayManager:
    """_summary_ The Display Manager Handler that will us the correct dysplay type"""

    def __init__(self, type: DisplayType, parentWindow: QWidget | None = None) -> None:
        self.type: DisplayType = type
        if parentWindow is not None:
            self.parentWindow: QWidget = parentWindow

    def displayInfo(self, msg: str, title: str = "Information") -> None:
        """_summary_
            Display Information with a msg and a title
        Args:
            msg (str): _description_ : the body message
            title (str, optional): _description_ the title of the message. (Do not apply if type is Console) Defaults to "Information".
        """
        if self.type == DisplayType.CONSOLE or DisplayType.MIXED:
            term_service.print_information(msg)
        if self.type == DisplayType.QMESSAGE_BOX or DisplayType.MIXED:
            QMessageBox.information(self.parentWindow, title, msg)

    def displayWarn(self, msg: str, title: str = "Warning") -> None:
        """_summary_
            Display Warning with a msg and a title
        Args:
            msg (str): _description_ : the body message
            title (str, optional): _description_. The title of the message (Do not apply if type is Console). Defaults to "Warning".
        """
        if self.type == DisplayType.CONSOLE or DisplayType.MIXED:
            term_service.print_warning(msg)
        if self.type == DisplayType.QMESSAGE_BOX or DisplayType.MIXED:
            QMessageBox.warning(self.parentWindow, title, msg)

    def displayError(self, msg: str, title: str = "❗Error") -> None:
        """_summary_
            Display Error with a msg and a title
        Args:
            msg (str): _description_ the body message
            title (str | None, optional): _description_.  The title of the message (Do not apply if type is Console). Defaults to "❗Error".
        """
        if self.type == DisplayType.CONSOLE or DisplayType.MIXED:
            term_service.print_error(msg)
        if self.type == DisplayType.QMESSAGE_BOX or DisplayType.MIXED:
            QMessageBox.critical(
                self.parentWindow,
                title,
                msg,
            )
