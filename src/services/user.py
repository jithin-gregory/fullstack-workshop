import os
from repositories.user import UserRepository
from fastapi import UploadFile
from model.user_dto import UserDTO
from model.user_request import UserRequest
from document.user_document import UserDocument
from passlib.context import CryptContext
import shutil


class UserService:
    def __init__(self):
        self.repo = UserRepository()
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def register_user(self, user: UserRequest):
        user_document = UserDocument(**user.model_dump())
        user_document.password = self.pwd_context.hash(user.password)
        return self.repo.create_user(user_document)

    def authenticate_user(self, username: str, password: str):
        user = self.repo.get_user_by_username(username)
        print(user)
        if not user or not self.pwd_context.verify(password, user.password):
            return None
        return user

    def get_all_users(self):
        users = self.repo.get_all_users()
        user_dto_list = [
            UserDTO(
                id=str(user["_id"]),
                email=user["email"],
                username=user["username"],
                first_name=user["first_name"],
                last_name=user["last_name"],
            )
            for user in users
        ]
        return user_dto_list

    def upload_user_image(self, user_id, file: UploadFile):
        image_dir = "user_images"
        if not os.path.exists(image_dir):
            os.mkdir(image_dir)
        file_path = os.path.join(image_dir, f"{user_id}.jpg")
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        self.repo.update_user_image_path(user_id, file_path)

    def get_user_image(self, user_id):
        user = self.repo.get_user(user_id)
        if user and "image_path" in user:
            return user["image_path"]
        else:
            raise Exception("Image not found")

    def get_user(self, user_id: str):
        user = self.repo.get_user(user_id)
        return UserDTO(
            id=str(user["_id"]),
            email=user["email"],
            username=user["username"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            is_admin=user["is_admin"],
        )
