from fastapi.testclient import TestClient
from app.main import app

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

def test_get_employee():

    # First create an employee
    response = client.post(
        "/employees",
        json={
            "full_name": "John Doe",
            "job_title": "QA Engineer",
            "country": "India",
            "salary": 100000
        }
    )

    emp_id = response.json()["id"]

    # Now fetch employee
    response = client.get(f"/employees/{emp_id}")

    assert response.status_code == 200
    data = response.json()

    assert data["full_name"] == "John Doe"
    assert data["job_title"] == "QA Engineer"

def test_update_employee():

    # Create employee
    response = client.post(
        "/employees",
        json={
            "full_name": "Alice",
            "job_title": "Developer",
            "country": "India",
            "salary": 80000
        }
    )

    emp_id = response.json()["id"]

    # Update employee
    response = client.put(
        f"/employees/{emp_id}",
        json={
            "full_name": "Alice Smith",
            "job_title": "Senior Developer",
            "country": "India",
            "salary": 120000
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["full_name"] == "Alice Smith"
    assert data["job_title"] == "Senior Developer"
    assert data["salary"] == 120000

def test_delete_employee():

    # Create employee
    response = client.post(
        "/employees",
        json={
            "full_name": "Bob",
            "job_title": "Manager",
            "country": "United States",
            "salary": 150000
        }
    )

    emp_id = response.json()["id"]

    # Delete employee
    response = client.delete(f"/employees/{emp_id}")

    assert response.status_code == 200

    # Ensure employee is deleted
    response = client.get(f"/employees/{emp_id}")

    assert response.status_code == 404

def test_get_employee_not_found():

    response = client.get("/employees/999")

    assert response.status_code == 404

def test_delete_employee_not_found():

    response = client.delete("/employees/999")

    assert response.status_code == 404