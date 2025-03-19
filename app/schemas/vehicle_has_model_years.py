# schemas/vehicle_has_model_years.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VehicleHasModelYearsBase(BaseModel):
    vehicle_id: int
    value: str
    meta: Optional[str] = None

class VehicleHasModelYearsCreate(VehicleHasModelYearsBase):
    """Schema for creating a new vehicle model year."""
    pass

class VehicleHasModelYearsUpdate(VehicleHasModelYearsBase):
    """Schema for updating an existing vehicle model year."""
    pass

class VehicleHasModelYears(VehicleHasModelYearsBase):
    """Schema for returning vehicle model year data."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True