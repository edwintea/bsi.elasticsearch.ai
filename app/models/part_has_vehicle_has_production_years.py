from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class PartHasVehicleHasProductionYears(Base):
    __tablename__ = 'part_has_vehicle_has_production_years'

    my_row_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    part_has_vehicle_id = Column(BigInteger, nullable=False)
    value = Column(String(191), nullable=False)
    meta = Column(Text, nullable=True)  # Using Text for longtext
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<PartHasVehicleHasProductionYears(my_row_id={self.my_row_id}, part_has_vehicle_id={self.part_has_vehicle_id}, value={self.value})>"