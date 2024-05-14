from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import jwt
from utils.jwt_utils import validate_access_token
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError


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
            return JSONResponse(
                status_code=401,
                content="Unauthorized: Bearer token missing or incorrect",
            )

        # Extract the JWT token from the header
        token = auth_header.split(" ")[1]

        # Verify the JWT token
        try:
            validate_access_token(token)
        except ExpiredSignatureError:
            return JSONResponse(
                status_code=401,
                content="Unauthorized: Token expired",
            )
        except InvalidTokenError:
            return JSONResponse(
                status_code=401,
                content="Unauthorized: Invalid token",
            )

        # If the token is valid, continue to the next middleware/endpoint
        return await call_next(request)
