import sys
from fastapi import APIRouter, Depends

sys.path.append('..')
from endpoints import build, health, status, execution
from models import Status, BuildResponse, Execution
from middlewares import get_api_key


router = APIRouter()

router.add_api_route('/v1/build', endpoint=build.build_docker, methods=["POST"],
                     response_model=BuildResponse, dependencies=[Depends(get_api_key)], 
                     status_code=201)
router.add_api_route('/v1/health', endpoint=health.health, methods=["GET"])
router.add_api_route('/v1/status', endpoint=status.check_status, methods=["GET"],
                     response_model=Status, dependencies=[Depends(get_api_key)])
router.add_api_route('/v1/execution', endpoint=execution.check_execution,
                     methods=["GET"], response_model=Execution,
                     dependencies=[Depends(get_api_key)])
