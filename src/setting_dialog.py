from PySide6.QtWidgets  import QDialog, QVBoxLayout, QLabel

class SettingDialog(QDialog):
    def __init__(self, parent):
        setting_dialog = QDialog(parent)
        layout = QVBoxLayout()

        label = QLabel("Setting")
        layout.addWidget(label)

        label2 = QLabel("Coming Soon!")
        layout.addWidget(label2)

        setting_dialog.setLayout(layout)
        setting_dialog.show()