# routers/part_image_ocr_has_part_number_cars.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.part_image_ocr_has_part_number_cars import PartImageOCRHasPartNumberCarsBase,PartImageOCRHasPartNumberCars,PartImageOCRHasPartNumberCarsCreate,PartImageOCRHasPartNumberCarsUpdate
from ..crud.part_image_ocr_has_part_number_cars import get_part_image_ocr_has_part_number_cars,get_part_image_ocr_has_part_number_car,create_part_image_ocr_has_part_number_car,update_part_image_ocr_has_part_number_car,delete_part_image_ocr_has_part_number_car

router = APIRouter()

@router.post("/", response_model=PartImageOCRHasPartNumberCars)
def create_part_image_ocr_has_part_number_car(part_image_ocr_has_part_number_car: PartImageOCRHasPartNumberCarsCreate, db: Session = Depends(get_db)):
    """Create a new part image OCR has part number car."""
    return create_part_image_ocr_has_part_number_car(db=db, **part_image_ocr_has_part_number_car.dict())

@router.get("/", response_model=list[PartImageOCRHasPartNumberCars])
def read_part_image_ocr_has_part_number_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of part image OCR has part number cars."""
    return get_part_image_ocr_has_part_number_cars(db=db, skip=skip, limit=limit)

@router.get("/{my_row_id}", response_model=PartImageOCRHasPartNumberCars)
def read_part_image_ocr_has_part_number_car(my_row_id: int, db: Session = Depends(get_db)):
    """Retrieve a part image OCR has part number car by my_row_id."""
    part_image_ocr_has_part_number_car = get_part_image_ocr_has_part_number_car(db=db, my_row_id=my_row_id)
    if part_image_ocr_has_part_number_car is None:
        raise HTTPException(status_code=404, detail="Part image OCR has part number car not found")
    return part_image_ocr_has_part_number_car

@router.put("/{my_row_id}", response_model=PartImageOCRHasPartNumberCars)
def update_part_image_ocr_has_part_number_car(my_row_id: int, part_image_ocr_has_part_number_car: PartImageOCRHasPartNumberCarsUpdate, db: Session = Depends(get_db)):
    """Update an existing part image OCR has part number car."""
    updated_part_image_ocr_has_part_number_car = update_part_image_ocr_has_part_number_car(db=db, my_row_id=my_row_id, **part_image_ocr_has_part_number_car.dict())
    if updated_part_image_ocr_has_part_number_car is None:
        raise HTTPException(status_code=404, detail="Part image OCR has part number car not found")
    return updated_part_image_ocr_has_part_number_car

@router.delete("/{my_row_id}", response_model=PartImageOCRHasPartNumberCars)
def delete_part_image_ocr_has_part_number_car(my_row_id: int, db: Session = Depends(get_db)):
    """Delete a part image OCR has part number car by my_row_id."""
    deleted_part_image_ocr_has_part_number_car = delete_part_image_ocr_has_part_number_car(db=db, my_row_id=my_row_id)
    if deleted_part_image_ocr_has_part_number_car is None:
        raise HTTPException(status_code=404, detail="Part image OCR has part number car not found")
    return deleted_part_image_ocr_has_part_number_car