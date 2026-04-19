@echo off

call .venv\Scripts\activate.bat || exit /b 1

python src\legacy-qt-launcher\main.py || exit /b 1