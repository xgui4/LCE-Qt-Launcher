from PySide6.QtWidgets import QWizard

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
        self.ui_dialog.setupUi(self.dialog)

        icon_pixmap = QPixmap(":/assets/jigsaw-ico.png")
        background_pixmap = QPixmap(":/assets/background.png")

        self.dialog.setPixmap(QWizard.WizardPixmap.LogoPixmap, icon_pixmap)
        # self.dialog.setPixmap(QWizard.WizardPixmap.WatermarkPixmap, background_pixmap)
        # self.dialog.setPixmap(QWizard.WizardPixmap.BannerPixmap, background_pixmap)
        self.dialog.setPixmap(QWizard.WizardPixmap.BackgroundPixmap, background_pixmap)

        def generate_config():
            dataSource : str = self.ui_dialog.instanceDataSourceInputBox.text()
            username : str = self.ui_dialog.usernameInputBox.text()

            print(f"data source : {dataSource}\nusername : {username}")

        self.dialog.finished.connect(generate_config)

        self.dialog.exec()
