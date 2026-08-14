from sqlalchemy.ext.asyncio import AsyncSession

from models.users import UserORM
from schemas.users import UserAddDTO


async def create_user(
    user: UserAddDTO,
    db: AsyncSession,
):
    new_user = UserORM(**user.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
