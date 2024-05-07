from fastapi import APIRouter, Depends, File, UploadFile, status, HTTPException
from fastapi.responses import FileResponse
from service import UserService
from fastapi.security import OAuth2PasswordRequestForm
from model.user_dto import UserDTO
from model.user_request import UserRequest
from jwt_utils import create_access_token
import os

router = APIRouter()

user_service = UserService()


@router.post("/register", response_model=dict)
async def register_user(user: UserRequest):
    user_id = user_service.register_user(user)
    return {"user_id": user_id}


@router.get("/users", response_model=list[UserDTO])
async def get_all_users():
    users = user_service.get_all_users()
    return users

@router.get("/users/{user_id}", response_model=UserDTO)
async def get_user(user_id: str):
    return user_service.get_user(user_id)


@router.post("/users/{user_id}/upload_image", response_model=dict)
async def upload_user_image(user_id: str, file: UploadFile = File(...)):
    user_service.upload_user_image(user_id, file)
    return {"message": "Image uploaded successfully"}


@router.get("/users/{user_id}/image", response_model=dict)
async def get_user_image(user_id: str):
    file_path = user_service.get_user_image(user_id)
    return FileResponse(path=file_path)


@router.post("/token", status_code=status.HTTP_200_OK)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Authenticate the user with the provided credentials
    user = user_service.authenticate_user(
        form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.username})

    # Return the JWT token to the client
    return {"access_token": access_token, "token_type": "bearer"}
