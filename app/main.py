from fastapi import FastAPI
from app.controllers.gemini_controller import router

app = FastAPI()
app.include_router(router, prefix="/v1beta")