import os
import sys

from pathlib import Path

def get_source_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))

def get_project_root_dir() -> str:
    if "__compiled__" in globals():
        return Path(get_source_dir())
    else:
        dir: Path = Path(get_source_dir())
        return str(dir.parent.parent)

def get_locales_dir() -> str:
    return os.path.join(get_project_root_dir(),"assets", "languages")

def get_assets_dir() -> str:
    return os.path.join(get_project_root_dir(), "assets")
