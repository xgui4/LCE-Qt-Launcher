pyside6-rcc "res.qrc" -o "src\res_rc.py" &&
pyside6-uic "src\system_info.ui" -o "src\ui_system_info.py" &&
pyside6-uic "src\form.ui" -o "src\ui_form.py"