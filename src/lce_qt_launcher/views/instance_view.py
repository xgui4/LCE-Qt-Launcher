from PySide6.QtWidgets  import QDialog, QHBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

from lce_qt_launcher.build_info import BuildInfo

class InstanceView(QDialog):
    """_summary_ #TODO docstring

    Args:
        QDialog (_type_): _description_
    """
    def __init__(self, parent : QWidget, url : str, build_info : BuildInfo) -> None:
        super().__init__()
        browser_dialog = QDialog(parent)
        webview = QWebEngineView()
        webview.load(QUrl(url))
        browser_dialog.setWindowTitle(build_info.app_name)
        layout = QHBoxLayout()
        layout.addWidget(webview)
        browser_dialog.setLayout(layout)
        browser_dialog.show()