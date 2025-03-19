# crud/part_groups.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.part_groups import PartGroup
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_part_group(db: Session, id: int):
    """Retrieve a part group by ID."""
    try:
        return db.query(PartGroup).filter(PartGroup.id == id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part group with id {id}: {e}")
        return None

def get_part_groups(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of part groups with pagination."""
    try:
        return db.query(PartGroup).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part groups: {e}")
        return []

def create_part_group(db: Session, code: str, name: str, part_category_id: int, image: int, description: str, status: int, meta: str):
    """Create a new part group."""
    part_group = PartGroup(
        code=code,
        name=name,
        part_category_id=part_category_id,
        image=image,
        description=description,
        status=status,
        meta=meta
    )
    try:
        db.add(part_group)
        db.commit()
        db.refresh(part_group)
        return part_group
    except SQLAlchemyError as e:
        logger.error(f"Error creating part group: {e}")
        db.rollback()
        return None

def update_part_group(db: Session, id: int, code: str, name: str, part_category_id: int, image: int, description: str, status: int, meta: str):
    """Update an existing part group."""
    part_group = db.query(PartGroup).filter(PartGroup.id == id).first()
    if part_group:
        part_group.code = code
        part_group.name = name
        part_group.part_category_id = part_category_id
        part_group.image = image
        part_group.description = description
        part_group.status = status
        part_group.meta = meta
        try:
            db.commit()
            return part_group
        except SQLAlchemyError as e:
            logger.error(f"Error updating part group with id {id}: {e}")
            db.rollback()
            return None
    return None

def delete_part_group(db: Session, id: int):
    """Delete a part group by ID."""
    part_group = db.query(PartGroup).filter(PartGroup.id == id).first()
    if part_group:
        try:
            db.delete(part_group)
            db.commit()
            return part_group
        except SQLAlchemyError as e:
            logger.error(f"Error deleting part group with id {id}: {e}")
            db.rollback()
            return None
    return None