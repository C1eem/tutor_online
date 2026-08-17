from fastapi import APIRouter, Depends

from dependencies.services import get_user_service
from schemas.users import UserAddDTO
from services.users import UserService

router = APIRouter(prefix="/users")


@router.post("/")
async def create_user_Ivan(
    new_user: UserAddDTO,
    service: UserService = Depends(get_user_service),
):
    res = await service.create_user(new_user)
    return res
