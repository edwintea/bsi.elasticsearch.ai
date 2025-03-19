# schemas/part_image_ocrs.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartImageOCRsBase(BaseModel):
    id: str  # Assuming this is a UUID or similar
    code: Optional[str] = None
    text_ori: Optional[str] = None
    ocr_pos_hash: Optional[str] = None
    vehicle_id: Optional[int] = None
    part_id: Optional[int] = None
    part_image_id: Optional[int] = None
    coordinate: Optional[str] = None
    status: Optional[int] = 0
    meta: Optional[str] = None
    status_api: Optional[int] = 0

class PartImageOCRsCreate(PartImageOCRsBase):
    """Schema for creating a new part image OCR."""
    pass

class PartImageOCRsUpdate(PartImageOCRsBase):
    """Schema for updating an existing part image OCR."""
    pass

class PartImageOCRs(PartImageOCRsBase):
    """Schema for returning part image OCR data."""
    my_row_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True