from fastapi import Depends

from database.repositories import UserRepository
from database.schemas import UserDocument
from models.request import CreateUserRequest
from models.response import UserResponse
from utils.password_helper import hash_password


class UserService:
    def __init__(self, user_repository: UserRepository = Depends(UserRepository)):
        self.user_repository = user_repository

    def create_user(self, request: CreateUserRequest):
        user = UserDocument(email=request.email,
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
                                           user_role=user.user_role))
        return resp_users

    async def get_user_by_email(self, email):
        user = {
            'email': email,
            'username': email.split('@')[0],
            'first_name': 'John',
            'last_name': 'Doe',
            'user_role': 1
        }

        return user
