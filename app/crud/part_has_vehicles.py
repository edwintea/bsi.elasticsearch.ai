# crud/part_has_vehicles.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.part_has_vehicles import PartHasVehicles
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_part_has_vehicle(db: Session, id: int):
    """Retrieve a part has vehicle by ID."""
    try:
        return db.query(PartHasVehicles).filter(PartHasVehicles.id == id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part has vehicle with id {id}: {e}")
        return None

def get_part_has_vehicles(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of part has vehicles with pagination."""
    try:
        return db.query(PartHasVehicles).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part has vehicles: {e}")
        return []

def create_part_has_vehicle(db: Session, vehicle_id: int, part_id: int, meta: str):
    """Create a new part has vehicle."""
    part_has_vehicle = PartHasVehicles(
        vehicle_id=vehicle_id,
        part_id=part_id,
        meta=meta
    )
    try:
        db.add(part_has_vehicle)
        db.commit()
        db.refresh(part_has_vehicle)
        return part_has_vehicle
    except SQLAlchemyError as e:
        logger.error(f"Error creating part has vehicle: {e}")
        db.rollback()
        return None

def update_part_has_vehicle(db: Session, id: int, vehicle_id: int, part_id: int, meta: str):
    """Update an existing part has vehicle."""
    part_has_vehicle = db.query(PartHasVehicles).filter(PartHasVehicles.id == id).first()
    if part_has_vehicle:
        part_has_vehicle.vehicle_id = vehicle_id
        part_has_vehicle.part_id = part_id
        part_has_vehicle.meta = meta
        try:
            db.commit()
            return part_has_vehicle
        except SQLAlchemyError as e:
            logger.error(f"Error updating part has vehicle with id {id}: {e}")
            db.rollback()
            return None
    return None

def delete_part_has_vehicle(db: Session, id: int):
    """Delete a part has vehicle by ID."""
    part_has_vehicle = db.query(PartHasVehicles).filter(PartHasVehicles.id == id).first()
    if part_has_vehicle:
        try:
            db.delete(part_has_vehicle)
            db.commit()
            return part_has_vehicle
        except SQLAlchemyError as e:
            logger.error(f"Error deleting part has vehicle with id {id}: {e}")
            db.rollback()
            return None
    return None