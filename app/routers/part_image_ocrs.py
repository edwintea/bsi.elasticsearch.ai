# routers/part_image_ocrs.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.part_image_ocrs import PartImageOCRs,PartImageOCRsBase,PartImageOCRsCreate,PartImageOCRsUpdate
from ..crud.part_image_ocrs import create_part_image_ocr,get_part_image_ocr,get_part_image_ocrs,delete_part_image_ocr,update_part_image_ocr

router = APIRouter()

@router.post("/", response_model=PartImageOCRs)
def create_part_image_ocr(part_image_ocr: PartImageOCRsCreate, db: Session = Depends(get_db)):
    """Create a new part image OCR."""
    return create_part_image_ocr(db=db, **part_image_ocr.dict())

@router.get("/", response_model=list[PartImageOCRs])
def read_part_image_ocrs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of part image OCRs."""
    return get_part_image_ocrs(db=db, skip=skip, limit=limit)

@router.get("/{my_row_id}", response_model=PartImageOCRs)
def read_part_image_ocr(my_row_id: int, db: Session = Depends(get_db)):
    """Retrieve a part image OCR by my_row_id."""
    part_image_ocr = get_part_image_ocr(db=db, my_row_id=my_row_id)
    if part_image_ocr is None:
        raise HTTPException(status_code=404, detail="Part image OCR not found")
    return part_image_ocr

@router.put("/{my_row_id}", response_model=PartImageOCRs)
def update_part_image_ocr(my_row_id: int, part_image_ocr: PartImageOCRsUpdate, db: Session = Depends(get_db)):
    """Update an existing part image OCR."""
    updated_part_image_ocr = update_part_image_ocr(db=db, my_row_id=my_row_id, **part_image_ocr.dict())
    if updated_part_image_ocr is None:
        raise HTTPException(status_code=404, detail="Part image OCR not found")
    return updated_part_image_ocr

@router.delete("/{my_row_id}", response_model=PartImageOCRs)
def delete_part_image_ocr(my_row_id: int, db: Session = Depends(get_db)):
    """Delete a part image OCR by my_row_id."""
    deleted_part_image_ocr = delete_part_image_ocr(db=db, my_row_id=my_row_id)
    if deleted_part_image_ocr is None:
        raise HTTPException(status_code=404, detail="Part image OCR not found")
    return deleted_part_image_ocr