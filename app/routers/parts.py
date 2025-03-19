# routers/parts.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.parts import Parts,PartsCreate,PartsUpdate,PartsBase,Optional
from ..crud.parts import create_part,get_parts,get_part,logger,delete_part,update_part

router = APIRouter()

@router.post("/", response_model=Parts)
def create_part(part: PartsCreate, db: Session = Depends(get_db)):
    """Create a new part."""
    return create_part(db=db, **part.dict())

@router.get("/", response_model=list[Parts])
def read_parts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of parts."""
    return get_parts(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=Parts)
def read_part(id: int, db: Session = Depends(get_db)):
    """Retrieve a part by ID."""
    part = get_part(db=db, id=id)
    if part is None:
        raise HTTPException(status_code=404, detail="Part not found")
    return part

@router.put("/{id}", response_model=Parts)
def update_part(id: int, part: PartsUpdate, db: Session = Depends(get_db)):
    """Update an existing part."""
    updated_part = update_part(db=db, id=id, **part.dict())
    if updated_part is None:
        raise HTTPException(status_code=404, detail="Part not found")
    return updated_part

@router.delete("/{id}", response_model=Parts)
def delete_part(id: int, db: Session = Depends(get_db)):
    """Delete a part by ID."""
    deleted_part = delete_part(db=db, id=id)
    if deleted_part is None:
        raise HTTPException(status_code=404, detail="Part not found")
    return deleted_part