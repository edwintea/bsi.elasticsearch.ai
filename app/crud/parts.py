# crud/parts.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.parts import Parts
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_part(db: Session, id: int):
    """Retrieve a part by ID."""
    try:
        return db.query(Parts).filter(Parts.id == id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part with id {id}: {e}")
        return None

def get_parts(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of parts with pagination."""
    try:
        return db.query(Parts).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving parts: {e}")
        return []

def create_part(db: Session, code: str, name: str, part_group_id: int, part_category_id: int, image: int, description: str, status: int, meta: str):
    """Create a new part."""
    part = Parts(
        code=code,
        name=name,
        part_group_id=part_group_id,
        part_category_id=part_category_id,
        image=image,
        description=description,
        status=status,
        meta=meta
    )
    try:
        db.add(part)
        db.commit()
        db.refresh(part)
        return part
    except SQLAlchemyError as e:
        logger.error(f"Error creating part: {e}")
        db.rollback()
        return None

def update_part(db: Session, id: int, code: str, name: str, part_group_id: int, part_category_id: int, image: int, description: str, status: int, meta: str):
    """Update an existing part."""
    part = db.query(Parts).filter(Parts.id == id).first()
    if part:
        part.code = code
        part.name = name
        part.part_group_id = part_group_id
        part.part_category_id = part_category_id
        part.image = image
        part.description = description
        part.status = status
        part.meta = meta
        try:
            db.commit()
            return part
        except SQLAlchemyError as e:
            logger.error(f"Error updating part with id {id}: {e}")
            db.rollback()
            return None
    return None

def delete_part(db: Session, id: int):
    """Delete a part by ID."""
    part = db.query(Parts).filter(Parts.id == id).first()
    if part:
        try:
            db.delete(part)
            db.commit()
            return part
        except SQLAlchemyError as e:
            logger.error(f"Error deleting part with id {id}: {e}")
            db.rollback()
            return None
    return None