from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    password: str
