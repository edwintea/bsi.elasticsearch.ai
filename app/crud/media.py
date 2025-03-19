# crud/media.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.media import Media
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_media(db: Session, id: int):
    """Retrieve a media record by ID."""
    try:
        print("ok")
        return db.query(Media).filter(Media.id == id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving media with id {id}: {e}")
        return None

def get_media_list(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of media records with pagination."""
    try:
        return db.query(Media).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving media records: {e}")
        return []

def create_media(db: Session, model_type: str, model_id: int, uuid: str, collection_name: str, name: str, file_name: str, mime_type: str, disk: str, conversions_disk: str, size: int, manipulations: str, custom_properties: str, generated_conversions: str, responsive_images: str, order_column: int):
    """Create a new media record."""
    media = Media(
        model_type=model_type,
        model_id=model_id,
        uuid=uuid,
        collection_name=collection_name,
        name=name,
        file_name=file_name,
        mime_type=mime_type,
        disk=disk,
        conversions_disk=conversions_disk,
        size=size,
        manipulations=manipulations,
        custom_properties=custom_properties,
        generated_conversions=generated_conversions,
        responsive_images=responsive_images,
        order_column=order_column
    )
    try:
        db.add(media)
        db.commit()
        db.refresh(media)
        return media
    except SQLAlchemyError as e:
        logger.error(f"Error creating media record: {e}")
        db.rollback()
        return None

def update_media(db: Session, id: int, model_type: str, model_id: int, uuid: str, collection_name: str, name: str, file_name: str, mime_type: str, disk: str, conversions_disk: str, size: int, manipulations: str, custom_properties: str, generated_conversions: str, responsive_images: str, order_column: int):
    """Update an existing media record."""
    media = db.query(Media).filter(Media.id == id).first()
    if media:
        media.model_type = model_type
        media.model_id = model_id
        media.uuid = uuid
        media.collection_name = collection_name
        media.name = name
        media.file_name = file_name
        media.mime_type = mime_type
        media.disk = disk
        media.conversions_disk = conversions_disk
        media.size = size
        media.manipulations = manipulations
        media.custom_properties = custom_properties
        media.generated_conversions = generated_conversions
        media.responsive_images = responsive_images
        media.order_column = order_column
        try:
            db.commit()
            return media
        except SQLAlchemyError as e:
            logger.error(f"Error updating media with id {id}: {e}")
            db.rollback()
            return None
    return None

def delete_media(db: Session, id: int):
    """Delete a media record by ID."""
    media = db.query(Media).filter(Media.id == id).first()
    if media:
        try:
            db.delete(media)
            db.commit()
            return media
        except SQLAlchemyError as e:
            logger.error(f"Error deleting media with id {id}: {e}")
            db.rollback()
            return None
    return None