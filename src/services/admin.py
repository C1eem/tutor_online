from sqlalchemy.ext.asyncio import AsyncSession

from repositories.admin import delete_user_by_id, get_all_users


async def delete_user_service(
    user_id: int,
    db: AsyncSession,
):
    await delete_user_by_id(user_id, db)


async def select_all_users_service(
    db: AsyncSession,
):
    return await get_all_users(db)
