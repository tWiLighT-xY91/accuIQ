from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/", summary="Health Check")
async def health_check():
    return {
        "status": "healthy",
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "environment": (
            "development"
            if settings.DEBUG
            else "production"
        ),
    }