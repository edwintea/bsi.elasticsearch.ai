# schemas/part_has_vehicle_has_production_years.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartHasVehicleHasProductionYearsBase(BaseModel):
    part_has_vehicle_id: int
    value: str
    meta: Optional[str] = None

class PartHasVehicleHasProductionYearsCreate(PartHasVehicleHasProductionYearsBase):
    """Schema for creating a new part has vehicle production year."""
    pass

class PartHasVehicleHasProductionYearsUpdate(PartHasVehicleHasProductionYearsBase):
    """Schema for updating an existing part has vehicle production year."""
    pass

class PartHasVehicleHasProductionYears(PartHasVehicleHasProductionYearsBase):
    """Schema for returning part has vehicle production year data."""
    my_row_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True