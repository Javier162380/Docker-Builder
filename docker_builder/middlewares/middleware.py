import sys
from fastapi import HTTPException
from fastapi import Header
from starlette.status import HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST
sys.path.append('..')
from settings import API_KEY

async def get_api_key(X_API_Key: str = Header(None)):

    if X_API_Key == API_KEY:
        return X_API_Key
    
    raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid Credentials")
