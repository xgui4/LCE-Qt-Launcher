import platformdirs

def get_user_doc_folder() -> str:
    return platformdirs.user_documents_dir()

def get_user_download_folder() -> str:
    return platformdirs.user_downloads_dir()