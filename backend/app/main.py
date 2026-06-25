from fastapi import FastAPI
from .api.api_v1.api import api_router
from .core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": f"{settings.PROJECT_NAME} API is running"}
