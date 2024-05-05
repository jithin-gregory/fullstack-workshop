import uuid

from fastapi import Depends, HTTPException

from database.repositories import UserRepository
from database.schemas import UserDocument
from models.request import CreateUserRequest
from models.response import UserResponse
from services.image_service import ImageService
from utils.password_helper import hash_password


class UserService:
    def __init__(self, user_repository: UserRepository = Depends(UserRepository)):
        self.user_repository = user_repository

    def create_user(self, request: CreateUserRequest):
        if self.is_user_exists(request.username):
            raise HTTPException(status_code=400, detail='User already exists')

        user = UserDocument(id=str(uuid.uuid4()),
                            email=request.email,
                            username=request.username,
                            first_name=request.first_name,
                            last_name=request.last_name,
                            user_role=request.user_role,
                            password=hash_password(request.password))
        inserted_id = self.user_repository.insert(user)

        response = UserResponse(id=inserted_id,
                                email=user.email,
                                username=user.username,
                                first_name=user.first_name,
                                last_name=user.last_name,
                                user_role=user.user_role)
        return response

    def get_all_users(self) -> list[UserResponse]:
        users = self.user_repository.find({})

        resp_users = []
        for user in users:
            resp_users.append(UserResponse(id=user.id,
                                           email=user.email,
                                           username=user.username,
                                           first_name=user.first_name,
                                           last_name=user.last_name,
                                           user_role=user.user_role,
                                           image_url=self.__get_profile_image_path(user.id)))
        return resp_users

    def is_user_exists(self, username: str) -> bool:
        users = self.user_repository.find({'username': username})
        return len(users) > 0

    @staticmethod
    def __get_profile_image_path(user_id: str) -> str:
        image_service = ImageService()
        return image_service.get_image_path(user_id)


