# crud/part_categories.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.part_categories import PartCategory
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_part_category(db: Session, id: int):
    """Retrieve a part category by ID."""
    try:
        return db.query(PartCategory).filter(PartCategory.id == id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part category with id {id}: {e}")
        return None

def get_part_categories(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of part categories with pagination."""
    try:
        return db.query(PartCategory).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part categories: {e}")
        return []

def create_part_category(db: Session, name: str, image: int, description: str, x: float, y: float, status: int, meta: str):
    """Create a new part category."""
    part_category = PartCategory(
        name=name,
        image=image,
        description=description,
        x=x,
        y=y,
        status=status,
        meta=meta
    )
    try:
        db.add(part_category)
        db.commit()
        db.refresh(part_category)
        return part_category
    except SQLAlchemyError as e:
        logger.error(f"Error creating part category: {e}")
        db.rollback()
        return None

def update_part_category(db: Session, id: int, name: str, image: int, description: str, x: float, y: float, status: int, meta: str):
    """Update an existing part category."""
    part_category = db.query(PartCategory).filter(PartCategory.id == id).first()
    if part_category:
        part_category.name = name
        part_category.image = image
        part_category.description = description
        part_category.x = x
        part_category.y = y
        part_category.status = status
        part_category.meta = meta
        try:
            db.commit()
            return part_category
        except SQLAlchemyError as e:
            logger.error(f"Error updating part category with id {id}: {e}")
            db.rollback()
            return None
    return None

def delete_part_category(db: Session, id: int):
    """Delete a part category by ID."""
    part_category = db.query(PartCategory).filter(PartCategory.id == id).first()
    if part_category:
        try:
            db.delete(part_category)
            db.commit()
            return part_category
        except SQLAlchemyError as e:
            logger.error(f"Error deleting part category with id {id}: {e}")
            db.rollback()
            return None
    return None