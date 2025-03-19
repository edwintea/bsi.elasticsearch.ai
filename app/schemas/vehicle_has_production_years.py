# schemas/vehicle_has_production_years.py
from pydantic import BaseModel
from typing import Optional

class VehicleHasProductionYearsBase(BaseModel):
    vehicle_id: int
    value: str
    meta: Optional[str] = None

class VehicleHasProductionYearsCreate(VehicleHasProductionYearsBase):
    pass

class VehicleHasProductionYears(VehicleHasProductionYearsBase):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True