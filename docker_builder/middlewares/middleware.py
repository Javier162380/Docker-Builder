import sys
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
sys.path.append('..')
from settings import API_KEY


async def get_api_key(api_key_header):
    api_key_header: str = Security(api_key_header),

    if api_key_header == API_KEY:
        return api_key_header
    
    return HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid Credentials")
