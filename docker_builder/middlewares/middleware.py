import sys
import os
import secrets

from fastapi import Security, Depends
from fastapi.security.api_key import APIKeyHeader
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import HTTPException
from fastapi import Header
from starlette.status import HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

api_key_header = APIKeyHeader(name='X-API-Key', auto_error=False)
security = HTTPBasic()

async def get_api_key(api_key_header: str = Security(api_key_header),):

    api_key = os.environ["API_KEY"]
    if api_key_header == api_key:
        return api_key_header
    
    if not api_key_header:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Invalid Request")

    raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid Credentials")


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, os.environ['DOCS_USERNAME'])
    correct_password = secrets.compare_digest(credentials.password, os.environ['DOCS_PASSWORD'])
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
