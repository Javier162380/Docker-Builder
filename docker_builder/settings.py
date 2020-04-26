import os
from rq import Queue

Q = Queue(connection=os.getenv('REDIS_URL'))
BUILD_TIMEOUT = 600
SUCCESSFUL_JOB_TIMEOUT = 36000
FAILED_JOB_TIMEOUT = 1314000
