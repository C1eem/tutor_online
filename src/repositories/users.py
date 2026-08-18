from sqlalchemy.ext.asyncio import AsyncSession

from src.models.users import UserORM
from src.schemas.users import UserCreateInDB


class UserRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def create_user(self, user: UserCreateInDB):
        new_user = UserORM(**user.model_dump())
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user
