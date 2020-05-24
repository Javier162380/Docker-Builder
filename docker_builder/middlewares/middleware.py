import sys
from fastapi import HTTPException
from fastapi import Header
from starlette.status import HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST
sys.path.append('..')
from settings import API_KEY

async def get_api_key(api_key: str = Header(None)):

    if api_key == API_KEY:
        return api_key
    
    raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid Credentials")
