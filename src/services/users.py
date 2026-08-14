from sqlalchemy.ext.asyncio import AsyncSession

from repositories.users import create_user
from schemas.users import UserAddDTO


async def create_user_ivan(
    new_user: UserAddDTO,
    db: AsyncSession,
):
    res = await create_user(new_user, db)
    return res
