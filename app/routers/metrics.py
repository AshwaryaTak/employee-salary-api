from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Employee

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)

@router.get("/salary/country/{country}")
def salary_by_country(country: str, db: Session = Depends(get_db)):

    employees = db.query(Employee).filter(Employee.country == country).all()

    salaries = [e.salary for e in employees]

    if not salaries:
        return {"message": "No employees found"}

    return {
        "min_salary": min(salaries),
        "max_salary": max(salaries),
        "avg_salary": sum(salaries) / len(salaries)
    }