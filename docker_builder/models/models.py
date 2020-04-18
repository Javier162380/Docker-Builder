from typing import List

from pydantic import BaseModel


class Build(BaseModel):
    dockerfile: str
    tags: List[str]
    image_name: str
    image_registry: str
    github_repository: str = None

class Status(BaseModel):
    build_id: str
    build_status: str
