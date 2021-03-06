import sys
from rq.job import Job
import rq.exceptions

sys.path.append('..')
from worker import conn
from models import Status


async def check_status(build_id: str) -> Status:

    try:
        job = Job.fetch(build_id, connection=conn)
        status = job.get_status()
        return Status(build_id=build_id, build_status=status)

    except rq.exceptions.NoSuchJobError:
        return Status(build_id=build_id, build_status="NotFound/Deleted")
