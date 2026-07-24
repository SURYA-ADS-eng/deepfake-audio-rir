import os
import shutil
from uuid import uuid4

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class UploadService:

    @staticmethod
    def save_file(file):
        extension = os.path.splitext(file.filename)[1]

        filename = f"{uuid4().hex}{extension}"

        filepath = os.path.join(UPLOAD_DIR, filename)

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return filepath
