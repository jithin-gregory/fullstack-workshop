from fastapi import APIRouter, HTTPException, status

from model.login_request import LoginRequest
from utils.jwt_utils import create_access_token
from services.user import UserService

router = APIRouter()
user_service = UserService()


@router.post("/token", status_code=status.HTTP_200_OK)
async def login(request: LoginRequest):
    # Authenticate the user with the provided credentials
    user = user_service.authenticate_user(request.username, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.username})

    # Return the JWT token to the client
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "is_admin": user.is_admin,
    }
