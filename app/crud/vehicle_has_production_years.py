# crud/vehicle_has_production_years.py
from sqlalchemy.orm import Session
from ..models.vehicle_has_production_years import VehicleHasProductionYears

def get_vehicle_production_year(db: Session, id: int):
    return db.query(VehicleHasProductionYears).filter(VehicleHasProductionYears.id == id).first()

def get_vehicle_production_years(db: Session, skip: int = 0, limit: int = 10):
    return db.query(VehicleHasProductionYears).offset(skip).limit(limit).all()

def create_vehicle_production_year(db: Session, vehicle_id: int, value: str, meta: str = None):
    production_year = VehicleHasProductionYears(
        vehicle_id=vehicle_id,
        value=value,
        meta=meta
    )
    db.add(production_year)
    db.commit()
    db.refresh(production_year)
    return production_year