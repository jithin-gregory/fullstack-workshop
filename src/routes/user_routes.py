from fastapi import APIRouter

from models.response import APIResponse, UserResponse
from services.user_service import UserService
from services.user_service import *
from config import MONGO_CONFIG

router = APIRouter()


@router.get("/")
async def get_users(user_service: UserService = Depends(UserService)) -> APIResponse[list[UserResponse]]:
    users = await user_service.get_all_users()

    return APIResponse[list[UserResponse]](data=users, message="Successfully retrieved user details.", status_code=200)


@router.post("/", response_model=APIResponse[str])
async def create_user(request: CreateUserRequest, user_service: UserService = Depends(UserService)):
    id = user_service.create_user(request)

    return APIResponse(data=id, message="User created successfully.", status_code=201)