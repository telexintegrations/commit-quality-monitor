from fastapi import FastAPI
import uvicorn
from config import settings


app = FastAPI(docs_url="/")

if __name__ == "__main__":
    reload_value = settings.reload_value.lower() == "true"
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=reload_value)