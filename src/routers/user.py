from fastapi import APIRouter, Depends, File, UploadFile, status, HTTPException
from fastapi.responses import FileResponse
from services.user import UserService
from fastapi.security import OAuth2PasswordRequestForm
from model.user_dto import UserDTO
from model.user_request import UserRequest
import os

router = APIRouter()

user_service = UserService()


@router.post("/", response_model=dict)
async def register_user(user: UserRequest):
    user_id = user_service.register_user(user)
    return {"user_id": user_id}


@router.get("/", response_model=list[UserDTO])
async def get_all_users():
    users = user_service.get_all_users()
    return users


@router.get("/{user_id}", response_model=UserDTO)
async def get_user(user_id: str):
    return user_service.get_user(user_id)


@router.post("/{user_id}/image", response_model=dict)
async def upload_user_image(user_id: str, file: UploadFile = File(...)):
    user_service.upload_user_image(user_id, file)
    return {"message": "Image uploaded successfully"}


@router.get("/{user_id}/image", response_model=dict)
async def get_user_image(user_id: str):
    file_path = user_service.get_user_image(user_id)
    return FileResponse(path=file_path)
