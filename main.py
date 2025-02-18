from fastapi import FastAPI
from src.config.middleware import middleware
from src.routers.router import webhook_router
from src.config.config import settings
import uvicorn


app = FastAPI(docs_url="/", middleware=middleware)
app.include_router(webhook_router)

if __name__ == "__main__":
    reload_value = settings.reload_value.lower() == "true"
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=reload_value)
