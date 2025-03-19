# routers/part_categories.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas.part_categories import PartCategories,PartCategoriesBase,PartCategoriesCreate,PartCategoriesUpdate
from ..crud.part_categories import get_part_categories,update_part_category,delete_part_category
router = APIRouter()

@router.post("/", response_model=PartCategories)
def create_part_category(part_category: PartCategoriesCreate, db: Session = Depends(get_db)):
    """Create a new part category."""
    return create_part_category(db=db, **part_category.dict())

@router.get("/", response_model=list[PartCategories])
def read_part_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of part categories."""
    return get_part_categories(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=PartCategories)
def read_part_category(id: int, db: Session = Depends(get_db)):
    """Retrieve a part category by ID."""
    part_category = get_part_categories(db=db, id=id)
    if part_category is None:
        raise HTTPException(status_code=404, detail="Part category not found")
    return part_category

@router.put("/{id}", response_model=PartCategories)
def update_part_category(id: int, part_category: PartCategoriesUpdate, db: Session = Depends(get_db)):
    """Update an existing part category."""
    updated_part_category = update_part_category(db=db, id=id, **part_category.dict())
    if updated_part_category is None:
        raise HTTPException(status_code=404, detail="Part category not found")
    return updated_part_category

    @router.delete("/{id}", response_model=PartCategories)
    def delete_part_category(id: int, db: Session = Depends(get_db)):
        """Delete a part category by ID."""
        deleted_part_category = delete_part_category(db=db, id=id)
        if deleted_part_category is None:
            raise HTTPException(status_code=404, detail="Part category not found")
        return deleted_part_category