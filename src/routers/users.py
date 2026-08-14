from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from schemas.users import UserAddDTO
from services.users import create_user_ivan

router = APIRouter(prefix="/users")


@router.post("/")
async def create_user_Ivan(
    new_user: UserAddDTO,
    db: AsyncSession = Depends(get_db),
):
    res = await create_user_ivan(new_user, db)
    return res
