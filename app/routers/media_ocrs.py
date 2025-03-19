# routers/media_ocrs.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from .. import crud, schemas
from ..crud.media_ocrs import create_media_ocr,get_media_ocrs,update_media_ocr,delete_media_ocr
from ..schemas.media_ocrs import MediaOCRs,MediaOCRsCreate,MediaOCRsBase,MediaOCRsUpdate

router = APIRouter()

@router.post("/", response_model=MediaOCRs)
def create_media_ocr(media_ocr: MediaOCRsCreate, db: Session = Depends(get_db)):
    """Create a new media OCR."""
    return create_media_ocr(db=db, **media_ocr.dict())

@router.get("/", response_model=list[MediaOCRs])
def read_media_ocrs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of media OCRs."""
    return get_media_ocrs(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=MediaOCRs)
def read_media_ocr(id: int, db: Session = Depends(get_db)):
    """Retrieve a media OCR by ID."""
    media_ocr = get_media_ocrs(db=db, id=id)
    if media_ocr is None:
        raise HTTPException(status_code=404, detail="Media OCR not found")
    return media_ocr

@router.put("/{id}", response_model=MediaOCRs)
def update_media_ocr(id: int, media_ocr: MediaOCRsUpdate, db: Session = Depends(get_db)):
    """Update an existing media OCR."""
    updated_media_ocr = update_media_ocr(db=db, id=id, **media_ocr.dict())
    if updated_media_ocr is None:
        raise HTTPException(status_code=404, detail="Media OCR not found")
    return updated_media_ocr

@router.delete("/{id}", response_model=MediaOCRs)
def delete_media_ocr(id: int, db: Session = Depends(get_db)):
    """Delete a media OCR by ID."""
    deleted_media_ocr = delete_media_ocr(db=db, id=id)
    if deleted_media_ocr is None:
        raise HTTPException(status_code=404, detail="Media OCR not found")
    return deleted_media_ocr