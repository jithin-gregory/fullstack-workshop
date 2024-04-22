from fastapi.responses import JSONResponse

from models.response.APIResponse import APIResponse


def create_response(response: APIResponse):
    return JSONResponse(content=response.model_dump(), status_code=response.status_code, media_type='application/json')
