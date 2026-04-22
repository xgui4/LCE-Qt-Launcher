from PySide6.QtCore import QObject, Signal
import json
import os

import lce_qt_launcher.models.app_data as AppData
import lce_qt_launcher.views.term_service as term_service

class JsonTrans(QObject):
    """_summary_ The JSON Translators. Translating str with a json locales file

    Args:
        QObject (_type_): _description_ inherited from QObject
    """
    languageChanged: Signal = Signal()

    def __init__(self, appData : AppData.AppData, lang_code : str = "translations") -> None:
        super().__init__()
        self.json_data: dict[str, str] = {}
        self._current_lang: str = lang_code
        self.appDataManager : AppData.AppData = appData
        self.load_lang(lang_code=self._current_lang)

    def load_lang(self, lang_code: str) -> None:
        """_summary_ load an languages

        Args:
            lang_code (str): _description_ : the language code of the language to enabled
        """
        file_path: str = os.path.join(self.appDataManager.localesDir, f"{lang_code}.json")
        if not os.path.exists(file_path):
            term_service.print_error(f"{file_path} introuvable.")
            return
        try:
            with open(file=file_path, mode="r", encoding="utf-8") as f:
                self.json_data = json.load(f)
                self._current_lang = lang_code
                self.languageChanged.emit() 
        except Exception as e:
            term_service.print_error(f"lors du chargement JSON: {e}")

    def translate(self, key: str, default: str = "") -> str:
        """_summary_ Get the localized Text from a key and a fallback (attr default)

        Args:
            key (str): _description_ : the key of the locaziled text 
            default (str, optional): _description_. Defaults to "". : the fallback tr

        Returns:
            str: _description_ : the locaziled str
        """
        return self.json_data.get(key, default or key)
