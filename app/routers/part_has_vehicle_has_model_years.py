# routers/part_has_vehicle_has_model_years.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.part_has_vehicle_has_model_years import PartHasVehicleHasModelYears,PartHasVehicleHasModelYearsBase,PartHasVehicleHasModelYearsCreate,PartHasVehicleHasModelYearsUpdate
from ..crud.part_has_vehicle_has_model_years import get_part_has_vehicle_model_year,get_part_has_vehicle_model_years,update_part_has_vehicle_model_year,delete_part_has_vehicle_model_year,create_part_has_vehicle_model_year
router = APIRouter()

@router.post("/", response_model=PartHasVehicleHasModelYears)
def create_part_has_vehicle_model_year(part_has_vehicle_model_year: PartHasVehicleHasModelYearsCreate, db: Session = Depends(get_db)):
    """Create a new part has vehicle model year."""
    return create_part_has_vehicle_model_year(db=db, **part_has_vehicle_model_year.dict())

@router.get("/", response_model=list[PartHasVehicleHasModelYears])
def read_part_has_vehicle_model_years(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of part has vehicle model years."""
    return get_part_has_vehicle_model_years(db=db, skip=skip, limit=limit)

@router.get("/{my_row_id}", response_model=PartHasVehicleHasModelYears)
def read_part_has_vehicle_model_year(my_row_id: int, db: Session = Depends(get_db)):
    """Retrieve a part has vehicle model year by my_row_id."""
    part_has_vehicle_model_year = get_part_has_vehicle_model_year(db=db, my_row_id=my_row_id)
    if part_has_vehicle_model_year is None:
        raise HTTPException(status_code=404, detail="Part has vehicle model year not found")
    return part_has_vehicle_model_year

@router.put("/{my_row_id}", response_model=PartHasVehicleHasModelYears)
def update_part_has_vehicle_model_year(my_row_id: int, part_has_vehicle_model_year: PartHasVehicleHasModelYearsUpdate, db: Session = Depends(get_db)):
    """Update an existing part has vehicle model year."""
    updated_part_has_vehicle_model_year = update_part_has_vehicle_model_year(db=db, my_row_id=my_row_id, **part_has_vehicle_model_year.dict())
    if updated_part_has_vehicle_model_year is None:
        raise HTTPException(status_code=404, detail="Part has vehicle model year not found")
    return updated_part_has_vehicle_model_year

@router.delete("/{my_row_id}", response_model=PartHasVehicleHasModelYears)
def delete_part_has_vehicle_model_year(my_row_id: int, db: Session = Depends(get_db)):
    """Delete a part has vehicle model year by my_row_id."""
    deleted_part_has_vehicle_model_year = delete_part_has_vehicle_model_year(db=db, my_row_id=my_row_id)
    if deleted_part_has_vehicle_model_year is None:
        raise HTTPException(status_code=404, detail="Part has vehicle model year not found")
    return deleted_part_has_vehicle_model_year