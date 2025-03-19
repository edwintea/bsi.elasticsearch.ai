# crud/part_image_ocr_has_part_number_cars.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.part_image_ocr_has_part_number_cars import PartImageOCRHasPartNumberCars
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_part_image_ocr_has_part_number_car(db: Session, my_row_id: int):
    """Retrieve a part image OCR has part number car by my_row_id."""
    try:
        return db.query(PartImageOCRHasPartNumberCars).filter(PartImageOCRHasPartNumberCars.my_row_id == my_row_id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part image OCR has part number car with my_row_id {my_row_id}: {e}")
        return None

def get_part_image_ocr_has_part_number_cars(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of part image OCR has part number cars with pagination."""
    try:
        return db.query(PartImageOCRHasPartNumberCars).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part image OCR has part number cars: {e}")
        return []

def create_part_image_ocr_has_part_number_car(db: Session, id: str, part_image_ocr_id: str, code: str, part_number: str, vehicle_id: int, part_id: int, part_image_id: int, part_number_car_id: int):
    """Create a new part image OCR has part number car."""
    part_image_ocr_has_part_number_car = PartImageOCRHasPartNumberCars(
        id=id,
        part_image_ocr_id=part_image_ocr_id,
        code=code,
        part_number=part_number,
        vehicle_id=vehicle_id,
        part_id=part_id,
        part_image_id=part_image_id,
        part_number_car_id=part_number_car_id
    )
    try:
        db.add(part_image_ocr_has_part_number_car)
        db.commit()
        db.refresh(part_image_ocr_has_part_number_car)
        return part_image_ocr_has_part_number_car
    except SQLAlchemyError as e:
        logger.error(f"Error creating part image OCR has part number car: {e}")
        db.rollback()
        return None

def update_part_image_ocr_has_part_number_car(db: Session, my_row_id: int, id: str, part_image_ocr_id: str, code: str, part_number: str, vehicle_id: int, part_id: int, part_image_id: int, part_number_car_id: int):
    """Update an existing part image OCR has part number car."""
    part_image_ocr_has_part_number_car = db.query(PartImageOCRHasPartNumberCars).filter(PartImageOCRHasPartNumberCars.my_row_id == my_row_id).first()
    if part_image_ocr_has_part_number_car:
        part_image_ocr_has_part_number_car.id = id
        part_image_ocr_has_part_number_car.part_image_ocr_id = part_image_ocr_id
        part_image_ocr_has_part_number_car.code = code
        part_image_ocr_has_part_number_car.part_number = part_number
        part_image_ocr_has_part_number_car.vehicle_id = vehicle_id
        part_image_ocr_has_part_number_car.part_id = part_id
        part_image_ocr_has_part_number_car.part_image_id = part_image_id
        part_image_ocr_has_part_number_car.part_number_car_id = part_number_car_id
        try:
            db.commit()
            return part_image_ocr_has_part_number_car
        except SQLAlchemyError as e:
            logger.error(f"Error updating part image OCR has part number car with my_row_id {my_row_id}: {e}")
            db.rollback()
            return None
    return None

def delete_part_image_ocr_has_part_number_car(db: Session, my_row_id: int):
    """Delete a part image OCR has part number car by my_row_id."""
    part_image_ocr_has_part_number_car = db.query(PartImageOCRHasPartNumberCars).filter(PartImageOCRHasPartNumberCars.my_row_id == my_row_id).first()
    if part_image_ocr_has_part_number_car:
        try:
            db.delete(part_image_ocr_has_part_number_car)
            db.commit()
            return part_image_ocr_has_part_number_car
        except SQLAlchemyError as e:
            logger.error(f"Error deleting part image OCR has part number car with my_row_id {my_row_id}: {e}")
            db.rollback()
            return None
    return None