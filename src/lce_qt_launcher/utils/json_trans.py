from PySide6.QtCore import QObject, Signal
import json
import os

from lce_qt_launcher import utils
import lce_qt_launcher.views.term_service as term_service

class JsonTrans(QObject):
    languageChanged: Signal = Signal()

    def __init__(self, lang_code : str = "translations") -> None:
        super().__init__()
        self.json_data: dict[str, str] = {}
        self._current_lang: str = lang_code
        self.load_lang(lang_code=self._current_lang)

    def load_lang(self, lang_code: str) -> None:
        file_path: str = os.path.join(utils.get_locales_dir(), f"{lang_code}.json")
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
        return self.json_data.get(key, default or key)
