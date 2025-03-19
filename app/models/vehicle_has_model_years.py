from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class VehicleHasModelYears(Base):
    __tablename__ = 'vehicle_has_model_years'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    vehicle_id = Column(BigInteger, nullable=False)
    value = Column(String(191), nullable=False)
    meta = Column(Text, nullable=True)  # Using Text for longtext
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return (f"<VehicleHasModelYears(id={self.id}, vehicle_id={self.vehicle_id}, "
                f"value={self.value})>")