from fastapi import FastAPI, staticfiles

from config import static_folder_root
from models.response import APIResponse
from routes import user_router

app = FastAPI()


@app.get("/")
def index() -> APIResponse[bool]:
    return APIResponse[bool](message="Your app is working", data=True, status_code=200)


app.mount("/static", staticfiles.StaticFiles(directory=static_folder_root))

app.include_router(user_router, prefix="/api/v1/user")
