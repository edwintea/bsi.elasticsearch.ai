# crud/part_image_ocrs.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.part_image_ocrs import PartImageOCRs
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_part_image_ocr(db: Session, my_row_id: int):
    """Retrieve a part image OCR by my_row_id."""
    try:
        return db.query(PartImageOCRs).filter(PartImageOCRs.my_row_id == my_row_id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part image OCR with my_row_id {my_row_id}: {e}")
        return None

def get_part_image_ocrs(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of part image OCRs with pagination."""
    try:
        return db.query(PartImageOCRs).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving part image OCRs: {e}")
        return []

def create_part_image_ocr(db: Session, id: str, code: str, text_ori: str, ocr_pos_hash: str, vehicle_id: int, part_id: int, part_image_id: int, coordinate: str, status: int, meta: str, status_api: int):
    """Create a new part image OCR."""
    part_image_ocr = PartImageOCRs(
        id=id,
        code=code,
        text_ori=text_ori,
        ocr_pos_hash=ocr_pos_hash,
        vehicle_id=vehicle_id,
        part_id=part_id,
        part_image_id=part_image_id,
        coordinate=coordinate,
        status=status,
        meta=meta,
        status_api=status_api
    )
    try:
        db.add(part_image_ocr)
        db.commit()
        db.refresh(part_image_ocr)
        return part_image_ocr
    except SQLAlchemyError as e:
        logger.error(f"Error creating part image OCR: {e}")
        db.rollback()
        return None

def update_part_image_ocr(db: Session, my_row_id: int, id: str, code: str, text_ori: str, ocr_pos_hash: str, vehicle_id: int, part_id: int, part_image_id: int, coordinate: str, status: int, meta: str, status_api: int):
    """Update an existing part image OCR."""
    part_image_ocr = db.query(PartImageOCRs).filter(PartImageOCRs.my_row_id == my_row_id).first()
    if part_image_ocr:
        part_image_ocr.id = id
        part_image_ocr.code = code
        part_image_ocr.text_ori = text_ori
        part_image_ocr.ocr_pos_hash = ocr_pos_hash
        part_image_ocr.vehicle_id = vehicle_id
        part_image_ocr.part_id = part_id
        part_image_ocr.part_image_id = part_image_id
        part_image_ocr.coordinate = coordinate
        part_image_ocr.status = status
        part_image_ocr.meta = meta
        part_image_ocr.status_api = status_api
        try:
            db.commit()
            return part_image_ocr
        except SQLAlchemyError as e:
            logger.error(f"Error updating part image OCR with my_row_id {my_row_id}: {e}")
            db.rollback()
            return None
    return None

def delete_part_image_ocr(db: Session, my_row_id: int):
    """Delete a part image OCR by my_row_id."""
    part_image_ocr = db.query(PartImageOCRs).filter(PartImageOCRs.my_row_id == my_row_id).first()
    if part_image_ocr:
        try:
            db.delete(part_image_ocr)
            db.commit()
            return part_image_ocr
        except SQLAlchemyError as e:
            logger.error(f"Error deleting part image OCR with my_row_id {my_row_id}: {e}")
            db.rollback()
            return None
    return None