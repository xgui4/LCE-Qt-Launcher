import os
import subprocess

if os.name == "posix":
    _ = subprocess.run("./scripts/packages.sh", check=True)
if os.name == "nt":
    _ = subprocess.run("scripts\\packages.cmd", check=True, shell=True)