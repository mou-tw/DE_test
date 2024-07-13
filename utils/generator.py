import os

file_base_path = "/DE_TEST"

def ensure_directory_exists(path):
    """
    Check if a directory exists at the given path.
    If the directory does not exist, create it.

    """
    if not os.path.exists(path):
        os.makedirs(path)
