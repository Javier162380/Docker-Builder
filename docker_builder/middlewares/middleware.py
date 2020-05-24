import sys
from fastapi import HTTPException
import os

from fastapi import Security
from fastapi.security.api_key import APIKeyHeader
from fastapi import Header
from starlette.status import HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST

api_key_header = APIKeyHeader(name='X-API-Key', auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header),):

    api_key = os.environ["API_KEY"]
    if api_key_header == api_key:
        return api_key_header
    
    if not api_key_header:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Invalid Request")

    raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid Credentials")
