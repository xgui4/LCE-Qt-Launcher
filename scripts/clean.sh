#!/usr/bin/env sh

set -e

rm -rf dist/

rm "src/res_rc.py"
rm "src/ui_system_info.py"
rm "src/ui_form.py"
rm "src/ui_instance.py"
rm "src/ui_settingDialog.py" 
rm "src/ui_about.py"

rm -rf "*/__pycache__"