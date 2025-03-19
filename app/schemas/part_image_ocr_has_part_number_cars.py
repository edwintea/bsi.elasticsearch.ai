# schemas/part_image_ocr_has_part_number_cars.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartImageOCRHasPartNumberCarsBase(BaseModel):
    id: str  # Assuming this is a UUID or similar
    part_image_ocr_id: Optional[str] = None
    code: Optional[str] = None
    part_number: Optional[str] = None
    vehicle_id: Optional[int] = None
    part_id: Optional[int] = None
    part_image_id: Optional[int] = None
    part_number_car_id: int  # This is required

class PartImageOCRHasPartNumberCarsCreate(PartImageOCRHasPartNumberCarsBase):
    """Schema for creating a new part image OCR has part number car."""
    pass

class PartImageOCRHasPartNumberCarsUpdate(PartImageOCRHasPartNumberCarsBase):
    """Schema for updating an existing part image OCR has part number car."""
    pass

class PartImageOCRHasPartNumberCars(PartImageOCRHasPartNumberCarsBase):
    """Schema for returning part image OCR has part number car data."""
    my_row_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True