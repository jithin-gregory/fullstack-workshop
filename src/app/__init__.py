from fastapi import FastAPI

from models.response import APIResponse
from routes import user_router

app = FastAPI()


@app.get("/")
def index() -> APIResponse[bool]:
    return APIResponse[bool](message="Your app is working", data=True, status_code=200)


app.include_router(user_router, prefix="/api/v1/user")
