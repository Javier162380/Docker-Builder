import sys

sys.path.append('..')
from models import Status


async def check_status(build_id: int):
    return Status(build_id=build_id, build_status='in_progress')