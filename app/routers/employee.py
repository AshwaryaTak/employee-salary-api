from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("/")
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):

    return crud.create_employee(db, employee)


@router.get("/{employee_id}")
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = crud.get_employee(db, employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@router.get("/")
def get_employees(db: Session = Depends(get_db)):

    return crud.get_employees(db)


@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):

    updated = crud.update_employee(db, employee_id, employee)

    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")

    return updated


@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_employee(db, employee_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted"}