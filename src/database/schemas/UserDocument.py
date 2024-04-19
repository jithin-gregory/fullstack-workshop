from .BaseDocument import BaseDocument


class UserDocument(BaseDocument):
    email: str
    username: str
    first_name: str
    last_name: str
    user_role: int
    password: str
