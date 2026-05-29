from PySide6.QtWidgets import QDialog

from lce_qt_launcher.managers import mod_manager
from lce_qt_launcher.ui_contentInstaller import Ui_contentInstallerDialog


class ContentInstallerView(QDialog):
    """_summary_ The Content installer UI View

    Args:
        QDialog (_type_): _description_ inherited from QDialog
    """

    def __init__(self) -> None:
        super().__init__()
        self.ui_dialog: Ui_contentInstallerDialog = Ui_contentInstallerDialog()
        self.dialog: QDialog = QDialog()
        self.ui_dialog.setupUi(self.dialog)

        self.contentToInstallPath : str = ""
        self.instancePath : str = ""
        self.contentTypeStr : str = ""

        self.contentToInstallPath = self.ui_dialog.contentToInstallInputBox.text()
        self.contentTypeStr = self.ui_dialog.contentTypeComboBox.currentText()
        self.instancePath = self.ui_dialog.instamcePathInputPath.text()

        def installContentCommand():
            self.contentToInstallPath = self.ui_dialog.contentToInstallInputBox.text()
            self.contentTypeStr = self.ui_dialog.contentTypeComboBox.currentText()
            self.instancePath = self.ui_dialog.instamcePathInputPath.text()
            mod_manager.install_content(
                self.instancePath,
                mod_manager.from_str_to_enum(self.contentTypeStr),
                self.contentToInstallPath,
            )

        self.ui_dialog.mainButtonBox.clicked.connect(installContentCommand)

        self.dialog.show()
