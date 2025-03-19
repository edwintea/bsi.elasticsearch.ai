# routers/part_number_cars.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.part_number_cars import PartNumberCars,PartNumberCarsBase,PartNumberCarsCreate,PartNumberCarsUpdate
from ..crud.part_number_cars import create_part_number_car,get_part_number_car,get_part_number_cars,update_part_number_car

router = APIRouter()

@router.post("/", response_model=PartNumberCars)
def create_part_number_car(part_number_car: PartNumberCarsCreate, db: Session = Depends(get_db)):
    """Create a new part number car."""
    return create_part_number_car(db=db, **part_number_car.dict())

@router.get("/", response_model=list[PartNumberCars])
def read_part_number_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of part number cars."""
    return get_part_number_cars(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=PartNumberCars)
def read_part_number_car(id: int, db: Session = Depends(get_db)):
    """Retrieve a part number car by ID."""
    part_number_car = get_part_number_car(db=db, id=id)
    if part_number_car is None:
        raise HTTPException(status_code=404, detail="Part number car not found")
    return part_number_car

@router.put("/{id}", response_model=PartNumberCars)
def update_part_number_car(id: int, part_number_car: PartNumberCarsUpdate, db: Session = Depends(get_db)):
    """Update an existing part number car."""
    updated_part_number_car = update_part_number_car(db=db, id=id, **part_number_car.dict())
    if updated_part_number_car is None:
        raise HTTPException(status_code=404, detail="Part number car not found")
    return updated_part_number_car

@router.delete("/{id}", response_model=PartNumberCars)
def delete_part_number_car(id: int, db: Session = Depends(get_db)):
    """Delete a part number car by ID."""
    deleted_part_number_car = delete_part_number_car(db=db, id=id)
    if deleted_part_number_car is None:
        raise HTTPException(status_code=404, detail="Part number car not found")
    return deleted_part_number_car