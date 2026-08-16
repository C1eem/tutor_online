from sqlalchemy.ext.asyncio import AsyncSession

from models.users import UserORM
from schemas.users import UserCreateInDB


async def create_user(
    user: UserCreateInDB,
    db: AsyncSession,
):
    new_user = UserORM(**user.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
