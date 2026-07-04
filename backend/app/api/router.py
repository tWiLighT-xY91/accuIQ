from fastapi import APIRouter

from app.api.endpoints import course, document, question, occurrence

api_router = APIRouter()

api_router.include_router(course.router)
api_router.include_router(document.router)