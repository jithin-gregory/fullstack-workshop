from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    user_role: int
    password: str
