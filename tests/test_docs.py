from requests.auth import HTTPBasicAuth


def test_docs_endpoint(
        TestApp, mock_env_docs_username, mock_env_docs_password):

    response = TestApp.get("/docs", auth=HTTPBasicAuth('admin', 'admin'))

    assert response.status_code == 200


def test_openapi_endpoint(
        TestApp, mock_env_docs_username, mock_env_docs_password):

    response = TestApp.get("/openapi.json", auth=HTTPBasicAuth('admin', 'admin'))

    assert response.status_code == 200
