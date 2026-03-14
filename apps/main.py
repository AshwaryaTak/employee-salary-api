from fastapi import FastAPI

app = FastAPI()

employees = []

@app.post("/employees")
def create_employee(employee: dict):
    employees.append(employee)
    return employee