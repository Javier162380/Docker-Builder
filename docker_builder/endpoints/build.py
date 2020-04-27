import sys
import time
from rq import Queue

sys.path.append('..')
from builder import Builder
from models import Build, BuildResponse
from worker import conn
from settings import Q, BUILD_TIMEOUT, FAILED_JOB_TIMEOUT, SUCCESSFUL_JOB_TIMEOUT


def build_submit(build: Build):

    build_instance = Build(build_instance=build)
    build_instance.execute()

async def build_docker(build: Build):

    builder = Builder(build_instance=build)
    
    result = Q.enqueue(
        build_submit,
        build,
        job_timeout=BUILD_TIMEOUT,
        result_ttl=SUCCESSFUL_JOB_TIMEOUT,
        failure_ttl=FAILED_JOB_TIMEOUT
    )

    return BuildResponse(build_id=result.id)
