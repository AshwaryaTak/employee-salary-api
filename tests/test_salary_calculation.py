from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_salary_india():

    response = client.post(
        "/employees",
        json={
            "full_name": "Raj",
            "job_title": "Engineer",
            "country": "India",
            "salary": 100000
        }
    )

    emp_id = response.json()["id"]
    response = client.get(f"/employees/{emp_id}/salary")

    data = response.json()

    assert data["tds"] == 10000
    assert data["net_salary"] == 90000