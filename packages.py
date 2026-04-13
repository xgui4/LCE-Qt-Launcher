import os
import subprocess

if os.name == "posix":
    subprocess.run("./scripts/packages.sh", check=True)
if os.name == "nt":
    subprocess.run("scripts/packages.cmd", check=True, shell=True)