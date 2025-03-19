# schemas/vehicle_has_source_of_truths.py
from pydantic import BaseModel
from typing import Optional

class VehicleHasSourceOfTruthsBase(BaseModel):
    vehicle_id: int
    path: str
    data: Optional[str] = None
    summary: Optional[str] = None

class VehicleHasSourceOfTruthsCreate(VehicleHasSourceOfTruthsBase):
    pass

class VehicleHasSourceOfTruths(VehicleHasSourceOfTruthsBase):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True