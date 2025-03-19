# schemas/part_number_cars.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartNumberCarsBase(BaseModel):
    code: Optional[str] = None
    part_number: Optional[str] = None
    stock: int = 0
    price: int = 0
    product_category_id: Optional[int] = None
    product_type: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    remarks: Optional[str] = None
    colour: Optional[str] = None
    is_warranty: int = 0
    reference_code: Optional[str] = None
    year: Optional[str] = None
    part_label: Optional[str] = None
    alternatif_part_number: Optional[str] = None
    model_code: Optional[str] = None
    supplier_code: Optional[str] = None
    alternatif_part_name: Optional[str] = None
    is_manually_input: int = 0
    meta: Optional[str] = None
    updated_stock_at: Optional[datetime] = None
    api_last_checked: Optional[datetime] = None
    api_last_modified_value: Optional[datetime] = None

class PartNumberCarsCreate(PartNumberCarsBase):
    """Schema for creating a new part number car."""
    pass

class PartNumberCarsUpdate(PartNumberCarsBase):
    """Schema for updating an existing part number car."""
    pass

class PartNumberCars(PartNumberCarsBase):
    """Schema for returning part number car data."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True