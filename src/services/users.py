from repositories.users import create_user
from schemas.users import UserAddDTO


async def create_user_ivan(new_user: UserAddDTO):
    res = await create_user(new_user)
    return res
