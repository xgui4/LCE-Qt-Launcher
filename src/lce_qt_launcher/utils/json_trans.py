from PySide6.QtCore import QObject, Signal
import json
import os

from lce_qt_launcher import utils
import lce_qt_launcher.views.term_service as term_service

class JsonTrans(QObject):
    # Correction ici : Pas d'annotation de type sur le signal
    languageChanged = Signal()

    FALLBACK_LANG = "translations"

    def __init__(self, lang_code=None):
        super().__init__()
        self.json_data: dict[str, str] = {}
        self._current_lang = lang_code or self.FALLBACK_LANG
        self.load_lang(self._current_lang)

    def load_lang(self, lang_code: str) -> None:
        file_path = os.path.join(utils.get_locales_dir(), f"{lang_code}.json")
        if not os.path.exists(file_path):
            term_service.print_error(f"{file_path} introuvable.")
            return
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.json_data = json.load(f)
                self._current_lang = lang_code
                self.languageChanged.emit() 
        except Exception as e:
            term_service.print_error("lors du chargement JSON: {e}")

    def translate(self, key: str, default: str = "") -> str:
        return self.json_data.get(key, default or key)
