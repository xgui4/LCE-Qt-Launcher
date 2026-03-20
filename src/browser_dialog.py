from PySide6.QtWidgets  import QDialog, QHBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

class BrowserDialog(QDialog):
    def __init__(self, parent, url : str):
        browser_dialog = QDialog(parent)
        webview = QWebEngineView()
        webview.load(QUrl(url))
        layout = QHBoxLayout()
        layout.addWidget(webview)
        browser_dialog.setLayout(layout)
        browser_dialog.show()