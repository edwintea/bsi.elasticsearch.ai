from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class VehicleHasSourceOfTruths(Base):
    __tablename__ = 'vehicle_has_source_of_truths'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    vehicle_id = Column(BigInteger, nullable=False)
    path = Column(String(512), nullable=False)
    data = Column(Text, nullable=True)  # Using Text for longtext
    summary = Column(Text, nullable=True)  # Using Text for longtext
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return (f"<VehicleHasSourceOfTruths(id={self.id}, vehicle_id={self.vehicle_id}, "
                f"path={self.path})>")