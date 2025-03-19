# crud/part_number_car_has_variants.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.part_number_car_has_variants import PartNumberCarHasVariants
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_part_number_car_variant(db: Session, id: int):
    """Retrieve a part number car variant by ID."""
    try:
        return db.query(PartNumberCarHasVariants).filter(PartNumberCarHasVariants.id == id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part number car variant with id {id}: {e}")
        return None

def get_part_number_car_variants(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of part number car variants with pagination."""
    try:
        return db.query(PartNumberCarHasVariants).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part number car variants: {e}")
        return []

def create_part_number_car_variant(db: Session, part_number_car_id: int, value: str, meta: str, part_number_car_alternate_id: str):
    """Create a new part number car variant."""
    variant = PartNumberCarHasVariants(
        part_number_car_id=part_number_car_id,
        value=value,
        meta=meta,
        part_number_car_alternate_id=part_number_car_alternate_id
    )
    try:
        db.add(variant)
        db.commit()
        db.refresh(variant)
        return variant
    except SQLAlchemyError as e:
        logger.error(f"Error creating part number car variant: {e}")
        db.rollback()
        return None

def update_part_number_car_variant(db: Session, id: int, part_number_car_id: int, value: str, meta: str, part_number_car_alternate_id: str):
    """Update an existing part number car variant."""
    variant = db.query(PartNumberCarHasVariants).filter(PartNumberCarHasVariants.id == id).first()
    if variant:
        variant.part_number_car_id = part_number_car_id
        variant.value = value
        variant.meta = meta
        variant.part_number_car_alternate_id = part_number_car_alternate_id
        try:
            db.commit()
            return variant
        except SQLAlchemyError as e:
            logger.error(f"Error updating part number car variant with id {id}: {e}")
            db.rollback()
            return None
    return None

def delete_part_number_car_variant(db: Session, id: int):
    """Delete a part number car variant by ID."""
    variant = db.query(PartNumberCarHasVariants).filter(PartNumberCarHasVariants.id == id).first()
    if variant:
        try:
            db.delete(variant)
            db.commit()
            return variant
        except SQLAlchemyError as e:
            logger.error(f"Error deleting part number car variant with id {id}: {e}")
            db.rollback()
            return None
    return None