from fastapi.testclient import TestClient
from apps.main import app

client = TestClient(app)

def test_create_employee():

    response = client.post(
        "/employees",
        json={
            "full_name": "John Doe",
            "job_title": "QA Engineer",
            "country": "India",
            "salary": 100000
        }
    )

    assert response.status_code == 200
    assert response.json()["full_name"] == "John Doe"