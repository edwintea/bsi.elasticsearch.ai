# crud/vehicle_has_model_years.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.vehicle_has_model_years import VehicleHasModelYears
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_vehicle_model_year(db: Session, id: int):
    """Retrieve a vehicle model year by ID."""
    try:
        return db.query(VehicleHasModelYears).filter(VehicleHasModelYears.id == id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving vehicle model year with id {id}: {e}")
        return None

def get_vehicle_model_years(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of vehicle model years with pagination."""
    try:
        return db.query(VehicleHasModelYears).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving vehicle model years: {e}")
        return []

def create_vehicle_model_year(db: Session, vehicle_id: int, value: str, meta: str = None):
    """Create a new vehicle model year."""
    model_year = VehicleHasModelYears(
        vehicle_id=vehicle_id,
        value=value,
        meta=meta
    )
    try:
        db.add(model_year)
        db.commit()
        db.refresh(model_year)
        return model_year
    except SQLAlchemyError as e:
        logger.error(f"Error creating vehicle model year: {e}")
        db.rollback()
        return None

def update_vehicle_model_year(db: Session, id: int, vehicle_id: int, value: str, meta: str = None):
    """Update an existing vehicle model year."""
    model_year = db.query(VehicleHasModelYears).filter(VehicleHasModelYears.id == id).first()
    if model_year:
        model_year.vehicle_id = vehicle_id
        model_year.value = value
        model_year.meta = meta
        try:
            db.commit()
            return model_year
        except SQLAlchemyError as e:
            logger.error(f"Error updating vehicle model year with id {id}: {e}")
            db.rollback()
            return None
    return None

def delete_vehicle_model_year(db: Session, id: int):
    """Delete a vehicle model year by ID."""
    model_year = db.query(VehicleHasModelYears).filter(VehicleHasModelYears.id == id).first()
    if model_year:
        try:
            db.delete(model_year)
            db.commit()
            return model_year
        except SQLAlchemyError as e:
            logger.error(f"Error deleting vehicle model year with id {id}: {e}")
            db.rollback()
            return None
    return None