from PySide6.QtCore import QSettings

class Config (QSettings):
    def __init__(self):
        super().__init__(QSettings.NativeFormat, QSettings.UserScope, "Xgui4", "LCE QT Laucher")

    def set_instance_url(self, url_str : str):
        super().setValue("instances/repo", url_str)
        super().sync()

    def set_instance_exe_name(self, filename : str):
        super().setValue("instances/filename", filename)
        super().sync()

    def set_instance_archive(self, archive : str):
        super().setValue("instances/archive", archive)
        super().sync()

    def set_instance_name(self, name : str):
        super().setValue("instances/name", name)
        super().sync()

    def set_instance_version(self, version : str):
        super().setValue("instances/version", version)
        super().sync()

    def set_profile_skin(self, skin_file_path : str):
        super().setValue("profiles/skin_file_path", skin_file_path)
        super().sync()

    def set_profile_name(self, name : str):
        super().setValue("profiles/name", name)
        super().sync()

    def get__instance_url(self) -> str:
        return  self.value("instances/repo", "https://github.com/smartcmd/MinecraftConsoles");

    def get_instance_name(self) -> str:
        return self.value("instances/name", "default")
    
    def get_instance_exe_name(self) -> str:
        return self.value("instances/filename", "Minecraft.Client.exe")

    def get_instance_archive(self) -> str:
        return self.value("instances/archive", "LCEWindows64.zip")

    def get_instance_version(self) -> str:
        return self.value("instances/version", "default")

    def get_profile_skin(self) -> str:
        return self.value("profiles/skin_file_path", "default")

    def get_profile_name(self) -> str:
        return self.value("profiles/name", "default")
    
    def generate_default_config(self):
        self.set_instance_url("https://github.com/smartcmd/MinecraftConsoles")
        self.set_instance_name("default")
        self.set_instance_exe_name("Minecraft.Client.exe")
        self.set_instance_archive("LCEWindows64.zip")
        self.set_instance_version("nightly")
        self.set_profile_skin("default")
        self.set_profile_name("Steve")
