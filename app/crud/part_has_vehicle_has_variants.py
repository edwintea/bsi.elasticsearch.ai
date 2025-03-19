# crud/part_has_vehicle_has_variants.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.part_has_vehicle_has_variants import PartHasVehicleHasVariants
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_part_has_vehicle_variant(db: Session, my_row_id: int):
    """Retrieve a part has vehicle variant by my_row_id."""
    try:
        return db.query(PartHasVehicleHasVariants).filter(PartHasVehicleHasVariants.my_row_id == my_row_id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part has vehicle variant with my_row_id {my_row_id}: {e}")
        return None

def get_part_has_vehicle_variants(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of part has vehicle variants with pagination."""
    try:
        return db.query(PartHasVehicleHasVariants).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part has vehicle variants: {e}")
        return []

def create_part_has_vehicle_variant(db: Session, part_has_vehicle_id: int, value: str, meta: str):
    """Create a new part has vehicle variant."""
    part_has_vehicle_variant = PartHasVehicleHasVariants(
        part_has_vehicle_id=part_has_vehicle_id,
        value=value,
        meta=meta
    )
    try:
        db.add(part_has_vehicle_variant)
        db.commit()
        db.refresh(part_has_vehicle_variant)
        return part_has_vehicle_variant
    except SQLAlchemyError as e:
        logger.error(f"Error creating part has vehicle variant: {e}")
        db.rollback()
        return None

def update_part_has_vehicle_variant(db: Session, my_row_id: int, part_has_vehicle_id: int, value: str, meta: str):
    """Update an existing part has vehicle variant."""
    part_has_vehicle_variant = db.query(PartHasVehicleHasVariants).filter(PartHasVehicleHasVariants.my_row_id == my_row_id).first()
    if part_has_vehicle_variant:
        part_has_vehicle_variant.part_has_vehicle_id = part_has_vehicle_id
        part_has_vehicle_variant.value = value
        part_has_vehicle_variant.meta = meta
        try:
            db.commit()
            return part_has_vehicle_variant
        except SQLAlchemyError as e:
            logger.error(f"Error updating part has vehicle variant with my_row_id {my_row_id}: {e}")
            db.rollback()
            return None
    return None

def delete_part_has_vehicle_variant(db: Session, my_row_id: int):
    """Delete a part has vehicle variant by my_row_id."""
    part_has_vehicle_variant = db.query(PartHasVehicleHasVariants).filter(PartHasVehicleHasVariants.my_row_id == my_row_id).first()
    if part_has_vehicle_variant:
        try:
            db.delete(part_has_vehicle_variant)
            db.commit()
            return part_has_vehicle_variant
        except SQLAlchemyError as e:
            logger.error(f"Error deleting part has vehicle variant with my_row_id {my_row_id}: {e}")
            db.rollback()
            return None
    return None