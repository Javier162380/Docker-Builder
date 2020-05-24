import sys
import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html
from docker_builder.middlewares import get_current_username


sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from router import router


app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.router)

@app.get("/docs",
         dependencies=[Depends(get_current_username)])
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Docker Builder")

@app.get("/openapi.json",
          dependencies=[Depends(get_current_username)],
          include_in_schema=False)
async def get_open_api_endpoint():
    return JSONResponse(get_openapi(title="Docker Builder",
                                    description="Efficient Web Service to build Docker Images",
                                    version="0.1.0",
                                    routes=app.routes))
