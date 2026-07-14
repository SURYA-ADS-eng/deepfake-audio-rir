from fastapi import FastAPI

app = FastAPI(
    title="AcousticSpace API",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "project": "AcousticSpace",
        "status": "Running"
    }