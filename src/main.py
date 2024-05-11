from fastapi import Depends, FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware

from middlewares.jwt_middleware import JWTMiddleware

from routers.auth import router as auth_router
from routers.user import router as user_router

app = FastAPI(
    title="Fullstack Workshop Demo App",
    description="This API documentation serves as the reference guide for the Demo app developed during the Full Stack Workshop.",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
app.add_middleware(
    JWTMiddleware,
    exempt_routes=[
        "/api/auth/token",
        "/docs",  # Swagger UI
        "/redoc",  # Redoc documentation
        "/openapi.json",  # OpenAPI schema
    ],
)

security = HTTPBearer(
    description="Enter the Bearer Authorization string without <code>Bearer</code>"
)

app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])

app.include_router(
    user_router, prefix="/api/user", tags=["User"], dependencies=[Depends(security)]
)


@app.get("/", dependencies=[Depends(security)])
async def root():
    return {"message": "Welcome to the User Management API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
