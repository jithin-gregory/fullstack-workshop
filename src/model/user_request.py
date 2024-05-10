from pydantic import BaseModel


class UserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
