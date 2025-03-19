# routers/part_has_vehicle_has_variants.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.part_has_vehicle_has_variants import PartHasVehicleHasVariantsBase,PartHasVehicleHasVariantsCreate,PartHasVehicleHasVariants,PartHasVehicleHasVariantsUpdate
from ..crud.part_has_vehicle_has_variants import get_part_has_vehicle_variant,get_part_has_vehicle_variants,update_part_has_vehicle_variant,create_part_has_vehicle_variant,delete_part_has_vehicle_variant
router = APIRouter()

@router.post("/", response_model=PartHasVehicleHasVariants)
def create_part_has_vehicle_variant(part_has_vehicle_variant: PartHasVehicleHasVariantsCreate, db: Session = Depends(get_db)):
    """Create a new part has vehicle variant."""
    return create_part_has_vehicle_variant(db=db, **part_has_vehicle_variant.dict())

@router.get("/", response_model=list[PartHasVehicleHasVariants])
def read_part_has_vehicle_variants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of part has vehicle variants."""
    return get_part_has_vehicle_variants(db=db, skip=skip, limit=limit)

@router.get("/{my_row_id}", response_model=PartHasVehicleHasVariants)
def read_part_has_vehicle_variant(my_row_id: int, db: Session = Depends(get_db)):
    """Retrieve a part has vehicle variant by my_row_id."""
    part_has_vehicle_variant = get_part_has_vehicle_variant(db=db, my_row_id=my_row_id)
    if part_has_vehicle_variant is None:
        raise HTTPException(status_code=404, detail="Part has vehicle variant not found")
    return part_has_vehicle_variant

@router.put("/{my_row_id}", response_model=PartHasVehicleHasVariants)
def update_part_has_vehicle_variant(my_row_id: int, part_has_vehicle_variant: PartHasVehicleHasVariantsUpdate, db: Session = Depends(get_db)):
    """Update an existing part has vehicle variant."""
    updated_part_has_vehicle_variant = update_part_has_vehicle_variant(db=db, my_row_id=my_row_id, **part_has_vehicle_variant.dict())
    if updated_part_has_vehicle_variant is None:
        raise HTTPException(status_code=404, detail="Part has vehicle variant not found")
    return updated_part_has_vehicle_variant

@router.delete("/{my_row_id}", response_model=PartHasVehicleHasVariants)
def delete_part_has_vehicle_variant(my_row_id: int, db: Session = Depends(get_db)):
    """Delete a part has vehicle variant by my_row_id."""
    deleted_part_has_vehicle_variant = delete_part_has_vehicle_variant(db=db, my_row_id=my_row_id)
    if deleted_part_has_vehicle_variant is None:
        raise HTTPException(status_code=404, detail="Part has vehicle variant not found")
    return deleted_part_has_vehicle_variant