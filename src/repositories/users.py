from sqlalchemy.ext.asyncio import AsyncSession

from models.users import UserORM
from schemas.users import UserAddDTO, UserCreateInDB


class UserRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def create_user(self, user: UserAddDTO):
        new_user = UserORM(**user.model_dump())
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user
