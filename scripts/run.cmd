@echo off

call .venv/Scripts/activate.bat || exit /b 1

python src/main.py || exit /b 1