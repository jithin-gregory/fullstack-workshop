from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

# Constants for JWT configuration
SECRET_KEY = "my_super_secret_key"
ALGORITHM = "HS256"

# Middleware class to verify JWT tokens
class JWTMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, exempt_routes=None):
        # Initialize middleware with FastAPI application and optional exempt routes
        super().__init__(app)
        self.exempt_routes = exempt_routes or []

    async def dispatch(self, request: Request, call_next):
        # Check if the request path is in the exempt routes
        if any(request.url.path.startswith(route) for route in self.exempt_routes):
            return await call_next(request)

        # Get the authorization header
        auth_header = request.headers.get("authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(
                status_code=401,
                detail="Unauthorized: Bearer token missing or incorrect",
            )

        # Extract the JWT token from the header
        token = auth_header.split(" ")[1]

        # Verify the JWT token
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Unauthorized: Token expired")
        except InvalidTokenError:
            raise HTTPException(
                status_code=401, detail="Unauthorized: Invalid token"
            )

        # If the token is valid, continue to the next middleware/endpoint
        return await call_next(request)
