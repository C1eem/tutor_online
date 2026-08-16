from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.users import UserORM


async def delete_user_by_id(
    user_id: int,
    db: AsyncSession,
):
    query = delete(UserORM).where(UserORM.id == user_id)
    await db.execute(query)
    await db.commit()
    return


async def get_all_users(
    db: AsyncSession,
):
    query = select(UserORM)
    res = await db.execute(query)
    return res.scalars().all()
