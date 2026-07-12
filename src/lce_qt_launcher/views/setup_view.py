import platform

from PySide6.QtWidgets import QMessageBox, QWizard

from PySide6.QtGui import QPixmap

from lce_qt_launcher.ui_setup import Ui_LCE_Qt_Launcher_Wizard


class SetupView(QWizard):
    """_summary_ The Setup UI View

    Args:
        QDialog (_type_): _description_ inherited from QDialog
    """

    def __init__(self) -> None:
        super().__init__()
        self.ui_dialog: Ui_LCE_Qt_Launcher_Wizard = Ui_LCE_Qt_Launcher_Wizard()
        self.dialog: QWizard = QWizard()
        self.ui_dialog.setupUi(self.dialog)  # type: ignore

        if platform.system == "Windows":
            self.dialog.setWizardStyle(QWizard.WizardStyle.AeroStyle)
        if platform.system == "MacOS":
            self.dialog.setWizardStyle(QWizard.WizardStyle.MacStyle)
        else:
            self.dialog.setWizardStyle(QWizard.WizardStyle.ModernStyle)

        icon_pixmap = QPixmap(":/assets/jigsaw-ico.png")
        watermark = QPixmap(":/assets/watermark.png")
        # banner = QPixmap(":/assets/banner.png")
        background_pixmap = QPixmap(":/assets/background.png")

        self.dialog.setPixmap(QWizard.WizardPixmap.LogoPixmap, icon_pixmap)
        self.dialog.setPixmap(QWizard.WizardPixmap.WatermarkPixmap, watermark)
        # self.dialog.setPixmap(QWizard.WizardPixmap.BannerPixmap, banner)
        self.dialog.setPixmap(QWizard.WizardPixmap.BackgroundPixmap, background_pixmap)

        def generate_config() -> None:
            dataSource: str = self.ui_dialog.instanceDataSourceInputBox.text()
            username: str = self.ui_dialog.usernameInputBox.text()

            QMessageBox(QMessageBox.Icon.Information, "LCE Qt Launcher", f"Data Source : {dataSource}\nUsername : {username}").exec()

        self.dialog.finished.connect(generate_config)

        self.dialog.exec()
