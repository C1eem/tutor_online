from fastapi import APIRouter, Depends

from src.dependencies.services import get_user_service
from src.schemas.users import UserAddDTO, UserResponseDTO
from src.services.users import UserService

router = APIRouter(prefix="/users")


@router.post("/")
async def create_user(
    new_user: UserAddDTO,
    service: UserService = Depends(get_user_service),
) -> int:
    return await service.add_user(new_user)
