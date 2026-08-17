from sqlalchemy.ext.asyncio import AsyncSession

from repositories.users import UserRepository
from schemas.users import UserAddDTO


class UserService:

    def __init__(self, db: AsyncSession) -> None:
        self.db = db
        self.user_repo = UserRepository(self.db)

    async def create_user(self, new_user: UserAddDTO):
        res = await self.user_repo.create_user(new_user)
        return res
