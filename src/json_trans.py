from PySide6.QtCore import QObject, Signal

import json
import os

import build_info


class JsonTrans(QObject):

    languageChanged: Signal = Signal()  # Signal QT about the language changes

    FALLBACK_LANG: str = "en"

    def __init__(self, lang_code: str = FALLBACK_LANG):
        super().__init__()
        self.json_data : dict[str, str] = {}
        self._current_lang = lang_code
        self.load_lang(lang_code)

    def load_lang(self, lang_code: str):
        file_path: str = os.path.join(build_info.os, f"{lang_code}.json")

        if not os.path.exists(path=file_path):
            print(f"Error: Language file {file_path} not found. Defaulting to English Fallback.")
            return

        try:
            with open(file_path, "r", "utf-8") as f:
                self.json_data = json.load(f)
                self._current_lang = lang_code
                self.languageChanged.emit()  # Notify the UI
        except Exception as e:
            print(f"Error loading JSON: {e}. Defaulting to English Fallback.")

    def translate(self, key: str, default: str = "") -> str:
        return self.json_data.get(key, default or key)