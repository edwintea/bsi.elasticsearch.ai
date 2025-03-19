# schemas/part_groups.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartGroupsBase(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    part_category_id: Optional[int] = None
    image: Optional[int] = None
    description: Optional[str] = None
    status: Optional[int] = 0
    meta: Optional[str] = None

class PartGroupsCreate(PartGroupsBase):
    """Schema for creating a new part group."""
    pass

class PartGroupsUpdate(PartGroupsBase):
    """Schema for updating an existing part group."""
    pass

class PartGroups(PartGroupsBase):
    """Schema for returning part group data."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True