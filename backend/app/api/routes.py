from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter()

UPLOAD_FOLDER = "uploads"

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.get("/")
def home():
    return {
        "message": "Welcome to AcousticSpace API"
    }


@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    """
    Upload an audio file (.wav or .mp3)
    """

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "status": "Uploaded Successfully"
    }