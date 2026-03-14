from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/employees", response_model=schemas.EmployeeResponse)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):

    return crud.create_employee(db, employee)

@app.get("/employees")
def list_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee =  crud.get_employee(db, emp_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.update_employee(db, emp_id, emp)


@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted successfully"}