

def test_middleware_route_request(TestApp, mock_env_api_key, headers):

    body = {"build_id": "12"}

    response = TestApp.get(f"/v1/status", params=body, headers=headers)

    assert response.status_code not in (403, 400)


def test_middleware_invalid_request(TestApp, mock_env_api_key):

    body = {"build_id": "12"}
    headers = {'X-API-KEY': "1234"}

    response = TestApp.get(f"/v1/status", params=body, headers=headers)

    assert response.status_code == 403



