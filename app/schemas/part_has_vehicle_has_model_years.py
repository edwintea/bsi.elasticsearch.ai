# schemas/part_has_vehicle_has_model_years.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartHasVehicleHasModelYearsBase(BaseModel):
    part_has_vehicle_id: int
    value: str
    meta: Optional[str] = None

class PartHasVehicleHasModelYearsCreate(PartHasVehicleHasModelYearsBase):
    """Schema for creating a new part has vehicle model year."""
    pass

class PartHasVehicleHasModelYearsUpdate(PartHasVehicleHasModelYearsBase):
    """Schema for updating an existing part has vehicle model year."""
    pass

class PartHasVehicleHasModelYears(PartHasVehicleHasModelYearsBase):
    """Schema for returning part has vehicle model year data."""
    my_row_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True