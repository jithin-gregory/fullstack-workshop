from fastapi import Depends, FastAPI
from fastapi.security import HTTPBearer

from routers.user import router as user_router

app = FastAPI(
    title="Fullstack Workshop Demo App",
    description="This API documentation serves as the reference guide for the Demo app developed during the Full Stack Workshop.",
)

app.include_router(user_router, prefix="/api/user", tags=["User"])


@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
