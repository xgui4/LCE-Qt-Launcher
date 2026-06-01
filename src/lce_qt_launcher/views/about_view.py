import platform

from PySide6.QtWidgets import QDialog, QWidget

from lce_qt_launcher import features

from lce_qt_launcher.ui_about import Ui_AboutDialog

from lce_qt_launcher import (
    app_name_str,
    version_str,
    version_type_str,
    git_repo_url_str,
    license_text_str,
)


class AboutView(QDialog):
    def showAboutQtActionCommand(self) -> None:
        """_summary_ Show the About Qt Dialog"""
        features.show_about_qt(self)

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.about: Ui_AboutDialog = Ui_AboutDialog()
        self.aboutDialog: QDialog = QDialog()

        self.about.setupUi(self.aboutDialog)

        self.about.title.setText(app_name_str)
        self.about.versionLabel.setText(f"{version_str}")
        self.about.urlLabel.setText(git_repo_url_str)
        self.about.creditsText.setText("Xgui4")
        self.about.copyLabel.setText("Copyleft (C) GPLv3 Xgui4")
        self.about.channelLabel.setText(f"**Channel** : {version_type_str}")
        self.about.platformLabel.setText(f"**Platform** : {platform.release()}")

        self.about.licenseText.setMarkdown(license_text_str)
        self.about.aboutQt.clicked.connect(self.showAboutQtActionCommand)
        self.about.closeButton.clicked.connect(self.aboutDialog.close)

        self.aboutDialog.show()
