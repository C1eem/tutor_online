from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from services.admin import delete_user_service, select_all_users_service

router = APIRouter(prefix="/admin", tags=["admin"])


@router.delete("/users/{user_id}")
async def delete_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    await delete_user_service(user_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/users")
async def get_all_users(
    db: AsyncSession = Depends(get_db),
):
    return await select_all_users_service(db)
