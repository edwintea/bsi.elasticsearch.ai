# schemas/part_has_vehicle_has_variants.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartHasVehicleHasVariantsBase(BaseModel):
    part_has_vehicle_id: int
    value: str
    meta: Optional[str] = None

class PartHasVehicleHasVariantsCreate(PartHasVehicleHasVariantsBase):
    """Schema for creating a new part has vehicle variant."""
    pass

class PartHasVehicleHasVariantsUpdate(PartHasVehicleHasVariantsBase):
    """Schema for updating an existing part has vehicle variant."""
    pass

class PartHasVehicleHasVariants(PartHasVehicleHasVariantsBase):
    """Schema for returning part has vehicle variant data."""
    my_row_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True