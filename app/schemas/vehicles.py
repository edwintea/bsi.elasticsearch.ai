# schemas/vehicles.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VehiclesBase(BaseModel):
    title: Optional[str] = None
    slug: str
    description: Optional[str] = None
    image: Optional[int] = None
    model: Optional[str] = None
    status: Optional[int] = 0
    meta: Optional[str] = None
    published_at: Optional[datetime] = None
    category_description: str = "Light Duty"
    emission: str = "EURO 2"

class VehiclesCreate(VehiclesBase):
    pass

class VehiclesUpdate(VehiclesBase):
    pass

class Vehicles(VehiclesBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True