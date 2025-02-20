from fastapi.routing import APIRouter
from .github import router as github_router
from .telex import router as telex_router


webhook_router = APIRouter(prefix="/api/v1/webhook")
webhook_router.include_router(github_router)
webhook_router.include_router(telex_router)