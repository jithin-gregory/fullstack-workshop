from fastapi import APIRouter, UploadFile, File

from models.response import APIResponse
from services.image_service import ImageService
from services.user_service import *
from utils import create_response

router = APIRouter()


@router.get("/")
async def get_all_users(user_service: UserService = Depends(UserService)) -> APIResponse[list[UserResponse]]:
    users = user_service.get_all_users()

    return create_response(
        APIResponse[list[UserResponse]](
            data=users,
            message="Successfully retrieved user details.",
            status_code=200))


@router.post("/",
             response_model=APIResponse[UserResponse],
             status_code=201,
             description="User created successfully.")
async def create_user(request: CreateUserRequest, user_service: UserService = Depends(UserService)):
    response_data = user_service.create_user(request)
    return create_response(APIResponse(data=response_data, message="User created successfully.", status_code=201))


@router.post("/{user_id}/upload-image")
async def upload_user_image(user_id: str, image: UploadFile = File(description="Upload an profile image"), image_service: ImageService = Depends(ImageService)):
    if image.content_type not in ("image/jpeg", "image/png"):
        return create_response(APIResponse(data=None, message="Unsupported media type. Only JPEG and PNG images allowed.", status_code=415))
    try:
        image_service.upload_image(image, user_id)
    except Exception:
        return create_response(APIResponse(data=None, message="Failed to upload profile image.", status_code=500))

    return create_response(APIResponse(data=None, message="Profile image uploaded successfully.", status_code=201))

