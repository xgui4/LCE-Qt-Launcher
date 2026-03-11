# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPalette, QPixmap, QBrush

from config import Config

import webbrowser

def launch():
        config = Config()
        print(f"Lauching {config.get_instance_name()} {config.get_instance_version()}")

def update_page():
        webbrowser.open_new_tab("https://github.com/xgui4/LCE_QT_Launcher")

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_launcher

class launcher(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        background_pixmap = QPixmap(":/assets/assets/background.png")
        if not background_pixmap.isNull():
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(background_pixmap))
            self.setPalette(palette)
            self.setAutoFillBackground(True)

        self.ui = Ui_launcher()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(app.quit)
        self.ui.playButton.clicked.connect(launch)

        self.ui.actionUpdate.triggered.connect(update_page)

        self.ui.actionAbout.triggered.connect(self.createPopupMenu)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = launcher()
    widget.show()
    sys.exit(app.exec())
