from pydantic import BaseModel, EmailStr

from models.users import UserRole


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
