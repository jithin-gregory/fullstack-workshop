from pydantic import BaseModel

from utils.contants.UserRole import UserRole


class UserResponse(BaseModel):
    id: str
    email: str
    username: str
    first_name: str
    last_name: str
    user_role: UserRole
