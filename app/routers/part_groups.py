# routers/part_groups.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.part_groups import PartGroups,PartGroupsBase,PartGroupsCreate,PartGroupsUpdate
from ..crud.part_groups import get_part_group,get_part_groups,update_part_group,delete_part_group,create_part_group
router = APIRouter()

@router.post("/", response_model=PartGroups)
def create_part_group(part_group: PartGroupsCreate, db: Session = Depends(get_db)):
    """Create a new part group."""
    return create_part_group(db=db, **part_group.dict())

@router.get("/", response_model=list[PartGroups])
def read_part_groups(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of part groups."""
    return get_part_groups(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=PartGroups)
def read_part_group(id: int, db: Session = Depends(get_db)):
    """Retrieve a part group by ID."""
    part_group = get_part_group(db=db, id=id)
    if part_group is None:
        raise HTTPException(status_code=404, detail="Part group not found")
    return part_group

@router.put("/{id}", response_model=PartGroups)
def update_part_group(id: int, part_group: PartGroupsUpdate, db: Session = Depends(get_db)):
    """Update an existing part group."""
    updated_part_group = update_part_group(db=db, id=id, **part_group.dict())
    if updated_part_group is None:
        raise HTTPException(status_code=404, detail="Part group not found")
    return updated_part_group

@router.delete("/{id}", response_model=PartGroups)
def delete_part_group(id: int, db: Session = Depends(get_db)):
    """Delete a part group by ID."""
    deleted_part_group = delete_part_group(db=db, id=id)
    if deleted_part_group is None:
        raise HTTPException(status_code=404, detail="Part group not found")
    return deleted_part_group