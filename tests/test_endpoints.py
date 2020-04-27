import json

def test_health(TestApp):

    response = TestApp.get("/v1/health")
    assert response.status_code == 200
    assert response.text == ""
    

def test_check_status(TestApp):

    body = {"build_id": "12"}

    response = TestApp.get("/v1/status", params=body)
    assert response.status_code == 200
    assert response.json() == {"build_id": "12", "build_status": "NotFound/Deleted"}
