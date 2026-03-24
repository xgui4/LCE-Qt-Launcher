from PySide6.QtWidgets  import QDialog, QHBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

from build_info import BuildInfo

class BrowserDialog(QDialog):
    def __init__(self, parent, url : str, build_info : BuildInfo):
        browser_dialog = QDialog(parent)
        webview = QWebEngineView()
        webview.load(QUrl(url))
        website_title = webview.title()
        browser_dialog.setWindowTitle(f"{website_title} - {build_info.title}")
        layout = QHBoxLayout()
        layout.addWidget(webview)
        browser_dialog.setLayout(layout)
        browser_dialog.show()