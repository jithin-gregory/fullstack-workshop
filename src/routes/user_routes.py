from fastapi import APIRouter

from models.response import APIResponse, UserResponse
from services import user_service
from services.user_service import *

router = APIRouter()

@router.get("/")
async def get_users() -> APIResponse[list[UserResponse]]:
    users = await get_all_users()

    return APIResponse[list[UserResponse]](data=users, message="Successfully retrieved user details.", status_code=200)
