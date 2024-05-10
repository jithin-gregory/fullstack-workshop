from repositories.user import UserRepository
from model.user_request import UserRequest
from document.user_document import UserDocument
from passlib.context import CryptContext


class UserService:
    def __init__(self):
        self.repo = UserRepository()
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def register_user(self, user: UserRequest):
        user_document = UserDocument(**user.model_dump())
        user_document.password = self.pwd_context.hash(user.password)
        return self.repo.create_user(user_document)
