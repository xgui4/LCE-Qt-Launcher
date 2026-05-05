from PySide6.QtWidgets  import QDialog, QHBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

from lce_qt_launcher.managers import mod_manager
from lce_qt_launcher.ui_contentInstaller import Ui_Dialog
from lce_qt_launcher.views import term_service


class ContentInstallerView(QDialog):
    """ #TODO _summary_  

    Args:
        QDialog (_type_): _description_ inherited from QDialog
    """
    def __init__(self) -> None:
        super().__init__()
        self.ui_dialog: Ui_Dialog = Ui_Dialog()
        self.dialog: QDialog = QDialog()
        self.ui_dialog.setupUi(self.dialog)

        self.contentToInstallPath = ""
        self.instancePath = ""
        self.contentTypeStr = ""

        self.contentToInstallPath = self.ui_dialog.contentToInstallInputBox.text()
        self.contentTypeStr = self.ui_dialog.contentTypeComboBox.currentText()
        self.instancePath = self.ui_dialog.instamcePathInputPath.text()

        def installContentCommand():
            self.contentToInstallPath = self.ui_dialog.contentToInstallInputBox.text()
            self.contentTypeStr = self.ui_dialog.contentTypeComboBox.currentText()
            self.instancePath = self.ui_dialog.instamcePathInputPath.text()
            mod_manager.install_content(self.instancePath, mod_manager.from_str_to_enum(self.contentTypeStr), self.contentToInstallPath)

        self.ui_dialog.mainButtonBox.clicked.connect(installContentCommand)

        self.dialog.show()

