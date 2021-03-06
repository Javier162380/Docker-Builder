

api_version = 'v1'


def test_health(TestApp):

    response = TestApp.get(f"/{api_version}/health")
    assert response.status_code == 200
    assert response.text == '"Up and running!"'


def test_check_status(TestApp, mock_env_api_key, headers):


    body = {"build_id": "12"}

    response = TestApp.get(f"/{api_version}/status", params=body, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"build_id": "12", "build_status": "NotFound/Deleted"}


def test_invalid_model_check_status(TestApp, mock_env_api_key, headers):

    response = TestApp.get(f"/{api_version}/status", headers=headers)
    assert response.status_code == 422


def test_build(TestApp, headers, mock_env_api_key):
    body = {"dockerfile": "Dockerfile", "image_name": "test", "tags": ["prod", "latest"]}

    response = TestApp.post(f"/{api_version}/build", json=body, headers=headers)

    assert response.status_code == 201


def test_invalid_model_build(TestApp, headers, mock_env_api_key):

    response = TestApp.post(f"/{api_version}/build", headers=headers)

    assert response.status_code == 422


def test_execution(TestApp, headers, mock_env_api_key):
    body = {"build_id": "12"}

    response = TestApp.get(f"/{api_version}/execution", params=body, headers=headers)
    assert response.status_code == 200


def test_execution_invalid_model(TestApp, headers, mock_env_api_key):

    response = TestApp.get(f"/{api_version}/execution", headers=headers)

    assert response.status_code == 422

