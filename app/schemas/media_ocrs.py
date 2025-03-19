# schemas/media_ocrs.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MediaOCRsBase(BaseModel):
    media_id: int
    name: Optional[str] = None
    ocr_raw: Optional[str] = None
    ocr_applied: Optional[str] = None
    ocr_applied_hash: Optional[str] = None
    percentage: int = 0
    folder_id: int
    folder_path: Optional[str] = None
    status: int = 0
    meta: Optional[str] = None

class MediaOCRsCreate(MediaOCRsBase):
    """Schema for creating a new media OCR."""
    pass

class MediaOCRsUpdate(MediaOCRsBase):
    """Schema for updating an existing media OCR."""
    pass

class MediaOCRs(MediaOCRsBase):
    """Schema for returning media OCR data."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True