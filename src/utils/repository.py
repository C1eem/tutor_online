from abc import ABC, abstractmethod
from typing import Any

from sqlalchemy import insert, select

from src.core.database import SessionLocal


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model: Any = None

    async def add_one(self, data: dict) -> int:
        async with SessionLocal() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with SessionLocal() as session:
            query = select(self.model)
            res = await session.execute(query)
            return res.scalars().all()
