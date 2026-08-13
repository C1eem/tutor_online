from pydantic import BaseModel, EmailStr, Field

from models.users import UserRole


class UserAddDTO(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    middle_name: str | None
    role: UserRole
