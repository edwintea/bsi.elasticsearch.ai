# crud/vehicle_has_variants.py
from sqlalchemy.orm import Session
from ..models.vehicle_has_variants import VehicleHasVariants

def get_vehicle_variant(db: Session, id: int):
    return db.query(VehicleHasVariants).filter(VehicleHasVariants.id == id).first()

def get_vehicle_variants(db: Session, skip: int = 0, limit: int = 10):
    return db.query(VehicleHasVariants).offset(skip).limit(limit).all()

def create_vehicle_variant(db: Session, vehicle_id: int, value: str, meta: str = None):
    variant = VehicleHasVariants(
        vehicle_id=vehicle_id,
        value=value,
        meta=meta
    )
    db.add(variant)
    db.commit()
    db.refresh(variant)
    return variant