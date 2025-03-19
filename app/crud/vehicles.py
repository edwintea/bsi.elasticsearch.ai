# crud/vehicles.py
from sqlalchemy.orm import Session
from ..models.vehicles import Vehicles


def get_vehicle(db: Session, id: int):
    """Retrieve a vehicle by ID."""
    return db.query(Vehicles).filter(Vehicles.id == id).first()


def get_vehicles(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of vehicles with pagination."""
    return db.query(Vehicles).offset(skip).limit(limit).all()


def create_vehicle(db: Session, title: str, slug: str, description: str = None, image: int = None, model: str = None,
                   status: int = 0, meta: str = None, published_at: str = None,
                   category_description: str = "Light Duty", emission: str = "EURO 2"):
    """Create a new vehicle record."""
    vehicle = Vehicles(
        title=title,
        slug=slug,
        description=description,
        image=image,
        model=model,
        status=status,
        meta=meta,
        published_at=published_at,
        category_description=category_description,
        emission=emission
    )
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)

    # Index the vehicle in Elasticsearch
    index_vehicle(vehicle.id, vehicle.__dict__)

    return vehicle


def update_vehicle(db: Session, id: int, **vehicle_data):
    """Update an existing vehicle record."""
    vehicle = get_vehicle(db, id)
    if vehicle:
        for key, value in vehicle_data.items():
            setattr(vehicle, key, value)
        db.commit()
        db.refresh(vehicle)

        # Update the vehicle in Elasticsearch
        index_vehicle(vehicle.id, vehicle.__dict__)

        return vehicle
    return None


def delete_vehicle(db: Session, id: int):
    """Delete a vehicle record."""
    vehicle = get_vehicle(db, id)
    if vehicle:
        db.delete(vehicle)
        db.commit()

        # Delete the vehicle from Elasticsearch
        delete_vehicle_from_elasticsearch(vehicle.id)

        return vehicle
    return None