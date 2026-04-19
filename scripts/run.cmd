@echo off

call .venv\Scripts\activate.bat || exit /b 1

python src\legacy_qt_launcher\main.py || exit /b 1