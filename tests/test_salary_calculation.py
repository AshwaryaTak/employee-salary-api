from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_salary_india():

    response = client.get("/employees/1/salary")

    data = response.json()

    assert data["tds"] == 10000
    assert data["net_salary"] == 90000