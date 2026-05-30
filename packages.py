import os
import subprocess

if os.name == "posix":
    _ = subprocess.run("./scripts/packages.sh", check=True)
if os.name == "nt":
    _ = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "scripts\\packages.ps1"], check=True, shell=True)
