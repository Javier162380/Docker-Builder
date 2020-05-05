import json

api_version = 'v1'


def test_health(TestApp):

    response = TestApp.get(f"/{api_version}/health")
    assert response.status_code == 200
    assert response.text == '"Up and running!"'


def test_check_status(TestApp):

    body = {"build_id": "12"}

    response = TestApp.get(f"/{api_version}/status", params=body)
    assert response.status_code == 200
    assert response.json() == {"build_id": "12", "build_status": "NotFound/Deleted"}


def test_invalid_model_check_status(TestApp):

    response = TestApp.get(f"/{api_version}/status")
    assert response.status_code == 422


def test_build(TestApp):
    body = {"dockerfile": "Dockerfile", "image_name": "test", "tags": ["prod", "latest"]}

    response = TestApp.post(f"/{api_version}/build", json=body)

    assert response.status_code == 201


def test_invalid_model_build(TestApp):

    response = TestApp.post(f"/{api_version}/build")
    assert response.status_code == 422

def test_execution(TestApp):
    body = {"build_id": "12"}

    response = TestApp.get(f"/{api_version}/execution", params=body)

    assert response.status_code == 200

def test_execution_invalid_model(TestApp):

    response = TestApp.get(f"/{api_version}/execution")

    assert response.status_code == 422

