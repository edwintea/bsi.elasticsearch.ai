# schemas/vehicle_has_variants.py
from pydantic import BaseModel
from typing import Optional

class VehicleHasVariantsBase(BaseModel):
    vehicle_id: int
    value: str
    meta: Optional[str] = None

class VehicleHasVariantsCreate(VehicleHasVariantsBase):
    pass

class VehicleHasVariants(VehicleHasVariantsBase):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True