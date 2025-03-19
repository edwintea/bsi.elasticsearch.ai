# routers/vehicle_has_source_of_truths.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.vehicle_has_source_of_truths import VehicleHasSourceOfTruthsCreate,VehicleHasSourceOfTruths,VehicleHasSourceOfTruthsBase
from ..crud.vehicle_has_source_of_truths import get_vehicle_sources_of_truth,get_vehicle_source_of_truth

router = APIRouter()

@router.post("/", response_model=VehicleHasSourceOfTruths)
def create_vehicle_source_of_truth(source_of_truth: VehicleHasSourceOfTruthsCreate, db: Session = Depends(get_db)):
    return create_vehicle_source_of_truth(db=db, **source_of_truth.dict())

@router.get("/", response_model=list[VehicleHasSourceOfTruths])
def read_vehicle_sources_of_truth(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_vehicle_sources_of_truth(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=VehicleHasSourceOfTruths)
def read_vehicle_source_of_truth(id: int, db: Session = Depends(get_db)):
    return get_vehicle_source_of_truth(db=db, id=id)