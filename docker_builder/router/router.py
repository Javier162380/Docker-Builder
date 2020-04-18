import sys
from fastapi import APIRouter

sys.path.append('..')
from endpoints import build, health, status


router = APIRouter()

router.add_api_route('/build', endpoint=build.build_docker, methods=["POST"])
router.add_api_route('/health', endpoint=health.health)
router.add_api_route('/status', endpoint=status.check_status)