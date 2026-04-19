#!/usr/bin/env sh

set -e

rm -rf dist/

rm "src/legacy_qt_launcher/res_rc.py"
rm "src/legacy_qt_launcher/ui_system_info.py"
rm "src/legacy_qt_launcher/ui_form.py"
rm "src/legacy_qt_launcher/ui_instance.py"
rm "src/legacy_qt_launcher/ui_settingDialog.py" 
rm "src/legacy_qt_launcher/ui_about.py"

rm -rf "*/__pycache__"