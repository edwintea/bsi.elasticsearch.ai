# routers/part_has_vehicles.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.part_has_vehicles import PartHasVehicles,PartHasVehiclesBase,PartHasVehiclesCreate,PartHasVehiclesUpdate
from ..crud.part_has_vehicles import get_part_has_vehicle,get_part_has_vehicles,create_part_has_vehicle,update_part_has_vehicle,delete_part_has_vehicle
router = APIRouter()

@router.post("/", response_model=PartHasVehicles)
def create_part_has_vehicle(part_has_vehicle: PartHasVehiclesCreate, db: Session = Depends(get_db)):
    """Create a new part has vehicle."""
    return create_part_has_vehicle(db=db, **part_has_vehicle.dict())

@router.get("/", response_model=list[PartHasVehicles])
def read_part_has_vehicles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of part has vehicles."""
    return get_part_has_vehicles(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=PartHasVehicles)
def read_part_has_vehicle(id: int, db: Session = Depends(get_db)):
    """Retrieve a part has vehicle by ID."""
    part_has_vehicle = get_part_has_vehicle(db=db, id=id)
    if part_has_vehicle is None:
        raise HTTPException(status_code=404, detail="Part has vehicle not found")
    return part_has_vehicle

@router.put("/{id}", response_model=PartHasVehicles)
def update_part_has_vehicle(id: int, part_has_vehicle: PartHasVehiclesUpdate, db: Session = Depends(get_db)):
    """Update an existing part has vehicle."""
    updated_part_has_vehicle = update_part_has_vehicle(db=db, id=id, **part_has_vehicle.dict())
    if updated_part_has_vehicle is None:
        raise HTTPException(status_code=404, detail="Part has vehicle not found")
    return updated_part_has_vehicle

@router.delete("/{id}", response_model=PartHasVehicles)
def delete_part_has_vehicle(id: int, db: Session = Depends(get_db)):
    """Delete a part has vehicle by ID."""
    deleted_part_has_vehicle = delete_part_has_vehicle(db=db, id=id)
    if deleted_part_has_vehicle is None:
        raise HTTPException(status_code=404, detail="Part has vehicle not found")
    return deleted_part_has_vehicle