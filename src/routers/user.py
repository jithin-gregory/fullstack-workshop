from fastapi import APIRouter
from services.user import UserService
from model.user_request import UserRequest

router = APIRouter()

user_service = UserService()


@router.post("/", response_model=dict)
async def register_user(user: UserRequest):
    user_id = user_service.register_user(user)
    return {"user_id": user_id}
