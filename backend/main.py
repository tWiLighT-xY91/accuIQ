from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import router
from app.core.config import settings
from app.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("=" * 50)
    logger.info(f"Starting {settings.PROJECT_NAME}")
    logger.info(f"Version: {settings.PROJECT_VERSION}")
    logger.info("=" * 50)

    yield

    logger.info(f"Shutting down {settings.PROJECT_NAME}")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="AI-powered Academic Intelligence Platform",
    lifespan=lifespan,
)

app.include_router(router)