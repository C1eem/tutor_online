from database import sesison_factory
from models.users import UserORM
from schemas.users import UserAddDTO


async def create_user(user: UserAddDTO):
    async with sesison_factory() as session:
        new_user = UserORM(**user.model_dump())
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user
