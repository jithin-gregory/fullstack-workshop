from fastapi import FastAPI
from routes import router as user_router
from jwt_middleware import JWTMiddleware

app = FastAPI(openapi_tags=[
    {
        "name": "Auth",
        "description": "Authentication and authorization endpoints",
    },
    {
        "name": "Registration",
        "description": "User registration endpoints",
    },
],
    # Define security schema to support Bearer tokens in Swagger UI
    openapi_schema={
        "openapi": "3.0.0",
        "info": {
            "title": "My FastAPI Application",
            "version": "1.0.0",
        },
        "paths": {},
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                },
            },
        },
        "security": [
            {"bearerAuth": []},
        ],
},)

app.include_router(user_router)
app.add_middleware(
    JWTMiddleware,
    exempt_routes=["/token", "/register",
                   "/docs",  # Swagger UI
                   "/redoc",  # Redoc documentation
                   "/openapi.json",  # OpenAPI schema
                   ],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
