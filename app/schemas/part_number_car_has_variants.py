# schemas/part_number_car_has_variants.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartNumberCarHasVariantsBase(BaseModel):
    part_number_car_id: int
    value: str
    meta: Optional[str] = None
    part_number_car_alternate_id: str

class PartNumberCarHasVariantsCreate(PartNumberCarHasVariantsBase):
    """Schema for creating a new part number car variant."""
    pass

class PartNumberCarHasVariantsUpdate(PartNumberCarHasVariantsBase):
    """Schema for updating an existing part number car variant."""
    pass

class PartNumberCarHasVariants(PartNumberCarHasVariantsBase):
    """Schema for returning part number car variant data."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True