from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MediaBase(BaseModel):
    model_type: str
    model_id: int
    uuid: Optional[str] = None
    collection_name: str
    name: str
    file_name: str
    mime_type: Optional[str] = None
    disk: str
    conversions_disk: Optional[str] = None
    size: int
    manipulations: str
    custom_properties: str
    generated_conversions: str
    responsive_images: str
    order_column: Optional[int] = None

class MediaCreate(MediaBase):
    """Schema for creating a new media record."""
    pass

class MediaUpdate(MediaBase):
    """Schema for updating an existing media record."""
    pass

class Media(MediaBase):
    """Schema for returning media data."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True