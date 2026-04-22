import os

from PySide6.QtCore import QByteArray, QFile, QIODevice
from PySide6.QtWidgets import QApplication, QMessageBox

from lce_qt_launcher.app_context import AppContext
from lce_qt_launcher.models.app_data import AppData
from lce_qt_launcher.views.launcher import Launcher
from lce_qt_launcher.views.theme import Theme
import lce_qt_launcher.views.term_service as term_service

class App(QApplication):
    """QApplication Main Instance"""
    def __init__(self,
                theme :  Theme, 
                appContext : AppContext,
                argv : list[str] ) -> None:
        super().__init__(argv)        
        self.appContext: AppContext = appContext
        self.appData: AppData = AppData()

        _ = self.setStyle("Fusion")

        self.widget: Launcher = Launcher(self.appContext, self)
        self.widget.show()

        self.set_theme(theme)
        
    def set_theme(self, theme : Theme) -> None:
        """#Set Application Theme using a pretermined theme
        #TODO To Upgrade!
        """
        try:
            theme_file : str = theme
            file = QFile(theme_file)
            if file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
                content: QByteArray = file.readAll()
                stylesheet: str = str(content, encoding='utf-8')    # pyright: ignore[reportArgumentType]
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(FileNotFoundError.with_traceback)
            term_service.print_warning(f"Theme ({theme}) not found in ressource, searching in the local storage.")
            try: 
                with open(os.path.join(self.appData.assetsDirs, "styles", "minecraft.qss"), "r") as file:
                    self.setStyleSheet(file.read())
            except FileNotFoundError:
                _ = QMessageBox.warning(None,"Error", f"{theme} file not found. Reverting to default theme")