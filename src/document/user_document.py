from pydantic import BaseModel, EmailStr


class UserDocument(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    password: str
    is_admin: bool = False
