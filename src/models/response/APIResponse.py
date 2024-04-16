from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")  # Generic type for data


class APIResponse(BaseModel, Generic[T]):
    """
    Pydantic-based class for representing responses from a FastAPI API server.

    Attributes:
        message (str): A human-readable message describing the response.
        data (T): The actual data returned by the API endpoint.
        status_code (int, optional): The HTTP status code of the response.
    """

    message: str
    data: T
    status_code: int = 200
