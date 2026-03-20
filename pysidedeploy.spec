[app]

# title of your application
title = LCE Qt Launcher

# project root directory. default = The parent directory of input_file
project_dir = .

# source file entry point path. default = main.py
input_file = src/main.py

# directory where the executable output is generated
exec_directory = output/

# path to the project file relative to project_dir
project_file = pyproject.toml

# application icon
icon = assets/app.ico

[python]
packages = Nuitka==2.7.11,PySide6
python_packages = Nuitka==2.7.11,PySide6
python_path = .venv/bin/python

[qt]

# qt modules used. comma separated
modules = Core,DBus,Gui,Widgets
qml_files = 
plugins = accessiblebridge,egldeviceintegrations,generic,iconengines,imageformats,platforminputcontexts,platforms,platforms/darwin,platformthemes,styles,xcbglintegrations

[nuitka]

# mode of using nuitka. accepts standalone or onefile. default = onefile
mode = standalone
extra_args = --quiet

[buildozer]

# build mode
mode = release

# architecture of deployed platform
arch = x86_64

