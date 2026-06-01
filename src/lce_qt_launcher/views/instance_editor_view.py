from PySide6.QtWidgets import QDialog, QWidget
from PySide6.QtGui import QPixmap

from lce_qt_launcher.managers.instance_manager import Instance
from lce_qt_launcher.ui_instance import Ui_InstancesEditor

from lce_qt_launcher import (
    app_name_str,
)


class InstanceEditorView(QDialog):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.instance_window: QDialog = QDialog()
        self.instance_editor: Ui_InstancesEditor = Ui_InstancesEditor()
        self.instance_editor.setupUi(self.instance_window)
        self.instance_window.setWindowTitle(app_name_str)

        self.instance_window.show()

    def loadInstance(self, instance : Instance):
        self.instance_editor.instanceNameInputBox.setText(instance.name)
        self.instance_editor.usernameInputBox.setText(instance.username)
        self.instance_editor.repoURLInputBox.setText(instance.repo_url)
        self.instance_editor.versionsComboBox.setCurrentText(instance.version)
        self.instance_editor.pathInputBox.setText(instance.installation_path)
        image_pixmap = QPixmap(instance.image)
        self.instance_editor.instanceLogo.setPixmap(image_pixmap)
        self.instance_editor.steamLinkValue.setText(instance.image)