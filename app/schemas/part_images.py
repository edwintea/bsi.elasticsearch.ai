# schemas/part_images.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PartImagesBase(BaseModel):
    name: Optional[str] = None
    vehicle_id: Optional[int] = None
    part_id: Optional[int] = None
    image: Optional[int] = None
    media_ocr_id: Optional[int] = None
    spatie_image_id: Optional[int] = None
    percentage: Optional[int] = None
    status_api: Optional[int] = 0
    status: Optional[int] = 0
    meta: Optional[str] = None

class PartImagesCreate(PartImagesBase):
    """Schema for creating a new part image."""
    pass

class PartImagesUpdate(PartImagesBase):
    """Schema for updating an existing part image."""
    pass

class PartImages(PartImagesBase):
    """Schema for returning part image data."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True