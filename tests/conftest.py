import pytest
from fastapi.testclient import TestClient

from docker_builder.app import app
from docker_builder.builder import Builder
from docker_builder.models import Build


@pytest.fixture(scope='module')
def TestApp():
    return TestClient(app)

@pytest.fixture
def mock_env_api_key(monkeypatch):
    monkeypatch.setenv('API_KEY', '1234')


@pytest.fixture
def TestBuilderNoRepository():

    return Builder(build_instance=Build(dockerfile='Dockerfile',
                                         image_name='test',
                                         tags=['prod', 'latest']),
                  job_id='asfsdfsf-sdfdsf')

@pytest.fixture
def TestBuilderRepository():

    return Builder(build_instance=Build(dockerfile='Dockerfile',
                                         image_name='test',
                                         tags=['prod', 'latest'],
                                         image_registry='javier162380'),
                   job_id='asfsdfsf-sdfdsf')
