import sys
import time
from rq import Queue

sys.path.append('..')
from settings import Q, BUILD_TIMEOUT, FAILED_JOB_TIMEOUT, SUCCESSFUL_JOB_TIMEOUT
from worker import conn
from models import Build


def sleep():
    return time.sleep(10)


async def build_docker(build: Build):
    result = Q.enqueue(
        sleep, 10, job_timeout=BUILD_TIEMOUT, failure_ttl=FAILED_JOB_TIEMOUT,
        result_ttl=SUCCESSFUL_JOB_TIMEOUT)
    return result
