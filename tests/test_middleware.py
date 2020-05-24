
api_version = 'v1'

def test_middleware_route_request(TestApp, mock_env_api_key, headers):

    body = {"build_id": "12"}

    response = TestApp.get(f"/{api_version}/status", params=body, headers=headers)

    assert response.status_code not in (403, 400)


def test_middleware_not_authorize_request(TestApp, mock_env_api_key):

    body = {"build_id": "12"}
    headers = {'X-API-KEY': "123674"}

    response = TestApp.get(f"/{api_version}/status", params=body, headers=headers)

    assert response.status_code == 403

def test_middleware_invalid_request(TestApp, mock_env_api_key):
    
    body = {"build_id": "12"}
    response = TestApp.get(f"/{api_version}/status", params=body)

    assert response.status_code == 400