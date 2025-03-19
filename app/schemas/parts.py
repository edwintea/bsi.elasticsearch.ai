# schemas/parts.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartsBase(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    part_group_id: Optional[int] = None
    part_category_id: Optional[int] = None
    image: Optional[int] = None
    description: Optional[str] = None
    status: Optional[int] = 0
    meta: Optional[str] = None
    published_at: Optional[datetime] = None

class PartsCreate(PartsBase):
    """Schema for creating a new part."""
    pass

class PartsUpdate(PartsBase):
    """Schema for updating an existing part."""
    pass

class Parts(PartsBase):
    """Schema for returning part data."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True