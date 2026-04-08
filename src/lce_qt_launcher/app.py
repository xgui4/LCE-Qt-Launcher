from PySide6.QtWidgets import ( 
    QApplication, 
    QMessageBox, 
)
from PySide6.QtCore import ( 
    QFile, 
    QIODevice 
)

from lce_qt_launcher.gui.theme import Theme
from lce_qt_launcher.gui.launcher import Launcher
from lce_qt_launcher.app_context import AppContext

import lce_qt_launcher.utils as utils
import lce_qt_launcher.term_service as term_service

import os 

class App(QApplication):
    def __init__(self,
                theme :  Theme, 
                launcher_ui : object,
                sys_diag_ui : object,
                instance_editor_ui : object,
                setting_ui : object,
                appContext : AppContext,
                argv : list ):
        super().__init__(argv)        
        self.appContext = appContext

        _ = self.setStyle("Fusion")

        self.widget = Launcher(self.appContext, launcher_ui, sys_diag_ui, instance_editor_ui, setting_ui, self)
        self.widget.show()

        try:
            theme_file : str = theme.value if theme is not None else Theme.MINECRAFT
            file = QFile(theme_file)
            if file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
                content = file.readAll()
                stylesheet = str(content, encoding='utf-8')  # pyright: ignore[reportArgumentType]
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(FileNotFoundError.with_traceback)
            term_service.print_warning("Theme ({theme}) not found in ressource, searching in the local storage.")
            try: 
                with open(os.path.join(utils.get_assets_dir(), "styles", "minecraft.qss"), "r") as file:
                    self.setStyleSheet(file.read())
            except FileNotFoundError:
                _ = QMessageBox.warning(None,"Error", f"{theme} file not found. Reverting to default theme")