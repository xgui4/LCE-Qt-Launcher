from PySide6.QtWidgets  import QDialog, QHBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

from src.build_info import BuildInfo

class BrowserDialog(QDialog):
    def __init__(self, parent : QWidget, url : str, build_info : BuildInfo):
        super().__init__()
        browser_dialog = QDialog(parent)
        webview = QWebEngineView()
        webview.load(QUrl(url))
        website_title: str = webview.title()
        browser_dialog.setWindowTitle(f"{website_title} - {build_info.app_name}")
        layout = QHBoxLayout()
        layout.addWidget(webview)
        browser_dialog.setLayout(layout)
        browser_dialog.show()