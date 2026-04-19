#!/usr/bin/env sh

set -e

rm -rf dist/

rm "src/legacy-qt-launcher/res_rc.py"
rm "src/legacy-qt-launcher/ui_system_info.py"
rm "src/legacy-qt-launcher/ui_form.py"
rm "src/legacy-qt-launcher/ui_instance.py"
rm "src/legacy-qt-launcher/ui_settingDialog.py" 
rm "src/legacy-qt-launcher/ui_about.py"

rm -rf "*/__pycache__"