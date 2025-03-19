# crud/part_number_cars.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.part_number_cars import PartNumberCars
import logging
from datetime import datetime

# Configure logging
logger = logging.getLogger(__name__)

def get_part_number_car(db: Session, id: int):
    """Retrieve a part number car by ID."""
    try:
        return db.query(PartNumberCars).filter(PartNumberCars.id == id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part number car with id {id}: {e}")
        return None

def get_part_number_cars(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of part number cars with pagination."""
    try:
        return db.query(PartNumberCars).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part number cars: {e}")
        return []

def create_part_number_car(db: Session, code: str, part_number: str, stock: int, price: int, product_category_id: int, product_type: str, name: str, description: str, remarks: str, colour: str, is_warranty: int, reference_code: str, year: str, part_label: str, alternatif_part_number: str, model_code: str, supplier_code: str, alternatif_part_name: str, is_manually_input: int, meta: str, updated_stock_at: datetime, api_last_checked: datetime, api_last_modified_value: datetime):
    """Create a new part number car."""
    part_number_car = PartNumberCars(
        code=code,
        part_number=part_number,
        stock=stock,
        price=price,
        product_category_id=product_category_id,
        product_type=product_type,
        name=name,
        description=description,
        remarks=remarks,
        colour=colour,
        is_warranty=is_warranty,
        reference_code=reference_code,
        year=year,
        part_label=part_label,
        alternatif_part_number=alternatif_part_number,
        model_code=model_code,
        supplier_code=supplier_code,
        alternatif_part_name=alternatif_part_name,
        is_manually_input=is_manually_input,
        meta=meta,
        updated_stock_at=updated_stock_at,
        api_last_checked=api_last_checked,
        api_last_modified_value=api_last_modified_value
    )
    try:
        db.add(part_number_car)
        db.commit()
        db.refresh(part_number_car)
        return part_number_car
    except SQLAlchemyError as e:
        logger.error(f"Error creating part number car: {e}")
        db.rollback()
        return None

def update_part_number_car(db: Session, id: int, code: str, part_number: str, stock: int, price: int, product_category_id: int, product_type: str, name: str, description: str, remarks: str, colour: str, is_warranty: int, reference_code: str, year: str, part_label: str, alternatif_part_number: str, model_code: str, supplier_code: str, alternatif_part_name: str, is_manually_input: int, meta: str, updated_stock_at: datetime, api_last_checked: datetime, api_last_modified_value: datetime):
    """Update an existing part number car."""
    part_number_car = db.query(PartNumberCars).filter(PartNumberCars.id == id).first()
    if part_number_car:
        part_number_car.code = code
        part_number_car.part_number = part_number
        part_number_car.stock = stock
        part_number_car.price = price
        part_number_car.product_category_id = product_category_id
        part_number_car.product_type = product_type
        part_number_car.name = name
        part_number_car.description = description
        part_number_car.remarks = remarks
        part_number_car.colour = colour
        part_number_car.is_warranty = is_warranty
        part_number_car.reference_code = reference_code
        part_number_car.year = year
        part_number_car.part_label = part_label
        part_number_car.alternatif_part_number = alternatif_part_number
        part_number_car.model_code = model_code
        part_number_car.supplier_code = supplier_code