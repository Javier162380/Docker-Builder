import pytest
from fastapi.testclient import TestClient

from docker_builder.app import app


@pytest.fixture(scope='module')
def TestApp():
    return TestClient(app)