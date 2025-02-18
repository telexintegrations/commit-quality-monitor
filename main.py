from fastapi import FastAPI
import uvicorn
from src.config.config import settings
from src.config.middleware import middleware


app = FastAPI(docs_url="/", middleware=middleware)

if __name__ == "__main__":
    reload_value = settings.reload_value.lower() == "true"
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=reload_value)