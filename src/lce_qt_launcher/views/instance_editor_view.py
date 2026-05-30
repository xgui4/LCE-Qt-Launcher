from PySide6.QtWidgets import QDialog, QWidget

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
