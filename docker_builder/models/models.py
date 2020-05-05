from typing import List, Dict

from pydantic import BaseModel


class Build(BaseModel):
    dockerfile: str
    image_name: str
    tags: List[str] = ["latest"]
    image_registry: str = None
    args: Dict = None
    github_repository: str = None


class Status(BaseModel):
    build_id: str
    build_status: str

class Execution(BaseModel):
    build_id: str
    build_execution: List

class BuildResponse(BaseModel):
    build_id: str
