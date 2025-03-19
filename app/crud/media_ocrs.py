# crud/media_ocrs.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.media_ocrs import MediaOCR
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_media_ocr(db: Session, id: int):
    """Retrieve a media OCR by ID."""
    try:
        return db.query(MediaOCR).filter(MediaOCR.id == id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving media OCR with id {id}: {e}")
        return None

def get_media_ocrs(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of media OCRs with pagination."""
    try:
        return db.query(MediaOCR).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving media OCRs: {e}")
        return []

def create_media_ocr(db: Session, media_id: int, name: str, ocr_raw: str, ocr_applied: str, ocr_applied_hash: str, percentage: int, folder_id: int, folder_path: str, status: int, meta: str):
    """Create a new media OCR."""
    media_ocr = MediaOCR(
        media_id=media_id,
        name=name,
        ocr_raw=ocr_raw,
        ocr_applied=ocr_applied,
        ocr_applied_hash=ocr_applied_hash,
        percentage=percentage,
        folder_id=folder_id,
        folder_path=folder_path,
        status=status,
        meta=meta
    )
    try:
        db.add(media_ocr)
        db.commit()
        db.refresh(media_ocr)
        return media_ocr
    except SQLAlchemyError as e:
        logger.error(f"Error creating media OCR: {e}")
        db.rollback()
        return None

def update_media_ocr(db: Session, id: int, media_id: int, name: str, ocr_raw: str, ocr_applied: str, ocr_applied_hash: str, percentage: int, folder_id: int, folder_path: str, status: int, meta: str):
    """Update an existing media OCR."""
    media_ocr = db.query(MediaOCR).filter(MediaOCR.id == id).first()
    if media_ocr:
        media_ocr.media_id = media_id
        media_ocr.name = name
        media_ocr.ocr_raw = ocr_raw
        media_ocr.ocr_applied = ocr_applied
        media_ocr.ocr_applied_hash = ocr_applied_hash
        media_ocr.percentage = percentage
        media_ocr.folder_id = folder_id
        media_ocr.folder_path = folder_path
        media_ocr.status = status
        media_ocr.meta = meta
        try:
            db.commit()
            return media_ocr
        except SQLAlchemyError as e:
            logger.error(f"Error updating media OCR with id {id}: {e}")
            db.rollback()
            return None
    return None

def delete_media_ocr(db: Session, id: int):
    """Delete a media OCR by ID."""
    media_ocr = db.query(MediaOCR).filter(MediaOCR.id == id).first()
    if media_ocr:
        try:
            db.delete(media_ocr)
            db.commit()
            return media_ocr
        except SQLAlchemyError as e:
            logger.error(f"Error deleting media OCR with id {id}: {e}")
            db.rollback()
            return None
    return None