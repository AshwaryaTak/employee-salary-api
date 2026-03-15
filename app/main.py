from fastapi import FastAPI
from .database import Base, engine
from app.routers import employee, metrics

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(employee.router)
app.include_router(metrics.router)