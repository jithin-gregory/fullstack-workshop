from pydantic import BaseModel


class UserDTO(BaseModel):
    id: str
    email: str
    username: str
    first_name: str
    last_name: str
    is_admin: bool = False
