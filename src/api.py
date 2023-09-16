from fastapi.routing import APIRouter
from src.to_do.views import router as todo_views

api_router = APIRouter()

api_router.include_router(todo_views, prefix="/to_do", tags=["To Do List"])
