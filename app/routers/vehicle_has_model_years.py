# routers/vehicle_has_model_years.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.vehicle_has_model_years import VehicleHasModelYears,VehicleHasModelYearsBase,VehicleHasModelYearsCreate,VehicleHasModelYearsUpdate
from ..crud.vehicle_has_model_years import create_vehicle_model_year,get_vehicle_model_years,get_vehicle_model_year,update_vehicle_model_year,delete_vehicle_model_year

router = APIRouter()

@router.post("/", response_model=VehicleHasModelYears)
def create_vehicle_model_year(model_year: VehicleHasModelYearsCreate, db: Session = Depends(get_db)):
    return create_vehicle_model_year(db=db, **model_year.dict())

@router.get("/", response_model=list[VehicleHasModelYears])
def read_vehicle_model_years(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_vehicle_model_years(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=VehicleHasModelYears)
def read_vehicle_model_year(id: int, db: Session = Depends(get_db)):
    model_year = get_vehicle_model_year(db=db, id=id)
    if model_year is None:
        raise HTTPException(status_code=404, detail="Vehicle model year not found")
    return model_year

@router.put("/{id}", response_model=VehicleHasModelYears)
def update_vehicle_model_year(id: int, model_year: VehicleHasModelYearsUpdate, db: Session = Depends(get_db)):
    updated_model_year = update_vehicle_model_year(db=db, id=id, **model_year.dict())
    if updated_model_year is None:
        raise HTTPException(status_code=404, detail="Vehicle model year not found")
    return updated_model_year

@router.delete("/{id}", response_model=VehicleHasModelYears)
def delete_vehicle_model_year(id: int, db: Session = Depends(get_db)):
    deleted_model_year = delete_vehicle_model_year(db=db, id=id)
    if deleted_model_year is None:
        raise HTTPException(status_code=404, detail="Vehicle model year not found")
    return deleted_model_year