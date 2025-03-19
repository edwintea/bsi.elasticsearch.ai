# routers/part_images.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.part_images import PartImages,PartImagesBase,PartImagesCreate,PartImagesUpdate
from ..crud.part_images import create_part_image,get_part_image,get_part_images,update_part_image,delete_part_image
router = APIRouter()

@router.post("/", response_model=PartImages)
def create_part_image(part_image: PartImagesCreate, db: Session = Depends(get_db)):
    """Create a new part image."""
    return create_part_image(db=db, **part_image.dict())

@router.get("/", response_model=list[PartImages])
def read_part_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of part images."""
    return get_part_images(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=PartImages)
def read_part_image(id: int, db: Session = Depends(get_db)):
    """Retrieve a part image by ID."""
    part_image = get_part_image(db=db, id=id)
    if part_image is None:
        raise HTTPException(status_code=404, detail="Part image not found")
    return part_image

@router.put("/{id}", response_model=PartImages)
def update_part_image(id: int, part_image: PartImagesUpdate, db: Session = Depends(get_db)):
    """Update an existing part image."""
    updated_part_image = update_part_image(db=db, id=id, **part_image.dict())
    if updated_part_image is None:
        raise HTTPException(status_code=404, detail="Part image not found")
    return updated_part_image

@router.delete("/{id}", response_model=PartImages)
def delete_part_image(id: int, db: Session = Depends(get_db)):
    """Delete a part image by ID."""
    deleted_part_image = delete_part_image(db=db, id=id)
    if deleted_part_image is None:
        raise HTTPException(status_code=404, detail="Part image not found")
    return deleted_part_image