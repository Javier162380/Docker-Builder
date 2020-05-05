import os
import multiprocessing

from rq import Queue
from rq.job import Job
from worker import conn

Q = Queue(connection=conn)
BUILD_TIMEOUT = 1200
SUCCESSFUL_JOB_TIMEOUT = 36000
FAILED_JOB_TIMEOUT = 1314000
