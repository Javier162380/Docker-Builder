import sys
from fastapi import APIRouter, Depends

sys.path.append('..')
from middlewares import get_api_key
from models import Status, BuildResponse, Execution
from endpoints import build, health, status, execution


router = APIRouter()

router.add_api_route('/v1/build', endpoint=build.build_docker, methods=["POST"],
                     response_model=BuildResponse, dependencies=[Depends(get_api_key)],
                     status_code=201)
router.add_api_route('/v1/health', endpoint=health.health, methods=["GET"],
                     include_in_schema=False)
router.add_api_route('/v1/status', endpoint=status.check_status, methods=["GET"],
                     response_model=Status, dependencies=[Depends(get_api_key)],)
router.add_api_route('/v1/execution', endpoint=execution.check_execution,
                     methods=["GET"], response_model=Execution,
                     dependencies=[Depends(get_api_key)])
