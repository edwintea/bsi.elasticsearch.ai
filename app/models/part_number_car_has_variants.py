from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class PartNumberCarHasVariants(Base):
    __tablename__ = 'part_number_car_has_variants'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    part_number_car_id = Column(BigInteger, nullable=False, index=True)
    value = Column(String(191), nullable=False)
    meta = Column(Text, nullable=True)  # Using Text for longtext
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)
    part_number_car_alternate_id = Column(String(191), nullable=False)

    def __repr__(self):
        return (f"<PartNumberCarHasVariants(id={self.id}, "
                f"part_number_car_id={self.part_number_car_id}, value={self.value}, "
                f"part_number_car_alternate_id={self.part_number_car_alternate_id})>")