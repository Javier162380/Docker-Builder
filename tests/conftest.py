import pytest
from fastapi.testclient import TestClient

from docker_builder.app import app
from docker_builder.builder import Builder
from docker_builder.models import Build


@pytest.fixture(scope='module')
def TestApp():
    return TestClient(app)


@pytest.fixture
def TestBuilder():

    return Builder(build_instance=(Build(dockerfile='Dockerfile',
                                         image_name='test',
                                         tags=['prod', 'latest'])))
