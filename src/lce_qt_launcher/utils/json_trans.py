from PySide6.QtCore import QObject, Signal

import json
import os

from lce_qt_launcher import utils
import lce_qt_launcher.views.term_service as term_service

class JsonTrans(QObject):

    languageChanged: Signal = Signal()

    FALLBACK_LANG: str = "translations"

    def __init__(self, lang_code: str = FALLBACK_LANG):
        super().__init__()
        self.json_data : dict[str, str] = {}
        self._current_lang: str = lang_code
        self.load_lang(lang_code)

    def load_lang(self, lang_code: str) -> None:
        file_path: str = os.path.join(utils.get_locales_dir(), f"{lang_code}.json")

        if not os.path.exists(path=file_path):
            term_service.print_error(f"Language file {file_path} not found. Defaulting to English Fallback")
            return
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.json_data = json.load(f)
                self._current_lang = lang_code
                self.languageChanged.emit()
        except Exception as e:
            term_service.print_error(f"loading JSON: {e}. Defaulting to English Fallback.")

    def translate(self, key: str, default: str = "") -> str:
        return self.json_data.get(key, default or key)