from fastapi import APIRouter, Depends

from src.dependencies.services import get_user_service
from src.schemas.users import UserAddDTO, UserResponseDTO
from src.services.users import UserService

router = APIRouter(prefix="/users")


@router.post("/", response_model=UserResponseDTO)
async def create_user(
    new_user: UserAddDTO,
    service: UserService = Depends(get_user_service),
):
    return await service.create_user(new_user)
