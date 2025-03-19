# routers/part_has_vehicle_has_production_years.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.part_has_vehicle_has_production_years import PartHasVehicleHasProductionYears,PartHasVehicleHasProductionYearsBase,PartHasVehicleHasProductionYearsCreate,PartHasVehicleHasProductionYearsUpdate
from ..crud.part_has_vehicle_has_production_years import get_part_has_vehicle_production_years,get_part_has_vehicle_production_year,update_part_has_vehicle_production_year,delete_part_has_vehicle_production_year,create_part_has_vehicle_production_year
router = APIRouter()

@router.post("/", response_model=PartHasVehicleHasProductionYears)
def create_part_has_vehicle_production_year(part_has_vehicle_production_year: PartHasVehicleHasProductionYearsCreate, db: Session = Depends(get_db)):
    """Create a new part has vehicle production year."""
    return create_part_has_vehicle_production_year(db=db, **part_has_vehicle_production_year.dict())

@router.get("/", response_model=list[PartHasVehicleHasProductionYears])
def read_part_has_vehicle_production_years(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of part has vehicle production years."""
    return get_part_has_vehicle_production_years(db=db, skip=skip, limit=limit)

@router.get("/{my_row_id}", response_model=PartHasVehicleHasProductionYears)
def read_part_has_vehicle_production_year(my_row_id: int, db: Session = Depends(get_db)):
    """Retrieve a part has vehicle production year by my_row_id."""
    part_has_vehicle_production_year = get_part_has_vehicle_production_year(db=db, my_row_id=my_row_id)
    if part_has_vehicle_production_year is None:
        raise HTTPException(status_code=404, detail="Part has vehicle production year not found")
    return part_has_vehicle_production_year

@router.put("/{my_row_id}", response_model=PartHasVehicleHasProductionYears)
def update_part_has_vehicle_production_year(my_row_id: int, part_has_vehicle_production_year: PartHasVehicleHasProductionYearsUpdate, db: Session = Depends(get_db)):
    """Update an existing part has vehicle production year."""
    updated_part_has_vehicle_production_year = update_part_has_vehicle_production_year(db=db, my_row_id=my_row_id, **part_has_vehicle_production_year.dict())
    if updated_part_has_vehicle_production_year is None:
        raise HTTPException(status_code=404, detail="Part has vehicle production year not found")
    return updated_part_has_vehicle_production_year

@router.delete("/{my_row_id}", response_model=PartHasVehicleHasProductionYears)
def delete_part_has_vehicle_production_year(my_row_id: int, db: Session = Depends(get_db)):
    """Delete a part has vehicle production year by my_row_id."""
    deleted_part_has_vehicle_production_year = delete_part_has_vehicle_production_year(db=db, my_row_id=my_row_id)
    if deleted_part_has_vehicle_production_year is None:
        raise HTTPException(status_code=404, detail="Part has vehicle production year not found")
    return deleted_part_has_vehicle_production_year