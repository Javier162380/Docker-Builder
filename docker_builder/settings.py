import os
from rq import Queue


from cli import cli

params = cli()


Q = Queue(connection=params['REDIS_URL'])
BUILD_TIMEOUT = params['build_timeout']
SUCCESSFUL_JOB_TIMEOUT = params['successful_job_timeout']
FAILED_JOB_TIMEOUT = params['failed_job_timeout']
