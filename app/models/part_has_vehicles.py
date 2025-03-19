from sqlalchemy import Column, BigInteger, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class PartHasVehicles(Base):
    __tablename__ = 'part_has_vehicles'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    vehicle_id = Column(BigInteger, nullable=False)
    part_id = Column(BigInteger, nullable=False)
    meta = Column(Text, nullable=True)  # Using Text for longtext
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<PartHasVehicles(id={self.id}, vehicle_id={self.vehicle_id}, part_id={self.part_id})>"