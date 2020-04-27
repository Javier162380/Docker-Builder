import sys
from fastapi import APIRouter

sys.path.append('..')
from endpoints import build, health, status
from models import Status, BuildResponse


router = APIRouter()

router.add_api_route('/v1/build', endpoint=build.build_docker, methods=["POST"], response_model=BuildResponse)
router.add_api_route('/v1/health', endpoint=health.health, methods=["GET"])
router.add_api_route('/v1/status', endpoint=status.check_status, methods=["GET"], response_model=Status)