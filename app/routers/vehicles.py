# routers/vehicles.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.vehicles import Vehicles, VehiclesCreate, VehiclesUpdate
from ..crud.vehicles import get_vehicles, get_vehicle, create_vehicle, update_vehicle, delete_vehicle

router = APIRouter()


@router.post("/", response_model=Vehicles)
def create_vehicle(vehicle: VehiclesCreate, db: Session = Depends(get_db)):
    """Create a new vehicle record."""
    return create_vehicle(db=db, **vehicle.dict())


@router.get("/", response_model=list[Vehicles])
def read_vehicles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of vehicle records."""
    return get_vehicles(db=db, skip=skip, limit=limit)


@router.get("/{id}", response_model=Vehicles)
def read_vehicle(id: int, db: Session = Depends(get_db)):
    """Retrieve a vehicle record by ID."""
    vehicle = get_vehicle(db=db, id=id)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle


@router.put("/{id}", response_model=Vehicles)
def update_vehicle(id: int, vehicle: VehiclesUpdate, db: Session = Depends(get_db)):
    """Update a vehicle record."""
    updated_vehicle = update_vehicle(db=db, id=id, **vehicle.dict())
    if updated_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return updated_vehicle


@router.delete("/{id}", response_model=Vehicles)
def delete_vehicle(id: int, db: Session = Depends(get_db)):
    """Delete a vehicle record."""
    deleted_vehicle = delete_vehicle(db=db, id=id)
    if deleted_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return deleted_vehicle
