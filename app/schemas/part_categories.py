# schemas/part_categories.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartCategoriesBase(BaseModel):
    name: Optional[str] = None
    image: Optional[int] = None
    description: Optional[str] = None
    x: Optional[float] = None
    y: Optional[float] = None
    status: Optional[int] = 0
    meta: Optional[str] = None

class PartCategoriesCreate(PartCategoriesBase):
    """Schema for creating a new part category."""
    pass

class PartCategoriesUpdate(PartCategoriesBase):
    """Schema for updating an existing part category."""
    pass

class PartCategories(PartCategoriesBase):
    """Schema for returning part category data."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True