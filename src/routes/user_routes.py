from fastapi import APIRouter

from models.response import APIResponse
from services.user_service import *
from utils import create_response

router = APIRouter()


@router.get("/")
async def get_users(user_service: UserService = Depends(UserService)) -> APIResponse[list[UserResponse]]:
    users = await user_service.get_all_users()

    return APIResponse[list[UserResponse]](data=users, message="Successfully retrieved user details.", status_code=200)


@router.post("/",
             response_model=APIResponse[UserResponse],
             status_code=201,
             description="User created successfully.")
async def create_user(request: CreateUserRequest, user_service: UserService = Depends(UserService)):
    response_data = user_service.create_user(request)
    return create_response(APIResponse(data=response_data, message="User created successfully.", status_code=201))
