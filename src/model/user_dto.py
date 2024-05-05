from pydantic import BaseModel

class UserDTO(BaseModel):
    _id: str
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
