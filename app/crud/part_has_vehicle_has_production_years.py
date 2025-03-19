# crud/part_has_vehicle_has_production_years.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.part_has_vehicle_has_production_years import PartHasVehicleHasProductionYears
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_part_has_vehicle_production_year(db: Session, my_row_id: int):
    """Retrieve a part has vehicle production year by my_row_id."""
    try:
        return db.query(PartHasVehicleHasProductionYears).filter(PartHasVehicleHasProductionYears.my_row_id == my_row_id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part has vehicle production year with my_row_id {my_row_id}: {e}")
        return None

def get_part_has_vehicle_production_years(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of part has vehicle production years with pagination."""
    try:
        return db.query(PartHasVehicleHasProductionYears).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part has vehicle production years: {e}")
        return []

def create_part_has_vehicle_production_year(db: Session, part_has_vehicle_id: int, value: str, meta: str):
    """Create a new part has vehicle production year."""
    part_has_vehicle_production_year = PartHasVehicleHasProductionYears(
        part_has_vehicle_id=part_has_vehicle_id,
        value=value,
        meta=meta
    )
    try:
        db.add(part_has_vehicle_production_year)
        db.commit()
        db.refresh(part_has_vehicle_production_year)
        return part_has_vehicle_production_year
    except SQLAlchemyError as e:
        logger.error(f"Error creating part has vehicle production year: {e}")
        db.rollback()
        return None

def update_part_has_vehicle_production_year(db: Session, my_row_id: int, part_has_vehicle_id: int, value: str, meta: str):
    """Update an existing part has vehicle production year."""
    part_has_vehicle_production_year = db.query(PartHasVehicleHasProductionYears).filter(PartHasVehicleHasProductionYears.my_row_id == my_row_id).first()
    if part_has_vehicle_production_year:
        part_has_vehicle_production_year.part_has_vehicle_id = part_has_vehicle_id
        part_has_vehicle_production_year.value = value
        part_has_vehicle_production_year.meta = meta
        try:
            db.commit()
            return part_has_vehicle_production_year
        except SQLAlchemyError as e:
            logger.error(f"Error updating part has vehicle production year with my_row_id {my_row_id}: {e}")
            db.rollback()
            return None
    return None

def delete_part_has_vehicle_production_year(db: Session, my_row_id: int):
    """Delete a part has vehicle production year by my_row_id."""
    part_has_vehicle_production_year = db.query(PartHasVehicleHasProductionYears).filter(PartHasVehicleHasProductionYears.my_row_id == my_row_id).first()
    if part_has_vehicle_production_year:
        try:
            db.delete(part_has_vehicle_production_year)
            db.commit()
            return part_has_vehicle_production_year
        except SQLAlchemyError as e:
            logger.error(f"Error deleting part has vehicle production year with my_row_id {my_row_id}: {e}")
            db.rollback()
            return None
    return None