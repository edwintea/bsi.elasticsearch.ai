# crud/part_images.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.part_images import PartImages
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_part_image(db: Session, id: int):
    """Retrieve a part image by ID."""
    try:
        return db.query(PartImages).filter(PartImages.id == id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part image with id {id}: {e}")
        return None

def get_part_images(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of part images with pagination."""
    try:
        return db.query(PartImages).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part images: {e}")
        return []

def create_part_image(db: Session, name: str, vehicle_id: int, part_id: int, image: int, media_ocr_id: int, spatie_image_id: int, percentage: int, status_api: int, status: int, meta: str):
    """Create a new part image."""
    part_image = PartImages(
        name=name,
        vehicle_id=vehicle_id,
        part_id=part_id,
        image=image,
        media_ocr_id=media_ocr_id,
        spatie_image_id=spatie_image_id,
        percentage=percentage,
        status_api=status_api,
        status=status,
        meta=meta
    )
    try:
        db.add(part_image)
        db.commit()
        db.refresh(part_image)
        return part_image
    except SQLAlchemyError as e:
        logger.error(f"Error creating part image: {e}")
        db.rollback()
        return None

def update_part_image(db: Session, id: int, name: str, vehicle_id: int, part_id: int, image: int, media_ocr_id: int, spatie_image_id: int, percentage: int, status_api: int, status: int, meta: str):
    """Update an existing part image."""
    part_image = db.query(PartImages).filter(PartImages.id == id).first()
    if part_image:
        part_image.name = name
        part_image.vehicle_id = vehicle_id
        part_image.part_id = part_id
        part_image.image = image
        part_image.media_ocr_id = media_ocr_id
        part_image.spatie_image_id = spatie_image_id
        part_image.percentage = percentage
        part_image.status_api = status_api
        part_image.status = status
        part_image.meta = meta
        try:
            db.commit()
            return part_image
        except SQLAlchemyError as e:
            logger.error(f"Error updating part image with id {id}: {e}")
            db.rollback()
            return None
    return None

def delete_part_image(db: Session, id: int):
    """Delete a part image by ID."""
    part_image = db.query(PartImages).filter(PartImages.id == id).first()
    if part_image:
        try:
            db.delete(part_image)
            db.commit()
            return part_image
        except SQLAlchemyError as e:
            logger.error(f"Error deleting part image with id {id}: {e}")
            db.rollback()
            return None
    return None