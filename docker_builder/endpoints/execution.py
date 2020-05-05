import sys
from rq.job import Job
import rq.exceptions

sys.path.append('..')
from models import Execution
from worker import conn


async def check_execution(build_id: str) -> Execution:

    try:
        job = Job.fetch(build_id, connection=conn)
        status = job.meta
        return Execution(build_id=build_id, build_execution=job.meta)

    except rq.exceptions.NoSuchJobError:
        return Execution(build_id=build_id, build_execution=[{"stream": "Execution not started/deleted or job not found/deleted"}])
