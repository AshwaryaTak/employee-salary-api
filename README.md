# Employee Salary API (TDD)

This project implements an Employee Management API with salary calculations and salary metrics using **FastAPI**, **SQLite**, and **SQLAlchemy**, following **Test-Driven Development (TDD)** principles.

---

## Features

### 1. Employee CRUD API

* Create Employee
* Get Employee
* Update Employee
* Delete Employee

Each employee has:

* Full Name
* Job Title
* Country
* Salary

All data is stored in a **SQLite database**.

---

### 2. Salary Calculation

Endpoint:

GET /employees/{id}/salary

Rules:

| Country         | TDS Deduction |
| --------------- | ------------- |
| India           | 10%           |
| United States   | 12%           |
| Other Countries | 0%            |

Example Response:

```
{
  "gross_salary": 100000,
  "tds": 10000,
  "net_salary": 90000
}
```

---

### 3. Salary Metrics

#### Salary by Country

Endpoint:

GET /metrics/salary/country/{country}

Returns:

* Minimum Salary
* Maximum Salary
* Average Salary

Example:

```
{
  "min_salary": 100000,
  "max_salary": 200000,
  "avg_salary": 150000
}
```

---

#### Salary by Job Title

Endpoint:

GET /metrics/salary/job/{job_title}

Returns:

```
{
  "avg_salary": 120000
}
```

---

## Project Structure

```
employee-salary-api
│
├── app
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   │
│   ├── routers
│   │   └── employee.py
│   │
│   └── services
│       └── salary_service.py
│
├── tests
│   ├── test_employee_crud.py
│   ├── test_salary_calculation.py
│   └── test_salary_metrics.py
│
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```
git clone <repository_url>
cd employee-salary-api
```

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## Run Application

```
uvicorn app.main:app --reload
```

API will start at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## Run Tests

```
pytest
```

---

## Development Approach

This project follows **Test-Driven Development (TDD)**:

1. Write failing test
2. Implement minimal code
3. Refactor

Git commit history reflects the **Red → Green → Refactor cycle**.

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pytest
* Pydantic
