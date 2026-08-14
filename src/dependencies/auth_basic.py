from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from models.users import UserORM

security = HTTPBasic()


async def get_current_user_basic(
    credentials: HTTPBasicCredentials = Depends(security),
    db: AsyncSession = Depends(get_db),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
    query = select(UserORM).where(
        UserORM.email == credentials.username, UserORM.password == credentials.password
    )

    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if not user:
        raise unauthed_exc
    return user
