import os

ALLOWED_EXTENSIONS = {".wav", ".mp3", ".flac", ".ogg"}

def allowed_file(filename):
    ext = os.path.splitext(filename)[1].lower()
    return ext in ALLOWED_EXTENSIONS

def validate_audio_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")

    if not allowed_file(file_path):
        raise ValueError("Unsupported audio format")

    return True
