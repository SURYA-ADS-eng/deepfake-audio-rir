import os
from pathlib import Path


def create_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def file_exists(file_path):
    return os.path.isfile(file_path)


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower()


def get_filename(file_path):
    return os.path.basename(file_path)


def delete_file(file_path):
    if file_exists(file_path):
        os.remove(file_path)
        return True
    return False
