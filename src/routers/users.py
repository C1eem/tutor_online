from fastapi import APIRouter

from schemas.users import UserAddDTO
from services.users import create_user_ivan

router = APIRouter(prefix="/users")


@router.post("/")
async def create_user_Ivan(new_user: UserAddDTO):
    res = await create_user_ivan(new_user)
    return res
