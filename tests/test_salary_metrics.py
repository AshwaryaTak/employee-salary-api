from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_country_metrics():

    client.post(
        "/employees/",
        json={
            "full_name": "Raj",
            "job_title": "Engineer",
            "country": "India",
            "salary": 100000
        }
    )

    client.post(
        "/employees/",
        json={
            "full_name": "Amit",
            "job_title": "Engineer",
            "country": "India",
            "salary": 200000
        }
    )

    response = client.get("/metrics/salary/country/India")

    assert response.status_code == 200

    data = response.json()

    assert "min_salary" in data
    assert "max_salary" in data
    assert "avg_salary" in data