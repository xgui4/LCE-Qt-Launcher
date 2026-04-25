@echo off

echo "Activate the python venv"
call .venv\Scripts\activate.bat || exit /b 1
echo "done"

python src\lce_qt_launcher\main.py || exit /b 1