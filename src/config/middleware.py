from .config import settings
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware


middleware = (
    Middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins.split(","),
        allow_credentials=True,
        allow_methods=["GET", "POST", "HEAD", "OPTIONS"]
    ),
    Middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.allowed_hosts.split(",")
    )
)