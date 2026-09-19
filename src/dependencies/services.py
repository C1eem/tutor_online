from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.repositories.users import UserRepository
from src.services.users import UserService


async def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(db)
