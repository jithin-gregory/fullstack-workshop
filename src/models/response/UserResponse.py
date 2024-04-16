from pydantic import BaseModel

from utils.contants.UserRole import UserRole


class UserResponse(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    user_role: UserRole
