from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}
    
    

def test_get_estimated_cvr_by_ads():
    mock_request_data = {
        "adIdList": [1, 2]
    }
    response = client.post("/api/v1/predict", json=mock_request_data)
    assert response.status_code == 200
    expected_response = [{"adId": 1, "estimatedCVR": 0.841029708}, {"adId": 2, "estimatedCVR": 0.6407288316}]
    assert response.json() == expected_response

