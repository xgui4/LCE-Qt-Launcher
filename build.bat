@echo off

pyside6-rcc "res.qrc" -o "src\res_rc.py"
pyside6-uic "src\system_info.ui" -o "src\ui_system_info.py"
pyside6-uic "src\form.ui" -o "src\ui_form.py"
pyside6-uic "src\instance.ui" -o "src\ui_instance.py"
pyside6-uic "src\settingDialog.ui" -o "src\ui_settingDialog.py" 
pyside6-uic "src\about.ui" -o "src\ui_about.py" 
