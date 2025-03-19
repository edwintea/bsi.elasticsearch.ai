# routers/vehicle_has_variants.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.vehicle_has_variants import VehicleHasVariants,VehicleHasVariantsCreate,VehicleHasVariantsBase
from ..crud.vehicle_has_variants import create_vehicle_variant,get_vehicle_variants

router = APIRouter()

@router.post("/", response_model=VehicleHasVariants)
def create_vehicle_variant(variant: VehicleHasVariantsCreate, db: Session = Depends(get_db)):
    return create_vehicle_variant(db=db, **variant.dict())

@router.get("/", response_model=list[VehicleHasVariants])
def read_vehicle_variants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_vehicle_variants(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=VehicleHasVariants)
def read_vehicle_variant(id: int, db: Session = Depends(get_db)):
    return get_vehicle_variant(db=db, id=id)