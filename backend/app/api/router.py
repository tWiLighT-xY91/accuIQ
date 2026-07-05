from fastapi import APIRouter

from app.api.endpoints import course, document, question, occurrence, upload

api_router = APIRouter()

api_router.include_router(course.router)
api_router.include_router(document.router)
api_router.include_router(question.router)
api_router.include_router(occurrence.router)
api_router.include_router(upload.router)