from fastapi import APIRouter

from src.api.admin import router as admin_router
from src.api.auth import router as auth_router
from src.api.users import router as user_router

main_router = APIRouter()

main_router.include_router(admin_router)
main_router.include_router(auth_router)
main_router.include_router(user_router)
