import os
import subprocess

if os.name == "posix":
    subprocess.run("./packages.sh", check=True)
if os.name == "nt":
    subprocess.run("packages.bat", check=True, shell=True)