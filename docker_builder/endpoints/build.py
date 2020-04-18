import sys

sys.path.append('..')
from models import Build


async def build_docker(build: Build):

    return build