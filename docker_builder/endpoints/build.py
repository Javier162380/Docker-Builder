import sys
import time
import uuid
from rq import Queue
sys.path.append('..')
from builder import Builder
from models import Build, BuildResponse
from worker import conn
from settings import Q, BUILD_TIMEOUT, FAILED_JOB_TIMEOUT, SUCCESSFUL_JOB_TIMEOUT


def build_submit(build: Build, job_id: str):

    build_instance = Builder(build_instance=build, job_id=job_id)
    build_instance.execute()

async def build_docker(build: Build):
    
    job_id = str(uuid.uuid4())
    
    result = Q.enqueue(
        build_submit,
        kwargs={'build':build, 'job_id': job_id},
        job_timeout=BUILD_TIMEOUT,
        result_ttl=SUCCESSFUL_JOB_TIMEOUT,
        failure_ttl=FAILED_JOB_TIMEOUT,
        job_id=job_id
    )

    return BuildResponse(build_id=result.id)
