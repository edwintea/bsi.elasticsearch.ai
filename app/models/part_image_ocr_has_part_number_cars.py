from sqlalchemy import Column, BigInteger, String, CHAR, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class PartImageOCRHasPartNumberCars(Base):
    __tablename__ = 'part_image_ocr_has_part_number_cars'

    my_row_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    id = Column(CHAR(36), nullable=False)
    part_image_ocr_id = Column(CHAR(36), nullable=True, index=True)
    code = Column(String(50), nullable=True, index=True)
    part_number = Column(String(100), nullable=True, index=True)
    vehicle_id = Column(BigInteger, nullable=True)
    part_id = Column(BigInteger, nullable=True, index=True)
    part_image_id = Column(BigInteger, nullable=True, index=True)
    part_number_car_id = Column(BigInteger, nullable=False, index=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return (f"<PartImageOCRHasPartNumberCars(my_row_id={self.my_row_id}, "
                f"id={self.id}, part_image_ocr_id={self.part_image_ocr_id}, "
                f"part_number={self.part_number}, vehicle_id={self.vehicle_id})>")