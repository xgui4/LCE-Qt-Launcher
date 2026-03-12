from instance_manager import Instance

import requests
import zipfile
import io

SUCCESS_STATUS_CODE = 200

class Downloader:
    def __init__(self, instance : Instance):
        self.instance: Instance = instance 

    def download_client(self):
        response = requests.get(self.instance)

        if response.status_code == SUCCESS_STATUS_CODE:
            try:
                with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
                    archive.extractall(self.installation_path)
            except zipfile.BadZipFile as err:
                print(f"Error : {err} while extracting {archive.filename}")
            except zipfile.zipfile.LargeZipFile as err:
                print(f"Error : {archive.filename} was too big.")
        else:
            print(f"Error : {response.status_code} during the dowbloading of the Minecraft LCE Client")