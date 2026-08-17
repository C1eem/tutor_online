from sqlalchemy.ext.asyncio import AsyncSession

from core.security import hash_password
from repositories.users import UserRepository
from schemas.users import UserAddDTO, UserCreateInDB


class UserService:

    def __init__(self, db: AsyncSession) -> None:
        self.db = db
        self.user_repo = UserRepository(self.db)

    async def create_user(self, new_user: UserAddDTO):

        user_data = UserCreateInDB(
            **new_user.model_dump(exclude={"password"}),
            hashed_password=hash_password(new_user.password),
        )
        return await self.user_repo.create_user(user_data)
