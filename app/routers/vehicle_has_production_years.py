# routers/vehicle_has_production_years.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.vehicle_has_production_years import VehicleHasProductionYears,VehicleHasProductionYearsCreate,VehicleHasProductionYearsBase
from ..crud.vehicle_has_production_years import create_vehicle_production_year,get_vehicle_production_years,get_vehicle_production_year

router = APIRouter()

@router.post("/", response_model=VehicleHasProductionYears)
def create_vehicle_production_year(production_year: VehicleHasProductionYearsCreate, db: Session = Depends(get_db)):
    return create_vehicle_production_year(db=db, **production_year.dict())

@router.get("/", response_model=list[VehicleHasProductionYears])
def read_vehicle_production_years(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_vehicle_production_years(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=VehicleHasProductionYears)
def read_vehicle_production_year(id: int, db: Session = Depends(get_db)):
    return get_vehicle_production_year(db=db, id=id)