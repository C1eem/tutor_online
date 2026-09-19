from pydantic import BaseModel, EmailStr

from src.models.users import UserRole


class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    middle_name: str | None
    role: UserRole


class UserAddDTO(UserCreate):
    password: str


class UserCreateInDB(UserCreate):
    hashed_password: str


class UserResponseDTO(UserCreate):
    pass


class UserLoginSchema(BaseModel):
    username: str
    password: str
