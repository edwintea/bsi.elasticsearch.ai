# routers/part_number_car_has_variants.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.part_number_car_has_variants import PartNumberCarHasVariants,PartNumberCarHasVariantsCreate,PartNumberCarHasVariantsBase,PartNumberCarHasVariantsUpdate
from ..crud.part_number_car_has_variants import get_part_number_car_variants,get_part_number_car_variant,create_part_number_car_variant,update_part_number_car_variant,delete_part_number_car_variant

router = APIRouter()

@router.post("/", response_model=PartNumberCarHasVariants)
def create_part_number_car_variant(variant: PartNumberCarHasVariantsCreate, db: Session = Depends(get_db)):
    """Create a new part number car variant."""
    return create_part_number_car_variant(db=db, **variant.dict())

@router.get("/", response_model=list[PartNumberCarHasVariants])
def read_part_number_car_variants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of part number car variants."""
    return get_part_number_car_variants(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=PartNumberCarHasVariants)
def read_part_number_car_variant(id: int, db: Session = Depends(get_db)):
    """Retrieve a part number car variant by ID."""
    variant = get_part_number_car_variant(db=db, id=id)
    if variant is None:
        raise HTTPException(status_code=404, detail="Part number car variant not found")
    return variant

@router.put("/{id}", response_model=PartNumberCarHasVariants)
def update_part_number_car_variant(id: int, variant: PartNumberCarHasVariantsUpdate, db: Session = Depends(get_db)):
    """Update an existing part number car variant."""
    updated_variant = update_part_number_car_variant(db=db, id=id, **variant.dict())
    if updated_variant is None:
        raise HTTPException(status_code=404, detail="Part number car variant not found")
    return updated_variant

@router.delete("/{id}", response_model=PartNumberCarHasVariants)
def delete_part_number_car_variant(id: int, db: Session = Depends(get_db)):
    """Delete a part number car variant by ID."""
    deleted_variant = delete_part_number_car_variant(db=db, id=id)
    if deleted_variant is None:
        raise HTTPException(status_code=404, detail="Part number car variant not found")
    return deleted_variant