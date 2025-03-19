from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.media import Media, MediaCreate, MediaUpdate  # Correct import
from ..crud.media import create_media,update_media,delete_media,get_media,get_media_list

router = APIRouter()

@router.post("/", response_model=Media)
def create_media(media: MediaCreate, db: Session = Depends(get_db)):
    """Create a new media record."""
    return create_media(db=db, **media.dict())

@router.get("/", response_model=list[Media])
def read_media_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of media records."""
    return get_media_list(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=Media)
def read_media(id: int, db: Session = Depends(get_db)):
    """Retrieve a media record by ID."""
    media = get_media(db=db, id=id)
    if media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return media

@router.put("/{id}", response_model=Media)
def update_media(id: int, media: MediaUpdate, db: Session = Depends(get_db)):
    """Update an existing media record."""
    updated_media = update_media(db=db, id=id, **media.dict())
    if updated_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return updated_media

@router.delete("/{id}", response_model=Media)
def delete_media(id: int, db: Session = Depends(get_db)):
    """Delete a media record by ID."""
    deleted_media = delete_media(db=db, id=id)
    if deleted_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return deleted_media