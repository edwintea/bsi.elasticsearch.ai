# schemas/part_has_vehicles.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartHasVehiclesBase(BaseModel):
    vehicle_id: int
    part_id: int
    meta: Optional[str] = None

class PartHasVehiclesCreate(PartHasVehiclesBase):
    """Schema for creating a new part has vehicle."""
    pass

class PartHasVehiclesUpdate(PartHasVehiclesBase):
    """Schema for updating an existing part has vehicle."""
    pass

class PartHasVehicles(PartHasVehiclesBase):
    """Schema for returning part has vehicle data."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True