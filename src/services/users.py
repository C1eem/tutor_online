from sqlalchemy.ext.asyncio import AsyncSession

from core.security import hash_password
from repositories.users import create_user
from schemas.users import UserAddDTO, UserCreateInDB


async def create_user_ivan(
    new_user: UserAddDTO,
    db: AsyncSession,
):
    user = UserCreateInDB(
        **new_user.model_dump(exclude={"password"}),
        hashed_password=hash_password(new_user.password)
    )
    return await create_user(user, db)
