pyside6-rcc "res.qrc" -o "src\res_rc.py" || exit /b 1
pyside6-uic "src\system_info.ui" -o "src\ui_system_info.py" || exit /b 1
pyside6-uic "src\form.ui" -o "src\ui_form.py" || exit /b 1
pyside6-uic "src\instance.ui" -o "src\ui_instance.py" || exit /b 1
pyside6-uic "src\settingDialog.ui" -o "src\ui_settingDialog.py" || exit /b 1
pyside6-uic "src\about.ui" -o "src\ui_about.py" || exit /b 1