from sqlalchemy.orm import Session
from . import models, schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employees(db: Session):
    return db.query(models.Employee).all()

def update_employee(db: Session, employee_id: int, data: schemas.EmployeeCreate):
    emp = get_employee(db, employee_id)
    if not emp:
        return None

    for key, value in data.dict().items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)
    return emp


def delete_employee(db: Session, employee_id: int):
    emp = get_employee(db, employee_id)
    if not emp:
        return None

    db.delete(emp)
    db.commit()
    return emp

