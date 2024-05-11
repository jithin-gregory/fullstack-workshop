from pydantic import BaseModel, EmailStr


class UserDTO(BaseModel):
    id: str
    email: EmailStr
    username: str
    first_name: str
    last_name: str
