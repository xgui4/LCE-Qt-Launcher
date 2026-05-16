# TODO : doctstring and more functions

from enum import Enum

import lce_qt_launcher.views.term_service as term_service

from PySide6.QtWidgets import QMessageBox, QWidget


class DisplayType(Enum):
    CONSOLE = 0
    QMESSAGE_BOX = 1
    MIXED = 2


class DisplayManager:
    def __init__(self, type: DisplayType, parentWindow: QWidget | None = None) -> None:
        self.type: DisplayType = type
        if parentWindow != None:
            self.parentWindow: QWidget = parentWindow

    def displayInfo(self, msg: str, title: str | None = None) -> None:
        if self.type == DisplayType.CONSOLE or DisplayType.MIXED:
            term_service.print_information(msg)
        if self.type == DisplayType.QMESSAGE_BOX or DisplayType.MIXED:
            QMessageBox.information(
                self.parentWindow, title if not None else "Information", msg
            )  # pyright: ignore[reportArgumentType, reportUnusedCallResult]

    def displayWarn(self, msg: str, title: str | None = None) -> None:
        if self.type == DisplayType.CONSOLE or DisplayType.MIXED:
            term_service.print_warning(msg)
        if self.type == DisplayType.QMESSAGE_BOX or DisplayType.MIXED:
            QMessageBox.warning(
                self.parentWindow, title if not None else "⚠️ Warning!", msg
            )  # pyright: ignore[reportArgumentType, reportUnusedCallResult]

    def displayError(self, msg: str, title: str | None = None) -> None:
        if self.type == DisplayType.CONSOLE or DisplayType.MIXED:
            term_service.print_error(msg)
        if self.type == DisplayType.QMESSAGE_BOX or DisplayType.MIXED:
            QMessageBox.critical(
                self.parentWindow, title if not None else "❗ Error", msg
            )  # pyright: ignore[reportArgumentType, reportUnusedCallResult]
