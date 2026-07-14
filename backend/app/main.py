from fastapi import FastAPI
from app.api.routes import router as routes_router
from app.api.predict import router as predict_router

app = FastAPI(
    title="AcousticSpace API",
    version="1.0"
)

app.include_router(routes_router)
app.include_router(predict_router)