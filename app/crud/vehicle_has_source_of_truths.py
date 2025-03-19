# crud/vehicle_has_source_of_truths.py
from sqlalchemy.orm import Session
from ..models.vehicle_has_source_of_truths import VehicleHasSourceOfTruths

def get_vehicle_source_of_truth(db: Session, id: int):
    return db.query(VehicleHasSourceOfTruths).filter(VehicleHasSourceOfTruths.id == id).first()

def get_vehicle_sources_of_truth(db: Session, skip: int = 0, limit: int = 10):
    return db.query(VehicleHasSourceOfTruths).offset(skip).limit(limit).all()

def create_vehicle_source_of_truth(db: Session, vehicle_id: int, path: str, data: str = None, summary: str = None):
    source_of_truth = VehicleHasSourceOfTruths(
        vehicle_id=vehicle_id,
        path=path,
        data=data,
        summary=summary
    )
    db.add(source_of_truth)
    db.commit()
    db.refresh(source_of_truth)
    return source_of_truth