from sqlalchemy.ext.asyncio import AsyncSession

from src.models.users import UserORM
from src.schemas.users import UserCreateInDB
from src.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = UserORM
